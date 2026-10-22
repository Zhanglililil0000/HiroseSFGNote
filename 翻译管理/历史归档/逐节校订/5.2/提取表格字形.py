from pathlib import Path
import pdfplumber,json,collections,re
o=Path(__file__).resolve().parent;r=o.parents[2]
greek={'g':r'\gamma ','b':r'\beta ','f':r'\phi ','s':r'\sigma ','”':r'\equiv ','¥':r'\infty ','S':r'\Sigma ','F':r'\Phi ','P':r'\Pi ','D':r'\Delta ','G':r'\Gamma ','(cid:214)':'ROOT'}
def baseline(c):return round(842-c['matrix'][5],2)
def rows(page):
 chars=[dict(c,uid=i) for i,c in enumerate(page.chars) if c['top']<765]
 # PDF baseline coordinates, rather than glyph bounding boxes, keep Symbol and Roman aligned.
 vals=collections.Counter(baseline(c) for c in chars if c['size']>=9)
 clusters=[]
 for b in sorted(vals):
  if clusters and b-clusters[-1][-1]<=2:clusters[-1].append(b)
  else:clusters.append([b])
 bases=[max(v,key=lambda b:vals[b]) for v in clusters];grouped={b:[] for b in bases}
 mains=[c for c in chars if c['size']>=9 and c['text'].strip()]
 for c in chars:
  own=baseline(c)
  if c['size']<9 and c['x0']<98:
   parents=[m for m in mains if m['fontname']=='Symbol' and m['text'] in 'SDFPG' and -2<=c['x0']-m['x1']<22 and abs(baseline(m)-own)<8]
   if parents:own=baseline(min(parents,key=lambda m:abs(c['x0']-m['x1'])+0.15*abs(baseline(m)-own)))
  b=min(bases,key=lambda v:abs(v-own))
  assert abs(b-baseline(c))<=8,(page.page_number,c)
  grouped[b].append(c)
 return [(b,sorted(cs,key=lambda c:(c['x0'],c['top']))) for b,cs in grouped.items()]
def tex(cs,b):
 out=[];script=None;buf='';prev=None
 def flush():
  nonlocal script,buf
  if buf:out.append(('_' if script=='sub' else '^')+'{'+buf+'}')
  script=None;buf=''
 for c in cs:
  v=c['text'];v=greek.get(v,v) if c['fontname']=='Symbol' else v
  v=v.replace('–','-').replace('−','-').replace('•',r'\mathord{\bullet}').replace('°',r'{}^\circ ')
  if v=='ROOT':v='√'
  small=c['size']<9
  if small:
   kind='sup' if baseline(c)<b-1 else 'sub'
   if kind!=script:flush();script=kind
   buf+=v
  else:
   flush()
   if prev and c['x0']-prev['x1']>4:out.append(r'\quad ')
   out.append(v)
  prev=c
 flush();s=''.join(out).strip()
 s=re.sub(r'√\s*([23])',r'\\sqrt{\1}',s)
 s=re.sub(r'(?<![a-zA-Z\\])(cos|sin)(?![a-zA-Z])',r'\\\1 ',s)
 s=s.replace('all components',r'\text{全部分量}').replace('without internal rotation',r'\text{无内旋转}').replace('trans-dichloroethylene',r'\text{反式二氯乙烯}').replace('ethylene',r'\text{乙烯}').replace('trans-',r'\text{反式}-')
 s=s.replace('(Two HOO/HSS planes are perpendicular.)',r'\text{（两个HOO/HSS平面互相垂直。）}')
 s=s.replace('すべての',r'\text{全部}')
 s=s.replace('(without consideration of the above "distributed terms,)',r'\text{（不计上述“分配项”。原引号未闭合。）}')
 return s
data={};audit=[]
with pdfplumber.open(r/'日语原版/Chapter5/chap5-2.pdf') as doc:
 for pi,page in enumerate(doc.pages[1:],2):
  tables=page.find_tables();lines=rows(page);events=[];used=[]
  for ti,tab in enumerate(tables):
   bx=tab.bbox;related=[(b,cs) for b,cs in lines if bx[1]-2<=b-7<=bx[3]+2]
   # Assign only characters spatially within this table; all other characters remain prose/math below.
   related=[(b,[c for c in cs if bx[0]-1<=c['x0']<bx[2]+1 and bx[1]-2<=c['top']<bx[3]+1]) for b,cs in related]
   related=[(b,cs) for b,cs in related if cs]
   # Preserve original vertical partitions; a shared operation cell remains a shared operation column.
   edges=sorted({round(x,2) for cell in tab.cells for x in [cell[0],cell[2]]})
   grid=[]
   for b,cs in related:
    cells=[]
    for l,u in zip(edges,edges[1:]):
     sub=[c for c in cs if l-0.1<=c['x0']<u-0.1];used.extend(c['uid'] for c in sub);cells.append(tex(sub,b))
    grid.append({'y':b,'cells':cells,'字符数':sum(len(c['text']) for c in cs)})
   events.append({'kind':'table','y':bx[1],'bbox':bx,'rows':grid,'原表序':ti+1})
  usedset=set(used);assert len(usedset)==len(used),(pi,'duplicate chars')
  for b,cs in lines:
   left=[c for c in cs if c['uid'] not in usedset]
   if left:
    events.append({'kind':'line','y':b,'tex':tex(left,b),'字符数':sum(len(c['text']) for c in left)})
    usedset.update(c['uid'] for c in left)
  assert len(usedset)==sum(len(cs) for b,cs in lines),(pi,'lost chars')
  events.sort(key=lambda x:x['y']);data[str(pi)]=events
  audit.append({'页':pi,'表格':len(tables),'字形数':len(usedset),'无丢失':True,'无重复分配':True})
(o/'表格字形.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'提取覆盖审计.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
for p in ['2','14','21','22']:
 print('PAGE',p)
 for ev in data[p]:
  if ev['kind']=='table':
   print('TABLE',ev['原表序'], 'ROWS',len(ev['rows']))
   for row in ev['rows'][:4]:print(row['cells'])
  else:print(ev['tex'])

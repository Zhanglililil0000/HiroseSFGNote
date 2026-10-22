from pathlib import Path
import pdfplumber,re,json,collections
out=Path(__file__).resolve().parent;root=out.parents[2]
greek=dict(zip('abgdezhqiklmnxoprstufcyw','αβγδεζηθικλμνξοπρστυφχψω'))
greek.update({'D':'Δ','F':'Φ','Q':'Θ','W':'Ω','G':'Γ','P':'Π','S':'Σ','X':'Ξ','Y':'Ψ','Z':'Ζ','v':'ϖ','„':'≠','¥':'∞','·':'×'})
def glyph(c):
 t=c['text']
 if t=='(cid:214)':return '√'
 if t=='(cid:229)':return 'Σ'
 if 'Symbol' in c['fontname']:t=''.join(greek.get(x,x) for x in t)
 return t.replace('ß','β').replace('(cid:160)',' ').replace('\xa0',' ')
def tex(s):
 # Escape displayed grouping braces without manufacturing scalable pairs.
 scripts=[]
 s=re.sub(r'([_^])\{([^}]*)\}',lambda m: 'SCRIPTPLACE'+str(len(scripts))+'END' if not scripts.append(m[0]) else '',s)
 s=s.replace('{',r'\{').replace('}',r'\}')
 for i,v in enumerate(scripts):s=s.replace('SCRIPTPLACE'+str(i+1)+'END',v)
 for a,b in {'α':'alpha','β':'beta','γ':'gamma','δ':'delta','ε':'epsilon','ζ':'zeta','η':'eta','θ':'theta','κ':'kappa','λ':'lambda','μ':'mu','ν':'nu','ξ':'xi','π':'pi','ϖ':'varpi','ρ':'rho','σ':'sigma','τ':'tau','υ':'upsilon','φ':'phi','χ':'chi','ψ':'psi','ω':'omega','Δ':'Delta','Φ':'Phi','Θ':'Theta','Ω':'Omega','Γ':'Gamma','Π':'Pi','Σ':'Sigma','Ξ':'Xi','Ψ':'Psi','≠':'ne','∞':'infty','×':'times','±':'pm','√':'sqrt'}.items():s=s.replace(a,'\\'+b+' ')
 s=re.sub(r'(?<![A-Za-z\\])(sin|cos)(?![A-Za-z])',r'\\\1 ',s)
 # Functions are often adjacent to Greek command after mapping.
 s=re.sub(r'(?<![A-Za-z\\])(sin|cos)(?=\\)',r'\\\1 ',s)
 s=s.replace('>>',r'\gg ').replace('~',r'\sim ')
 return re.sub(r' +',' ',s).strip()
def convert(chars,base):
 chars=sorted(chars,key=lambda c:c['x0']);pieces=[];mode=None;buf='';prev=None
 def flush():
  nonlocal buf
  if buf:pieces.append((mode,buf));buf=''
 for c in chars:
  v=glyph(c)
  if not v.strip():
   if mode=='base':buf+=' '
   continue
  m='base'
  if c['size']<8.1 and c['matrix'][5]<base-0.8:m='sub'
  elif c['size']<8.1 and c['matrix'][5]>base+0.8:m='sup'
  if m!=mode:flush();mode=m
  if prev and c['x0']-prev['x1']>2.8 and m=='base':buf+=' '
  buf+=v;prev=c
 flush();result=''
 for m,v in pieces:
  if m=='base':result+=v
  else:result+=('_' if m=='sub' else '^')+'{'+v+'}'
 return result.strip()
doc=pdfplumber.open(root/'日语原版/Chapter4/chap4-5.pdf');allpages=[];symbols=collections.Counter()
for n,p in enumerate(doc.pages,1):
 chars=[c for c in p.chars if 65<c['matrix'][5]<790 and c['text']!='(cid:160)']
 # Every normal-sized glyph has an explicit text baseline; scripts attach to the closest line.
 bases=sorted(set(round(c['matrix'][5],1) for c in chars if c['size']>=8.1 and glyph(c).strip()),reverse=True)
 lines={b:[] for b in bases}
 for c in chars:
  b=min(bases,key=lambda y:abs(y-c['matrix'][5]));lines[b].append(c)
  if 'Symbol' in c['fontname']:symbols[c['text']]+=1
 rows=[]
 for j,(b,cs) in enumerate(lines.items()):
  raw=convert(cs,b)
  if not raw:continue
  jp=bool(re.search(r'[\u3040-\u30ff\u4e00-\u9fff]',raw))
  # Japanese punctuation alone isn't a Japanese prose line.
  rows.append({'id':f'p{n:02d}l{j+1:02d}','baseline':b,'raw':raw,'tex':tex(raw) if not jp else None,'jp':jp})
 allpages.append({'page':n,'lines':rows})
(out/'逐行提取.json').write_text(json.dumps(allpages,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'叙述清单.txt').write_text('\n'.join(f"{x['id']} {x['raw']}" for p in allpages for x in p['lines'] if x['jp'] and p['page']>=3),encoding='utf-8')
(out/'数学提取预览.txt').write_text('\n'.join(f"{x['id']} {x['tex'] or x['raw']}" for p in allpages for x in p['lines'] if p['page']>=3),encoding='utf-8')
print('Symbol',symbols);print('lines',sum(len(p['lines']) for p in allpages))

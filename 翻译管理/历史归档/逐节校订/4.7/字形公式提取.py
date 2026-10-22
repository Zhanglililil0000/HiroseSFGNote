from pathlib import Path
import json,re,collections,pdfplumber
out=Path(__file__).resolve().parent;root=out.parents[2]
greek={'b':r'\beta ','c':r'\chi ','q':r'\theta ','f':r'\phi ','t':r'\tau ','g':r'\gamma ','w':r'\omega ','p':r'\pi ','a':r'\alpha ','m':r'\mu ','n':r'\nu ','D':r'\Delta ','±':r'\pm ','√':r'\sqrt '}
greek.update({'x':r'\xi ','z':r'\zeta ','h':r'\eta ','v':r'\varpi ','·':r'\cdot '})
def lines(page):
 chars=[c for c in page.chars if c['top']<765]
 bases=collections.Counter(round(c['top']+(.8 if c['fontname'].startswith('Heisei') else 0),1) for c in chars if c['fontname']!='Symbol' and abs(c['size']-10)<.2)
 bases=sorted(y for y,n in bases.items() if n>=1)
 # 根号在底本中常由四段矢量线绘制，文本层没有根号字符。
 for bar in page.lines:
  if abs(bar['height'])>.1 or bar['width']<5:continue
  diagonals=[l for l in page.lines if l['height']>5 and abs(l['x1']-bar['x0'])<2 and abs(l['top']-bar['top'])<2]
  if not diagonals:continue
  near=min(bases,key=lambda a:abs(a-(bar['top']+1.7)))
  if abs(near-bar['top'])>8:continue
  for x,v in [(bar['x0']-5,r'\sqrt{'),(bar['x1']+.01,'}')]:chars.append({'text':v,'x0':x,'top':near,'size':10,'fontname':'RawTeX'})
 grouped={y:[] for y in bases}
 for c in chars:
  y=c['top']+(2.2 if c['fontname']=='Symbol' and c['size']>8 else .8 if c['fontname'].startswith('Heisei') else 0)
  near=min(bases,key=lambda a:abs(a-y))
  if abs(near-y)<6.5:grouped[near].append(c)
 result=[]
 for y,cs in grouped.items():
  cs=sorted(cs,key=lambda c:c['x0']);parts=[];script='';buf=''
  def flush():
   nonlocal buf,script
   if buf:parts.append(('_' if script=='sub' else '^')+'{'+buf+'}');buf='';script=''
  for c in cs:
   v=c['text'];small=c['size']<8
   if small:
    if c['fontname']=='Symbol':v=greek.get(v,v)
    typ='sub' if c['top']>y+2 else 'sup'
    if script and typ!=script:flush()
    script=typ;buf+=v
   else:
    flush()
    if c['fontname']=='Symbol':v=greek.get(v,v)
    elif c['fontname']!='RawTeX':v=v.replace('{',r'\{').replace('}',r'\}')
    parts.append(v)
  flush();s=''.join(parts)
  s=re.sub(r'(?<![a-zA-Z\\])(sin|cos)',lambda m:'\\'+m[1]+' ',s)
  s=re.sub(r'\\(beta|chi) _\{',r'\\\1_{',s)
  result.append({'y':y,'tex':s.strip()})
 return result
if __name__=='__main__':
 d=pdfplumber.open(root/'日语原版/Chapter4/chap4-7.pdf')
 data={str(p+1):lines(d.pages[p]) for p in range(15,24)}
 (out/'附录字形提取.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 for p,ls in data.items():
  print('PAGE',p)
  for l in ls:print(l['y'],l['tex'])

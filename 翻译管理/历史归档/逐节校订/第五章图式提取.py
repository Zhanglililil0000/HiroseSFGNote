from pathlib import Path
import re,json,hashlib
import pdfplumber,pypdfium2 as pdfium
from PIL import Image
r=Path(__file__).resolve().parents[2];out=r/'翻译管理/校订记录/第五章收尾';assets=r/'中文版本/assets/ch05';assets.mkdir(parents=True,exist_ok=True)
manifest=[]
def crop(doc,p,box,name):
 scale=3.5
 im=doc[p].render(scale=scale).to_pil().convert('RGB')
 x0,y0,x1,y1=box
 im=im.crop((int(x0*scale),int(y0*scale),int(x1*scale+1),int(y1*scale+1)))
 im.save(assets/name)
 return im
src=r/'日语原版/Chapter5/chap5-3.pdf';doc=pdfium.PdfDocument(str(src));forms=[]
with pdfplumber.open(src) as pp:
 for pn in range(1,len(pp.pages)):
  p=pp.pages[pn]; words=p.extract_words(extra_attrs=['size']); starts=[]
  for w in words:
   if re.fullmatch('[XYZ]{3}',w['text']) and w['x0']<160 and w['size']<8:
    starts.append((w['top']-9,w['text']))
  heads=[l['top'] for l in p.extract_text_lines() if '軸に沿った' in l['text']]
  footer=min([l['top'] for l in p.extract_text_lines() if '分子から空間' in l['text']],default=p.height-45)
  boundaries=[x[0] for x in starts]+[footer]
  if forms and starts:
   # The previous formula continues before the first new left-hand side.
   end=min([starts[0][0]]+[h for h in heads if h<starts[0][0]])-2
   chars=[c for c in p.chars if c['top']<end and c['bottom']>60]
   if chars:
    box=(65,min(c['top'] for c in chars)-3,p.width,max(c['bottom'] for c in chars)+3)
    forms[-1]['片段'].append({'页':pn+1,'框':box})
  for k,(top,label) in enumerate(starts):
   end=boundaries[k+1]-2
   hs=[h for h in heads if top<h<end]
   if hs:end=min(hs)-3
   chars=[c for c in p.chars if c['top']>=top-1 and c['bottom']<end+1]
   assert chars,(pn,label)
   box=(65,min(c['top'] for c in chars)-3,p.width,max(c['bottom'] for c in chars)+3)
   forms.append({'分量':label,'片段':[{'页':pn+1,'框':box}]})
 for i,f in enumerate(forms):
  ims=[crop(doc,z['页']-1,z['框'],f'ch05-s03-tmp-{i+1:03d}-{j}.png') for j,z in enumerate(f['片段'])]
  canvas=Image.new('RGB',(max(im.width for im in ims),sum(im.height for im in ims)+12*(len(ims)-1)),'white'); y=0
  for im in ims:canvas.paste(im,(0,y));y+=im.height+12
  name=f'ch05-s03-formula-{i+1:03d}.png';canvas.save(assets/name)
  for j in range(len(ims)):(assets/f'ch05-s03-tmp-{i+1:03d}-{j}.png').unlink()
  f.update({'节':'5.3','序号':i+1,'轴':('c' if i<27 else 'a' if i<54 else 'b'),'资源':name,'类型':'完整分量式图','来源摘要':hashlib.sha256(src.read_bytes()).hexdigest()})
  manifest.append(f)
 print('5.3 formulas',len(forms),[f['分量'] for f in forms])
for sec in ['5.4','5.5','5.6']:
 src=r/f'日语原版/Chapter5/chap{sec.replace(".","-")}.pdf';doc=pdfium.PdfDocument(str(src))
 with pdfplumber.open(src) as pp:
  for pn,p in enumerate(pp.pages):
   for tn,t in enumerate(p.find_tables()):
    name=f'ch05-s{sec[-1]:0>2}-p{pn+1:02d}-table{tn+1:02d}.png';b=t.bbox;box=(max(0,b[0]-3),max(0,b[1]-3),min(p.width,b[2]+3),min(p.height,b[3]+3))
    crop(doc,pn,box,name)
    manifest.append({'节':sec,'页':pn+1,'表':tn+1,'框':box,'行数含表头':len(t.rows),'列数含行标':len(t.rows[0].cells),'资源':name,'类型':'原表保真图','来源摘要':hashlib.sha256(src.read_bytes()).hexdigest()})
(out/'公式图表资源.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('table resources', {s:len([x for x in manifest if x['节']==s]) for s in ['5.3','5.4','5.5','5.6']})

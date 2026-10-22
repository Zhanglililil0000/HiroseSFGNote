from pathlib import Path
import re,json,hashlib
import pdfplumber,pypdfium2 as pdfium
from PIL import Image,ImageOps,ImageDraw
r=Path(__file__).resolve().parents[2]; out=r/'翻译管理/校订记录/第五章收尾';out.mkdir(exist_ok=True)
alljp=[];meta=[]
for sec in ['5.3','5.4','5.5','5.6']:
 src=r/f'日语原版/Chapter5/chap{sec.replace(".","-")}.pdf'
 doc=pdfium.PdfDocument(str(src));pages=[]
 with pdfplumber.open(src) as pp:
  for j,p in enumerate(pp.pages):
   lines=(p.extract_text(x_tolerance=2,y_tolerance=3) or '').splitlines()
   jp=[x for x in lines if re.search('[ぁ-んァ-ヶ一-龯]',x)]
   alljp.append(f'\n===== {sec} p{j+1} =====\n'+'\n'.join(jp))
   pages.append({'页':j+1,'宽':p.width,'高':p.height,'日语行':jp})
 for start in range(0,len(doc),2):
  thumbs=[]
  for j in range(start,min(start+2,len(doc))):
   im=doc[j].render(scale=1.55).to_pil().convert('RGB'); im=ImageOps.expand(im,border=(8,28,8,8),fill='white'); ImageDraw.Draw(im).text((15,4),f'{sec} PDF p{j+1}',fill='black');thumbs.append(im)
  sheet=Image.new('RGB',(sum(x.width for x in thumbs),max(x.height for x in thumbs)),'#dddddd');x=0
  for im in thumbs:sheet.paste(im,(x,0));x+=im.width
  sheet.save(out/f'{sec}-p{start+1:02d}-{min(start+2,len(doc)):02d}.png')
 meta.append({'节':sec,'页数':len(doc),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'页面':pages})
(out/'日语文字逐页清单.txt').write_text('\n'.join(alljp),encoding='utf-8')
(out/'底本及页面.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
print('\n'.join(f"{x['节']}: {x['页数']}页" for x in meta))

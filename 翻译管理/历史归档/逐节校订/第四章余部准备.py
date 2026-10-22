from pathlib import Path
import pypdfium2 as pdf,pdfplumber,json,sys
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(Path(__file__).parent/'4.7'))
from 字形公式提取 import lines
for sec in ['4.8','4.9','4.10','4.11']:
 out=root/'翻译管理/校订记录'/sec;out.mkdir(exist_ok=True)
 source=root/f'日语原版/Chapter4/chap4-{sec.split(".")[1]}.pdf'
 d=pdf.PdfDocument(str(source));pl=pdfplumber.open(source)
 data={str(i+1):lines(p) for i,p in enumerate(pl.pages)}
 (out/'字形行.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 for i in range(len(d)):
  dest=out/f'原文p{i+1}.png'
  if not dest.exists():d[i].render(scale=2).to_pil().save(dest)
 for start in range(0,len(d),4):
  sheet=Image.new('RGB',(1600,2320),'#ddd');draw=ImageDraw.Draw(sheet)
  for j in range(4):
   if start+j>=len(d):break
   im=Image.open(out/f'原文p{start+j+1}.png');im.thumbnail((790,1120));x=(j%2)*800;y=(j//2)*1160;sheet.paste(im,(x,y+25));draw.text((x+10,y+5),f'{sec} PDF p{start+j+1}',fill='black')
  sheet.save(out/f'原文总览{start+1}-{min(start+4,len(d))}.png')
 print(sec,len(d),'pages rendered')

from pathlib import Path
import csv,subprocess
import pypdfium2 as pdfium
from PIL import Image, ImageOps, ImageDraw
root=Path('HiroseSFGNote').resolve(); out=root/'翻译管理'/'全书调查'/'页面抽查'; out.mkdir(parents=True,exist_ok=True)
rows=list(csv.DictReader((root/'翻译管理'/'章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
exe=r'C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'
for start in range(0,len(rows),4):
 batch=rows[start:start+4]; sheet=Image.new('RGB',(1800,1320),'#cccccc'); draw=ImageDraw.Draw(sheet)
 for j,r in enumerate(batch):
  for k,p in enumerate([1,int(r['PDF页数'])]):
   prefix=out/f'{r["编号"]}-p{p}'
   doc=pdfium.PdfDocument(str(root/r['原文路径'])); page=doc[p-1]; bitmap=page.render(scale=1.5); img=bitmap.to_pil().convert('RGB'); img.save(str(prefix)+'.png'); page.close(); doc.close(); img.thumbnail((440,610))
   x=j*450; y=k*650+30; sheet.paste(img,(x,y)); draw.text((x+8,k*650+8),f'{r["编号"]} PDF p.{p}',fill='black')
 sheet.save(out/f'contact-{start//4+1:02}.jpg',quality=90)
 print('contact',start//4+1,flush=True)

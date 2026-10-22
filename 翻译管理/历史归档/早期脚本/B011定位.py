from pathlib import Path
import pypdfium2 as p
r=Path('HiroseSFGNote');o=r/'翻译管理/校订记录/1.1';d=p.PdfDocument(str(r/'日语原版/Chapter1/chap1-1Japanese.pdf'))
for n in [8,9]:
 im=d[n-1].render(scale=1.6).to_pil();im.save(o/f'B011-原文p{n}.png')
im=d[6].render(scale=3).to_pil();im.crop((0,int(im.height*.43),im.width,im.height)).save(o/'B011-式13首组原文.png')

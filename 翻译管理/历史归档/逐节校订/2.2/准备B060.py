from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
d=pdfium.PdfDocument(str(root/'日语原版/Chapter2/chap2-2.pdf'))
d[2].render(scale=1.8).to_pil().save(out/'原文p3.png')
for page,box in [(2,(.10,.67,.92,.90)),(3,(.11,.10,.92,.51))]:
    im=d[page-1].render(scale=3).to_pil();w,h=im.size
    im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(out/f'公式核对p{page}.png')
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
backup=out/'B060-修订前.md'
if not backup.exists():backup.write_bytes(p.read_bytes())

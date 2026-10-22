from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
d=pdfium.PdfDocument(str(root/'日语原版/Chapter2/chap2-1.pdf'))
for page,box in [(5,(.15,.80,.88,.92)),(6,(.10,.06,.90,.17)),(7,(.11,.10,.92,.71))]:
    im=d[page-1].render(scale=3).to_pil();w,h=im.size
    im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(out/f'公式局部p{page}.png')

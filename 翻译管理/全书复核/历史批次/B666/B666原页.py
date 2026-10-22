from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image,ImageOps,ImageDraw
R=Path(__file__).resolve().parents[2]; O=R/'翻译管理/全书复核/B666原页';O.mkdir(exist_ok=True)
spec=[('1.3','日语原版/Chapter1/chap1-3Japanese.pdf',[1,5]),('7.1','日语原版/Chapter7/chap7-1.pdf',[2,3,4]),('8.1','日语原版/Chapter8/chap8-1.pdf',[3])]
for section,rel,pages in spec:
 doc=pdfium.PdfDocument(str(R/rel))
 for n in pages:
  im=doc[n-1].render(scale=1.8).to_pil().convert('RGB');im.save(O/f'{section}-p{n}.png')
print(str(O))

from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
d=pdfium.PdfDocument(str(root/'日语原版/Chapter2/chap2-2.pdf'))
for n in [4,5]:d[n-1].render(scale=1.8).to_pil().save(out/f'原文p{n}.png')
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
if not (out/'B063-修订前.md').exists():(out/'B063-修订前.md').write_bytes(p.read_bytes())

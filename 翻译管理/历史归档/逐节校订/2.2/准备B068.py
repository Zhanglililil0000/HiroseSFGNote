from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
d=pdfium.PdfDocument(str(root/'日语原版/Chapter2/chap2-2.pdf'))
im=d[5].render(scale=3.5).to_pil();w,h=im.size
im.crop((int(.10*w),int(.68*h),int(.91*w),int(.91*h))).save(out/'B068-原式局部.png')
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
if not (out/'B068-修订前.md').exists():(out/'B068-修订前.md').write_bytes(p.read_bytes())

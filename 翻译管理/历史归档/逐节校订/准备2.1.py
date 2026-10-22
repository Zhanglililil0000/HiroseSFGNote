from pathlib import Path
import pypdfium2 as pdfium
import hashlib
root=Path(__file__).resolve().parents[2]
out=root/'翻译管理/校订记录/2.1'
out.mkdir(exist_ok=True)
source=root/'日语原版/Chapter2/chap2-1.pdf'
md=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.1 *.md'))
backup=out/'B050-修订前.md'
if not backup.exists(): backup.write_bytes(md.read_bytes())
doc=pdfium.PdfDocument(str(source))
for n in range(len(doc)):
    doc[n].render(scale=1.6).to_pil().save(out/f'原文p{n+1}.png')
print('pages',len(doc),'sha256',hashlib.sha256(source.read_bytes()).hexdigest())

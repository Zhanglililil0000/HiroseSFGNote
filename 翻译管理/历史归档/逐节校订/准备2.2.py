from pathlib import Path
import pypdfium2 as pdfium
import hashlib,re
root=Path(__file__).resolve().parents[2]
out=root/'翻译管理/校订记录/2.2';out.mkdir(exist_ok=True)
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
backup=out/'B058-修订前.md'
if not backup.exists():backup.write_bytes(p.read_bytes())
src=root/'日语原版/Chapter2/chap2-2.pdf'
d=pdfium.PdfDocument(str(src))
for n in [1,2]:d[n-1].render(scale=1.7).to_pil().save(out/f'原文p{n}.png')
print('pages',len(d),'sha256',hashlib.sha256(src.read_bytes()).hexdigest())
print('\n'.join(x for x in p.read_text(encoding='utf-8').splitlines() if re.match(r'^#{1,4} ',x)))

from pathlib import Path
import pypdfium2 as pdfium

root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
doc=pdfium.PdfDocument(str(root/'日语原版/Chapter1/chap1-1Japanese.pdf'))
for page in [3,4]:
    doc[page-1].render(scale=2).to_pil().save(out/f'Q012-p{page}.png')
p=next((root/'中文版本/第一章 SFG快速入门').glob('1.1 *.md'))
print('\n'.join(p.read_text(encoding='utf-8').splitlines()[85:145]))

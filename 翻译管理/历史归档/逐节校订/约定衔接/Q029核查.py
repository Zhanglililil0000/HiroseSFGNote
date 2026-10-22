from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
d=pdfium.PdfDocument(str(root/'日语原版/Chapter1/chap1-4Japanese.pdf'))
for n in [5,6,7,8,9]:
    d[n-1].render(scale=1.5).to_pil().save(out/f'Q029-p{n}.png')
p=next((root/'中文版本/第一章 SFG快速入门').glob('1.4 *.md'))
lines=p.read_text(encoding='utf-8').splitlines()
print('\n'.join(lines[224:279]))

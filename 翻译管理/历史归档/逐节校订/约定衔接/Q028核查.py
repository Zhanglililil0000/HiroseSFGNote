from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
d=pdfium.PdfDocument(str(root/'日语原版/Chapter1/chap1-3Japanese.pdf'))
for n in [1,2,3]:
    d[n-1].render(scale=1.7).to_pil().save(out/f'Q028-p{n}.png')
p=next((root/'中文版本/第一章 SFG快速入门').glob('1.3 *.md'))
print('\n'.join(p.read_text(encoding='utf-8').splitlines()[260:315]))

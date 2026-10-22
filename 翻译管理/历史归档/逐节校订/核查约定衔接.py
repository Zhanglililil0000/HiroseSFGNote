from pathlib import Path
import pypdfium2 as pdfium

r = Path(__file__).resolve().parents[1]
out = r / '校订记录/约定衔接'
out.mkdir(exist_ok=True)
root = r.parent
for sec, page in [('1.1', 8), ('1.2', 10)]:
    pdf = pdfium.PdfDocument(str(root / f'日语原版/Chapter1/chap{sec.replace(".", "-")}Japanese.pdf'))
    pdf[page-1].render(scale=2).to_pil().save(out / f'{sec}-p{page}.png')
for name, a, b in [('1.1', 296, 310), ('1.2', 588, 636)]:
    p = next((root / '中文版本/第一章 SFG快速入门').glob(name + ' *.md'))
    lines = p.read_text(encoding='utf-8').splitlines()
    print('\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1, b)))
print((r / '校订记录/1.2/B034.md').read_text(encoding='utf-8'))

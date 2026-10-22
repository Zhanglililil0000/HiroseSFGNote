from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
for name,pages in [('chap1-1Japanese.pdf',[1,2,12,13]),('chap1-3Japanese.pdf',[4,5])]:
    d=pdfium.PdfDocument(str(root/'日语原版/Chapter1'/name))
    for n in pages:
        d[n-1].render(scale=1.5).to_pil().save(out/f'Q010-{name[:-4]}-p{n}.png')
for prefix in ['1.1','1.3']:
    p=next((root/'中文版本/第一章 SFG快速入门').glob(prefix+' *.md'))
    for i,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        if any(k in line for k in ['分子数','单位体积','单位面积','厚度','极化层','量纲']):
            print(f'{prefix}:{i} {line}')

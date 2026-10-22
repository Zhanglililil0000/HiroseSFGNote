from pathlib import Path
import pypdfium2 as pdfium
r=Path(__file__).resolve().parents[1];o=r/'翻译管理/校订记录/6.1';o.mkdir(parents=True,exist_ok=True)
d=pdfium.PdfDocument(str(r/'日语原版/Chapter6/chap6-1.pdf'))
for n in range(3):d[n].render(scale=2.3).to_pil().save(o/f'原文p{n+1}.png')
print('底本',len(d),'页；首页三页已渲染。')

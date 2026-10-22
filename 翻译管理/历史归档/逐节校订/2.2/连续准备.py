from pathlib import Path
import pypdfium2 as pdfium,re,json
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
if not (out/'B069-持续执行前.md').exists():(out/'B069-持续执行前.md').write_bytes(p.read_bytes())
d=pdfium.PdfDocument(str(root/'日语原版/Chapter2/chap2-2.pdf'))
for n in range(7,48):
    f=out/f'原文p{n}.png'
    if not f.exists():d[n-1].render(scale=1.5).to_pil().save(f)
cache=(root/'翻译管理/全书调查/文本缓存/2.2.txt').read_text(encoding='utf-8')
pages=re.split(r'===== PDF p\.\d+ =====',cache)[1:]
prose={}
for n,t in enumerate(pages,1):
    prose[n]='\n'.join(line for line in t.splitlines() if re.search('[ぁ-ゖァ-ヶ]',line) or re.match(r'^(?:[45]\.\d|付録)',line))
(out/'日语叙述定位.json').write_text(json.dumps(prose,ensure_ascii=False,indent=2),encoding='utf-8')
for n in range(7,12):print(f'=== p{n} ===\n'+prose[n])

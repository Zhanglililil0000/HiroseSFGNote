from pathlib import Path
import re,json
import pdfplumber
out=Path(__file__).resolve().parent;root=out.parents[2]
body=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md')).read_text(encoding='utf-8')
manifest=json.loads((out/'公式图索引.json').read_text(encoding='utf-8'))
rows=[];missing=[]
with pdfplumber.open(root/'日语原版/Chapter2/chap2-2.pdf') as doc:
    for p,page in enumerate(doc.pages,1):
        for w in page.extract_words():
            m=re.fullmatch(r'\(([245ABC]\.\d+[abc]?)\)',w['text'])
            if not m or w['x0']/page.width<.80:continue
            label=m[1];a=w['top']/page.height;b=w['bottom']/page.height
            imgs=[x['file'] for x in manifest if x['page']==p and x['actual_y'][0]<=a and x['actual_y'][1]>=b]
            tex=bool(re.search(r'\\tag\{'+re.escape(label)+r'\}',body))
            orphan=label=='4.24' and p==9
            status='数学转写' if tex else ('原式图' if imgs else ('跨页编号：公式在p8，图注保留4.24' if orphan else '未定位'))
            if status=='未定位':missing.append({'page':p,'label':label,'y':[a,b]})
            rows.append({'page':p,'equation':label,'representation':status,'images':imgs})
(out/'全节公式编号索引.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'全节公式编号索引.md').write_text('# 2.2公式编号覆盖索引\n\n以底本右侧独立编号定位；不把正文中的引用重复计数。无编号推导另见各批记录与公式图索引。覆盖不等于代数正确性认证。\n\n| PDF页 | 原编号 | 表示方式 | 对应图片 |\n|---|---|---|---|\n'+''.join(f"| {r['page']} | {r['equation']} | {r['representation']} | {', '.join(r['images'])} |\n" for r in rows),encoding='utf-8')
print(json.dumps({'count':len(rows),'unique':len({r['equation'] for r in rows}),'missing':missing},ensure_ascii=False))
assert not missing,missing

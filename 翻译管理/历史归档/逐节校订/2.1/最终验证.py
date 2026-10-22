from pathlib import Path
import re,csv,io,json,hashlib
from urllib.parse import unquote
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
md=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.1 *.md'))
s=md.read_text(encoding='utf-8')
baseline=(out/'B050-修订前.md').read_text(encoding='utf-8')
tags=lambda t:re.findall(r'\\tag\{([^}]+)\}',t)
assert sorted(tags(s))==sorted(tags(baseline))
assert len(tags(s))==40
parts=[(out/f'B{i:03}-本批译文.md').read_text(encoding='utf-8') for i in range(50,58)]
assert ''.join(parts)==s
links=[]
for p in [md,root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md',root/'中文版本/附件/原文勘误表.md']:
    t=p.read_text(encoding='utf-8')
    for m in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',t):
        href=unquote(m.group(1))
        if '://' in href or href.startswith('#'):continue
        target=p.parent/href.split('#')[0]
        assert target.exists(),str(target)
        links.append(str(target))
rows=list(csv.reader(io.StringIO((root/'翻译管理/术语表.tsv').read_text(encoding='utf-8-sig')),delimiter='\t'))
assert len(rows)-1==87 and all(len(r)==12 for r in rows)
src=root/'日语原版/Chapter2/chap2-1.pdf'
base=root/'翻译管理/基线快照/2026-10-16/日语原版/Chapter2/chap2-1.pdf'
assert src.read_bytes()==base.read_bytes()
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert len(render['results'])==8
assert all(r['width']==r['scrollWidth'] and not r['overs'] and all(i['loaded'] for i in r['images']) for r in render['results'])
report={'date':'2026-10-19','pages':11,'batches':8,'numberedEquations':40,'mathFragments':render['math'],'termEntries':87,'checkedLinks':len(links),'sourceHash':hashlib.sha256(src.read_bytes()).hexdigest(),'sourceMatchesBaseline':True,'batchTextsMatchFinal':True,'allBatchesNoHorizontalOverflow':True,'scope':'页面对照与排版整理；未独立认证原式物理正确性'}
(out/'最终验证.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

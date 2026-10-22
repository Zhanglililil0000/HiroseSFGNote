from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B089-修订前.md').read_text(encoding='utf-8')
new=(out/'B089-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
a=old.index('![式（4.28b）：');b=old.index('> **译校注（Q046，',a)
assert new in body
norm=lambda s:re.sub(r'^> \*\*译校状态.*$','STATUS',s,flags=re.M)
assert norm(body.replace(new,old[a:b],1))==norm(old)
assert re.findall(r'\\tag\{([^}]+)\}',new)==['4.28b'] and new.count('$$')==4
assert "t_{mm''," in new and "t_{m'm," in new and "h_{m'}" in new
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));r=next(x for x in render['results'] if x['batch']=='B089')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'));assert len(idx)==116
assert next(x for x in idx if x['equation']=='4.28b')['representation']=='数学转写'
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B089','date':'2026-10-19','page':10,'numbered_equation':'4.28b','unnumbered_formulas_added':1,'body_image_blocks_replaced':2,'scope_check':'仅本分支与状态行改变，Q046及其他正文相同','math_syntax_pass':render['math'],'render_overflow':False,'visual_review':'参考渲染与两幅高清原式对照通过','issue_status':'Q046保留；无新增','adopted_source_corrections':0,'next':'B090，式4.29'}
(out/'B089验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

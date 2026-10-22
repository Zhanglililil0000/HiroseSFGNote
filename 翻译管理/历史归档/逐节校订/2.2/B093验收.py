from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B093-修订前.md').read_text(encoding='utf-8')
new=(out/'B093-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
a=old.index('![式（5.1a）—（5.2c）');b=old.index('介质2与薄膜 $m$ 之间',a)
assert new in body
norm=lambda s:re.sub(r'^> \*\*译校状态.*$','STATUS',s,flags=re.M)
assert norm(body.replace(new,old[a:b],1))==norm(old)
labels=['5.1a','5.1b','5.1c','5.2a','5.2b','5.2c']
assert re.findall(r'\\tag\{([^}]+)\}',new)==labels and new.count('$$')==12
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));r=next(x for x in render['results'] if x['batch']=='B093')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'));assert len(idx)==116
assert all(next(x for x in idx if x['equation']==label)['representation']=='数学转写' for label in labels)
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B093','date':'2026-10-19','page':12,'equations':labels,'body_image_blocks_replaced':1,'scope_check':'仅六式及状态行改变，其他正文相同','math_syntax_pass':render['math'],'render_overflow':False,'visual_review':'参考渲染与高清原图及z分量局部对照通过','new_issues':0,'adopted_source_corrections':0,'next':'B094，5.3a—5.4c'}
(out/'B093验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

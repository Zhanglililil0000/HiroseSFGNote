from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B087-修订前.md').read_text(encoding='utf-8')
new=(out/'B087-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
a=old.index('![式（4.27）：');b=old.index('> **译校注（Q045，',a)
assert new in body
norm=lambda s:re.sub(r'^> \*\*译校状态.*$','STATUS',s,flags=re.M)
assert norm(body.replace(new,old[a:b],1))==norm(old)
assert re.findall(r'\\tag\{([^}]+)\}',new)==['4.27'] and new.count('$$')==2
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));r=next(x for x in render['results'] if x['batch']=='B087')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'));assert len(idx)==116
assert next(x for x in idx if x['equation']=='4.27')['representation']=='数学转写'
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B087','date':'2026-10-19','page':10,'equation':'4.27','body_image_blocks_replaced':1,'scope_check':'仅公式与状态行改变，原引用及Q045不变','math_syntax_pass':render['math'],'render_overflow':False,'visual_review':'参考渲染、高清原式及六倍指数局部对照通过','new_issues':0,'adopted_source_corrections':0,'next':'B088，式4.28a'}
(out/'B087验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

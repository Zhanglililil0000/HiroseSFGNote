from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B085-修订前.md').read_text(encoding='utf-8')
new=(out/'B085-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
a=old.index('![式（4.26a）');b=old.index('如果表面已经形成完整薄膜',a)
assert new in body
normalize=lambda s:re.sub(r'^> \*\*译校状态.*$','STATUS',s,flags=re.M)
assert normalize(body.replace(new,old[a:b],1))==normalize(old)
assert re.findall(r'\\tag\{([^}]+)\}',new)==['4.26a']
assert new.count(r'\Bigr\}')==2 and new.count('$$')==2
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));r=next(x for x in render['results'] if x['batch']=='B085')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'));assert len(idx)==116
assert next(x for x in idx if x['equation']=='4.26a')['representation']=='数学转写'
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B085','date':'2026-10-19','page':9,'equation':'4.26a','editable_equations_added':1,'body_image_blocks_replaced':1,'scope_check':'仅本公式及状态行改变，其他正文相同','math_syntax_pass':render['math'],'render_overflow':False,'visual_review':'参考渲染与高清原式对照通过','new_issue':'Q061；两处原括号保留','adopted_source_corrections':0,'next':'B086，完整表面膜无编号乘积与4.26b'}
(out/'B085验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

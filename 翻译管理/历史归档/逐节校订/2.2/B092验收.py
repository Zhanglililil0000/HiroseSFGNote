from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B092-修订前.md').read_text(encoding='utf-8')
new=(out/'B092-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
a=old.index('![式（4.30b）：');b=old.index('## 5. L系数与SFG电场',a)
assert new in body
norm=lambda s:re.sub(r'^> \*\*译校状态.*$','STATUS',s,flags=re.M)
assert norm(body.replace(new,old[a:b],1))==norm(old)
assert re.findall(r'\\tag\{([^}]+)\}',new)==['4.30b'] and new.count('$$')==2
assert r'\exp\!\left[-2ih_m' not in new
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));r=next(x for x in render['results'] if x['batch']=='B092')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'));assert len(idx)==116
sec4=[x for x in idx if x['equation'].startswith('4.')]
assert len(sec4)==33 and all(x['representation']=='数学转写' for x in sec4)
section=body.split('## 4. 光路上的SFG极化',1)[1].split('## 5. L系数与SFG电场',1)[0]
assert '![' not in section
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B092','date':'2026-10-19','page':11,'equation':'4.30b','body_image_blocks_replaced':1,'scope_check':'仅公式及状态行改变，其他正文相同','math_syntax_pass':render['math'],'render_overflow':False,'visual_review':'参考渲染与高清原式独立对照通过','section_4_numbered_equations_editable':33,'section_4_formula_image_references':0,'new_issues':0,'adopted_source_corrections':0,'next':'B093，5.1a—5.2c的L系数'}
(out/'B092验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

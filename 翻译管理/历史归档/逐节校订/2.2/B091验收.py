from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B091-修订前.md').read_text(encoding='utf-8')
new=(out/'B091-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
a=old.index('![式（4.30a）：');b=old.index('由式（4.24），得到A类源点',a)
assert new in body
norm=lambda s:re.sub(r'^> \*\*译校状态.*$','STATUS',s,flags=re.M)
assert norm(body.replace(new,old[a:b],1))==norm(old)
assert re.findall(r'\\tag\{([^}]+)\}',new)==['4.30a'] and new.count('$$')==2
formula=new.split('> **译校注')[0]
assert r'r_{m2,\mathrm{vis},\beta}e^{2i\beta_{m,\mathrm{ir}}h_m}' in formula
assert r'r_{m2,\mathrm{ir},\gamma}e^{2i\beta_{m,\mathrm{vis}}h_m}' in formula
assert r'\exp\!\left[-2ih_m' in formula
assert formula.count(r'\exp\!\left[-i\,2nh_m')==2
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));r=next(x for x in render['results'] if x['batch']=='B091')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'));assert len(idx)==116
assert next(x for x in idx if x['equation']=='4.30a')['representation']=='数学转写'
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B091','date':'2026-10-19','page':11,'equation':'4.30a','body_image_blocks_replaced':1,'scope_check':'仅公式及状态行改变，其他正文相同','math_syntax_pass':render['math'],'render_overflow':False,'visual_review':'参考渲染与高清全式及六倍首部对照通过','new_issue':'Q064；交叉频率与全部整体相位保留','adopted_source_corrections':0,'next':'B092，式4.30b'}
(out/'B091验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

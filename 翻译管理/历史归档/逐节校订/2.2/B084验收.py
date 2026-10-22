from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B084-修订前.md').read_text(encoding='utf-8')
new=(out/'B084-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
a=old.index('![式（4.22）—（4.24）');b=old.index('> **译校注（Q044，',a)
assert new in body
restored=body.replace(new,old[a:b],1)
norm=lambda s:re.sub(r'^> \*\*译校状态.*$','STATUS',s,flags=re.M)
assert norm(restored)==norm(old),'Unexpected content change'
assert re.findall(r'\\tag\{([^}]+)\}',new)==['4.22','4.23','4.24']
assert new.count('$$')==6
assert r'\sin\theta_{m,\mathrm{vis}}\;k_{m,\mathrm{ir}}' in new
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
r=next(x for x in render['results'] if x['batch']=='B084')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'))
assert len(idx)==116
assert all(next(x for x in idx if x['equation']==f'4.{n}')['representation']=='数学转写' for n in range(22,25))
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B084','date':'2026-10-19','pages':[8,9],'equations':['4.22','4.23','4.24'],'editable_equations_added':3,'body_image_blocks_replaced':1,'scope_check':'仅公式组和状态行改变，其他正文相同','strict_syntax_math_fragments':render['math'],'render_overflow':False,'visual_review':'B084-参考渲染.png与p8高清原式及p9编号对照','new_issue':'Q060；原式并置保留','new_errata':0,'next':'B085，式4.26a起'}
(out/'B084验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))

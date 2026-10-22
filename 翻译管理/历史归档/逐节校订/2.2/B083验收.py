from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B083-修订前.md').read_text(encoding='utf-8')
new=(out/'B083-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
assert new in body
a=old.index('![式（4.19）—（4.21）');b=old.index('再考虑 $A_n$',a)
restored=body.replace(new,old[a:b],1)
def normalize(s):
    s=re.sub(r'^> \*\*译校状态.*$', 'STATUS',s,flags=re.M)
    s=re.sub(r'^> \*\*译校注（Q044，保留原式）：\*\*.*$', 'Q044',s,flags=re.M)
    return s
assert normalize(restored)==normalize(old),'Unexpected content change'
assert re.findall(r'\\tag\{([^}]+)\}',new)==['4.19','4.20','4.21']
assert new.count('$$')==6
assert r'2(n+1)' in new.split(r'\tag{4.19}')[0]
assert r'2(n+1)' in new.split(r'\tag{4.20}')[0].split(r'\tag{4.19}')[1]
assert r'\exp\!\left[-i(2n+1)' in new.split(r'\tag{4.20}')[1]
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
r=next(x for x in render['results'] if x['batch']=='B083')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'))
assert len(idx)==116
assert all(next(x for x in idx if x['equation']==f'4.{n}')['representation']=='数学转写' for n in range(19,22))
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B083','date':'2026-10-19','page':8,'equations':['4.19','4.20','4.21'],'editable_equations_added':3,'body_image_blocks_replaced':1,'scope_check':'仅替换公式组、细化Q044与状态行，其他正文相同','strict_syntax_math_fragments':render['math'],'render_overflow':False,'visual_review':'B083-参考渲染.png与p8高清原式对照','issue_updated':'Q044；原式未改','new_errata':0,'next':'B084，式4.22—4.24'}
(out/'B083验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))

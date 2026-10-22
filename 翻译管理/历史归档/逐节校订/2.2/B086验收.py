from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');old=(out/'B086-修订前.md').read_text(encoding='utf-8')
new=(out/'B086-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
a=old.index('![式（4.26b）之前');b=old.index('#### 4.2b.',a)
assert new in body
def normalize(s):
    s=re.sub(r'^> \*\*译校状态.*$','STATUS',s,flags=re.M)
    return re.sub(r'^> \*\*译校注（Q046，保留原式）：\*\*.*$','Q046',s,flags=re.M)
assert normalize(body.replace(new,old[a:b],1))==normalize(old)
assert re.findall(r'\\tag\{([^}]+)\}',new)==['4.26b'] and new.count('$$')==4
assert new.count("(h_{m'})")==2 and 'Q046续' in new
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));r=next(x for x in render['results'] if x['batch']=='B086')
assert not r['overs'] and r['width']==r['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'));assert len(idx)==116
assert next(x for x in idx if x['equation']=='4.26b')['representation']=='数学转写'
assert hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B086','date':'2026-10-19','page':9,'numbered_equation':'4.26b','unnumbered_formula_added':1,'body_image_blocks_replaced':2,'scope_check':'仅本分支、状态行及Q046识别说明改变，其他正文相同','math_syntax_pass':render['math'],'render_overflow':False,'visual_review':'参考渲染与两幅高清原式及六倍左端局部图对照通过','issue_updated':'Q046：h_m′原记号复核','new_source_corrections':0,'next':'B087，式4.27'}
(out/'B086验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

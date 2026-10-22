from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
target=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=target.read_text(encoding='utf-8');old=(out/'B082-修订前.md').read_text(encoding='utf-8')
new=(out/'B082-本批译文.md').read_text(encoding='utf-8').strip()
assert new in body
assert body[body.index('#### 4.1g.'):]==old[old.index('#### 4.1g.'):]
assert body[body.index('## 1. 序论'):body.index('#### 4.1d.')]==old[old.index('## 1. 序论'):old.index('#### 4.1d.')]
assert re.findall(r'\\tag\{([^}]+)\}',new)==[f'4.{n}' for n in range(10,19)]
assert r'e^{\beta_{m,\mathrm{ir}}h_m}' in new.split(r'\tag{4.17}')[0].split(r'\tag{4.16}')[1]
assert new.count('$$')==18
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
check=next(r for r in render['results'] if r['batch']=='B082')
assert not check['overs'] and check['width']==check['scrollWidth']
idx=json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8'))
assert all(next(r for r in idx if r['equation']==f'4.{n}')['representation']=='数学转写' for n in range(10,19))
source=root/'日语原版/Chapter2/chap2-2.pdf'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
result={'batch':'B082','date':'2026-10-19','source_page':7,'equations':[f'4.{n}' for n in range(10,19)],'editable_equations_added':9,'body_image_blocks_replaced':3,'prefix_body_unchanged':True,'tail_from_4_1g_unchanged':True,'source_unchanged':True,'strict_syntax_math_fragments':render['math'],'render_overflow':False,'visual_review':'B082-版面抽查.png与原文p7及三幅高清原式图对照','new_issue':'Q059','adopted_source_corrections':0,'remaining':'从4.19—4.21继续可编辑转写；未进入2.3'}
(out/'B082验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))

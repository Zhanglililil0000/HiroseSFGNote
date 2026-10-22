from pathlib import Path
import re,json
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];D=ROOT/'中文版本/第二章 薄膜产生的SFG'
files=[next(D.glob('2.3 *.md')),OUT/'B115-本批译文.md',next(D.glob('2.2 *.md')),OUT.parent/'2.2/B111-本批译文.md']
for p in files:
 s=p.read_text(encoding='utf-8').replace(chr(9)+'heta',chr(92)+'theta').replace(chr(36)+'sin^2',chr(36)+chr(92)+'sin^2')
 p.write_text(s,encoding='utf-8')
s=files[0].read_text(encoding='utf-8');old=(OUT/'B115-修订前.md').read_text(encoding='utf-8')
assert s[s.index('## 附录B'):]==old[old.index('## 附录B'):]
tags=re.findall(r'\\tag\{([^}]+)\}',s[:s.index('## 附录B')]);assert len(tags)==16 and len(set(tags))==16
assert not [c for c in s if ord(c)<32 and c not in '\n\r']
report={'batch':'B115','pages':[1,3],'end':'附录B标题前','numbered_equations':tags,'unreviewed_B_to_D_unchanged':True,'issue':'Q073；关联第2.2节Q053/Q072','source_corrections_adopted':False,'status':'内容核验完成；最终显示见渲染检查.json'}
(OUT/'B115验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

from pathlib import Path
import re,json
o=Path(__file__).resolve().parent
# Each entry is manually transcribed from the page image. sN denotes sqrt(N).
groups=[[
('xxx','2Y(1;1b,1)/s8+2Y(1;1b,3)/s40-3Y(3;1b)/s60-Y(3;3b)/2'),
('xyy','Y(1;1b,1)/s8+Y(1;1b,2)/2-Y(1;1b,3)/s40+Y(2;1a,1)/2-Y(2;1a,2)/s12-Y(3;1b)/s60+Y(3;3b)/2'),
('xzz','Y(1;1b,1)/s8+Y(1;1b,2)/2-Y(1;1b,3)/s40-Y(2;1a,1)/2+Y(2;1a,2)/s12+4Y(3;1b)/s60'),
('xxy','Y(1;1a,1)/s8-Y(1;1a,2)/2-Y(1;1a,3)/s40+Y(2;1b,1)/2+Y(2;1b,2)/s12-Y(3;1a)/s60+Y(3;3a)/2'),
('xyx','4Y(1;1a,3)/s40-2Y(2;1b,2)/s12-Y(3;1a)/s60+Y(3;3a)/2'),
('xyz','Y(0;0)/s6+Y(2;0,1)/s12-Y(2;0,2)/2+Y(2;02b,1)/2+Y(2;2b,2)/s12+Y(3;2a)/s6'),
('xzy','-Y(0;0)/s6+2Y(2;0,1)/s12-2Y(2;2b,2)/s12+Y(3;2a)/s6'),
('xzx','4Y(1;0,3)/s40+2Y(2;2a,2)/s12+Y(3;0)/s10-Y(3;2b)/s6'),
('xxz','Y(1;0,1)/s8-Y(1;0,2)/2-Y(1;0,3)/s40-Y(2;2a,1)/2-Y(2;2a,2)/s12-Y(3;0)/s10-Y(3;2b)/s6')
],[
('yxx','Y(1;1a,1)/s8+Y(1;1a,2)/2-Y(1;1a,3)/s40-Y(2;1b,1)/2+Y(2;1b,2)/s12-Y(3;1a)/s60+Y(3;3a)/2'),
('yyy','2Y(1;1a,1)/s8+2Y(1;1a,3)/s40-3Y(3;1a)/s60-Y(3;3a)/2'),
('yzz','Y(1;1a,1)/s8+Y(1;1a,2)/2-Y(1;1a,3)/s40+Y(2;1b,1)/2-Y(2;1b,2)/s12+4Y(3;1a)/s60'),
('yxy','4Y(1;1b,3)/s40+2Y(2;1a,2)/s12-Y(3;1b)/s60+Y(3;3b)/2'),
('yyx','Y(1;1b,1)/s8-Y(1;1b,2)/2-Y(1;1b,3)/s40-Y(2;1a,1)/2-Y(2;1a,2)/s12-Y(3;1b)/s60+Y(3;3b)/2'),
('yyz','Y(1;0,1)/s8-Y(1;0,2)/2-Y(1;0,3)/s40+Y(2;2a,1)/2+Y(2;2a,2)/s12+Y(3;0)/s10+Y(3;2b)/s6'),
('yzy','4Y(1;0,3)/s40-2Y(2;2a,2)/s12+Y(3;0)/s10+Y(3;2b)/s6'),
('yzx','Y(0;0)/s6-2Y(2;0,1)/s12-2Y(2;2b,2)/s12+Y(3;2a)/s6'),
('yxz','-Y(0;0)/s6-Y(2;0,1)/s12+Y(2;0,2)/2+Y(2;02b,1)/2+Y(2;2b,2)/s12+Y(3;2a)/s6')
],[
('zxx','Y(1;0,1)/s8+Y(1;0,2)/2-Y(1;0,3)/s40+Y(2;2a,1)/2-Y(2;2a,2)/s12+Y(3;0)/s10-Y(3;2b)/s6'),
('zyy','Y(1;0,1)/s8+Y(1;0,2)/2-Y(1;0,3)/s40-Y(2;2a,1)/2+Y(2;2a,2)/s12+Y(3;0)/s10+Y(3;2b)/s6'),
('zzz','2Y(1;0,1)/s8+2Y(1;0,3)/s40-2Y(3;0)/s10'),
('zxy','Y(0;0)/s6+Y(2;0,1)/s12+Y(2;0,2)/2-Y(2;02b,1)/2+Y(2;2b,2)/s12+Y(3;2a)/s6'),
('zyx','-Y(0;0)/s6-Y(2;0,1)/s12-Y(2;0,2)/2-Y(2;02b,1)/2+Y(2;2b,2)/s12+Y(3;2a)/s6'),
('zyz','4Y(1;1a,3)/s40+2Y(2;1b,2)/s12+4Y(3;1a)/s60'),
('zzy','Y(1;1a,1)/s8-Y(1;1a,2)/2-Y(1;1a,3)/s40-Y(2;1b,1)/2-Y(2;1b,2)/s12+4Y(3;1a)/s60'),
('zzx','Y(1;1b,1)/s8-Y(1;1b,2)/2-Y(1;1b,3)/s40+Y(2;1a,1)/2+Y(2;1a,2)/s12+4Y(3;1b)/s60'),
('zxz','4Y(1;1b,3)/s40-2Y(2;1a,2)/s12+4Y(3;1b)/s60')
]]
pat=r'([+-]?)(\d*)Y\((\d);([^)]*)\)/(s?\d+)'
manifest=[]
for g,rows in enumerate(groups):
 batch=f'B{427+g}';parts=['### 式(5'+chr(97+g)+')：首指标为'+ 'xyz'[g]+'的分量','']
 if g==0:parts+=['> **排版说明（译者）：** 原式(5a)跨PDF p3—4。以下按原顺序逐分量断行，式(5a)—(5c)的每组9个等式共用原组号；分段不改变原指标、项序或符号。','']
 for j,(sub,expr) in enumerate(rows):
  matches=list(re.finditer(pat,expr));assert ''.join(m.group() for m in matches)==expr
  terms=[]
  for m in matches:
   sign,coef,rank,idx,den=m.groups();num=(coef if coef and coef!='1' else '')+'Y^{('+rank+')}_{'+idx+'}'
   denominator='\\sqrt{'+den[1:]+'}' if den.startswith('s') else den
   terms.append(sign+'\\frac{'+num+'}{'+denominator+'}')
  # Split long rows after three terms to fit a reading-width page.
  lines=[]
  for k in range(0,len(terms),3):lines.append(('\\beta_{'+sub+'}={}&' if k==0 else '&')+''.join(terms[k:k+3]))
  tag='\\tag{5'+chr(97+g)+'}' if j==8 else ''
  parts+=['$$','\\begin{aligned}\n'+'\\\\\n'.join(lines)+'\n\\end{aligned}'+tag,'$$','']
  manifest.append({'batch':batch,'component':sub,'source':'p3—4' if g==0 else 'p4','terms':len(terms),'原序表达':expr})
 if g==0:parts+=['> **原文疑点（Q203，PDF p3—4，式(5)）：** $Y_{02b,1}^{(2)}$中的前导0在xyz、yxz、zxy、zyx四行均按底本保留；与其他基底的$2b,1$记法是否相同尚未确认，不自行删去。另，xxy及xyx两行均按底本保留各项系数，未按对称关系替换。','']
 (o/(batch+'-本批译文.md')).write_text('\n'.join(parts),encoding='utf-8')
assert len({x['component'] for x in manifest})==27
assert {x['component'] for x in manifest}=={a+b+c for a in 'xyz' for b in 'xyz' for c in 'xyz'}
(o/'式5逐项清单.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('27分量，逐项清单及B427—B429译稿已生成。')

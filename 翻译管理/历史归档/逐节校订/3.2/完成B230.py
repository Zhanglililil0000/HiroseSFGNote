from pathlib import Path
import re,json,hashlib
p=Path(__file__).resolve().parent
root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8')
start=s.index('<!-- B229止；')
body_start=s.index('下文所用符号定义如下。',start)
end=s.index('**$m\'$',body_start)
body=s[body_start:end]
body=body.replace('**（到达第一个界面前的相位变化）**','#### 到达第一个界面之前的相位变化')
body=body.replace('**（多重反射中的单元）**','#### 多重反射中的单元')
body=body.replace('（注意：带 $*$ 号的量并不表示复共轭。）','（这里需要注意，带$*$号的量并不表示复共轭。）\n\n> **译者注（原文疑点Q113，PDF p2）：** 原文将$b_0$、$b_0^*$分别写成与$a_0$、$a_0^*$相同的表达式，仍使用$z_1$、$h_{m\'}$和$\\theta_{m\'}$，此处照录。若$b_0$对应$m$层内源点，候选为相应的$z_2$、$h_m$、$\\theta_m$写法，须结合后续路径定义核验；未采用替换。这些相位指数未显式写波数因子，原页亦未在此说明长度归一化，不自行补入。')
body=body.replace('\\begin{pmatrix}','\\begin{bmatrix}').replace('\\end{pmatrix}','\\end{bmatrix}')
z='Z = |E - X| = |E - X\'| = |E - Y| = |E - Y\'| = 1 + r_{1m\'} r_{m\'m} a^2 + (r_{m\'m} + r_{1m\'} a^2) r_{m2} b^2'
zr=r'''\begin{aligned}
Z&=|E-X|=|E-X'|=|E-Y|=|E-Y'|\\
&=1+r_{1m'}r_{m'm}a^2+(r_{m'm}+r_{1m'}a^2)r_{m2}b^2
\end{aligned}'''
assert z in body
body=body.replace(z,zr)
body+='> **译者注（矩阵记号）：** 由本段矩阵级数及逆矩阵的用法，这里的$E$应读作二阶单位矩阵，竖线表示行列式；它与后面表示电场的$E^\\pm$不同。此说明为译者依据上下文作出的记号解释，原文未在本段另列定义。$a$、$b$为传播相位因子，$\\alpha$、$\\beta$、$\\gamma$为反射和透射因子与相位的组合，不等同于其他章节的分子响应系数。\n\n'
batch='## 2. 二层系（$1/m\'/m/2$）的和频\n\n### 2.1 概述\n\n'+body
(p/'B230-本批译文.md').write_text(batch,encoding='utf-8')
s=s[:start]+batch+'<!-- B230止；以下为旧译待核 -->\n\n> **校订状态：** 以下源点场公式尚未完成本轮逐页校订。\n\n'+s[end:]
s=s.replace('B228—B229已核第1—2页开篇及第1部分全部系数；第2部分起仍为旧译待核。','B228—B230已核第1部分及2.1的相位、矩阵与Z定义；式(2.1)起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
# 辅助代数检查只验证四行列式的一致性，不改写原文。
def add(a,b,sign=1):
    out=dict(a)
    for k,v in b.items(): out[k]=out.get(k,0)+sign*v
    return {k:v for k,v in out.items() if v}
def mul(a,b):
    out={}
    for i,v in a.items():
        for j,w in b.items():
            k=tuple(x+y for x,y in zip(i,j))
            out[k]=out.get(k,0)+v*w
    return {k:v for k,v in out.items() if v}
one={(0,0,0):1}; a={(1,0,0):1}; b={(0,1,0):1}; c={(0,0,1):1}
matrices=[(a,b,a,add(b,c)),(add(a,b),mul(b,c),one,c),(add(b,c),mul(a,b),one,a),(c,b,c,add(a,b))]
dets=[add(mul(add(one,u,-1),add(one,x,-1)),mul(v,w),-1) for u,v,w,x in matrices]
expected={(0,0,0):1,(1,0,0):-1,(0,1,0):-1,(0,0,1):-1,(1,0,1):1}
assert all(x==expected for x in dets)
record=dict(batch='B230',date='2026-10-20',pages=[2],units='2.1的相位、αβγ、X/X′/Y/Y′及Z定义',source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,unresolved=['Q113'],four_determinants_equal=True,determinant_polynomial='1-alpha-beta-gamma+alpha*gamma',next='B231：p2—3的m′层E+源，式2.1—2.2；核矩阵乘法顺序与源点坐标')
(p/'B230-覆盖.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B230.md').write_text('''# B230 校订记录

核对PDF p2的2.1引言、a₀/a₀*、b₀/b₀*、a/b及αβγ、四个2×2矩阵和Z。全部保留为可编辑数学文本；恢复原方括号矩阵外形，Z仅分行。辅助代数检查证实四个行列式均为1−α−β−γ+αγ，不据此反向重写原式。

原文b₀定义的层标/深度与a₀相同，登记Q113并就地保留候选，不自动替换；指数波数或长度归一化未在本段明确，也不补定。原文明确说明星号非复共轭。单位矩阵E与行列式的解释标为译者上下文推断，不冒称作者定义。无原文修正采用，不新增已确认勘误。

下一批必须重核式2.1—2.2的行向量、矩阵级数、列向量顺序。旧译存在乘法顺序可疑的迹象，尚未在本批修改。
''',encoding='utf-8')
card=p/'局部约定卡.md'
t=card.read_text(encoding='utf-8').replace('- 待核：a、b与α、β、γ的不同含义；a₀、b₀上星号的非共轭约定；矩阵E的单位矩阵含义、Z行列式、δ的局部定义。','- B230已核：a/b为相位因子，αβγ为本节多重反射组合；星号明确不是复共轭。b₀定义照原页重复a₀定义，记Q113。长度归一化/波数未在本段说明，不补定。E为二阶单位矩阵、竖线为行列式的解释依据上下文，已在正文注明译者推断。四矩阵行列式一致性通过辅助检查。\n- 待核：δ的局部定义，以及Q113与后续源点路径的对应。')
card.write_text(t,encoding='utf-8')
structure=p/'结构与复用核验表.md'
t=structure.read_text(encoding='utf-8').replace('| 2.1概述，p2—4 | 旧译待核 | 待分批 |','| 2.1符号与矩阵定义，p2 | 已对照原页；Q113未决 | B230 |\n| 2.1源点场公式，p2—4 | 旧译待核 | 下一批B231起 |')
structure.write_text(t,encoding='utf-8')
question='''\n\n## Q113：3.2相位因子的重复定义（待核验）

位置：3.2 PDF p2，2.1“到达第一个界面之前的相位变化”。b₀和b₀*原式与a₀和a₀*相同，均使用z₁、hₘ′、θₘ′；正文保留原式。若b₀对应m层源点，候选为z₂、hₘ、θₘ的对应式，须结合后续源点路径核验。指数未显式列波数，归一化本段未说明；不自行补入。星号非复共轭则由原文明示。未采用原文修正，不纳入已确认勘误附件。B230登记。
'''
questions=root/'翻译管理/疑难与勘误.md'
questions.write_text(questions.read_text(encoding='utf-8')+question,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'
t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B230完成3.2的2.1符号定义（2026-10-20）\n\n已核p2相位、αβγ、四矩阵及Z，辅助检查四行列式一致。星号非共轭按原文明示；b₀重复a₀的定义记Q113，保留原式并列候选。未采用原文修正。\n\n下一批B231：接p2—3中m′层E+源的式2.1—2.2；重点核行向量—矩阵—列向量的次序、源坐标及路径因子，不复用旧译的矩阵乘法次序。式2.1起仍待本轮校订。以下为历史记录。\n',1)
progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'
t=nav.read_text(encoding='utf-8').replace('第2部分仍待校订，下一批核2.1的相位与矩阵定义。','B230已核2.1相位与矩阵定义（Q113保留待核）；下一批核式2.1—2.2的源点场。')
nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'
t=listing.read_text(encoding='utf-8').replace('本轮校订中：B228—B229已核开篇与第1部分全部系数；第2部分待核','本轮校订中：B228—B230已核第1部分及2.1符号矩阵定义；式2.1起待核')
listing.write_text(t,encoding='utf-8')
print(json.dumps(record,ensure_ascii=False))

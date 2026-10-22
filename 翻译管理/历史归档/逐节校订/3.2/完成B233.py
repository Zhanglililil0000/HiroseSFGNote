from pathlib import Path
from fractions import Fraction as F
import json,hashlib
p=Path(__file__).resolve().parent
root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8')
start=s.index('<!-- B232止；')
end=s.index('$E^-$ sources:',start)
batch=r'''#### $m$层中距$m'/m$界面深度$z_2$处产生的和频光

**$E^+$源（初始向下传播的光）**

$$
\begin{aligned}
E^-(0^-)
&=t_{m'1}b_0^*r_{m2}ab
\begin{bmatrix}t_{m'm}&\gamma t_{m'm}\end{bmatrix}\\
&\qquad\cdot[E+X'+X'^2+\cdots]
\begin{bmatrix}1\\0\end{bmatrix}L^+_{m/m}P(z_2)\\
&=t_{m'1}b_0^*r_{m2}ab
\begin{bmatrix}t_{m'm}&\gamma t_{m'm}\end{bmatrix}\\
&\qquad\cdot[E-X']^{-1}
\begin{bmatrix}1\\0\end{bmatrix}L^+_{m/m}P(z_2)\\
&=t_{m'1}b_0^*t_{mm'}r_{m2}abL^+_{m/m}P(z_2)/Z
\end{aligned}
\tag{2.5}
$$

$$
\begin{aligned}
E^+(h_m^+)
&=t_{m2}b_0^*t_{m'm}b
\begin{bmatrix}\gamma&\beta\end{bmatrix}
[E+Y'+Y'^2+\cdots]
\begin{bmatrix}1\\1\end{bmatrix}L^+_{m/m}P(z_2)\\
&=t_{m2}b_0^*t_{m'm}b
\begin{bmatrix}\gamma&\beta\end{bmatrix}
[E-Y']^{-1}
\begin{bmatrix}1\\1\end{bmatrix}L^+_{m/m}P(z_2)\\
&=t_{m2}b_0^*(1+r_{1m'}r_{m'm}a^2)L^+_{m/m}P(z_2)/Z
\end{aligned}
\tag{2.6}
$$

> **译者注（原文疑点Q115，PDF p3，式2.5—2.6）：** 式(2.5)前两行的行向量含$t_{m'm}$，末行却写$t_{mm'}$。按前述$X'$求矩阵乘积，得到$t_{m'm}/Z$，层标差异保留原样；候选为统一至同一透射方向，须结合光路核验。式(2.6)前两行保留外部$t_{m'm}b$及行向量$[\gamma,\beta]$，其中矩阵乘积为$[\gamma(1-\alpha)+\beta]/Z$；末行则不含该外部因子，括号为$1+r_{1m'}r_{m'm}a^2=1-\alpha$，两者一般不一致。候选为重新核对行向量和外部路径因子的配置，未采用替换。$b_0^*$仍沿用本节原定义，相关层标疑点见Q113。

> **译者注（旧译转录修复）：** 已恢复两式首行的“行向量—矩阵级数—列向量”顺序，并补回两式旧译遗漏的逆矩阵中间行。式(2.5)续行乘点仅为排版所加；所有原文因子均保留。

'''
(p/'B233-本批译文.md').write_text(batch,encoding='utf-8')
s=s[:start]+batch+'<!-- B233止；以下为旧译待核 -->\n\n> **校订状态：** 以下从$m$层$E^-$源的式(2.7)起仍待本轮逐页校订。\n\n'+s[end:]
s=s.replace('B228—B232已核第1部分、2.1符号定义及式(2.1)—(2.4)；式(2.5)起仍为旧译待核。','B228—B233已核第1部分、2.1符号定义及式(2.1)—(2.6)；式(2.7)起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
# 精确有理数辅助检查，与按二阶伴随矩阵展开所得表达式比对。
for a,b,c,t in [(F(1,5),F(1,7),F(1,11),F(2,3)),(F(-1,3),F(1,8),F(1,9),F(3,4))]:
    z=1-a-b-c+a*c
    assert t*(1-c)/z+c*t/z==t/z
    # (E-Y′)^(-1)(1,1)^T = (1-alpha,1)^T/Z。
    assert c*(1-a)/z+b/z==(c*(1-a)+b)/z
record=dict(batch='B233',date='2026-10-20',pages=[3],tags=['2.5','2.6'],source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,unresolved=['Q113','Q115'],old_translation_repairs=['恢复矩阵乘法顺序','补回两式逆矩阵中间行'],next='B234：p3—4的m层E−源式2.7—2.8，接完整跨页三行并核对因子')
(p/'B233-覆盖.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B233.md').write_text('''# B233 校订记录

核PDF p3的m层E+源式2.5、2.6，各三行完整保留。核源深度z₂、b₀*、两层透射方向、ab/b相位、X′/Y′及列向量(1,0)/(1,1)、L+、P(z₂)和Z。补回旧译两中间行，恢复首行矩阵次序；非原文修正。

Q115：2.5行向量tₘ′ₘ与末行tₘₘ′不同；2.6矩阵乘积与外部因子配置和末行不一致。保留原式、就地说明，未采用候选。Q113仍未解决，m层源点语境加强了层标疑问，但不据此替换b₀定义。辅助逆矩阵展开及精确有理数检查用于说明疑点，不代替源页核对。

下一批B234接p3—4的m层E−源2.7—2.8，须接全跨页推导行。
''',encoding='utf-8')
q='''\n\n## Q115：3.2式2.5—2.6的透射层标与矩阵化简（待核验）

位置：PDF p3。式2.5前两行行向量为[tₘ′ₘ, γtₘ′ₘ]，矩阵乘积为tₘ′ₘ/Z，而末行使用tₘₘ′；候选为按光路统一透射方向，未采用。式2.6前两行含外部tₘ′ₘ b及行向量[γ,β]，矩阵乘积为[γ(1−α)+β]/Z；末行不含该外部因子且括号为1−α。候选为复核向量及路径因子配置，不能仅凭末行补改。正文完整三行照录，未采用原文修正，不新增已确认勘误。关联Q113的b₀*定义。B233登记。
'''
questions=root/'翻译管理/疑难与勘误.md'
questions.write_text(questions.read_text(encoding='utf-8')+q,encoding='utf-8')
card=p/'局部约定卡.md'
card.write_text(card.read_text(encoding='utf-8')+'\n- B233：m层源点深度自m′/m界面计为z₂；2.5、2.6使用b₀*，保留其原定义（Q113）。透射方向差异及矩阵化简差异记Q115，不跨行统一。\n',encoding='utf-8')
structure=p/'结构与复用核验表.md'
t=structure.read_text(encoding='utf-8').replace('| m层源点场，p3—4，式2.5起 | 旧译待核 | 下一批B233起 |','| m层E+源，p3，式2.5—2.6 | 已对照原页；Q115未决 | B233 |\n| m层E−源，p3—4，式2.7—2.8 | 旧译待核 | 下一批B234 |')
structure.write_text(t,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'
t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B233完成3.2式2.5—2.6（2026-10-20）\n\n已核p3的m层E+源两式，补回两条逆矩阵中间行并修复旧译矩阵次序。原式透射层标与矩阵化简差异登记Q115，正文保留原三行；Q113仍未决，未采用原文修正。\n\n下一批B234：接p3—4的m层E−源式2.7—2.8，完整核跨页三行、前因子、层标与矩阵次序。2.7起仍为旧译待核。以下为历史记录。\n',1)
progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'
t=nav.read_text(encoding='utf-8').replace('下一批核m层E+源式2.5—2.6。','B233已核m层E+源式2.5—2.6（Q115保留原式待核）；下一批核E−源式2.7—2.8。')
nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'
t=listing.read_text(encoding='utf-8').replace('本轮校订中：B228—B232已核第1部分、2.1定义及式2.1—2.4；式2.5起待核','本轮校订中：B228—B233已核第1部分、2.1定义及式2.1—2.6；式2.7起待核')
listing.write_text(t,encoding='utf-8')
print(json.dumps(record,ensure_ascii=False))

from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8')
start=s.index('<!-- B231止；')
end=s.index('**$m$ 层中',start)
batch=r'''**$E^-$源（初始向上传播的光）**

$$
\begin{aligned}
E^-(0^-)
&=t_{m'1}a_0
\begin{bmatrix}\alpha&\beta\end{bmatrix}
[E+X+X^2+\cdots]
\begin{bmatrix}1\\1\end{bmatrix}L^-_{m'/m'}P(z_1)\\
&=t_{m'1}a_0
\begin{bmatrix}\alpha&\beta\end{bmatrix}
[E-X]^{-1}
\begin{bmatrix}1\\1\end{bmatrix}L^-_{m'/m'}P(z_1)\\
&=t_{m'1}a_0(1+r_{mm'}r_{m2}b^2)L^-_{m'/m'}P(z_1)/Z
\end{aligned}
\tag{2.3}
$$

$$
\begin{aligned}
E^+(h_m^+)
&=t_{m2}a_0r_{m'1}at_{m'm}
\begin{bmatrix}1&\alpha\end{bmatrix}
[E+Y+Y^2+\cdots]
\begin{bmatrix}1\\0\end{bmatrix}L^-_{m'/m'}P(z_1)\\
&=t_{m2}a_0r_{m'1}at_{m'm}
\begin{bmatrix}1&\alpha\end{bmatrix}
[E-Y]^{-1}
\begin{bmatrix}1\\0\end{bmatrix}L^-_{m'/m'}P(z_1)\\
&=t_{m2}a_0r_{m'1}t_{m'm}abL^-_{m'/m'}P(z_1)/Z
\end{aligned}
\tag{2.4}
$$

> **译者注（原文疑点Q114，PDF p3，式2.3—2.4）：** 式(2.3)前两行的行向量原印为$[\alpha,\beta]$，但按已定义的$X$计算，该矩阵乘积为$(\alpha+\beta-\alpha\gamma)/Z$，与末行的$(1+r_{mm'}r_{m2}b^2)/Z$不一致。若将行向量改为$[1,0]$，可得到末行所写的$(1-\gamma)/Z$，但这仅是待核候选，本译文仍保留原向量。式(2.4)前两行的外部因子均未写$b$，末行却含$b$；由于其中的矩阵乘积为$1/Z$，两种写法亦存在待核差异。候选为前两行补$b$或另核末行相位，均未采用。两式完整三行按底本保留，未用候选值替换。

> **译者注（旧译转录修复）：** 两式首行恢复为“行向量—矩阵级数—列向量”的原文次序；式(2.4)补回旧译遗漏的逆矩阵中间行。这些属于旧译修复，不是对原文公式的修正。

'''
(p/'B232-本批译文.md').write_text(batch,encoding='utf-8')
s=s[:start]+batch+'<!-- B232止；以下为旧译待核 -->\n\n> **校订状态：** 以下从$m$层源点的式(2.5)起仍待本轮逐页校订。\n\n'+s[end:]
s=s.replace('B228—B231已核第1部分、2.1符号定义及式(2.1)—(2.2)；式(2.3)起仍为旧译待核。','B228—B232已核第1部分、2.1符号定义及式(2.1)—(2.4)；式(2.5)起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
# 有理数取值辅助复核逆矩阵结果，不据此修正原文。
from fractions import Fraction as F
for a,b,c in [(F(1,5),F(1,7),F(1,11)),(F(-1,3),F(1,8),F(1,9))]:
    z=1-a-b-c+a*c
    xcol=((1-c)/z,1/z)
    assert a*xcol[0]+b*xcol[1]==(a+b-a*c)/z
    # 注意X的逆矩阵乘(1,1)为((1-gamma),1)/Z。
    assert xcol[0]==(1-c)/z
    ycol=((1-a)/z,1/z)
    assert ycol[0]+a*ycol[1]==1/z
record=dict(batch='B232',date='2026-10-20',pages=[3],tags=['2.3','2.4'],source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,unresolved=['Q114'],old_translation_repairs=['恢复两首行的矩阵乘法顺序','补回2.4逆矩阵中间行'],next='B233：p3的m层E+源式2.5—2.6；核b₀*、层标和三行关系')
(p/'B232-覆盖.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B232.md').write_text('''# B232 校订记录

核PDF p3的m′层E−源式2.3、2.4。各保留级数、逆矩阵及末行化简式。旧译首行列向量提前和2.4中间行遗漏已修复，正文就地说明。

Q114：2.3原行向量与末行不一致；2.4前两行缺b而末行含b。保留原式，不采用候选，不收入已确认勘误。辅助代数关系见验收记录；这些计算只用于说明不一致，不替代源页对照。

下一批接m层E+源2.5—2.6；Q113继续待后续路径核验。
''',encoding='utf-8')
q='''\n\n## Q114：3.2式2.3—2.4的矩阵化简与相位差异（待核验）

PDF p3。2.3前两行行向量为[α,β]，与X逆矩阵及(1,1)列向量乘积应为(α+β−αγ)/Z，而非末行(1−γ)/Z；候选行向量[1,0]可给出末行，尚未采用。2.4前两行无b，末行含b，矩阵部分为1/Z；候选为前两行补b或复核末行相位，均待核。正文保留原三行。旧译次序及漏行另作转录修复，不混入原文勘误。B232登记，未采用原文修正。
'''
questions=root/'翻译管理/疑难与勘误.md'
questions.write_text(questions.read_text(encoding='utf-8')+q,encoding='utf-8')
card=p/'局部约定卡.md'
card.write_text(card.read_text(encoding='utf-8')+'\n- B232：式2.3行向量及式2.4前后b因子差异记Q114，原三行均保留；不把末行自动作为前行的修订依据。\n',encoding='utf-8')
structure=p/'结构与复用核验表.md'
t=structure.read_text(encoding='utf-8').replace('| 2.1其余源点场，p3—4，式2.3起 | 旧译待核 | 下一批B232起 |','| m′层E−源，p3，式2.3—2.4 | 已对照原页；Q114未决 | B232 |\n| m层源点场，p3—4，式2.5起 | 旧译待核 | 下一批B233起 |')
structure.write_text(t,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'
t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B232完成3.2式2.3—2.4（2026-10-20）\n\n已核p3的m′层E−源，两式各三行完整转写；修复旧译首行次序及2.4漏行。2.3行向量化简差异、2.4前两行与末行b因子差异登记Q114，正文保留原式及候选说明，未采用原文修正。\n\n下一批B233：p3的m层E+源2.5—2.6，核b₀*、层标、矩阵次序及完整三行；结合后续路径继续核Q113，不擅自替换相位定义。式2.5起仍为旧译待核。以下为历史记录。\n',1)
progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'
t=nav.read_text(encoding='utf-8').replace('下一批核E−源式2.3—2.4。','B232已核E−源式2.3—2.4（Q114保留原式待核）；下一批核m层E+源式2.5—2.6。')
nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'
t=listing.read_text(encoding='utf-8').replace('本轮校订中：B228—B231已核第1部分、2.1定义及式2.1—2.2；式2.3起待核','本轮校订中：B228—B232已核第1部分、2.1定义及式2.1—2.4；式2.5起待核')
listing.write_text(t,encoding='utf-8')
print(json.dumps(record,ensure_ascii=False))

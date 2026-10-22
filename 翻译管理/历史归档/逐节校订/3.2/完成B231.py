from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8')
start=s.index('<!-- B230止；')
end=s.index('$E^-$ sources:',start)
batch=r'''#### $m'$层中深度$z_1$处产生的和频光

**$E^+$源（初始向下传播的光）**

$$
\begin{aligned}
E^-(0^-)
&=t_{m'1}a_0^*a
\begin{bmatrix}r_{m'm}&t_{m'm}r_{m2}t_{mm'}b^2\end{bmatrix}\\
&\qquad\cdot[E+X+X^2+\cdots]
\begin{bmatrix}1\\1\end{bmatrix}L^+_{m'/m'}P(z_1)\\
&=t_{m'1}a_0^*a
\begin{bmatrix}r_{m'm}&t_{m'm}r_{m2}t_{mm'}b^2\end{bmatrix}\\
&\qquad\cdot[E-X]^{-1}
\begin{bmatrix}1\\1\end{bmatrix}L^+_{m'/m'}P(z_1)\\
&=t_{m'1}a_0^*a(r_{m'm}+r_{m2}b^2)L^+_{m'/m'}P(z_1)/Z
\end{aligned}
\tag{2.1}
$$

$$
\begin{aligned}
E^+(h_m^+)
&=t_{m2}a_0^*t_{m'm}b
\begin{bmatrix}1&\alpha\end{bmatrix}
[E+Y+Y^2+\cdots]
\begin{bmatrix}1\\0\end{bmatrix}L^+_{m'/m'}P(z_1)\\
&=t_{m2}a_0^*t_{m'm}b
\begin{bmatrix}1&\alpha\end{bmatrix}
[E-Y]^{-1}
\begin{bmatrix}1\\0\end{bmatrix}L^+_{m'/m'}P(z_1)\\
&=t_{m2}a_0^*t_{m'm}bL^+_{m'/m'}P(z_1)/Z
\end{aligned}
\tag{2.2}
$$

> **译者注（转录与排版）：** 两式按原页保持“行向量—矩阵级数（或逆矩阵）—列向量”的顺序；旧译将第一个等号后的列向量提前，现已恢复底本顺序。式(2.1)为适应页面宽度分行，续行的乘点仅为排版所加。$0^-$、$h_m^+$等场位置记法均依本节原式，不改成其他章节的界面坐标。

'''
(p/'B231-本批译文.md').write_text(batch,encoding='utf-8')
s=s[:start]+batch+'<!-- B231止；以下为旧译待核 -->\n\n> **校订状态：** 以下从$E^-$源的式(2.3)起仍待本轮逐页校订。\n\n'+s[end:]
s=s.replace('B228—B230已核第1部分及2.1的相位、矩阵与Z定义；式(2.1)起仍为旧译待核。','B228—B231已核第1部分、2.1符号定义及式(2.1)—(2.2)；式(2.3)起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
record=dict(batch='B231',date='2026-10-20',pages=[2,3],tags=['2.1','2.2'],units='m′层深度z₁处E+源的反射、透射场；完整矩阵级数、逆矩阵与化简式',source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,old_translation_repairs=['两式首行的矩阵和列向量顺序恢复原文'],next='B232：p3的m′层E−源式2.3—2.4；完整核三行等式与相位因子')
(p/'B231-覆盖.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B231.md').write_text('''# B231 校订记录

源页：PDF p2末至p3上部。核m′层深度z₁处E+源，完整式2.1、2.2各三行：行向量、级数/逆矩阵、列向量、L+、P(z₁)、Z及外部相位。式2.1核两个反射路径分量、a₀* a及rₘ′ₘ+rₘ₂b²；式2.2核tₘ₂ a₀* tₘ′ₘ b及[1,α]和[1,0]列向量。

旧译两式首行把列向量放在矩阵级数之前，已按底本恢复。此为旧译转录错误，不是原文修正，不进入原文勘误附件。正文就地说明。式2.1仅分行并添加可见续行乘点；无物理量简写，无省略推导行。场位置保持底本0−、hₘ+；未自行替换坐标。

无新增原文疑点，无原文公式修正采用。Q113仍待后续m层路径核验。
''',encoding='utf-8')
card=p/'局部约定卡.md'
card.write_text(card.read_text(encoding='utf-8')+'\n- B231已核：m′层E+源两式沿用a₀*、a及b；矩阵乘法按行向量—矩阵—列向量顺序；0−与hₘ+是原式场位置记法，不跨章节自动重命名。\n',encoding='utf-8')
structure=p/'结构与复用核验表.md'
t=structure.read_text(encoding='utf-8').replace('| 2.1源点场公式，p2—4 | 旧译待核 | 下一批B231起 |','| m′层E+源，p2—3，式2.1—2.2 | 已对照原页；修复旧译乘法顺序 | B231 |\n| 2.1其余源点场，p3—4，式2.3起 | 旧译待核 | 下一批B232起 |')
structure.write_text(t,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'
t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B231完成3.2式2.1—2.2（2026-10-20）\n\n已核p2—3的m′层E+源反射/透射场，两式各三行完整保留。旧译首行的列向量提前问题已按底本恢复，属转录修复。源点、相位、L+及Z照录；未采用原文修正。\n\n下一批B232：p3的m′层E−源式2.3—2.4；核完整三行、矩阵次序与前因子，尤其不同等号前后相位因子的写法，疑点保留原式再注。式2.3起仍待校订。以下为历史记录。\n',1)
progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'
t=nav.read_text(encoding='utf-8').replace('下一批核式2.1—2.2的源点场。','B231已核m′层E+源式2.1—2.2；下一批核E−源式2.3—2.4。')
nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'
t=listing.read_text(encoding='utf-8').replace('本轮校订中：B228—B230已核第1部分及2.1符号矩阵定义；式2.1起待核','本轮校订中：B228—B231已核第1部分、2.1定义及式2.1—2.2；式2.3起待核')
listing.write_text(t,encoding='utf-8')
print(json.dumps(record,ensure_ascii=False))

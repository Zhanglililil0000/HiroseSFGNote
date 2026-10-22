from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8'); start=s.index('<!-- B233止；'); end=s.index('\n---\n',start)
batch=r'''**$E^-$源（初始向上传播的光）**

$$
\begin{aligned}
E^-(0^-)
&=t_{m'1}b_0\begin{bmatrix}1&\gamma\end{bmatrix}
[E+X'+X'^2+\cdots]
\begin{bmatrix}1\\0\end{bmatrix}L^-_{m/m}P(z_2)\\
&=t_{m'1}b_0\begin{bmatrix}1&\gamma\end{bmatrix}
[E-X']^{-1}
\begin{bmatrix}1\\0\end{bmatrix}L^-_{m/m}P(z_2)\\
&=t_{m'1}b_0at_{mm'}L^-_{m/m}P(z_2)/Z
\end{aligned}
\tag{2.7}
$$

$$
\begin{aligned}
E^+(h_m^+)
&=t_{m2}b_0b
\begin{bmatrix}r_{mm'}&t_{mm'}r_{m'1}t_{m'm}a^2\end{bmatrix}\\
&\qquad\cdot[E+Y'+Y'^2+\cdots]
\begin{bmatrix}1\\1\end{bmatrix}L^-_{m/m}P(z_2)\\
&=t_{m2}b_0b
\begin{bmatrix}r_{mm'}&t_{mm'}r_{m'1}t_{m'm}a^2\end{bmatrix}\\
&\qquad\cdot[E-Y']^{-1}
\begin{bmatrix}1\\1\end{bmatrix}L^-_{m/m}P(z_2)\\
&=-t_{m2}b_0b(r_{m'm}+r_{1m'}a^2)L^-_{m/m}P(z_2)/Z
\end{aligned}
\tag{2.8}
$$

> **译者注（原文疑点Q116，PDF p3—4，式2.7）：** 按前面定义的$X'$，行向量$[1,\gamma]$、逆矩阵与列向量$[1,0]^{\mathsf T}$的乘积为$1/Z$。原式前两行的外部因子只有$t_{m'1}b_0$，末行却另含$at_{mm'}$。候选为前两行补入该路径因子或重新核对末行，尚未采用；三行均按原页保留。$b_0$定义的层标疑点仍见Q113。

> **译者注（旧译转录修复）：** 恢复两式首行的矩阵乘法顺序，补回两式旧译遗漏的逆矩阵中间行。式(2.8)为适应页面宽度分行，续行乘点仅为排版所加。

'''
(p/'B234-本批译文.md').write_text(batch,encoding='utf-8')
s=s[:start]+batch+'<!-- B234止；以下为旧译待核 -->\n\n> **校订状态：** 以下2.2详论尚待本轮逐页校订。\n\n'+s[end:].replace('\n---\n','',1).lstrip()
s=s.replace('#### 2.2 详论','### 2.2 详论',1)
s=s.replace('B228—B233已核第1部分、2.1符号定义及式(2.1)—(2.6)；式(2.7)起仍为旧译待核。','B228—B234已核第1部分及2.1全部内容（式2.1—2.8）；2.2详论起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
record=dict(batch='B234',date='2026-10-20',pages=[3,4],tags=['2.7','2.8'],source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,unresolved=['Q113','Q116'],old_translation_repairs=['恢复两首行矩阵乘法顺序','补回两式逆矩阵中间行'],next='B235：p4的2.2引言、路径分类及式2.9—2.10')
(p/'B234-覆盖.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B234.md').write_text('''# B234 校订记录

核p3末至p4上部的m层E−源两式，完整保留各三行。2.7前两行在p3、末行在p4，未漏跨页项；2.8核反向r、两t、a²、总负号、b₀b、L−、P(z₂)与Z。补回旧译漏行及矩阵次序，非原文修正。

Q116：2.7末行比前两行多atₘₘ′，矩阵部分为1/Z，正文保留原式并列候选。2.8在使用本节r反号及t乘积关系时，矩阵化简可得到末行的负号与括号，无新增对应疑点。Q113继续未决。

至此2.1概述的符号定义和8个编号式已全部对照，Q113—Q116未解决。2.2详论仍待本轮校订，不能据概述替代原页核验。
''',encoding='utf-8')
q='''\n\n## Q116：3.2式2.7前后缺少路径因子（待核验）

PDF p3末—p4首。原前两行外部为tₘ′₁b₀，行向量[1,γ]、(E−X′)逆矩阵及(1,0)列向量乘积为1/Z；末行另含atₘₘ′。候选为前两行补入该因子或另核末行路径，未采用。正文完整三行照原页，不纳入已确认勘误。关联Q113的b₀定义。B234登记。
'''
questions=root/'翻译管理/疑难与勘误.md'
questions.write_text(questions.read_text(encoding='utf-8')+q,encoding='utf-8')
card=p/'局部约定卡.md'
card.write_text(card.read_text(encoding='utf-8')+'\n- B234：2.7前后atₘₘ′差异记Q116；2.8保留总负号与b₀b。2.1全部页面对照完成，Q113—Q116未决，不据候选反向改写。\n',encoding='utf-8')
structure=p/'结构与复用核验表.md'
t=structure.read_text(encoding='utf-8').replace('| m层E−源，p3—4，式2.7—2.8 | 旧译待核 | 下一批B234 |','| m层E−源，p3—4，式2.7—2.8 | 已对照原页；Q116未决；2.1全部覆盖 | B234 |')
structure.write_text(t,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'
t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B234完成3.2内2.1全部内容（2026-10-20）\n\n已核跨p3—4的m层E−源式2.7—2.8，各三行完整保留；修复旧译矩阵次序及漏行。2.7前后atₘₘ′差异记Q116，保留原式。至此2.1符号定义、四矩阵、Z及8个编号式均已核，Q113—Q116未决，未采用原文修正。\n\n下一批B235：p4的2.2详论引言、路径分类和式2.9—2.10；核反转次数、x/x′及y/y′标记与αβγ，不用概述替代逐页核验。2.2起仍为旧译待核。以下为历史记录。\n',1)
progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'
t=nav.read_text(encoding='utf-8').replace('下一批核E−源式2.7—2.8。','B234已核E−源式2.7—2.8，2.1全部覆盖（Q113—Q116未决）；下一批进入2.2详论。')
nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'
t=listing.read_text(encoding='utf-8').replace('本轮校订中：B228—B233已核第1部分、2.1定义及式2.1—2.6；式2.7起待核','本轮校订中：B228—B234已核第1部分与2.1全部；2.2详论待核')
listing.write_text(t,encoding='utf-8')
print(json.dumps(record,ensure_ascii=False))

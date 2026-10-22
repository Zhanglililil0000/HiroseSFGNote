from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent; root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8'); start=s.index('<!-- B234止；'); end=s.index('因此，若将经过',start)
batch=r'''### 2.2 详论

考察光即将出射到外部之前的电场振幅。

#### $m'$层中深度$z_1$处产生的和频光

光的路径在来自介质1的光于介质2的界面发生反射、折射时出现分支选择。恰当地计入这种选择，并考虑使$E^+$反转为$E^-$的反射次数增加，便可求得所需的表达式。

按照所产生的光最初到达$m'/m$界面时的行为分类。对于在$m'/m$界面反射的情形，再增加一次反转时衍生出的路径可写为：

$$
\begin{aligned}
xr_{m'm}y
&\Rightarrow xr_{m'm}r_{m'1}a^2r_{m'm}y
=xr_{m'm}\alpha y,\\
xt_{m'm}r_{m2}t_{mm'}r_{m'1}a^2b^2r_{m'm}y
&=xt_{m'm}\alpha[r_{m2}t_{mm'}b^2]y.
\end{aligned}
\tag{2.9}
$$

对于透过$m'/m$界面、在$m/2$界面反射的情形，再增加一次反转时衍生出的路径可写为：

$$
\begin{aligned}
x't_{m'm}y'
&\Rightarrow xr_{m'm}r_{m'1}a^2t_{m'm}y'\\
&=xr_{m'm}[r_{m'1}a^2t_{m'm}]y',\\
xt_{m'm}r_{m2}t_{mm'}r_{m'1}a^2b^2t_{m'm}y'
&=xt_{m'm}\beta y',\\
xt_{m'm}r_{m2}r_{mm'}b^2y'
&=xt_{m'm}\gamma y'.
\end{aligned}
\tag{2.10}
$$

（先参照下文的具体例子，可能更容易理解。）

> **译者注（局部记号与原文疑点Q117，PDF p4）：** 这里的$x$、$x'$、$y$、$y'$用于光路因子的组织，不按坐标分量解读。式(2.10)箭头左端原印$x'$，箭头右端及后续各支写$x$，本段未说明二者关系，此处保留差异。候选为同一前置因子的记号统一，但应结合后续递推定义核验，未采用。式(2.9)—(2.10)内的$\alpha$、$\beta$、$\gamma$沿用2.1的多重反射组合定义。

'''
(p/'B235-本批译文.md').write_text(batch,encoding='utf-8')
s=s[:start]+batch+'<!-- B235止；以下为旧译待核 -->\n\n> **校订状态：** 以下从$n$次至$(n+1)$次反转的递推关系起仍待本轮逐页校订。\n\n'+s[end:]
s=s.replace('B228—B234已核第1部分及2.1全部内容（式2.1—2.8）；2.2详论起仍为旧译待核。','B228—B235已核第1部分、2.1全部及2.2开篇至式(2.10)；其后递推关系起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
rec=dict(batch='B235',date='2026-10-20',pages=[4],tags=['2.9','2.10'],units='2.2详论引言、m′层源两类路径及2+3条路径关系',source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,unresolved=['Q117'],next='B236：p4—5反转次数递推及矩阵重新组合，接全跨页关系')
(p/'B235-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B235.md').write_text('''# B235 校订记录

核PDF p4的2.2开篇、m′层源路径选择说明、式2.9的两条关系和2.10的三条关系及括注。完整保留各路径中的r/t方向、a²/b²、x/x′与y/y′。原编号按完整组归并，2.10首条仅分行；未省略路径。

按2.1定义代入αβγ可核各等号后的因子组合；箭头表示路径派生，不作为同一路径的代数等号。x′至x的未说明记号差异记Q117，正文原样保留并注，不擅自统一。无原文修正采用。下一批从n次反转的电场与n+1递推接起，跨p4—5接完整矩阵关系。
''',encoding='utf-8')
q='''\n\n## Q117：3.2式2.10路径前置因子的撇号（待核验）

PDF p4，2.2路径分类。式2.10首条箭头左侧为x′tₘ′ₘy′，箭头右侧及其余支为x；本段未说明x与x′关系。保留原记号，候选为前置因子统一，须结合后续递推语境核验。箭头为路径派生，不据代数相等擅自改写。正文已注，未采用原文修正，不新增已确认勘误。B235登记。
'''
questions=root/'翻译管理/疑难与勘误.md'; questions.write_text(questions.read_text(encoding='utf-8')+q,encoding='utf-8')
card=p/'局部约定卡.md'; card.write_text(card.read_text(encoding='utf-8')+'\n- B235：2.2以E+转为E−的反射次数组织光路；箭头表示派生路径。x/x′、y/y′作为路径因子阅读，不能当作坐标分量；x′与x关系本段未明，记Q117。\n',encoding='utf-8')
structure=p/'结构与复用核验表.md'; t=structure.read_text(encoding='utf-8').replace('| 2.2详论，p4—13 | 旧译待核 | 待分批 |','| 2.2开篇与路径分类，p4，式2.9—2.10 | 已对照原页；Q117未决 | B235 |\n| 2.2递推关系及后文，p4—13 | 旧译待核 | 下一批B236起 |'); structure.write_text(t,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'; t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B235完成3.2式2.9—2.10（2026-10-20）\n\n已核p4的2.2引言、m′层源路径分类，两式分别保留2条和3条路径关系。x′至x的记号差异登记Q117，保留原式；无原文修正采用。\n\n下一批B236：从p4的n次反转电场及(n+1)递推开始，接p5的矩阵重组；核非对角元素、αβγ与路径因子的对应，不跨页截断完整关系。其后仍为旧译待核。以下为历史记录。\n',1); progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'; t=nav.read_text(encoding='utf-8').replace('下一批进入2.2详论。','B235已核2.2开篇与式2.9—2.10（Q117待核）；下一批接反转次数递推。'); nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'; t=listing.read_text(encoding='utf-8').replace('本轮校订中：B228—B234已核第1部分与2.1全部；2.2详论待核','本轮校订中：B228—B235已核至2.2式2.10；递推关系及后文待核'); listing.write_text(t,encoding='utf-8')
print(json.dumps(rec,ensure_ascii=False))

from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent; root=p.parents[2]
f=root/'中文版本/第四章 单层膜与多层膜的和频/4.1 CH、CH₂、CH₃基团CH伸缩振动的和频极化率.md'
s=f.read_text(encoding='utf-8'); start=s.index('<!-- B249止；'); end=s.index('**（反对称伸缩模式',start)
batch=r'''### CH₂基

沿HCH夹角的角平分线，从C原子指向两个H原子中点的方向取$c$轴，在HCH平面内取$a$轴。（$c$轴垂直于HCH平面。）

> **译者注（原文疑点Q122，PDF p2）：** 原文先将$c$轴定义为HCH夹角的角平分线，随后又称$c$轴垂直于HCH平面，二者不一致。此处均按原文保留；候选为末句的$c$应为$b$，须结合后续坐标变换和张量定义核验，尚未采用。旧译另行混淆了$a$、$c$方向，现已恢复底本的两句描述，不将候选写为确定约定。

设HCH夹角为$\alpha$。

#### 对称伸缩振动：$a_1$模式

$$
\begin{aligned}
\beta_{ccc}
&=2G_{a1}\left[\frac{(1+r)+(1-r)\cos\alpha}{2}\cos(\alpha/2)\right]
\beta_0(Q_{a1}^2)_{v+1,v},\\
\beta_{aac}
&=2G_{a1}\left[\frac{(1+r)-(1-r)\cos\alpha}{2}\cos(\alpha/2)\right]
\beta_0(Q_{a1}^2)_{v+1,v},\\
\beta_{bbc}
&=2G_{a1}[r\cos(\alpha/2)]\beta_0(Q_{a1}^2)_{v+1,v}.
\end{aligned}
\tag{0.3}
$$

$$
G_{a1}=\frac{1+\cos\alpha}{m_C}+\frac{1}{m_H}
=\frac{m_C+m_H(1+\cos\alpha)}{m_Cm_H}
$$

对于亚甲基（$\alpha=109.5^\circ$）：

$$
G_{a1}=(3m_C+2m_H)/(3m_Cm_H)
=\frac{1}{m_H}+\frac{2}{3}\frac{1}{m_C}
$$

对于乙烯基CH₂（$\alpha=120^\circ$）：

$$
G_{a1}=(2m_C+m_H)/(2m_Cm_H)
=\frac{1}{m_H}+\frac{1}{2}\frac{1}{m_C}
$$

$$
(Q_{a1}^2)_{v+1,v}
\equiv[\langle v+1|Q_{a1}|v\rangle]^2
=\frac{h}{2\pi c\omega_{a1}}(v+1)
$$

参见退偏比：

$$
\rho=\frac{3}{4}\frac{1}{1+\frac{15}{2}\left(\frac{1+2r}{1-r}\right)^2}
$$

> **译者注（记号与转录）：** 本段$\alpha$表示HCH夹角，须与前文带分量下标的分子极化率张量$\alpha$区分；$a_1$是模式标记。式(0.3)的前因子按底本为$2G_{a1}$，旧译的$\sqrt{2}$和空分母已修复，$\beta$也恢复为希腊字母。退偏比中的分量比按底本为$r$，旧译误作$\rho$已修复；$15/2$与前面CH基的$5/4$分别保留。矩阵元平方表达式也按本模式原式保留，不用CH基式中的$1/2$统一替换。原文角度值及等号照录，$109.5^\circ$为所列亚甲基角度的近似值。

'''
(p/'B250-本批译文.md').write_text(batch,encoding='utf-8')
s=s[:start]+batch+'<!-- B250止；以下为旧译待核 -->\n\n> **校订状态：** 以下从CH₂反对称伸缩式(0.4)起仍为旧译待核。\n\n'+s[end:]
s=s.replace('B249已核原目录、要点中CH基部分及p2开头续文；CH₂基起仍为旧译待核。','B249—B250已核原目录、CH基要点及CH₂对称伸缩式(0.3)与相关关系；式(0.4)起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
rec=dict(batch='B250',date='2026-10-20',pages=[2],tags=['0.3'],scope='CH₂坐标、a1对称伸缩三分量、Ga1通式及两种角度、矩阵元平方和退偏比',source_sha256=hashlib.sha256((root/'日语原版/Chapter4/chap4-1.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,unresolved=['Q122'],next='B251：p2反对称伸缩0.4、Gb1及矩阵元平方；核额外字形，完整接IR强度比')
(p/'B250-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B250.md').write_text('''# B250 校订记录

对照PDF p2的CH₂坐标与对称伸缩完整单元。核0.3三个分量的2Ga1、分母2、±cosα与cos(α/2)、β₀及Q平方；核Ga1通式、两种角度质量关系、矩阵元及15/2退偏比。旧译√2、空分母、b/β、夹角a/α及退偏比r/ρ均按原页修复，非原文修正。

原坐标两句对c轴的定义矛盾登记Q122，保留原文，候选末句b轴未采用。109.5度及原等号保留，不将圆整角度的代入当成精确三角恒等式。模式间矩阵元因子差异原样保留，待后文归一化核验。无原文公式修正采用。
''',encoding='utf-8')
q='''\n\n## Q122：4.1要点CH₂坐标的c轴描述矛盾（待核验）

位置：PDF p2，CH₂基开篇。原文先沿HCH角平分线从C指向两H中点取c轴、在HCH平面内取a轴，随后却称c轴垂直HCH平面。正文两句均照译；候选末句c轴应为b轴，须结合后文坐标变换及张量定义核验，尚未采用。旧译自加的a/c互换已按底本清除，属于译文修复。未采用原文修正，不增已确认勘误。B250登记。
'''
questions=root/'翻译管理/疑难与勘误.md'; questions.write_text(questions.read_text(encoding='utf-8')+q,encoding='utf-8')
card=p/'局部约定卡.md'; card.write_text(card.read_text(encoding='utf-8')+'\n- B250：CH₂原c轴两句矛盾记Q122，候选b不采用。夹角用α，模式a1；0.3前因子2Ga1按底本，不沿旧译√2。r与退偏比ρ不可混同；a1模式Q平方与CH模式的1/2因子差异保留待归一化核验。\n',encoding='utf-8')
structure=p/'结构与复用核验表.md'; t=structure.read_text(encoding='utf-8').replace('| CH₂要点起及其后正文、附录 | 旧译待核；不得直接复用公式状态 | B250起 |','| CH₂坐标与对称伸缩0.3、Ga1及相关关系 | 已核p2；Q122未决 | B250 |\n| CH₂反对称0.4起及其后正文、附录 | 旧译待核；不得直接复用公式状态 | B251起 |'); structure.write_text(t,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'; t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B250完成4.1的CH₂对称伸缩要点（2026-10-20）\n\n已核p2坐标定义、0.3三分量、Ga1及两种角度质量关系、矩阵元平方和退偏比。修复旧译√2、空分母、r/ρ等转录错误。原c轴描述矛盾记Q122，候选b轴未采用。无原文修正采用。\n\n下一批B251：p2反对称伸缩0.4、Gb1和矩阵元平方，核原页额外字形及IR强度比；不沿用旧译√2。0.4起仍为旧译待核。以下为历史记录。\n',1); progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md'; t=nav.read_text(encoding='utf-8').replace('CH₂起尚待本轮校订。','B250已核CH₂对称伸缩0.3及相关关系（Q122未决）；0.4起尚待本轮校订。'); nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'; t=listing.read_text(encoding='utf-8').replace('B249已核开篇、目录及CH基要点；CH₂起待核','B249—B250已核开篇、CH基与CH₂对称伸缩要点；0.4起待核').replace('已核0.1a/b、0.2及相关无编号关系；其余待核','已核0.1a/b、0.2、0.3及相关无编号关系；其余待核'); listing.write_text(t,encoding='utf-8')
print(json.dumps(rec,ensure_ascii=False))

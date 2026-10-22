from pathlib import Path
import json,hashlib,re
p=Path(__file__).resolve().parent; root=p.parents[2]
f=root/'中文版本/第四章 单层膜与多层膜的和频/4.1 CH、CH₂、CH₃基团CH伸缩振动的和频极化率.md'
s=f.read_text(encoding='utf-8'); (p/'B249前旧译.md').write_text(s,encoding='utf-8')
end=s.index('## 1. 振动偶极矩')
intro=r'''# 4.1 CH、CH₂、CH₃基团CH伸缩振动的和频极化率

> 原作：广瀬千秋（广濑千秋）
> 中文翻译：章力；本轮校订日期：2026-10-20。
> 底本：`日语原版/Chapter4/chap4-1.pdf`，共33页。B249已核原目录、要点中CH基部分及p2开头续文；CH₂基起仍为旧译待核。

## 原文目录

| 内容 | 原目录页码 |
|---|---|
| 要点 | 1 |
| 1. 振动偶极矩、拉曼张量、和频张量 | 4 |
| 第1部分：振动偶极矩 | 6 |
| 第1部分：拉曼张量 | 7 |
| 第1部分：和频张量 | 13 |
| 2. 振动坐标的矩阵元 | 14 |
| 3. 近似的检验之一：振动频率及光谱强度 | 16 |
| 4. 近似的检验之二：拉曼光谱强度与退偏比 | 18 |
| 附录1：谐振子与矩阵元 | 22 |
| 附录2：内部正交坐标、内坐标、对称坐标、简正坐标 | 24 |
| 附录3：GF矩阵法 | 28 |
| 附录4：CH₃基团的C₃ᵥ对称性破缺时的处理 | 31 |

> **译者注（目录定位）：** 原目录附录4页码保留为31；实际标题从PDF p30下部开始。以上为原目录的翻译及页面定位，后续正文尚须分批对照，不能据目录将整节视为已核验。

## 要点

考虑CH键的伸缩振动，取CH键轴为$c$轴。CH键的偶极矩只有$c$轴分量$\mu_c$；分子极化率张量$\alpha$除$c$轴分量$\alpha_{cc}$外，还具有$a$轴和$b$轴分量，即垂直于CH键轴的分量，并有$\alpha_{aa}=\alpha_{bb}$。设可写成$\alpha_{aa}=r\alpha_{cc}$，将$\mu_c$、$\alpha_{cc}$和$\alpha_{aa}$对CH键的伸缩振动坐标$r_{\mathrm{CH}}$作泰勒展开，并将其一阶导数系数的乘积定义为：

$$
\beta_0=
\left(\frac{\partial\alpha_{cc}}{\partial r_{\mathrm{CH}}}\right)_0
\left(\frac{\partial\mu_c}{\partial r_{\mathrm{CH}}}\right)_0
\tag{0.1a}
$$

$$
r\beta_0=
\left(\frac{\partial\alpha_{aa}}{\partial r_{\mathrm{CH}}}\right)_0
\left(\frac{\partial\mu_c}{\partial r_{\mathrm{CH}}}\right)_0
\tag{0.1b}
$$

将CH₂基和CH₃基视为若干CH键在一点相连，并采用下列假设：（1）作为简正振动的CH伸缩模式不包含HCH弯曲等其他内振动坐标，即高频隔离（high-frequency isolation）是良好近似；（2）在一点相连也不会使CH键周围的电子云产生显著畸变。在这些条件下，各基团CH伸缩模式的和频张量满足下列关系。（正文也给出了在考虑成键使CH键周围轴对称性破缺时仍可适用的推导。）

以下表达式对振动采用算符形式。

### CH基（取CH键轴为$c$轴）

$$
\begin{aligned}
\beta_{ccc}&=G_{\mathrm{CH}}\beta_0(Q_{\mathrm{CH}}^2)_{v+1,v},\\
\beta_{aac}=\beta_{bbc}&=G_{\mathrm{CH}}r\beta_0(Q_{\mathrm{CH}}^2)_{v+1,v}.
\end{aligned}
\tag{0.2}
$$

$$
G_{\mathrm{CH}}=\frac{1}{m_C}+\frac{1}{m_H}
=\frac{m_C+m_H}{m_Cm_H}
$$

$$
(Q_{\mathrm{CH}}^2)_{v+1,v}
\equiv[\langle v+1|Q_{\mathrm{CH}}|v\rangle]^2
=\frac{h}{2\pi c\omega_{\mathrm{CH}}}\frac{v+1}{2}
$$

$$
r=\alpha_{aa}/\alpha_{cc},\qquad
\left(\text{参见退偏比：}\quad
\rho=\frac{3}{4}\frac{1}{1+\frac{5}{4}\left(\frac{1+2r}{1-r}\right)^2}\right)
$$

像vinyl-CH那样，CH基相对于分子轴倾斜时，需要作相应的坐标变换。

> **译者注（局部符号）：** $\alpha$在这里为分子极化率（线性场响应），$\beta$为一阶超极化率（二阶场响应），不是拉丁字母$b$。$\beta_0$按作者的导数乘积定义保留，不补入其他章节的频率分母或归一化因子。$r$是分子极化率分量比，$r_{\mathrm{CH}}$是伸缩坐标，二者不可混同。$(Q_{\mathrm{CH}}^2)_{v+1,v}$在本页明确指跃迁矩阵元的平方，不擅自改读为平方算符$Q_{\mathrm{CH}}^2$的非对角矩阵元。$\omega_{\mathrm{CH}}$与$c$的原组合保留，具体频率单位约定待后文定义核验。

'''
(p/'B249-本批译文.md').write_text(intro,encoding='utf-8')
tail=s[end:].replace('## 1. 振动偶极矩与极化率、SFG强度\n\n### CH2分析','### CH₂基（旧译待核）',1)
f.write_text(intro+'<!-- B249止；以下为旧译待核 -->\n\n> **校订状态：** 以下从要点中的CH₂基起仍为旧译，标题、公式及正文尚待逐页校订。\n\n'+tail,encoding='utf-8')
rec=dict(batch='B249',date='2026-10-20',pages=[1,2],tags=['0.1a','0.1b','0.2'],scope='原题、12条目录、两项近似、CH基公式组及p2开头r/退偏比和倾斜说明',source_sha256=hashlib.sha256((root/'日语原版/Chapter4/chap4-1.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,next='B250：p2的CH₂坐标、对称伸缩式0.3及Ga1；先核坐标矛盾，保留原约定')
(p/'B249-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B249.md').write_text('''# B249 校订记录

核p1与p2开头；原目录附录4定位另核p30。旧目录漏项并误将正文近似检验列为附录，已完整恢复12条原目录与页码。附录4实际p30开始，原目录31保留并说明。

旧译将CH₂/CH₃两项近似误写为孤立CH模式且漏掉成键电子云假设，现忠实重译；删除旧译自行增加的无力学相互作用说明。β被转为拉丁b，恢复原希腊字母，含β₀与三分量。0.2作为完整两行同编号；G与矩阵元平方照录。补回p2开头r、退偏比公式（5/4系数）与vinyl-CH坐标变换句。无原文修正采用。

CH₂起未修改旧公式和坐标说明，仅清楚标为待核。其c轴前后定义存在疑问，下一批逐项核验，不根据旧译统一。未将结构初查当作全33页校订。
''',encoding='utf-8')
(p/'局部约定卡.md').write_text('''# 4.1 局部约定卡

- B249：CH键轴为c；αaa=αbb，αaa=rαcc。α为分子极化率，β为一阶超极化率（二阶场响应），β₀定义为导数乘积。r与rCH必须区分。
- 原(QCH²)v+1,v明确定义为跃迁矩阵元的平方，不按平方算符矩阵元另读。
- 原h/(2πcωCH)及(v+1)/2保留，频率/波数单位、简正坐标质量归一化须随后文核验，不继承第三章。
- high-frequency isolation译“高频隔离”，与成键不显著扭曲电子云为两项独立近似，不扩大为所有CH键无力学相互作用。
- 待核：CH₂坐标前后矛盾、夹角α与张量α的区分、简正坐标及GF质量因子；原未定义者不补定。
''',encoding='utf-8')
(p/'结构与复用核验表.md').write_text('''# 4.1 结构与复用核验表

底本33页。目录与文本层初查：要点p1—3；第1部分p4—13；第2部分p14—15；第3部分p16—17；第4部分p18—21；附录1 p22—23；附录2 p24—27；附录3 p28—30前部；附录4 p30后部—33。原目录末项列p31，实际p30标题已视觉核验；其余页界仍随批次复核。

| 单元 | 状态 | 批次 |
|---|---|---|
| 原题与12项目录 | 已核p1；附录4起点核p30 | B249 |
| 要点两项近似、CH基0.1a/b与0.2、p2起r与退偏比 | 已核 | B249 |
| CH₂要点起及其后正文、附录 | 旧译待核；不得直接复用公式状态 | B250起 |

旧译快照留存B249前旧译.md。首批发现目录错位、假设误译、β转写和漏译，后续以原页重新核验。
''',encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'; t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B249开始4.1（2026-10-20）\n\n已核p1原题、12条目录、两项近似、CH基0.1a/b与0.2及p2开头r/退偏比和倾斜说明。修复旧译近似假设、β转写及漏译；结构初查和局部约定卡已建。原目录附录4列31，实际p30开始，保留原值并说明。无原文修正采用。\n\n下一批B250：p2要点CH₂坐标定义、对称伸缩式0.3及Ga1；先核c轴前后描述矛盾，保留原文并注明候选，不据旧译统一。CH₂起仍为旧译待核。以下为历史记录。\n',1); progress.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'; lines=listing.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    if line.startswith('4.1\t'):
        c=line.split('\t'); c[2]='CH、CH₂、CH₃基团CH伸缩振动的和频极化率'; c[7]='B249已核开篇、目录及CH基要点；CH₂起待核'; c[8]='p1及p2开头已对照；附录4起点p30已核'; c[9]='已核0.1a/b、0.2及相关无编号关系；其余待核'; lines[i]='\t'.join(c)
listing.write_text('\n'.join(lines)+'\n',encoding='utf-8')
nav=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md'
if not nav.exists():
    nav.write_text('# 第四章阅读导航\n\n## 4.1 CH、CH₂、CH₃基团CH伸缩振动的和频极化率\n\n[进入4.1](4.1%20CH、CH₂、CH₃基团CH伸缩振动的和频极化率.md)。共33页，B249已核目录、两项近似与CH基要点（p1—2开头）；CH₂起尚待本轮校订。先区分分子极化率α、一阶超极化率β、r分量比与rCH伸缩坐标。其余小节仍待逐页校订，不据旧译标题判定主题。\n',encoding='utf-8')
renderer=(root/'翻译管理/校订记录/3.2/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/3.2','校订记录/4.1').replace('第三章 双层膜的和频','第四章 单层膜与多层膜的和频').replace("startsWith('3.2 ')","startsWith('4.1 ')")
(p/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print(json.dumps(rec,ensure_ascii=False))

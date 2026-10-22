from pathlib import Path
import re,json,hashlib
p=Path(__file__).resolve().parent
root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8')
start=s.index('<!-- B228止；')
coeffstart=s.index('对于介质 1 与层叠薄膜')
end=s.index('\n---\n',coeffstart)
coeff=s[coeffstart:end]
intro=r'''### L系数与电场振幅

L系数将极化与由该极化产生的光的电场振幅联系起来：

$$
E_{\mathrm{SF},\alpha}=\sum_{\beta}L_{\alpha\beta}P^{\mathrm{SF}}_{\beta}
$$

根据广义斯涅耳折射公式，所产生的和频光既有向上的（$-$），也有向下的（$+$）。此外，L系数的表达式随极化所在位置而异。最初导出的公式考虑无限薄的膜$m$发生极化，以及由此向介质1和介质2射出的光，将$s$、$p$偏振的电场振幅与极化的$x$、$y$、$z$分量联系起来；这里将其推广。另外，省略公共因子$4\pi i\omega_{\mathrm{SF}}/c$（用波矢代替折射率时，为$4\pi i\omega_{\mathrm{SF}}^2/c^2$）。

L系数的记法为$L_{i/j,s(p),\alpha}$：当极化薄片$m'$夹在$i$层与$j$层之间时，它表示极化的$\alpha$分量（$\alpha=x,y,z$）与其所产生光的$s$或$p$偏振分量之间的系数。向上（$-$）与向下（$+$）的光分别以上标$-$和$+$区分。

> **译者注（局部约定）：** 此处L连接极化分量与辐射场偏振分量；上下标顺序与前式$L_{\alpha\beta}$的抽象分量记法应结合各自定义阅读。下列折射率比按原文不补SF下标，$m'$、$m''$是各界面极化薄片的标记，不自行等同于下一部分中的有限厚度膜层。所省略的公共因子按本节原文保留。

'''
# 将双重等式排为两行，完整保留两种写法及所有系数。
def wrap(m):
    tex=m.group(1).strip()
    if '\n= ' in tex:
        a,b=tex.split('\n= ',1)
        lhs,rhs=a.split(' = ',1)
        tex='\\begin{aligned}\n'+lhs+' & = '+rhs+' \\\\\n& = '+b+'\n\\end{aligned}'
    return '$$\n'+tex+'\n$$'
coeff=re.sub(r'\$\$([\s\S]*?)\$\$',wrap,coeff)
coeff=coeff.replace('对于介质 1 与层叠薄膜 $m$ 之间的极化薄片 $m\'$ 的光产生：','对于介质1与层叠膜$m$之间的极化薄片$m\'$所产生的光：')
coeff=coeff.replace('对于介质 2 与层叠薄膜 $m$ 之间的极化薄片 $m\'\'$ 的光产生：','对于介质2与层叠膜$m$之间的极化薄片$m\'\'$所产生的光：')
coeff=coeff.replace('对于层叠薄膜内部的极化薄片的光产生：','对于层叠膜内部的极化薄片所产生的光：')
batch=intro+coeff+'\n'
(p/'B229-本批译文.md').write_text(batch,encoding='utf-8')
tail=s[end:].replace('\n---\n','',1).lstrip()
tail=tail.replace('### 2. 双层系 ($1/m\'/m/2$) 的 SFG','## 2. 二层系（$1/m\'/m/2$）的和频',1).replace('#### 2.1 概述','### 2.1 概述',1)
s=s[:start]+batch+'\n<!-- B229止；以下为旧译待核 -->\n\n> **校订状态：** 以下第2部分尚未完成本轮逐页校订。\n\n'+tail
s=s.replace('B228已核第1页开篇及反射、透射系数组；L系数起仍为旧译待核。','B228—B229已核第1—2页开篇及第1部分全部系数；第2部分起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
record=dict(batch='B229',date='2026-10-20',pages=[1,2],units='L定义、上下传播方向、省略公共因子、15组完整L系数',source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,next='B230：p2的2.1符号定义；逐项核a₀/b₀星号、a/b与αβγ、四矩阵及Z')
(p/'B229-覆盖.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B229.md').write_text('''# B229 校订记录

逐页核对p1—2的L定义、记法、15组L系数，覆盖1/m的6组、2/m的6组及膜内3组。核对x/y/z、正反方向、z分量负号、折射率比与平方等式、SF角度和分母。旧译此15组数学可复用；将四条双重等式分行并保留两种完整写法。抽象定义的E下标恢复为底本的SF,α记法，属旧译转录调整。

原文省略公共因子及未带频率下标的折射率比保持不变。无原文公式修正采用，无新增已确认勘误。完成第1部分，不将第2部分旧译标为已核。
''',encoding='utf-8')
card=p/'局部约定卡.md'
t=card.read_text(encoding='utf-8').replace('- 待核：L的方向、公共因子与界面薄片标记；','- B229已核：L将极化分量连接至辐射场s/p分量，−向上、+向下；省略4πiωSF/c（改用波矢时4πiωSF²/c²）。界面极化薄片标记m′、m″随位置阅读；原折射率比不擅自补频率下标。膜内x/y分量上下同号、z分量反号。\n- 待核：')
card.write_text(t,encoding='utf-8')
structure=p/'结构与复用核验表.md'
t=structure.read_text(encoding='utf-8').replace('| L定义与完整系数组，p1—2 | 旧译待核 | 下一批B229 |','| L定义与完整15组系数，p1—2 | 已对照原页 | B229 |')
structure.write_text(t,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'
t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B229完成3.2第1部分（2026-10-20）\n\n已核p1—2的L定义、方向、公共因子及15组系数；加上B228，第1部分全部完成。保留完整折射率比两种等式，未采用原文公式修正，无新增已确认勘误。\n\n下一批B230：从p2的2.1符号定义开始，核a₀/b₀及星号非共轭约定、a/b与αβγ、X/X′/Y/Y′及Z；不直接继承3.1符号含义。第2部分仍为旧译待核。以下为历史记录。\n',1)
progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'
t=nav.read_text(encoding='utf-8').replace('B228已核原题、引言及p1反射/透射关系。L系数起仍待校订，下一批核其定义与完整系数组。','B228—B229已核原题、引言及第1部分全部系数（p1—2）。第2部分仍待校订，下一批核2.1的相位与矩阵定义。')
nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'
t=listing.read_text(encoding='utf-8').replace('本轮校订中：B228已核开篇与p1反射/透射关系；其余待核','本轮校订中：B228—B229已核开篇与第1部分全部系数；第2部分待核')
listing.write_text(t,encoding='utf-8')
print('B229写入完成；15组L关系及定义')

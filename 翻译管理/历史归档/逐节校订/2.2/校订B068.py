from pathlib import Path
import csv,io
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'));s=p.read_text(encoding='utf-8')
start=s.index('#### 4.1c.');end=s.index('#### 4.1d.',start);tail=s[end:]
part=r'''#### 4.1c. $1/m/2$ 体系中 $1/m$ 界面介质1侧的激发电场

本小节讨论稀疏吸附分子所感受到的电场。所考察的源点为

$$
x=-2nh_m\tan\theta_{m,\mathrm{SF}},\qquad z=0^-.
$$

在界面位置 $x=-2nh_m\tan\theta_{m,\mathrm{SF}}$、$z=0$ 处，将入射光、反射光以及从膜内出射的光相加，得到：

$$
\begin{aligned}
E_{\mathrm{vis},\alpha}(0^-)
={}&E^0_{\mathrm{vis},\alpha}
\frac{(1+r_{1m,\mathrm{vis},\alpha})
(1+r_{m2,\mathrm{visr},\alpha}e^{2i\beta_{m,\mathrm{vis}}h_m})}
{1+r_{1m,\mathrm{vis},\alpha}r_{m2,\mathrm{visr},\alpha}e^{2i\beta_{m,\mathrm{vis}}h_m}}\\
&\times\exp\!\bigl[-ik_{m,\mathrm{vis}}\,2nh_m
\tan\theta_{m,\mathrm{SF}}\sin\theta_{m,\mathrm{vis}}\bigr].
\end{aligned}
\tag{4.7}
$$

> **译者注（原下标待核验 E-2.2-003；Q043）：** 底本第6页式（4.7）的分子、分母两处均写 $r_{m2,\mathrm{visr},\alpha}$。第4.1部分已定义的波长标记为 $\mathrm{ir},\mathrm{vis},\mathrm{SF}$，式（4.9）对应项又写 $\mathrm{vis}$；因此 $\mathrm{vis}$ 是候选读法，但尚未确认。旧译曾直接采用 $\mathrm{vis}$，本轮恢复底本的 $\mathrm{visr}$，仅在本注保留候选，不据此改动式（4.9）。

$$
\begin{aligned}
E_{\mathrm{ir},\beta}(0^-)
={}&E^0_{\mathrm{ir},\beta}
\frac{(1+r_{1m,\mathrm{ir},\beta})
(1+r_{m2,\mathrm{ir},\beta}e^{2i\beta_{m,\mathrm{ir}}h_m})}
{1+r_{1m,\mathrm{ir},\beta}r_{m2,\mathrm{ir},\beta}e^{2i\beta_{m,\mathrm{ir}}h_m}}\\
&\times\exp\!\bigl[-ik_{m,\mathrm{ir}}\,2nh_m
\tan\theta_{m,\mathrm{SF}}\sin\theta_{m,\mathrm{ir}}\bigr].
\end{aligned}
\tag{4.8}
$$

$$
\begin{aligned}
&E_{\mathrm{vis},\alpha}(0^-)E_{\mathrm{ir},\beta}(0^-)\\
&=E^0_{\mathrm{vis},\alpha}E^0_{\mathrm{ir},\beta}
\frac{\begin{aligned}
&(1+r_{1m,\mathrm{vis},\alpha})(1+r_{m2,\mathrm{vis},\alpha}e^{2i\beta_{m,\mathrm{vis}}h_m})\\
&\quad\times(1+r_{1m,\mathrm{ir},\beta})(1+r_{m2,\mathrm{ir},\beta}e^{2i\beta_{m,\mathrm{ir}}h_m})
\end{aligned}}
{\begin{aligned}
&(1+r_{1m,\mathrm{vis},\alpha}r_{m2,\mathrm{vis},\alpha}e^{2i\beta_{m,\mathrm{vis}}h_m})\\
&\quad\times(1+r_{1m,\mathrm{ir},\beta}r_{m2,\mathrm{ir},\beta}e^{2i\beta_{m,\mathrm{ir}}h_m})
\end{aligned}}\\[5pt]
&\quad\times\exp\!\Bigl[i\,2nh_m\tan\theta_{m,\mathrm{SF}}
\bigl(-k_{m,\mathrm{ir}}\sin\theta_{m,\mathrm{ir}}
-k_{m,\mathrm{vis}}\sin\theta_{m,\mathrm{vis}}\bigr)\Bigr].
\end{aligned}
\tag{4.9}
$$

> **译者注（相位与下标）：** $\theta_{m,\mathrm{SF}}$ 对应生成SFG光的源点横向位置，$k_{m,\mathrm{vis}}$、$k_{m,\mathrm{ir}}$ 及各自的入射角对应两束激发光，不能把三种角度直接合并。式（4.9）分子、分母内的两组因子仅为排版而分行，乘积关系不变；其中 $\alpha,\beta$ 是坐标方向，带 $m$ 和波长标记的 $\beta$ 则是传播参数。式（4.7）与式（4.9）的原下标差异仍见Q043，本轮未将两者视为已完成独立代数核验。

'''
s=s[:start]+part+tail
s=s.replace('当前完成B058—B067：序论、定义、式（2.1）—（2.6）、第3部分光路，以及第4部分开头至4.1b的分量约定和式（4.1）—（4.6）；**4.1c起仍为旧译待校订**。','当前完成B058—B068：序论、定义、式（2.1）—（2.6）、第3部分光路，以及第4部分开头至4.1c、式（4.1）—（4.9）；**4.1d起仍为旧译待校订**。')
p.write_text(s,encoding='utf-8');assert s[s.index('#### 4.1d.'):]==tail
(out/'B068-本批译文.md').write_text(part,encoding='utf-8')
(out/'B058-本批译文.md').write_text(s[:s.index('## 2. 准备')],encoding='utf-8')
(out/'B068.md').write_text('''# B068 校订记录

2026-10-19。范围：PDF p6下部，完整4.1c及式4.7—4.9。目视核对原文p6.png及B068-原式局部.png；修订前备份B068-修订前.md。

核对两波长的界面系数、往返相位、横向源点位移及场乘积；修复旧译裸数学和编号格式，保留0−侧别。底本4.7两处visr下标恢复，候选vis移入就地注和E-2.2-003/Q043；不将4.9改成visr，也不在未确认前把4.7、4.9统一。乘积长式仅作分行排版，没有增补物理条件。

4.1d起与本批备份相同；后续从p7式4.10—4.12的完整4.1d开始。
''',encoding='utf-8')
rp=out/'检查排版.cjs';t=rp.read_text(encoding='utf-8').replace("'B066','B067']","'B066','B067','B068']").replace('6[0-7]','6[0-8]');rp.write_text(t,encoding='utf-8')
q=mg/'疑难与勘误.md';t=q.read_text(encoding='utf-8');t+='\n| 编号 | 原文位置 | 疑点 | 类别/优先级 | 处理与状态 |\n|---|---|---|---|---|\n| Q043 | 2.2 PDF p6式4.7两处下标及4.9 | 4.7写visr，前文和4.9为vis | 原文下标/P2 | B068高分辨率确认原字；正文恢复visr，候选vis移注及附件E-2.2-003，未确认修正；4.9保持原式。 |\n';q.write_text(t,encoding='utf-8')
ep=root/'中文版本/附件/原文勘误表.md';t=ep.read_text(encoding='utf-8')
needle='## 后续维护';row='| E-2.2-003／Q043 | PDF第6页，式（4.7）分子、分母 | 两处反射系数下标为visr | 2026-10-19恢复visr；候选vis只列注释，式（4.9）照原文保留vis | 根据前文定义及式4.9提出候选，尚未确认、未用于正文。 |\n\n'
assert needle in t;t=t.replace(needle,row+needle);ep.write_text(t,encoding='utf-8')
card=out/'局部约定卡.md';t=card.read_text(encoding='utf-8');card.write_text(t+'\n## B068补充\n\n4.1c为1/m/2体系在1/m界面介质1侧，位置x=−2nh_m tanθ_m,SF、z=0−。源点坐标由SF方向给出，两束激发光相位分别用vis/ir的k与角度。4.7两处visr原下标保留，4.9的vis不改，见Q043。\n',encoding='utf-8')
pp=mg/'当前进度与续接.md';t=pp.read_text(encoding='utf-8');entry='''## 最新续接：2.2的B068完成（2026-10-19）

已目视核对p6下部完整4.1c（式4.7—4.9），恢复数学与原编号。高分辨率确认4.7分子/分母的visr，原下标恢复、候选vis移注，登记Q043及附件E-2.2-003；4.9仍按原文用vis。界面系数与两激发光/生成光角度区分，不据排版修复宣称原式已认证。

下一批从4.1d（p7，式4.10—4.12）开始，完整处理1/m界面薄膜侧，再按4.1e/f推进。4.1d起旧译与B068前备份相同；本节仍未完成。

''';pp.write_text(t.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
cp=mg/'章节清单.tsv';rows=list(csv.DictReader(io.StringIO(cp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['编号']=='2.2':row['状态']='处理中：B058—B068，已至4.1c末';row['映射核验']='p1—6截至4.1c；4.1d起未校订';row['公式图表范围']='式2.1—2.6、4.1—4.9、分量关系及第3部分图文已覆盖'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);cp.write_text(buf.getvalue(),encoding='utf-8-sig')
print('B068正文及管理已同步')

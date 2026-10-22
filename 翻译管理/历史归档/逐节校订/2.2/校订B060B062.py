from pathlib import Path
import re,csv,io
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');start=s.index('"反射光"中，除在1/m界面反射的光之外');end=s.index('## 3. SFG光的光路',start)
head=s[:start];tail=s[end:]
part=r'''“反射光”不仅包含在 $1/m$ 界面直接反射的光，还包括进入薄膜后经多重反射、再从 $1/m$ 界面出射的上行（−）光。应用 $1/m$ 界面处的边界条件时，须在界面两侧分别计入这些多重反射光。根据附录C，将入射光振幅取为1，反射光的电场振幅为：

$$
\begin{aligned}
\text{反射光电场振幅}
={}&r_{1m}+t_{1m}t_{m1}r_{m2}\sum_{n=0}^{\infty}(r_{m2}r_{m1})^n
\exp\!\left(i\frac{2\pi n_m\,2nh_m\cos\theta_m}{\lambda}\right)\\[5pt]
={}&r_{1m}+\frac{t_{1m}t_{m1}r_{m2}\exp\!\left(i\frac{2\pi n_m\,2h_m\cos\theta_m}{\lambda}\right)}
{1-r_{m2}r_{m1}\exp\!\left(i\frac{2\pi n_m\,2h_m\cos\theta_m}{\lambda}\right)}\\[5pt]
={}&\frac{r_{1m}+[-r_{1m}r_{m1}+t_{1m}t_{m1}]r_{m2}\exp\!\left(i\frac{2\pi n_m\,2h_m\cos\theta_m}{\lambda}\right)}
{1-r_{m2}r_{m1}\exp\!\left(i\frac{2\pi n_m\,2h_m\cos\theta_m}{\lambda}\right)}\\[5pt]
={}&\frac{r_{1m}+r_{m2}\exp\!\left(i\frac{2\pi n_m\,2h_m\cos\theta_m}{\lambda}\right)}
{1-r_{m2}r_{m1}\exp\!\left(i\frac{2\pi n_m\,2h_m\cos\theta_m}{\lambda}\right)}.
\end{aligned}
\tag{2.1}
$$

> **译者注（Q040）：** 底本第2页首行相位中的路程写为 $2nh_m$，这里恢复旧译漏掉的求和指标 $n$。但这一首行与下一行分子含一次往返相位因子的闭式，在起始相位上并未直接衔接；尚未确认应改动哪一处，故等式各行均保留原写法，不自行改为 $2(n+1)h_m$。

振幅绝对值的平方给出光强，因此反射光会随 $2n_mh_m\cos\theta_m/\lambda$ 呈现周期性干涉。原文给出的反射光强度为：

$$
\text{反射光强度}=1-
\frac{(1-r_{1m}^{2})(1-r_{m2}^{2})}
{\begin{aligned}
&1+\lvert r_{1m}r_{m2}\rvert^2
+(r_{1m}r_{m2}+r_{1m}^{*}r_{m2}^{*})\cos(2\beta_mh_m)\\
&\quad+i(r_{1m}r_{m2}-r_{1m}^{*}r_{m2}^{*})\sin(2\beta_mh_m)
\end{aligned}},
\qquad \beta_m\equiv\frac{2\pi n_m\cos\theta_m}{\lambda}.
\tag{2.2}
$$

当 $r_{1m}$、$r_{m2}$ 为实数时，原文称反射光在 $2n_mh_m\cos\theta_m/\lambda$ 为整数时取极大值，因此扫描波数时，相邻峰的间隔为 $\Delta\nu=1/(2n_mh_m\cos\theta_m)$。不过，薄膜存在吸收时 $r_{1m}$ 成为复数；介质2为金属时 $r_{2m}$ 成为复数，分母中的第二项也会起作用。

> **译者注（Q040续）：** 式（2.2）的分母首两项在底本为 $1+\lvert r_{1m}r_{m2}\rvert^2$，旧译的模号和幂次位置已按底本恢复；分子仍按原文写普通平方。上述复数情形下的适用条件、极大值与反射系数符号的关系、波数间隔中的色散假设及 $r_{2m}$ 下标的衔接，尚待独立核验，不因转录已修复就视为已验证的通用结论。此处 $\beta_m$ 是沿法线的相位参数，不是分子的一阶超极化率。

“透射光”除直接穿过薄膜的光之外，还叠加了进入膜内后经多重反射、再从 $m/2$ 界面出射的光。应用 $m/2$ 界面的边界条件时，应计入这些多重反射光。根据附录C，将入射光振幅取为1、相位取为 $e^{-i\omega t}$，透射光的电场振幅为：

$$
\begin{aligned}
&t_{1m}t_{m2}\sum_{n=0}^{\infty}(r_{m2}r_{m1})^n
\left[\exp\!\left(i\frac{2\pi n_m\,2h_m\cos\theta_m}{\lambda}\right)\right]^n
\exp\!\left(i\frac{2\pi n_mh_m\cos\theta_m}{\lambda}\right)\\[5pt]
&\quad=\frac{t_{1m}t_{m2}\exp\!\left(i\frac{2\pi n_mh_m\cos\theta_m}{\lambda}\right)}
{1-r_{m2}r_{m1}\exp\!\left(i\frac{2\pi n_m\,2h_m\cos\theta_m}{\lambda}\right)}.
\end{aligned}
\tag{2.3}
$$

透射光强度为：

$$
\text{透射光强度}=
\frac{\lvert t_{1m}\rvert^2\lvert t_{m2}\rvert^2}
{\begin{aligned}
&1+\lvert r_{1m}r_{m2}\rvert^2
+(r_{1m}r_{m2}+r_{1m}^{*}r_{m2}^{*})\cos(2\beta_mh_m)\\
&\quad+i(r_{1m}r_{m2}-r_{1m}^{*}r_{m2}^{*})\sin(2\beta_mh_m)
\end{aligned}}.
\tag{2.4}
$$

干涉引起的起伏与反射光相反：一方的峰顶位置对应另一方的谷底。

> **译者注（Q040，透射部分）：** 底本式（2.4）的分子为两个透射系数各自的模平方乘积，旧译误写的普通平方已恢复；分母模号亦已恢复。本段“光强度”与前后能流归一化、复折射率以及复相位的关系尚未完整说明，故不擅自给原式补入折射率或余弦的比值。上述峰谷关系按作者表述保留，不扩展到所有吸收与入射条件。

### 薄膜内部点 $(x,z)$ 处的光电场

设原点处的入射光电场为 $E_0e^{-i\omega t}$。如作者另备文件「膜内の電場」式（4.4）所述，薄膜只有一层时，点 $(x,z)$ 处上行（−）光的电场 $E^{-}$ 与上行（＋）光的电场 $E^{+}$ 表示如下。两层或三层薄膜的情况，参见该文件第4部分。

> **译者注（原方向名称待核验 E-2.2-002；Q041）：** 底本第3页在此将负、正两种光都称为「上向き」。按本节第2部分的定义及式（2.5）的传播方向，“＋”光的候选名称为“下行光”；旧译已采用该名称，本轮正文恢复原文“上行（＋）”，候选仅列于注释，不修改作者公式。

$$
\begin{aligned}
E_a^+={}&E_0e^{-i\omega t}\exp\!\bigl[ik_m(x\sin\theta_m+z\cos\theta_m)\bigr]\\
&\times\frac{t_{1m,a}}{1+r_{1m,a}r_{m2,a}e^{2i\beta_mh_m}}.
\end{aligned}
\tag{2.5}
$$

$$
\begin{aligned}
E_a^-={}&E_0e^{-i\omega t}\exp\!\bigl[ik_m(x\sin\theta_m-z\cos\theta_m)\bigr]\\
&\times\frac{t_{1m}r_{m2}e^{2i\beta_mh_m}}{1+r_{1m}r_{m2}e^{2i\beta_mh_m}}.
\end{aligned}
\tag{2.6}
$$

> **译者注（局部约定，Q041）：** 本段明确使用负时间因子；场的“＋／−”上标按本节上下行定义识别，不沿用第1.3节的辐射侧别标签。式（2.5）的 $r,t$ 带有 $a$ 下标，式（2.6）相应系数省略该下标，均按底本保留；这里只登记这种差异，不擅自在每项中补加下标，也不将 $a$ 解释为分子坐标轴。

'''
s=head+part+tail
s=s.replace('当前仅完成B058—B059：第1页序论及第1页末至第2页的坐标、符号定义；**式（2.1）起及其后内容仍为旧译待校订**。','当前完成B058—B062：序论、坐标定义及第2—3页的式（2.1）—（2.6）；**第3部分“SFG光的光路”起仍为旧译待校订**。')
p.write_text(s,encoding='utf-8')
assert s[s.index('## 3. SFG光的光路'):]==tail
cuts=[0,part.index('“透射光”'),part.index('### 薄膜内部'),len(part)]
scopes=['p2反射场式2.1/2.2及p3开头解释，跨页完整单元','p3透射场与强度式2.3/2.4','p3膜内场式2.5/2.6，止于第3部分前']
for j,(a,b) in enumerate(zip(cuts,cuts[1:]),60):
    bid=f'B{j:03}';(out/f'{bid}-本批译文.md').write_text(part[a:b],encoding='utf-8')
    (out/f'{bid}.md').write_text(f'# {bid} 校订记录\n\n2026-10-19。范围：{scopes[j-60]}。已目视核对底本原文p2.png、原文p3.png及高分辨率公式局部。修订前备份B060-修订前.md。修复模号、复共轭与n的转录；原文的相位衔接和方向名称疑点分别登记Q040/Q041，未擅改。数学渲染和实际宽度见本批截图与渲染检查.json。\n',encoding='utf-8')
# Refresh already-reviewed opening batch metadata, keeping the batch boundaries unchanged.
opening=s[:s.index('## 2. 准备')];definitions=s[s.index('## 2. 准备'):s.index('“反射光”不仅包含')]
(out/'B058-本批译文.md').write_text(opening,encoding='utf-8');(out/'B059-本批译文.md').write_text(definitions,encoding='utf-8')
q=mg/'疑难与勘误.md';t=q.read_text(encoding='utf-8');assert '| Q040 |' not in t
t+='\n| Q040 | 2.2 p2—3式2.1—2.4及干涉解释 | 首行相位求和与闭式的起始相位、复数强度和极值条件及归一化 | 原式关系/P1 | B060—B061恢复原文2nh_m及模平方，不补候选相位或能流权重；各等式与极值说法按底本加注，尚待独立核验。 |\n| Q041 | 2.2 p3式2.5/2.6前后 | 原文把+光也称上行；两式a下标有省略差异 | 原文方向名称/记号/P2 | B062恢复原称，候选下行移注及附件E-2.2-002；时间因子与方向登记，公式不改。 |\n'
q.write_text(t,encoding='utf-8')
ep=root/'中文版本/附件/原文勘误表.md';t=ep.read_text(encoding='utf-8')
oldrow='| E-2.2-001／Q039 | PDF第2页，r₂m定义 | 从介质2侧来，在1/m界面反射 | 2026-10-19正文恢复原界面名1/m；候选2/m移注 | 旧译曾采用候选，本轮恢复原文；候选未确认、未采用。 |'
assert oldrow in t
t=t.replace(oldrow,oldrow+'\n| E-2.2-002／Q041 | PDF第3页，式（2.5）前 | 正、负两种光均称「上向き」 | 正文恢复“上行（＋）”；候选“下行（＋）”移注 | 依据本节原定义提出候选，未确认、未用于正文；不改公式。 |')
ep.write_text(t,encoding='utf-8')
card=out/'局部约定卡.md';t=card.read_text(encoding='utf-8');t+='\n## B060—B062补充\n\n式2.2定义β_m=2π n_m cosθ_m/λ，是传播的法线相位参数，不是分子超极化率；相位中的小写n另为求和指标。式2.3、2.5/2.6明确使用exp(−iωt)。2.2分母模平方及2.4透射系数模平方均已按底本恢复；功率/能流归一化尚未独立确认。2.5/2.6偏振a下标写法依原文，原文“上行+”名称疑点见Q041。\n';card.write_text(t,encoding='utf-8')
# Renderer validates only completed batches, avoiding the untouched old-translation mathematics.
rp=out/'检查排版.cjs';t=rp.read_text(encoding='utf-8');t=t.replace("['B058','B059']","['B058','B059','B060','B061','B062']").replace('/^B05[89]-本批译文.md$/','/^B0(?:5[89]|6[0-2])-本批译文.md$/');rp.write_text(t,encoding='utf-8')
cp=mg/'章节清单.tsv';rows=list(csv.DictReader(io.StringIO(cp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['编号']=='2.2':row['状态']='处理中：B058—B062，序论、定义及式2.1—2.6已对照';row['映射核验']='p1—3截至式2.6及注释；第3部分起未校订';row['公式图表范围']='已核式2.1—2.6，后续编号式/图待校订'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);cp.write_text(buf.getvalue(),encoding='utf-8-sig')
pp=mg/'当前进度与续接.md';t=pp.read_text(encoding='utf-8');entry='''## 最新续接：2.2的B060—B062完成（2026-10-19）

已目视核对p2—3，完成反射/透射场与强度式（2.1）—（2.4）及膜内场式（2.5）、（2.6）；含跨页反射解释。旧译模号、模平方、首行相位n、公式编号与数学格式已修复。Q040原相位及强度关系未决；Q041“上行+”原称保留，候选下行入注及E-2.2-002，附件现13项。仅更新本批及已核开头元数据，未处理后文。

下一批从第3部分“SFG光的光路”起，跨p3—4核对源点分类及图3.1；不得只按p3页末切断(a)—(f)分类。第2.2节共47页，当前只覆盖序论至式2.6，尚未完成全节。

''';pp.write_text(t.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
print('B060—B062正文与管理已同步')

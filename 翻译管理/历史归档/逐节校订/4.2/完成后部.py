from 整节工具 import *
from 完成张量表 import table
angle=r'''以$\phi$表示$ac$面与$xz$面的角（内部旋转角），$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角，$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴的角（面内取向角），公式中使用的欧拉角为$\phi=\phi$、$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi+\chi_{\mathrm{ip}}$。
'''
def tables(s):
    a=s.index('**全对称模式**');b=s.index('**简并模式**',a)
    sym=table(s[a:b]);deg=table(s[b:])
    return r'''#### 全对称振动

在$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时，$\beta_{aac}\sim(4/9)\beta_{\zeta\zeta\zeta}$、$\beta_{ccc}\sim(1/9)\beta_{\zeta\zeta\zeta}$。
'''+sym+r'''
#### 简并振动

在$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时，$\beta_{caa}\sim(4/9)\beta_{\zeta\zeta\zeta}$、$\beta_{aaa}\sim(\sqrt{32}/9)\beta_{\zeta\zeta\zeta}$。
'''+deg

add(288,[12,13],r'''### 4d. 两个H原子等价时（内部旋转被冻结）

此时，内部旋转角为$\phi$的甲基，与$\phi+2\pi/3$及$\phi+4\pi/3\;(=\phi-2\pi/3)$的甲基相区别，张量也不同。（若认为甲基本身的张量相同，就会得到与第4c部分相同的表达式。）利用三角函数的求和关系，将两种配置的正弦、余弦用$\phi$表示后相加，得：

$$
\begin{aligned}
\sum1&=2,\\
\sum\sin\phi&=-\sin\phi,\qquad\sum\cos\phi=-\cos\phi,\\
\sum\sin2\phi&=-\sin2\phi,\qquad\sum\cos2\phi=-\cos2\phi,\\
\sum\sin3\phi&=2\sin3\phi,\qquad\sum\cos3\phi=2\cos3\phi.
\end{aligned}
$$

内部旋转角为$\phi$的甲基直接使用第4a部分的表达式；两个等价甲基则使用把上式代入第4a部分后的结果。原则上，对振动模式也需要考察其线性组合。只要两种甲基的性质没有很大差异，总张量就与第4c部分的结果相同。

## 5. 表面取向造成的和频张量差异

（以下叙述中使用的角$\chi$，是指以$\phi$表示$ac$面与$xz$面的角、$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角、$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴的角时的$\chi_{\mathrm{ip}}$。它们与张量分量表达式中所用欧拉角的关系为$\phi=\phi$、$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi+\chi_{\mathrm{ip}}$。）

甲基的面内取向用角$\chi$定义。将入射面与表面的交线沿光传播方向取为正方向，并以此交线与甲基$C_3$轴在表面上的投影之间的角作为取向角，就能导出解析测量数据所需的张量，也能考察和频信号随样品旋转的变化。若将$\chi$定义为表面固定轴——例如LB膜的提拉轴或晶轴——与甲基轴投影之间的角，则求得的是表面固有的张量分量。

不过，对于第5d部分的$C_s$对称情况，定义两个角更便于解释数据：一是入射面与表面的交线，相对于镜面对称面与表面交线（director）的角；二是甲基轴的投影相对于该镜面与表面交线的角。在$C_s$对称表面的和频实验中，入射面与对称面重合时，自由旋转甲基不产生(spp)、(psp)、(pps)、(sss)光；内部旋转冻结时，则仅对简并振动能观测到这些偏振的光。

以下考察代表性取向形式下的张量分量。为简便起见，假定甲基内部旋转冻结，但三个H等价，即第4c部分的情形。一个重要之处在于：如第5a部分所示，内部旋转停止时，三角锥的顶点朝向表面，还是其底边平行于表面，会使简并振动带的和频张量值有很大差异。

> **译者注（局部符号Q142，PDF p12）：** 作者在本部分叙述中用$\chi$指面内取向角，而公式仍用欧拉角$\chi$；两者相差$\pi$。此处保留原文区分说明，不将两种$\chi$直接等同。director在这里指镜面与表面的交线，不是旧译自行引入的取向分布函数。
''','4d两种甲基的区别与第5部分完整引入，含跨页续句')

a=part('### 5a.','### 5b.')
add(289,[13,14],r'''### 5a. 随机（二维）取向表面的和频张量

甲基面内取向随机时，面内取向角$\chi$在$0$至$2\pi$之间以相同概率取任意值。因为：

$$
\int_0^{2\pi}\cos(n\chi)\,d\chi=\int_0^{2\pi}\sin(n\chi)\,d\chi=0\qquad(n=1,2,3),
$$

张量分量大幅简化如下。

'''+angle+tables(a),'5a面内随机平均与全对称/简并两张分量表')

b=part('### 5b.','### 5c.')
bt=tables(b)
# The p15 approximation uses 4 sqrt2 rather than sqrt32; keep local original form.
bt=bt.replace(r'\sqrt{32}/9',r'4\sqrt2/9')
add(290,[14,15],r'''### 5b. C₃ᵥ取向表面的和频张量

此时，面内角取$\chi$、$\chi+2\pi/3$、$\chi+4\pi/3\;(=\chi-2\pi/3)$三个值的甲基以相同概率存在。利用三角函数的求和关系，将三种取向的正弦、余弦用$\chi$表示后相加，得到：

$$
\begin{aligned}
\sum1&=3,\\
\sum\sin\chi=\sum\cos\chi=\sum\sin2\chi=\sum\cos2\chi&=0,\\
\sum\sin3\chi&=3\sin3\chi,\qquad\sum\cos\chi=3\cos3\chi.
\end{aligned}
$$

将上式代入第4b部分的结果，得到下列结果，可知：(a) 光谱随表面旋转呈六重对称；(b) 即使甲基自由旋转，也能得到(spp)、(psp)、(psp)、(pss)信号；(c) 即使倾斜角为$90^\circ$，在某些基板取向下也能得到(spp)、(psp)、(pps)、(sss)信号。

'''+angle+r'''
倾斜角为零时，全对称振动不出现(spp)、(psp)、(pps)、(sps)、(pss)、(sss)信号。另一方面，对于简并振动，依内部旋转角而定，可以出现这些信号。

> **译者注（原文疑点Q143，PDF p14—15）：** 求和式末项原写$\sum\cos\chi=3\cos3\chi$，候选左侧为$\sum\cos3\chi$；尚未采用。正文引用第4b部分并讨论自由旋转，但下表仍含内部角的三倍角项；(b)中的(psp)重复，(pss)与邻近段落所列组合也不同，均照原文保留，须核验。下表简并$\chi_{zzz}$的系数与5a不同，也未按5a改写。原表简并(spp)、(psp)、(pps)、(sss)行有孤立的花括号，排版仅整理定界符，不改变项的加乘结构。
'''+bt,'5b三重表面取向求和、原文三项结论与全部表内分量')

add(291,[15,16],r'''### 5c. C₄ᵥ、C₆ᵥ取向表面的和频张量

此时，因有：

$$
\sum\sin\chi=\sum\cos\chi=\sum\sin2\chi=\sum\cos2\chi
=\sum\sin3\chi=\sum\cos\chi=0,
$$

所得表达式与第5a部分相同。

> **译者注（原文疑点Q143续，PDF p15）：** 上式末项原文再次写$\sum\cos\chi$，候选为$\sum\cos3\chi$；按原式保留，尚未采用。

### 5d. Cₛ取向表面的和频张量

这是关于垂直于表面的平面具有镜面对称的情况。例如，沿提拉方向取向的LB膜中，甲基相对于提拉方向呈左右V形排列。设甲基轴在表面上的投影，相对于镜面对称面与表面交线的角分别为$+\beta$、$-\beta$；交线与$x$轴的取向角为$\alpha$，则面内取向角$\chi_{\mathrm{ip}}=\alpha+\beta$和$\alpha-\beta$的甲基数量相同。

以$\phi$表示分子面与$xy$面的角（内部旋转角），$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角，$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴的角，则下式所用欧拉角为$\phi=\phi$、$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi+\chi_{\mathrm{ip}}$。即：

$$
\begin{aligned}
\sin\chi&=-\sin\chi_{\mathrm{ip}},&\cos\chi&=-\cos\chi_{\mathrm{ip}},\\
\sin2\chi&=\sin2\chi_{\mathrm{ip}},&\cos2\chi&=\cos2\chi_{\mathrm{ip}},\\
\sin3\chi&=-\sin3\chi_{\mathrm{ip}},&\cos3\chi&=-\cos3\chi_{\mathrm{ip}}.
\end{aligned}
$$

再利用下列三角函数求和关系，将两种配置的正弦、余弦用$\chi$表示并相加，代入第4a部分，即得所需表达式：

$$
\begin{aligned}
\sum1&=2,\\
\sum\sin\chi_{\mathrm{ip}}&=2\sin\alpha\cos\beta,&\sum\cos\chi_{\mathrm{ip}}&=2\cos\alpha\cos\beta,\\
\sum\sin2\chi_{\mathrm{ip}}&=2\sin2\alpha\cos2\beta,&\sum\cos2\chi_{\mathrm{ip}}&=2\cos2\alpha\cos2\beta,\\
\sum\sin3\chi_{\mathrm{ip}}&=2\sin3\alpha\cos3\beta,&\sum\cos3\chi_{\mathrm{ip}}&=2\cos3\alpha\cos3\beta.
\end{aligned}
$$

令$\beta=0$，即得表面固定系的张量分量。同时可知：和频实验中，若使入射面与对称面重合，全对称带不产生(spp)、(psp)、(pps)、(sss)光；甲基自由旋转时，简并带也不产生这些偏振的光。

> **译者注（原文疑点Q144，PDF p15—16）：** 此处原文将内部旋转角说成“分子面与$xy$面的角”，与前文$ac$面和$xz$面的定义不同；候选为沿用前文定义，但未采用。此处$\alpha,\beta$是取向角，其中$\beta$不是分子一阶超极化率。旧译将$\beta=0$称为$C_{2v}$极限、并称自由旋转简并带仍产生上述偏振信号，均非原文，已删除。
''','5c全式与5d镜面对称定义、跨页求和及选择规则')

e=part('### 5e.','## 6.')
add(292,[16,17],r'''### 5e. C₂ᵥ取向表面的和频张量

对应的情况是：甲基成对排列，其分子轴相对于表面法线呈V形。此时，存在面内取向角为$\chi$和$\chi+\pi$的甲基。利用三角函数求和关系，将两种配置的正弦、余弦用$\chi$表示后相加，得到以下结果。

'''+angle+r'''
$$
\begin{aligned}
\sum1&=2,\qquad\sum\sin\chi=0,\qquad\sum\cos\chi=0,\\
\sum\sin2\chi&=2\sin2\chi,\qquad\sum\cos2\chi=2\cos2\chi,\\
\sum\sin3\chi&=0,\qquad\sum\cos3\chi=0.
\end{aligned}
$$
'''+tables(e),'5e两种配置、求和及全对称/简并张量表全部分量')

s=part('## 6.','## 7.');m=maths(s,False)
add(293,[17,18],r'''## 6. 从表面电场到和频极化

和频极化$\mathbf P(\omega_{\mathrm{SF}})$与入射光的表面电场——入射电场$\mathbf E^{(i)}(\omega_{\mathrm{ir}})$、$\mathbf E^{(i)}(\omega_{\mathrm{vis}})$分别加上反射电场$\mathbf E^{(r)}(\omega_{\mathrm{ir}})$、$\mathbf E^{(r)}(\omega_{\mathrm{vis}})$后的矢量和——具有以下关系：
'''+fmt(m[0])+r'''
下标$i,j,k$从左到右依次表示和频光、vis光、ir光电场的坐标轴分量方向，$i,j,k=x,y,z$。一般将入射角为$\theta_I$的入射电场$E^{(i)}$分为$p$、$s$偏振分量，即$E^{(i)}=E_p^{(i)}+E_s^{(i)}$。光电场振幅的$x,y,z$分量用偏振分量的电场振幅表示为：
'''+fmt(m[1])+r'''
同样，对于反射角为$\theta_r$的反射电场$E^{(r)}$：
'''+fmt(m[2])+r'''
反射电场与入射电场通过菲涅尔振幅反射系数满足：
'''+fmt(m[3])+r'''
$n_1$、$n_2$分别为入射侧与透射侧介质的折射率，$\theta_t$为折射角。因此，表面电场$E^{(\mathrm{surf})}$的坐标分量如下：
'''+''.join(fmt(x) for x in m[4:])+r'''
式(6.5c)中的$n'$为发出和频信号的表面层折射率。分别由式(6.5)求红外和可见电场的坐标分量，再代入式(6.1)，即可求极化矢量的大小。

> **译者注（原式保留）：** 式(6.5c)的$ (n_1n_2/n')^2$按原页保留，不据其他章节的场因子表达式替换。$\theta_I$与式中的$\theta_i$也按原文局部写法保留。
''','第6部分场分解、菲涅尔振幅关系与6.1—6.5c')

s=part('## 7.');m=maths(s,False)
add(294,[18,19],r'''## 7. 从和频极化到和频电场

由和频极化$\mathbf P(\omega_{\mathrm{SF}})$产生的和频电场$\mathbf E(\omega_{\mathrm{SF}})$，向“反射方向”和“透射方向”传播。沿这两个方向出射的和频电场$E^{(r)}(\omega_{\mathrm{SF}})$、$E^{(t)}(\omega_{\mathrm{SF}})$的振幅满足：
'''+''.join(fmt(x) for x in m[:4])+r'''
引入菲涅尔$L$因子，可以简化表达式：
'''+''.join(fmt(x) for x in m[4:])+r'''
关于式(7.1b)及式(7.4b)中乘在极化分量上的系数的符号，由于会随$z$轴取向而变化，仍有不明确之处。

（完）

> **译者注（原文疑点Q145，PDF p18—19）：** 式(7.1a)、(7.2a)的系数为正，而式(7.4a)、(7.5a)定义的对应$L$因子带负号；式(7.4c)、(7.5c)的$L$定义还含$P_z(\omega_{\mathrm{SF}})$，若代入式(7.3)会再次乘以极化。原文这些写法全部保留；候选为核对$s$分量符号并从$L_{p,z}$中移除极化，但尚未采用。作者最后明确保留的符号不确定性亦照译，不能用旧译所添“s偏振混合效应”解释取代。
''','第7部分全部7.1a—7.5c及作者末尾符号不确定性说明')

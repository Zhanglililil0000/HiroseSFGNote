from 整节工具 import *
add(278,[2,3],r'''## 2. 甲基的取向与欧拉角

本文的表面坐标系取指向基板内部的法线为$z$轴，并在面内取$x$轴、$y$轴。（例如，可将和频光的“入射面”与表面的交线，沿光传播方向取为$x$轴；也可将LB膜制作时的提拉方向或晶面的长轴方向取为$x$轴。）Born & Wolf、Bloembergen及Shen的光学表达式都取指向基板内部的$z$轴。表面科学中常将$z$轴取为相反方向；本文为与上述表达式一致，也采用光学中的定义。定义表面倾斜角时，则使用从外向法线量起的角，须加注意。

固定于甲基的坐标系取从C原子指向三个H原子的$C_3$对称轴为$c$轴，取包含三个CH键之一CH(1)的平面为$ac$面。甲基的取向用以下三个角定义。

(1) **内部旋转角$\phi$：** 即甲基相对于表面的扭转角。从$x$轴负侧向正方向观察，$ac$面（包含分子轴与CH(1)键的平面）向下、向右倾斜时为正旋转。“通过绕$c$轴旋转”，该角可表述为：

(a) 面向$x$轴正方向时，在左侧、即$y$轴负侧，使$b$轴平行于表面。

(b) 沿$a$轴进入基板内部的方向，使$ac$面垂直于$xy$面所需的旋转角。

(c) 或者，使$a$轴重合到$-z$轴在$ab$面上的投影所需的旋转角。（重合方向应使沿$a$轴和沿$x$轴的矢量内积为正。）

(d) XCH(1)面垂直于表面、CH(1)面朝向表面侧时，$\phi=0$；CH(1)面朝向真空侧时，$\phi=\pi$。

(e) 三个CH键等价时，内部旋转角为$\phi$及$\phi\pm2\pi/3$的甲基以相同权重存在。

(f) 两个CH键等价时，认为内部旋转角为$\phi+2\pi/3$和$\phi-2\pi/3$的甲基等价，而内部旋转角为$\phi$的甲基属于另一种。

(g) 自由旋转时，$\phi$在$0$至$2\pi$之间以相同权重取任意值。

(2) **倾斜角（tilt角）$\theta_{\mathrm{tilt}}$：** 按通常定义，取$c$轴（$C_3$轴）与外向法线之间的角，并以绕$N$轴使$c$轴重合到外向法线上的方向为正旋转。本文表面坐标系的$z$轴是向下的法线，所以欧拉角$\theta=\pi-\theta_{\mathrm{tilt}}$。甲基的三个H原子朝向真空侧时，$\theta_{\mathrm{tilt}}<\pi/2$。

(3) **面内取向角$\chi_{\mathrm{in\text{-}plane}}$（简称$\chi_{\mathrm{ip}}$）：** 绕$z$轴旋转，使$c$轴在$xy$面上的投影重合到$x$轴上所需的角。从$x$轴负侧向正方向观察，投影在左侧时为正旋转。

(a) 投影后的$C_3$轴偏离$x$轴的角为$\alpha$时，$b$轴与$y$轴之间的角也是$\alpha$。投影后的$C_3$轴相对于$x$轴呈“八”字形左右交替偏转时，$\chi_{\mathrm{ip}}=+\alpha$和$-\alpha$的甲基数量相同。

(b) 面内取向随机时，$\chi_{\mathrm{ip}}$在$0$至$2\pi$之间以相同权重取任意值。

本文$(x,y,z)$系的$z$轴指向基板内部，因此对应的欧拉角$\chi=\pi+\chi_{\mathrm{ip}}$。

这里所说的负旋转，相对于上述正旋转，按欧拉角定义是指从$2\pi$中减去该旋转角后，再沿正方向旋转。当这样定义甲基的取向时，应确认其与下文表达式中的欧拉角有如下关系：

$$
\phi=\phi,\qquad\theta=\pi-\theta_{\mathrm{tilt}},\qquad\chi=\pi+\chi_{\mathrm{ip}}.
$$

> **译者注（局部约定）：** $\phi$是绕甲基自身$c$轴的内部旋转角，$\chi_{\mathrm{ip}}$才是面内取向角；二者不能沿用旧译混称“方位角”。本节公式中的$\theta$也不能直接替换为从外向法线计量的倾斜角。
''','第2部分全部定义、七项内部旋转角条件及跨页角度关系')

intro=r'''## 3. 甲基的$\beta_{abc}$（分子固定系）

作为练习另一个文件《变换矩阵(xyz)》及 *Appl. Spectrosc.* 论文中变换表用法的例子，下面从每个CH键的和频张量分量求甲基的张量分量。将固定于CH键的坐标系记为$(\xi\eta\zeta)$系，取从C指向H的$C_3$轴为$\zeta$轴；选取$\xi$轴，使$\xi\zeta$面垂直于$ab$面，这样三个CH键的$\eta$轴都平行于$ab$面。再规定$\eta$轴正方向，使绕$\eta$轴旋转$\theta<\pi$时，$\zeta$轴重合到$z$轴。

将各CH键的$(\xi\eta\zeta)$系重合到固定于甲基的$(abc)$系，所需的欧拉角$(\chi,\theta,\phi)$如下。（先将CH轴即$\zeta$轴重合到$c$轴，再将$\eta$轴重合到$b$轴。）

$$
\begin{aligned}
\mathrm{CH}(1)&:(\pi,\pi-\tau,0),\\
\mathrm{CH}(2)&:(5\pi/3,\pi-\tau,0),\\
\mathrm{CH}(3)&:(\pi/3,\pi-\tau,0).
\end{aligned}
$$

其中$\tau$为HCX键角。取$T_{dv}$角时，$\cos\tau=-1/3$、$\sin\tau=\sqrt8/3$，所以变换中所需的三角函数如下：
'''
sec=part('## 3. 分子极化率','## 4. 实验室极化率')
mm=maths(sec,False)
# Reuse only individually compared numeric rows and tensor rows.
rows=''.join(('\nCH('+str(i-2)+')：\n' if i>=3 else '')+fmt(m.replace(r'\sin 2\theta = -\sqrt{32}',r'\sin 2\theta = \sqrt{32}').replace(r'-10\sqrt{2}/27',r'-\sqrt{200}/27')) for i,m in enumerate(mm[1:6],1))
# mm[0] is the tau row; rows 1..5 are phi/theta/CH1..3.
tensors=mm[6].replace(r'\beta_{aaa} &= -',r'\beta_{aaa} &= ')
approx=''.join(fmt(m.replace(r'\approx -\frac',r'\approx \frac')) for m in mm[7:10])
body=r'''
CH键的伸缩振动沿$\zeta$轴，因此认为振动和频张量的分量为$\beta_{\xi\xi\zeta}$、$\beta_{\eta\eta\zeta}$、$\beta_{\zeta\zeta\zeta}$。（绕CH键有轴对称性时，$\beta_{\xi\xi\zeta}=\beta_{\eta\eta\zeta}$。）将变换表中的$(abc)$、$(xyz)$分别替换为$(\xi\eta\zeta)$、$(abc)$，对三个CH键的三个分量，分别利用上述关系计算其对$\beta_{aaa}$、$\beta_{aab}$等的贡献，再求出对三个CH求和不为零的分量，即得以下结果。这意味着把三个CH键极化的矢量和作为甲基的极化，并假定三个CH键的$\beta_{\xi\xi\zeta}$、$\beta_{\eta\eta\zeta}$、$\beta_{\zeta\zeta\zeta}$分别相等。
'''
end=r'''
在$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时（估计$\beta_{\xi\xi\zeta}\sim\beta_{\eta\eta\zeta}\sim0.1\beta_{\zeta\zeta\zeta}$），值得记住上面的近似关系：第一行对应全对称振动。尤其应注意：CH基团有$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$，甲基却有$\beta_{aac}\sim4\beta_{ccc}$，即分子轴方向与垂直方向分量的大小关系发生了反转。

CH₃基团伸缩振动中，全对称振动沿$c$轴，简并振动沿$a$、$b$轴。张量下标从左到右，依次表示和频光、VIS光、IR光对应的跃迁矩方向或投影分量。因此，产生振动共振的和频张量分量如下：

全对称振动：

$$
\beta_{aac}=\beta_{bbc},\qquad\beta_{ccc}.
$$

简并振动：

$$
\beta_{aaa}=-\beta_{abb}=-\beta_{bab}=-\beta_{bba},\qquad
\beta_{caa}=\beta_{cbb}=\beta_{aca}=\beta_{bcb}.
$$

注意：即使$\beta_{\xi\xi\zeta}\ne\beta_{\eta\eta\zeta}$，这些关系也成立。

> **译者注（原文疑点Q139，PDF p3）：** 原文前一句写将$\zeta$轴重合到$z$轴，下一句却明确说重合到甲基$c$轴；此处保留二者，候选前一$z$应为$c$，尚未采用。原文四面体角标记写作$T_{dv}$，不据惯用写法改字。旧译将$\sin2\theta$误加负号、将$\beta_{aaa}$首式及近似值误加负号、将$\beta_{caa}$近似值误加负号，并误称末尾关系只在两个横向分量相等时成立，均已按原页恢复。
'''
add(279,[3,4],intro+rows+body+fmt(tensors)+approx+end,'第3部分CH键坐标、三角函数表、11个分子张量分量及模式归属')

add(280,[4,5],r'''## 4. 取向甲基的$\beta_{xyz}$（表面固定系）

用欧拉角$(\chi,\theta,\phi)$表示甲基相对于表面固定$(xyz)$坐标系的取向，借助《变换矩阵(xyz)》及 *Appl. Spectrosc.* 论文中的表，可求得以下表面系张量分量。关于倾斜角$\theta$，这里不用变换表中$\sin\theta$、$\sin2\theta$、$\sin3\theta$形式的三角函数，而利用下列关系改写为$\sin\theta$、$\cos\theta$的幂的形式：

$$
\begin{aligned}
\sin2\theta&=2\sin\theta\cos\theta,\\
\cos2\theta&=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta,\\
\sin3\theta&=3\sin\theta-4\sin^3\theta,\\
\sin\theta+\sin3\theta&=4(\sin\theta-\sin^3\theta),\\
\cos3\theta&=4\cos^3\theta-3\cos\theta,\\
\cos\theta-\cos3\theta&=4(\cos\theta-\cos^3\theta).
\end{aligned}
$$

对于简并振动，考虑CH键与表面的相互作用、位阻等造成$C_{3v}$对称性破缺的情况，给出将两个模式分别作为$a$轴方向振动和$b$轴方向振动的表达式。甲基自由旋转时，将两个张量相加即可。全对称振动从表中求$\beta_{aac}$、$\beta_{bbc}$、$\beta_{ccc}$的变换，并将$\beta_{aac}$与$\beta_{bbc}$的贡献相加。简并振动则将$\beta_{aaa}$、$\beta_{bba}$、$\beta_{caa}$、$\beta_{aca}$一组，与$\beta_{abb}$、$\beta_{bab}$、$\beta_{cbb}$、$\beta_{bcb}$一组分别变换，再利用上述关系求和。

以$\phi$表示$ac$面与$xz$面的角（内部旋转角），$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角，$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴的角（面内取向角），则以下表达式中的欧拉角为：

$$
\phi=\phi,\qquad\theta=\pi-\theta_{\mathrm{tilt}},\qquad\chi=\pi+\chi_{\mathrm{ip}}.
$$

以下给出代表性取向的张量分量。

> **译者注（公式读法）：** 必须区分$\sin^3\theta$与$\sin3\theta$、$\cos^2\theta$与$\cos2\theta$。后文大量使用前者；原式中关于$\phi$与$\chi$的倍角仍为倍角。标题的分子$\beta$与表内表面响应$\chi$依原文分别保留。
''','第4部分引入、三角恒等式、模式分组与角度关系')

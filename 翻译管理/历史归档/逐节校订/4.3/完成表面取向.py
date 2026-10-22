from 整节工具 import *
add(307,[16,17],r'''## 5. 表面取向造成的和频张量差异

（以下叙述中使用的角$\chi$，是指以$\phi$表示分子面与$xy$面的角（内部旋转角）、$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角、$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴的角时的$\chi_{\mathrm{ip}}$。它们与张量分量表达式中所用欧拉角的关系为$\phi=\pi/2+\phi$、$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi/2+\chi_{\mathrm{ip}}$。）

亚甲基的面内取向用角$\chi$定义。将入射面与表面的交线沿光传播方向取为正方向，以此交线与亚甲基$C_2$轴在表面上投影之间的角作为取向角，便能导出解析测量数据所需的张量，并研究信号随样品旋转的变化。若将$\chi$定义为表面固定轴——例如LB膜提拉轴或晶轴——与亚甲基轴投影之间的角，则求得的是表面固有的张量分量。

不过，对于第5d部分$C_s$对称的情况，分别定义两个角更便于解释数据：一是入射面与表面的交线，相对于镜面对称面与表面交线（director）的角；二是亚甲基轴的投影相对于镜面与表面交线的角。

在具有$C_s$对称性的表面和频实验中，入射面与对称面重合时，自由旋转亚甲基不产生(spp)、(psp)、(pps)、(sss)光。而该旋转冻结时，仅出现简并振动，显示(spp)、(psp)、(pps)、(sss)光。

以下考察代表性取向形式下的张量分量。为简便起见，假定亚甲基内部旋转冻结，但两个CH键等价。

> **译者注（原文疑点Q156，PDF p16—17）：** 原文在此仍用“简并振动”，而第3部分将CH₂模式分为$a_1,b_1,b_2$；此词按原文保留，不改成某一指定模式。叙述中的$\chi$指$\chi_{\mathrm{ip}}$，公式欧拉角$\chi$则为$\pi/2+\chi_{\mathrm{ip}}$，应区分。旧译自行添加的背反射、双官能团及分布讨论已删除；director在这里是镜面与表面的交线。
''','第5部分引入，含表面固定轴、director、选择规则和冻结旋转条件')

def mode_tables(s,kind):
    res=''
    for label,title in [(sym,'对称($a_1$)振动'),(anti,'反对称($b_1$)振动'),(oop,'面外($b_2$)振动')]:
        g=group(s,label);tab=table(g[g.index('#####'):])
        if kind=='5b':
            if label==anti:tab=tab.replace(r'\chi_{zzz} =',r'c_{zzz} =')
            if label==oop:tab=tab.replace(r'\chi_{yxx} =',r'c_{yxx} =')
        if kind=='5e' and label==oop:
            def orig(m):
                x=m[0]
                if r'\chi_{yzy}' in x.split('=')[0]:
                    x=x.replace(r'\frac{1}{4}\beta_{cbb}',r'\frac{1}{4}\beta_{cbb}(1/4)\beta_{caa}',1)
                return x
            tab=re.sub(r'\$\$[\s\S]*?\$\$',orig,tab)
        res+='\n\n#### '+title+'\n\n'+approx(g)+tab
    return res

a=part('### 5a.','### 5b.')
add(308,[17,18,19],r'''### 5a. 随机（二维）取向表面的和频张量

亚甲基的面内取向随机时，面内取向角$\chi$在$0$至$2\pi$之间以相同概率取任意值。由于：

$$
\int_0^{2\pi}\cos(n\chi)\,d\chi=\int_0^{2\pi}\sin(n\chi)\,d\chi=0\qquad(n=1,2,3),
$$

张量分量大幅简化如下。

'''+angle+r'''
即使面内取向随机，反对称振动带也只产生(ppp)、(ssp)、(sps)、(pss)信号；但与甲基不同，对称振动带只要$\phi$不是$0$或$\pi/2$，并且$\theta_{\mathrm{tilt}}\ne0$，也会产生(spp)、(psp)、(pps)、(sss)信号。
'''+mode_tables(a,'5a')+r'''
> **译者注（原文疑点Q156续，PDF p18）：** 反对称表$\chi_{zyy}$含$\cos\theta-2\cos^3\theta$，与同表$\chi_{yzy}$的$\cos\theta-\cos^3\theta$不同；照原式保留。候选从一般式作面内平均核算，尚未采用。
''','5a随机面内平均与三种模式全部表项、无信号项')

b=part('### 5b.','### 5c.')
add(309,[19,20,21],r'''### 5b. C₃ᵥ取向表面的和频张量

此时，角$\chi$取$\chi$、$\chi+2\pi/3$、$\chi+4\pi/3\;(=\chi-2\pi/3)$三个值的亚甲基以相同概率存在。利用三角函数求和关系，将三种取向的正弦、余弦用$\chi$表示后相加，得到：

$$
\begin{aligned}
\sum1&=3,\\
\sum\sin\chi=\sum\cos\chi=\sum\sin2\chi=\sum\cos2\chi&=0,\\
\sum\sin3\chi&=3\sin3\chi,\qquad\sum\cos3\chi=3\cos3\chi.
\end{aligned}
$$

将其代入第4a部分，得到下列结果，可知：(a) 和频光谱随表面旋转呈六重对称；(b) 即使亚甲基自由旋转，也能得到(spp)、(psp)、(psp)、(pss)信号；(c) 即使倾斜角为$90^\circ$，也能得到(spp)、(psp)、(pps)、(sss)信号。

'''+angle+r'''
> **译者注（原文疑点Q157，PDF p19—21）：** (b)中的(psp)重复，且所列组合与邻近句不同，原述保留。下表仍带$\phi$相关项，引用自由旋转结论时须核查平均条件。原表p20反对称的$c_{zzz}$、p21面外的$c_{yxx}$使用拉丁$c$，此处照录；其他分量仍为$\chi$。候选为两处应与同表统一为$\chi$，尚未采用。
'''+mode_tables(b,'5b'),'5b三重面内取向求和、原文结论及三模式全部表项')

add(310,[21,22],r'''### 5c. C₄ᵥ、C₆ᵥ取向表面的和频张量

此时，因为：

$$
\sum\sin\chi=\sum\cos\chi=\sum\sin2\chi=\sum\cos2\chi
=\sum\sin3\chi=\sum\cos\chi=0,
$$

所得表达式与第5a部分相同。

### 5d. Cₛ取向表面的和频张量

这是关于垂直于表面的平面具有镜面对称的情况。例如，沿提拉方向取向的LB膜中，亚甲基相对于提拉方向呈V形排列。设镜面对称面与表面的交线，相对于亚甲基轴在表面上投影的角为$+\beta$、$-\beta$，交线与$x$轴的取向角为$\alpha$，则面内取向角$\chi_{\mathrm{ip}}=\alpha+\beta$、$\alpha-\beta$的亚甲基数量相同。

'''+angle+r'''
即有：

$$
\begin{aligned}
\sin\chi&=\cos\chi_{\mathrm{ip}},&\cos\chi&=-\sin\chi_{\mathrm{ip}},\\
\sin2\chi&=-\sin2\chi_{\mathrm{ip}},&\cos2\chi&=-\cos2\chi_{\mathrm{ip}},\\
\sin3\chi&=-\cos3\chi_{\mathrm{ip}},&\cos3\chi&=+\sin3\chi_{\mathrm{ip}}.
\end{aligned}
$$

再利用三角函数求和关系，将两种配置的正弦、余弦用$\chi$表示后相加，得到：

$$
\begin{aligned}
\sum1&=2,\\
\sum\sin\chi_{\mathrm{ip}}&=2\sin\alpha\cos\beta,&\sum\cos\chi_{\mathrm{ip}}&=2\cos\alpha\cos\beta,\\
\sum\sin2\chi_{\mathrm{ip}}&=2\sin2\alpha\cos2\beta,&\sum\cos2\chi_{\mathrm{ip}}&=2\cos2\alpha\cos2\beta,\\
\sum\sin3\chi_{\mathrm{ip}}&=2\sin3\alpha\cos3\beta,&\sum\cos3\chi_{\mathrm{ip}}&=2\cos3\alpha\cos3\beta.
\end{aligned}
$$

将上式代入第4a部分，就得到所需表达式。令$\beta=0$，即得表面固定系中的张量分量。和频实验中，若使入射面与对称面重合，全对称带不产生(spp)、(psp)、(pps)、(sss)光；亚甲基自由旋转时，简并带也不产生这些偏振的光。

> **译者注（原文疑点Q158，PDF p21—22）：** 第5c部分求和式末项原写$\sum\cos\chi$，与前面重复；候选为$\sum\cos3\chi$，未采用。第5d部分仍使用“全对称带”“简并带”的原文表述。这里的$\alpha,\beta$是几何角；$\beta$不是分子一阶超极化率。
''','5c原求和式与5d完整镜面几何、转换关系、跨页求和及选择规则')

e=part('### 5e.','## 6.')
add(311,[22,23,24,25],r'''### 5e. C₂ᵥ取向表面的和频张量

此时，面内取向角为$\chi$与$\chi+\pi$的亚甲基数量相同。利用三角函数求和关系，将两种配置的正弦、余弦用$\chi$表示后相加，得到以下结果。

'''+angle+r'''
$$
\begin{aligned}
\sum1&=2,\qquad\sum\sin\chi=\sum\cos\chi=0,\\
\sum\sin2\chi&=2\sin2\chi,\qquad\sum\cos2\chi=2\cos2\chi,\\
\sum\sin3\chi&=\sum\cos3\chi=0.
\end{aligned}
$$
'''+mode_tables(e,'5e')+r'''
> **译者注（原文疑点Q158续，PDF p24）：** 面外表的$\chi_{yzy}$原含$\beta_{cbb}(1/4)\beta_{caa}$，即重复引入一个分子张量因子，此处照录，不按相邻$\chi_{zyy}$删去。原$\chi_{yyz}$用$\sin2\chi$、$\cos2\chi$的写法也保留。候选须从变换式核算后确认，尚未采用。
''','5e双取向求和与三种模式全部分量，含p25表末续行')

from 整节工具 import *
def table(s):
    tokens=[]
    for m in re.finditer(r'\$\$([\s\S]*?)\$\$|\$\((ppp|spp|ssp|psp|sps|pps|pss|sss)\)\$',s):
        if m[1] is not None: tokens.append(fmt(norm(m[1])))
        else:
            tokens.append('\n**('+m[2]+')**\n')
            if '（无）' in s[m.end():m.end()+25]:tokens.append('\n无。\n')
    return ''.join(tokens)
def fixed(s):
    s=s.replace(r'\mp',r'\pm')
    s=s.replace(r'\approx -\frac',r'\approx \frac')
    s=s.replace(r'\sin^2\theta - 4\cos^2\theta',r'\sin^2\theta + 4\cos^2\theta')
    return s
sym=part('### 4a. 一般公式','**简并模式**（上段')
add(281,[5,6],r'''### 4a. 一般式

先给出一般表达式。它们是按取向条件进行简化时的出发点，也应能适用于各种条件。

#### 全对称振动

CH基团的和频张量表达式也与下面相同。在$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时，$\beta_{aac}\sim(4/9)\beta_{\zeta\zeta\zeta}$、$\beta_{ccc}\sim(1/9)\beta_{\zeta\zeta\zeta}$。
'''+table(sym),'4a全对称振动八种偏振组合、全部27个张量分量')
deg=part('**简并模式**（上段','### 4b.')
groups=[('**$(ppp)$', '**$(spp)$'),('**$(spp)$','**$(psp)$'),('**$(psp)$','**$(pps)$'),('**$(pps)$',None)]
for n,(a,b) in zip(range(282,286),groups):
    x=deg[deg.index(a):deg.index(b)] if b else deg[deg.index(a):]
    pre=''
    if n==282:
        pre=r'''#### 简并振动

下列双重符号的上号对应$(\mathrm{deg},a)$模式，下号对应$(\mathrm{deg},b)$模式。把最后一个下标为$a$的分量（$\beta_{caa}$、$\beta_{aaa}$、$\beta_{bba}$）和最后一个下标为$b$的分量（$\beta_{cbb}$、$\beta_{abb}$、$\beta_{bab}$）分别处理。

在$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时，$\beta_{caa}\sim(4/9)\beta_{\zeta\zeta\zeta}$、$\beta_{aaa}\sim(\sqrt{32}/9)\beta_{\zeta\zeta\zeta}$。

> **译者注（原文疑点Q140，PDF p6—9）：** 本表上、下号按原文分别对应两个模式，符号均按原页恢复为$\pm$。两模式相加、单模式或取向平均的归一化关系仍须结合原文约定理解，不能把表中的单模式系数直接当作总简并带响应。尤其本表$\chi_{zzx}$含$\sin\theta-2\sin^3\theta$，而4b、4c相应项写$\sin\theta-\sin^3\theta$；原式均保留，差异未修正。

> **译者注（排版）：** 原表个别行存在方括号与圆括号不配对。下文仅整理分组定界符以便数学排版，未改动括内项、运算符及分组范围。
'''
    add(n, {282:[6,7],283:[7],284:[7,8],285:[8,9]}[n],pre+fixed(table(x)),f'4a简并振动公式组{n-281}，按偏振组合逐项对照')

b=part('### 4b.','### 4c.')
add(286,[9,10],r'''### 4b. 自由旋转、随机扭转角

甲基内部旋转（torsion）自由时，内部旋转角$\phi$在$0$至$2\pi$之间以相同概率取任意值。由于：

$$
\int_0^{2\pi}\cos(n\phi)\,d\phi=\int_0^{2\pi}\sin(n\phi)\,d\phi=0\qquad(n=1,2,3),
$$

简并振动的张量分量大幅简化如下。（须注意：这与旋转冻结、角$\phi$固定为$0$或$\pi$时的表达式不同。）以$\phi$表示$ac$面与$xz$面的角，$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角，$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴的角，使用的欧拉角仍为$\phi=\phi$、$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi+\chi_{\mathrm{ip}}$。

**全对称振动：** 与第4a部分相同。

**简并振动：** 在$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时，$\beta_{caa}\sim(4/9)\beta_{\zeta\zeta\zeta}$、$\beta_{aaa}\sim(\sqrt{32}/9)\beta_{\zeta\zeta\zeta}$。
'''+table(b[b.index('$(ppp)$'):]),'4b自由内部旋转条件、平均积分与27个分量')

c=part('### 4c.','### 4d.')
add(287,[10,11,12],r'''### 4c. 三个H原子等价时（内部旋转被冻结），或C₃ᵥ对称性破缺而振动频率不分裂时

此时，内部旋转角为$\phi$、$\phi+2\pi/3$、$\phi+4\pi/3\;(=\phi-2\pi/3)$的甲基数量相同。利用三角函数的求和关系，将三种配置的正弦、余弦用$\phi$表示后相加，有：

$$
\begin{aligned}
\sum1&=3,\\
\sum\sin\phi=\sum\cos\phi=\sum\sin2\phi=\sum\cos2\phi&=0,\\
\sum\sin3\phi&=3\sin3\phi,\qquad\sum\cos3\phi=3\cos3\phi.
\end{aligned}
$$

将这些关系代入第4a部分，换算为每个甲基的张量，即得到下式。以$\phi$表示$ac$面与$xz$面的角，$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角，$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴的角，所用欧拉角为$\phi=\phi$、$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi+\chi_{\mathrm{ip}}$。

**全对称振动：** 与第4a部分相同。

**简并振动：** 在$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时，$\beta_{caa}\sim(4/9)\beta_{\zeta\zeta\zeta}$、$\beta_{aaa}\sim(\sqrt{32}/9)\beta_{\zeta\zeta\zeta}$。
'''+table(c[c.index('$(ppp)$'):])+r'''
> **译者注（原文疑点Q141，PDF p10—12）：** 原式保留不同偏振分量中的符号差别，例如$\chi_{yxx}$与$\chi_{xyx}$的$\cos3\phi$、$\sin3\phi$项并不完全同形；本表$\chi_{xyy}$中$\sin3\phi$括号内也保留减号。候选可从一般式作三重平均重新核算，尚未用于正文。旧译的幂次、负号及$\sum1$漏掉求和号等转录问题已按原页恢复。
''','4c三重配置求和、每个甲基归一化与27个简并分量')

from pathlib import Path
import shutil
r=Path('HiroseSFGNote').resolve();p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';o=r/'翻译管理/校订记录/1.1';s=p.read_text(encoding='utf-8');a=s.index('## 3. 分子的 SFG 极化与振动共振');marker='\u200b\t相互作用哈密顿量为';b=s.index(marker,a);assert not (o/'B003-修订前.md').exists();shutil.copy2(p,o/'B003-修订前.md')
t=r'''## 3. 分子的 SFG 极化与振动共振

在封闭的物理系统中，各组成部分在总能量保持不变的条件下交换能量。在由光和分子组成的系统中，光的能量增加或减少时，分子的能量（包括动能）就相应减少或增加。对于固体，可以把整体看作一个大分子，将固体整体的能量也包括在内，仍然遵守能量守恒定律。各组成部分之间的能量交换，依照相互作用（耦合）的形式和强度进行。

光诱导分子极化时，在第一近似下，分子电偶极矩与光电场之间的作用力是能量交换的原因。（分子内部的电荷分布存在偏置时，就形成电偶极子；分子的电偶极子在电场中获得能量的效应，以发现者的名字称为斯塔克效应。）将这一作用写成相互作用哈密顿量，即从力的量纲转为能量的量纲，得到

$$
H'(t)=-\boldsymbol{\mu}\cdot\mathbf{E}(t).
\tag{6}
$$

> **译者注（原文疑误）：** 此处原文写作「電荷分布が遍在する」，其中「遍在」疑为「偏在」之误；这里按“电荷分布存在偏置”译出。

通常熟悉的薛定谔方程 $H\psi(\mathbf{r})=E\psi(\mathbf{r})$，是仅以空间坐标为变量的微分方程。然而，由式（6）可知，涉及光的相互作用还包含时间变量，因此必须使用式（7）所示的含时薛定谔方程。

$$
i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t)
=H\Psi(\mathbf{r},t).
\tag{7}
$$

通常将式（6）表示的项视为相对于系统总哈密顿量足够小的量；总哈密顿量包含无光时定义的那一部分。因此，可从不存在光相互作用时的哈密顿量 $H_0$ 的解出发，用微扰论计算偏离该解的修正。设 $H_0$ 的本征函数为 $\Psi_n(\mathbf{r},t)$，本征值为 $E_n$。由于 $H_0$ 不显含时间，有

$$
i\hbar\frac{\partial}{\partial t}\Psi_n(\mathbf{r},t)
=H_0\Psi_n(\mathbf{r},t)
=E_n\Psi_n(\mathbf{r},t),
$$

由此得到

$$
\begin{aligned}
\Psi_n(\mathbf{r},t)&=\psi_n(\mathbf{r})\exp(-iE_nt/\hbar),\\
H_0\psi_n(\mathbf{r})&=E_n\psi_n(\mathbf{r}).
\end{aligned}
\tag{8}
$$

实验中观测的并不是真空中孤立的分子，而是受到周围环境相互作用的一群分子。穿过这群分子并传播到外部的光，是各分子极化所发出电磁波的矢量和，再与没有分子时直接传播出来的入射电磁波作矢量相加的结果。光与样品的相互作用用宏观的、即整个介质的极化率来描述；为弥补薛定谔方程的不足，广泛采用密度矩阵法。这里所说的不足，是指不能在方程中表达系统的弛豫现象。关于密度矩阵法的基本思想，霜田光一《激光物理入门》（或 K. Shimoda, *Introduction to Laser Physics*, Springer）第 7 章有易于理解的说明。本笔记列出 Y. R. Shen 的 *The Principles of Nonlinear Optics* 第 2 章中将密度矩阵法用于非线性光学现象所得到的结果。对于 CARS、CSRS 等四波混频，则列出广濑推导的表达式（虽然也有其他相关论文）。（课堂上熟悉的量子力学微扰论以孤立分子为对象。为了说明使用通常的微扰法也能得到相应结果，附录 A 给出了这部分计算。）

'''
head=s[:a].replace('第 3 部分及以后仍为待校订旧译。','第 3 部分开头（至式（8）及密度矩阵法引入）已由 B003 校订，其后仍为待校订旧译。').replace('PDF 第 1–2 页。','PDF 第 1–3 页。')
p.write_text(head+t+s[b:],encoding='utf-8');assert p.read_text(encoding='utf-8').split(marker,1)[1]==s.split(marker,1)[1]
print('B003: PDF p3 complete; eqs 6–8; p4 onward unchanged.')

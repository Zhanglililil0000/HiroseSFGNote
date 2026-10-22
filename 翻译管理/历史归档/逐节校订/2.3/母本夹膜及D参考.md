### 两种介质之间夹有薄膜的体系

介质1（入射侧）与介质2之间夹有厚度 $h_m$ 的膜 $m$，两界面均为平面且相互平行。原点与坐标轴沿用上面的定义。

| 记号 | 定义 |
|---|---|
| $1/m$、$m/1$ 界面 | 介质1与膜的界面；分别着眼于介质1侧、薄膜侧 |
| $2/m$、$m/2$ 界面 | 介质2与膜的界面；分别着眼于介质2侧、薄膜侧 |
| $n_1,n_2,n_m$ | 介质1、介质2与薄膜的折射率 |
| $k_1,k_2,k_m$ | 三者内部的波矢 |
| $\theta_1,\theta_2,\theta_m$ | 各介质中光路与法线的夹角 |
| $t_{1m},t_{m1},t_{m2}$ | 电场由介质1透入膜、由膜透入介质1、由膜透入介质2的透射系数 |
| $r_{1m},r_{m1},r_{m2}$ | 分别由介质1入射在 $1/m$ 反射、由膜内入射在 $m/1$ 反射、由膜内入射在 $m/2$ 反射的电场反射系数 |
| 上行（−）光 | 从 $m/2$ 界面向 $m/1$ 界面传播的光 |
| 下行（+）光 | 从 $m/1$ 界面向 $m/2$ 界面传播的光 |

底本说反射与透射系数表达式见“附录B”。

> **译校注（Q047）：** 本文这些系数列在附录A，附录B为波动复习。“附录B”按底本记录，候选为附录A。

入射光在膜内点P产生的电场如下图；图中 $d=h_m$。

![入射光在膜内点P产生的上下行场示意图](../../../../%E4%B8%AD%E6%96%87%E7%89%88%E6%9C%AC/assets/ch02/s02/B080-p41-01.png)

*入射光在膜内点P产生的上下行场示意图（底本p41，原图）。*

*图内“媒質-1”“媒質-2”为介质1、介质2；$d$ 为膜厚，$θ_1,θ_m,θ_2$ 表示各介质中的光路角，P为膜内观测点。*

原点反射光所包含的多重反射分量，在膜内沿以下光路传播；图中仍有 $d=h_m$。

![对原点反射场有贡献的多重反射光路](../../../../%E4%B8%AD%E6%96%87%E7%89%88%E6%9C%AC/assets/ch02/s02/B080-p42-02.png)

*对原点反射场有贡献的多重反射光路（底本p42，原图）。*

*图内 $A_1,A_2,A_3$ 与 $B_1,B_2$ 为图示反射光路上的点；“媒質”译为介质。*

#### 反射光

“反射光”除在 $1/m$ 界面直接反射的光外，还包括进入薄膜、多重反射后从 $m/1$ 界面出射的上行（−）光。应对包含这些多重反射分量的总场，在界面两侧应用边界条件。

原点反射光中多重反射分量的性质如下：

| 项目 | 表达式 |
|---|---|
| 入射点 | $(-2nh_m\tan\theta_m,0)$，$n=1,2,\ldots$ |
| 入射点处光路差 | $-2nh_m\tan\theta_m\sin\theta_1$ |
| 相对于原点入射光的初始相位差 | $-2nh_mk_1\tan\theta_m\sin\theta_1$ |
| 膜内传播距离 | $2nh_m/\cos\theta_m$ |
| 膜内相位前进量 | $2nh_mk_m/\cos\theta_m$ |
| 与直接反射光的净相位差 | $2nh_mk_m\cos\theta_m$；底本还写成 $2\pi nn_mh_m\cos\theta_m/\lambda$ |
| 透射与反射因子 | $t_{1m}t_{m1}r_{m2}(r_{m2}r_{m1})^{n-1}$ |

这里使用 $k_1\sin\theta_1=k_m\sin\theta_m$；$n_m$ 为膜折射率，$\lambda$ 为波长。取入射振幅为1，反射场振幅为：

$$
\begin{aligned}
&r_{1m}+t_{1m}t_{m1}r_{m2}\sum_{n=1}^{\infty}(r_{m2}r_{m1})^{n-1}\exp(i2\pi n2n_mh_m\cos\theta_m/\lambda)\\
&=r_{1m}+\frac{t_{1m}t_{m1}r_{m2}\exp\!\left[i2\pi n_m2h_m\cos\theta_m/\lambda\right]}{1-r_{m2}r_{m1}\exp\!\left[i2\pi n_m2h_m\cos\theta_m/\lambda\right]}\\
&=\frac{r_{1m}+[-r_{1m}r_{m1}+t_{1m}t_{m1}]r_{m2}\exp\!\left[i2\pi n_m2h_m\cos\theta_m/\lambda\right]}{1-r_{m2}r_{m1}\exp\!\left[i2\pi n_m2h_m\cos\theta_m/\lambda\right]}\\
&=\frac{r_{1m}+r_{m2}\exp\!\left[i2\pi n_m2h_m\cos\theta_m/\lambda\right]}{1-r_{m2}r_{m1}\exp\!\left[i2\pi n_m2h_m\cos\theta_m/\lambda\right]}
\end{aligned}\tag{C.2}
$$

模平方给出光强，因此会随 $2n_mh_m\cos\theta_m/\lambda$ 出现干涉变化。波数扫描时，条纹间隔为 $\Delta\nu=1/(2n_mh_m\cos\theta_m)$。

> **译校注（Q057，保留原式）：** 上表净相位差的第一式与底本随后含 $2\pi$ 的式子，结合 $k_m=2\pi n_m/\lambda$，存在一个因子2的差别。正文与附录中的干涉周期及相位因子宜联查；这里不根据候选结果重写原式。

底本接着再次给出膜内点P的电场图和反射光路图，均保留：

![再次给出的膜内点P电场图（d等于膜厚）](../../../../%E4%B8%AD%E6%96%87%E7%89%88%E6%9C%AC/assets/ch02/s02/B080-p43-04.png)

*再次给出的膜内点P电场图（d等于膜厚）（底本p43，原图）。*

![再次给出的多重反射光路图（d等于膜厚）](../../../../%E4%B8%AD%E6%96%87%E7%89%88%E6%9C%AC/assets/ch02/s02/B080-p43-05.png)

*再次给出的多重反射光路图（d等于膜厚）（底本p43，原图）。*

*两图中的“媒質-1”“媒質-2”分别为介质1、介质2；其余符号与前图相同。底本图前“加重反射”按上下文译为多重反射，文字勘误见E-2.2-005。*

#### 透射光

“透射光”除直接穿过薄膜的光外，还包括进入膜内、多重反射后从 $m/2$ 界面出射的光。应对包含这些分量的总场，在 $2/m$ 界面应用边界条件。

到达 $(h_m\tan\theta_m,h_m)$ 的多重反射分量具有下列性质：

| 项目 | 表达式 |
|---|---|
| 入射点 | $(-2nh_m\tan\theta_m,0)$，$n=0,1,2,\ldots$；$n=0$ 为直接透射 |
| 入射点处光路差 | $-2nh_m\tan\theta_m\sin\theta_1$ |
| 相对于原点入射光的初始相位差 | $-2nh_mk_1\tan\theta_m\sin\theta_1$ |
| 膜内传播距离 | $(2n+1)h_m/\cos\theta_m$ |
| 膜内相位前进量 | $(2n+1)h_mk_m/\cos\theta_m$ |
| 相对于直接透射光的净相位差 | $2nh_mk_m\cos\theta_m$；底本亦写成 $2\pi nn_mh_m\cos\theta_m/\lambda$，疑点同Q057 |
| 透射与反射因子 | $t_{1m}t_{m2}(r_{m2}r_{m1})^n$ |

入射光的振幅和时间因子分别为1和 $e^{-i\omega t}$ 时，透射场如下；底本的求和式与闭式跨p43—44：

$$
\left[t_{1m}t_{m2}+t_{1m}t_{m2}\sum_{n=1}^{\infty}(r_{m2}r_{m1})^n\exp(in_m2\pi n2h_m\cos\theta_m/\lambda)\right]\exp(i2\pi n_mh_m\cos\theta_m/\lambda)
$$

$$
=\frac{t_{1m}t_{m2}\exp(i2\pi n_mh_m\cos\theta_m/\lambda)}{1-r_{m2}r_{m1}\exp\!\left[i2\pi n_m2h_m\cos\theta_m/\lambda\right]}\tag{C.3}
$$

取模平方得到光强，干涉变化由 $2n_mh_m\cos\theta_m/\lambda$ 控制；波数扫描时的条纹间隔为 $\Delta\nu=1/(2n_mh_m\cos\theta_m)$。反射光的峰对应透射光的谷。

#### 内部光

“内部光”定义为薄膜内部点P处的光。膜内同时存在下行（+）光和上行（−）光。先考察任意点 $(x,z)$，$0^+<z<h_m^-$。

下行（+）光的光路、相位及净电场如下：

| 项目 | 表达式 |
|---|---|
| 入射位置 | $[x-(2nh_m+z)\tan\theta_m,0]$，$n=0,1,2,\ldots$ |
| 入射点处光路差 | $[x-(2nh_m+z)\tan\theta_m]\sin\theta_1$ |
| 初始相位差 | $k_1[x-(2nh_m+z)\tan\theta_m]\sin\theta_1=k_m[x-(2nh_m+z)\tan\theta_m]\sin\theta_m$ |
| 入射后距离、相位前进量 | $(2nh_m+z)/\cos\theta_m$；$k_m(2nh_m+z)/\cos\theta_m$ |
| 净相位差 | $k_m[x\sin\theta_m+(2nh_m+z)\cos\theta_m]$ |
| 从 $m/2$ 出射的位置（原文） | $[x+(h_m-z)\tan\theta_m,0]$ |
| 至出射点的距离、相位前进量 | $(h_m-z)/\cos\theta_m$；$k_m(h_m-z)/\cos\theta_m$ |

下行净电场为

$$
\frac{t_{1m}\exp[-i\omega t+ik_m(x\sin\theta_m+z\cos\theta_m)]}
{1-r_{m2}r_{m1}\exp(i2k_mh_m\cos\theta_m)}.
$$

上行（−）光的对应结果为：

| 项目 | 表达式 |
|---|---|
| 入射位置 | $[x-(2nh_m-z)\tan\theta_m,0]$，$n=1,2,\ldots$ |
| 入射点处光路差 | $[x-(2nh_m-z)\tan\theta_m]\sin\theta_1$ |
| 初始相位差 | $k_1[x-(2nh_m-z)\tan\theta_m]\sin\theta_1=k_m[x-(2nh_m-z)\tan\theta_m]\sin\theta_m$ |
| 入射后距离、相位前进量 | $(2nh_m-z)/\cos\theta_m$；$k_m(2nh_m-z)/\cos\theta_m$ |
| 净相位差 | $k_m[x\sin\theta_m+(2nh_m-z)\cos\theta_m]$ |
| 从 $m/2$ 出射的位置（原文） | $[x+(h_m+z)\tan\theta_m,0]$ |
| 至出射点的距离、相位前进量（原文） | $(h_m+z)/\cos\theta_m$；$k_m(h_m+z)/\cos\theta_m$ |

上行净电场为

$$
\frac{t_{1m}r_{m2}\exp[-i\omega t+ik_m(x\sin\theta_m+(2h_m-z)\cos\theta_m)]}
{1-r_{m2}r_{m1}\exp(i2k_mh_m\cos\theta_m)}.
$$

> **译校注（Q058，保留原式）：** 两处“$m/2$ 出射”位置的第二坐标均写作0，而界面位于 $z=h_m$；上行光到背面所列 $h_m+z$ 也应结合先在前界面反射的路径核查。这些原式与位置标签均保留，不以直觉改写。

接着求出从原点向介质1侧出射的光所经过的膜内坐标；这束光若在 $m/1$ 界面反射，就从 $(h_m\tan\theta_m,h_m)$ 向介质2侧出射。在深度 $z$，将上行点记作 $A_0,A_1,A_2,\ldots$，下行点记作 $B_0,B_1,B_2,\ldots$；考察透射光时，B类还包括 $n=-1$。

**A类点：** $x=-(2nh_m+z)\tan\theta_m$，$n=0,1,2,\ldots$。到原点的相位前进量为 $k_m(2nh_m+z)/\cos\theta_m$；到背面出射点的相位前进量为 $k_m[(2n+1)h_m+z]/\cos\theta_m$。

存在入射光时，该处上下行电场为：

**上行（−）光的电场：**

$$
\frac{t_{1m}r_{m2}\exp[-i\omega t+ik_m(x\sin\theta_m+(2h_m-z)\cos\theta_m)]}{1-(r_{m2}r_{m1})\exp(ik_m2h_m\cos\theta_m)}
$$

**下行（+）光的电场：**

$$
\frac{t_{1m}\exp[-i\omega t+ik_m(x\sin\theta_m+z\cos\theta_m)]}{1-(r_{m2}r_{m1})\exp(ik_m2h_m\cos\theta_m)}
$$

**B类点：** 底本本处写为 $x=-[2(n+1)h_m-z]\tan\theta_m$，$n=(-1),0,1,2,\ldots$。到原点与背面出射点的相位前进量，底本均写作 $k_m[2(n+1)h_m-z]/\cos\theta_m$。

存在入射光时，该处上下行电场为：

**上行（−）光的电场：**

$$
\frac{t_{1m}r_{m2}\exp[-i\omega t+ik_m(x\sin\theta_m+(2h_m-z)\cos\theta_m)]}{1-(r_{m2}r_{m1})\exp(ik_m2h_m\cos\theta_m)}
$$

**下行（+）光的电场：**

$$
\frac{t_{1m}\exp[-i\omega t+ik_m(x\sin\theta_m+z\cos\theta_m)]}{1-(r_{m2}r_{m1})\exp(ik_m2h_m\cos\theta_m)}
$$

> **译校注（Q044、Q058）：** B点坐标与正文部分小节相差一个膜厚；这里两种出射点的传播相位又写成相同表达式。各处照录，留待结合图3.1与透射光路统一复核。

## 附录D. 介质之间极化薄片的L系数

正文所称“式（4.29）—（4.32）”，是将极化薄片所产生的SFG光经过无限薄片内多重反射、向两侧介质出射时的电场与极化联系起来的系数。下面从底本所称的片内L系数“式（4.33）—（4.36）”出发加以证明。

若介质1或介质2的厚度有限，必须考虑其中的多重反射，则下述分析还不充分，上述“式（4.29）—（4.32）”严格说来不能直接使用。

> **译校注（Q047，保留原引用）：** 本附录的（4.29）—（4.36）与现底本正文编号不匹配。本节界面和片内L系数实际集中于5.1，式（5.1a）—（5.5c）；这里只提供定位线索，不建立未经验证的一一换号关系。

考虑夹在介质1与介质2之间的极化薄片 $m$。向介质1侧出射的是上行（−）SFG光；计入片内多重反射后，各分量如下。

**s偏振：来自 $P_y$ 的贡献。**

$$
\begin{aligned}
E^{-}_{\mathrm{SF},s}&=\Bigl[L^-_{m/m,y}P_y\frac{1}{1-r_{m1,s}r_{m2,s}}+L^+_{m/m,y}P_y\frac{r_{m2,s}}{1-r_{m1,s}r_{m2,s}}\Bigr]t_{m1,s}\\
&=\frac{P_y}{2n_m\cos\theta_m}\frac{\left(n_1\cos\theta_1+n_m\cos\theta_m\right)\left(n_2\cos\theta_2+n_m\cos\theta_m\right)}{2n_m\cos\theta_m\left(n_1\cos\theta_1+n_2\cos\theta_2\right)}\frac{2n_m\cos\theta_m}{\left(n_2\cos\theta_2+n_m\cos\theta_m\right)}\\
&\quad\times\frac{2n_m\cos\theta_m}{\left(n_1\cos\theta_1+n_m\cos\theta_m\right)}\\
&=\frac{P_y}{\left(n_1\cos\theta_1+n_2\cos\theta_2\right)}=L^{-}_{1/2,y}P_y
\end{aligned}
$$

**p偏振：来自 $P_x$ 的贡献。** 推导跨p45—46：

$$
\begin{aligned}
E^{-}_{\mathrm{SF},p}(\text{来自 }P_x)&=\Bigl[L^-_{m/m,x}P_x\frac{1}{1-r_{m1,p}r_{m2,p}}+L^+_{m/m,x}P_x\frac{r_{m2,p}}{1-r_{m1,p}r_{m2,p}}\Bigr]t_{m1,p}\\
&=\frac{\cos\theta_m}{2n_m\cos\theta_m}P_x\frac{\left(n_1\cos\theta_m+n_m\cos\theta_1\right)\left(n_2\cos\theta_m+n_m\cos\theta_2\right)}{2n_m\cos\theta_m\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}\frac{2n_m\cos\theta_m}{\left(n_1\cos\theta_m+n_m\cos\theta_1\right)}\\
&\quad\times\frac{2n_m\cos\theta_2}{\left(n_2\cos\theta_m+n_m\cos\theta_2\right)}\\
&=\frac{\cos\theta_2}{\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}P_x=L^{-}_{1/2,x}P_x
\end{aligned}
$$

<!-- 介质1侧Px推导跨页续式已并入前式。 -->

**p偏振：来自 $P_z$ 的贡献。**

$$
\begin{aligned}
E^{-}_{\mathrm{SF},p}(\text{来自 }P_z)&=\Bigl[L^-_{m/m,z}P_z\frac{1}{1-r_{m1,p}r_{m2,p}}-L^+_{m/m,z}P_z\frac{r_{m2,p}}{1-r_{m1,p}r_{m2,p}}\Bigr]t_{m1,p}\\
&=\frac{\sin\theta_m}{2n_m\cos\theta_m}P_z\frac{\left(n_1\cos\theta_m+n_m\cos\theta_1\right)\left(n_2\cos\theta_m+n_m\cos\theta_2\right)}{2n_m\cos\theta_m\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}\frac{2n_m\cos\theta_m}{\left(n_1\cos\theta_m+n_m\cos\theta_1\right)}\\
&\quad\times\frac{2n_2\cos\theta_m}{\left(n_2\cos\theta_m+n_m\cos\theta_2\right)}\\
&=\frac{(n_2/n_m)\sin\theta_m}{\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}P_z=\frac{(n_2/n_m)^2\sin\theta_2}{\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}P_z=L^{-}_{1/2,z}P_z
\end{aligned}
$$

另一方面，向介质2侧出射的是下行（+）SFG光。计入片内多重反射，各分量如下。

**s偏振：来自 $P_y$ 的贡献。**

$$
\begin{aligned}
E^{+}_{\mathrm{SF},s}&=\Bigl[L^-_{m/m,y}P_y\frac{r_{m1,s}}{1-r_{m1,s}r_{m2,s}}+L^+_{m/m,y}P_y\frac{1}{1-r_{m1,s}r_{m2,s}}\Bigr]t_{m2,s}\\
&=\frac{P_y}{2n_m\cos\theta_m}\frac{\left(n_1\cos\theta_1+n_m\cos\theta_m\right)\left(n_2\cos\theta_2+n_m\cos\theta_m\right)}{2n_m\cos\theta_m\left(n_1\cos\theta_1+n_2\cos\theta_2\right)}\frac{2n_m\cos\theta_m}{\left(n_2\cos\theta_2+n_m\cos\theta_m\right)}\\
&\quad\times\frac{2n_m\cos\theta_m}{\left(n_1\cos\theta_1+n_m\cos\theta_m\right)}\\
&=\frac{P_y}{\left(n_1\cos\theta_1+n_2\cos\theta_2\right)}=L^{+}_{1/2,y}P_y
\end{aligned}
$$

**p偏振：来自 $P_x$ 的贡献。**

$$
\begin{aligned}
E^{+}_{\mathrm{SF},p}(\text{来自 }P_x)&=\Bigl[L^-_{m/m,x}P_x\frac{r_{m1,p}}{1-r_{m1,p}r_{m2,p}}+L^+_{m/m,x}P_x\frac{1}{1-r_{m1,p}r_{m2,p}}\Bigr]t_{m2,p}\\
&=\frac{\cos\theta_m}{2n_m\cos\theta_m}P_x\frac{\left(n_1\cos\theta_m+n_m\cos\theta_1\right)\left(n_2\cos\theta_m+n_m\cos\theta_2\right)}{2n_m\cos\theta_m\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}\frac{2n_m\cos\theta_1}{\left(n_1\cos\theta_m+n_m\cos\theta_1\right)}\\
&\quad\times\frac{2n_m\cos\theta_m}{\left(n_2\cos\theta_m+n_m\cos\theta_2\right)}\\
&=\frac{\cos\theta_1}{\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}P_x=L^{+}_{1/2,x}P_x
\end{aligned}
$$

**p偏振：来自 $P_z$ 的贡献。** 标题位于p46末，公式在p47：

$$
\begin{aligned}
E^{+}_{\mathrm{SF},p}(\text{来自 }P_z)&=\Bigl[L^-_{m/m,z}P_z\frac{r_{m1,p}}{1-r_{m1,p}r_{m2,p}}+L^+_{m/m,z}P_z\frac{1}{1-r_{m1,p}r_{m2,p}}\Bigr]t_{m2,p}\\
&=\frac{-\sin\theta_m}{2n_m\cos\theta_m}P_z\frac{\left(n_1\cos\theta_m+n_m\cos\theta_1\right)\left(n_2\cos\theta_m+n_m\cos\theta_2\right)}{2n_m\cos\theta_m\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}\frac{2n_m\cos\theta_m}{\left(n_1\cos\theta_m+n_m\cos\theta_1\right)}\\
&\quad\times\frac{2n_m\cos\theta_m}{\left(n_2\cos\theta_m+n_m\cos\theta_2\right)}\\
&=\frac{-(n_1/n_m)\sin\theta_m}{\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}P_z=\frac{-(n_1/n_m)^2\sin\theta_1}{\left(n_1\cos\theta_2+n_2\cos\theta_1\right)}P_z=L^{+}_{1/2,z}P_z
\end{aligned}
$$

证毕。

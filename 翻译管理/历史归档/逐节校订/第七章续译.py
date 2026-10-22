from pathlib import Path
import re,json,hashlib
import pypdfium2 as pdfium
R=Path(__file__).resolve().parents[2]
D=R/'中文版本/第七章 Heinz论文解读'
batches={}
def batch(n,s,pages,text):
    if s=='7.1':
        text=re.sub(r'^## (2\.[3-6] .*)$',r'### \1',text,flags=re.M)
        text=re.sub(r'^### (?!2\.|3\.)',r'#### ',text,flags=re.M)
    batches[n]=(s,pages,text.strip()+'\n')

batch(613,'7.1',[3],r'''
<!-- B613：PDF p3路径积分至2.2末；原式跳号照录。 -->
原论文巧妙地使用路径积分（这也是 Born & Wolf 采用的方法），导出了下列表达式。

$$\Delta B_z=B_z(z=0^+)-B_z(z=0^-)=0.\tag{5}$$

$$\Delta\boldsymbol H_t=\boldsymbol H_t(z=0^+)-\boldsymbol H_t(z=0^-)
=\frac{4\pi}{c}\frac{\partial\boldsymbol P}{\partial t}\times\boldsymbol n_z.\tag{7}$$

$$\Delta D_z=D_z(z=0^+)-D_z(z=0^-)=-4\pi\nabla_t\cdot\boldsymbol P(x,y).\tag{9}$$

其中，

$$\nabla_t=\boldsymbol n_z\frac{\partial}{\partial x}+\boldsymbol n_y\frac{\partial}{\partial y}.\tag{10}$$

$$\Delta\boldsymbol E_t=\boldsymbol E_t(z=0^+)-\boldsymbol E_t(z=0^-)
=-\frac{4\pi}{\varepsilon'}\nabla_tP_z.\tag{11}$$

> **原文疑点（Q278）：** 式(10)的首个单位矢量原印为 $\boldsymbol n_z$，与“面内梯度”及 $\partial/\partial x$ 不一致，候选为 $\boldsymbol n_x$；保留原印。式(7)、(9)、(11)沿用原文 $\boldsymbol P$，汇总式才明确写 $\boldsymbol P_s$。

最后一式偏离通常的连续条件，是按原论文图2b所示路径积分得到的结果。原作者解释说：对穿过薄片的 $E_z$ 作积分时，必须允许这一积分具有有限值。

汇总如下：

$$\Delta D_z=-4\pi\nabla_t\cdot\boldsymbol P_s,\tag{12a}$$

$$\Delta\boldsymbol E_t=-\frac{4\pi}{\varepsilon'}\nabla_tP_{s,z},\tag{12b}$$

$$\Delta B_z=0,\tag{12c}$$

$$\Delta\boldsymbol H_t=\frac{4\pi}{c}\frac{\partial\boldsymbol P_s}{\partial t}\times\boldsymbol n_z.\tag{12d}$$

即使极化薄片的线性响应并非各向同性，只要它在 $(x,y,z)$ 系中为对角形式，把 $\varepsilon'$ 换成 $\varepsilon'_{zz}$，上述四式仍然成立。

> **译者记号说明：** 原句将 $\varepsilon'$ 称为“线性极化率”。这里所指仍是前文定义的膜层介电常数，不能据此将其等同于 $\chi^{(1)}$；原文的命名差异予以标明。
''')
batch(614,'7.1',[3,4,5],r'''
<!-- B614：PDF p3的2.3至p5首行。 -->
## 2.3 极化薄片的辐射

原论文讨论的是二次谐波产生（SHG）；这里尝试将其改写为和频过程（SFG）。把两个平面波在表面诱导的极化看作极化薄片，写成

$$\boldsymbol P(x,y,z,t)=\boldsymbol P_s(x,y,t)\delta(z),\tag{13a}$$

$$\boldsymbol P_s(x,y,t)=\boldsymbol P_s\exp(ipx-i\Omega t)+\mathrm{c.c.}\tag{13b}$$

（c.c. 表示紧邻其前的一项的复共轭，即 $e^{ia}$ 对应的 $e^{-ia}$。）

由面二阶非线性极化率 $\chi_s^{(2)}$ 引起的源项 $\boldsymbol P_s$，稍后再详细讨论。现在只需知道，它可以作为以波矢 $p\boldsymbol u_x$ 和频率 $\Omega$ 描述、并在空间中变化的薄片来处理。极化薄片向介电常数为 $\varepsilon_1$ 的介质1辐射“反射光”，向介电常数为 $\varepsilon_2$ 的介质2辐射“透射光”。

反射光的波矢为

$$\boldsymbol k_1=p\boldsymbol u_x-q_1\boldsymbol u_z.\tag{14a}$$

$p$ 与 $q_1$ 分别表示波矢的 $x$ 分量及法向分量的大小；$p$ 在两个介质中相同。

$$q_1=\sqrt{\varepsilon_1K^2-p^2}.\tag{14b}$$

$K=\Omega/c$ 为自由空间波数，$\varepsilon_1$ 为频率 $\Omega$ 下的介电常数。所考虑的波离开界面传播，因此，当 $\varepsilon_1$ 为实数且 $p^2<\varepsilon_1K^2$ 时，须取 $q_1>0$。更一般地，若 $p^2>\varepsilon_1K^2$ 或 $\varepsilon_1$ 为复数，波随远离界面而衰减，此时式(14b)中的 $q_1$ 应具有非负的虚部。

透射光满足

$$\boldsymbol k_2=p\boldsymbol u_x+q_2\boldsymbol u_z,\tag{15a}$$

$$q_2=\sqrt{\varepsilon_2K^2-p^2}.\tag{15b}$$

这里也有 $q_2>0$（更一般地，$\operatorname{Im}q_2>0$）。

> **译者说明：** 此处“$>0$”按原文保留；前一段对 $q_1$ 使用的是“虚部非负”。无损传播波的虚部可以为零，应用时须结合传播或衰减分支选择，不能机械要求所有情形均严格大于零。

同一极化薄片成对产生的反射波和透射波，在薄片两侧满足式(12)。为简化讨论，先取 $\varepsilon_1=\varepsilon_2=\varepsilon'$，则两个介质中的光电场为

$$\boldsymbol E_i(x,y,z,t)=\boldsymbol E_i(\Omega)\exp(i\boldsymbol k_i\boldsymbol x-i\Omega t)+\mathrm{c.c.}\tag{16}$$

$$\boldsymbol E_i=\boldsymbol E_i(\Omega)=\frac{2\pi iK^2}{q_i}
\left[\boldsymbol P_{sv}-\boldsymbol u_{ki}(\boldsymbol u_{ki}\cdot\boldsymbol P_s)\right].\tag{17}$$

> **原文疑点（Q279）：** 式(17)方括号内第一项原印为 $\boldsymbol P_{sv}$，后文解释则为 $\boldsymbol P_s$；候选是多印了下标 $v$。式(16)保留原式波矢与位置矢量的并置写法，按平面波语境理解为内积。

$\boldsymbol u_{ki}$ 是沿光传播方向的单位矢量，$\boldsymbol u_{ki}=\boldsymbol k_i/(\boldsymbol k_i\cdot\boldsymbol k_i)^{1/2}$。式(17)括号内表示从 $\boldsymbol P_s$ 中减去沿 $\boldsymbol u_{ki}$ 的投影。因此，辐射电场正比于源极化的横向分量，并垂直于光的传播方向。

引入偏振方向单位矢量 $\boldsymbol e_i$，满足 $\boldsymbol k_i\cdot\boldsymbol e_i=0$，则

$$\boldsymbol e_i\cdot\boldsymbol E_i=\frac{2\pi iK^2}{q_i}(\boldsymbol e_i\cdot\boldsymbol P_s).\tag{18}$$

将式(17)右边与 $\boldsymbol u_{ki}$ 作内积即可看出，$\boldsymbol E_i$ 垂直于 $\boldsymbol u_{ki}$。所以 $\boldsymbol E_i$ 和 $\boldsymbol e_i$ 都在垂直于传播方向的平面内，式(18)给出电场在 $\boldsymbol e_i$ 上的投影。（进行圆偏振或椭圆偏振实验时，需要这项讨论。）

无论如何，从式(16)至此的讨论只适用于 $\varepsilon_1=\varepsilon_2=\varepsilon'$，不具有一般性。去除此近似的一般推导见[附录A（7.2）](7.2%20附录A：去除等介电常数近似的式17推导.md)；用于实际体系的表达式请参阅该附录。
''')
batch(615,'7.1',[5],r'''
<!-- B615：PDF p5线性响应与式(19)—(20)、折射率表示。 -->
### 线性响应与菲涅尔变换

体相和薄膜都具有线性响应。要将其纳入，只需考虑适当的菲涅尔变换。为对称地处理界面激发和由该激发产生的辐射，可以对入射光——即从两个体相进入介电常数为 $\varepsilon'$ 的膜的光——作菲涅尔修正。

用 $\boldsymbol e_i$ 表示介质1或2中光电场的偏振矢量，满足 $\boldsymbol k_i\cdot\boldsymbol e_i=0$。若光在介质 $i$ 中朝介质 $j$ 传播，电场为 $E_0\boldsymbol e_i$，那么它在界面区域产生的电场可写为 $E_0\boldsymbol e$，其中

$$\boldsymbol e=\boldsymbol F_{i\to j}\boldsymbol e_i.\tag{19}$$

分别考虑 s、p 偏振后，可用透射系数表示 $\boldsymbol F_{i\to j}$。若 $\varepsilon_1=\varepsilon'$ 或 $\varepsilon_2=\varepsilon'$，折射率相同的界面不发生反射，便得到通常的菲涅尔因子。若膜的介电常数与两侧都不同，则在图示坐标系中表示变换较方便。各向同性体相对应

$$\boldsymbol F_{i\to j}=F^{xx}_{i\to j}\hat{\boldsymbol x}\hat{\boldsymbol x}+F^{yy}_{i\to j}\hat{\boldsymbol y}\hat{\boldsymbol y}+F^{zz}_{i\to j}\hat{\boldsymbol z}\hat{\boldsymbol z},\tag{20a}$$

$$F^{xx}_{i\to j}=\frac{2\varepsilon_iq_j}{\varepsilon_jq_i+\varepsilon_iq_j},\tag{20b}$$

$$F^{yy}_{i\to j}=\frac{2q_i}{q_i+q_j},\tag{20c}$$

$$F^{zz}_{i\to j}=\frac{2(\varepsilon_i\varepsilon_j/\varepsilon')q_i}{\varepsilon_jq_i+\varepsilon_iq_j}.\tag{20d}$$

$q_i$（$i=1,2$）是式(14b)、(15b)定义的法向波矢量；与附录A的记号对应为 $q_1=-k_{1z}$、$q_2=k_{2z}$。推导见[附录B（7.3）](7.3%20附录B：式20的推导.md)。

这些式子描述穿过膜到达另一侧的光与入射光的关系。除 $z$ 分量外，膜的介电常数都不出现，所以 $x$、$y$ 分量与无膜时相同。（广濑对有限厚度膜所作的推导——其他推导也有——在膜厚趋于零时也给出这一关系。）

实际使用时，往往采用折射率而非介电常数。追踪膜的生长还需要适用于不可忽略膜厚的表达式。下面先把式(20)写为折射率和波数的形式，再将膜内光场分成两个传播方向，纳入多重反射。

![式20的折射率与波数表示，四行完整保留](../assets/7.1/p5-折射率.png)

> **公式保真说明：** 本章较长的原式组采用清晰原式图，正文与解释均译为中文。图内的系数、上下标和推导中间步骤保持原印；这些公式图尚非可编辑的 LaTeX。
''')
batch(616,'7.1',[5,6],r'''
<!-- B616：PDF p5末跨p6，上下行膜内场及式(21)—(22)。 -->
### 膜内两个传播方向的场

膜内光场包括朝介质1传播、波矢为 $\boldsymbol k_s=k_x\boldsymbol u_x-q_m\boldsymbol u_z$ 的“向上光、反射光”，以及朝介质2传播、波矢为 $\boldsymbol k_s=k_x\boldsymbol u_x+q_m\boldsymbol u_z$ 的“向下光、透射光”。原文称“式(20b)至式(29d)”给出两者电场的矢量和。考虑不可忽略的膜厚时，还需要分别给出两个方向的系数。

> **原文交叉引用疑点（Q280）：** 原印“(29d)”在本节并不存在，按上下文候选为“(20d)”；保留原引用并说明。两个方向原文都记 $\boldsymbol k_s$，这里按原记号区分其正负号。

**向上光：**

![式20′b—20′d，向上光的三个分量](../assets/7.1/p6-向上.png)

**向下光：**

![式20″b—20″d，向下光的三个分量](../assets/7.1/p6-向下.png)

膜内多重反射的处理见[附录C（7.4）](7.4%20附录C：式20的折射率表示与多重反射.md)。

由式(19)、(20)可得膜内偏振矢量的表达式，从而把线性响应——即介质间介电常数的差别——纳入极化薄片的辐射，得到

$$\boldsymbol e_i\cdot\boldsymbol E_i=2\pi i q_i^{-1}K^2(\boldsymbol e\cdot\boldsymbol P_s),\qquad K=\omega/c.\tag{21}$$

也可写成

$$\boldsymbol e_i\cdot\boldsymbol E_i=2\pi i\frac{K}{\sqrt{\varepsilon_i}}\sec\theta_i(\boldsymbol e\cdot\boldsymbol P_s),\tag{22a}$$

$$\sec\theta_i=\frac{\sqrt{\varepsilon_iK}}{q_i}.\tag{22b}$$

在没有吸收等损耗时，$\theta_i$ 是光的传播方向与表面法线之间的夹角。

> **原文疑点（Q281）：** 式(22b)原式根号覆盖 $\varepsilon_iK$；由式(21)、(22a)及 $q_i=\sqrt{\varepsilon_i}K\cos\theta_i$ 比较，候选为 $\sqrt{\varepsilon_i}K/q_i$。保留原式，不把候选直接代入。
''')
batch(617,'7.1',[6,7],r'''
<!-- B617：PDF p6—7式(21)证明框全部。 -->
### 式(21)的证明

由附录A的结果，即式(A9)、(A10)，有

![证明起点：两个p偏振振幅](../assets/7.1/p6-证明起点.png)

![证明起点续：两个s偏振振幅相等](../assets/7.1/p7-s振幅.png)

将其变形如下：

![五行笛卡尔分量变形，E1x、E2x、E1y与E2y、E1z、E2z](../assets/7.1/p7-分量变形.png)

这里使用以下关系：

![s、p偏振单位矢量及其电场投影关系](../assets/7.1/p7-偏振关系.png)

因此，

![E1p和E2p各四行推导，中间步骤及末行均保留](../assets/7.1/p7-证明末组.png)

此外，由于定义为 $\boldsymbol e=\boldsymbol F_{i\to j}\boldsymbol e_i$，所以 $\boldsymbol e_2$ 与 $\boldsymbol e$ 的关系必须从 $\boldsymbol e=\boldsymbol F_{2\to1}\boldsymbol e_2$ 导出。

> **原文疑点（Q282）：** 证明框中的单位矢量关系把两个 p 偏振矢量都标成 $\boldsymbol e_{2p}$，其中含 $\theta_1$ 的一个候选为 $\boldsymbol e_{1p}$。末组出现 $k_1k_2/k_m$，而前面的介电常数比涉及波数平方；又在改写为偏振矢量后，原先的法向波数分母不再出现，末行与式(21)的 $q_i^{-1}$ 因子不一致。原式图保留每一步，尚不能据此认定证明闭合；需对照原综述及附录A、B复算。此处 $\boldsymbol e_1,\boldsymbol e_2$ 与修正后的 $\boldsymbol e$ 的混用也一并待核。
''')
batch(618,'7.1',[7,8,9],r'''
<!-- B618：PDF p7的2.4至p9首段计算说明。 -->
## 2.4 表面非线性响应

为完成唯象模型的表述，下面考察此前使用的非线性极化薄片与表面二阶非线性极化率张量之间的关系。基本式为

$$\boldsymbol P_s(\omega)=\chi_s^{(2)}(\omega=\omega_1+\omega_2):\boldsymbol E(\omega_1)\boldsymbol E(\omega_2).\tag{23}$$

这里的 $\boldsymbol E(\omega_1)$、$\boldsymbol E(\omega_2)$ 是介电常数为 $\varepsilon'$ 的介质内部的电场 $\boldsymbol E_m$ 或 $\boldsymbol E_{m'}$。把激发光视为平面波，从介质 $i$ 一侧入射的电场为

$$\begin{aligned}
\boldsymbol E_i(x,y,z,t)&=\boldsymbol E_i(\omega)\exp(i\boldsymbol k_i\cdot\boldsymbol x-i\omega t)+\mathrm{c.c.}\\
&=E_i(\omega)\boldsymbol e_i(\omega)\exp(i\boldsymbol k_i\cdot\boldsymbol x-i\omega t)+\mathrm{c.c.}
\end{aligned}\tag{24}$$

式中 $\omega$ 表示 $\omega_1$ 或 $\omega_2$，$\boldsymbol e_i(\omega)$ 是单位矢量。（按广濑在附录中的记号，下标 $i$ 则为 $m$。）把介质 $i$ 内波矢的正 $z$ 分量的大小记为 $q_i$，朝界面传播的激发光波矢为

$$\boldsymbol k_1=p\boldsymbol u_x+q_1\boldsymbol u_z\quad\text{（从介质1到界面）},\tag{25a}$$

$$\boldsymbol k_2=p\boldsymbol u_x-q_2\boldsymbol u_z\quad\text{（从介质2到界面）},\tag{25b}$$

$$q_i=\sqrt{\varepsilon_i(\omega/c)-p^2}.\tag{26}$$

（设激发光在 $xz$ 平面内传播，即入射面为 $xz$ 面。）

> **原文疑点（Q283）：** 式(26)的 $\omega/c$ 原印没有平方，与式(14b)、(15b)及量纲不符，候选为 $\sqrt{\varepsilon_i(\omega/c)^2-p^2}$。式(24)后括注把介质侧下标 $i$ 对应到膜内 $m$，而后文又区分两者，按原文保留，不能将外场直接当作膜内场。

在这一定义下有

$$\boldsymbol P_s(\omega)=\chi_s^{(2)}(\omega=\omega_1+\omega_2):\boldsymbol e_{i1}(\omega_1)\boldsymbol e_{i2}(\omega_2)E_{i1}(\omega_1)E_{i2}(\omega_2).\tag{27}$$

这里的 $\boldsymbol e_{i1}(\omega_1)$、$\boldsymbol e_{i2}(\omega_2)$，原文称为对激发光场施加菲涅尔因子修正后得到的偏振矢量〔式(20)、(19)〕，即

$$\boldsymbol e(\omega)=\boldsymbol F_{i\to j}\boldsymbol e_i(\omega),\qquad i=i1\text{ 或 }i2.\tag{28}$$

（广濑原注：多半，这一式子是把下列关系写成一般形式。）

$$\boldsymbol e(\omega_1)=\boldsymbol F_{i1\to j}\boldsymbol e_{i1}(\omega_1),\qquad
\boldsymbol e(\omega_2)=\boldsymbol F_{i2\to j}\boldsymbol e_{i2}(\omega_2).$$

这里考虑光从介质 $i$ 穿过界面进入介质 $j$。将相应频率的介电参数和式(26)给出的 $q_i$ 代入式(20)，便得到所用的 $\boldsymbol F$。

> **记号待核（Q284）：** 原文式(27)用带介质下标的 $\boldsymbol e_{i1},\boldsymbol e_{i2}$ 表示已经修正的矢量，但式(28)将 $\boldsymbol e_i$ 放在修正前一侧，式(29)又使用无下标 $\boldsymbol e$。两套记号不能未经核验互换。原文此处还把用于菲涅尔因子的介电参数称为“极化率”；结合式(20)，这里指 $\varepsilon$，不是额外引入的 $\chi$。

结合式(22)和式(27)，将界面和频过程与体相电场联系起来：

$$\boldsymbol e_i(\omega)\cdot\boldsymbol E_i(\omega)=
\frac{2\pi i\omega\sec\theta_i(\omega)}{c\sqrt{\varepsilon_i(\omega)}}
\left[\boldsymbol e(\omega)\cdot\chi_s^{(2)}:\boldsymbol e(\omega_1)\boldsymbol e(\omega_2)\right]
E_{i1}(\omega_1)E_{i2}(\omega_2).\tag{29}$$

此式给出由介质 $i1$ 中的激发光 $\boldsymbol e_{i1}(\omega_1)$ 和介质 $i2$ 中的激发光 $\boldsymbol e_{i2}(\omega_2)$ 共同激发的和频光电场振幅及偏振矢量；对任一输出介质 $i=1,2$ 均适用。

计算所需的膜内偏振矢量 $\boldsymbol e(\omega)$、$\boldsymbol e(\omega_1)$、$\boldsymbol e(\omega_2)$，由式(19)、(20)求出。波矢的面内分量为 $p(\omega_1)$、$p(\omega_2)$、$p(\omega)=p(\omega_1)+p(\omega_2)$，垂直分量则用式(14)、(15)、(26)计算。（也就是说，先求各介质中相同的面内分量，再算垂直分量。）由 $\theta_i$ 为光路与界面法线的夹角，可得

$$\sec\theta_i(\omega)=\frac{\sqrt{\varepsilon_i(\omega)}\,\omega}{cq_i(\omega)}.$$

（广濑原注：原文的语法有问题。）
''')
batch(619,'7.1',[9,10],r'''
<!-- B619：PDF p9各向异性与不同入射面至p10的式32参数定义。 -->
### 一般入射几何与辐照度

只要 $\varepsilon_1$、$\varepsilon_2$、$\varepsilon'$ 各向同性，即便它们为复数，式(29)也成立。若膜层各向异性，但具有张量主轴，可写成

$$\boldsymbol\varepsilon'=\varepsilon'_{xx}\hat{\boldsymbol x}\hat{\boldsymbol x}+\varepsilon'_{yy}\hat{\boldsymbol y}\hat{\boldsymbol y}+\varepsilon'_{zz}\hat{\boldsymbol z}\hat{\boldsymbol z},$$

则把 $\varepsilon'$ 换为 $\varepsilon'_{zz}$ 后也可使用。

此前推导假定两个激发光共用同一入射面，但式(29)适用于更一般的情况。式(20)中的菲涅尔变换是以 $xz$ 为入射面写出的，用于其他几何时须作相应变换。两个激发光的入射面不同时，还须根据下面的面内波矢关系，以及介质 $i$ 中的线性色散式〔式(14)、(15)，其中取 $p^2=\boldsymbol p(\omega)\cdot\boldsymbol p(\omega)$〕求出和频光方向：

$$\boldsymbol p(\omega)=\boldsymbol p(\omega_1)+\boldsymbol p(\omega_2).\tag{30}$$

为用两个输入频率的辐照度（irradiance）表示频率 $\omega$ 的输出辐照度，采用平面波关系

$$I=\frac{c\sqrt\varepsilon\,|E|^2}{2\pi}.$$

由式(29)得到

![式31：输出辐照度与两个输入辐照度的关系](../assets/7.1/p9-式31.png)

$I_{i1}(\omega_1)$ 是从介质 $i1$ 入射的 $\omega_1$ 光辐照度；$I_{i2}(\omega_2)$ 是从介质 $i2$ 入射的 $\omega_2$ 光辐照度；$I_i(\omega)$ 是以偏振矢量 $\boldsymbol e_i(\omega)$ 向介质 $i$ 输出的和频光辐照度。这里 $\boldsymbol e_i(\omega)$ 对应经过适当菲涅尔修正后的 $\boldsymbol e(\omega)$。

> **原文疑点（Q285）：** 式(31)的频率因子原印为 $\omega^3$，后续式(32)、(33a)则为 $\omega^2$；从式(29)的振幅平方及平面波辐照度关系复算时，也应核验此前因子。式(31)角度的频率自变量原写 $\omega_i$，未另行定义。保留原式图，不作无注释统一。

与实验比较时，更方便的是有限空间宽度激发光束产生的和频光总功率。假设几何光学适用，可由式(31)得到以下结果。

若两个激发光的传播方向和尺寸均相同，以 $A$ 为光束横截面积，则以偏振 $\boldsymbol e_i(\omega)$ 向介质 $i$ 辐射的和频光总功率为

![式32：传播方向及尺寸相同的两个光束对应的总功率](../assets/7.1/p9-式32.png)

其中，$P_{i1}$、$P_{i2}$ 为激发光总功率，$\theta_{i1}$、$\theta_{i2}$ 为激发光入射角。
''')
batch(620,'7.1',[10],r'''
<!-- B620：PDF p10任意光束至2.5前。 -->
### 有限光束与空间重叠

当激发光具有任意空间宽度（束径）时，

![式33a：任意光束宽度对应的输出功率](../assets/7.1/p10-式33a.png)

式中 $A(\omega)$ 是用光束总功率 $P(\omega)$ 除以代表性辐照度 $I^0(\omega)$——中心或峰值处的值——所定义的有效面积：

$$A(\omega)=P(\omega)/I^0(\omega).\tag{33b}$$

两个激发光束的重叠由无量纲因子 $f$ 表示：

![式33c：光束重叠积分，分子保留面积乘积的平方根](../assets/7.1/p10-式33c.png)

积分在非线性膜的平面上进行。

当共线的高斯激发光聚焦在界面上，并在界面形成束腰时，由式(21)〔原文如此引用〕有 $A(\omega_1)=\pi r_1^2$、$A(\omega_2)=\pi r_2^2$。也就是说，设强度分布为 $\exp(-r^2/r_0^2)$，按束中心测得的强度计算。（广濑原注：是否将总强度除以中心强度定义为面积，再由此求出 $r$？）此时

$$f=\frac{\cos\theta_i(\omega)/\cos\theta(\omega)}{r_1/r_2+r_2/r_1},\qquad\theta(\omega)\text{：入射角。}$$

> **译者说明：** 原文高斯光束段的式(21)引用与主题未直接对应，暂按原引用保留，见Q280的交叉引用待核项。式(33a)、(33c)中的面积乘积均在平方根内，不能按文本层提取结果漏掉根号。此处 $P$ 表示光功率，与前文的极化矢量 $\boldsymbol P$ 区分。
''')
batch(621,'7.1',[10,11,12],r'''
<!-- B621：PDF p10的2.5至p12首段。 -->
## 2.5 体相非线性响应

考虑体相极化时，按非局域性（nonlocality）的程度作多极展开。（例如，电荷分布仅向两侧分开时是偶极分布，呈纺锤状时是四极分布，等等。）

$$\begin{aligned}
\boldsymbol P^{\mathrm{nls}}(\omega)={}&\chi^{(2)}(\omega=\omega_1+\omega_2):\boldsymbol E(\omega_1)\boldsymbol E(\omega_2)\\
&+\tfrac12\chi_q^{(2)}(\omega=\omega_1+\omega_2):\boldsymbol E(\omega_1)\nabla\boldsymbol E(\omega_2)\\
&+\tfrac12\chi_q^{(2)}(\omega=\omega_1+\omega_2):\boldsymbol E(\omega_2)\nabla\boldsymbol E(\omega_1).
\end{aligned}\tag{34}$$

以 $a$ 为原子尺度，以 $l$ 为电场显著改变的空间尺度，则式(34)第二、三项相对于第一项的贡献可按 $a/l$ 估计。$a\sim1\,\text{Å}$，$a/l\sim ka$；可见光的波数约为 $10^{-3}\,\text{Å}^{-1}$，所以 $a/l\ll1$。在均匀体相内，展开应当很快收敛，因此描述体相响应时，只需考虑首个非零项。

当第一项（电偶极项）为零时，界面、表面研究便获得一个有用的切入点。典型例子是具有中心对称（反演对称）的体系。进一步限于 SHG 时，即使无中心对称，各向同性体系及具有432（$O$）对称性的晶体也属于这种情形。

对于液体、气体等无序物质，应考虑宏观体积上的平均。若无中心对称的分子随机取向，只有分子为手性分子时，宏观体系才不具有中心对称。原文接着说：只有分子点群的对称元素中不含“反演”操作和“旋转”操作时，体相中心对称才被破坏，偶极项才非零。

> **原文疑点（Q286）：** 上句“旋转”按日文原印保留；手性点群可以含正常旋转轴，疑为涉及非正常旋转的用词错误，不能把这句话作为手性点群的一般判据。原文又在讨论体相贡献时写 $\chi_s^{(2)}$，其中面下标与语境不一致，亦保留待核。

非相干的非线性辐射则略有不同：在液体、非晶固体等能形成局部非中心对称结构的体系中，应有可能观测到这一现象。

有时可巧妙选择激发光和和频光的偏振组合，消去体相电偶极项。适用条件是体相对称性高、独立的 $\chi_s^{(2)}$ 分量少，例如具有 $T_d$ 对称性的 GaAs。

现在转向体相不含电偶极项的情形。此时最低阶非零项是电四极项和磁偶极项，它们由电场与电场空间导数的乘积表示。

**［广濑原作中略：原综述用约两页讨论 SHG 中的四极项。这里只摘录对 SFG 也可能有意义的部分。］**

对于具有 $m3m\,(O_h)$ 或 $432\,(O)$ 对称性的立方介质，以 $i,j$ 表示晶轴，独立张量分量为

$$\chi^{(2)}_{q,iiii},\quad\chi^{(2)}_{q,iijj},\quad\chi^{(2)}_{q,ijij},\quad\chi^{(2)}_{q,ijji}.$$

二次谐波极化的 $i$ 分量为

![式36：体相二次谐波极化的分量](../assets/7.1/p11-式36.png)

上述唯象参数定义为

![式37a—37d：β、γ、δ、ζ的定义](../assets/7.1/p11-式37.png)

> **原文疑点及局部符号（Q287）：** 式(37d)括号末项原印 $\chi^{(2)}_{q,ijj}$，比其他四指标分量少一个指标，候选为 $\chi^{(2)}_{q,ijji}$，保留原图。本处 $\beta,\gamma,\delta,\zeta$ 是体相四极响应的唯象参数，不能套用前章分子一阶、二阶超极化率的命名。

$\beta$、$\gamma$、$\delta$ 描述各向同性响应。在均匀介质中，式(36)第三项可忽略〔麦克斯韦方程给出 $\nabla\cdot\boldsymbol E=\nabla\cdot\varepsilon^{-1}\boldsymbol D=0$〕。在单频平面波范围内，激发电场为横向场，所以第二项也可忽略。但只要不使用圆偏振，第一项总是存在，并具有“沿 $\boldsymbol k_i$ 方向振荡，即 transverse”的 $P_i$。各向同性体系中 $\zeta=0$。

> **原文疑点（Q288）：** 原文将“沿波矢方向”称为 transverse（横向），两者相矛盾；下文讨论将该 $\gamma$ 项称为 longitudinal（纵向）。这里照录并指出差异，不把原词悄然改为纵向。
''')
batch(622,'7.1',[12,13],r'''
<!-- B622：PDF p12“372页中段起”至p13首句，式38—40。 -->
### 体相极化与表面极化

**［广濑原注：从原综述第372页中段起。］**

用单一波矢 $\boldsymbol k_b$ 表示体相非线性极化：

$$\boldsymbol P(x,y,z,t)=\boldsymbol P_b(\omega,\boldsymbol k_b)
\exp(i\boldsymbol k_b\cdot\boldsymbol x-i\omega t)\theta(z)+\mathrm{c.c.}\tag{38}$$

$\theta(z)$ 是阶跃函数，表示假定介质1一侧没有非线性极化。$\boldsymbol k_b$ 可取为两个激发光波矢之和。向介质1输出的光的方向由 $\boldsymbol k_b$ 平行于界面的分量匹配决定。因此，描述体相非线性极化的辐射时，也可将它替换成放在界面上的一张极化薄片：

$$\boldsymbol P_s^{\mathrm{eq}}(x,y,z,t)=\boldsymbol P_s^{\mathrm{eq}}(\omega,\boldsymbol k_b)
\exp(i\boldsymbol k_b\cdot\boldsymbol x-i\omega)\delta(z)+\mathrm{c.c.}\tag{39}$$

> **原文疑点（Q289）：** 式(39)指数中原印 $-i\omega$，缺少时间 $t$，候选为 $-i\omega t$；保留原式。这里 $\theta$ 是阶跃函数，与前文入射角的同字母记号无关。

上标 eq 表示用等效薄片表示实际极化。为考虑深度效应，将体相看作多张极化薄片的叠加，并计入源极化相位（两个激发波矢之和与位置矢量的内积）与介质2内非线性光相位（和频波矢与位置矢量的内积）之间的差，得到

![式40：体相非线性极化对应的等效面极化](../assets/7.1/p12-式40.png)

其中 $q_b$ 是 $\boldsymbol k_b$ 的 $z$ 分量，$q_2$ 是介质2中频率 $\omega$ 光波的法向波矢。$P_{b,z}$ 前的系数来自把极化薄片看作位于介电常数 $\varepsilon'(\omega)$ 的介质中。体相产生的非线性光可再用式(21)等具体写出。

式(40)的含义是：描述从体相向介质1辐射的光时，决定非线性极化有效大小的是距离界面不超过相干长度 $l_c=(q_s+q_2)^{-1}$ 的体相极化。在“反射”配置中，$q_s$、$q_2$ 都为正，相干长度较短。原文括注为

$$q=q_2:\qquad l_c=\left|\frac{\Lambda}{2\cos\theta_2(\omega)}\right|,\qquad
\Lambda=\frac{2\pi c}{\omega\sqrt{\varepsilon_2(\omega)}};$$

$$\cos\theta_2(\omega)=\frac{(\omega/c)q_2}{\sqrt{\varepsilon_2(\omega)}}.$$

$\Lambda$ 为介质2内部的波长。若泵浦光从介质2一侧入射，相干长度会大得多。

> **原文疑点（Q290）：** 式(40)用 $q_b$，随后的相干长度却写 $q_s$；括注又写未加下标的 $q=q_2$。原式 $l_c=(q_s+q_2)^{-1}$ 与使用波长 $\Lambda$ 的表达式存在 $2\pi$ 因子的核验问题，且所印余弦关系的 $\omega/c$ 位置也与色散关系不符。候选应从 $q_2=\sqrt{\varepsilon_2}(\omega/c)\cos\theta_2$ 重新推导，尚未采用修正。

就“反射”而言，相干长度约为 $\Lambda$ 的量级，式(40)给出的有效面极化约为 $\Lambda P_b$。另一方面，四极项相对于电偶极项约为 $a/\Lambda$。因此，以 $P_d$ 表示电偶极允许的非线性源极化，反射配置中体相项的等效面极化约为 $P_s^{\mathrm{eq}}\sim aP_d$，即与界面区域贡献同量级。不过，对于介电常数较大的物质，体相内的屏蔽可能减小体相贡献。

由于式(40)中的体相项含相干长度，原则上可通过改变激发光入射角，区分体相项与表面项。
''')
batch(623,'7.1',[13],r'''
<!-- B623：PDF p13余下，纵向体相响应与等效表面响应。 -->
### 纵向体相响应与表面项的不可区分性

**［广濑原注：随后三页讨论四极项，这里只记要点。］**

在各向同性且均匀的介质中，体相非线性源极化的最低阶非局域项具有

$$\boldsymbol P(\omega)=\gamma\nabla(\boldsymbol E\cdot\boldsymbol E)
+(\delta-\beta-2\gamma)(\boldsymbol E\cdot\nabla)\boldsymbol E$$

的形式。第一项，即纵向极化产生的辐射，不能与界面辐射区分。纵向极化（$\gamma$ 项）产生的 p 偏振振幅正比于 $\boldsymbol e_p\cdot\boldsymbol P_s^{\mathrm{eq}}$。这里 $\boldsymbol e_p$ 为 p 偏振矢量，而 $\boldsymbol P_s^{\mathrm{eq}}$ 是体相非线性极化

$$\boldsymbol P_b(\omega)=i\gamma\boldsymbol k_s[\boldsymbol E(\omega_i)\cdot\boldsymbol E(\omega_j)]$$

对应的等效面极化。

![式41：纵向体相极化的投影与等效面极化的对应，完整四行](../assets/7.1/p13-式41.png)

$$\boldsymbol P_s^\gamma(\omega)=-\gamma\frac{\varepsilon'}{\varepsilon_2}
[\boldsymbol E(\omega_i)\cdot\boldsymbol E(\omega_j)]\boldsymbol u_z
\quad\text{（面极化）}.\tag{42}$$

引入 $\boldsymbol P_s^\gamma\parallel\boldsymbol u_z$ 这一面极化性质后，不使用 $\boldsymbol k_s$ 也能重现纵向体相极化的角度和偏振特征。因此，体相纵向极化与面极化的 $z$ 分量不可区分。

当介质1、2都具有非线性时，有

![式46：两侧介质都有非线性时的等效面极化](../assets/7.1/p13-式46.png)

相应的等效面二阶非线性极化率为

![式47a—47b：等效面张量的两个分量](../assets/7.1/p13-式47.png)

$\perp$ 表示 $z$ 方向，$\parallel$ 表示面内 $x,y$ 方向。

> **原文疑点（Q291）：** 式(46)两侧贡献原印均为负号，而式(47a)、(47b)是介质1项减介质2项，符号衔接需结合两侧法线方向重推。式(41)未定义的系数 $c$、矢量并置与点积及 $q_s$ 的记号也保留原图，不能仅因同字母就把此 $c$ 指定为光速。式号从(42)跳至(46)，原作未列(43)—(45)，译文不补造。

若 $(\boldsymbol E\cdot\nabla)\boldsymbol E$ 可忽略，则两个具有中心对称的介质产生的和频响应，可用以下有效面二阶非线性极化率张量描述：

$$\chi_{s,\mathrm{eff}}^{(2)}=\chi_s^{(2)}+\chi_{s,\gamma}^{(2)}.\tag{48}$$

其中 $\chi_s^{(2)}$ 是描述局域在界面或表面的电流的面二阶非线性极化率；$\chi_{s,\gamma}^{(2)}$ 则表示体相纵向非线性极化的贡献。
''')
batch(624,'7.1',[14],r'''
<!-- B624：PDF p14全页；原作略去处保留。 -->
## 2.6 讨论

（广濑原作省略。）

## 3 实验

### 3.1 各向同性介质

原综述表1汇总了代表性对称性下，各向同性介质中具有非零值的极化率张量分量。[附录D（7.5）](7.5%20附录D：和频张量的非零分量.md)增加了一些对称性。

下面仅作十分粗略的概括。

“各向同性”表面的张量分量取决于是否存在垂直于表面的镜面。存在这样一个镜面时，下列分量可非零：

$$\chi^{(2)}_{s,\perp\perp\perp},\quad\chi^{(2)}_{s,\perp\parallel\parallel},\quad
\chi^{(2)}_{s,\parallel\perp\parallel},\quad\chi^{(2)}_{s,\parallel\parallel\perp}.$$

没有镜面对称时，还可增加

$$\chi^{(2)}_{s,xyz}=-\chi^{(2)}_{s,yzx},\qquad
\chi^{(2)}_{s,xzy}=-\chi^{(2)}_{s,yxz},\qquad
\chi^{(2)}_{s,zxy}=-\chi^{(2)}_{s,zyx}.$$

> **原文疑点（Q292）：** 第一组原印为 $xyz$ 与 $yzx$ 互为负值；常见按前两指标配对的候选为 $xyz$ 与 $yxz$，而原文后两组的配对也须整体核验。这里保留全部原指标，不能单独替换一个后便假定整组对称关系成立。

手性分子的液面在宏观上各向同性，但没有垂直于界面的镜面。

**具有镜面对称的界面产生 SFG、SHG 的特点：** 两个激发光的偏振相同时，生成 p 偏振光；两者互相正交时，生成 s 偏振光。垂直入射不产生该信号，因为 $\chi^{(2)}_{s,\parallel\parallel\parallel}=0$。

各向同性表面具有 $C_{4v}$ 或更高对称性时，和频张量有以下四组独立分量：

$$\begin{aligned}
\chi^{(2)}_{s,\perp\perp\perp}&:\quad\chi^{(2)}_{s,zzz},\\
\chi^{(2)}_{s,\perp\parallel\parallel}&:\quad\chi^{(2)}_{s,zxx}=\chi^{(2)}_{s,zyy},\\
\chi^{(2)}_{s,\parallel\perp\parallel}&:\quad\chi^{(2)}_{s,xzx}=\chi^{(2)}_{s,yzy},\\
\chi^{(2)}_{s,\parallel\parallel\perp}&:\quad\chi^{(2)}_{s,xxz}=\chi^{(2)}_{s,yyz}.
\end{aligned}$$

偏振选择实验的讨论：原作省略。

利用参考样品产生干涉条纹的讨论：原作省略。

### 3.2 各向异性介质

例如单晶表面、重构表面等。

具有 $m3m\,(O_h)$ 及 $432\,(O)$ 对称性的晶体，其表面对称性为：

| 晶面 | 表面对称性 |
| --- | --- |
| (110) | 二重旋转对称 |
| (111) | 三重旋转对称 |
| (001) | 四重旋转对称 |

以下原作略。

（广濑原注：电偶极近似适用性的讨论见原综述第400—410页。）
''')

batch(625,'7.2',[1],r'''
# 7.2 附录A：去除等介电常数近似的式(17)推导

<!-- B625：底本chap7-2.pdf p1全页。 -->
> 本附录属于广濑对 Heinz 综述的解读笔记；对应[7.1式(17)](7.1%20解读Tony%20F.%20Heinz的综述.md)。正文与原注已译，复杂原式按图保留；疑似笔误均未擅自采用修正。

## 波矢、场方向与基本关系

波矢和电场矢量如下图。

![介质1、膜层、介质2中的出射波矢和p偏振电场方向](../assets/7.2/p1-示意图.png)

先汇总基本量之间的关系：

$$k=(n/c)\omega,\qquad\varepsilon=(c^2/\omega^2)k^2,\qquad\lambda=c/\nu.$$

> **译者辨读说明：** 最后一式分母为频率 $\nu$，不是前一个式子中的折射率 $n$；按原PDF字形区分，不照搬文本层的拉丁字母识别结果。

考虑单频光（平面波），利用微分算符 $\nabla$ 可替换为 $i\boldsymbol k$，由式(2b)得到电场和磁场的关系：

$$\boldsymbol H=(\omega/c)\boldsymbol k\times\boldsymbol E.\tag{A1}$$

$$\begin{aligned}
H_x&=(\omega/c)(k_yE_z-k_zE_y),\\
H_y&=(\omega/c)(k_zE_x-k_xE_z),\\
H_z&=(\omega/c)(k_xE_y-k_yE_x).
\end{aligned}\tag{A2}$$

将电场分成 transverse（面内）分量与 longitudinal（垂直）分量，写为 $\boldsymbol E=\boldsymbol E_t+E_z\boldsymbol u_z$，则

$$\begin{aligned}
\boldsymbol H&=\boldsymbol H_t+H_z\boldsymbol u_z\\
&=(\omega/c)\{\boldsymbol k_t\times\boldsymbol E_t+k_z(\boldsymbol u_z\times\boldsymbol E_t)+E_z(\boldsymbol k_t\times\boldsymbol u_z)\}.
\end{aligned}$$

> **原文疑点（Q293）：** 式(A1)、(A2)及其后无编号式的系数原印为 $\omega/c$；由式(2b)及时间因子 $e^{-i\omega t}$ 在非磁性假设下导出的是 $c/\omega$，附录B也使用后者。原文未说明附录A采用不同归一化，保留原系数待核。此外，这里的“面内／垂直”是相对于界面，不是相对于波矢；不能据英文 transverse、longitudinal 就认定与通常横波、纵波定义一致。

如图，取两个光线（波矢）构成的平面为 $xz$ 面，从介质1指向介质2的界面法线为 $z$ 轴；原点取界面上的发光位置。此时 $k_{1z}<0$、$k_{2z}>0$。p 偏振电场 $\boldsymbol E_p$ 的方向选择有 $180^\circ$ 任意性，这里按图选取，所以 $E_{1z}>0$、$E_{2z}<0$。还应记住下列关系。
''')
batch(626,'7.2',[2,3],r'''
<!-- B626：PDF p2全页与p3式A7，跨页波矢组完整。 -->
## 将边界条件写成场分量

$$\varepsilon=(c^2/\omega^2)k^2.\tag{A3}$$

用以上关系改写正文式(12a)—(12d)。由式(12a)得

$$\varepsilon_2E_{z2}-\varepsilon_1E_{z1}=-4\pi i\boldsymbol k_t\cdot\boldsymbol P_{s,t}
=-4\pi i(k_xP_{s,x}+k_yP_{s,y}).\tag{A4a}$$

由式(12b)得 $\boldsymbol E_{t2}-\boldsymbol E_{t1}=-(4\pi i/\varepsilon')P_{s,z}\boldsymbol k_t$，即

$$E_{x2}-E_{x1}=-(4\pi i/\varepsilon')k_xP_{s,z},\tag{A4b}$$

$$E_{y2}-E_{y1}=-(4\pi i/\varepsilon')k_yP_{s,z}.\tag{A4c}$$

由式(12c)得 $(k_xE_{y2}-k_yE_{x2})-(k_xE_{y1}-k_yE_{x1})=0$，即

$$k_x(E_{y2}-E_{y1})=k_y(E_{x2}-E_{x1}).\tag{A4d}$$

由式(12d)得

![磁场跳变的两行中间式及式A4e、A4f](../assets/7.2/p2-式A4ef.png)

> **译者提示：** 原图第三行前的“即ち”意为“即”。此处原式已使用 $c/\omega$，与前页(A1)、(A2)的 $\omega/c$ 差异见Q293。

$\boldsymbol k_1$、$\boldsymbol k_2$、$\boldsymbol k_s$ 的 $x$、$y$ 分量在界面两侧相同。两个激发光共用同一入射面时，可选择坐标使 $k_y=0$。

式(A4d)可从(A4b)、(A4c)导出，(A4a)可从(A4e)、(A4f)导出，所以六式中只有四式独立。后者的推导可对 $(\mathrm{A4e})k_y+(\mathrm{A4f})k_x$，结合 $\boldsymbol k_i\cdot\boldsymbol E_i=0$ 和 $k_i^2=(\omega/c)^2\varepsilon_i$ 进行。

设 $\boldsymbol E_1$、$\boldsymbol E_2$ 与 $xz$ 面的夹角分别为 $\tau_1$、$\tau_2$。（绕 $\boldsymbol k$ 轴使 $xz$ 面转到 $\boldsymbol E$ 所在方向，定义为正方向。）

$$\begin{aligned}
E_{1p}&=E_1\cos\tau_1,&E_{2p}&=E_2\cos\tau_2,\\
E_{1s}&=E_1\sin\tau_1,&E_{2s}&=E_2\sin\tau_2.
\end{aligned}\tag{A5}$$

所考虑的介质均匀，波也为均匀波，$\boldsymbol E$ 与 $\boldsymbol H$ 正交。用 $\theta_1$、$\theta_2$ 表示场和波矢的坐标分量：

$$\begin{aligned}
E_{x1}&=E_{1p}\cos\theta_1,&E_{x2}&=E_{2p}\cos\theta_2,\\
E_{y1}&=E_{1s},&E_{y2}&=E_{2s},\\
E_{z1}&=E_{1p}\sin\theta_1,&E_{z2}&=E_{2p}\sin\theta_2.
\end{aligned}\tag{A6}$$

$$\begin{aligned}
k_x&=k_{x1}=k_{x2}=k_1\sin\theta_1=k_2\sin\theta_2,\\
k_y&=k_{y1}=k_{y2}=0,\\
k_{1z}&=-k_1\cos\theta_1,\qquad k_{2z}=+k_2\cos\theta.
\end{aligned}\tag{A7}$$

> **原文疑点（Q294）：** 式(A6)的 $E_{z2}$ 原印为正号，与p1选定的 $E_{2z}<0$ 及图中方向不一致；候选为 $-E_{2p}\sin\theta_2$。式(A7)末尾原印角度不带下标，候选为 $\theta_2$。这里保留原印，不将符号改动藏在后续推导中。
''')
batch(627,'7.2',[3],r'''
<!-- B627：PDF p3式A8至全文末。 -->
## 解出两侧辐射振幅

将式(A6)、(A7)代入(A4a)—(A4f)，得到

![式A8a—A8f，六个边界方程全部保留](../assets/7.2/p3-式A8.png)

从(A8a)、(A8b)，利用

$$\varepsilon_1\sin\theta_1\cos\theta_2+\varepsilon_2\cos\theta_1\sin\theta_2
=\frac{c^2}{\omega^2}(k_1\cos\theta_2+k_2\cos\theta_1),$$

得到

![式A9a、A9b，两侧p偏振辐射振幅](../assets/7.2/p3-式A9.png)

> **原文疑点（Q295）：** 上述无编号恒等式右侧只含一次波数，与左侧及 $\varepsilon=(c^2/\omega^2)k^2$ 的量纲不一致，疑缺切向波数因子。由 $k_1\sin\theta_1=k_2\sin\theta_2=k_x$ 可构造带 $k_x$ 的候选，但整条推导仍需结合Q294的符号问题核验，暂不采用。

这一结果说明：即使 $\varepsilon_1=\varepsilon_2=\varepsilon'$，普通反射的反射率为零，仍会产生和频光，并且原文指出 $|E_{1p}|\ne|E_{2p}|$。

> **译者限定说明：** 不同方向的辐射振幅一般可不同；上句不等式沿原文保留，特殊源分量或几何下仍可能相等，不宜视作所有情形都严格不等的定理。

把(A8c)、(A9a)、(A9b)代入(A8e)，得

$$E_{2s}=E_{1s}=4\pi i\frac{\omega^2}{c^2}\frac{P_{s,y}}{k_{2z}-k_{1z}}
=4\pi i\frac{\omega^2}{c^2}\frac{P_{s,y}}{k_1\cos\theta_1+k_2\cos\theta_2}.\tag{A10}$$

对(A9)、(A10)加入 $\varepsilon_1=\varepsilon_2=\varepsilon'=1$ 的条件，可以验证正文式(17)得到满足。（关键是此时 $k_1=k_2$、$\theta_1=\theta_2$。）
''')
batch(628,'7.3',[1],r'''
# 7.3 附录B：式(20)的推导

<!-- B628：底本chap7-3.pdf p1全页。 -->
> 对应[7.1的菲涅尔变换](7.1%20解读Tony%20F.%20Heinz的综述.md)。上标 $i,r,t$ 分别标记入射、反射和透射光；下标 $i,m,j$ 标记入射侧体相、膜、透射侧体相。复杂公式用原式图保留。

## 光场记号与s偏振

设体相各向同性，因此膜内电场也垂直于波矢。入射侧有入射光和反射光，透射侧只有透射光。在入射侧，以 $i,r$ 为上标，电场写成 $\boldsymbol E_i^i,\boldsymbol E_i^r$，磁场写成 $\boldsymbol H_i^i,\boldsymbol H_i^r$。透射光的电场、磁场原文写作 $\boldsymbol E_i^t,\boldsymbol H_i^t$。膜内有透射和反射两种光，原文先将电场写为 $\boldsymbol E_m^i,\boldsymbol E_m^r$，磁场写为 $\boldsymbol H_m^i,\boldsymbol H_m^r$。

（广濑原注：膜内可能有多重反射，因此更严谨的说法是，朝透射侧传播的光标上标 $t$，朝入射侧返回的光标上标 $r$。）

> **译者记号说明：** 原文引言给透射侧使用下标 $i$，图与后续公式则用 $j$；膜内向前波也在 $i,t$ 间切换。这些原记号予以注明，计算须按传播方向与所在介质逐项辨认。

每束光满足 $\boldsymbol H=(c/\omega)\boldsymbol k\times\boldsymbol E$，又选择 $k_y=0$，所以

$$\begin{aligned}
H_x&=-(c/\omega)k_zE_y,\\
H_y&=(c/\omega)(k_zE_x-k_xE_z),\\
H_z&=(c/\omega)k_xE_y.
\end{aligned}\tag{B1}$$

光路和电场矢量取向如下图。

![三层介质的入射、反射、透射与膜内双向场](../assets/7.3/p1-示意图.png)

分别对 s、p 偏振施加线性光学的界面连续条件，得到以下结果。

**s 偏振：**

$$E_{iy}^i+E_{iy}^r=E_{my}^t+E_{my}^r=E_{jy}^t,\tag{B2a}$$

$$k_x(E_{iy}^i+E_{iy}^r)=k_x(E_{my}^t+E_{my}^r)=k_xE_{jy}^t,\tag{B2b}$$

$$k_{iz}(E_{iy}^i-E_{iy}^r)=k_{mz}(E_{my}^t-E_{my}^r)=k_{jz}E_{jy}^t.\tag{B2c}$$

这三式依次来自 $E_y$、$H_z$、$H_x$；取 $k_{iz}^i=-k_{iz}^r=k_{iz}$。
''')
batch(629,'7.3',[2],r'''
<!-- B629：PDF p2全页，末句与下批B7衔接。 -->
式(B2a)与(B2b)等价，由(B2a)、(B2c)得到

$$E_{jy}^t=E_{my}^t+E_{my}^r=\frac{2k_{iz}}{k_{iz}+k_{jz}}E_{iy}^i,\tag{B3a}$$

$$E_{jy}^r=\frac{k_{iz}-k_{jz}}{k_{iz}+k_{jz}}E_{iy}^i.\tag{B3b}$$

> **原文疑点（Q296）：** 式(B3b)左侧原印 $E_{jy}^r$，但反射光位于介质 $i$，候选为 $E_{iy}^r$；暂不改原式。后面(B7)首项原印 $E_j^{xt}$，指标位置也与(B6)的 $E_{jx}^t$ 不同，见下一批原式。

## p偏振与透射场

由 $E_x$、法向电位移和 $H_y$ 的连续条件得

![式B4a—B4c：p偏振的三个边界关系](../assets/7.3/p2-式B4.png)

式(B4c)可由(B4a)、(B4b)导出，因此仅由后两者即可求所需关系。求解时，将下列关系代入，用 $E_p$ 表示 $E_x$ 和 $E_z$：

![六组电场分量与p偏振振幅的关系](../assets/7.3/p2-电场分量.png)

另有

$$\begin{aligned}
k_x&=k_i\sin\theta_i=k_m\sin\theta_m=k_j\sin\theta_j,\\
k_{iz}&=k_i\cos\theta_i,\quad k_{mz}=k_m\cos\theta_m,\quad k_{jz}=k_j\cos\theta_j,\\
k&=(\omega/c)\sqrt\varepsilon.
\end{aligned}$$

首先导出

![式B5：透射和反射p偏振振幅](../assets/7.3/p2-式B5.png)

因此，

![式B6：透射场的x、z分量及中间变形](../assets/7.3/p2-式B6.png)
''')
batch(630,'7.3',[2,3],r'''
<!-- B630：PDF p2末“另一方面”至p3全文末。 -->
## 膜内总场及零厚度极限

另一方面，令 $E_{mx}=E_{mx}^t+E_{mx}^r$、$E_{mz}=E_{mz}^t+E_{mz}^r$，则

$$E_{mx}=E_j^{xt},\qquad E_{mz}=(\varepsilon_j/\varepsilon')E_{jz}^t.\tag{B7}$$

因此，

![式B8：膜内总场的x、z分量，与正文式20对应](../assets/7.3/p3-式B8.png)

顺带一提，如 Born & Wolf 教科书第1.6.4节所示，若介质1和2之间有厚度为 $b$ 的膜，从介质1入射时的振幅反射系数 $r$、振幅透射系数 $t$ 可表示为

$$r=\frac{r_{im}+r_{mj}e^{2i\beta}}{1+r_{im}r_{mj}e^{2i\beta}},\qquad
t=\frac{t_{im}t_{mj}e^{i\beta}}{1+r_{im}r_{mj}e^{2i\beta}}.$$

其中 $\beta=bk_{mz}=b(2\pi/\lambda)n_m\cos\theta_m$。当 $\beta\to0$ 时，可见其与上述结果一致。

下面从(B4a)、(B4b)导出的关系，也许在某些场合有用：

![末尾两条无编号p偏振边界关系，保留全部上标](../assets/7.3/p3-末两式.png)

> **译者局部符号说明：** 这里 $\beta$ 是膜内传播相位厚度，与7.1体相四极项的唯象参数 $\beta$、此前分子一阶超极化率 $\beta$ 均不同。$r,t$ 为振幅系数，不应直接视为功率反射率、透射率。
''')
batch(631,'7.4',[1],r'''
# 7.4 附录C：式(20)的折射率表示与多重反射

<!-- B631：底本chap7-4.pdf p1全页。 -->
> 接续[附录B（7.3）](7.3%20附录B：式20的推导.md)，对应正文式(20)的扩展。式中的 $r,t$ 为振幅反射、透射系数；$m,m'$ 区分膜的两个边界位置。所有公式步骤按原印保留。

## 路径记号与多重反射求和

如下图，用“起始”和“结果”的介质作下标，表示相关光的反射系数 $r$ 与透射系数 $t$。对于反射，下标依次为光所在一侧的介质、构成反射界面的另一侧介质；对于透射，下标依次为入射侧介质、透射侧介质。

![膜内多重反射路径及两个边界的场取向](../assets/7.4/p1-示意图.png)

计入多重反射，并区分膜两侧电场的传播方向，可得

![四个场的多重反射级数，保留各阶路径乘积](../assets/7.4/p1-级数.png)

使用 $r_{im}=-r_{mi}$、$r_{im}^2+t_{im}^2=1$，并计入厚度方向的光程，令 $\beta=(2\pi/\lambda_0)nd\cos\theta_m$，得

![总反射场与另一出射场的闭式，两个左端按原印保留](../assets/7.4/p1-闭式.png)

> **原文疑点（Q297）：** 原印 $r_{im}^2+t_{im}^2=1$ 对通常电场振幅的透射系数并非普遍成立，需区分功率归一化与 $t_{im}t_{mi}$ 等乘积关系。紧随其后的两个闭式左端均标为 $E_i^r$，第二个右端是含 $t_{im}t_{mj}$ 的透射路径，候选左端为 $E_j^t$。保留原式，不在未明确归一化前套用该恒等式。
''')
batch(632,'7.4',[2],r'''
<!-- B632：PDF p2全页。 -->
膜内两端、两个方向的电场为

![膜内Et_m、Et_m′、Er_m、Er_m′四式，传播相位全部保留](../assets/7.4/p2-膜内场.png)

## s、p偏振的界面系数

反射、透射系数如下。

**s 偏振：**

![s偏振的六个界面振幅系数](../assets/7.4/p2-s系数.png)

**p 偏振：**

![p偏振的六个界面振幅系数及波数表示](../assets/7.4/p2-p系数.png)

> **原文疑点（Q298）：** p 偏振组的 $t_{im}$ 第二个分母原印为 $2k_m\cos\theta_i+k_i\cos\theta_m$，与前一个介电常数表示不一致；$t_{mj}$ 分子原印含 $k_i$，而该界面连接 $m,j$；末行左端写 $r_{jm}$，右侧却是形式类似透射系数的 $2\varepsilon_mk_{jz}/(\varepsilon_jk_{mz}+\varepsilon_mk_{jz})$，候选标签为 $t_{jm}$。这些条目需成组复算，保留原图，不任选一个表达式当作已确认正确值。

## 与零厚度结果的对应

由附录B式(B2)得到的关系可写为

![s偏振膜内前向、后向振幅的两条三段等式](../assets/7.4/p2-s对应.png)

由式(B4)得到的关系可写为

![p偏振膜内前向、后向振幅的两条三段等式](../assets/7.4/p2-p对应.png)

这些式子与计入多重反射后令膜厚趋于零的极限一致。
''')
batch(633,'7.5',[1],r'''
# 7.5 附录D：和频张量的非零分量

<!-- B633：底本chap7-5.pdf p1全页，十个独立分量数分组全部保留。 -->
详细内容记在另一文件中。这里仅按独立非零分量的个数，列出分类表。

> **译者说明：** 原表用 $\beta_{ijk}$ 表示张量分量，保留其记号，不直接改成 $\chi_{s,ijk}^{(2)}$；本页未交代从分子到宏观响应的换算，也没有指定每个点群采用的坐标轴方向。本表不能脱离坐标约定直接替代前文面张量。原式图完整保留等号、负号和指标，各组计数标题译为中文。

## 1个独立分量

![D3h、Td、O三组张量关系](../assets/7.5/p1-1个.png)

## 2个独立分量

![C3h、T两组张量关系](../assets/7.5/p1-2个.png)

## 3个独立分量

![D2d以及D4、D6的张量关系](../assets/7.5/p1-3个.png)

## 4个独立分量

![C4v至C∞v及D3的张量关系](../assets/7.5/p1-4个.png)

## 5个独立分量

![C3v的张量关系](../assets/7.5/p1-5个.png)

## 6个独立分量

![D2与S4的张量关系](../assets/7.5/p1-6个.png)

## 7个独立分量

![C2v以及C4、C6至C∞的张量关系](../assets/7.5/p1-7个.png)

## 9个独立分量

![C3的张量关系，两行完整保留](../assets/7.5/p1-9个.png)

## 13个独立分量

![C2的十三项原列表](../assets/7.5/p1-13个.png)

## 14个独立分量

![Cs的十四项原列表](../assets/7.5/p1-14个.png)

> **原文疑点（Q299）：** $C_3$ 组第二行原印 $\beta_{yyy}=-\beta_{yxxy}=\cdots$，其中 $yxxy$ 为四个指标，与本页三指标张量不符，候选为 $yxx$。$C_2$ 的“13个”列表中 $\beta_{yxz}$ 重复，而 $\beta_{yzx}$ 未列出，候选为其中一项误植，但须在其坐标约定下核验。$T_d$、$T$ 所列的 $xxz$ 等分量及 $D_3$ 中 $\beta_{zzz}=-2\beta_{xxz}=\cdots$ 的关系也不宜不加坐标依据地照作通用表；均保留原印，待独立对称性复核。
''')

# Crops use coordinates on scale=1.8 preview; render at twice that scale.
crops={'7.1':[
(5,'折射率',(195,1160,950,1303)),(6,'向上',(195,289,952,456)),(6,'向下',(195,518,952,687)),
(6,'证明起点',(195,1222,951,1333)),(7,'s振幅',(195,128,951,182)),(7,'分量变形',(195,273,951,551)),
(7,'偏振关系',(195,645,951,711)),(7,'证明末组',(195,769,951,1128)),
(9,'式31',(195,872,951,931)),(9,'式32',(195,1309,951,1380)),
(10,'式33a',(195,288,951,351)),(10,'式33c',(195,596,951,661)),
(11,'式36',(195,969,951,1011)),(11,'式37',(195,1098,951,1235)),
(12,'式40',(195,806,951,851)),(13,'式41',(195,423,951,551)),
(13,'式46',(195,776,951,818)),(13,'式47',(195,934,951,1038))],
'7.2':[(1,'示意图',(298,253,806,674)),(2,'式A4ef',(197,653,947,773)),(3,'式A8',(197,276,950,449)),(3,'式A9',(197,565,950,685))],
'7.3':[(1,'示意图',(233,608,810,1086)),(2,'式B4',(196,310,950,425)),(2,'电场分量',(196,575,950,756)),(2,'式B5',(196,940,950,1047)),(2,'式B6',(196,1119,950,1305)),(3,'式B8',(196,245,950,357)),(3,'末两式',(196,697,950,758))],
'7.4':[(1,'示意图',(287,355,842,828)),(1,'级数',(196,948,950,1071)),(1,'闭式',(196,1170,950,1318)),(2,'膜内场',(196,151,950,303)),(2,'s系数',(196,430,950,520)),(2,'p系数',(196,579,950,760)),(2,'s对应',(196,847,950,969)),(2,'p对应',(196,1064,950,1179))],
'7.5':[(1,'1个',(198,305,954,394)),(1,'2个',(198,425,954,483)),(1,'3个',(198,513,954,572)),(1,'4个',(198,602,954,661)),(1,'5个',(198,721,954,750)),(1,'6个',(198,750,954,811)),(1,'7个',(198,835,954,902)),(1,'9个',(198,925,954,987)),(1,'13个',(198,1015,954,1048)),(1,'14个',(198,1074,954,1109))]}

names={
'7.2':'7.2 附录A：去除等介电常数近似的式17推导.md',
'7.3':'7.3 附录B：式20的推导.md',
'7.4':'7.4 附录C：式20的折射率表示与多重反射.md',
'7.5':'7.5 附录D：和频张量的非零分量.md'}

def write_all():
    crops['7.3']=[(p,l,(b[0],b[1],b[2],375) if l=='式B8' else b) for p,l,b in crops['7.3']]
    crops['7.4']=[(p,l,(b[0],130,b[2],b[3]) if l=='膜内场' else b) for p,l,b in crops['7.4']]
    crops['7.5']=[(p,l,(198,689,954,722) if l=='5个' else b) for p,l,b in crops['7.5']]
    for s,items in crops.items():
        asset=R/'中文版本/assets'/s;asset.mkdir(parents=True,exist_ok=True)
        doc=pdfium.PdfDocument(str(R/f'日语原版/Chapter7/chap7-{s[-1]}.pdf'))
        for p,label,box in items:
            im=doc[p-1].render(scale=3.6).to_pil()
            im.crop(tuple(int(v*2) for v in box)).save(asset/f'p{p}-{label}.png')
        doc.close()
    for n,(s,pages,t) in batches.items():
        out=R/'翻译管理/校订记录'/s;out.mkdir(parents=True,exist_ok=True)
        (out/f'B{n}-本批译文.md').write_text(t,encoding='utf8')
    for s in sorted(set(v[0] for v in batches.values())):
        out=R/'翻译管理/校订记录'/s
        chunks=sorted(out.glob('B[0-9][0-9][0-9]-本批译文.md'))
        texts=[re.sub(r'<!-- B\d+结束：[\s\S]*?-->','',p.read_text(encoding='utf8')).strip() for p in chunks]
        target=next(D.glob(s+' *.md'),D/names.get(s,'unused.md'))
        target.write_text('\n\n'.join(texts)+'\n',encoding='utf8')
    from PIL import Image,ImageDraw
    renderer=(R/'翻译管理/校订记录/7.1/检查排版.cjs').read_text(encoding='utf8')
    for s in ['7.2','7.3','7.4','7.5']:
        (R/f'翻译管理/校订记录/{s}/检查排版.cjs').write_text(renderer.replace('7.1',s),encoding='utf8')
    for s in crops:
        files=[R/f'中文版本/assets/{s}/p{p}-{label}.png' for p,label,_ in crops[s]]
        for start in range(0,len(files),6):
            ims=[]
            for f in files[start:start+6]:
                im=Image.open(f);im.thumbnail((960,500))
                ims.append((f.name,im.copy()))
            sheet=Image.new('RGB',(1000,sum(im.height+42 for _,im in ims)+15),'#dedede')
            draw=ImageDraw.Draw(sheet);y=10
            for label,im in ims:
                draw.text((10,y),label,fill='black');y+=30
                sheet.paste(im,(10,y));y+=im.height+12
            sheet.save(R/f'翻译管理/校订记录/{s}/原式裁图核对{start//6+1}.png')

if __name__=='__main__':write_all()

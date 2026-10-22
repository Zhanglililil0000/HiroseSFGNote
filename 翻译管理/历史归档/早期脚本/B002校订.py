from pathlib import Path
import shutil
root=Path('HiroseSFGNote').resolve();p=root/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';out=root/'翻译管理/校订记录/1.1';old=p.read_text(encoding='utf-8');a=old.index('## 2. SFG 极化与和频过程');b=old.index('## 3. 分子的 SFG 极化与振动共振');assert not (out/'B002-修订前.md').exists();shutil.copy2(p,out/'B002-修订前.md')
new=r'''## 2. SFG 极化与和频过程

电场 $\mathbf{E}$ 与其诱导的电偶极矩（极化）$\mathbf{p}$ 之间的关系，可用分子极化率张量 $\alpha$、$\beta$、$\gamma$ 写成式（1）。普通光照射时，诱导的只是与电场成正比的线性极化，即以 $\alpha$ 为系数的项。但是，当激光等强光入射时，以高阶极化率张量 $\beta$、$\gamma$ 为系数产生的非线性极化也不能忽略。

$$
\mathbf{p}=\alpha:\mathbf{E}+\beta:\mathbf{E}\mathbf{E}+\gamma:\mathbf{E}\mathbf{E}\mathbf{E}+\cdots
\tag{1}
$$

下面说明式（1）的含义。左边是矢量，具有 $x$、$y$、$z$ 分量，记为 $p_i$。右边第一项是二阶张量 $\alpha$ 的分量 $\alpha_{ij}$ 与电场矢量的 $j$ 分量 $E_j$ 的乘积对 $j$ 求和，即 $\sum_j\alpha_{ij}E_j$。这里 $i,j=x,y,z$，且 $i$ 始终位于下标的最左端。第二项将具有三个下标的张量分量 $\beta_{ijk}$ 与两个电场分量的乘积 $E_jE_k$ 相乘，再对 $j$、$k$ 求和，即 $\sum_{jk}\beta_{ijk}E_jE_k$；$\beta$ 的第一个下标始终为 $i$，其余下标分别与两个电场分量的下标一致。第三项及以后各项也按同样方式理解。

光与分子相互作用的量子力学计算表明，当光的频率与分子振动跃迁或电子跃迁的频率一致时，极化率张量的值会共振增强。实际测量的样品是由大量分子组成的宏观介质，因此还需要定义介质的宏观极化率，并将电场与宏观极化 $\mathbf{P}$ 的关系写成式（2）。

$$
\mathbf{P}=\chi^{(1)}:\mathbf{E}+\chi^{(2)}:\mathbf{E}\mathbf{E}+\chi^{(3)}:\mathbf{E}\mathbf{E}\mathbf{E}+\cdots
\tag{2}
$$

> **译者注：** 式（2）中的 $\chi^{(2)}$ 称为“二阶非线性极化率”；上下文明确时可简称“极化率”。这里的宏观响应与式（1）的分子极化率张量应加以区分。

实际上，每个分子都会发生极化并具有电偶极矩 $\mathbf{p}$，样品的宏观极化 $\mathbf{P}$ 可看作各分子极化 $\mathbf{p}$ 的矢量和。实用处理中，用 $\mathbf{p}$ 的系综平均或取向平均乘以分子数 $N$ 来替代这一矢量和，就得到式（3）。

$$
\chi^{(1)}=N\langle\alpha\rangle,\qquad
\chi^{(2)}=N\langle\beta\rangle,\qquad
\chi^{(3)}=N\langle\gamma\rangle.
\tag{3}
$$

> **译者注：** 原文在此将 $N$ 称为“分子数”。本译文保留这一称呼及原式；具体使用时，应结合 $\mathbf{P}$ 的定义核实归一化，不能直接将 $N$ 改作数密度或擅自补入 $\epsilon_0$。

这种极化沿光的传播路径产生，因此，由极化产生的光也沿入射光前进的方向，即光路，叠加起来。特别是由激光等在空间和时间上波的相位一致的相干光诱导极化时，所产生的光具有很强的方向性。

频率为 $\omega$ 的光，其振荡电场可写为

$$
\begin{aligned}
\mathbf{E}(\omega;\mathbf{r},t)
&=\mathbf{E}_0(\omega)\left\{\exp[i(\omega t-\mathbf{k}\cdot\mathbf{r})]+\mathrm{c.c.}\right\}\\
&=2\mathbf{E}_0(\omega)\cos(\omega t-\mathbf{k}\cdot\mathbf{r}).
\end{aligned}
\tag{4}
$$

其中，c.c. 表示紧邻其前的项的复共轭。

当某处受到频率不同的两束光照射时，该处电场为

$$
\mathbf{E}(\omega,\mathbf{r},t)
=\mathbf{E}(\omega_1;\mathbf{r},t)+\mathbf{E}(\omega_2;\mathbf{r},t).
\tag{5}
$$

将式（5）代入式（1）、式（2）右边的第二项，可以看出，除了零频率以及以 $2\omega_1$、$2\omega_2$ 振荡的分量外，还包含频率为 $\omega_1+\omega_2$ 和 $\omega_1-\omega_2$ 的分量。由频率为 $\omega_1+\omega_2$ 和 $\omega_1-\omega_2$ 的极化产生光的现象，分别称为和频过程（SFG）和差频过程（DFG）。当入射光采用红外光与可见光的组合时，就分别是红外–可见光和频过程与差频过程。分子的振动跃迁频率与红外光频率一致时，SFG 光强会共振增强；通过观测这一增强来测量表面物种振动光谱的方法，称为红外–可见光 SFG 光谱。

'''
head=old[:a].replace('B001 已对照校订“1. 引言”；第 2 部分及以后仍为待校订旧译。','B001–B002 已对照校订第 1、2 部分；第 3 部分及以后仍为待校订旧译。').replace('PDF 第 1 页。','PDF 第 1–2 页。')
p.write_text(head+new+old[b:],encoding='utf-8')
assert p.read_text(encoding='utf-8').split('## 3. 分子的 SFG 极化与振动共振',1)[1]==old.split('## 3. 分子的 SFG 极化与振动共振',1)[1]
print('B002: second subsection updated; equations (1)-(5); third subsection onward unchanged.')

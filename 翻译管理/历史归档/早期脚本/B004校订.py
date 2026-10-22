from pathlib import Path
import shutil
r=Path('HiroseSFGNote').resolve();p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';o=r/'翻译管理/校订记录/1.1';s=p.read_text(encoding='utf-8');a=s.index('\u200b\t相互作用哈密顿量为');b=s.index('**（二阶非线性极化：三波混频）**',a);assert not (o/'B004-修订前.md').exists();shutil.copy2(p,o/'B004-修订前.md')
t=r'''相互作用哈密顿量写为 $H'=e\mathbf{r}\cdot\mathbf{E}$，宏观极化矢量写为 $\mathbf{P}=-Ne\mathbf{r}$。这里，$\mathbf{r}$ 是矢量算符，表示构成分子的粒子——原子和电子——的位置坐标。分子内电荷分布的偏置，用最粗略的电偶极近似来表示。另外，原文以电子的电荷为基准取 $e$，因此 $e$ 为负值。

取实验室固定的直角坐标系，用下标 $i,j,k,l$ 表示其坐标轴。孤立分子的能量本征态用下标 $g,n,n',n''$ 表示；这里同时考虑电子态与振动态。对于气体分子，许多情况下还可以明确定义转动态，因此也包括转动态。其中，$g$ 表示没有光微扰时分子所处的状态。密度矩阵的矩阵元计算见附录 B。根据这一结果，若假设分子只占据能级 $g$，则计算得到的极化如下。

**（线性极化）**

$$
\begin{aligned}
\chi_{ij}^{(1)}(\omega)
&=\frac{P_i^{(1)}(\omega)}{E_j(\omega)}\\
&=N\frac{e^2}{\hbar}\sum_{gn}
\left[
\frac{(r_i)_{ng}(r_j)_{gn}}{\omega+\omega_{ng}+i\Gamma_{ng}}
-\frac{(r_j)_{ng}(r_i)_{gn}}{\omega-\omega_{ng}+i\Gamma_{ng}}
\right]\rho_g^{(0)}.
\end{aligned}
\tag{9}
$$

'''
head=s[:a].replace('第 3 部分开头（至式（8）及密度矩阵法引入）已由 B003 校订，其后仍为待校订旧译。','第 3 部分已校订至线性响应式（9）（B003–B004），式（10）起仍为待校订旧译。').replace('PDF 第 1–3 页。','PDF 第 1–3 页及第 4 页至式（9）。')
p.write_text(head+t+s[b:],encoding='utf-8')
assert p.read_text(encoding='utf-8').split('**（二阶非线性极化：三波混频）**',1)[1]==s.split('**（二阶非线性极化：三波混频）**',1)[1]
print('B004: two definition paragraphs and equation (9) updated; equation (10) onward preserved.')

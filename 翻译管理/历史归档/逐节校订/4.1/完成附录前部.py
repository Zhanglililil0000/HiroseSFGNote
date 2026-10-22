from 整节工具 import *
b='## 附录1：谐振子与矩阵元\n\n解释分子振动光谱时，零阶近似将分子视为一组谐振子。出发点是：键长、键角和二面角偏离平衡值时，恢复力正比于偏离量；更一般地说，振动势能可写为位移坐标的二次型。该近似能较好解释实测，了解其定式很有用。参考水岛三一郎、岛内武彦《赤外線吸収とラマン効果》（共立全书），以及中川一朗《振動分光学》（日本分光学会测定法系列，学会出版中心）。\n\n双原子分子只有一个振动自由度。令原子间距偏离平衡值为$\\Delta r$，其动能与势能为：\n\n'+eq('A.1')
b+='其中$\\mu=m_1m_2/(m_1+m_2)$为约化质量，$K_{rr}$为力常数、弹簧常数。$\\Delta r$具有长度量纲；仿照多原子分子，换成质量调整坐标$Q=\\sqrt\\mu\\Delta r$，得到：\n\n'+eq('A.2')
b+='其中$\\lambda=K_{rr}/\\mu$。按先将动能写成动量形式再算符化的标准量子力学步骤，得到：\n\n'+math(r'E_v=h\nu(v+1/2),\quad v=0,1,2,\ldots,\qquad\nu\ (\mathrm{s}^{-1})=\frac1{2\pi}\sqrt{K_{rr}/\mu}')
b+='再将振动坐标无量纲化：\n\n'+eq('A.3')+'则无量纲算符$q$的矩阵元为：\n\n'+eq('A.4')
b+='由此可得到计算光谱强度、能量本征值或费米共振矩阵元所需的项。下列结果一般适用于非简并模式：\n\n'+math(r'\langle1|q|0\rangle=\sqrt{1/2},\quad\langle2|q|1\rangle=\sqrt{2/2}')
b+=math(r'''\begin{aligned}\langle v|q^2|v\rangle&=\langle v|q|v-1\rangle\langle v-1|q|v\rangle+\langle v|q|v+1\rangle\langle v+1|q|v\rangle=v+1/2,\\
\langle v+2|q^2|v\rangle&=\langle v+2|q|v+1\rangle\langle v+1|q|v\rangle=[(v+2)(v+1)/2]^{1/2}.
\end{aligned}\tag{A.5}''')
b+='简并振动的矩阵元参见另文《振动共振与费米共振》。振动偶极矩与拉曼张量由分子偶极矩$\\mu$及光散射张量$\\alpha$对振动坐标展开得到（中川一朗教材2.4、2.5节）：\n\n'+eq('A.6')+eq('A.7')
b+='其中$\\mu_e$为永久偶极矩，$\\alpha_0$为瑞利散射张量。参照(A.5)第一式，可求基频与热带的矩阵元。振动非谐性通过势能中三次及以上坐标项表示。位移原点在平衡结构，势能对所有位移为极小，故没有一次项：\n\n'+math(r'H^{\prime}=K_{rrr}(\Delta r)^3+K_{rrrr}(\Delta r)^4+\cdots')
b+='三次非谐项的矩阵元存在于$v$与$v\\pm1,v\\pm3$之间，四次项存在于$v$与$v$（对角）、$v\\pm2,v\\pm4$之间。非对角哈密顿量用微扰论处理；若$K_{rrr}$项显著，相邻振动能级将混合。多原子振动除伸缩外，还有键角、二面角变化及绕键轴扭转，因而须采用附录2的变换与处理。\n\n'
add(270,b,[22,23,24],'Q133：A.5最后一式原分母位于根号内，为√[(v+2)(v+1)/2]，由A.4相乘候选为√[(v+2)(v+1)]/2；原式保留，未采用。第2部分与本附录的无量纲化因子差异分别照录。')
b='## 附录2：内部正交坐标、内坐标、对称坐标、简正坐标\n\n### A. 实验室固定坐标系（1）：X系\n\n分析实验的定式首先应在实验室固定坐标中表示。分子转动、振动乃至电子运动的动能起初都在此写下，同时用势能表示键长不会成为零或无穷大等条件；电子势能则包括核吸引与电子间排斥。这里坐标轴方向与原点都固定于实验室，一般用直角坐标。以下不考虑电子，分子动能为：\n\n'+eq('B.1')
b+='$m_i$为第$i$个原子的质量（单原子，amu），$X_i,Y_i,Z_i$为实验室坐标；势能暂写为一般式$U(R)$。\n\n### B. 实验室固定坐标系（2）：X′系\n\n分子有平衡结构，振动态也不会远离它，分子内电子亦不会离开分子。因此可保持坐标轴方向不变，将原点移到分子质心。若质心在X系的坐标为$(X_0,Y_0,Z_0)$，则第$i$个原子的X′坐标是$(X_i-X_0,Y_i-Y_0,Z_i-Z_0)$。质心仍由A中的坐标定义。将(B.1)重写为：\n\n'
b+=math(r'''\begin{aligned}T&=\frac12\left\{M(dX_0/dt)^2+(dY_0/dt)^2+(dZ_0/dt)^2+\sum_i m_i[(dX_i'/dt)^2+(dY_i'/dt)^2+(dZ_i'/dt)^2]\right\},\\
M&=\sum_i m_i,\qquad\sum_i m_iX_i'=\sum_i m_iY_i'=\sum_i m_iZ_i'=0\quad\text{（质心条件）}.
\end{aligned}''')
b+='这将分子动能分成总质量集中在质心的平动能，以及用X′表示的分子内运动动能。若空间无电磁场且忽略重力，孤立分子不受外力，平动没有势能，仅有相对空间的动能；全部势能转移到X′系。去除平动后，余下为$U(X\\prime)$及：\n\n'+eq('B.2')
add(271,b,[24,25],'Q134：原T展开式只在X₀速度项前明确列M，Y₀/Z₀项未列；三项统一乘M是候选读法，未采用。势能最初写U(R)、随后写U(X′)，按各段保留。')
b='### C. 分子固定直角坐标系：r（a,b,c）系\n\n无外力的均匀体系中，分子通常随机取向；但平均结构确定，指定原子位置时使用方向也固定于分子的坐标更直观。称为r系，分量为$(a,b,c)$。例如水分子取分子面为ab面，二重轴从两H朝O为b轴，则O只有b分量，两H有大小相等、符号相反的a分量和相同b分量。\n\n从头算和DFT计算势能及分子振动广泛使用此系；后面的D、E主要便于讨论振动形和谱带归属。共原点的两直角坐标可通过欧拉角相互变换（见另文）：\n\n'+eq('B.3')
b+='指定r系对X′系取向的$(\\chi,\\theta,\\phi)$描述分子转动，只有三个参数。若每一瞬间按振动结构重新定义轴，振动摆动也会混入欧拉角，模糊整体转动。因此用“r系针对平衡结构定义”的Eckart条件，使欧拉角反映整体转动。（简并振动线性组合也能产生角动量，严格说以上说明尚不足以概括Eckart条件。）线形分子只需两个欧拉角，a、b轴仍有任意性。\n\\nX′分量已有三个质心约束，r分量再增加三个Eckart约束。因此N原子虽有3N个分量，振动自由度为3N−6，线形分子为3N−5。设r系相对X′系的角速度矢量为$\\boldsymbol\\omega$，有：\n\n'
b+=math(r'''\frac{d\mathbf X'}{dt}=\boldsymbol\omega\times\mathbf r+\frac{d\mathbf r}{dt},\qquad\frac{d\mathbf r}{dt}\cdot(\boldsymbol\omega\times\mathbf r)=\boldsymbol\omega\cdot\left(\mathbf r\times\frac{d\mathbf r}{dt}\right)''')
b+=math(r'''\begin{aligned}2T&=M(dX_0/dt)^2+(dY_0/dt)^2+(dZ_0/dt)\\&\quad+\sum_i m_i[(da_i/dt)^2+(db_i/dt)^2+(dc_i/dt)^2]\bigr]\\
&\quad+(I_{aa}\omega_a^2+I_{bb}\omega_b^2+I_{cc}\omega_c^2)\\&\quad-\bigl(I_{ab}\omega_a\omega_b+(I_{bc}\omega_b\omega_c+(I_{ca}\omega_c\omega_a)\\&\quad+2(\Omega_a\omega_a+\Omega_b\omega_b+\Omega_c\omega_c).
\end{aligned}''')
b+=math(r'''\begin{aligned}I_{aa}&=\sum_i m_i(b_i^2+c_i^2),&I_{bb}&=\sum_i m_i(c_i^2+a_i^2),&I_{cc}&=\sum_i m_i(a_i^2+b_i^2),\\I_{ab}&=\sum_i m_i a_ib_i,&I_{bc}&=\sum_i m_i b_ic_i,&I_{ca}&=\sum_i m_i c_ia_i.
\end{aligned}''')
b+=math(r'''\begin{aligned}\Omega_a&=-\sum_i m_i[(db_i/dt)c_i-b_i(dc_i/dt)],\\\Omega_b&=-\sum_i m_i[(dc_i/dt)a_i-c_i(da_i/dt)],\\\Omega_c&=-\sum_i m_i[(da_i/dt)b_i-a_i(db_i/dt)].\end{aligned}''')
b+='以$\\mathbf r^0$为平衡结构原子坐标，$d\\mathbf r$为偏离，则$\\mathbf r=\\mathbf r^0+d\\mathbf r$，且$0=\\sum_i m_i da_i=\\sum_i m_i db_i=\\sum_i m_i dc_i$。若平衡系$\\mathbf x^0$的轴取惯性主轴，有$0=\\sum_i m_ix_i^0y_i^0=\\sum_i m_iy_i^0z_i^0=\\sum_i m_iz_i^0x_i^0$。要求振动产生的角动量在零阶近似为零，在振幅远小于原子间距时Eckart条件为：\n\n'
b+=math(r'''\begin{aligned}0&=\sum_i m_i[a_i^0d(db_i/dt)-b_i^0d(da_i/dt)]\\&=\sum_i m_i[b_i^0d(dc_i/dt)-c_i^0d(db_i/dt)]\\&=\sum_i m_i[c_i^0d(da_i/dt)-a_i^0d(dc_i/dt)].\end{aligned}''')
b+='如此定义的分子固定直角坐标与简正坐标联系为：\n\n'+math(r'''\begin{aligned}\sqrt{m_i}a_i&=\sum_s l_{is}^{(a)}Q_s,&\sqrt{m_i}b_i&=\sum_s l_{is}^{(b)}Q_s,&\sqrt{m_i}c_i&=\sum_s l_{is}^{(c)}Q_s,\\
\sum_i[(l_{is}^{(a)})^2+(l_{is}^{(b)})^2+(l_{is}^{(c)})^2]&=1,\\0&=\sum_i l_{is}^{(a)}l_{is'}^{(a)}=\sum_i l_{is}^{(b)}l_{is'}^{(b)}=\sum_i l_{is}^{(c)}l_{is'}^{(c)}.
\end{aligned}''')
b+='此时动能右端第二项可写为$\\sum_s(dQ_s/dt)^2$。零阶谐势近似为：\n\n'+math(r'V_0=\sum_s(\lambda_s/2)Q_s^2,\qquad\lambda_s=(2\pi c\omega_s)^2')
b+='还可用无量纲简正坐标：\n\n'+math(r'Q_s=[(h/2\pi)^2/\lambda_s]^{1/4}q_s')+'其振动哈密顿量为：\n\n'+math(r'H_{\mathrm{vib}}^{(0)}=[(h/4\pi)\sum_s\lambda_s]^{1/2}[q_s^2+(p_s2\pi/h)^2]')+'其中$p_s$为与$q_s$共轭的动量算符。\n\n'
add(272,b,[25,26],'Q134：原2T的Z₀速度项未平方、质量因子范围、方/圆括号配对以及转动交叉项系数均按原字形保留；不以标准动能重写。Eckart导数记号、分轴正交等式及最后H的求和/根号范围也照原式，候选为按完整坐标变换核算，未采用。')

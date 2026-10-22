from 整节工具 import *
b=r'''#### 反对称伸缩振动：$b_1$模式
'''+math(r'''\begin{aligned}
\beta_{caa}&=-2G_{b1}\left[\frac{1-r}{2}\sin\alpha\sin(\alpha/2)\right]\beta_0(Q_{b1}^2)_{v+1,v},\\
\beta_{aca}&=-2G_{b1}\left[\frac{1-r}{2}\sin\alpha\sin(\alpha/2)\right]\beta_0(Q_{b1}^2)_{v+1,v}.
\end{aligned}\tag{0.4}''')
b+=math(r'''G_{b1}=\frac{1-\cos\alpha}{m_C}+\frac1{m_H}=\frac{m_C+m_H(1-\cos\alpha)}{m_Cm_H}\,w''')
b+='对于亚甲基（$\\alpha=109.5^\\circ$）：\n\n'+math(r'G_{b1}=(3m_C+4m_H)/(3m_Cm_H)=\frac1{m_H}+\frac43\frac1{m_C}')
b+='对于乙烯基CH₂（$\\alpha=120^\\circ$）：\n\n'+math(r'G_{b1}=(2m_C+3m_H)/(2m_Cm_H)=\frac1{m_H}+\frac32\frac1{m_C}')
b+=math(r'(Q_{b1}^2)_{v+1,v}\equiv[\langle v+1|Q_{b1}|v\rangle]^2=\frac{h}{2\pi c\omega_{b1}}(v+1)')
b+='红外光谱强度比：\n\n'+math(r'(d\mu_{a1}/dr_{\mathrm{CH}})^2/(d\mu_{b1}/dr_{\mathrm{CH}})^2\approx G_{a1}\cos^2(\alpha/2)/G_{b1}\sin^2(\alpha/2)\approx0.475')
b+='拉曼光谱强度比：\n\n'+math(r'I_{a1}/I_{b1}\approx G_{a1}[30(1+2r)^2+7(1-r)^2]/[14G_{b1}(1-r)^2]\approx0.475+2.063(1+2r)^2/(1-r)^2')
add(251,b,[2,3],'Q123：p2的G通式末尾有孤立的w字形，原样保留，未定义；候选为排版杂字，未删除。强度比原斜线串保留，需结合上下文读分组。')
b='### CH₃基\n\n沿C₃轴从C指向H₃取$c$轴，在三个HCX平面中的任一个平面上取$a$轴；$b$轴位于平分其余两个HCX平面的平面上。设HCX角为$\\tau$。\n\n#### 全对称伸缩振动：$a_1$模式\n\n'
b+=math(r'''\begin{aligned}
\beta_{ccc}&=3G_{\mathrm{sym}}\left[\frac{r+(1-r)\cos^2\tau}{2}\cos\tau\right]\beta_0(Q_{a1}^2)_{v+1,v},\\
\beta_{aac}=\beta_{bbc}&=3G_{\mathrm{sym}}\left[\frac{2r+(1-r)\sin^2\tau}{2}\cos\tau\right]\beta_0(Q_{a1}^2)_{v+1,v}.
\end{aligned}\tag{0.5}''')
b+=eq('0.5').split('$$')[0] if False else ''
b+=math(r'G_{\mathrm{sym}}=\frac{1+2\cos\tau}{m_C}+\frac1{m_H}=\frac{m_C+m_H(1+2\cos\tau)}{m_Cm_H}=\frac1{m_H}+\frac13\frac1{m_C}')
b+=math(r'''\begin{aligned}(Q_{\mathrm{sym}}^2)_{v+1,v}&\equiv[\langle v+1|Q_{\mathrm{sym}}|v\rangle]^2\\
&=(Q_{\mathrm{sym}}^2)_{v,v+1}\equiv[\langle v|Q_{\mathrm{sym}}|v+1\rangle]^2=\frac h{2\pi c\omega_{\mathrm{sym}}}(v+1).
\end{aligned}''')
b+='参见退偏比：\n\n'+math(r'\rho=\frac34\frac1{1+\frac{45}{4}\left(\frac{1+2r}{1-r}\right)^2}')
b+='#### 简并伸缩振动：$e$模式\n\n'+math(r'''\begin{aligned}
\beta_{caa}=\beta_{cbb}=\beta_{aca}=\beta_{bcb}
&=-3G_{\mathrm{deg}}\left[\frac{1-r}{2}\sin^2\tau\cos\tau\right]\beta_0(Q_{\mathrm{deg}}^2)_{v+1,v},\\
\beta_{aaa}=-\beta_{bba}=-\beta_{abb}=-\beta_{bab}
&=\frac32G_{\mathrm{deg}}\left[\frac{1-r}{2}\sin^3\tau\right]\beta_0(Q_{\mathrm{deg}}^2)_{v+1,v}.
\end{aligned}\tag{0.6}''')
b+=math(r'G_{\mathrm{deg}}=\frac{1-\cos\tau}{m_C}+\frac1{m_H}=\frac{m_C+m_H(1-\cos\tau)}{m_Cm_H}=\frac1{m_H}+\frac43\frac1{m_C}')
b+=math(r'''\begin{aligned}(Q_{\mathrm{deg}}^2)_{v+1,v}&\equiv[\langle v+1|Q_{\mathrm{deg}}|v\rangle]^2=\frac h{2\pi c\omega_{\mathrm{deg}}}(v+1)(v+2),\\
(Q_{\mathrm{deg}}^2)_{v-1,v}&\equiv[\langle v-1|Q_{\mathrm{deg}}|v\rangle]^2=\frac h{2\pi c\omega_{\mathrm{deg}}}v(v+1).
\end{aligned}''')
b+='以上乘入了初态$l$型二重项分裂数$v+1$作为权重。（二重简并模式$v$态的基函数由$v=1$的基函数取$v$次幂而成，有$v+1$个独立基函数，例如$E^2=A_1+E$（$v=2$）、$E^3=2E$（$v=3$）。\n\n红外光谱强度比：\n\n'+math(r'(d\mu_{\mathrm{sym}}/dr_{\mathrm{CH}})^2/(d\mu_{\mathrm{deg}}/dr_{\mathrm{CH}})^2\approx G_{\mathrm{sym}}\cos^2\tau/G_{\mathrm{deg}}\sin^2\tau\approx0.913')
b+='拉曼带强度比：\n\n'+math(r'''\begin{aligned}I_{\mathrm{sym}}/I_{\mathrm{deg}}&\approx\frac{G_{\mathrm{sym}}[15(1+2r)^2+(21/4)(1-r)^2(1-3\cos^2\tau)^2]}{(63/2)G_{\mathrm{deg}}(1-r)^2\sin^2\tau(1+3\cos^2\tau)}\\&\approx0.119+0.762(1+2r)^2/(1-r)^2.
\end{aligned}''')
add(252,b,[3],'Q123：本页τ称HCX角，后文p5又将τ称HCH角，各处保留，不统一。0.5的Q下标a1原样保留。关于简并基函数的E³=2E及矩阵元权重原叙述保留，模式计数/归一化须结合第2部分；不能把两模式权重合并到单个张量分量。')
b='对于烷基链的基频（$v=1-0$），以甲基全对称振动为基准比较$\\eta_{\\mathrm{vib}}=\\beta_0(Q_{\\mathrm{vib}}^2)_{1,0}$，得到：\n\n'
b+=math(r'''\begin{aligned}\eta_{\mathrm{sym}}&=\beta_0(Q_{\mathrm{sym}}^2)_{1,0},\\
\eta_{\mathrm{deg}}&=\beta_0(Q_{\mathrm{deg}}^2)_{1,0}=2\omega_{\mathrm{sym}}/\omega_{\mathrm{deg}}\approx1.95\eta_{\mathrm{sym}},\\
\eta_{a1}&=\beta_0(Q_{a1}^2)_{1,0}=2\omega_{\mathrm{sym}}/\omega_{a1}\approx1.01\eta_{\mathrm{sym}},\\
\eta_{b1}&=\beta_0(Q_{b1}^2)_{1,0}=2\omega_{\mathrm{sym}}/\omega_{b1}\approx0.98\eta_{\mathrm{sym}}.
\end{aligned}''')
b+='据此可得到甲基与亚甲基的和频张量分量关系。以甲基$\\beta_{aac}$为基准，记为$\\beta_{aac}^*$；以下分别在各基团固定的局部坐标系中表示。\n\n| 分量 | CH₃ | CH₂ |\n|---|---|---|\n| $\\beta_{aac}$ | $\\beta_{aac}^*$ | $-1.80\\beta_{aac}^*$ |\n| $\\beta_{ccc}$ | $0.25\\beta_{aac}^*$ | $-0.90\\beta_{aac}^*$ |\n| $\\beta_{aaa}$ | $1.49\\beta_{aac}^*$ | $-1.84\\beta_{aac}^*$ |\n| $\\beta_{caa}$ | $-1.05\\beta_{aac}^*$ | $-1.84\\beta_{aac}^*$ |\n\n'
b+='类似地，对乙烯基的=CH₂与乙炔基的≡CH，以CH₂的$\\beta_{aac}$（记为$\\beta_{aac}^+$）为基准比较，得到下列结果。两种基团均取C=C键为$c$轴、分子平面内取$a$轴。\n\n| =CH₂ | ≡CH |\n|---|---|\n| $\\beta_{aac}=\\beta_{aac}^+$ | $\\beta_{aac}=-0.51\\beta_{aac}^+$ |\n| $\\beta_{ccc}=0.33\\beta_{aac}^+$ | $\\beta_{acc}=\\beta_{cac}=\\beta_{cca}=-0.30\\beta_{aac}^+$ |\n| $\\beta_{aaa}=\\beta_{caa}=1.04\\beta_{aac}^+$ | $\\beta_{ccc}=-0.17\\beta_{aac}^+$ |\n|  | $\\beta_{aaa}=-0.89\\beta_{aac}^+$ |\n|  | $\\beta_{aca}=\\beta_{caa}=-0.51\\beta_{aac}^+$ |\n\n'
add(253,b,[3,4],'Q123：ηdeg/ηa1/ηb1的等号链将有量纲量与频率比相连，候选为在频率比后补ηsym或视作比值定义，未采用；末尾已写的ηsym照录。≡CH处仍写取C=C键，原层次/键名保留，候选为相应分子轴待核。星号和加号在此是基准标记，不解释为共轭或传播方向。')
b='## 1. 振动偶极矩、拉曼张量、和频张量\n\\nCH键伸缩引起的偶极矩和光散射张量变化分别写为$(d\\mu/dr)_0\\Delta r=\\mu_{\\mathrm{CH}}\\Delta r$和$(d\\alpha/dr)_0\\Delta r=\\alpha_0\\Delta r$，其中$r$表示CH键伸缩。为统一处理甲基、亚甲基和次甲基，使用附录2c的质量调整（mass adjusted）坐标较方便。再假设不与弯曲等振动耦合。（即使在谐振子近似内，原则上仍有耦合。尤其HCH弯曲、HCC弯曲、CC伸缩、CO伸缩等频率接近的模式会强烈混合，论文的归属通常只标贡献最大的振动模式，可通过计算势能分布（potential energy distribution，原缩写PES）估计。）\n\n在这些近似下，CH伸缩独立于其他振动构成简正坐标，CH₃、CH₂和CH的局部对称坐标与简正坐标一致。因此CH可按双原子分子处理，其质量调整简正坐标为：\n\n'
b+='由经典力学可知，一组谐振子的总能量可写成$\\sum[(dQ/dt)^2+\\lambda Q^2]$。\n\n'+eq('1.1').replace('\\sqrt{G_{\\mathrm{CH}}}','G_{\\mathrm{CH}}')
b+='其中$G_{\\mathrm{CH}}$如下定义；对双原子分子它是约化质量的倒数。\n\n'+eq('1.2')+'以$K$为弹簧常数，势能为：\n\n'+eq('1.3')
b+='令$F_{\\mathrm{CH}}=K$，则$\\lambda_{\\mathrm{CH}}=F_{\\mathrm{CH}}G_{\\mathrm{CH}}$，由$\\nu\\ (\\mathrm{cm}^{-1})=\\sqrt{\\lambda_{\\mathrm{CH}}}/(2\\pi c)$可知其正比于固有振动频率的平方。\n\n'
b+='CH₂的两个CH伸缩位移为$\\Delta r_1$、$\\Delta r_2$，其对称和反对称模式为：\n\n'+eq('1.4a')+eq('1.4b')+'HCH角为$\\alpha$时：\n\n'+eq('1.5a')+eq('1.5b')
b+='势能如下，使用正四面体角的$\\cos\\alpha=-1/3$：\n\n'+eq('1.6')
b+='这里$F$是所谓Shimanouti field中引入的H···H排斥项力常数，取$F^{\\prime\\prime}=-0.1F$，并使用正四面体角。因此：\n\n'+math(r'\lambda_{a1}=(K+K^{\prime}+4F/3)G_{a1},\qquad\lambda_{b1}=(K-K^{\prime}-0.2F/3)G_{b1}')
b+='CH₃的三个CH伸缩位移为$\\Delta r_1,\\Delta r_2,\\Delta r_3$，全对称模式与两个简并模式如下。选取$ac$平面包含H₁原子。\n\n'+eq('1.7a')+eq('1.7b')+eq('1.7c')+eq('1.8a')+eq('1.8b')
b+='这里$\\tau$为HCH键角，因此正四面体角下$\\cos\\tau=-1/3$。势能为：\n\n'+eq('1.9')+math(r'\lambda_{\mathrm{sym}}=(K+2K^{\prime}+2.03F)G_{\mathrm{sym}},\quad\lambda_{\mathrm{deg}}=(K-K^{\prime}-0.07F)G_{\mathrm{deg}}')
add(254,b,[4,5,6],'Q124：1.1原分母为GCH，而p7重引该式时写√GCH；两处分别保留，候选1.1补根号未采用。总能量式原未列1/2。1.6、1.9首个势能式未显式列后式排斥项而等号连接，原样保留，未补项。τ在此按HCH角定义，关联Q123。')

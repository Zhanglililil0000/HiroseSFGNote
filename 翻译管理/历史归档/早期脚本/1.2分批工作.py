from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.2';p=r/'中文版本/第一章 SFG快速入门/1.2 振动共振、费米共振与双原子分子.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B028-修订前.md');s=s.replace('​\t','').replace('SFG 感受率','二阶非线性极化率').replace('谱带的感受率张量','谱带的极化率张量').replace('与感受率的平方','与极化率的平方');s=s.replace('本章将说明','本节将说明')
# Missing hbar factor in old equation1-2.
a=s.index('$$',s.index(r'\tag{1-1}'))+2;b=s.index(r'\tag{1-2}',a);t=s[a:b].replace(r'\sum_s \left[',r'\sum_s \frac{1}{\hbar}\left[');s=s[:a]+t+s[b:]
# Source1-5 includes its complex conjugate expression, absent in old translation.
pos=s.index(r'\tag{1-5}');extra=r'\\ (\alpha^*_{\alpha\beta})_{vg}=\frac{1}{\hbar}\sum_s\left[\frac{(er_\alpha)_{gs}(er_\beta)_{sv}}{\omega_{sv}+\omega}+\frac{(er_\beta)_{gs}(er_\alpha)_{sv}}{\omega_{sg}-\omega}\right]'+'\n';s=s[:pos]+extra+s[pos:]
a=s.rfind('$$',0,s.index(r'\tag{1-7}'));b=s.index('$$',s.index(r'\tag{1-7}'))+2
s=s[:a]+r'''$$
\begin{aligned}
\beta_{\alpha\beta\gamma}&=\langle g|\hat\beta_{\alpha\beta\gamma}|g\rangle\\
&=\sum_v\frac{(\hat\alpha_{\alpha\beta})_{gv}(\hat\mu_\gamma)_{vg}}{\hbar(\omega_2-\omega_{vg}-i\Gamma_{\mathrm{vib}})}(\rho_g^{(0)}-\rho_v^{(0)})\\
&=\sum_v\frac{(\hat\beta^R_{\alpha\beta\gamma})_{gg}}{\hbar(\omega_2-\omega_{vg}-i\Gamma_{\mathrm{vib}})}(\rho_g^{(0)}-\rho_v^{(0)})
\end{aligned}
\tag{1-7}
$$'''+s[b:]
s=s.replace(r'\left( \frac{\partial \mu_{\gamma}}{\partial q_v} \right)_0 \sum_v \hat{q}_v',r'\sum_v\left( \frac{\partial \mu_{\gamma}}{\partial q_v} \right)_0 \hat{q}_v').replace(r'\left( \frac{\partial \alpha_{\alpha\beta}}{\partial q_v} \right)_0 \sum_v \hat{q}_v',r'\sum_v\left( \frac{\partial \alpha_{\alpha\beta}}{\partial q_v} \right)_0 \hat{q}_v')
s=s.replace('请参考第五章 *张量·对称性* 中的第一部分 *SFG 张量与对称性* 以及第二部分 *基与特征标表*','请参考作者“テンソル・対称性”文件夹中的“SFGテンソルと対称性”和“基底とキャラクターテーブル”文件')
s=s.replace('对应于全对称种的基态','是全对称种的基函数').replace('构成二重简并种的基态','构成二重简并种的基函数').replace('%、%',' $、$ ')
s=s.replace('（$R_a, R_b$\\）','（$R_a, R_b$）').replace('($R_a, R_b$\\)','($R_a, R_b$)')
s=s.replace('是全对称 HCH 弯曲振动的倍频，即简并','是全对称 HCH 弯曲振动的倍频，以及简并')
s=s.replace(r'$2 \left( k_{r_1 \phi_1 \phi_1} - \frac{k_{r_1 \phi_2 \phi_3}}{2} + 2k_{r_1 \phi_2 \phi_2} - k_{r_1 \phi_1 \phi_2} \right).$',r'$\sqrt{2}\left(k_{r_1\phi_1\phi_1}-\frac{k_{r_1\phi_2\phi_3}}{2}-2k_{r_1\phi_2\phi_2}-k_{r_1\phi_1\phi_2}\right)$。')
s=s.replace('**绕旋转后的 Y 轴旋转角度 $\\theta$ **','**绕旋转后的 Y 轴旋转角度 $\\theta$**').replace('以 Z 轴和 Y 轴的负方向为正方向观察','沿 Z 轴和 Y 轴从负方向朝正方向观察')
# Add source-vs-translation cautions at the applicable sections.
s=s.replace('### 二重简并\n','> **译者注（Q025）：** 此处“基底”指基函数，旧译误作基态已改。底本对圆柱坐标与球坐标分量的归一化、$q^\pm$的符号/比例有不一致迹象（包括后续$\\sqrt2$关系），以下保留原式，未作统一归一化；$l$型分裂的MHz与波数数量级也按原文列出，待复核。\n\n### 二重简并\n',1)
s=s.replace('## 3. 双原子分子的 SFG 张量：分子坐标系与表面坐标系','> **译者注（Q026）：** 本段$a,b$与跃迁概率/谱强的关系按作者原话列出；应区别跃迁振幅、概率与SFG极化率，不能将$a^2+b^2=1$直接解释为两条SFG谱带的光强守恒。\n\n## 3. 双原子分子的 SFG 张量：分子坐标系与表面坐标系',1)
# Original3-2 product matrix has a nonzero row2 col3, unlike its factors; show bottom discrepancy in note, retain old computed0 explicitly.
s+='\n> **译者注（Q027）：** 式（3-2）原文乘积矩阵第二行第三列写作$\\sin\\chi\\sin\\theta$，与前列两矩阵相乘不符；此处保留旧译的$0$并明确记下原值。式（3-4）的$E_{2,b}$正号按底本保留，与式（3-2）的符号衔接待核。末尾随机取向非零分量清单亦按原文保留，未作为完整张量表的独立证明。\n'
# Apply verified existing reflow helper, preserving matrix row/column syntax inside matrices.
helper=(m/'B019至21工作.py').read_text(encoding='utf-8');fn=helper[helper.index('def reflow(mat):'):helper.index("t=re.sub(r'\\$\\$",helper.index('def reflow(mat):'))];exec(fn)
def flow(mat):
 if r'\begin{pmatrix}' in mat.group(1):
  tex=mat.group(1).replace(r'\begin{align*}',r'\begin{aligned}').replace(r'\end{align*}',r'\end{aligned}')
  tag=re.search(r'\\tag\{[^}]+\}',tex);tex=tex.replace(tag.group(0),'') if tag else tex
  return '$$\n'+tex+'\n'+(tag.group(0) if tag else '')+'\n$$'
 return reflow(mat)
s=re.sub(r'\$\$([\s\S]*?)\$\$',flow,s)
s=s.replace('> 中文翻译：章力','> 中文翻译：章力\n\n> **校订状态（2026-10-16）：** B028—B034全12页已分批页面对照及排版整理；Q025—Q027等原式约定未决，见注。')
p.write_text(s,encoding='utf-8')
# Split into small logical units; no formula cut in half.
markers=[s.index('### 二重简并振动'),s.index('### 三重简并\n'),s.index('## 2.'),s.index('作为具体实例'),s.index('## 3.'),s.index('分子中诱导的极化在分子固定系')]
# include paragraph boundary before markers to avoid partial prefixes
markers=[s.rfind('\n',0,x)+1 for x in markers];bounds=[0]+markers+[len(s)]
scopes=['p1—2至非简并振动；1-1至1-12','p2末—4二重简并至1-20','p4—5三重简并全部矩阵元','p5—8首费米共振一般讨论及2-1至2-7','p8甲基CH/HCH例与四类非谐常数','p8末—10双原子分子坐标与3-1至3-5','p11—12逆变换、3-6/3-7及八类偏振组合']
for i,(a,b,scope) in enumerate(zip(bounds,bounds[1:],scopes),28):
 id=f'B{i:03d}';(o/f'{id}-本批译文.md').write_text(f'# {id}：1.2分批校订\n\n'+s[a:b],encoding='utf-8');(o/f'{id}.md').write_text(f'''# {id} 校订记录

2026-10-16。范围：{scope}。逐段及公式页面对照，原图本目录原文p1至12.png。联合修订前备份B028-修订前.md；分批输出/渲染保留。

修订汇总：1-2补旧译漏掉的内层1/hbar；1-5补旧译漏掉的共轭表达式；1-7及1-9/1-10将求和放回底本位置。基底误译为基态已改，三重简并段被%隐藏的定义恢复。甲基例全对称两种通道的“以及”恢复；第二耦合系数2改sqrt2、+2k改−2k，均按原页。原文件引用恢复。所有偏振组合、三重简并无编号矩阵元及3-7a/b/c均纳入覆盖。

Q025归一化/分裂数量级，Q026振幅/概率用语，Q027矩阵乘积及E2b符号/末尾分量表保留问题并注明；不冒称已推导解决。SFG宏观chi用二阶非线性极化率，微观beta不机械等同宏观量。
''',encoding='utf-8')
p=m/'疑难与勘误.md';t=p.read_text(encoding='utf-8')+'\n| Q025 | 1.2 p3—5 | 简并坐标q±归一化与符号、l型分裂数量级 | 原式约定/P1 | B028—B030按原文保留并注；基底误译基态已改，不统一未证归一化 |\n| Q026 | 1.2 p7—8 | a/b与振幅、概率及SFG光强用语应区分 | 原文表述/P2 | B031/B032保留作者讨论并注明非光强守恒断言 |\n| Q027 | 1.2 p10—12 | 3-2矩阵乘积原第三列与因子矛盾，3-4 E2b符号及末尾分量表待核 | 原式公式/P1 | B033/B034注明原矩阵值并保留旧译0，其他按底本留存，不作已验证推导 |\n';p.write_text(t,encoding='utf-8')
print('1.2 processed as seven bounded review units B028–B034; missing formulas and material coefficients restored.')


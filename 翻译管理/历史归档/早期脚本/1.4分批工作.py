from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.4';p=r/'中文版本/第一章 SFG快速入门/1.4 电偶极子的电场与辐射.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B039-修订前.md');s=s.replace('> 原作：广瀬千秋','> 原作：广濑千秋、狩野觉（原文署名：广濑・狩野合作）').replace('​\t','').replace('菲涅尔系数','菲涅尔因子')
a=s.index('| 电磁学基本方程');b=s.index('在麦克斯韦方程组中',a);s=s[:a]+r'''| 定律 | 原表“电磁学基本方程” | 麦克斯韦方程组 |
|---|---|---|
| 库仑定律 | $\nabla\cdot\mathbf D=4\pi\rho$ | $\nabla\cdot\mathbf D=4\pi\rho$ |
| 安培定律 | $\nabla\times\mathbf H=\frac{4\pi}{c}\mathbf J$ | $\nabla\times\mathbf H=\frac{4\pi}{c}\mathbf J+\frac1c\frac{\partial\mathbf D}{\partial t}$ |
| 法拉第定律 | $\nabla\times\mathbf E+\frac1c\frac{\partial\mathbf B}{\partial t}=0$ | $\nabla\times\mathbf E+\frac1c\frac{\partial\mathbf B}{\partial t}=0$ |
| 磁单极子不存在 | $\nabla\cdot\mathbf B=0$ | $\nabla\cdot\mathbf B=0$ |

'''+s[b:]
s=s.replace('（原注：应为式 1.8 的偶极子代入式 1.9）','（原文引用式 1.8，此处的代入关系见译者注）')
s=s.replace('near zone','近区').replace('far zone','远区').replace('near field','近场').replace('intermediate zone','中间区')
s=s.replace('near (static) zone','近区（静态区）').replace('intermediate (induction) zone','中间区（感应区）').replace('far (radiation) zone','远区（辐射区）')
s=s.replace('在源外部', '在源外部').replace('方位角 $\\theta$','方向角 $\\theta$').replace('方位角 $\\beta$','方向角 $\\beta$')
s+='\n> **译者注（Q029）：** 本节使用cgs高斯单位制。式（2.2）/（2.3）的$k^2$幂次、式（2.3）的立体角积分测度、式（3.1）与（3.2）/后文的符号不一致、式（3.3）省略总功率$P$、$R/T$的归一化，以及式（4.3）与前两式点积不一致等均为底本疑点，按原文列出，未作推导修正版。功率段原文引用式（1.8），不是作者已给出的更正注；旧译的“原注：应为……”已删除。\n'
helper=(m/'B019至21工作.py').read_text(encoding='utf-8');fn=helper[helper.index('def reflow(mat):'):helper.index("t=re.sub(r'\\$\\$",helper.index('def reflow(mat):'))];exec(fn)
def flow(mat):
 if r'\begin{pmatrix}' in mat.group(1):return mat.group(0)
 return reflow(mat)
s=re.sub(r'\$\$([\s\S]*?)\$\$',flow,s);s=s.replace('> 中文翻译：章力','> 中文翻译：章力\n\n> **校订状态（2026-10-16）：** B039—B043全9页已分批页面对照及排版整理；原式疑点Q029未决，见末注。')
p.write_text(s,encoding='utf-8')
markers=[s.index('由此，源外部'),s.index('**(2)**'),s.index('## 3.'),s.index('（下标 $s$ 和 $p$')];markers=[s.rfind('\n',0,x)+1 for x in markers];bounds=[0]+markers+[len(s)]
scopes=['p1—2，引言、1.1至1.3及完整双列方程对照表','p3—4，1.4至1.12b及第1条近场讨论','p5，讨论2/3及功率2.1至2.4','p6—7，界面自发辐射坐标与3.1至3.4b','p8—9，出射过程、SFG几何4.1至4.3及结语']
for i,(a,b,scope) in enumerate(zip(bounds,bounds[1:],scopes),39):
 id=f'B{i:03d}';(o/f'{id}-本批译文.md').write_text(f'# {id}：1.4分批校订\n\n'+s[a:b],encoding='utf-8');(o/f'{id}.md').write_text(f'''# {id} 校订记录

2026-10-16。范围：{scope}。逐页核对文字、矩阵、编号式、无编号场/功率式和比较表。恢复旧译漏掉的基本方程一列（特别是不含位移电流的安培式），补狩野合作署名；“原注应为”不是原文，改为译者说明。统一近区/中间区/远区与菲涅尔因子。

Q029列明原文k幂次、积分测度、矩阵方向余弦符号、缺P及功率归一化、4.3点积等；按原文不猜修。保留作者提出但未完成的计算和猜想语气，不写成定论。备份B039-修订前.md，源图本目录原文p1至9.png。下一节英文历史书目1.5。
''',encoding='utf-8')
p=m/'疑难与勘误.md';t=p.read_text(encoding='utf-8')+'\n| Q029 | 1.4 p5—9功率、方向余弦及点积 | k幂次/积分测度、3.1与3.2符号、3.3缺P、R/T归一化、4.3与矩阵点积不一致 | 原式公式/P1 | B039—B043照底本并注；恢复漏列方程表，去掉伪称原注的旧译说明；未独立推导改式 |\n';p.write_text(t,encoding='utf-8')
print('1.4 reviewed as five units; missing comparison-table column restored; source contradictions marked.')

from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B024-修订前.md');a=s.index('## 附录 C');t=s[a:].replace('​\t','').replace('P_{n\'n}$ 密度矩阵','P_{n\'n}$。密度矩阵')
x=t.index(r'\tag{C-4}');y=t.index(r'\tag{C-5}');sub=t[x:y].replace(r'(r_k)_{nn\'\'}',r'(r_k)_{nn\'\'}') if False else t[x:y]
sub=sub.replace("(r_k)_{nn''} \\rho^{(1)}(\\omega_1)_{nn''}","(r_k)_{nn''} \\rho^{(1)}(\\omega_1)_{n''n'}");t=t[:x]+sub+t[y:]
t=t.replace('为 ωj，其电场的方向为 j 轴','为 $\\omega_j$，其电场的方向为 $j$ 轴')
note='> **译者注（Q023）：** 式（C-3）及（C-5）中有独立的衰减常数项，式（C-5）的差频式仍写一阶密度矩阵，式（C-8）单频式中仍出现 $\\omega_1$。这些是底本原有写法，此处保留，不将其自动改写成推导修正版。\n\n'
t=t.replace('## 附录 C：密度矩阵中矩阵元素的微扰论计算\n\n','## 附录 C：密度矩阵中矩阵元素的微扰论计算\n\n'+note)
# Explicitly add missing transition sentence before third-order equations.
pos=t.index('$$',t.index(r'\tag{C-10}'))+2;t=t[:pos]+ '\n\n由此，三阶近似可按下式求得。\n'+t[pos:]
t += '\n> **译者注（Q024）：** 式（C-11）、（C-12）的递推式及展开式按底本列出；公共场因子与已有二阶密度矩阵的归一化衔接、展开等号后公共因子的省略，以及部分重复的矩阵元指标尚待独立推导核验。式（C-12）第三主组末子项的 $r_k$ 等指标未据对称性改动。\n'
helper=(m/'B019至21工作.py').read_text(encoding='utf-8');fn=helper[helper.index('def reflow(mat):'):helper.index("t=re.sub(r'\\$\\$",helper.index('def reflow(mat):'))];exec(fn);t=re.sub(r'\$\$([\s\S]*?)\$\$',reflow,t)
s=s[:a]+t;s=s.replace('红外-可见和频过程（SFG）是由照射的红外光和可见光与分子相互作用的微扰中的二阶项：相互作用微扰 $H\'$ 引起的。','红外-可见和频过程（SFG）由红外光和可见光与分子相互作用的二阶微扰产生。相互作用微扰记为 $H\'$。');p.write_text(s,encoding='utf-8')
# Complete formula units even where source spans pages.
ends=[]
for tag in ['C-5','C-10','C-11']:
 ends.append(t.index('$$',t.index('\\tag{'+tag+'}'))+2)
parts=[t[:ends[0]],t[ends[0]:ends[1]],t[ends[1]:ends[2]],t[ends[2]:]]
for id,txt,scope in zip(['B024','B025','B026','B027'],parts,['p18下半—19，C-1至C-5及全部说明','p20，C-6至C-10','p21—22首，完整C-11及三阶引导句','p22—23，完整C-12及疑点注']):
 (o/f'{id}-本批译文.md').write_text(f'# {id}：附录C分批校订\n\n'+txt,encoding='utf-8');(o/f'{id}.md').write_text(f'''# {id} 校订记录

2026-10-16。范围：{scope}。按原页核对各分母、矩阵元、占据差、频率符号及负频输入。C-5中旧译两处第三项rho下标nn″按底本改为n″n′；C-6第四项重复rk/rj、C-8残留omega1、C-12第三组末项rk等底本问题保留，不静默推改。C-3/C-5的裸衰减项与差频阶数登记Q023；三阶式归一化/公共因子及重复指标登记Q024。

C-11前原文三阶引导句已补齐。C-11和C-12均按完整式划批（各六主组，前四组各四子项、末两组各两子项并有矩阵元和），不将跨页公式切在中间。版式改为aligned并在完整分式间换行。备份B024-修订前.md保留附录C修订前；原图续校-原文p18至23.png。下一步1.1整节覆盖/符号/渲染及导读检查。
''',encoding='utf-8')
p=m/'疑难与勘误.md';z=p.read_text(encoding='utf-8')+'\n| Q023 | 1.1附录C p19—20 | C-3/C-5衰减裸项、C-5差频阶数、C-6重复指标及C-8残留omega1 | 原式公式/P1 | B024/B025按底本保留并注；仅改C-5旧译两处rho下标，未独立推导原式 |\n| Q024 | 1.1附录C p21—23 | C-11/C-12归一化和公共因子省略、重复指标 | 原式公式/P1 | B026/B027照底本并注，未将候选推导当确定修正 |\n';p.write_text(z,encoding='utf-8')
print('AppendixC split four complete units; C5 transcription repaired, source issues explicitly retained.')

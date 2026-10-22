from 整节续校工具 import *
mother=(OUT/'母本夹膜及D参考.md').read_text(encoding='utf-8')
u=mother[:mother.index('#### 内部光')]
for q in ['Q047','Q057']:u=u.replace(q,'关联第2.2节'+q)
mapping=[('B080-p41-01.png','ch02-s03-fig02.png'),('B080-p42-02.png','ch02-s03-fig03.png'),('B080-p43-04.png','ch02-s03-fig04.png'),('B080-p43-05.png','ch02-s03-fig05.png')]
for a,b in mapping:u=u.replace('../assets/ch02/s02/'+a,'../assets/ch02/s03/'+b)
u=u.replace('底本p41','独立底本p7').replace('底本p42','独立底本p7').replace('底本p43','独立底本p8').replace('跨p43—44','位于独立底本p9')
u=u.replace('E-2.2-005','E-2.3-001')
u=u.replace(tex('$(-2nh_m§tan§theta_m,0)$'),tex('$(-2h_m§tan§theta_m,0)$'),1)
where='这里使用 '
pos=u.index(where)
u=u[:pos]+tex('''> **译校注（Q075，保留原式）：** 独立PDF p7的入射点坐标写作 $(-2h_m§tan§theta_m,0)$，但同列又给出 $n=1,2,§ldots$，后续光程项含 $n$。本处不补写坐标中缺少的 $n$；候选 $(-2nh_m§tan§theta_m,0)$ 仅供核查。

''')+u[pos:]
# In the independent PDF two pi symbols have a printed subscript m.
def phase(m):
 block=m.group()
 if tex('§tag{C.2}') not in block:return block
 lines=block.splitlines();key=tex('i2§pi n_m2h_m');value=tex('i2§pi_m n_m2h_m')
 for i,line in enumerate(lines):
  if line.startswith('&=r_{1m}+'):
   pre,post=line.rsplit(key,1);lines[i]=pre+value+post
  elif '[-r_{1m}r_{m1}+' in line:lines[i]=line.replace(key,value,1)
 return '\n'.join(lines)
u=re.sub(r'\$\$[\s\S]*?\$\$',phase,u)
u=u.replace('模平方给出光强，因此',tex('> **译校注（Q076，保留原字形）：** 独立PDF p8，式（C.2）第一条闭式的分母和下一行分子中，$§pi$ 另带一个下标 $m$，排为 $§pi_m n_m$。此处按局部放大图保留；候选去除 $§pi$ 的下标 $m$ 未采用。\n\n')+'模平方给出光强，因此')
u=u.replace(tex('§Delta§nu=1/(2n_mh_m§cos§theta_m)'),tex('§Delta§nu=1/2n_mh_m§cos§theta_m'))
u+=tex('''
> **译校注（斜线与干涉量）：** 两处条纹间隔均按底本保留 $§Delta§nu=1/2n_mh_m§cos§theta_m$ 的连写。候选将分母整体读作 $2n_mh_m§cos§theta_m$，不把补括号写成原式。净相位差中的因子2问题沿关联第2.2节Q057保留；不据此自动调整周期或系数。
''')
put('B120','### 两种介质之间夹有薄膜的系统','### 关于"内部光"',u,'夹膜定义、反射与透射求和',[6,9],['全量界面/折射率/角度/场系数定义','独立p7/p8四幅示意图，保留重复原图','反射路径表、全部C.2求和及闭式；Q075、Q076原字形保留','透射路径表、全部C.3求和与闭式、条纹及峰谷关系','原文“加重反射”暂按“多重反射”译；就地E-2.3-001登记'])

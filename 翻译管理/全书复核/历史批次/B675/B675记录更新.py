from pathlib import Path
import json,shutil,re,math,cmath,random
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B675修改前'
changes=[];notes={}
def edit(rel,fn):
 p=R/rel;s=p.read_text(encoding='utf-8-sig');t=fn(s)
 if s!=t:
  b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
  p.write_text(t,encoding='utf-8');changes.append(rel)
def append(rel,text):edit(rel,lambda s:s if text.splitlines()[0] in s else s.rstrip()+'\n\n'+text+'\n')
p81='中文版本/第八章 拟合/8.1 和频光谱的线形.md';p82='中文版本/第八章 拟合/8.2 和频光谱分析便览.md';p83='中文版本/第八章 拟合/8.3 拟合概述.md'
q311=r'式(A4)最后一个极限下标原印为 $x\to0$，而所变参数似应为 $\alpha$；式(A5)则印 $\alpha\to0$，分别保留，不统一改动。'
new311=r'B675放大原页确认式(A4)、(A5)均印 $\alpha\to0$；旧注称(A4)为 $x\to0$ 是译者误读，现撤回。原式未明确正侧极限及分布条件，此疑点保留。'
edit(p81,lambda s:s.replace(q311,new311))
edit('翻译管理/疑难与勘误.md',lambda s:s.replace(q311,new311))
old319=r'所印 $f_{ir}$ 与 $g_{ir}$ 的指数分别是 $-4\ln2\,\delta_{ir}^2/\Delta_{ir}^2$ 和 $-2\ln2\,\delta_{ir}^2/\Delta_{ir}^2$，因此并非简单的 $f_{ir}=\sqrt2g_{ir}$。'
new319=r'B675放大确认条件3文字原印为 $\sqrt{2g_{ir}(\delta_{ir})}$，已修复旧译把g移出根号的转写错误；旧注不应据此称原文写了 $f_{ir}=\sqrt2g_{ir}$。所列f、g的指数分别为 $-4\ln2\,\delta_{ir}^2/\Delta_{ir}^2$ 和 $-2\ln2\,\delta_{ir}^2/\Delta_{ir}^2$；两者各自面积归一，关系须按平方后重新归一计算，仍与该原句不一致。'
edit(p83,lambda s:s.replace(r'原文说，此时采用 $\sqrt2g_{ir}(\delta_{ir})$ 作归一化函数',r'原文说，此时采用 $\sqrt{2g_{ir}(\delta_{ir})}$ 作归一化函数').replace(old319,new319))
edit('翻译管理/疑难与勘误.md',lambda s:s.replace(old319,new319))
inserts={p81:[('> **原文条件待核（Q311',r'> **数学条件补充（B675，Q311）：** 对实数a≠0，洛伦兹积分为π/|a|；原印π/a及虚部积分−π需要a>0。实部积分为零须取对称主值；δ正则化应明示正侧极限与分布意义。此处只说明使用条件，不改原式。'),('> **原文表述待核（Q312',r'> **适用范围补充（B675，Q312）：** 偶极矩乘场除以普朗克常数给出频率量纲，不能直接作为时间周期。即使另假定指数弛豫，一个平均等待时间内也不保证必有事件；原文的动力学及熵说明未给出完整模型，保留作者说法。'),('> **原文疑点（Q313',r'> **能流与符号补充（B675，Q313）：** 若采用本段负时间指数、实场E₀cosωt及正阻尼，平均物质受功为ωE₀²Imχ/2。近共振改写上述分母时须同时改变分子整体号；原(B9)最后正虚部式与前式存在符号差异。原式图保留，未把这组条件跨章套用。'),('> **原文疑点（Q314',r'> **变换与完整性补充（B675，Q314）：** 令τ=t−t₁后，负时间指数电场应分解出正号的延迟指数；(C2)/(C5)的符号衔接已复核，仍未统一改式。总场乘积有两个vis/IR次序，能否合并须先约定响应核的对称化及半幅系数。p14作者未证明与未解决之处均已译出。')],p82:[('> **原文记号疑点（Q315',r'> **本轮复核（B675，Q315/Q316）：** 原页频率标签混用及强度比例因子的省略已确认，保留原图；分子数积分与谱宽问题沿用B667的条件性复核，不据此静默改写本节。')],p83:[('> **原文记号疑点（Q318',r'> **雅可比使用条件（B675，Q317/Q318）：** 对实参数应按2Re(E*∂E/∂u)计算强度导数；原页三条单带电场偏导可由共振分母直接求得。原图的uSF、漏求和及前述宽度比较仍保留疑点，不据校验示例补改原图。'),('> **原文积分变量疑点（Q320',r'> **截断与求导提示（B675，Q319/Q320）：** 两套高斯函数分别面积归一，光强权重等于电场权重平方后再归一。单变量与双变量积分须各自指定宽度和区间；若数值截断端点随拟合参数移动，求导还须检查边界项。本稿未附原程序，不能把条件性雅可比示例视为作者实现已通过测试。'),('> **原文宽度用语疑点（Q321',r'> **宽度关系补充（B675，Q321）：** 对纯高斯函数，原函数半高处在其平方中成为四分之一高度，而平方函数的半峰全宽缩为原来的1/√2。高度比例与宽度比例需区分；含均匀展宽或背景时不能直接照搬。'),('> **原文记号及收敛条件疑点（Q322',r'> **迭代边界补充（B675，Q322）：** 正规方程给出的是线性化的最小二乘步；即使雅可比满列秩，非线性全步更新仍可使残差增大。vx的维数冲突及原文停止条件保留，不据此宣布拟合已达到全局最优。')]}
for rel,items in inserts.items():
 def add(s):
  for prefix,note in items:
   if note not in s:
    line=next(x for x in s.splitlines() if x.startswith(prefix));s=s.replace(line,line+'\n\n'+note,1)
  return s
 edit(rel,add);notes[rel]='\n\n'.join(n for _,n in items)
append('翻译管理/疑难与勘误.md','''## B675：第八章剩余附录及拟合专项复核（2026-10-22）

Q311—Q322本轮处置见[专项报告](全书复核/B675附录与拟合复核.md)。Q311的(A4)极限下标误报撤回，Q319文字根号转写按原页修复，均非原文修正。积分条件、吸收号、傅里叶核、雅可比、归一化、截断、宽度和迭代条件已作明确条件的复核；作者未说明部分仍保留，未新增Q/E。Q316沿用B667核查，不重复声称新增底本证据。''')
append('翻译管理/符号与约定.md','''## B675：附录、拟合与条件边界

α→0需分清正侧和分布意义；(A4)原印确为α，不是x。吸收符号与时间指数、近共振分母整体号及半幅约定共同转换。8.3的g与f各自面积归一，不能相互直接平方或仅乘√2；条件3文字根号覆盖2g整体。参数求导按实参数复模平方规则，有限截断另查边界项。正规方程只保证相应线性化问题的最小二乘性质。详见[B675报告](全书复核/B675附录与拟合复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B675核查与译者修复（2026-10-22）

Q311旧注把(A4)的α→0读成x→0，现撤回这一子项；Q319条件3的文字根号覆盖2g整体，已恢复旧译移出根号的g。两项均为译者修复，原式图不改，不新增E。Q311其余积分条件及Q312—Q322未获确认的原文修法仍保留；Q316沿用B667。专项证据见[附录与拟合复核](../../翻译管理/全书复核/B675附录与拟合复核.md)。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B675补充

先放大确认字形再判断原式错误；Q311极限下标和Q319根号误读已修复，历史判断须与现行状态区分。积分、时间指数、归一化、截断及拟合迭代的条件性核查不等于确认作者修式，见[B675报告](B675附录与拟合复核.md)。''')
(O/'B675新增阅读提示.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2),encoding='utf-8')
# Independent checks, with explicit chosen conventions.
checks={};random.seed(675)
checks['signed_lorentz_integrals']=[{'a':a,'area':math.pi/abs(a),'imaginary_area':-math.pi*math.copysign(1,a)} for a in [-2,-.3,.3,2]]
for a in [.1,1,3]:
 for x in [-2,-.5,0,.5,2]:
  plus=1/(2j*math.pi*(x-1j*a));minus=plus.conjugate()
  assert abs(plus+minus-a/(math.pi*(a*a+x*x)))<1e-12
  assert abs(plus-minus-x/(1j*math.pi*(a*a+x*x)))<1e-12
checks['delta_kernel_identity_cases']=15
checks['gaussian_test_function_delta_values']=[{'alpha':a,'positive_side':math.exp(a*a)*math.erfc(a),'negative_side':-math.exp(a*a)*math.erfc(a)} for a in [1,.1,.01,.001]]
checks['exponential_waiting_no_event_probability_at_mean']=math.exp(-1)
energy=[]
for w in [.6,.9,1,1.1,1.5]:
 gamma=.1;chi=1/(1-w*w-2j*gamma*w);n=4000;T=2*math.pi/w
 average=sum(math.cos(w*(k+.5)*T/n)*(-1j*w*chi*cmath.exp(-1j*w*(k+.5)*T/n)).real for k in range(n))/n
 exact=w*chi.imag/2;assert abs(average-exact)<1e-11 and exact>0
 energy.append({'omega':w,'time_average':average,'positive_absorption':exact})
checks['oscillator_energy']=energy
for w,t,tau in [(random.random()*4,random.random(),random.random()) for _ in range(40)]:assert abs(cmath.exp(-1j*w*(t-tau))-cmath.exp(-1j*w*t)*cmath.exp(1j*w*tau))<1e-12
checks['Fourier_substitution_cases']=40
gauss=[]
for width in [.4,1,3]:
 a=2*math.log(2)/width**2;g=lambda x:math.sqrt(a/math.pi)*math.exp(-a*x*x);f=lambda x:math.sqrt(2*a/math.pi)*math.exp(-2*a*x*x)
 for x in [0,width/3,width]:assert abs(f(x)-math.sqrt(2*math.pi/a)*g(x)**2)<1e-12
 assert abs((math.exp(-4*math.log(2)*(width/(2*math.sqrt(2)))**2/width**2))**2-.5)<1e-12
 gauss.append({'width':width,'squared_gaussian_fwhm':width/math.sqrt(2),'f_area':1,'g_area':1,'g_squared_area':math.sqrt(a/(2*math.pi))})
checks['gaussian_relations']=gauss
def grid(width):
 n=80;h=12*width/n
 return [(-6*width+j*h,h*(1 if j in [0,n] else 4 if j%2 else 2)/3) for j in range(n+1)]
ir_grid=grid(.25);g_grid=grid(.4)
def weights(x,width,field=False):
 a=(2 if field else 4)*math.log(2)/width**2
 f=math.sqrt(a/math.pi)*math.exp(-a*x*x)
 return f,f*(-1/width+2*a*x*x/width)
def field(x,v):
 A,center,gamma,br,bi,width=v;d=x-center+1j*gamma;e=br+1j*bi+A/d
 return e,[1/d,A/d**2,-1j*A/d**2,1,1j,0j]
def model(k,v):
 use_g=k>=4;coherent=k in [2,5,8];use_ir=k in [2,3,5,6,8,9];variable=k>=7
 def inner(shift):
  if not use_g:return field(.15+shift,v)
  e=0j;der=[0j]*6
  for x,w in g_grid:
   f,df=weights(x,v[5]);z,d=field(.15+shift+x,v);e+=w*f*z
   for i in range(5):der[i]+=w*f*d[i]
   der[5]+=w*df*z
  return e,der
 def squared(e,d):return abs(e)**2,[2*(e.conjugate()*z).real for z in d]
 if not use_ir:return squared(*inner(0))
 if coherent:
  e=0j;d=[0j]*6
  for x,w in ir_grid:
   f,_=weights(x,.25,True);z,dz=inner(x);e+=w*f*z
   for i in range(6):d[i]+=w*f*dz[i]
  return squared(e,d)
 val=0;der=[0.]*6
 for x,w in ir_grid:
  f,_=weights(x,.25);z,dz=squared(*inner(x));val+=w*f*z
  for i in range(6):der[i]+=w*f*dz[i]
 return val,der
v=[1.2,-.2,.3,.4,-.15,.4];errs=[]
for k in range(1,10):
 val,d=model(k,v)
 for i in range(6 if k>=7 else 5):
  h=1e-5;vp=v.copy();vm=v.copy();vp[i]+=h;vm[i]-=h;num=(model(k,vp)[0]-model(k,vm)[0])/(2*h)
  err=abs(num-d[i]);assert err<1e-6,(k,i,err)
  errs.append({'model':k,'parameter':i,'abs_error':err})
checks['nine_model_finite_difference_cases']=errs
checks['nine_model_scope']='独立单谱带示例，固定数值积分区间；非作者程序或所有原图公式认证'
p=.1;step=(1-p*p)/(2*p);old=(1-p*p)**2;new=(1-(p+step)**2)**2;assert new>old
checks['Gauss_Newton_counterexample']={'p':p,'step':step,'old_squared_residual':old,'new_squared_residual':new}
checks['changes']=changes;checks['adopted_source_corrections']=0
(O/'B675代数检查.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print('B675: source-reading fixes, notes and checks saved; nine models /',len(errs),'finite differences passed')

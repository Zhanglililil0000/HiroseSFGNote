from pathlib import Path
import json,shutil,math,cmath
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B674修改前'
rel='中文版本/第八章 拟合/8.1 和频光谱的线形.md';p=R/rel
note='> **积分与探测条件补充（B674，Q310）：** 复振幅的强度通常需取模平方；即使f取实数，也不能据此把复χ的普通平方当作非负强度。另须区别同一输出模式内的贡献相加、不同输出频率的积分及探测时间平均：相位锁定本身不保证所有差频交叉项都进入读数。式(18)未计系统谱相位，不能未经探测时间窗、带宽和归一化说明就与整脉冲能量等同。本批只补条件性说明，式(17)/(18)和原句均保留，Q310仍待核。'
s=p.read_text(encoding='utf-8-sig');old=B/rel
if not old.exists():old.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,old)
anchor='上式 $\\chi^{\\mathrm{SFG}}(\\omega_{\\mathrm{IR}’})$'
# Use the actual source sentence rather than normalizing its prime or frequency labels.
anchor=next(line for line in s.splitlines() if line.startswith('上式 $') and '应根据展宽情况' in line)
if note not in s:
 s=s.replace(anchor,note+'\n\n'+anchor,1);p.write_text(s,encoding='utf-8')
assert s.replace(note+'\n\n','',1)==old.read_text(encoding='utf-8-sig')
(O/'B674新增阅读提示.json').write_text(json.dumps({rel:note},ensure_ascii=False,indent=2),encoding='utf-8')
def append(rel,text):
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if text.splitlines()[0] not in s:
  b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
  p.write_text(s.rstrip()+'\n\n'+text+'\n',encoding='utf-8')
append('翻译管理/疑难与勘误.md','''## B674：Q310模平方与相干探测条件复核（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q310 | 8.1 p8—9，式(17)/(18)及定义段 | 原式(17)普通平方已确认；复响应不能一般地产生非负强度。不同输出频率与同一输出模式内相干贡献还需探测条件 | 原文公式/条件/P2 | B674补模平方反例、有限时间窗及有限脉冲能量的条件性分析，外查第一方拍频/能量资料。作者拟用模号及具体测量条件仍不唯一，保留原式/原句，不新增Q/E。详见全书复核/B674相干积分复核.md |''')
append('翻译管理/符号与约定.md','''## B674：积分对象、谱相位与测量条件（2026-10-22）

8.1 p8分子中心频率分布的积分、p9激光谱频率的积分和同一输出模式内贡献求和不能混同。复响应的普通平方与模平方分开；相干性还须结合探测时间窗、带宽、偏振/空间模式及归一化。有限脉冲能量的时频积分等价不意味着某时刻相干场强等于总能量，不能把本批示例的傅里叶常数直接用于原书。Q310仍未决，见[本批复核](全书复核/B674相干积分复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B674相干积分复核（2026-10-22）

Q310原式(17)未标模号已核，并补复平方反例与探测条件说明；式(18)对应的观测量、谱相位及归一化仍不明确。候选模平方结构未替换原式，不新增E。作者原句、两张公式图及频率标签保持原样。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B674补充

先明确积分变量、同一输出模式的贡献及探测观测量，再讨论相干求和或强度累加。相位锁定、可观察拍频和整脉冲能量不是同一个判据，普通复平方不能充当一般强度。有限窗与傅里叶常数仅作带明示条件的说明，不静默改原式。Q310仍待核，见[B674复核](B674相干积分复核.md)。''')
p=R/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8-sig');head='## 当前有效状态：B674模平方与相干积分条件复核（2026-10-22）'
if head not in s:
 s=s.replace('## 当前有效状态：B673','## 历史状态：B673',1)
 s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+head+'''\n\n核对8.1 p8/p9及式(17)/(18)，确认普通平方与复模平方的记号问题，补积分对象、谱相位、探测时间窗/带宽及能量归一化边界；第一方拍频与时频能量资料已登记。Q310的作者修法和具体测量条件仍未决，原式/原句/图片不改，无新增Q/E。

正文与管理记录同步，合稿更新为B674。详见全书复核/B674相干积分复核.md及本批验收。下一批B675核查Q311：附录A的参数符号、主值/分布意义与极限下标；Q304保持已撤回状态。\n\n''',1);p.write_text(s,encoding='utf-8')
sources=[{'label':'RP Photonics：拍频','author':'Dr. Rüdiger Paschotta','url':'https://www.rp-photonics.com/beat_note.html','read_scope':'作者正文的空间/偏振重叠与探测带宽条件；不以AI辅助FAQ作独立依据','supports':'可观察差频交叉项有探测条件，不等于仅由相位锁定决定'}, {'label':'Ansys Optics：Parseval能量核查示例','author':'Ansys Optics官方技术文档','url':'https://optics.ansys.com/hc/en-us/articles/360034394274-Using-Parseval-s-theorem-to-check-for-energy-conservation-between-the-time-and-frequency-domain','read_scope':'有限脉冲的时频能量等价及软件归一化限制；未运行附带FDTD文件','supports':'区分时域总能量、谱能量积分和软件所用常数'}]
(O/'B674来源记录.json').write_text(json.dumps({'access_date':'2026-10-22','sources':sources,'scope':'外部技术条件作参照，时间窗推导为译者独立条件性分析'},ensure_ascii=False,indent=2),encoding='utf-8')
# Algebraic counterexample and independently integrated finite observation windows.
counter={'f':1,'chi':'-i','ordinary_square':-1,'absolute_square':1}
cases=[];n=6000
for T in [.01,.3,1,2]:
 h=T/n;u=math.pi*T;weight=math.sin(u)/u
 for phase in [0,math.pi/2,math.pi]:
  a2=cmath.exp(1j*phase)
  actual=h/(3*T)*sum((1 if j in [0,n] else 4 if j%2 else 2)*abs(1+a2*cmath.exp(-2j*math.pi*(-T/2+j*h)))**2 for j in range(n+1))
  exact=2+2*math.cos(phase)*weight
  assert abs(actual-exact)<1e-9 and actual>=-1e-12
  cases.append({'T':T,'relative_phase':phase,'window_cross_weight':weight,'integrated_signal':actual,'analytic_signal':exact})
phase_average=sum(abs(1+cmath.exp(2j*math.pi*k/64))**2 for k in range(64))/64
assert abs(phase_average-2)<1e-12
size=16;energies=[];peaks=[]
for chirp in [0,.3]:
 spectrum=[math.exp(-((k-size/2)/3)**2)*cmath.exp(1j*chirp*(k-size/2)**2) for k in range(size)]
 time=[sum(spectrum[k]*cmath.exp(2j*math.pi*k*j/size) for k in range(size))/size for j in range(size)]
 e_time=sum(abs(z)**2 for z in time);e_spectrum=sum(abs(z)**2 for z in spectrum)/size
 assert abs(e_time-e_spectrum)<1e-12
 energies.append(e_time);peaks.append(max(abs(z)**2 for z in time))
assert abs(energies[0]-energies[1])<1e-12 and abs(peaks[0]-peaks[1])>1e-4
data={'complex_square_counterexample':counter,'finite_window_cases':cases,'max_window_error':max(abs(x['integrated_signal']-x['analytic_signal']) for x in cases),'phase_averaged_signal':phase_average,'DFT_size':size,'DFT_time_energies':energies,'DFT_peak_intensities':peaks,'original_body_preserved_after_removing_note':True,'source_corrections':0,'scope':'有限窗与离散Parseval示例；非仪器模型或一般相干理论认证'}
(O/'B674代数检查.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');print('B674 updated; 12 finite-window cases, phase average and DFT energy checks passed; original body preserved.')

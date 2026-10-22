from pathlib import Path
import json,shutil,math,cmath,random
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B670修改前'
rel='中文版本/第八章 拟合/8.1 和频光谱的线形.md';p=R/rel
note='> **分项核查补充（B670，Q308）：** 四处原印均已核对。按式(9)/(11)的实系数模型展开，交叉项只含cosφ，不再乘φ；模号内βᵥ²会产生后续未列的四次项。孤立高斯平方项的半高宽为原高斯的1/√2，而非√2；总谱形含背景或干涉时不能照搬这一项宽度。“实部变号”也不足以指定相移90°，需明确频率区间。本批给出条件性推导与反例，候选未替换原文，Q308继续保留；Q304误报仍维持撤回。'
s=p.read_text(encoding='utf-8-sig');oldpath=B/rel
if not oldpath.exists():oldpath.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,oldpath)
anchor='<!-- B643：PDF p7,8；均匀与非均匀展宽并存。 -->'
if note not in s:
 assert anchor in s;s=s.replace(anchor,note+'\n\n'+anchor,1);p.write_text(s,encoding='utf-8')
assert s.replace(note+'\n\n','',1)==oldpath.read_text(encoding='utf-8-sig')
(O/'B670新增阅读提示.json').write_text(json.dumps({rel:note},ensure_ascii=False,indent=2),encoding='utf-8')
def append(rel,text):
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if text.splitlines()[0] not in s:
  b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
  p.write_text(s.rstrip()+'\n\n'+text+'\n',encoding='utf-8')
append('翻译管理/疑难与勘误.md','''## B670：Q308分项原印与条件复核（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q308 | 8.1 p4式(2)、p6末段、p7式(8)—(12)及文字 | 额外φ、模号内βv²、√2宽度及固定90°四个子项原印均确认 | 原文公式/条件/P2 | B670从实系数响应重展，并按原半高宽定义核算；相位反例表明频率区间不可省略。数学差异已查明，作者修正意图仍未确认，保留原式/原句及候选，不关闭Q308、不新增E。详见全书复核/B670非均匀展宽复核.md |''')
append('翻译管理/符号与约定.md','''## B670：纯非均匀模型的实系数与相位条件（2026-10-22）

Q308原印复核：实高斯响应取模平方的交叉项含cosφ，不能再有额外φ；模号内βv与βv²产生不同阶数。平方项半高宽按Δ1/2/√2理解，但保留原文相反文字和候选，不自动改原式。总谱宽与单项宽度分开。实部变号不能单独决定相移90°；以正γ的1/(x+iγ)为例，两对称频点±a的连续相移为2 arctan(a/γ)。示例辐角与原拟合背景相位分别理解，不统一改号。见[本批复核](全书复核/B670非均匀展宽复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B670纯非均匀展宽复核（2026-10-22）

Q308的四个子项已逐处核对原印并补条件性推导：式(10)额外φ、式(12)首行βv²、平方项宽度及固定90°相位文字。原式和原句均保留，候选未采用，不新增E或宣称作者已确认。Q304是另一条已撤回的译者误报，状态不受本批影响。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B670补充

纯非均匀展宽的实高斯模型和复洛伦兹模型分开核算；实系数展开不能套用到任意复系数。高斯平方项半高宽、背景交叉项宽度和总谱形的宽度分别说明。相位变化必须指定区间及分支，不以实部变号独断90°。Q308保留未决，Q304维持撤回。详见[B670复核](B670非均匀展宽复核.md)。''')
p=R/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8-sig');head='## 当前有效状态：B670纯非均匀展宽展开与相位复核（2026-10-22）'
if head not in s:
 s=s.replace('## 当前有效状态：B669','## 历史状态：B669',1)
 s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+head+'''\n\n核对8.1 p4/p6/p7三页，Q308额外φ、首行βv²、平方项宽度及固定90°相位四项原印已确认。条件性展开、半高宽及相位反例已整理；原作者修正意图仍未确认，Q308继续保留，不改原式/原句，无新增Q/E。Q304保持已撤回状态。

正文增加分项提示，问题/符号/勘误维护与跨章规则同步，合稿更新为B670。详见全书复核/B670非均匀展宽复核.md及本批验收。下一批B671核查Q307的多谱带均匀展宽式(6)—(7)，从完整复响应重展，查N、π及背景交叉项范围。\n\n''',1);p.write_text(s,encoding='utf-8')
rng=random.Random(670);errors=[]
for count in [1,3]:
 for _ in range(20):
  pop=rng.uniform(.5,4);sigma=rng.uniform(.4,2);back=rng.uniform(.2,1);phi=rng.uniform(-math.pi,math.pi);w=rng.uniform(-2,2)
  coeffs=[pop*rng.uniform(-2,2)*math.exp(-(w-rng.uniform(-1,1))**2/(2*sigma*sigma))/(math.sqrt(2*math.pi)*sigma) for i in range(count)]
  direct=abs(back*cmath.exp(1j*phi)+sum(coeffs))**2
  expanded=back**2+sum(x*x for x in coeffs)+2*back*math.cos(phi)*sum(coeffs)+2*sum(coeffs[i]*coeffs[j] for i in range(count) for j in range(i+1,count))
  errors.append(abs(direct-expanded));assert errors[-1]<1e-10
wrong_phi={'B':.5,'a':.7,'phi':0,'true_intensity':(.5+.7)**2,'intensity_with_extra_phi':.5**2+.7**2}
assert abs(wrong_phi['true_intensity']-wrong_phi['intensity_with_extra_phi'])>.1
wrong_beta={'B':.5,'beta':.7,'N_G':1,'true_intensity':(.5+.7)**2,'intensity_with_beta_squared':(.5+.7**2)**2}
assert abs(wrong_beta['true_intensity']-wrong_beta['intensity_with_beta_squared'])>.1
phase=[]
for ratio in [.5,1,2]:
 arg1=cmath.phase(1/complex(-ratio,1));arg2=cmath.phase(1/complex(ratio,1));delta=arg2-arg1
 assert abs(delta-2*math.atan(ratio))<1e-12
 phase.append({'a/gamma':ratio,'phase_change_degrees':math.degrees(delta)})
width=[]
for sigma in [.3,1,2]:
 h=math.sqrt(2*math.log(2))*sigma;hs=math.sqrt(math.log(2))*sigma
 assert abs(math.exp(-hs*hs/(sigma*sigma))-.5)<1e-12
 width.append({'sigma':sigma,'Gaussian_HWHM':h,'squared_HWHM':hs,'ratio':hs/h})
(O/'B670代数检查.json').write_text(json.dumps({'amplitude_cases':40,'max_expansion_error':max(errors),'extra_phi_counterexample':wrong_phi,'beta_squared_counterexample':wrong_beta,'width_cases':width,'phase_cases':phase,'original_body_preserved_after_removing_note':True,'source_corrections':0,'scope':'实系数模型及指定相位区间的检查，不是作者意图或全模型认证'},ensure_ascii=False,indent=2),encoding='utf-8')
print('B670 updated; 40 expansions, two counterexamples, width/phase cases passed; original body preserved.')

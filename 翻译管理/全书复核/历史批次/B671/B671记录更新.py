from pathlib import Path
import json,shutil,math,cmath,random
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B671修改前'
rel='中文版本/第八章 拟合/8.1 和频光谱的线形.md';p=R/rel
note='> **因子范围核查补充（B671，Q307）：** 已从式(6)的完整复响应重展。背景及单分子系数固定时，背景—共振交叉项应随N/π变化，原式(7)按印刷括号却使其随N³/π³变化；单带纯共振和带间交叉项仍需各自的N²/π²因子，不能全部删除。单带退化亦显示原式(7)一般不能返回式(5)。候选四项重展已另记；原括号、系数及原图均保留，Q307尚未采用修正。'
s=p.read_text(encoding='utf-8-sig');old=B/rel
if not old.exists():old.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,old)
anchor='式(7)表明，除非共振干涉外'
if note not in s:
 assert anchor in s;s=s.replace(anchor,note+'\n\n'+anchor,1);p.write_text(s,encoding='utf-8')
assert s.replace(note+'\n\n','',1)==old.read_text(encoding='utf-8-sig')
(O/'B671新增阅读提示.json').write_text(json.dumps({rel:note},ensure_ascii=False,indent=2),encoding='utf-8')
def append(rel,text):
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if text.splitlines()[0] not in s:
  b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
  p.write_text(s.rstrip()+'\n\n'+text+'\n',encoding='utf-8')
append('翻译管理/疑难与勘误.md','''## B671：Q307完整响应与括号因子复核（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q307 | 8.1 p5式(4)、p6式(5)—(7) | 背景交叉项被外部N²/π²再乘，成为N³/π³；纯共振与带间项的平方因子须独立保留 | 原文公式/P2 | B671原页和裁图已核，按完整复响应给出条件性四项重展，单带退化/背景为零/N倍增检查通过。数学不一致位置已查明，作者括号或系数修法仍未确认，原式保留，无新增Q/E。见全书复核/B671多谱带复核.md |''')
append('翻译管理/符号与约定.md','''## B671：多谱带均匀展宽的N/π因子（2026-10-22）

8.1式(6)各共振振幅含N/π。在实系数、固定背景与单分子系数的条件下，背景交叉项随N/π、纯共振与带间项随N²/π²；原式(7)将前者放入额外平方因子括号。候选重展四项分别保留，不用共同强度比例常数掩盖不同项的相对系数，也不删除所有平方因子。Q307原式尚未修正，见[本批复核](全书复核/B671多谱带复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B671多谱带均匀展宽复核（2026-10-22）

Q307原括号及因子已核，背景交叉项按原印受到额外N²/π²倍乘。条件性重展及单带等检验已记录，尚未确认作者拟移动括号或改变哪一系数；原式/原图保留，不新增E。这里的数学分析不作为已采用原文勘误。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B671补充

多谱带复响应先完整取模平方，再分背景、单带、背景交叉、带间交叉四组；不同项的N与π因子不得因排版括号或省略强度比例号而混为共同常数。实系数形式不代替一般复系数共轭形式，单带与无背景特例分别检验。Q307仍保留未决，见[B671复核](B671多谱带复核.md)。''')
p=R/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8-sig');head='## 当前有效状态：B671多谱带均匀展宽因子复核（2026-10-22）'
if head not in s:
 s=s.replace('## 当前有效状态：B670','## 历史状态：B670',1)
 s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+head+'''\n\n核对8.1 p5/p6两页及式(4)—(7)，确认Q307背景交叉项受到额外N²/π²倍乘；从式(6)完整复响应分列四项，核验单带退化、无背景特例与N倍增关系。数学差异已查明，作者修法仍未确认，Q307保留，原式/原图未改，无新增Q/E。

正文、问题表、符号、勘误维护与跨章规则同步；合稿按B671更新。详见全书复核/B671多谱带复核.md及本批验收。下一批B672核查Q306：峰位偏移方向及背景/相位条件，限定式(5)模型，不静默改写原文判断。\n\n''',1);p.write_text(s,encoding='utf-8')
def terms(pop,back,beta,x,gamma,phi):
 c=pop/math.pi;d=[a*a+b*b for a,b in zip(x,gamma)]
 single=c*c*sum(b*b/den for b,den in zip(beta,d))
 cross=2*back*c*sum(b*(a*math.cos(phi)-g*math.sin(phi))/den for b,a,g,den in zip(beta,x,gamma,d))
 pair=2*c*c*sum(beta[i]*beta[j]*(x[i]*x[j]+gamma[i]*gamma[j])/(d[i]*d[j]) for i in range(len(beta)) for j in range(i+1,len(beta)))
 direct=abs(back*cmath.exp(1j*phi)+c*sum(b/complex(a,g) for b,a,g in zip(beta,x,gamma)))**2
 return direct,back*back+single+cross+pair,single,cross,pair
rng=random.Random(671);errors=[];zero_errors=[];single_errors=[]
for count in [1,3]:
 for _ in range(20):
  pop=rng.uniform(.4,6);back=rng.uniform(.3,2);beta=[rng.uniform(-2,2) for i in range(count)];x=[rng.uniform(-3,3) for i in range(count)];gamma=[rng.uniform(.2,2) for i in range(count)];phi=rng.uniform(-math.pi,math.pi)
  direct,expanded,single,cross,pair=terms(pop,back,beta,x,gamma,phi)
  errors.append(abs(direct-expanded));assert errors[-1]<1e-10
  z=terms(pop,0,beta,x,gamma,phi);zero_errors.append(abs(z[0]-z[1]));assert zero_errors[-1]<1e-10
  if count==1:
   c=pop/math.pi;d=x[0]**2+gamma[0]**2
   eq5=back**2+c*c*beta[0]**2/d+2*back*c*beta[0]*(x[0]*math.cos(phi)-gamma[0]*math.sin(phi))/d
   single_errors.append(abs(direct-eq5));assert single_errors[-1]<1e-10
example=terms(2,1,[1],[1],[1],0);c=2/math.pi
printed=1+example[2]+c*c*example[3]+example[4]
assert abs(printed-example[0])>.1
first=terms(2,1,[.7,-1.2],[1,2],[.5,.8],.4);second=terms(4,1,[.7,-1.2],[1,2],[.5,.8],.4)
assert abs(second[3]/first[3]-2)<1e-12
assert abs(second[2]/first[2]-4)<1e-12 and abs(second[4]/first[4]-4)<1e-12
data={'random_response_cases':40,'max_expansion_error':max(errors),'zero_background_cases':40,'max_zero_background_error':max(zero_errors),'single_band_cases':20,'max_single_band_error':max(single_errors),'counterexample':{'N':2,'B':1,'beta':1,'x':1,'gamma':1,'phi':0,'from_response':example[0],'printed_eq7_brackets':printed},'N_doubling_ratios':{'background_cross':second[3]/first[3],'printed_background_cross':8,'single_resonance':second[2]/first[2],'interband':second[4]/first[4]},'original_body_preserved_after_removing_note':True,'source_corrections':0,'scope':'固定实系数下的复响应代数检验，非作者修法确认'}
(O/'B671代数检查.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');print('B671 updated; expansion/limits/scaling passed; original body preserved.')

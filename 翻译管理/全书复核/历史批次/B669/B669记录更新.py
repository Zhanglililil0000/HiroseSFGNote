from pathlib import Path
import json,shutil,math
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B669修改前'
rel='中文版本/第八章 拟合/8.1 和频光谱的线形.md';p=R/rel
notes=[
'> **定义核查补充（B669，Q303）：** 已对照p4式(1)与p5式(4)。若γ为正，两式分别是实平方分母函数和复数一次分母响应核；前者在全实频率轴上的面积为1/γ，而非1。面积归一为1的实洛伦兹函数还需分子含γ；它对应本处复核虚部的负值，不等同于完整复核或其模平方。此处保留作者的同名记号及原式，未补γ或更改响应系数。',
'> **零阻尼极限补充（B669，Q309）：** 按原分母的+iγ并令γ从正侧趋零，面积归一的实洛伦兹核趋于δ；完整的1/[π(x+iγ)]复响应核则还含PV(1/x)/π及−iδ部分，不能整体换成实δ函数。卷积后主值项一般仍存在。原作者是否另取吸收部分或采用额外相位、色散近似，尚未说明；原句与原式保留，相关极限需按分布理解。'
]
s=p.read_text(encoding='utf-8-sig');oldpath=B/rel
if not oldpath.exists():oldpath.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,oldpath)
for note,anchor in zip(notes,['**非均匀展宽函数**',r'$\chi^R$ 中出现积分']):
 if note not in s:
  assert anchor in s;s=s.replace(anchor,note+'\n\n'+anchor,1)
p.write_text(s,encoding='utf-8')
assert s.replace(notes[0]+'\n\n','',1).replace(notes[1]+'\n\n','',1)==oldpath.read_text(encoding='utf-8-sig')
(O/'B669新增阅读提示.json').write_text(json.dumps({rel:'\n\n'.join(notes)},ensure_ascii=False,indent=2),encoding='utf-8')
def append(rel,text):
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if text.splitlines()[0] not in s:
  b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
  p.write_text(s.rstrip()+'\n\n'+text+'\n',encoding='utf-8')
append('翻译管理/疑难与勘误.md','''## B669：Q303/Q309实线形与复响应核复核（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q303 | 8.1 p4式(1)、p5式(4)、p8式(13) | 同名gL分别用于实平方分母和复一次分母；γ>0时式(1)全实轴面积为1/γ | 定义/归一化/P2 | B669四页原文及数学形式已核，不是转录漏γ。补就地定义提示；作者统一定义或补因子意图未确认，保留未决，不改原式 |
| Q309 | 8.1 p8式(13)、p10附录A | 完整复核γ→0+为主值部分与−iδ组合，不等同于单独实δ；卷积后主值一般仍在 | 极限条件/P2 | B669补分布与方向条件，数学推导及平滑权函数数值示例见全书复核/B669洛伦兹复核.md。原句具体意图仍未决，无新增Q/E或原式修正 |''')
append('翻译管理/符号与约定.md','''## B669：gL的不同对象（2026-10-22）

8.1 p4式(1)为1/[π(x²+γ²)]；p5式(4)、p8式(13)的复核为1/[π(x+iγ)]，不能同名互换。γ>0时，前者全实轴面积为1/γ；面积归一的实核γ/[π(x²+γ²)]是该复核虚部的负值。γ→0+的完整复核仍含主值/π与−iδ部分，和实归一核的δ极限区分。正负号只按这组分母分析，不自动决定光学吸收的正负。Q303/Q309仍未决，详见[本批复核](全书复核/B669洛伦兹复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B669洛伦兹核与极限复核（2026-10-22）

Q303/Q309的不同gL形式及零阻尼文字已对照原页，并补归一化、复核主值与δ部分的条件说明。仍不能唯一确定作者是否意在补因子、取虚部或另设近似，故不更改原式、不新增E。数学说明不等于已确认原文修正。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B669补充

区分实洛伦兹函数、面积归一核、复响应核、虚部和模平方；同名gL不能直接替换。零阻尼极限注明趋近侧及分布意义；完整复核的主值项不因实核存在δ极限而自动消失。原式、相位和β定义仍按各处保留。详见[B669复核](B669洛伦兹复核.md)。''')
p=R/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8-sig');head='## 当前有效状态：B669洛伦兹线形与零阻尼极限复核（2026-10-22）'
if head not in s:
 s=s.replace('## 当前有效状态：B668','## 历史状态：B668',1)
 s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+head+'''\n\n核对8.1 p4/p5/p8/p10四页及相关式，确认实线形、归一实核、复响应核的区别，补全正γ、全实轴面积与分布极限的应用边界。Q303/Q309原印和数学区别已查明，作者补因子/取虚部/近似意图仍未决；未改原式，无新增Q/E。

正文两处补说明，问题/符号/勘误维护与跨章规则同步，合稿按B669更新。详见全书复核/B669洛伦兹复核.md及本批验收。下一批B670核对Q308的纯非均匀展宽强度展开、宽度与相位文字，保持Q304已撤回状态，不将独立疑点合并。\n\n''',1);p.write_text(s,encoding='utf-8')
# Smooth rapidly decreasing weights distinguish the real principal-value part from delta.
cases=[];n=24000;h=12/n
def integ(f):return h/3*sum((1 if i in [0,n] else 4 if i%2 else 2)*f(i*h) for i in range(n+1))
for gamma in [.5,.1,.02]:
 E=math.exp(gamma*gamma)*math.erfc(gamma)
 even=-2/math.pi*integ(lambda x:gamma*math.exp(-x*x)/(x*x+gamma*gamma))
 odd=2/math.pi*integ(lambda x:x*x*math.exp(-x*x)/(x*x+gamma*gamma))
 assert abs(even+E)<1e-9 and abs(odd-(1/math.sqrt(math.pi)-gamma*E))<1e-9
 cases.append({'gamma':gamma,'even_weight_imaginary_part':even,'even_exact':-E,'even_limit':-1,'odd_weight_real_part':odd,'odd_exact':1/math.sqrt(math.pi)-gamma*E,'odd_limit':1/math.sqrt(math.pi)})
assert all(abs(cases[i+1]['even_weight_imaginary_part']+1)<abs(cases[i]['even_weight_imaginary_part']+1) for i in [0,1])
assert all(abs(cases[i+1]['odd_weight_real_part']-1/math.sqrt(math.pi))<abs(cases[i]['odd_weight_real_part']-1/math.sqrt(math.pi)) for i in [0,1])
(O/'B669代数检查.json').write_text(json.dumps({'weights':['exp(-x²)','x exp(-x²)'],'cases':cases,'original_body_preserved_after_removing_new_notes':True,'source_corrections':0,'scope':'平滑衰减权函数的核积分数值示例，不是分布收敛的一般证明'},ensure_ascii=False,indent=2),encoding='utf-8')
print('B669 updated; original body preserved; smooth-weight integrals checked.')

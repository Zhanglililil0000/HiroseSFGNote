from pathlib import Path
import json,cmath,random,re
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核'
def append(rel,text):
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if text.splitlines()[0] not in s:p.write_text(s.rstrip()+'\n\n'+text+'\n',encoding='utf-8')
append('翻译管理/疑难与勘误.md','''## B666：Q010/Q028跨章证据补充（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q010 | 1.1、1.3；7.1 p3式(4)/(13a)；8.1 p3 | 7.1明确面量厚度积分和δ函数表示，8.1明确N为总数；尚无这些节之间的完整归一化换算 | 跨章定义/P2 | B666已目视补核6页，局部定义已查明；跨节定量转换仍未决。三节补阅读提示，不改N、不补面积/膜厚/ε₀，无原式修正。见全书复核/B666归一化与相位复核.md |
| Q028 | 1.3式(1)；7.1式(13b)/(14)—(16) | 两节时间指数相反；7.1的出射方向及复q衰减分支与各自标签须成组理解 | 跨章约定/P2 | B666已查明差异并作条件性代数检查，不是原式错误；μ、式(2)/(3)/(10)及表面场相容性仍未决。不改单个i或批量共轭原式，无新增勘误 |''')
append('翻译管理/符号与约定.md','''## B666：全书跨章定义补充（2026-10-22）

7.1 p3式(4)、(13a)已明确本节厚度积分面量及δ函数表示，不能再将Q010概括成全书均未定义面量；未决的是1.1/1.3/7.1/8.1之间的定量归一化换算。8.1 p3明确N为分子总数，不改为面密度。

1.3式(1)为正时间指数，7.1式(13b)/(16)为负时间指数；两节复振幅、复波矢和响应参数不可只改单个i后混用。7.1的反射kz为−q1、透射为+q2；1.3上标+/−为侧别，不能当作相同标签。原文公式未改。详细证据及条件性代数说明见[本批复核](全书复核/B666归一化与相位复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B666跨章约定复核（2026-10-22）

Q010：7.1已给本节面极化量定义，8.1明确N为总数；跨节归一化转换仍未决。Q028：1.3与7.1的相反时间因子及出射侧别已核对，属于约定差异，不登记为原文错误。三节新增译者阅读提示，未改原式，无新增E条目。既有疑点、候选及用户确认的Q013处理均保留。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B666补充

7.1式(4)/(13a)局部面量定义已查明；Q010未决范围限定为跨节定量转换。8.1 p3的N为总分子数。1.3正时间指数与7.1负时间指数的差异已经原页核对；相位转换须成组处理，不将两节的单独辐射因子或吸收虚部直接比较。详见[B666复核](B666归一化与相位复核.md)。''')
p=R/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8-sig')
heading='## 当前有效状态：B666跨章归一化与相位约定复核（2026-10-22）'
if heading not in s:
 s=s.replace('## 当前有效状态：B665','## 历史状态：B665',1)
 note=heading+'''\n\n已补核1.3 p1/p5、7.1 p2—4及8.1 p3共6张原页。7.1的厚度积分面量及δ函数定义、8.1的N为总数均有直接证据；1.3正时间指数与7.1负时间指数的差异已明确。Q010跨节定量归一化、Q028其余公式相容性仍未决；没有新增原式修正或Q/E编号。

三节增加跨章阅读提示，问题/符号/勘误维护说明同步。详见翻译管理/全书复核/B666归一化与相位复核.md。合稿已按B666更新。原式保真及数学/资源检查见本批验收；既有B665全书浏览结果仅作原布局基线，本批只抽查新增提示。

下一批B667：优先回查Q302，比较8.1/8.2分子数估算、Γ因子和宽度定义；按完整公式组分批，不直接统一写法。\n\n'''
 s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+note,1);p.write_text(s,encoding='utf-8')
# Check that the only changes to the three body files are the recorded inserted notes.
notes=json.loads((O/'B666新增阅读提示.json').read_text(encoding='utf-8')); unchanged={}
for rel,note in notes.items():
 old=(O/'B666修改前'/rel).read_text(encoding='utf-8-sig');new=(R/rel).read_text(encoding='utf-8-sig')
 unchanged[rel]=new.replace('\n'+note+'\n','',1)==old
 assert unchanged[rel],rel
rng=random.Random(666);errors=[]
for _ in range(50):
 A=complex(rng.random(),rng.random());k=complex(rng.random(),rng.random());w,t,z=[rng.random() for _ in range(3)]
 a=A*cmath.exp(1j*(w*t-k*z));b=A.conjugate()*cmath.exp(1j*(k.conjugate()*z-w*t))
 errors.append(abs((a+a.conjugate())-(b+b.conjugate())))
data={'samples':50,'max_real_field_difference':max(errors),'body_unchanged_after_removing_added_notes':unchanged,'new_source_corrections':0,'scope':'条件性代数检验，非原文全部公式认证'}
(O/'B666代数检查.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(data,ensure_ascii=False))

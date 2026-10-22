from pathlib import Path
import json,shutil,math
def integrate(f,tol=1e-10):
 def recurse(a,b,fa,fm,fb,whole,tol,depth):
  mid=(a+b)/2;l=(a+mid)/2;r=(mid+b)/2;fl,fr=f(l),f(r)
  left=(mid-a)*(fa+4*fl+fm)/6;right=(b-mid)*(fm+4*fr+fb)/6
  delta=left+right-whole
  if abs(delta)<=15*tol:return left+right+delta/15
  if depth==0:raise ArithmeticError('quadrature did not converge')
  return recurse(a,mid,fa,fl,fm,left,tol/2,depth-1)+recurse(mid,b,fm,fr,fb,right,tol/2,depth-1)
 fa,fm,fb=f(0),f(.5),f(1)
 return recurse(0,1,fa,fm,fb,(fa+4*fm+fb)/6,tol,30)
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B667修改前'
notes={
'中文版本/第八章 拟合/8.1 和频光谱的线形.md':'> **跨节核查提示（B667，Q302/Q316）：** 已对照8.2 p2：两节都写χᵥ＝Nβᵥ，但8.1积分分子不含Γᵥ，8.2含Γᵥ。βᵥ不变本身不能保证βᵥ/Γᵥ不变；线宽变化时，不应将两节的分子数指标直接混用。对原积分的0至无穷界限，一般结果还含中心频率与宽度之比的反正切项，原π/2因子所需条件未说明。这里保留原式与原结论，未采用候选修正。',
'中文版本/第八章 拟合/8.2 和频光谱分析便览.md':'> **跨节核查提示（B667，Q316/Q302）：** 已对照8.1 p2，确认两节积分分子相差Γᵥ。对孤立、无背景且光学比例因子固定的均匀洛伦兹强度峰，恢复共振系数模平方需将峰高乘以半高半宽的平方；宽度不变时乘除只差常因子，不能据此推广到变线宽比较。原文“除以”仍保留。0至无穷的移位积分也不能一般地只用π/2；原作者意图尚未确认。'
}
anchors={list(notes)[0]:'**从积分强度估算分子数有风险。**',list(notes)[1]:'**认为积分强度正比于分子数是错误的。**'}
for rel,note in notes.items():
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if note in s:continue
 b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 assert anchors[rel] in s
 p.write_text(s.replace(anchors[rel],note+'\n\n'+anchors[rel],1),encoding='utf-8')
(O/'B667新增阅读提示.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2),encoding='utf-8')
def append(rel,text):
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if text.splitlines()[0] not in s:p.write_text(s.rstrip()+'\n\n'+text+'\n',encoding='utf-8')
append('翻译管理/疑难与勘误.md','''## B667：Q302/Q316原页及条件性代数复核（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q302 | 8.1 p1—3、8.2 p1—2 | 原积分分子确实相差Γ；两节χv=Nβv相同，βv恒定不保证βv/Γv恒定；0至无穷积分一般含反正切项 | 原文条件/跨节/P2 | B667原页及裁图复核完成，精确积分和单峰条件分析见全书复核/B667分子数复核.md。原作者积分变量/范围及Γ恒定假设意图仍未确认，保留原式及候选；未关闭、无新增E |
| Q316 | 8.2 p2 | 峰强除以宽度平方原印已核；孤立无背景固定比例因子时恢复χ模平方应乘宽度平方，正频移位积分的π/2亦需条件 | 原文条件/P2 | B667已补就地提示，宽度不变时常因子不能证明变线宽比较成立。候选未采用，原式/原文均保留；与Q302关联，不作静默统一 |''')
append('翻译管理/符号与约定.md','''## B667：分子数估算与宽度边界（2026-10-22）

8.1 p1—3、8.2 p1—2复核：两节都用χv=Nβv，但原积分分子分别为βv和βvΓv。8.2明示Γ为半高半宽，8.1后续γv、Δ1/2按局部定义保留。孤立无背景、固定光学比例因子的均匀洛伦兹峰才可将峰高乘Γ²恢复共振系数模平方；全宽2Γ只改常因子，不反转乘除。0至无穷移位积分的反正切项不能省略而不说明条件。Q302/Q316未关闭，详见[本批复核](全书复核/B667分子数复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B667分子数估算复核（2026-10-22）

Q302/Q316：8.1、8.2的积分分子差异及8.2“除以”原印已核。条件性代数显示其积分范围、Γ变化和峰强关系需要额外说明；尚不能确定作者意图，不改原式、不新增已采用E编号。两节均补译者提示，候选和既有原文保留。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B667补充

8.1/8.2的分子数指标不能在变线宽时直接互换；总数N与面密度不自动转换。半高半宽Γ、强度峰高、拟合分子系数和强度面积分别表述，简化比例关系须写明无背景、孤立单峰、均匀洛伦兹及光学比例因子固定等条件。详见[B667复核](B667分子数复核.md)，Q302/Q316原式未改。''')
p=R/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8-sig');heading='## 当前有效状态：B667分子数估算与线宽复核（2026-10-22）'
if heading not in s:
 s=s.replace('## 当前有效状态：B666','## 历史状态：B666',1)
 s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+heading+'''\n\n完成8.1 p1—3、8.2 p1—2共5张原页及两张积分裁图对照。确认两节积分分子相差Γ、χv=Nβv定义相同；条件性代数明确移位正频积分、峰高与宽度的适用关系。Q302/Q316保留未决，不新增原式修正或Q/E编号。

两节补就地提示，问题/符号/跨章约定/勘误维护说明同步，合稿按B667更新。细节及验证见全书复核/B667分子数复核.md；去掉新增提示后原有正文须与本批修改前逐字一致。

下一批B668：回查Q304高斯归一化及σ定义，按8.1参数、平方、卷积/附录的完整链处理，不直接替换原式图片。\n\n''',1);p.write_text(s,encoding='utf-8')
preserved={rel:(R/rel).read_text(encoding='utf-8-sig').replace(note+'\n\n','',1)==(B/rel).read_text(encoding='utf-8-sig') for rel,note in notes.items()}
assert all(preserved.values())
results=[]
for gamma in [0.5,2.0]:
 for ratio in [0,1,5,10]:
  center=ratio*gamma;beta=1.3;A=math.pi/2+math.atan(ratio)
  for numerator,expected in [(beta,beta/gamma*A),(beta*gamma,beta*A)]:
   # w=u/(1-u); the transformed rational integrand has a finite endpoint at u=1.
   actual=integrate(lambda u:numerator/((u-center*(1-u))**2+gamma**2*(1-u)**2))
   assert abs(actual-expected)<1e-8
   results.append({'Gamma':gamma,'omega_v/Gamma':ratio,'numerator':numerator,'exact':expected,'quadrature':actual,'absolute_error':abs(actual-expected)})
peak=[{'Gamma':g,'chi':12,'H':144/g**2,'H_times_Gamma_squared':144,'sqrt_H_times_Gamma':12} for g in [1,2,3]]
(O/'B667代数检查.json').write_text(json.dumps({'integrals':results,'max_error':max(x['absolute_error'] for x in results),'peak_examples':peak,'original_body_preserved':preserved,'source_corrections':0,'scope':'限定条件下的代数/数值检查，非作者意图认证'},ensure_ascii=False,indent=2),encoding='utf-8')
print('B667 notes/records updated; 16 quadratures passed; original body preserved.')

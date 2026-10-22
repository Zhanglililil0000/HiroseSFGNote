from pathlib import Path
import json,shutil,math,cmath,random
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B672修改前'
rel='中文版本/第八章 拟合/8.1 和频光谱的线形.md';p=R/rel
note='> **峰位条件核查补充（B672，Q306）：** 按式(5)的实系数、正宽度、固定背景单共振模型，偏移方向还取决于共振系数与cosφ；正背景本身不能保证向低波数偏移。正背景、正共振系数且φ=0时可向高侧偏移，改变相位或系数符号则可向低侧。cosφ=0时还须区分中心峰、凹陷或特殊抵消；没有色散形不等于没有均匀宽度。本批条件性导数与反例另记，原文判断保留，未采用修正。'
s=p.read_text(encoding='utf-8-sig');old=B/rel
if not old.exists():old.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,old)
anchor='有多个振动谱带时，式(4)、(5)改写为'
if note not in s:
 assert anchor in s;s=s.replace(anchor,note+'\n\n'+anchor,1);p.write_text(s,encoding='utf-8')
assert s.replace(note+'\n\n','',1)==old.read_text(encoding='utf-8-sig')
(O/'B672新增阅读提示.json').write_text(json.dumps({rel:note},ensure_ascii=False,indent=2),encoding='utf-8')
def append(rel,text):
 p=R/rel;s=p.read_text(encoding='utf-8-sig')
 if text.splitlines()[0] not in s:
  b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
  p.write_text(s.rstrip()+'\n\n'+text+'\n',encoding='utf-8')
append('翻译管理/疑难与勘误.md','''## B672：Q306峰位与背景相位条件复核（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q306 | 8.1 p5式(4)、p6式(5)及相邻文字 | 正背景不足以决定峰向低侧；按原式模型，非零奇项时最大值偏移符号由背景×共振系数×cosφ决定 | 原文条件/P2 | B672原页复查、导数与反例完成；cosφ=0还可能为中心峰/凹陷/平坦。作者额外符号假设仍未确定，原句/原式保留，无新增Q/E。见全书复核/B672峰位复核.md |''')
append('翻译管理/符号与约定.md','''## B672：单共振峰位与相位（2026-10-22）

8.1式(5)的条件性分析限定实A=Nβv/π、实B=χNR、γ>0及固定背景。写I=B²+(C+Dx)/(x²+γ²)，C=A²−2BAγsinφ、D=2BAcosφ。D非零时最大值偏移符号与D相同；D为零需另分中心峰、凹陷或平坦，不能把凹陷称最大峰。正背景不单独固定方向，结论不推广到邻峰和频率依赖光学因子。Q306仍未决，见[本批复核](全书复核/B672峰位复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B672峰位条件复核（2026-10-22）

Q306原文关于正背景与低波数偏移的判断已回查；指定模型的导数和反例表明还需共振系数及相位条件。原作者额外假设尚不唯一，不将原句改成相反的普遍判断，不新增E。正文补适用边界，原句、公式和图片保留。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B672补充

峰位偏移按完整响应、系数符号及相位分析，不只看背景正负。中心峰、中心凹陷、远离中心的极值和有限扫描窗分别理解；“无色散形”不等同于“无均匀宽度”。单共振固定背景模型不能成为复杂谱形的通用判据。Q306保留未决，见[B672复核](B672峰位复核.md)。''')
p=R/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8-sig');head='## 当前有效状态：B672峰位偏移与相位条件复核（2026-10-22）'
if head not in s:
 s=s.replace('## 当前有效状态：B671','## 历史状态：B671',1)
 s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+head+'''\n\n复查8.1 p5/p6两页，按式(5)分析Q306。正背景不独自决定峰位偏移方向；导数、极值及相位/共振系数反例已整理，cosφ=0时分别讨论峰、凹陷与平坦。数学条件已查明，作者附加假设仍未确认；原句/原式不改，无新增Q/E。

正文提示、问题表、符号、勘误维护与跨章规则同步，合稿按B672更新。详见全书复核/B672峰位复核.md及本批验收。下一批B673核查Q305：运动窄化段的NMR高速旋转毛细管例子，核对原句并查原始研究/权威技术资料，区分分子随机运动与机械旋转。\n\n''',1);p.write_text(s,encoding='utf-8')
def coefficients(A,B,g,p):return A*A-2*B*A*g*math.sin(p),2*B*A*math.cos(p)
def intensity(x,A,B,g,p):return abs(B*cmath.exp(1j*p)+A/complex(x,g))**2
def derivative(x,C,D,g):return (D*g*g-2*C*x-D*x*x)/(x*x+g*g)**2
rng=random.Random(672);value_errors=[];derivative_errors=[];roots=[]
for _ in range(40):
 A=rng.choice([-1,1])*rng.uniform(.4,2);back=rng.uniform(.2,1.5);g=rng.uniform(.5,2);phase=rng.uniform(-math.pi,math.pi)
 C,D=coefficients(A,back,g,phase)
 for ratio in [-2,-.3,0,.8,2]:
  x=ratio*g;val=intensity(x,A,back,g,phase);value_errors.append(abs(val-(back*back+(C+D*x)/(x*x+g*g))))
  h=1e-5*g;fd=(intensity(x+h,A,back,g,phase)-intensity(x-h,A,back,g,phase))/(2*h)
  derivative_errors.append(abs(fd-derivative(x,C,D,g)));assert derivative_errors[-1]<2e-6
 if abs(D)>1e-8:
  S=math.hypot(C,D*g);root=(D*g*g/(C+S)) if C>=0 else (-C+S)/D
  assert root*D>0 and abs(D*g*g-2*C*root-D*root*root)<1e-7*max(1,abs(D*root*root))
  h=1e-3*max(g,abs(root));peak=intensity(root,A,back,g,phase)
  assert peak>=intensity(root-h,A,back,g,phase)-1e-10 and peak>=intensity(root+h,A,back,g,phase)-1e-10
  roots.append(root)
assert max(value_errors)<1e-10
examples=[]
for A,phase,label in [(1,0,'high_side'),(1,math.pi,'low_side'),(-1,0,'low_side'),(1,-math.pi/2,'central_peak'),(1,math.pi/2,'central_dip'),(2,math.pi/2,'flat')]:
 C,D=coefficients(A,1,1,phase)
 if abs(D)<1e-12:
  D=0;assert (C>0 and label=='central_peak') or (C<0 and label=='central_dip') or (abs(C)<1e-12 and label=='flat');root=None
 else:
  root=(-C+math.hypot(C,D))/D;assert (root>0)==(label=='high_side')
 examples.append({'A':A,'B':1,'gamma':1,'phi':phase,'C':C,'D':D,'classification':label,'maximum_offset':root})
data={'random_parameter_sets':40,'intensity_and_derivative_points':200,'max_intensity_error':max(value_errors),'max_finite_difference_error':max(derivative_errors),'stationary_maxima_checked':len(roots),'examples':examples,'original_body_preserved_after_removing_note':True,'source_corrections':0,'scope':'单共振、固定背景、实系数与正γ条件下的代数/数值核验'}
(O/'B672代数检查.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');print('B672 updated; 200 value/derivative points, extrema and six examples checked; original body preserved.')

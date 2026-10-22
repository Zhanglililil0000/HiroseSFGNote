from pathlib import Path
import re,json,csv,io,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];M=ROOT/'翻译管理';D=ROOT/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.4 *.md'))
old=P.read_text(encoding='utf-8');assert not (OUT/'B124-修订前.md').exists();(OUT/'B124-修订前.md').write_text(old,encoding='utf-8')
def tex(s):return s.replace('§',chr(92))
def math(s):return '$$\n'+tex(s)+'\n$$\n'
def al(lines):return '§begin{aligned}\n'+('§§\n'.join(lines))+'\n§end{aligned}'
mother=next(D.glob('2.3 *.md')).read_text(encoding='utf-8');blocks=re.findall(r'\$\$[\s\S]*?\$\$',mother)
def named(label):
 block=next(x for x in blocks if tex('§tag{'+label+'}') in x)
 return block.replace(tex('§tag{'+label+'}'),'')+'\n'
pref='''# 2.4 薄膜产生的和频（表达式）

> 原作：广濑千秋（沿用项目作者归属；独立底本首页未列署名）  
> 中文翻译：章力
>
> **译校状态（2026-10-19）：** B124完成“准备工作”（独立PDF p1—2，至“L系数、电场振幅”标题前）的本轮译校；全部相应定义和无编号公式已核。L系数及后续各源点和频表达式仍为旧译待校订，不以可显示或同源内容视为已核。
>
> **底本：** `日语原版/Chapter2/chap2-4.pdf`，10页。本独立文件为《多层膜的和频过程（SFG）：表达式》，按其原有顺序与符号另行核验；文件名暂保留历史译名。

> **阅读导引（译者编写）：** 本节先备列界面、方向及菲涅尔因子，随后列出L系数、各源点电场和反射/透射和频表达式，最后列体相结果。当前仅“准备工作”已核，后续概括暂按标题与结构定位。

## 准备工作

原点取在光线入射点；光束有宽度时取其中央。$z$ 轴沿介质1指向介质2的法线；$x$ 轴沿光在界面上的传播方向，与波矢在界面上的投影一致。

| 记号 | 定义 |
|---|---|
| $1/m$ 界面 | 介质1与薄膜的界面 |
| $m/2$ 界面 | 介质1与薄膜的界面（底本原称） |
| $n_1,n_2,n_m$ | 介质1、介质2与膜 $m$ 的折射率 |
| $k_1,k_2,k_m$ | 介质1、介质2与膜 $m$ 中的波矢 |
'''+tex('''| $§theta_1,§theta_2,§theta_m$ | 各介质中光路与法线的夹角 |
| $t_{1m}$ | 从介质1侧透入薄膜侧的电场透射系数 |
| $t_{m1}$ | 从薄膜侧透入介质1侧的电场透射系数 |
| $r_{1m}$ | 从介质1侧入射、在 $1/m$ 界面反射的电场反射系数 |
| $r_{m1}$ | 从薄膜侧入射、在 $m/1$ 界面反射的电场反射系数 |
| $t_{m2}$ | 从薄膜侧透入介质2侧的电场透射系数 |
| $t_{2m}$ | 从介质2侧透入薄膜侧的电场透射系数 |
| $r_{m2}$ | 从薄膜侧入射、在 $m/2$ 界面反射的电场反射系数 |
| $r_{2m}$ | 从介质2侧入射、在 $1/m$ 界面反射的电场反射系数（底本原称） |
| 上行（−）光 | 从 $m/2$ 界面朝 $m/1$ 界面传播，与反射光一样沿 $-z$ 方向传播 |
| 下行（+）光 | 从 $m/1$ 界面朝 $m/2$ 界面传播，与入射光一样沿 $+z$ 方向传播 |

> **译校注（Q077，保留原文）：** PDF p1将 $m/2$ 界面解释为“介质1与膜的界面”，与其余界面记法不一致；候选为“膜与介质2的界面”，暂未采用。$r_{2m}$ 的反射界面又写成 $1/m$，与第2.2节Q039同类，候选为 $2/m$，同样只列注释。不能把旧译已经改成候选的表述当作原文。

### 反射系数

''')
u=pref+named('A.7')+'\n### 透射系数\n\n'+named('A.8')+'\n反向入射时，有：\n\n'+named('A.9a')+'\n'+named('A.9b')
u+='\n以界面内向法线为 $z$ 轴，以s偏振电场方向为 $y$ 轴，取光沿界面的传播方向为 $x$ 正向，可得电场的轴向分量：\n\n'
field=next(x for x in blocks if 'E_{x,i}&=' in x);u+=field+'\n\n'
u+='由上式，得到下列振幅反射系数与“振幅等效系数”的表达式：\n\n'
for label in ['A.10a','A.10b','A.11a','A.11b']:u+=named(label)+'\n'
u+=tex('''> **译校注（Q078及关联第2.2节Q072）：** PDF p2原文写「振幅等価係数」，这里照译“振幅等效系数”；按所列 $t$ 系数，候选为“振幅透射系数”，未改原词。轴分量首行原为 $E^s_{ri}$；反向透射一行先写 $t^x_{21}$，随后却写 $t^y_{12},t^z_{12}$。这些记号依本独立原页保留，不按对称性统一。

对于两侧界面，有：

''')
lines=[]
for ij,ji in [('1m','m1'),('2m','m2')]:
 lines.append('r_{'+ij+',x}&=-r_{'+ji+',x}=r_{'+ij+',p},§quad r_{'+ij+',y}=-r_{'+ji+',y}=r_{'+ij+',s},§quad r_{'+ij+',z}=-r_{'+ji+',z}=-r_{'+ij+',p}')
u+=math(al(lines))+'\n'
for ij,a,b in [('1m','m','1'),('m1','1','m'),('2m','m','2'),('m2','2','m')]:
 u+=math(al(['t_{'+ij+',x}&=(§cos§theta_'+a+'/§cos§theta_'+b+')t_{'+ij+',p},§quad t_{'+ij+',y}=t_{'+ij+',s},','t_{'+ij+',z}&=(§sin§theta_'+a+'/§sin§theta_'+b+')t_{'+ij+',p}.']))+'\n'
u+=math(al(['t_{1m,§alpha}t_{m1,§alpha}&=1+r_{1m,§alpha}r_{m1,§alpha}=1-r_{1m,§alpha}^2,','t_{2m,§alpha}t_{m2,§alpha}&=1+r_{2m,§alpha}r_{m2,§alpha}=1-r_{2m,§alpha}^2,§qquad(§alpha=x,y,z).']))
u+='\n上式满足以下关系；首行表示电场的边界条件：\n\n'+named('A.12')
u+=tex('''
光强正比于 $E^2n§cos§theta$，因此 $r_{12}^2n_1§cos§theta_1+t_{12}^2n_2§cos§theta_2=n_1§cos§theta_1$，即光强守恒。

> **译校注（关联第2.2节Q053，适用范围）：** 上述普通平方与守恒式照录底本。若振幅为复数，需核对模平方及吸收条件，不将这一简式无条件用于吸收介质；这里未据候选重写原关系。末行的 $§alpha$ 只是 $x,y,z$ 的坐标分量枚举下标，不是分子极化率。

''')
i=old.index('## L系数与电场振幅');new=u+old[i:]
assert new[new.index('## L系数与电场振幅'):]==old[i:]
assert not any(ord(c)<32 and c not in '\r\n' for c in new)
assert not re.findall(r'\\tag\{',u),'This source preparation has no original equation numbers'
P.write_text(new,encoding='utf-8');(OUT/'B124-本批译文.md').write_text(u,encoding='utf-8')
sha=hashlib.sha256((ROOT/'日语原版/Chapter2/chap2-4.pdf').read_bytes()).hexdigest();assert sha=='3f6eeee4f3418c4a89181b0c0142b95aee1adda31fb6e94a7c100fd000f58be2'
(OUT/'B124-覆盖.json').write_text(json.dumps({'batch':'B124','pages':[1,2],'end':'L系数、电场振幅标题前','source_sha256':sha,'numbered':[],'units':['坐标与界面/系数/方向定义','s/p反射、透射及反向入射关系','三行轴分量关系','r12/r21/t12/t21轴分量四组关系','两界面r轴分量两行、t轴分量四组','两组t乘积恒等式','电场边界/反射透射乘积/强度守恒'],'unreviewed_remainder_unchanged':True,'issues':['Q077','Q078','关联Q039/Q053/Q072'],'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'B124.md').write_text('''# B124：2.4准备工作

2026-10-19，独立底本chap2-4.pdf，PDF p1—2至L系数标题前。SHA256：3f6eeee4f3418c4a89181b0c0142b95aee1adda31fb6e94a7c100fd000f58be2。

逐项对原页与文字层校核：全部定义、s/p反射与透射、反向关系、轴向场三行、四组r/t轴系数、两界面r/t轴系数、乘积恒等式、电场边界和强度守恒。无原式编号，不借用2.3的A.7等标签制造编号。

2.3相应数学仅作录入候选，已对独立p1/p2复核后移除不属于本文件的标签。新增界面轴分量关系另逐项转写。Q077保留m/2定义为介质1/膜及r2m的1/m；Q078保留“振幅等価係数”、E_ri与t21/t12差异。旧译改成候选、公式连写丢上下标等问题作为译文修复，不混为原文勘误。没有采用原文修正。

数学验证仅覆盖已校订批次；其后的旧译仍含待整理由来已久的LaTex写法，不能把范围扩成整文件。L系数及后续内容与批前逐字一致。没有新术语命名决定，未决公式不进确定语料。
''',encoding='utf-8')
(OUT/'结构与复用核验表.md').write_text('''# 2.4结构及复用核验入口

独立底本10页，为表达式汇编；不能把2.2的推导正文或2.3附录直接复制为本文件已核。以下后续范围仅依据文本缓存的标题/分页定位，不是已核结论。

| 单元 | PDF范围 | 状态/复用边界 |
|---|---|---|
| 准备工作 | p1—2至L标题前 | B124逐项原页核验完成；与2.3线性光学重合但无相应编号；新增界面轴系数单独转写 |
| L系数与各源点电场 | p2—4 | 待核；优先按两出射方向和完整分量组分批，跨页z分量不截断 |
| 前界面外侧及完整表面膜 | p4—5 | 待核；反射/透射分别核其层标、相位和分母 |
| 前界面内侧 | p5—6 | 待核 |
| 背界面外侧及背面极化膜 | p6—7 | 待核 |
| 背界面内侧 | p7—8 | 待核 |
| 体相反射与透射 | p8—10 | 待核；长式分组、跨页与公共因子逐项保留 |

首次核验已确认的原文差异：本文件m/2定义误指介质1，r2m仍写1/m，“振幅等価係数”保留；Q077/Q078只注不改。不能继承2.3某些相同公式的编号，也不预先声称后续长式完全相同。
''',encoding='utf-8')
# Validate/render reviewed fragments only, while the unreviewed legacy tail remains.
r=(OUT.parent/'2.3/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/2.3','校订记录/2.4').replace("startsWith('2.3 ')","startsWith('2.4 ')")
r=r.replace("const s=fs.readFileSync(source,'utf8');", "const s=fs.readdirSync(out).filter(f=>/^B[0-9]{3}-本批译文[.]md$/.test(f)).sort().map(f=>fs.readFileSync(path.join(out,f),'utf8')).join('\\n\\n');")
(OUT/'检查排版.cjs').write_text(r,encoding='utf-8');(OUT/'渲染检查.json').write_text(json.dumps({'results':[]}),encoding='utf-8')
def append(p,t):p.write_text(p.read_text(encoding='utf-8').rstrip()+'\n\n'+t+'\n',encoding='utf-8')
append(M/'疑难与勘误.md','''## 2.4准备工作（B124）

| 问题 | 独立PDF位置 | 原文及状态 |
|---|---|---|
| Q077 | p1，界面及r2m定义 | m/2定义为介质1与膜，候选膜/介质2未采用；r2m反射界面为1/m，关联Q039，候选2/m仅注 |
| Q078 | p2，轴分量式引言 | 原写振幅等価係数，照译等效，候选透射未采用；E_ri及反向t21/t12混用关联Q072 |

普通平方/守恒式适用范围关联Q053。无原文采用修正，没有新增E-2.4条目。后续L系数仍待独立核验。
''')
(OUT/'局部约定卡.md').write_text('# 2.4局部约定卡\n\nB124：z朝介质2、x沿界面波矢投影；上行−朝介质1、下行+朝介质2。r/t为电场振幅比，s/p偏振系数与x/y/z轴分量不同。原界面定义及反向下标异常按当地原值保留。乘积恒等式的α只枚举坐标，不是分子极化率。后续SF/vis/ir与公共因子待B125逐组核验。\n',encoding='utf-8')
def tsv(p,key,val,change):
 rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0]);found=0
 for row in rows:
  if row[key]==val:row.update(change);found+=1
 assert found
 buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_text(buf.getvalue(),encoding='utf-8-sig')
tsv(M/'章节清单.tsv','编号','2.4',{'状态':'B124完成准备工作；L系数及后续旧译待校订','映射核验':'独立底本10页；p1—2至L系数标题前已核，后续仅结构定位','公式图表范围':'已核准备工作全部无编号系数/边界/强度关系，不继承2.3编号','导读状态':'Preface及第二章导航更新B124范围'})
tsv(M/'全书调查/分批建议.tsv','节号','2.4',{'执行状态':'2026-10-19 B124完成p1—2准备工作至L标题前；下一批B125从L定义及1/m侧完整分量组起，后续待核'})
p=M/'当前进度与续接.md';s=p.read_text(encoding='utf-8');entry='''## 当前有效状态：2.4已开始，B124完成准备工作（2026-10-19）

独立底本chap2-4.pdf共10页，已核p1—2至“L系数、电场振幅”标题前：全部定义及菲涅尔/轴分量/边界/强度关系。无原式编号，不移植2.3标签；Q077/Q078保留原值，候选只注。后续L系数及各源点表达式仍为旧译，批前内容逐字保留。

下一批B125：从p2“L系数、电场振幅”起，核定义、公共因子、偏振/坐标分量区别及1/m侧两方向全部L系数（z分量跨p2—3，必须完整衔接）。之后再按m/2和膜内各分量组推进。数学检查暂仅限已校订批次，不能声称整文件语法/内容完成。历史脚本不要重跑覆盖正文。

''';p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
p=ROOT/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('（旧译待校订）：查阅相关表达式。','（B124已核准备工作，后续待校订）：独立表达式汇编；先定义界面和振幅系数，再列L系数与各源点的反射/透射和频场，体相长式仍待逐组核验。');p.write_text(s,encoding='utf-8')
p=D/'阅读导航.md';s=p.read_text(encoding='utf-8').replace('2.4以后仍待校订。','2.4已核准备工作，其后及2.5以后仍待校订。');s+='\n## 2.4 薄膜产生的和频（表达式）\n\n[进入正文](2.4%20多层膜的和频过程（SFG）：表达式.md)。独立底本10页，B124已核p1—2准备工作至L标题前。\n\n1. 准备工作（已核）：坐标、界面和方向定义；s/p与轴向振幅系数、反向关系、边界条件及强度守恒。Q077/Q078原值保留。\n2. L系数及各源点电场（p2—4，待核）：按两界面、膜内与两方向组织。\n3. 各界面源的反射/透射和频场（p4—8，待核）：前后界面内外及完整极化膜。\n4. 体相反射/透射表达式（p8—10，待核）：长式与跨页分组须逐项核验。\n\n后三项概括目前只据标题与文本结构定位，后续核验后更新。与2.2/2.3有重合，但不预先认定公式同一，也不借用其编号。\n';p.write_text(s,encoding='utf-8')
print('B124 preparation applied; legacy L-and-later tail unchanged; scope=reviewed fragments only')

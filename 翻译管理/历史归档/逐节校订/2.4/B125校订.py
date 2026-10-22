from pathlib import Path
import csv,io,json,hashlib
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
D=ROOT/'中文版本/第二章 薄膜产生的SFG'
p=next(D.glob('2.4 *.md'));old=p.read_text(encoding='utf-8')
backup=OUT/'B125-修订前.md'
assert not backup.exists(), 'Do not rerun a completed mutation'
start=old.index('## L系数与电场振幅')
end=old.index('对于媒质2与多层薄膜 m 之间的极化片')
text='''## L系数与电场振幅

$$
E_{§mathrm{SF},§alpha}=§sum_§beta L_{§alpha§beta}P_§beta^{§mathrm{SF}}.
$$

此处省略公共因子 $4§pi i§omega_{§mathrm{SF}}/c$（当用波矢代替折射率时，省略的因子为 $4§pi i§omega_{§mathrm{SF}}^2/c^2$）。

**L系数的记号**：当极化片 $m'$ 夹在 $i$ 层与 $j$ 层之间时，$L_{i/j,s(p),§alpha}$ 表示极化强度的 $§alpha$ 分量（$§alpha=x,y,z$）与其所产生光的 $s$ 偏振或 $p$ 偏振分量之间的系数。注意，此处的输出是 $s/p$ 偏振分量，而非电场的 $x,y,z$ 分量。原文以上标 $-$、$+$ 区分“上行（−）光”和“上行（+）光”。

> **原文疑点（Q041，2.4 PDF p2）**：两个方向在底本中均称「上向き」。这里保留原称及上下标；“+”光应称“下行”的候选解释暂只列在本注中，未作为原文修正采用。以下六式按底本分别列出，不以方向名称改变其符号。

### 介质1与膜之间的极化片

对于介质1与层叠膜 $m$ 之间的极化片 $m'$ 所产生的光，有：

$$
L^-_{1/m,p,x}=§frac{§cos§theta_{m,§mathrm{SF}}}
{n_{1,§mathrm{SF}}§cos§theta_{m,§mathrm{SF}}+n_{m,§mathrm{SF}}§cos§theta_{1,§mathrm{SF}}}.
$$

$$
L^-_{1/m,s,y}=§frac{1}
{n_{1,§mathrm{SF}}§cos§theta_{1,§mathrm{SF}}+n_{m,§mathrm{SF}}§cos§theta_{m,§mathrm{SF}}}.
$$

$$
§begin{aligned}
L^-_{1/m,p,z}
&=§frac{(n_{m,§mathrm{SF}}/n_{m',§mathrm{SF}})§sin§theta_{m',§mathrm{SF}}}
{n_{1,§mathrm{SF}}§cos§theta_{m,§mathrm{SF}}+n_{m,§mathrm{SF}}§cos§theta_{1,§mathrm{SF}}} \\
&=§frac{(n_{m,§mathrm{SF}}/n_{m',§mathrm{SF}})^2§sin§theta_{m,§mathrm{SF}}}
{n_{1,§mathrm{SF}}§cos§theta_{m,§mathrm{SF}}+n_{m,§mathrm{SF}}§cos§theta_{1,§mathrm{SF}}}.
§end{aligned}
$$

$$
L^+_{1/m,p,x}=§frac{§cos§theta_{1,§mathrm{SF}}}
{n_{1,§mathrm{SF}}§cos§theta_{m,§mathrm{SF}}+n_{m,§mathrm{SF}}§cos§theta_{1,§mathrm{SF}}}.
$$

$$
L^+_{1/m,s,y}=§frac{1}
{n_{1,§mathrm{SF}}§cos§theta_{1,§mathrm{SF}}+n_{m,§mathrm{SF}}§cos§theta_{m,§mathrm{SF}}}.
$$

$$
§begin{aligned}
L^+_{1/m,p,z}
&=-§frac{(n_{1,§mathrm{SF}}/n_{m',§mathrm{SF}})§sin§theta_{m',§mathrm{SF}}}
{n_{1,§mathrm{SF}}§cos§theta_{m,§mathrm{SF}}+n_{m,§mathrm{SF}}§cos§theta_{1,§mathrm{SF}}} \\
&=-§frac{(n_{1,§mathrm{SF}}/n_{m',§mathrm{SF}})^2§sin§theta_{1,§mathrm{SF}}}
{n_{1,§mathrm{SF}}§cos§theta_{m,§mathrm{SF}}+n_{m,§mathrm{SF}}§cos§theta_{1,§mathrm{SF}}}.
§end{aligned}
$$

'''.replace('§',chr(92))
# Replace the two explicit row separator lines without relying on shell escaping.
text=text.replace('} '+chr(92)+'\n','} '+chr(92)*2+'\n')
backup.write_text(old,encoding='utf-8')
new=old[:start]+text+old[end:]
assert new[:start]==old[:start] and new[new.index('对于媒质2与多层薄膜 m 之间的极化片'):]==old[end:]
assert not any(ord(c)<32 and c not in '\n\r\t' for c in text)
p.write_text(new,encoding='utf-8');(OUT/'B125-本批译文.md').write_text(text,encoding='utf-8')
sha=hashlib.sha256((ROOT/'日语原版/Chapter2/chap2-4.pdf').read_bytes()).hexdigest()
assert sha=='3f6eeee4f3418c4a89181b0c0142b95aee1adda31fb6e94a7c100fd000f58be2'
coverage={'batch':'B125','date':'2026-10-19','source_pages':[2,3],'source_sha256':sha,'units':['响应映射式','公共因子及波矢形式','L记号与s/p输出区别','方向原称及Q041注','1/m六系数及两个z分量等价式'],'numbered_equations':0,'coefficient_count':6,'z_equalities_complete':True,'unreviewed_tail_unchanged':True,'previous_prefix_unchanged':True,'source_corrections_adopted':False}
(OUT/'B125-覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'B125.md').write_text('''# B125：L系数定义及前界面六系数

2026-10-19。独立底本chap2-4.pdf，PDF p2“L係数、電場振幅”至p3介质2标题前，逐页对照原图和文字层。

覆盖响应映射、两种公共因子、L系数的输入坐标/输出偏振区别，以及1/m两方向共六系数。两个z分量均保留折射率一次比与平方比的完整等价链，负号仅在正向z式；逐项核角下标和两种分母的余弦配对。无原式编号，不借用2.2编号。

原文两个方向均称上向，旧译无注改下向已恢复为原称并就地说明，关联Q041。没有采用原文修正，勘误附件不增列未采用候选。所有数学为可编辑LaTeX，下一组介质2系数及以后旧译逐字保持；此前准备工作也未变。

下一批B126：介质2/膜与膜内L系数组，止于各源点电场振幅前；不能直接套前界面层标。
''',encoding='utf-8')
progress=ROOT/'翻译管理/当前进度与续接.md';s=progress.read_text(encoding='utf-8');pos=s.index('\n')+1
s=s[:pos]+'''\n## 当前有效状态：B125完成2.4前界面L系数（2026-10-19）

B124准备工作之后，已核PDF p2—3的L定义、公共因子与1/m两方向六系数，两个z分量跨页等价链均完整。方向双称上行保留并注Q041；没有采用原文修正。后续介质2/膜、膜内L及各源点电场仍待核，后段旧译逐字保持。

下一批B126：核介质2/膜六系数与膜内三条关系，止于各源点振幅前。数学检查限B124—B125已校订片段，不能称2.4全节完成。以下为历史记录。

'''+s[pos:];progress.write_text(s,encoding='utf-8')
for rel,key in [('翻译管理/章节清单.tsv','编号'),('翻译管理/全书调查/分批建议.tsv','节号')]:
 f=ROOT/rel
 with f.open(encoding='utf-8-sig',newline='') as h:r=csv.DictReader(h,delimiter='\t');fields=r.fieldnames;rows=list(r)
 hits=0
 for row in rows:
  if row[key]!='2.4':continue
  hits+=1
  if key=='编号':
   row['状态']='本轮B124—B125已核准备工作和1/m的L定义及六系数；后续待校订'
   row['映射核验']='独立PDF 10页；p1—3至介质2的L组前已逐项核验'
   row['公式图表范围']='准备工作及L映射/公共因子/1/m六系数已转写，无原式编号；后续待核'
   row['导读状态']='Preface与导航已更新B125范围'
  else:row['执行状态']='B124—B125已核准备工作、L定义及1/m六系数；B126续介质2/膜和膜内L；其后未核'
 assert hits>0
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(rows)
f=ROOT/'Preface序言.md';s=f.read_text(encoding='utf-8');assert '（B124已核准备工作，后续待校订）' in s;s=s.replace('（B124已核准备工作，后续待校订）','（B124—B125已核准备工作及前界面L系数，后续待校订）');f.write_text(s,encoding='utf-8')
f=D/'阅读导航.md';s=f.read_text(encoding='utf-8');s=s.replace('2.4已核准备工作，其后','2.4已核准备工作及前界面L系数，其后').replace('B124已核p1—2准备工作至L标题前。','B124—B125已核p1—3准备工作、L定义与前界面六系数。').replace('2. L系数及各源点电场（p2—4，待核）：按两界面、膜内与两方向组织。','2. L系数及各源点电场（p2—4，部分已核）：B125已核定义、公共因子与1/m两方向六系数；介质2/膜、膜内及各源点电场待核。');f.write_text(s,encoding='utf-8')
for rel,addition in [
 ('翻译管理/校订记录/2.4/结构与复用核验表.md','\nB125更新：p2—3的L定义、公共因子及1/m两方向六系数已对独立原页核验；不移植母本公式编号。介质2/膜、膜内及各源点电场仍待核。\n'),
 ('翻译管理/校订记录/2.4/局部约定卡.md','\n## B125：L记号\n\nL的末指标是源极化x/y/z分量，输出标记为s/p偏振；勿把两者同称坐标分量。省略因子为4πiω_SF/c，使用波矢时为4πiω_SF²/c²。原文两个方向均称上向，关联Q041；不以该名称改变系数正负号。仅1/m组已核。\n'),
 ('翻译管理/疑难与勘误.md','\nQ041续记（B125，2026-10-19）：2.4 PDF p2的L定义也把−、+都称「上向き」。正文恢复原称并注明下行候选；六式符号按原页保留，无新增已采用原文修正。\n')]:
 f=ROOT/rel;f.write_text(f.read_text(encoding='utf-8')+addition,encoding='utf-8')
print(json.dumps(coverage,ensure_ascii=False))

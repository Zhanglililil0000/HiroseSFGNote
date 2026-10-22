from pathlib import Path
import json,csv,hashlib
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.5 *.md'));old=P.read_text(encoding='utf-8');key='所谓"反射光"';end=old.index(key)
assert not (O/'B134-修订前.md').exists()
(O/'B134-修订前.md').write_text(old,encoding='utf-8')
prefix=old[:end]
a=prefix.index('## 1. 引言');prefix=prefix[a:]
b=prefix.index('## 2. 预备')
intro='''## 1. 引言

对于存在和频活性薄膜的体系，本文分别建立分析下列五类和频光信号强度行为所需的表达式：（a）在薄膜与介质1的界面上、介质一侧产生的和频光；（b）在同一界面的膜一侧产生的和频光；（c）在薄膜与介质2的界面上、介质一侧产生的和频光；（d）在同一界面的膜一侧产生的和频光；（e）在膜内部产生的和频光。具体而言，将膜厚纳入所观测的和频电场表达式，使两束激发光与和频光各自的干涉效应得以明确呈现。

'''
prefix=intro+prefix[b:];prefix=prefix.replace('## 2. 预备','## 2. 准备工作').replace('（原文如此，应为薄膜与介质 2 的界面）','（底本原称；见下方疑点说明）')
prefix=prefix.replace('- z 轴：','- $z$ 轴：').replace('- x 轴：','- $x$ 轴：').replace('（沿波矢 k 在界面上的投影方向）','（沿波矢 $k$ 在界面上的投影方向）').replace('向上(-)光','上行（−）光').replace('向下(+)光','下行（+）光').replace('向 -z 方向','沿 $-z$ 方向').replace('向 +z 方向','沿 $+z$ 方向')
prefix+='''> **原文疑点（Q077／Q039关联，2.5 PDF p1）**：底本将 $m/2$ 界面也定义为“介质1与膜之间的界面”，且将 $r_{2m}$ 的反射位置写成 $1/m$。此处均保留原称；候选分别为“膜与介质2之间的界面”和 $2/m$，尚未采用修正。

'''
head='''# 2.5 薄膜产生的和频（要点）

> 原作：广濑千秋（沿用项目作者归属；独立底本首页未列署名）  
> 中文翻译：章力
>
> **译校状态（2026-10-20）：** B134完成PDF p1的引言、体系设定及全部定义，止于“反射光”说明前；其后仍为旧译待校订。
>
> **底本：** `日语原版/Chapter2/chap2-5.pdf`，20页。按独立底本原顺序和编号推进，不据2.2—2.4的完成状态认定本节已核。

> **阅读导引（译者编写）：** 引言区分五类源点，准备工作建立界面与方向约定。后续含激发场、和频极化、反射/透射场与附录；这些后续概括目前仅据标题和结构定位，尚未逐项校订。

'''
new=head+prefix+old[end:];assert new[new.index(key):]==old[end:];P.write_text(new,encoding='utf-8');(O/'B134-本批译文.md').write_text(head+prefix,encoding='utf-8')
sha=hashlib.sha256((R/'日语原版/Chapter2/chap2-5.pdf').read_bytes()).hexdigest();assert sha=='6dff0000c7d1d7672b10e8a43cf9d683ac5fb7602b50aba9d875dba4992c4094'
structure='''# 2.5结构与复用核验入口

独立底本20页，SHA256：6dff0000c7d1d7672b10e8a43cf9d683ac5fb7602b50aba9d875dba4992c4094。以下范围据文字层分页和标题定位；只有B134所列首页定义已逐项对原图，其余不是已核结论。

| 单元 | PDF范围 | 状态及执行边界 |
|---|---|---|
| 引言、体系与定义 | p1 | B134完成；五类源点、膜厚、坐标、界面、八个r/t系数、两方向及附录指引 |
| 多重反射与透射场 | p1—2 | 待核；下一批B135从反射光说明起，完整核式2.1与2.3，止于4.1标题前 |
| 4.1激发电场 | p2—4 | 待核；界面各侧与膜内A/B源点；跨页完整分组 |
| 4.2和频极化 | p4—7 | 待核；各源点与膜内极化，边界须执行前复核 |
| 5.1 L系数与出射场 | p7—8 | 待核；不能据母本直接认定同一 |
| 5.2反射和频场 | p8—12 | 待核；界面内外侧、体相及净场 |
| 5.3与5.4透射和频场 | p12—15 | 待核；含跨页组，终点须原页确认 |
| 附录A线性光学关系 | p16—18 | 待核；不把原编号或疑点套用前节 |
| 附录D极化片L系数 | p18—20 | 待核；完整证明链逐组推进 |

编号从2跳到4.1等现象仅按原文记录，不自行补章或连续重排。与2.2—2.4的主题重合只是录入候选来源，各组必须重新核独立原页。首页m/2和r2m重复疑点关联Q077/Q039，候选只注。
'''
(O/'结构与复用核验表.md').write_text(structure,encoding='utf-8')
(O/'局部约定卡.md').write_text('''# 2.5局部约定卡

B134已核：膜厚h_m，z从介质1指向介质2，x沿界面波矢投影；−上行朝介质1，+下行朝介质2。r/t为电场振幅反射/透射系数；1/m、m/1、m/2按当地原文。m/2定义及r2m反射界面疑点只注。引言五类源点保持分开，不与微观分子响应系数混淆。后续相位、时间因子、L、χ和单位约定待逐组核验。
''',encoding='utf-8')
f=R/'翻译管理/当前进度与续接.md';s=f.read_text(encoding='utf-8');i=s.index('\n')+1;s=s[:i]+'''\n## 当前有效状态：2.5已开始，B134完成引言及定义（2026-10-20）

独立底本20页，已建立结构/复用入口；本批只完成p1引言、体系设定、全部定义与附录A指引，止于“反射光”说明前。首页m/2及r2m疑点关联Q077/Q039，候选只注，无采用原文修正。后段与批前逐字一致。

下一批B135：从p1“反射光”说明开始，完整核跨页反射推导2.1及透射2.3，止于p2的4.1标题前；注意求和首项与闭式相位、n与n_m区分、原编号跳号，不能把前节规范化公式移植为原文。数学检查只覆盖本批片段，2.5其余尚待校订。以下为历史记录。

'''+s[i:];f.write_text(s,encoding='utf-8')
for rel,keycol in [('翻译管理/章节清单.tsv','编号'),('翻译管理/全书调查/分批建议.tsv','节号')]:
 f=R/rel
 with f.open(encoding='utf-8-sig',newline='') as h:d=csv.DictReader(h,delimiter='\t');fields=d.fieldnames;rows=list(d)
 hit=0
 for row in rows:
  if row[keycol]!='2.5':continue
  hit+=1
  if keycol=='编号':
   row['状态']='B134已核引言及定义；后续旧译待校订';row['映射核验']='独立20页结构定位完成；p1至反射光说明前已逐项核验';row['公式图表范围']='本批无编号式；后续公式图表待逐组登记';row['导读状态']='已更新B134范围，后续概括仅结构定位'
  else:row['执行状态']='B134已核p1引言及定义；B135续跨页2.1和2.3；其后未核'
 assert hit
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(rows)
f=R/'Preface序言.md';s=f.read_text(encoding='utf-8');lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith('- [2.5 '):lines[i]=line+'（B134已核引言及定义，后续待校订）：独立20页，涉及五类源点的激发场、和频极化与出射场；后续概括仅结构定位。'
f.write_text('\n'.join(lines)+'\n',encoding='utf-8')
f=D/'阅读导航.md';s=f.read_text(encoding='utf-8').replace('2.5以后仍待校订。','2.5已核引言及定义，其后内容及2.6以后仍待校订。');s+='''\n## 2.5 薄膜产生的和频（要点）

[进入正文](2.5%20多层膜的和频过程（SFG）：要点.md)。独立底本20页。B134已核p1引言、体系设定及全部定义；反射光说明及后续尚待校订。

引言区分两界面各自两侧与膜内部五类源点；准备工作规定膜厚、坐标、界面、振幅系数及传播方向。后续依标题包含激发场、和频极化、L系数、反射/透射场及附录A/D；具体范围见管理中的结构入口，概括不表示后续已核。首页界面定义疑点保留并加注。
''';f.write_text(s,encoding='utf-8')
f=R/'翻译管理/疑难与勘误.md';f.write_text(f.read_text(encoding='utf-8')+'\nQ077／Q039续记（B134，2026-10-20）：2.5独立PDF p1重复m/2定义为介质1/膜、r2m反射位置为1/m的表述。正文保留，候选只注；不是新增采用的原文修正。\n',encoding='utf-8')
(O/'B134.md').write_text('''# B134：2.5结构入口、引言与定义

2026-10-20。独立底本20页；p1至“反射光”说明前完成逐项图文对照。覆盖五类源点、膜厚和平行界面、原点和两坐标轴、两界面名、n/k/θ、八个r/t振幅系数、两方向及附录A指引。无原式编号。

旧译将引言的“各束光自身的干涉”表述为光束之间干涉，已恢复原意；m/2候选由“应为”的断言改成未决注，关联Q077/Q039。无原文修正采用，后段逐字保持。结构表的后续范围只据文字层定位，不作完成结论。

下一批B135完整处理p1—2反射光与透射光及式2.1/2.3，止于4.1前。
''',encoding='utf-8')
(O/'B134-覆盖.json').write_text(json.dumps({'batch':'B134','date':'2026-10-20','source_sha256':sha,'source_pages':[1],'source_total_pages':20,'numbered_equations':0,'source_image_checked':True,'unreviewed_tail_unchanged':True,'adopted_source_corrections':False},ensure_ascii=False,indent=2),encoding='utf-8')
# Reuse the rendering implementation, retaining reviewed-fragment-only scope.
c=(R/'翻译管理/校订记录/2.4/检查排版.cjs').read_text(encoding='utf-8').replace("校订记录/2.4","校订记录/2.5").replace("startsWith('2.4 ')","startsWith('2.5 ')")
(O/'检查排版.cjs').write_text(c,encoding='utf-8');(O/'渲染检查.json').write_text('{"results":[]}',encoding='utf-8')
print('B134 prepared; unreviewed tail unchanged')

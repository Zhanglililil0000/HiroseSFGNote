from pathlib import Path
import re,json,hashlib,csv,io,difflib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];M=ROOT/'翻译管理'
TARGET=next((ROOT/'中文版本/第二章 薄膜产生的SFG').glob('2.3 *.md'))
old=TARGET.read_text(encoding='utf-8');backup=OUT/'B115-修订前.md'
assert not backup.exists();backup.write_text(old,encoding='utf-8')
mother=next(TARGET.parent.glob('2.2 *.md')).read_text(encoding='utf-8')
a=mother[mother.index('## 附录A.'):mother.index('## 附录B.')]
# Reuse only the independently page-checked appendix A unit, retaining its raw
# formulas; qualify issue numbers because those belong to section 2.2.
a=a.replace('Q053','关联第2.2节Q053').replace('Q072','关联第2.2节Q072')
a=a.replace('附录B、C主要使用','本节尚待校订的附录B、C与第2.2节主要使用')
a=a.replace('p35—37','PDF p1—3')
pref='''# 薄膜产生的和频（附录）

> 原作：广濑千秋（沿用项目作者归属；本独立底本首页未列署名）  
> 中文翻译：章力
>
> **译校状态（2026-10-19）：** B115已完成引言与附录A（PDF p1—3，至附录B标题前）的本轮校订，含全部编号公式及无编号关系。附录B—D仍为旧译待校订；其公式不因语法可显示而视为已核验。
>
> **底本：** `日语原版/Chapter2/chap2-3.pdf`，12页。与第2.2节附录内容重合，但独立排版、页码及差异逐项核验，不能将2.2的完成状态直接转移。本节A.1—A.12编号仅在本节范围内使用。

## 多层膜的和频过程（SFG）：附录集

本稿将《多层膜的和频过程（SFG）》卷末的附录单独汇集成册。

> **阅读导引（译者编写）：** 附录A整理线性光学与菲涅尔因子（本轮已核）；附录B复习波动的复表示，附录C追踪传播光路及相位，附录D讨论极化薄片的L系数（后三部分目前依据结构定位，待逐段校订）。本节不是新的SFG推导正文。

'''
tail=old[old.index('## 附录B'):]
new=pref+a+'\n'+tail
TARGET.write_text(new,encoding='utf-8')
(OUT/'B115-本批译文.md').write_text(pref+a,encoding='utf-8')
labels=re.findall(r'\\tag\{([^}]+)\}',a)
assert len(labels)==16 and len(set(labels))==16,labels
source=ROOT/'日语原版/Chapter2/chap2-3.pdf';sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert sha=='63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384'
(OUT/'B115-覆盖.json').write_text(json.dumps({'batch':'B115','pages':[1,3],'end':'附录B标题前','labels':labels,'source_sha256':sha,'unreviewed':'附录B—D','source_correction_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'B115.md').write_text('''# B115：2.3引言及附录A

2026-10-19。底本chap2-3.pdf，SHA256：`63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384`。

| PDF位置 | 单元 | 核对与处理 |
|---|---|---|
| p1标题/引言 | 独立附录汇编说明 | 补入底本、完成边界与译者导读，沿用户命名使用和频过程 |
| p1，A.1—A.6b | 平面波、线性响应、复折射率与根式 | 对照本独立PDF整页图和文字层；χ明确为线性极化率，保留正时间因子及原符号 |
| p1末—p2 | 反射/折射、边界条件、A.7—A.9b | 修复旧译反射/入射振幅比的叙述方向；采用菲涅尔因子；原p偏振符号和A.8斜线括号范围不静默改写 |
| p3上半，A.10a—A.12 | 轴分量、反向系数、守恒式 | 保留E_ri及A.11b的t21/t12混用，移除旧译未经确认的下标规范化；保留无编号边界与强度关系 |

复用边界：以第2.2节附录A的已核译文为候选基础，逐项对本独立PDF p1—3视觉及文字层核验后合入，不复用2.2正文或附录B—D。16个独立编号式、三行无编号轴分量、边界与强度式均有去向。本批结束于附录B标题前，不把p3下半页视为已完成。

原式疑点关联第2.2节Q053/Q072，本节已就地说明；没有采用新原文修正，不新增E编号。旧译误译/漏注/排版修复与原文勘误分开。原A.8的无括号斜线形式按本独立图照录，不将旧译补出的分母方括号当成作者原式。

本批译文、修订前快照、覆盖清单及参考渲染分别留档；语法检查涉及全文件，内容验收只限本批。
''',encoding='utf-8')
# A structure-level map is intentionally not called a full comparison of B–D.
(OUT/'2.2与2.3复用核验表.md').write_text('''# 第2.2/2.3节附录复用核验表

第2.3节原文引言明确说明为卷末附录的单独汇编。两底本分别为47页与12页，不能按固定页差机械复制；以下范围根据两个文本缓存中的标题与原编号定位。B—D暂只作结构映射，尚未完成内容一致性结论。

| 内容 | 2.2 PDF范围 | 2.3 PDF范围 | 核验状态 |
|---|---|---|---|
| 独立汇编标题与引言 | 无相同独立引言 | p1 | B115已译 |
| 附录A：线性光学 | p35—37，至B前 | p1—3，至B前 | B115本轮逐段/逐式核验；16个编号式及无编号关系已处理 |
| 附录B：波动复习 | p37—38 | p3—4，至C前 | 仅结构对应，待B116 |
| 附录C：传播与膜内场 | p38—45 | p4—10，至D前 | 仅结构对应，图形、相位、系数及文字差异待核 |
| 附录D：极化薄片L系数 | p45—47 | p10—12 | 仅结构对应，六条推导待核 |

已见A部共性：正时间指数、χ线性响应、复折射率同符号、u2v2条件、E_ri及A.11b下标问题均仍存在。保留当地原值，疑点关联2.2的Q053/Q072，不因母本注释而擅改独立底本。旧译曾将振幅比叙述方向颠倒，已修复；该项属于译文修正而非原文勘误。

每个后续单元须另作原页视觉核验；本表不声称两PDF二进制、文字或数学完全一致。
''',encoding='utf-8')
renderer=(OUT.parent/'2.2/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/2.2','校订记录/2.3').replace("startsWith('2.2 ')","startsWith('2.3 ')")
(OUT/'检查排版.cjs').write_text(renderer,encoding='utf-8')
(OUT/'渲染检查.json').write_text(json.dumps({'results':[]}),encoding='utf-8')
def tsv(p,key,val,changes):
 rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0]);found=0
 for row in rows:
  if row[key]==val:row.update(changes);found+=1
 assert found
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_text(out.getvalue(),encoding='utf-8-sig')
tsv(M/'章节清单.tsv','编号','2.3',{'状态':'B115完成引言与附录A；B—D旧译待校订','映射核验':'独立底本12页；A部p1—3至B标题前已逐项核对；其余仅结构映射','公式图表范围':'本批16个唯一编号式A.1—A.12及无编号关系已核','导读状态':'已更新Preface与第二章导航，区分本批与待核部分'})
tsv(M/'全书调查/分批建议.tsv','节号','2.3',{'执行状态':'2026-10-19 B115完成引言与附录A（p1—3至B前）；B116从p3附录B起，B—D仍待核'})
p=M/'当前进度与续接.md';s=p.read_text(encoding='utf-8');entry='''## 当前有效状态：2.3已开始，B115完成附录A（2026-10-19）

2.2已完成至B114，用户“继续”后进入独立2.3底本。B115完成汇编引言、附录A全部（PDF p1—3至附录B标题前），16个唯一编号式及无编号关系已核；母本复用前逐项对独立PDF核验。复用映射见校订记录/2.3/2.2与2.3复用核验表.md。

下一批B116：从PDF p3的附录B开始，完整处理波动复表示至p4附录C标题前。2.3的B—D尚未校订；不能以同源或语法通过视为内容已核。使用当前正文直接编辑，历史脚本不要再次运行覆盖。下面2.2及更早状态为历史。

''';p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
p=M/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s+='\n## 2.3附录A核验（B115，2026-10-19）\n\nPDF p1—3与2.2附录A关联的Q053/Q072在本独立底本仍存在：时间因子、χ阶数、复折射率与支路、边界条件适用范围、E_ri、A.11b下标及A.8斜线范围。正文按当地原值保留，明确关联原问题号；没有采用新公式修正。振幅比叙述方向修正属于旧译错误，不进入原文勘误附件。\n';p.write_text(s,encoding='utf-8')
(OUT/'局部约定卡.md').write_text('# 2.3局部约定卡\n\nB115：附录A为线性光学，χ称线性极化率；时间相位按A.1为exp[+iωt−ik·r]；复折射率虚部约定并列保留。反射/透射系数是相对入射场幅的比，p偏振符号按本底本；反向介质与轴分量各依原式。未将2.2附录其他部分的约定当作已核结论。关联Q053/Q072未决。\n',encoding='utf-8')
p=ROOT/'Preface序言.md';s=p.read_text(encoding='utf-8');s=s.replace('（旧译待校订）：配合上一节阅读补充内容。','（B115已核引言与附录A，B—D待校订）：独立汇编线性光学、波动复表示、传播相位与极化薄片L系数；已核部分区分χ的线性响应、菲涅尔因子和局部符号约定。');p.write_text(s,encoding='utf-8')
p=TARGET.parent/'阅读导航.md';s=p.read_text(encoding='utf-8');s=s.replace('2.3及以后仍为旧译待校订。','2.3已校订引言与附录A，B—D及2.4以后仍为旧译待校订。');s+='\n## 2.3 薄膜产生的和频（附录）\n\n[进入正文](2.3%20多层膜的和频过程（SFG）：附录集.md)。独立底本12页；B115完成引言及附录A。\n\n1. 附录A（p1—3至B前，已核）：平面波的复表示、线性极化率与复折射率；由边界条件得到菲涅尔因子、反向入射及轴向分量关系。保留原符号和适用范围疑点。\n2. 附录B（p3—4，待核）：波动、行波与驻波、实场的复表示。\n3. 附录C（p4—10，待核）：单一介质、双介质与夹膜体系的传播光路及相位。\n4. 附录D（p10—12，待核）：极化薄片的L系数推导。\n\nB—D的概括目前仅依据标题及结构定位，后续校订后更新。与2.2虽同源，仍对独立页逐项核验；A.1等编号引用须注明节号。\n';p.write_text(s,encoding='utf-8')
print('B115 applied; 16 numbered equations; B–D unchanged')

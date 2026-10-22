from pathlib import Path
import re,json,csv,io,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];M=ROOT/'翻译管理';D=ROOT/'中文版本/第二章 薄膜产生的SFG'
TARGET=next(D.glob('2.3 *.md'));old=TARGET.read_text(encoding='utf-8')
assert not (OUT/'B116-修订前.md').exists()
(OUT/'B116-修订前.md').write_text(old,encoding='utf-8')
mother=next(D.glob('2.2 *.md')).read_text(encoding='utf-8')
b=mother[mother.index('## 附录B.'):mother.index('## 附录C.')]
b=b.replace('Q054','关联第2.2节Q054').replace('Q055','关联第2.2节Q055')
b=b.replace('底本接着给出两种表示法：','底本接着给出两种表示法。\n\n**表示法1：**')
b=b.replace('c.c.表示紧邻前项的复共轭。\n\n$$','c.c.表示紧邻前项的复共轭。\n\n**表示法2：**\n\n$$',1)
b=b.replace('c.c.表示紧邻前项的复共轭；','')
b=b.replace('；原式图另存对照。','；原页对照见PDF p4。')
start=old.index('## 附录B');end=old.index('## 附录C')
new=old[:start]+b+'\n'+old[end:]
new=new.replace('B115已完成引言与附录A（PDF p1—3，至附录B标题前）的本轮校订，含全部编号公式及无编号关系。附录B—D仍为旧译待校订；其公式不因语法可显示而视为已核验。','B115—B116已完成引言、附录A及附录B（PDF p1—4，至附录C标题前）的本轮校订，含全部编号公式及无编号关系。附录C—D仍为旧译待校订；其公式不因语法可显示而视为已核验。')
new=new.replace('本节A.1—A.12编号仅在本节范围内使用。','本节A.1—A.12、B.1—B.2编号仅在本节范围内使用。')
new=new.replace('附录A整理线性光学与菲涅尔因子（本轮已核）；附录B复习波动的复表示，附录C追踪传播光路及相位，附录D讨论极化薄片的L系数（后三部分目前依据结构定位，待逐段校订）。','附录A整理线性光学与菲涅尔因子，附录B复习行波、驻波及实电场的复表示（A、B本轮已核）；附录C追踪传播光路及相位，附录D讨论极化薄片的L系数（C、D目前依据结构定位，待逐段校订）。')
new=new.replace('正文和本节尚待校订的附录B、C与第2.2节主要使用','本节附录B使用负时间因子；附录C待核。第2.2节SFG正文也主要使用')
TARGET.write_text(new,encoding='utf-8');(OUT/'B116-本批译文.md').write_text(b,encoding='utf-8')
assert new[new.index('## 附录C'):]==old[old.index('## 附录C'):]
assert re.findall(r'\\tag\{([^}]+)\}',b)==['B.1','B.2']
assert not any(ord(c)<32 and c not in '\r\n' for c in new)
sha=hashlib.sha256((ROOT/'日语原版/Chapter2/chap2-3.pdf').read_bytes()).hexdigest()
assert sha=='63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384'
record='''# B116：附录B波动的复习

2026-10-19。底本：chap2-3.pdf，PDF p3附录B标题至p4附录C标题前。源SHA256：`63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384`。

| 原文位置 | 论述/公式组 | 处理 |
|---|---|---|
| p3，开头及(a)/(b) | 平面波/球面波，空间/时间余弦，周期与频率 | 核对所有定义；频率ν=2πω按原式保留，候选只入注，关联2.2 Q054 |
| p3下半 | 行波方向、等相位点、速度ω/k、驻波恒等式 | 含两种传播方向与乘积展开，未用概括替代 |
| p4上半 | 实电场与B.1、欧拉公式及B.2 | 保留负时间因子和各自编号；与附录A正时间因子明确区分 |
| p4中部 | 表示法1、2及Re/Im | 两式右端原缺E0；旧译已补入的幅度因子撤回，疑点与候选仅注，关联2.2 Q055 |
| p4，C标题前 | 两种取观测量的约定 | 保留半和、共轭乘积、只取实部与平方的叙述；译注区分瞬时平方/模平方/周期平均，不据此擅加归一化系数 |

本批逐段对独立底本p3/p4原页与文字层核验后复用2.2对应译文；消除母本转写遗留的重复c.c.解释，恢复两种表示法的小标题。全批B.1/B.2及无编号式采用可编辑数学。

原式处理：Q054/Q055用关联原问题号，不重复分配新号；未采用任何新原文修正，无新增E编号。旧译的频率/幅度补改若无原文依据，恢复原值，属于译文校订；原式本身保持。附录C—D内容与修订前逐字一致。

管理更新：进度、章节清单、分批建议、阅读导航、Preface、复用核验表、局部及全局约定、疑难/勘误附件状态；没有新增术语决定或把未决公式收入已核验语料。语法/显示结果另存，整文件语法检查不代表C—D已校订。
'''
(OUT/'B116.md').write_text(record,encoding='utf-8')
(OUT/'B116-覆盖.json').write_text(json.dumps({'batch':'B116','pages':[3,4],'start':'附录B标题','end':'附录C标题前','labels':['B.1','B.2'],'units':['定义与(a)(b)','行波与驻波','B.1/B.2','表示法1/2','观测量约定1/2'],'source_sha256':sha,'unreviewed_C_D_unchanged':True,'source_correction_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
def append(p,s):p.write_text(p.read_text(encoding='utf-8').rstrip()+'\n\n'+s.strip()+'\n',encoding='utf-8')
append(OUT/'2.2与2.3复用核验表.md','## B116核验更新\n\n附录B（独立底本p3—4、母本p37—38）已逐段/逐式目视与文字层核验，含B.1/B.2与所有无编号式。独立底本同样保留ν=2πω及两种表示法右端未写E0，故关联Q054/Q055；不把同源疑点当作可删除内容。C—D仍只有结构映射。')
append(OUT/'局部约定卡.md','## B116：附录B\n\n选cos(kz−ωt)，沿正z传播，复表示取负时间因子；α只是相位，A为一般复振幅，不是响应系数。保留底本ν=2πω及两种右端缺E0的表示法，关联Q054/Q055；实场平方、复场模平方、周期平均不可跨约定直接混用。')
append(M/'符号与约定.md','## 2.3附录B（B116）\n\nPDF p3—4选cos(kz−ωt)，复表示为负时间指数，与本节A.1正时间指数并存。α为相位、A为一般复振幅；ν换算及E0因子疑点关联2.2 Q054/Q055，未统一改式。')
append(M/'疑难与勘误.md','## 2.3附录B核验（B116）\n\n独立底本p3仍写ν=2πω（候选ω/(2π)未采用）；p4两种实场复表示的左端有E0、右端均未写，归一化需另核。分别关联2.2 Q054/Q055，正文保留原式并加注；未采用新公式修正，不新增E编号。')
p=ROOT/'中文版本/附件/原文勘误表.md';s=p.read_text(encoding='utf-8');s=s.replace('B115已校订引言与附录A，关联第2.2节Q053/Q072，并新增Q073','B115—B116已校订引言、附录A/B，关联第2.2节Q053—Q055/Q072，并登记Q073');p.write_text(s,encoding='utf-8')
def tsv(p,key,val,changes):
 rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0]);found=0
 for row in rows:
  if row[key]==val:row.update(changes);found+=1
 assert found
 buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_text(buf.getvalue(),encoding='utf-8-sig')
tsv(M/'章节清单.tsv','编号','2.3',{'状态':'B115—B116完成引言及附录A/B；C—D旧译待校订','映射核验':'独立底本p1—4至C标题前已核；C—D仅结构映射','公式图表范围':'A部16个、B部2个唯一编号式及相应无编号关系已核','导读状态':'Preface与第二章导航按A/B完成范围更新'})
tsv(M/'全书调查/分批建议.tsv','节号','2.3',{'执行状态':'2026-10-19至B116，已核引言及附录A/B（p1—4至C前）；下一批B117从p4附录C开始；C—D待核'})
p=M/'当前进度与续接.md';s=p.read_text(encoding='utf-8');entry='''## 当前有效状态：B116完成2.3附录B（2026-10-19）

已校订独立底本p3附录B起至p4附录C标题前，含行波/驻波、B.1/B.2、两种复表示、两种观测量约定。与2.2逐项核验后复用，保留并就地说明关联Q054/Q055；没有新采用的原文修正。附录C—D正文与批前保持一致。

累计完成2.3引言及附录A/B，18个编号式及相应无编号关系。下一批B117：从p4附录C起，先完整处理“单一且均匀的介质”至“两种介质”前；再分批处理界面和夹膜体系。参考渲染与验收见校订记录/2.3/B116相关文件。下面记录为历史，不运行旧生成脚本覆盖当前正文。

''';p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
p=ROOT/'Preface序言.md';s=p.read_text(encoding='utf-8');s=s.replace('（B115已核引言与附录A，B—D待校订）','（至B116已核引言与附录A/B，C—D待校订）').replace('已核部分区分χ的线性响应、菲涅尔因子和局部符号约定。','已核部分涵盖线性响应、菲涅尔因子、行波与驻波及实场复表示，原式疑点保留。');p.write_text(s,encoding='utf-8')
p=D/'阅读导航.md';s=p.read_text(encoding='utf-8');s=s.replace('2.3已校订引言与附录A，B—D及2.4以后','2.3已校订引言与附录A/B，C—D及2.4以后').replace('B115完成引言及附录A。','B115—B116完成引言及附录A/B。').replace('附录B（p3—4，待核）：波动、行波与驻波、实场的复表示。','附录B（p3—4至C前，已核）：从空间/时间余弦区分行波方向与驻波，再给出实电场、欧拉公式、两种复表示及观测量约定；频率换算和振幅因子保留疑点。').replace('B—D的概括目前仅依据标题及结构定位','C—D的概括目前仅依据标题及结构定位');p.write_text(s,encoding='utf-8')
print('B116 applied; B.1/B.2 and all unnumbered units; C–D unchanged')

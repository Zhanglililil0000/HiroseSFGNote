from pathlib import Path
import csv,json,hashlib,re
r=Path('HiroseSFGNote').resolve();m=r/'翻译管理';rec=m/'校订记录/1.1'
p=m/'术语表.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));assert len(R)==49
for ident,ja,en,zh,note in [
('T050','ハミルトニアン','Hamiltonian','哈密顿量','总H、无光H₀及相互作用H′依上下文区分'),
('T051','摂動論','perturbation theory','微扰论','与原文第一近似的阶次表述区分'),
('T052','密度行列法','density-matrix method','密度矩阵法','本页为引入；具体矩阵元定义待后文'),
('T053','緩和','relaxation','弛豫','本页涉及系统弛豫；不擅增弛豫常数'),
('T054','固有関数','eigenfunction','本征函数','Ψₙ与ψₙ的时间依赖分别保留'),
('T055','カップリング','coupling','耦合','原文相互作用括号中的词'),
('T056','固有値','eigenvalue','本征值','本页为Eₙ')]:
 x={k:'' for k in R[0]};x.update({'术语编号':ident,'日语候选':ja,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':note,'原文位置':'1.1 PDF p3，式(6)—(8)及说明','依据':'B003模型页面对照；英文为译者辅助对应','状态':'本批用法已页面核对；项目译名暂用','文本定位状态':'原文p3已视觉核对','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'译者辅助对应，不声称作者原文逐项提供英文'});R.append(x)
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s+='\n| Q011 | 1.1 PDF p3 第二段 | 原文“電荷分布が遍在する”的遍在疑为偏在 | 原文疑误/P2 | B003按电荷分布存在偏置译出并注；未获作者确认，不宣称原文已纠正 |\n';p.write_text(s,encoding='utf-8')
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='''
## B003（1.1 PDF p3）

| 符号/对象 | 本段含义与约定 | 状态 |
|---|---|---|
| H′(t) / H / H₀ | H′为式(6)的相互作用项，H为式(7)中总哈密顿量；H₀为无光相互作用时的哈密顿量且不显含时间 | 已页面对照，不把H₀等同总H |
| μ / E(t) | 电偶极矩及光电场；H′=−μ·E，点积与负号保留 | 已页面对照 |
| Ψₙ(r,t) / ψₙ(r) / Eₙ | 含时态、空间本征函数与能量本征值；式(8)共用一个编号 | 已页面对照 |
| exp(−iEₙt/ℏ) | 未微扰态的时间因子；负号保留 | 已页面对照 |

p2式(4)光场的正时间因子与p3态函数的负时间因子均保留作者原式，不因符号不同全局统一。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/第1章.md';s=p.read_text(encoding='utf-8');s+='''
## C005：总哈密顿量与微扰（B003）

- 来源：1.1 PDF p3，式(7)之后。原文节录：この光との相互作用がないとしたときのハミルトニアン H₀ に対する解からのずれを摂動論によって計算する。
- 中文对应片段：可从不存在光相互作用时的哈密顿量 H₀ 的解出发，用微扰论计算偏离该解的修正。
- 关联：T050、T051；节录的前提是相互作用项相对于总哈密顿量足够小，不可删去这一上下文。
- 核验：B003模型页面对照，非独立专业人工审校。

## C006：其他论文的括号限定（B003）

- 来源：1.1 PDF p3末段。原文节录：廣瀬が導出したもの（他にも論文があるが）を記す。
- 中文对应片段：列出广濑推导的表达式（虽然也有其他相关论文）。
- 上下文：CARS、CSRS等四波混频表达式。不能译成同时采用其他相关论文的结果。
- 核验：B003模型页面对照，非独立专业人工审校。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/README.md';s=p.read_text(encoding='utf-8').replace('B001、B002 共四条','B001—B003 共六条');p.write_text(s,encoding='utf-8')
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['编号']=='1.1');x['状态']='校订中：PDF p1—3已对照及参考渲染，其余待校订';x['映射核验']='PDF p1—3已逐段对照；第三部分仅开头完成';x['公式图表范围']='引言5组无编号公式＋式(1)—(8)及p3无编号式已核对；本范围无图表';x['导读状态']='整节导读仍草案；已处理前3页'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'全书调查/分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['预排编号']=='P002');assert x['PDF起页']=='3';x['执行状态']='部分由B003覆盖：仅p3已对照及参考渲染，p4未执行'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('部分校订：第1、2部分已对照及参考渲染','部分校订：前3页已对照及参考渲染，第三部分未完');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B001–B002 已对照校订 1.1 第1、2部分并完成参考渲染，整节未完成。','B001—B003 已对照校订 1.1 前3页并完成参考渲染，第三部分及整节未完成。').replace('B001–B002 已完成 1.1 第1、2部分；下一批从 PDF p3 第三部分开始；','B001—B003 已完成 1.1 前3页；下一批从 PDF p4 的相互作用与符号定义开始，优先处理至线性响应式(9)；');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- B001—B003：1.1 PDF p1—3已对照校订及参考渲染；第三部分仅开头完成，p4起仍为旧译，整节未完成。
- 本批[B003记录](校订记录/1.1/B003.md)：式(6)—(8)、无编号关系式及密度矩阵法引入；原文疑似用字错误Q011已明确加注。
- 参考渲染：marked＋KaTeX HTML/本地字体，无界面Edge；截图和合并数据在校订记录/1.1。模型二次对照，未经独立专业人工审校，也不保证所有阅读器兼容。
- 全书39份、717页；23份旧译未开始重新校订，1.1部分校订，15节待译。P001由B001+B002覆盖，P002仅p3由B003覆盖，p4未执行。
- 已有六条模型页面对照语料，术语表56条（多数暂用或候选），原有用户决定保留。Preface整节导读仍草案。

## 最新断点

- 最后批次：B003。已起草/已对照/已参考渲染范围：p1起至p3末“通常の摂動法を使ってもそれなりの結果が得られることを示すために、その計算を付録 Aに示す。”及右括号。
- 底本：1.1；SHA256 55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 下一批B004：PDF p4“相互作用のハミルトニアンを H′=er·E…”开始。先核对电荷符号、坐标与能级定义及线性响应式(9)，准确终点在查看完整推导后登记，不把长式(10)默认纳入。
- 前文约定：H′为相互作用项，H为总哈密顿量，H₀为不显含时间的无光哈密顿量；式(8)时间因子 exp(−iEₙt/ℏ)，Ψ/ψ大小写保留。μ与前文p均涉及电偶极矩，符号变换按作者原文。
- 延续p/P、α/β/γ与χ的微观/宏观区分；用户决定SFG为和频过程，χ⁽²⁾全称二阶非线性极化率（明确上下文可简称极化率），Fresnel coefficient为菲涅尔因子。
- Q004、Q009已在B002处理；Q008和Q011为原文疑字，已加注但作者未确认；Q010宏观归一化待后文回查。

## 下一批入口

先读本文件、B003记录及相关术语，检查用户变更。p4已有原文图缓存，可直接查看；不扫描全书，不重复渲染未修改的前批。新批可按相同方式扩展参考渲染脚本。
''',encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');old=(rec/'B003-修订前.md').read_text(encoding='utf-8');mark='\u200b\t相互作用哈密顿量为';assert s.split(mark,1)[1]==old.split(mark,1)[1]
assert s.split('## 1. 引言',1)[1].split('## 3.',1)[0]==old.split('## 1. 引言',1)[1].split('## 3.',1)[0]
seg=s.split('## 3. 分子的 SFG 极化与振动共振',1)[1].split(mark,1)[0];assert re.findall(r'\\tag\{(\d+)\}',seg)==['6','7','8'];assert '\u200b' not in seg and '\t' not in seg
D=json.loads((rec/'渲染检查.json').read_text(encoding='utf-8'));assert len(D['results'])==3;check=next(x for x in D['results'] if x['batch']=='B003');assert check['width']==check['scrollWidth'] and check['formulas']==9
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('PASS: B003 source hash, equations 6–8, unaffected surrounding text, reference render; management, 56 terms and 6 corpus entries synchronized.')

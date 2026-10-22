from pathlib import Path
import csv,json,re,hashlib
r=Path('HiroseSFGNote').resolve();m=r/'翻译管理';rec=m/'校订记录/1.1'
p=m/'术语表.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));assert len(R)==59
for ident,ja,en,zh,note in [('T060','２倍波発生','second-harmonic generation','倍频过程','原文指ω₁=ω₂的情形；SHG完整名称还可讨论，非用户新确认'),('T061','３波混合','three-wave mixing','三波混频','原文式(10)标题；不与四波混频混淆')]:
 x={k:'' for k in R[0]};x.update({'术语编号':ident,'日语候选':ja,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':note,'原文位置':'1.1 PDF p4 式(10)标题及相邻说明','依据':'B005模型页面对照；英语为译者辅助对应','状态':'本批用法已页面核对；项目译名暂用','文本定位状态':'原文p4已视觉核对','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'辅助释义，缩写SHG由作者提供'});R.append(x)
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='''
## B005（1.1 PDF p4 式10）

χ_ijk^(2)(ω=ω₁+ω₂)=P_i^(2)/(E_j(ω₁)E_k(ω₂))按原式；整体系数−Ne³/ℏ²，求和g/n/n′。四组项均为外因子乘[A−B]，外层相加；所有iΓ为正号，矩阵元n′n/nn′的次序逐一保留，ρ_g^(0)在外层花括号后。

原文将ω₁=ω₂称SHG、ω₁≠ω₂称SFG；译文保留本式上下文的区分，不据此另造对全书过程分类的规则。详细核对见B005校订记录。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/第1章.md';s=p.read_text(encoding='utf-8');s+='''
## C009：式(10)后的过程名称（B005）

- 来源：1.1 PDF p4 式(10)之后括号说明。日语结构为“ω₁=ω₂ のときには２倍波発生(SHG)、ω₁≠ω₂のときには和周波発生(SFG)になる。”（数学符号按可读形式转录）。
- 中文：当ω₁=ω₂时，对应倍频过程（SHG）；当ω₁≠ω₂时，对应和频过程（SFG）。
- 关联：T001、T060；保留等号/不等号条件，适用范围为当前式(10)说明，不擅自推广。
- 核验：B005模型页面对照，非独立专业人工审校。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/README.md';s=p.read_text(encoding='utf-8').replace('B001—B004 共八条','B001—B005 共九条');p.write_text(s,encoding='utf-8')
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['编号']=='1.1');x['状态']='校订中：至p4式(10)及SHG/SFG说明已对照和参考渲染';x['映射核验']='p1起至p4式(10)后说明已逐项对照；式(11)起未校订';x['公式图表范围']='引言5组无编号公式、式(1)—(10)及p3无编号式已核对；本范围无图表';x['导读状态']='整节仍草案；第三部分仅至式(10)后说明'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'全书调查/分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));next(x for x in R if x['预排编号']=='P002')['执行状态']='部分由B003—B005覆盖：至p4式(10)后说明，式(11)起未执行'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('至第4页式（9）已对照及参考渲染','至第4页式（10）后说明已对照及参考渲染');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B001—B004 已校订至 1.1 第4页式（9）','B001—B005 已校订至 1.1 第4页式（10）后说明').replace('B001—B004 已处理至线性响应式(9)；下一批优先处理p4式(10)及相邻SHG/SFG说明，不默认包含差频式(11)；','B001—B005 已处理至p4式(10)及相邻说明；下一批处理差频式(11)及整流/DFG说明，跨页解释另行划分；');p.write_text(s,encoding='utf-8')
p=m/'排版工具/README.md';s=p.read_text(encoding='utf-8').replace('--b004 仅检查第四批','--b004 仅检查第四批，--b005 仅检查第五批');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- B001—B005：1.1已处理至PDF p4式(10)后SHG/SFG括号说明，页面对照及参考渲染通过；式(11)起仍为旧译，第三部分和整节未完成。
- [B005记录](校订记录/1.1/B005.md)登记四组项的矩阵元/分母/符号；本批未发现旧译新的实质符号错误，主要统一表述与排版。
- 全书39份717页；23份旧译未开始重新校订，1.1部分校订，15节待译。P001已覆盖，P002未完整覆盖（p4式11及后文未执行）。
- 术语61条，多数为暂用或候选；对照语料九条。模型页面核验，非独立专业人工审校。
- 参考渲染使用marked＋KaTeX HTML/配套字体、无界面Edge；检查图及各批合并指标在校订记录/1.1。只验证此参考环境。

## 最新断点

- 最后批次B005；已起草/对照/参考渲染：从p1起至p4式(10)后的等频SHG/异频SFG说明右括号。
- 底本1.1，SHA256：55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 下一批B006：从p4差频式(11)开始，处理完整公式和紧邻的ω₁=ω₂整流、ω₁≠ω₂差频说明；跨p4—5的解释段另按完整论述划界，不默认纳入。
- p4原文图复用B003-原文p4.png。不要重复扫描全书或渲染未改动前批。
- 延续约定：e取负；H′=er·E、P=−Ner保留；g不是自动等于基态。式(10)整体−Ne³/ℏ²，四组[A−B]相加，所有iΓ为正；不能套用到式(11)而不看原式。
- 用户决定：SFG为和频过程，χ⁽²⁾全称二阶非线性极化率（上下文明确可简称），Fresnel coefficient为菲涅尔因子；SHG倍频过程仍是译者暂用。
- 未决Q008/Q011疑字已有注；Q010宏观归一化、Q012电荷约定衔接待后文回查。Q004/Q009已处理。本批无新增疑难。

## 下一批入口

读取本文件及B005记录，检查用户改动，再逐组核对式(11)。Preface整节概括继续保留草案状态；更新的是局部进度，不是整节定稿。
''',encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');old=(rec/'B005-修订前.md').read_text(encoding='utf-8');start='**（二阶非线性极化：三波混频）**';end='**（差频过程（DFG））**';assert s.split(end,1)[1]==old.split(end,1)[1]
assert s[s.index('## 1. 引言'):s.index(start)]==old[old.index('## 1. 引言'):old.index(start)]
seg=s.split(start,1)[1].split(end,1)[0];assert re.findall(r'\\tag\{(\d+)\}',seg)==['10'];assert seg.count('\\left[')==4 and seg.count('\\right]')==4;assert '\u200b' not in seg and '\t' not in seg
D=json.loads((rec/'渲染检查.json').read_text(encoding='utf-8'));assert len(D['results'])==5;v=next(x for x in D['results'] if x['batch']=='B005');assert v['width']==v['scrollWidth'] and v['formulas']==3
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('PASS: B005 eq10, 4 groups, unchanged earlier text and eq11 onward, source hash and reference render; records synchronized.')

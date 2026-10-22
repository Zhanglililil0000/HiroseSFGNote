from pathlib import Path
import csv,re,json,hashlib
r=Path('HiroseSFGNote').resolve();m=r/'翻译管理';rec=m/'校订记录/1.1'
p=m/'术语表.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));assert len(R)==56
for ident,ja,en,zh,note in [('T057','演算子','operator','算符','此处r是矢量算符，不等同于其矩阵元'),('T058','エネルギー固有状態','energy eigenstate','能量本征态','包括电子、振动及适用时的转动状态；g不直接等同基态'),('T059','準位','level','能级','与能级占据的假设一起保留')]:
 x={k:'' for k in R[0]};x.update({'术语编号':ident,'日语候选':ja,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':note,'原文位置':'1.1 PDF p4 上部定义段，式(9)之前','依据':'B004模型页面对照，英文为译者辅助对应','状态':'本批用法已页面核对；项目译名暂用','文本定位状态':'原文p4相关定义已视觉核对','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'辅助对应，不声称作者原文提供英文'});R.append(x)
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='''
## B004（1.1 PDF p4 上部及式9）

| 符号 | 原文约定 | 状态 |
|---|---|---|
| e | 按电子电荷取负值；H′=er·E，P=−Ner | 已页面对照，不改成正元电荷；与μ约定的衔接后续回查 |
| r | 构成分子的粒子（原子和电子）位置坐标的矢量算符 | 已页面对照 |
| i,j,k,l | 实验室固定直角坐标系的坐标轴下标 | 已页面对照 |
| g,n,n′,n″ | 孤立分子能量本征态；含电子、振动及适用时的转动状态 | 已页面对照；g为无光微扰时分子所处状态，不预设基态 |
| χ_ij^(1)、ω_ng、Γ_ng、ρ_g^(0) | 式(9)按原符号保留；Γ及ρ的解释不在本段擅补 | 公式已核对，进一步定义后文回查 |

N的归一化问题Q010仍未因P=−Ner得到单位体积定义，不将其标为解决。
''';p.write_text(s,encoding='utf-8')
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s+='\n| Q012 | 1.1 p3式(6)与p4开头 | e明确取负值，H′=er·E与前文−μ·E的约定衔接需回查 | 原文约定/P2 | B004保留原符号和负电荷说明，不静默改成正元电荷；不在本批断言原文有误 |\n';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/第1章.md';s=p.read_text(encoding='utf-8');s+='''
## C007：g的限定（B004）

- 来源：1.1 PDF p4定义段。原文节录：このうちで状態 g は光による摂動がないときに分子がとる状態とする。
- 中文：其中，g表示没有光微扰时分子所处的状态。
- 关联：T058、T059。不直接补成基态；上下文还保留只占据g的假设。
- 核验：B004模型页面对照，非独立专业人工审校。

## C008：电荷的符号约定（B004）

- 来源：1.1 PDF p4首段。原文节录：また、e は電子の電荷を基準にとったため、負の値を持っている。
- 中文：另外，原文规定e以电子电荷为基准，并取负值。
- 使用限制：本条只记录作者约定，不据此擅自调整其他公式的符号；衔接问题见Q012。
- 核验：B004模型页面对照，非独立专业人工审校。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/README.md';s=p.read_text(encoding='utf-8').replace('B001—B003 共六条','B001—B004 共八条');p.write_text(s,encoding='utf-8')
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['编号']=='1.1');x['状态']='校订中：至PDF p4式(9)已对照及参考渲染，其余待校订';x['映射核验']='PDF p1—3及p4至式(9)已逐段对照；第三部分未完';x['公式图表范围']='引言5组无编号公式、式(1)—(9)及p3无编号式已核对；无图表';x['导读状态']='整节仍草案；第三部分仅至式(9)'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'全书调查/分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['预排编号']=='P002');x['执行状态']='部分由B003+B004覆盖：p3及p4至式(9)已对照和参考渲染；式(10)起未执行'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('部分校订：前3页已对照及参考渲染，第三部分未完','部分校订：至第4页式（9）已对照及参考渲染，第三部分未完');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B001—B003 已对照校订 1.1 前3页并完成参考渲染，第三部分及整节未完成。','B001—B004 已校订至 1.1 第4页式（9）并完成参考渲染，第三部分及整节未完成。').replace('B001—B003 已完成 1.1 前3页；下一批从 PDF p4 的相互作用与符号定义开始，优先处理至线性响应式(9)；','B001—B004 已处理至线性响应式(9)；下一批优先处理p4式(10)及相邻SHG/SFG说明，不默认包含差频式(11)；');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- B001—B004：1.1已校订至PDF p4线性响应式(9)，已完成页面对照及参考渲染；式(10)起仍为旧译，第三部分和整节未完成。
- [B004记录](校订记录/1.1/B004.md)覆盖两段定义和式(9)；没有把p4其余长公式标为完成。
- 原有用户决定：SFG为和频过程；χ⁽²⁾全称二阶非线性极化率（明确上下文可简称极化率）；Fresnel coefficient为菲涅尔因子。
- 全书39份717页；23份旧译未开始重新校订，1.1部分校订，15节待译。P001已覆盖，P002仅至p4式(9)，不能标记整窗完成。
- 对照语料八条、术语59条（多数暂用或候选）。核验为模型二次对照，未经独立专业人工审校。
- 参考渲染沿用marked＋KaTeX HTML/本地字体及无界面Edge；截图和各批合并指标在校订记录/1.1，不等于所有阅读器验证。

## 最新断点

- 最后批次B004；已起草/已对照/已参考渲染：p1起至p4式(9)的ρ_g^(0)及末尾标点。
- 底本1.1，SHA256：55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 下一批B005从p4“２次の非線形分極：３波混合”开始，优先处理式(10)及其相邻的ω₁=ω₂/ω₁≠ω₂说明；差频式(11)不默认纳入。
- p4原文图可复用B003-原文p4.png；不重复扫描全书或渲染未修改前批。
- 约定：e原文明确取负，H′=er·E、P=−Ner按原文；r为矢量算符；g为无光微扰时所处状态，不预设基态。坐标指标i/j/k/l和能级指标g/n/n′/n″区分。
- 式(9)保留gn求和、两个+iΓ_ng、矩阵元ng/gn次序及ρ_g^(0)。不要按其他教材表达式静默改符号。
- 未决：Q008/Q011原文疑字已有注；Q010宏观归一化、Q012电荷与μ约定衔接后续回查。Q004/Q009已处理。

## 开始下一批

先读本文件和B004记录，检查用户变更；新批按完整公式划界并逐组核对矩阵元、分母和求和。参考渲染脚本可按新边界扩展。Preface整节导读仍为草案。
''',encoding='utf-8')
p=m/'排版工具/README.md';s=p.read_text(encoding='utf-8').replace('脚本当前仅检查 1.1 的前两部分','脚本当前按批检查 1.1 的已处理部分').replace('--b003 仅检查第三批','--b003 仅检查第三批，--b004 仅检查第四批');p.write_text(s,encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');old=(rec/'B004-修订前.md').read_text(encoding='utf-8');end='**（二阶非线性极化：三波混频）**';assert s.split(end,1)[1]==old.split(end,1)[1]
assert s[s.index('## 1. 引言'):s.index('相互作用哈密顿量写为')]==old[old.index('## 1. 引言'):old.index('\u200b\t相互作用哈密顿量为')]
seg=s[s.index('相互作用哈密顿量写为'):s.index(end)];assert re.findall(r'\\tag\{(\d+)\}',seg)==['9'];assert '\u200b' not in seg and '\t' not in seg
assert '\\omega+\\omega_{ng}+i\\Gamma_{ng}' in seg and '\\omega-\\omega_{ng}+i\\Gamma_{ng}' in seg
D=json.loads((rec/'渲染检查.json').read_text(encoding='utf-8'));assert len(D['results'])==4;v=next(x for x in D['results'] if x['batch']=='B004');assert v['width']==v['scrollWidth'] and v['formulas']==9
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('PASS: B004 equation9 and source hash; previous body and eq10 onward unchanged; reference render and records synchronized.')

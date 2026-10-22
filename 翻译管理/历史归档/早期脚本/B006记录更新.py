from pathlib import Path
import csv,json,re,hashlib
r=Path('HiroseSFGNote').resolve();m=r/'翻译管理';rec=m/'校订记录/1.1'
p=m/'术语表.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));assert len(R)==61;x={k:'' for k in R[0]};x.update({'术语编号':'T062','日语候选':'整流効果','英语辅助释义':'rectification effect','推荐中文候选':'整流效应','定义与适用语境':'式(11)相邻说明：ω₁=ω₂时产生直流电场；不改写原频率条件','原文位置':'1.1 PDF p4 式(11)后','依据':'B006模型页面对照；英文为辅助释义','状态':'本批用法已页面核对；项目译名暂用','文本定位状态':'原文页面已核对','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'译者辅助对应，非作者提供的英文原词'});R.append(x)
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s+='\n| Q013 | 1.1 PDF p4 式(11)第三组B项 | 原文分子为(r_k)_{gn′}(r_j)_{n′n}，j是否应为i待核验 | 原文公式疑点/P1 | B006高分辨率确认原字为j；与旧译一致，译文照录并加注。尚未推导/外证，不擅自修正，不宣称原式无误 |\n';p.write_text(s,encoding='utf-8')
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='''
## B006（1.1 PDF p4 式11）

输出频率ω₁−ω₂，电场乘积E_j(ω₁)E_k(−ω₂)；整体−Ne³/ℏ²，求和g/n/n′，ρ_g^(0)在花括号后。四组外因子符号−、−、+、+；前两组外分母为−iΓ，后两组为+iΓ；八个内分母均+iΓ。第四组内部为−A−B，不能套式(10)的A−B。

第三组B原文为(r_k)_{gn′}(r_j)_{n′n}，保留j并注记Q013；其正确性尚未确认。原文将等频情形称直流电场生成/整流效应，异频称DFG。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/第1章.md';s=p.read_text(encoding='utf-8');s+='''
## C010：等频整流与异频差频（B006）

- 来源：1.1 PDF p4 式(11)后的括号说明；原文节录“直流電場の生成すなわち整流効果”。
- 中文对应：产生直流电场，即整流效应。
- 上下文：ω₁=ω₂时为上述情形；ω₁≠ω₂时对应差频过程（DFG）。数学条件不可省略。
- 关联：T020、T062。仅收录此语言片段，不把有未决指标问题的式(11)纳入已确认公式语料。
- 核验：B006模型页面对照，非独立专业人工审校。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/README.md';s=p.read_text(encoding='utf-8').replace('B001—B005 共九条','B001—B006 共十条');p.write_text(s,encoding='utf-8')
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['编号']=='1.1');x['状态']='校订中：至p4式(11)后说明已对照及参考渲染，Q013待核验';x['映射核验']='至p4式(11)后说明逐项对照，跨页解释段未校订';x['公式图表范围']='式(1)—(11)等已对照转录；式(11)指标疑点Q013保留，非全节验收';x['导读状态']='整节仍草案；局部至式(11)后说明'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'全书调查/分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));next(x for x in R if x['预排编号']=='P002')['执行状态']='部分由B003—B006覆盖：至p4式(11)后说明；p4末跨页段未执行，Q013待核验'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('至第4页式（10）后说明已对照及参考渲染','至第4页式（11）后说明已对照及参考渲染，原式指标有待核验');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B001—B005 已校订至 1.1 第4页式（10）后说明','B001—B006 已校订至 1.1 第4页式（11）后说明（原式指标Q013待核验）').replace('B001—B005 已处理至p4式(10)及相邻说明；下一批处理差频式(11)及整流/DFG说明，跨页解释另行划分；','B001—B006 已处理至p4式(11)及相邻说明；下一批从p4末跨页解释段开始，按完整论述划分，不默认纳入三阶长公式；');p.write_text(s,encoding='utf-8')
p=m/'排版工具/README.md';s=p.read_text(encoding='utf-8').replace('--b005 仅检查第五批','--b005 仅检查第五批，--b006 仅检查第六批');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- B001—B006：1.1已处理至PDF p4式(11)后整流/DFG括号说明，内容与公式照原文核对，参考渲染通过；第三部分/整节未完成。
- [B006记录](校订记录/1.1/B006.md)：原式第三组B项含r_j，已高分辨率确认；是否为r_i之误待核验Q013。译文保留原式并注，不把本批状态解释为原公式已证实正确。
- 全书39份717页；23份旧译未重新校订，1.1部分校订，15节待译。P001已覆盖，P002仍未全覆盖：p4末跨页段未处理。
- 术语62条、语言对照语料十条，多数译名暂用或候选；有疑点的式(11)未收入已确认公式语料。核验为模型页面对照，非独立专业人工审校。
- 参考渲染工具及字体已缓存，仅渲染本批；各批截图与合并指标在校订记录/1.1，只验证该参考环境。

## 最新断点

- 最后批次B006；已起草/对照/参考渲染：从p1起至p4式(11)后的整流/DFG说明右括号；原式正确性受Q013限制。
- 底本1.1 SHA256：55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 下一批B007从p4末“上に示した式は…”开始；旧译起点为“上述公式表示的是…”。跨页读取完整解释段，再按完整论述处理跃迁、拉曼张量与振动共振选择规则等说明，不默认包含后面的三阶长公式。
- p4图复用B003-原文p4.png，p5图已缓存B006-下批原文p5.png（未计完成）。
- 式(11)与式(10)不同：E_k参数−ω₂；四组外符号−、−、+、+；前两组外分母−iΓ；第四组内部−A−B。第三组B照原文r_j，禁止无记录改成r_i。
- 延续用户决定SFG为和频过程，χ⁽²⁾全称二阶非线性极化率（明确上下文可简称），Fresnel coefficient为菲涅尔因子。SHG倍频过程、整流效应仍为译者暂用。
- 未决Q008/Q011疑字已有注；Q010归一化、Q012电荷约定衔接待后文回查；Q013原式指标疑点需重点复核。Q004/Q009已处理。

## 开始下一批

读取本文件及B006记录，检查用户变更后继续。既有整节导读不定稿，不把P002或第三部分标为完成；尽可能复用文本与图像缓存。
''',encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');old=(rec/'B006-修订前.md').read_text(encoding='utf-8');a='**（差频过程（DFG））**';b='\u200b\t上述公式表示的是';assert s.split(b,1)[1]==old.split(b,1)[1]
assert s[s.index('## 1. 引言'):s.index(a)]==old[old.index('## 1. 引言'):old.index(a)]
seg=s.split(a,1)[1].split(b,1)[0];formula=re.search(r'\$\$([\s\S]*?)\$\$',seg).group(1);assert re.findall(r'\\tag\{(\d+)\}',formula)==['11'];assert formula.count('\\left[')==4 and formula.count('\\right]')==4
assert formula.count('-i\\Gamma')==2 and formula.count('+i\\Gamma')==10
assert '\\frac{(r_k)_{gn\'}(r_j)_{n\'n}}' in formula and '\\frac{E' not in formula
assert '\u200b' not in seg and '\t' not in seg
D=json.loads((rec/'渲染检查.json').read_text(encoding='utf-8'));assert len(D['results'])==6;v=next(x for x in D['results'] if x['batch']=='B006');assert v['width']==v['scrollWidth'] and v['formulas']==6
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('PASS: B006 transcription, 4 groups, signs, source hash, unchanged surrounding text and reference render; Q013 and progress synchronized.')

from pathlib import Path
import csv,json,re,hashlib
r=Path('HiroseSFGNote').resolve();m=r/'翻译管理';rec=m/'校订记录/1.1'
p=m/'术语表.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));assert len(R)==62
for ident,ja,en,zh,note in [('T063','選択則','selection rule','选择规则','本段须同时具备线性吸收与拉曼散射活性'),('T064','確率振幅','probability amplitude','概率振幅','跃迁概率振幅不与ρ_g^(0)占据概率混淆'),('T065','反ストークスラマン散乱','anti-Stokes Raman scattering','反斯托克斯拉曼散射','保留中间态与相同初末态的上下文'),('T066','電子共鳴','electronic resonance','电子共振','与振动共振区分；不单凭背景光断定'),('T067','バックグラウンド光','background light','背景光','暂不替换成非共振背景，原文允许其被电子共振增强'),('T068','核四重極子遷移','nuclear quadrupole transition','核四极跃迁','按作者原词暂译；物理所指待专业核验，不擅自改成电四极')]:
 x={k:'' for k in R[0]};x.update({'术语编号':ident,'日语候选':ja,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':note,'原文位置':'1.1 PDF p5，三阶响应段之前的解释','依据':'B007模型页面对照；英文辅助释义','状态':'源词已页面对照；译名暂用，物理解释按上下文核验','文本定位状态':'原文页面已对照','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'译者辅助对应，不声称作者提供英文'});R.append(x)
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s+='\n| Q014 | 1.1 p5 第二组跃迁解释 | 原文对向较低能态的跃迁仍称吸收，后段称受激发射型；核四重极子跃迁的所指亦待核验 | 原文表述/P2 | B007按原说法翻译，源词及上下文登记，未擅自纠正，不作为独立物理结论 |\n';p.write_text(s,encoding='utf-8')
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='''
## B007（1.1 PDF p4末—p5解释段）

ρ_g^(0)原文明确定义为无光微扰时处于状态g的分子比例/概率；与跃迁概率振幅区分。i=x,y,z逐分量考虑j/k的9种组合，只有一束入射光时6种；不额外补入对称性假设。

本段指定ω₂红外、ω₁可见。第一/第二组分别为向上吸收型和向下受激发射型振动跃迁共振；第三/第四组与交换两束光后的线性吸收有关。Q013和既有电荷/归一化问题不因解释段完成而关闭。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/第1章.md';s=p.read_text(encoding='utf-8');s+='''
## C011：振动共振选择规则（B007）

- 来源：1.1 PDF p5，原文“線形吸収とラマン散乱の両方に活性を持つ振動モードだけが SFG、DFG の振動共鳴を与える”。
- 中文：只有同时具有线性吸收活性和拉曼散射活性的振动模式，才能产生SFG、DFG的振动共振。
- 关联T063。“同时”“振动共振”限定不可省略，不将此片段推广到未限定的全部SFG来源。
- 核验：B007模型页面对照，非独立专业人工审校。

## C012：占据概率（B007）

- 来源：1.1 PDF p5首段，原文“光による摂動がないときに状態 g に分布している分子の分率（分子が g に見出される確率）”。
- 中文：没有光微扰时处于状态g的分子比例，即在状态g中找到分子的概率。
- 符号ρ_g^(0)，与跃迁概率振幅区分。上下文见B007第一段。
- 核验：B007模型页面对照，非独立专业人工审校。
''';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/README.md';s=p.read_text(encoding='utf-8').replace('B001—B006 共十条','B001—B007 共十二条');p.write_text(s,encoding='utf-8')
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['编号']=='1.1');x['状态']='校订中：至p5三阶段之前已对照及参考渲染；Q013等未决';x['映射核验']='p1起至p5解释段末已对照；三阶长公式起未执行';x['导读状态']='整节仍草案；第3部分解释段已处理'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'全书调查/分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));next(x for x in R if x['预排编号']=='P002')['执行状态']='p3—4已由B003—B007覆盖；p4末段跨到p5解释部分，原式疑点Q013未决';next(x for x in R if x['预排编号']=='P003')['执行状态']='仅p5顶部解释段由B007覆盖；三阶长公式起及后页未执行'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('至第4页式（11）后说明已对照及参考渲染，原式指标有待核验','至第5页三阶段之前已对照及参考渲染，原式指标仍有待核验');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B001—B006 已校订至 1.1 第4页式（11）后说明（原式指标Q013待核验）','B001—B007 已处理至 1.1 第5页三阶段之前（Q013等仍未决）').replace('B001—B006 已处理至p4式(11)及相邻说明；下一批从p4末跨页解释段开始，按完整论述划分，不默认纳入三阶长公式；','B001—B007 已完成二阶响应解释段；下一批定位p5起三阶长公式的完整跨页范围，按求和及括号层次划分；');p.write_text(s,encoding='utf-8')
p=m/'排版工具/README.md';s=p.read_text(encoding='utf-8').replace('--b006 仅检查第六批','--b006 仅检查第六批，--b007 仅检查第七批');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- B001—B007：1.1从p1起至PDF p5三阶段之前的解释段已对照及参考渲染；三阶长公式起仍为旧译，第三部分/整节未完成。
- [B007记录](校订记录/1.1/B007.md)：p4末跨页段、占据概率、选择规则、跃迁与拉曼张量、电子共振及背景说明。原式疑点Q013未解决；新表述问题Q014保持原文未擅改。
- 全书39份717页；23份旧译未重新校订，1.1部分校订，15节待译。P002的页范围已覆盖，但含未决公式疑点；P003仅p5顶部解释段已覆盖，不能标整窗完成。
- 术语68条，多数暂用/候选；语言对照语料十二条。核验为模型页面对照，非独立专业人工审校。
- 参考渲染缓存沿用marked＋KaTeX HTML/本地字体、无界面Edge；只渲染本批，截图/合并指标在校订记录/1.1。

## 最新断点

- 最后批次B007。已起草/对照/参考渲染止于p5“バックグラウンド光があるからといって直ちに電子共鳴が存在すると結論するのは早計である。”
- 底本1.1 SHA256：55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 下一批B008：p5“３次の分極－１：２波長光による４波混合”，旧译标题“三阶极化－1：双波长光引起的四波混合”。先查看其完整跨页公式范围，按完整求和/括号层次安排，不预定一次处理全部三阶公式。
- p4/p5图已缓存；新页按需渲染，不扫描全书，不重复渲染未改动前批。
- 新核对定义：ρ_g^(0)为无光微扰时g态分子比例/概率，不是概率振幅。ω₂红外、ω₁可见；同时具备线性吸收与拉曼活性是本段振动共振规则。
- 延续用户决定：SFG为和频过程，χ⁽²⁾全称二阶非线性极化率（明确上下文可简称），Fresnel coefficient为菲涅尔因子。新增译名不视为用户自动确认。
- Q013原式(11)第三组B的r_j照录并注；Q014原文向低能态仍称吸收、以及核四极跃迁所指待核验。Q008/Q011已注，Q010归一化和Q012电荷衔接仍待回查。

## 下一批入口

读本文件及B007记录，检查用户改动后定位完整长公式。保持原符号及整体编号，不能把尚未闭合的公式记为完成；Preface整节概括仍为草案。
''',encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');old=(rec/'B007-修订前.md').read_text(encoding='utf-8');start='上述各式给出的是相应的极化系数';oldstart='\u200b\t上述公式表示的是';end='**（三阶极化－1：双波长光引起的四波混合）**'
assert s.split(end,1)[1]==old.split(end,1)[1];assert s[s.index('## 1. 引言'):s.index(start)]==old[old.index('## 1. 引言'):old.index(oldstart)]
seg=s[s.index(start):s.index(end)];assert '\u200b' not in seg and '\t' not in seg;assert len(seg.strip().split('\n\n'))==5
D=json.loads((rec/'渲染检查.json').read_text(encoding='utf-8'));assert len(D['results'])==7;v=next(x for x in D['results'] if x['batch']=='B007');assert v['width']==v['scrollWidth'] and v['formulas']==35
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('PASS: B007 five paragraphs, source hash, unchanged surrounding text and reference render; records synchronized.')

from pathlib import Path
import csv,json,re,hashlib
r=Path('HiroseSFGNote').resolve();m=r/'翻译管理';rec=m/'校订记录/1.1'
p=m/'术语表.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));assert len(R)==68
for ident,ja,en,zh,note in [('T069','４波混合','four-wave mixing','四波混频','与原文三波混频区分；四波混合保留为旧译检索项'),('T070','χ⁽³⁾','third-order nonlinear susceptibility','三阶非线性极化率','译者候选；本批只核式(12)定义和首主组，不表示全文三阶公式通过')]:
 x={k:'' for k in R[0]};x.update({'术语编号':ident,'日语候选':ja,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':note,'原文位置':'1.1 PDF p5 三阶标题与式(12)开头','依据':'B008页面对照；英文辅助对应，T070日语栏为符号索引非作者日文措辞','状态':'本批源词/定义已对照；译名暂用','文本定位状态':'p5标题与定义已视觉核对；整式未完成','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'译者辅助对应，非作者提供的英文原词'});R.append(x)
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='''
## B008（1.1式12定义与第1主组，仅工作稿）

输出为2ω₁+ω₂，输入场E_j(ω₁)E_k(ω₁)E_l(ω₂)；总系数−Ne⁴/ℏ³，求和g/n/n′/n″。第1主组外因子(r_l)_{ng}/(ω₂−ω_ng+iΓ_ng)，4子项相加、内部A−B；13分母的iΓ均为正。

T₁仅是管理工作稿临时标识，原文无该符号。式12共6组24子项，后5组仍待核对；不因首组通过把其他组或整式标为完成。
''';p.write_text(s,encoding='utf-8')
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['编号']=='1.1');x['状态']='校订中：正文止于p5三阶前；式12定义与第1组工作稿已核，整式未完';x['公式图表范围']='式(1)—(11)等照录核对；式11有Q013；式12仅定义/第1组已核，正文旧式未替换'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'全书调查/分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));next(x for x in R if x['预排编号']=='P003')['执行状态']='B007完成p5顶部解释；B008仅工作稿核式12定义/第1组，p6后组未核，正文整式未替换'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('至第5页三阶段之前已对照及参考渲染，原式指标仍有待核验','正文至第5页三阶段之前；式（12）首组工作稿已核，整式未完；原式指标仍待核验');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B001—B007 已处理至 1.1 第5页三阶段之前（Q013等仍未决）','正文已处理至 1.1 第5页三阶段之前；B008已核式(12)定义与第1组工作稿，整式未完（Q013等仍未决）').replace('B001—B007 已完成二阶响应解释段；下一批定位p5起三阶长公式的完整跨页范围，按求和及括号层次划分；','式(12)已定位p5—7共6主组24子项，B008完成定义及第1组工作稿；下一批核p6第2—4组，后续核第5—6组并整式检查后统一替换正文；');p.write_text(s,encoding='utf-8')
p=m/'排版工具/README.md';s=p.read_text(encoding='utf-8').replace('--b007 仅检查第七批','--b007 仅检查第七批，--b008 检查第八批工作稿');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- 正文仍只校订至p5三阶响应段之前（B001—B007）；B008完成式(12)定义、总系数及第1主组的工作稿核对，不计整式完成。
- 式(12)跨p5—7，6主组、每组4子项，共24子项。为控量拆分：B008第1组；B009计划第2—4组；B010计划第5—6组及整式检查。实际可按疑难进一步拆分。
- [B008记录](校订记录/1.1/B008.md)、[工作稿](校订记录/1.1/B008-式12工作稿.md)。工作标识T₁不是作者符号；工作稿不作为正式译文。
- 正文仅加式12进度提示，原式12未替换。式13起完全未校订。第三部分/整节未完成。
- 全书39份717页；23份旧译未重新校订，1.1部分校订，15节待译。P003不完整：p5首组只在工作稿核对，后组未核。
- 术语70条，多数暂用/候选；语言对照语料仍十二条，未将部分公式加入完整公式语料。模型页面对照，非独立专业人工审校。

## 双断点：正式正文与公式工作稿

- 正文止于p5“バックグラウンド光があるからといって直ちに電子共鳴が存在すると結論するのは早計である。”
- 工作稿止于p5式12第1主组大方括号闭合；已核定义、−Ne⁴/ℏ³、g/n/n′/n″求和及4子项；第1组13分母均+iΓ。本批参考渲染已检查，只证明该工作稿显示正常。
- 下一批B009：PDF p6顶部第2组，外因子(r_l)_{gn″}/(ω₂+ω_n″g+iΓ_n″g)；再核第3组(r_k)_{ng}/(ω₁−ω_ng+iΓ_ng)、第4组(r_j)_{ng}/(ω₁−ω_ng+iΓ_ng)，各4子项。不默认包含p6末第5组。
- p6第5组外因子(r_j)_{gn″}/(ω₁+ω_n″g+iΓ_n″g)，以及p7第6组，留后批；所有组及整式闭合通过后再替换正文，保留编号12。
- 缓存：p5为B006-下批原文p5.png；p6/p7为B008-原文p6.png、B008-原文p7.png。后两页目前只定位结构，不算逐项核验。
- 底本1.1 SHA256：55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 用户决定：SFG和频过程；χ⁽²⁾全称二阶非线性极化率；Fresnel coefficient菲涅尔因子。新增三阶全称属候选，不假称用户确认。
- 既有Q013式11指标、Q014原文表述、Q010归一化/Q012电荷约定等待回查，未因本批关闭。

## 下一批入口

读B008记录及工作稿，检查用户变更。逐组核完后记录实际范围；未完成完整长公式前，不将正文页面、P003或整式标为完成。参考渲染本批只渲染工作稿，后批可复用依赖。
''',encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');old=(rec/'B008-修订前.md').read_text(encoding='utf-8');notice='\n> **式（12）工作进度：** B008已核对定义及第1主组，分组工作稿保存在翻译管理中；正文式（12）尚未整体校订，不计为完成。\n\n';assert s.replace(notice,'')==old
work=(rec/'B008-式12工作稿.md').read_text(encoding='utf-8');assert work.count('\\left[')==5 and work.count('\\right]')==5
D=json.loads((rec/'渲染检查.json').read_text(encoding='utf-8'));assert len(D['results'])==8;v=next(x for x in D['results'] if x['batch']=='B008');assert v['width']==v['scrollWidth'] and v['formulas']==6
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('PASS: B008 working draft and render, source hash, original translation unchanged apart from progress notice; partial scope recorded.')

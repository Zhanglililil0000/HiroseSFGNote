from pathlib import Path
import csv,json,hashlib
r=Path('HiroseSFGNote').resolve();m=r/'翻译管理';rec=m/'校订记录/1.1'
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='\n## B009（式12第2—4主组，仅工作稿）\n\n第2组外分母ω₂+ω_n″g+iΓ_n″g；第3/4组外分母ω₁−ω_ng+iΓ_ng。每组4子项相加、内括号A−B，三组39分母的iΓ均正。各中间频率不同，具体顺序见B009记录与工作稿；已核4/6组，不能据此推广尚未核的第5/6组。\n';p.write_text(s,encoding='utf-8')
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in R if x['编号']=='1.1');x['状态']='校订中：正文至p5三阶前；式12定义及第1—4组工作稿已核，整式未完';x['公式图表范围']='式1—11等已核（Q013待查）；式12已核4/6组工作稿，未整体替换正文'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'全书调查/分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));next(x for x in R if x['预排编号']=='P003')['执行状态']='B007完成p5顶部；B008—B009工作稿核式12定义/第1—4组；第5—6组及整式未完，正文未替换'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('式（12）首组工作稿已核','式（12）第1—4组工作稿已核');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B008已核式(12)定义与第1组工作稿','B008—B009已核式(12)定义与第1—4组工作稿').replace('B008完成定义及第1组工作稿；下一批核p6第2—4组，后续核第5—6组并整式检查后统一替换正文；','B008—B009完成定义及第1—4组工作稿；下一批核第5—6组并整式检查后统一替换正文，如有疑难进一步拆分；');p.write_text(s,encoding='utf-8')
p=m/'排版工具/README.md';s=p.read_text(encoding='utf-8').replace('--b008 检查第八批工作稿','--b008 检查第八批工作稿，--b009 检查第九批工作稿');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- 正式正文仍止于1.1 p5三阶响应段之前（B001—B007）。B008—B009已核式12定义与第1—4主组，共16/24子项；第5、6组及全式检查未完，正文旧式12未替换。
- [核对总表](校订记录/1.1/式12-核对进度.md)、[B009记录](校订记录/1.1/B009.md)、[本批工作稿](校订记录/1.1/B009-式12工作稿.md)。T₁—T₄只是管理标识，不是作者符号。
- B009工作稿3组参考渲染通过，4个数学片段，无水平溢出；本批只改正文进度提示，公式和其他正文保持不变。
- 全书39份717页；23份旧译未重新校订，1.1部分校订，15节待译。P003仍未完整覆盖。术语仍70条，语言对照语料仍十二条，不把部分公式纳入完整公式语料。
- 页面核对为模型复核，非独立专业人工审校；参考渲染仅验证本地marked/KaTeX/Edge环境。

## 最新双断点

- 正式正文：p5二阶解释段末；原式12仍是待整体校订旧译。
- 公式工作稿：第4主组大方括号已闭合，至p6中下部；已核1—4组，不包含p6最末第5组。
- 下一批B010：p6末第5主组，外因子(r_j)_{gn″}/(ω₁+ω_n″g+iΓ_n″g)；再核p7首第6主组，外因子(r_k)_{gn″}/(ω₁+ω_n″g+iΓ_n″g)。各4子项。
- 分组完成后必须整体验证：输出2ω₁+ω₂，输入场E_j(ω₁)E_k(ω₁)E_l(ω₂)，公共−Ne⁴/ℏ³，求和g/n/n′/n″，6组24子项的顺序、所有括号和编号12；原文末尾括号也须对照，不能仅拼接草稿。
- 若仍有疑点，登记并进一步拆批，不强行按计划宣布完成。式13未开始。
- 缓存：B008-原文p6.png/p7.png；B008、B009工作稿及检查图。复用已有文件，不重扫全书。
- 底本SHA256：55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 用户译名仍为SFG和频过程、χ⁽²⁾二阶非线性极化率、Fresnel coefficient菲涅尔因子。Q013式11指标等既有未决问题未关闭，本批无新增疑难。

## 下一批入口

读取本文件、核对总表和B009记录，先检查用户改动。待完整公式核验后统一替换正文；不因已核16子项就将整式或整节标为完成。
''',encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');old=(rec/'B009-修订前.md').read_text(encoding='utf-8');assert s.replace('B008–B009已核对定义及第1–4主组，第5、6组和整式检查未完','B008已核对定义及第1主组')==old
w=(rec/'B009-式12工作稿.md').read_text(encoding='utf-8');assert w.count('\\left[')==15 and w.count('\\right]')==15;assert w.count('\\frac')==39
D=json.loads((rec/'渲染检查.json').read_text(encoding='utf-8'));assert len(D['results'])==9;v=next(x for x in D['results'] if x['batch']=='B009');assert v['width']==v['scrollWidth'] and v['formulas']==4
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('PASS: B009 3 groups/12 subterms/39 fractions, reference render, unchanged formal text and source hash; partial progress synchronized.')

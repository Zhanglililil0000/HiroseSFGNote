from pathlib import Path
import json,re,csv,io,collections
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.5 两个CH₃基团的张量分量.md'
s=target.read_text(encoding='utf-8')
idx=json.loads((out/'全节公式与覆盖索引.json').read_text(encoding='utf-8'))
batch=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
whole=json.loads((out/'整节渲染检查.json').read_text(encoding='utf-8'))
assert batch['math']==whole['math']==1577
assert all(not r['overs'] and r['width']==r['scrollWidth'] for r in batch['results']+whole['results'])
p=root/'翻译管理/疑难与勘误.md';issues=p.read_text(encoding='utf-8')
for q in range(171,176):
 if re.search(rf'^## Q{q}\b',issues,re.M):continue
 notes=list(dict.fromkeys(line for line in s.splitlines() if line.startswith('>') and f'Q{q}' in line))
 assert notes,q
 issues+=f'\n\n## Q{q}｜4.5原文疑点\n\n状态：待核验，原式或原述保留，候选未采用。\n\n'+'\n\n'.join(notes)+'\n'
 if q==174:
  positions=json.loads((out/'原式分组疑点位置.json').read_text(encoding='utf-8'))
  issues+='\n27处具体来源：'+', '.join(x['source'] for x in positions)+'。详见4.5原式分组疑点位置与公式覆盖索引。\n'
if 'Q168续：PDF p5标题' not in issues:issues+='\n\n4.5 Q168续：PDF p5标题也重复“两者朝下”，已就地说明，候选未采用。\n'
p.write_text(issues,encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 4.5局部约定卡（全节，B323—B361）

- abc：单甲基固定系；xyz：双甲基基团固定系；XYZ：空间固定系。附录F简并部分的一般式又以abc分量写出，按原文说明先将abc换为xyz，再代入双甲基表达式。
- c沿甲基C₃轴从C朝H；z沿两C₃轴角平分线从X指向甲基；x位于两轴所成平面。α首先为CXC半角，第6部分面内示例又用α表示偏角，语境区分。
- φA、φB是各甲基内部旋转角；φ是整个基团CXC面相对于表面的扭转角。二者不能相互替换。第5部分等角标题与随后的正弦关系冲突见Q171。
- 第6部分Z指向基板内部：θ=π−θtilt、χ=π/2+χip。φ为使分子面垂直于表面的转角，原投影面ab保留待核，不改作xy。
- 内部甲基自由旋转、整体φ随机及面内χip随机是不同平均。正文仅面内随机；附录B—E保留一般空间取向。φ也随机时，原文置cos(nφ)=sin(nφ)=0。
- 分子β是一阶超极化率（二阶场响应）；空间χ为二阶非线性极化率，可在明确语境中简称极化率。键系ζ/ξ/η与分子abc、xyz分开。
- 单甲基全对称带组合成同相a₁与反相b₁；简并带组合成a₁、b₁、b₂三支。不同条件下±上/下号可能表示不同内部角配置，或a轴/b轴模式，依每处原定义辨认。
- θ、α的函数幂与φ/χ的倍角分开；附录F保留βijk=βjik前提，不推广为全置换对称。
- 分子模式分裂但光谱重叠时，原文要求对所列表达式求和，按原述保留。
- Q168—Q175均原式/原述保留，候选未采用。27处括号不配对分别就地标Q174，附录F求和末项varpi字形见Q175；不能据排版成功将其视为已证明。
''',encoding='utf-8')
with (out/'术语卡.md').open('a',encoding='utf-8') as h:h.write('''

## 全节补充

| 原文 | 中文 | 适用范围 |
|---|---|---|
| 空間固定(XYZ)系 | 空间固定(XYZ)系 | 大写轴与基团固定xyz不同 |
| ランダム配向 | 随机取向 | 正文是面内随机，整体扭转φ随机需另说明 |
| 面外振動 | 面外振动 | 本节组合模式b₂，不等同于把CH伸缩改成弯曲振动 |
| グループ1—4 | 第1—4组 | 附录A一般分子简并张量分组 |
| (none) | 无 | 对应原偏振组合无列出信号/分量，50处明确保留 |

分子β、空间χ、模式、上下号与取向条件均保留原层级；本阶段不新增未经确认的全书标准译法。
''')
table='# 4.5全节单元覆盖\n\n日期：2026-10-21。B323—B361覆盖原PDF全78页、6个正文部分及附录A—F。\n\nB323—B325为p1—3原题、目录、绪论、坐标、谱带和对称性分类；后续2627个原文物理行逐行索引，跨页续式并入同一表达式。\n\n| 批次 | PDF页 | 内容 | χ单分量等式 | β单分量等式 |\n|---|---|---|---|---|\n'
for r in idx['batches']:
 c=collections.Counter(x['symbol'] for x in r['tensor_components'])
 table+=f"| {r['batch']} | {','.join(map(str,r['pages']))} | {r['scope']} | {c['chi']} | {c['beta']} |\n"
table+='\n计数口径：单个三坐标下标分量起头的等式，链式相等只计首个左式，重复出现按所在位置分别计；和/差组合及求和恒等式另收于公式索引。空间χ共853式：正文178，附录B—F各135（两支全对称54，三支简并81）。β单分量等式共156式，包含正文/附录中重复的代入关系。总计1009式。原文未给这些表式编号，不人为补原编号。\n'
(out/'全节单元覆盖.md').write_text(table,encoding='utf-8')
(out/'结构与分批计划.md').write_text('''# 4.5结构与分批完成记录

原PDF78页，已按B323—B361共39批完成本轮译校。实际分界：第1—4部分p1—3；第5部分p3—6；第6部分p6—19；附录A p19—22、B p22—30、C p30—38、D p38—49、E p49—58、F p58—78。共享边界页分别按正文标题/公式组定位。

第5部分五类内部旋转逐类处理；第6部分四类条件按全对称/简并模式分批；附录A单独核一般分子式；附录B—E每类保留完整两支全对称和三支简并27分量表；附录F一般模式分三组完整27分量。没有用正文平均表或“同前”摘要替代附录长式。

所有公式均依据本节数字PDF字体、字形及基线转录，上下标与正文行分别记录；全页图浏览复核，异常及跨页公式重点检查。每个后续段落/公式在Markdown隐藏注释内保留来源行定位。27处原式括号疑点均原样保留，不作隐含补括号。

后续进入4.6（B362），先核原题与局部约定，不沿用旧文件名判断主题。全节专业复核时优先处理Q168—Q175，再比较正文平均表与附录一般式的系数、符号和归一化。
''',encoding='utf-8')
p=root/'翻译管理/当前进度与续接.md';old=p.read_text(encoding='utf-8');marker='## 当前有效状态：4.5全节译校完成（2026-10-21）'
if marker not in old:p.write_text('# 当前进度与续接\n\n'+marker+'\n\nB323—B361覆盖全78页、6个正文部分及附录A—F；新增36个完整条件/模式批次。已索引853个空间χ及156个分子β单分量等式（重复及代入关系按出现位置计），所有长式可编辑；1577个数学片段通过语法及参考排版检查。Q168—Q175原式/原述保留，未采用原文修正。覆盖、分组疑点和限制详见4.5整节完成复核。\n\n下一批B362：进入4.6，先核原题、实际印刷页码与局部约定。旧文件名“CH2弯曲振动的SFG光谱”不作为主题依据。以下为历史记录。\n\n'+old.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';records=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(records[0])
for r in records:
 if r['编号']=='4.5':r.update({'状态':'本轮全节覆盖、译校与参考排版完成；原文疑点待核','映射核验':'全78页按B323—B361核对；正文及附录A—F完整覆盖','公式图表范围':'853个空间χ及156个分子β单分量等式，组合关系另列；1577数学片段','导读状态':'节首、Preface及第四章导航已据全节更新','导读草案':'建立双甲基坐标、内部旋转及模式组合；按五类内部角求分子张量，再按四类条件求面内平均空间张量；附录A—F保留一般内部与空间取向完整表。'})
with p.open('w',encoding='utf-8',newline='') as h:
 w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(records)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';old=p.read_text(encoding='utf-8');old=old[:old.index('## 4.5')]+'''## 4.5 (CH₃)₂X基团的处理

[进入4.5](4.5%20%28CH3%292X型分子的SFG.md)。全78页完成本轮译校，正文与附录A—F均保留完整公式。

第1—4部分定义两级分子坐标、内部旋转及模式/对称分类；第5部分按五种内部旋转条件列分子β；第6部分定义空间角，给四类条件下面内随机取向χ。附录A给一般分子式；附录B—E补各类条件的一般空间取向；附录F给一般式及简并模式的代入条件。各部分实际页界和阅读概括见节首。

853个空间χ和156个分子β单分量等式有覆盖索引；重复及代入关系按出现位置计。Q168—Q175保留待核，注意两级内部角、±号含义、原括号缺损与一般式的交换对称前提。

## 后续

下一批B362进入4.6，先核原题、实际页码与局部约定。
''';p.write_text(old,encoding='utf-8')
p=root/'Preface序言.md';old=p.read_text(encoding='utf-8')
old=re.sub(r'(?m)^- \[4\.5 .*$', '- [4.5 (CH₃)₂X基团的处理](中文版本/第四章%20单层膜与多层膜的和频/4.5%20%28CH3%292X型分子的SFG.md)（全节译校完成）：从双甲基坐标、内部旋转与模式组合出发，先求分子张量，再求面内平均空间张量；附录A—F保留一般内部角与一般空间取向完整表，原文疑点就地说明。',old)
if '### 4.5阅读提示（全节完成' not in old:old+='\n\n### 4.5阅读提示（全节完成，2026-10-21）\n\n全78页正文及附录A—F完成本轮译校。先分清甲基abc、基团xyz、空间XYZ和φA/φB/整体φ，再选择内部旋转条件及模式；正文随机取向表与附录一般取向表不能互换。节首含各部分概括和实际PDF页界。Q168—Q175保留待核，27处括号疑点有逐处注释，未采用原文修正。\n'
p.write_text(old,encoding='utf-8')
for filename,txt in [
 ('翻译管理/符号与约定.md','## 4.5全节约定补充（2026-10-21）\n\nφA/φB为各甲基内部角，整体φ为CXC面扭转；abc、xyz、XYZ三级坐标分别处理。θ=π−θtilt，χ=π/2+χip；第6部分α另指面内偏角。正文仅面内随机，附录B—E一般空间取向，附录F后半以βijk=βjik为前提。所有±解释依所在条件，详见局部约定卡。'),
 ('翻译管理/分批执行与质量控制.md','## 4.5全节完成（2026-10-21）\n\nB323—B361共39批覆盖78页。按旋转条件、完整模式及附录拆分，后续2627原文物理行逐行建索引，公式跨页续接；853个空间χ及156个分子β单分量等式已覆盖。全页图浏览、异常重点核验、39批与合稿排版检查已完成；不把原文理论验证与翻译验收混同。下一批B362进入4.6。'),
 ('中文版本/附件/原文勘误表.md','## 4.5本轮状态（2026-10-21）\n\n全78页正文与附录A—F完成译校。Q168—Q175均保留原式或原陈述，候选未采用，暂无新增已采用的原文修正条目。Q174包含27处括号不配对，正文逐处说明，精确位置列于4.5校订记录；Q175保留原varpi字形。坐标、模式、对称性、旧译漏表及幂次修复属于译文校订。')]:
 p=root/filename;old=p.read_text(encoding='utf-8')
 if txt.split('\n')[0] not in old:p.write_text(old+'\n\n'+txt+'\n',encoding='utf-8')
p=root/'翻译管理/已核验对照语料/第4章.md';old=p.read_text(encoding='utf-8')
if 'C4.5-B324-01' not in old:p.write_text(old+'''

## C4.5-B324-01｜双甲基基团固定坐标

- 来源：`日语原版/Chapter4/chap4-5.pdf`，PDF p1—2，第2部分(2)。
- 日语：２個のメチル基のC₃軸の２等分線に沿ってz軸を取り、X原子からメチル基の方向を正方向とする。
- 中文：沿两个甲基C₃轴的角平分线取z轴，从X原子指向甲基的方向为正。
- 上下文：基团固定xyz系，与单甲基abc系、空间XYZ系分别处理；不连带确认附近原文投影面与角度疑点。
- 核验：模型对照原PDF文本与页图，2026-10-21；未经独立专业人工审校。
''',encoding='utf-8')
print('全节管理记录、导读、疑难与勘误状态已更新')

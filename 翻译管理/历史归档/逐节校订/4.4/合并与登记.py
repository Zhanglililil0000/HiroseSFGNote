from pathlib import Path
import re,json,csv,io
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.4 CH基团的取向与和频张量.md'
files=[out/f'B{n}-本批译文.md' for n in range(314,323)]
texts=[f.read_text(encoding='utf-8') for f in files]
head=texts[0].replace('B314—B315已对照PDF p1—3，完成原目录、引言及第1—3部分；第4部分起仍为旧译待核。','B314—B322已完成全10页本轮译校。原文疑点Q160—Q167保留并就地说明，未采用原文公式修正。')
guide='''## 阅读引导

- 第1部分（p1—2）：说明双原子及直线分子的轴对称性，区分欧拉角与有独立意义的取向角。
- 第2部分（p2—3）：定义CH基团、表面法线及面内取向角，保留原文中混入C₃轴和三个H的疑点。
- 第3部分（p3）：给出沿CH键伸缩的分子一阶超极化率分量，明确分子坐标与表面坐标的区别。
- 第4部分（p3—4）：列出一般取向下完整27个表面张量分量，注意函数幂与倍角的区别。
- 第5部分（p4—8）：分别讨论面内随机（5a，p5）、C₃ᵥ（5b，p5—6）、C₄ᵥ/C₆ᵥ（5c，p6）、Cₛ（5d，p6—7）及C₂ᵥ（5e，p7—8）取向。先确认取向条件，再查偏振组合；原文中的求和式、符号和选择规则疑点见就地注释。
- 第6部分（p8—9）：从入射、反射场及菲涅尔振幅反射系数得到表面场，进而计算和频极化。
- 第7部分（p9—10）：将和频极化转换为反射、透射方向的和频电场，保留作者末尾关于符号的不确定性。

> **译者注（阅读边界）：** 本轮核验原文覆盖、翻译转录及参考排版；原文理论疑点仍待核实。不得省略各表的角度、取向及求和条件。

'''
assert '## 引言' in head
joined='\n\n'.join([head.replace('## 引言',guide+'## 引言')]+texts[1:])
target.write_text(joined,encoding='utf-8')
index=[]
for f,s in zip(files,texts):
 c=json.loads((out/(f.name[:4]+'-覆盖.json')).read_text(encoding='utf-8'))
 displays='\n'.join(re.findall(r'\$\$([\s\S]*?)\$\$',s))
 lhs=re.findall(r'(?:^|\n)(\\chi_\{[xyz]{3}\})\s*&?=',displays)
 index.append({'batch':f.name[:4],'pages':c['pages'],'scope':c['scope'],'surface_tensor_left_sides':lhs,'numbered_labels':re.findall(r'\\tag\{([^}]+)\}',s)})
count=sum(len(x['surface_tensor_left_sides']) for x in index)
tags=re.findall(r'\\tag\{([^}]+)\}',joined)
assert count==89,(count,[(x['batch'],len(x['surface_tensor_left_sides'])) for x in index])
assert len(tags)==len(set(tags))==19,tags
assert '旧译待核' not in joined
(out/'全节公式与覆盖索引.json').write_text(json.dumps({'numbered':tags,'table_component_occurrences':count,'batches':index},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'全节单元覆盖.md').write_text('# 4.4全节单元覆盖\n\n日期：2026-10-21。原PDF全10页对照页图与文本。\n\n| 批次 | PDF页 | 内容 | 表内左式数 |\n|---|---|---|---|\n'+'\n'.join(f"| {x['batch']} | {','.join(map(str,x['pages']))} | {x['scope']} | {len(x['surface_tensor_left_sides'])} |" for x in index)+'\n\n一般式27项，5a随机7项，5b三重取向15项，5d镜面取向27项，5e双重取向13项，共89项。5c按原文指向5a，无重复表。19个编号式：'+', '.join(tags)+'。无独立插图。\n',encoding='utf-8')
renderer=(out.parent/'4.3/检查全节排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.3','校订记录/4.4').replace("startsWith('4.3 ')","startsWith('4.4 ')")
(out/'检查全节排版.cjs').write_text(renderer,encoding='utf-8')
# Append only new issues; reruns are safe.
p=root/'翻译管理/疑难与勘误.md';s=p.read_text(encoding='utf-8')
for q in range(163,168):
 if re.search(rf'^## Q{q}\b',s,re.M):continue
 lines=[line for t in texts for line in t.splitlines() if line.startswith('>') and f'Q{q}' in line]
 assert lines,q
 s+=f'\n\n## Q{q}｜4.4原文疑点\n\n状态：待核验，原式或原陈述保留，候选未采用。\n\n'+'\n\n'.join(lines)+'\n'
p.write_text(s,encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 4.4局部约定卡（全节更新，2026-10-21）

- 双原子及直线分子轴对称，只需两个独立取向角；φ的独立意义与形式上的欧拉角记法分别保留。
- 表面z指向基板内部，CH的c轴沿键；θ=π−θtilt，χ=π+χip。不得套用4.3亚甲基的π/2偏移。
- 分子β为一阶超极化率（二阶场响应）；表面χ为二阶非线性极化率。原坐标说明中χ/β及下标范围差异保留见Q161。
- 第3部分βccc及βaac=βbbc描述沿CH键伸缩；不按旧文件名擅加弯曲模式。
- θ的函数幂与χ的倍角分别核对；第4部分涉及φ的项置零，不等于把φ取零。
- 第5部分必须保留面内取向分布。镜面表使用两种配置之和，未擅自改成平均；该处α、β为几何角，与分子β区别。
- 第6/7部分c为光速，θi/r/t为光学角，n′为表面层折射率。6.3混用上标、6.5c平方因子和7.4c/7.5c的Pz照录；本节Lpz用正弦，与4.3不同。
- Q160—Q167均保留原式或原陈述并注明候选，未采用原文修正。
''',encoding='utf-8')
(out/'术语卡.md').write_text('''# 4.4局部术语对应

| 日语/符号 | 中文 | 辨析 |
|---|---|---|
| CH基 | CH基团 | 原题为取向与和频张量；旧文件名保留以兼容链接 |
| ２原子分子／直線分子 | 双原子分子／直线分子 | 轴对称，只需两个独立取向角 |
| 傾斜角／面内配向角 | 倾斜角／面内取向角 | θtilt从外向法线计量，χip是表面投影角 |
| β | 一阶超极化率 | 对应二阶场响应；几何角β另辨 |
| χ | 二阶非线性极化率 | 上下文明确时可简称极化率 |
| Fresnel coefficient | 菲涅尔因子 | 本节反射场关系具体称菲涅尔振幅反射系数 |

沿用全书已确认术语；不因原文疑点新增全书标准译法。
''',encoding='utf-8')
p=root/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8')
marker='## 当前有效状态：4.4全节译校完成（2026-10-21）'
if marker not in s:p.write_text('# 当前进度与续接\n\n'+marker+'\n\nB314—B322覆盖原PDF全10页、七正文部分，19个编号式与89个表内张量分量已索引。Q160—Q167保留原式或原述并就地说明，未采用原文修正。节首、Preface、第四章导航与管理记录已更新。最终排版与覆盖检查见4.4整节完成复核。\n\n下一批B323：进入4.5，先核原题、结构、局部坐标及角度，不直接套用4.4各表。以下为历史记录。\n\n'+s.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for r in rows:
 if r['编号']=='4.4':r.update({'状态':'本轮全节页面对照及排版整理完成；原文疑点未决','映射核验':'全10页按B314—B322逐页对照','公式图表范围':'19个编号式、89个表内张量左式及无编号关系已覆盖','导读状态':'已据核验正文更新节首、Preface及第四章导航','导读草案':'从轴对称分子与CH取向建立分子响应，列一般及不同面内取向下张量，再连接表面电场、极化与出射场。'})
with p.open('w',encoding='utf-8',newline='') as h:
 w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';s=p.read_text(encoding='utf-8');s=s[:s.index('## 4.4')]+'''## 4.4 CH基团的取向与和频张量

[进入4.4](4.4%20CH基团的取向与和频张量.md)。全10页完成本轮译校。旧文件名保留以兼容链接，正文题目按原文校正。

第1—3部分说明轴对称分子、CH取向及分子β；第4部分列一般取向下27个表面分量；第5部分分别讨论面内随机及C₃ᵥ、C₄ᵥ/C₆ᵥ、Cₛ、C₂ᵥ取向；第6、7部分连接表面场、和频极化及出射场。节首有逐部分概括。

19个编号式、89个表内分量已索引。Q160—Q167保留待核，注意原文混入甲基描述、随机表与一般式不一致、镜面表多余χ及场公式上标和符号差异。

## 后续

下一批B323进入4.5，先核原题、结构与局部约定。
''';p.write_text(s,encoding='utf-8')
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8')
s=re.sub(r'(?m)^- \[4\.4 .*$',lambda m:m[0].split('](')[0]+']('+m[0].split('](')[1].split(')')[0]+')（全节译校完成）：从轴对称分子及CH取向建立分子响应，列一般及不同面内取向下的张量，最后连接表面场、和频极化及出射场；Q160—Q167就地保留待核。',s)
if '### 4.4阅读提示（全节完成' not in s:s+='\n\n### 4.4阅读提示（全节完成，2026-10-21）\n\n全10页已完成本轮译校。先读轴对称与CH局部角度，再按面内取向选择张量表，最后阅读场关系。节首有各部分内容概括。正文讨论沿CH键伸缩，旧文件名“CH弯曲振动”仅为链接兼容保留。19个编号式、89个表分量已覆盖；Q160—Q167仍待核实。\n'
p.write_text(s,encoding='utf-8')
for filename,txt in [
 ('翻译管理/符号与约定.md','## 4.4全节约定补充（2026-10-21）\n\nθ=π−θtilt、χ=π+χip，不套用4.3偏移；分子β与表面χ分开。θ的幂与χ的倍角分别保留；镜面表几何β另辨。第6/7部分的上标、平方因子与正弦Lpz按本节原页保留。详见4.4局部约定卡。'),
 ('翻译管理/分批执行与质量控制.md','## 4.4全节完成（2026-10-21）\n\nB314—B322按完整定义、取向表与场关系分批覆盖10页；19个编号式和89个表分量已索引。下一批B323进入4.5，先独立核结构及局部约定。'),
 ('中文版本/附件/原文勘误表.md','## 4.4本轮状态（2026-10-21）\n\n全10页完成译校。Q160—Q167均保留原式或原陈述，候选未采用，暂无新增原文修正条目。原题、旧译漏项、幂次与选择规则反译的修复属于翻译校订；原文随机表差异、镜面表多余χ及场式上标混用等见正文就地说明与疑难记录。'),
 ('翻译管理/校订记录/4.4/结构与复用核验表.md','## 4.4全节完成（2026-10-21）\n\nB314—B322覆盖10页、七正文部分。一般27、随机7、三重15、镜面27、双重13，共89个表内左式，另有19个编号式。复用前节排版后逐项与本节原页独立比较，保留本节上标及符号差异。无独立插图遗漏；Q160—Q167未决，无原文修正采用。')]:
 p=root/filename;s=p.read_text(encoding='utf-8') if p.exists() else ''
 if txt.split('\n')[0] not in s:p.write_text(s+'\n\n'+txt+'\n',encoding='utf-8')
print(json.dumps({'numbered':len(tags),'table_left_sides':count,'by_batch':[(x['batch'],len(x['surface_tensor_left_sides']))for x in index]},ensure_ascii=False))

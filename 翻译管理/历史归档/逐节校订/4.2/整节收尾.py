from 整节工具 import *
import csv,io
files=[out/f'B{n}-本批译文.md' for n in range(277,295)]
texts=[f.read_text(encoding='utf-8') for f in files]
head=texts[0].replace('B277已对照PDF p1—2，完成原目录、引言及第1部分“欧拉角”；第2部分起仍为旧译待核。','B277—B294已完成全19页本轮译校。原文疑点Q138—Q145保留并就地说明，未采用原文公式修正。')
guide='''## 阅读引导

先明确角度和坐标，再查与样品取向相符的张量表，最后连接表面电场、极化及出射电场。不同表中的条件不能省略。

- 第1部分（p1—2）：定义欧拉角、交线轴、正旋转与旋转顺序。
- 第2部分（p2—3）：区分甲基内部旋转、外向法线倾斜角和面内取向角，并对应到公式所用欧拉角。
- 第3部分（p3—4）：从单个CH键变换到甲基分子固定系，区分全对称与简并振动的张量分量。
- 第4部分（p4—12）：先列一般取向的分量，再分别处理自由内部旋转、三个H等价且旋转冻结、两个H等价的情况。
- 第5部分（p12—17）：在内部旋转冻结且三个H等价的条件下，讨论面内随机及几种对称取向表面的响应与偏振选择。
- 第6部分（p17—18）：将入射与反射电场合成表面场，通过菲涅尔关系求和频极化。
- 第7部分（p18—19）：从极化求反射、透射方向的和频电场，并给出菲涅尔L因子。作者保留的符号疑问见末注。

> **译者注（阅读边界）：** 公式已对照原页恢复；原文表间系数、指标及场因子疑点尚未解决。译校完成不表示这些推导已获物理验证。

'''
head=head.replace('## 引言',guide+'## 引言')
joined='\n\n'.join([head]+texts[1:])
target.write_text(joined,encoding='utf-8')
tags=re.findall(r'\\tag\{([^}]+)\}',joined)
assert len(tags)==19 and len(set(tags))==19, tags
index=[]
for f,s in zip(files,texts):
    coverage=json.loads((out/(f.name[:4]+'-覆盖.json')).read_text(encoding='utf-8'))
    displays=re.findall(r'\$\$([\s\S]*?)\$\$',s)
    lhs=re.findall(r'\\chi_\{([xyz]{3})\}\s*&?=', '\n'.join(displays))
    index.append({'batch':f.name[:4],'pages':coverage['pages'],'scope':coverage['scope'],
                  'surface_tensor_left_sides':lhs,'numbered_labels':re.findall(r'\\tag\{([^}]+)\}',s)})
count=sum(len(x['surface_tensor_left_sides']) for x in index)
assert count==178, count
for number in [281,286,287]:
    assert len(index[number-277]['surface_tensor_left_sides'])==27
assert sum(len(index[n-277]['surface_tensor_left_sides']) for n in range(282,286))==27
(out/'全节公式与覆盖索引.json').write_text(json.dumps({'numbered':tags,'table_component_occurrences':count,'batches':index},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'全节单元覆盖.md').write_text('# 4.2全节单元覆盖\n\n日期：2026-10-21。PDF全19页均已对照页图。\n\n| 批次 | 原文PDF页 | 内容 | 表内χ左式数 |\n|---|---|---|---|\n'+'\n'.join(f"| {x['batch']} | {','.join(map(str,x['pages']))} | {x['scope']} | {len(x['surface_tensor_left_sides'])} |" for x in index)+'\n\n19个编号式：'+', '.join(tags)+'。\n\n4a全对称、4a简并、4b简并、4c简并各27个分量；5a共14项、5b共30项、5e共26项。无分量的偏振组合明确保留“无”。总计178个表内χ左式，不计正文引用或译者注。\n',encoding='utf-8')

issues=root/'翻译管理/疑难与勘误.md'
with issues.open('a',encoding='utf-8') as h:
    for q in range(139,146):
        notes=[]
        for s in texts:
            notes += [line for line in s.splitlines() if line.startswith('>') and f'Q{q}' in line]
        h.write(f'\n\n## Q{q}｜4.2原文疑点\n\n状态：待核验。原式保留，候选未采用。\n\n'+'\n\n'.join(notes)+'\n')

(out/'局部约定卡.md').write_text('''# 4.2局部约定卡（全节更新，2026-10-21）

- N为ab/xy交线轴；沿旋转轴负侧看向正侧，顺时针为正。依次绕c、N、z旋转，使abc与xyz重合；φ∈[0,2π)，θ∈[0,π)，χ∈[0,2π)。负θ等价三元组按原文保留。
- 表面z向基板内部；甲基c轴从C朝三个H。内部旋转φ，外向法线倾斜角θtilt，面内取向χip；公式欧拉角θ=π−θtilt、χ=π+χip。第5部分叙述χ又指χip，已就地标明。
- 键系ξ/η/ζ、甲基分子系a/b/c、表面系x/y/z不混用。β为分子一阶超极化率（二阶场响应），表面χ为二阶非线性极化率；U为坐标变换系数。张量下标顺序为SFG、VIS、IR。
- θ的平方/立方与倍角须分别核；φ、χ在公式表中的2φ/3φ/2χ/3χ为倍角。
- 4a简并上/下号对应deg,a与deg,b；4b自由内部旋转；4c旋转冻结且三个H等价；第5部分以4c为条件，不与4b混用。
- 第5d的α、β为几何角，β不表示超极化率；director指镜面与表面的交线。
- 第6、7部分c为光速，θi/θr/θt为入射/反射/折射角，不是分子欧拉角。L、n′及原文符号疑点不按其他章静默统一。
- Q138—Q145均保留原式或原陈述，候选未采用。括号配对只作已明示的排版整理，不改变项的分组。
''',encoding='utf-8')
with (out/'结构与复用核验表.md').open('a',encoding='utf-8') as h:h.write('\n\n## 全节完成（2026-10-21）\n\nB277—B294覆盖原PDF全19页，七正文部分齐备，4a—4d及5a—5e均逐组核对。19个编号式及178个表内χ左式已建立覆盖索引；旧译中幂次误作倍角、符号误写、选择规则反译、漏掉条件等已修复。Q138—Q145未决，无原文公式修正采用。\n')

p=root/'翻译管理/当前进度与续接.md'
s=p.read_text(encoding='utf-8');p.write_text('# 当前进度与续接\n\n## 当前有效状态：4.2全节译校完成（2026-10-21）\n\nB277—B294覆盖全部19页、七正文部分，含4a—4d及5a—5e。19个编号式和178个表内χ左式已核覆盖；恢复θ幂次与倍角、β/χ及ξ/η/ζ、模式条件和原文末尾说明。Q138—Q145均保留原式并就地说明，无原文公式修正采用。最终验收见4.2整节完成复核。\n\n下一批B295：进入4.3，先核原题、结构、坐标与CH₂局部约定，不直接继承4.2角度及选择规则。以下为历史记录。\n\n'+s.split('\n',1)[1],encoding='utf-8')

p=root/'翻译管理/章节清单.tsv'
rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['编号']=='4.2':
        row.update({'状态':'本轮全节页面对照及排版整理完成；原文疑点未决','映射核验':'全19页按B277—B294逐页对照','公式图表范围':'19个编号式、178个表内χ左式及全部无编号定义已覆盖','导读状态':'已依据核验正文更新节首、Preface及第四章阅读导航','导读草案':'由欧拉角与甲基取向进入分子/表面张量，区分自由旋转与冻结取向，再按表面对称求响应，最后连接表面电场、极化及反射透射场。'})
with p.open('w',encoding='utf-8',newline='') as h:
    w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md'
s=p.read_text(encoding='utf-8').split('## 后续')[0]
s+='''## 4.2 CH₃基团的取向与和频张量

[进入4.2](4.2%20CH₃基团的取向与和频张量.md)。全部19页本轮译校完成。

第1、2部分建立欧拉角和甲基取向；第3部分由单个CH键得到分子张量；第4部分列一般式并处理自由旋转、冻结旋转和H原子等价性；第5部分按面内随机或表面对称取向求分量；第6、7部分依次连接表面场、和频极化与出射场。详细概括见节首。

19个编号式、178个表内χ左式均有覆盖记录。Q138—Q145保留待核，使用表格时须保留模式及取向条件。

## 后续

下一批B295进入4.3，先核原题、结构及CH₂局部坐标。4.3及其后各节仍待本轮校订。
'''
p.write_text(s,encoding='utf-8')

p=root/'Preface序言.md';s=p.read_text(encoding='utf-8')
s=re.sub(r'(?m)^- \[4\.2 .*$',lambda m:m[0].split('](')[0].replace('CH₃ 的取向与张量分量','CH₃基团的取向与和频张量')+']('+m[0].split('](')[1].split(')')[0]+')（全节译校完成）：由欧拉角和甲基取向建立分子与表面张量，区分自由旋转和冻结取向，按表面对称选择分量，再连接表面电场、和频极化与出射场；原文疑点就地保留。',s)
s=re.sub(r'### 4\.2本轮阅读提示[\s\S]*$', '### 4.2本轮阅读提示（2026-10-21）\n\n全19页及七个正文部分已完成本轮译校。阅读时先核角度定义，再选择自由旋转或冻结取向的相应张量表，最后通过第6、7部分连接表面场与出射场。节首有逐部分概括；Q138—Q145原文疑点仍保留待核。\n',s)
p.write_text(s,encoding='utf-8')
for name,addition in [
 ('翻译管理/符号与约定.md','## 4.2约定补充（2026-10-21）\n\n表面z指向基板内部，倾斜角以外向法线计量；θ=π−θtilt、χ=π+χip。第5部分叙述χ与公式欧拉角χ须区分。键系ξ/η/ζ，分子系a/b/c，表面系x/y/z。φ为内部旋转；5d的β是几何角。模式条件、θ幂次与倍角、以及第6/7部分光速c和光学角度详见4.2局部约定卡。'),
 ('翻译管理/分批执行与质量控制.md','## 4.2全节完成及续接（2026-10-21）\n\nB277—B294覆盖全19页，以完整定义、偏振公式组与表面对称条件分批。19个编号式与178个表内χ左式建立索引。下一批B295进入4.3，独立核原题和CH₂局部坐标；不跨节继承取向条件。'),
 ('中文版本/附件/原文勘误表.md','## 4.2本轮状态（2026-10-21）\n\n全19页已完成译校。Q138—Q145均保留原式或原陈述，候选未采用，暂无新增原文公式修正条目。原表定界符配对仅作已明示的排版整理，不改动分组项；旧译幂次、符号、条件及选择规则修复归校订记录。')]:
    with (root/name).open('a',encoding='utf-8') as h:h.write('\n\n'+addition+'\n')

renderer=(out.parent/'4.1/检查全节排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.1','校订记录/4.2').replace("startsWith('4.1 ')","startsWith('4.2 ')").replace('2026-10-20','2026-10-21')
(out/'检查全节排版.cjs').write_text(renderer,encoding='utf-8')
print(json.dumps({'numbered':len(tags),'table_components':count,'batches':[(x['batch'],len(x['surface_tensor_left_sides']))for x in index]},ensure_ascii=False))

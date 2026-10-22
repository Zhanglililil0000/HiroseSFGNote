from pathlib import Path
import json,hashlib,csv,io,re
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.3 CH₂基团的取向与和频张量.md'
old=target.read_text(encoding='utf-8')
(out/'B295前旧译.md').write_text(old,encoding='utf-8')
head=r'''# 4.3 CH₂基团的取向与和频张量

> 原作：广瀬千秋（广濑千秋）；中文翻译：章力。本轮校订日期：2026-10-21。
> 底本：`日语原版/Chapter4/chap4-3.pdf`，共26页。B295—B296已对照PDF p1—3，完成原目录、引言及第1、2部分；第3部分起仍为旧译待核。

## 原文目录

| 内容 | 原目录页码 |
|---|---|
| 1. 欧拉角 | 1 |
| 2. 亚甲基的取向与欧拉角 | 2 |
| 3. 亚甲基的β（分子固定系） | 3 |
| 4. 取向亚甲基的β（表面固定系） | 4 |
| 4a. 一般式 | 4 |
| 4b. 自由旋转、随机扭转角 | 10 |
| 4c. 两个H原子等价时（旋转被冻结） | 13 |
| 5. 表面取向造成的和频张量差异 | 16 |
| 5a. 随机（二维）取向表面的和频张量 | 17 |
| 5b. C₃ᵥ取向表面的和频张量 | 19 |
| 5c. C₄ᵥ、C₆ᵥ取向表面的和频张量 | 21 |
| 5d. Cₛ取向表面的和频张量 | 21 |
| 5e. C₂ᵥ取向表面的和频张量 | 22 |
| 6. 从表面电场到和频极化 | 25 |
| 7. 从和频极化到和频电场 | 25 |

> **译者注（目录与符号）：** 第3、4部分标题中的β在原目录分别带$abc$、$xyz$下标，表示相应坐标系中的分量。分子β沿用项目命名“一阶超极化率”，对应二阶场响应。以上仅为原目录翻译，后续正文尚须逐组核验。

## 引言

本文记述从亚甲基中的CH₂或乙烯基中的CH₂的和频光谱中，获得CH₂基团取向信息时所需的事项。第1部分的内容与CH₃基团文件中的记述重复。

'''
previous=(out.parent/'4.2/B277-本批译文.md').read_text(encoding='utf-8')
section=previous[previous.index('## 1. 欧拉角'):previous.index('> **译者注（原文疑点Q138')]
note=r'''> **译者注（原文疑点Q146，PDF p2）：** 原式求和号未标范围，式后写作$(i,j,k=a,b,c)$；前文则说要得到$(xyz)$系分量。与第4.2节Q138相同，候选为输出指标取$x,y,z$并对分子指标求和，尚未采用。$U$是变换系数；这里的$\chi$按原式保留，不改成后文的分子$\beta$。

> **译者注（本部分核验）：** 本部分虽与第4.2节重复，仍已单独对照本节PDF p1—2。$N$为交线轴；沿旋转轴负侧看向正侧，顺时针为正。旧译关于逆时针、旋转轴、角度名称及范围的混淆，以及原文没有的方向余弦、归一化等论断，均已按本节底本改正。
'''
b295=head+section+note
(out/'B295-本批译文.md').write_text(b295,encoding='utf-8')
b296=(out/'B296-本批译文.md').read_text(encoding='utf-8')
tail=old[old.index('## 3. 对称'):]
target.write_text(b295+'\n\n'+b296+'\n\n<!-- B296止；第3部分起为旧译待核，不视为本轮确认。 -->\n\n'+tail,encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-3.pdf').read_bytes()).hexdigest()
for n,pages,scope in [(295,[1,2],'原题、15条目录、引言及第1部分欧拉角'),(296,[2,3],'第2部分全部取向定义与式(2-1)')]:
    (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','date':'2026-10-21','pages':pages,'scope':scope,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
    (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n{scope}已对照原页。恢复旋转轴、正方向、角度范围和完整限定。旧译添加的物理说明未作为底本保留；未采用原文公式修正。Q146—Q148分别记录指标范围、残缺不等式及投影轴疑点。\n',encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 4.3局部约定卡（B295—B296）

- N为ab/xy交线轴。沿旋转轴负侧看向正侧，顺时针为正；依次绕c、N、z旋转使abc与xyz重合。φ∈[0,2π)，θ∈[0,π)，χ∈[0,2π)。
- 表面z指向基板内部；亚甲基c轴沿从C朝两个H的C₂轴，a轴在分子面内。尚未核验后文对分子面或键系的其他写法，不提前统一。
- φ为内部旋转，θtilt从外向法线计量，χip为面内取向。原2-1：θ=π−θtilt，χ=π/2+χip；与4.2的χ=π+χip不同。
- 两个CH等价时，φ与−φ数量相同；随机内部旋转与随机面内取向分别对应φ和χip。
- Q146—Q148均保留原式/原述；候选未采用。第3部分起旧译待核。
''',encoding='utf-8')
(out/'结构与复用核验表.md').write_text('''# 4.3结构与复用核验

原题：CH₂基团的取向与和频张量。底本26页；原目录15项，七个正文部分，第4部分分a—c，第5部分分a—e。目录所列起始页已转录，后续实际页界按批次核对，不能按目录视为正文完成。

B295—B296已核p1—3至第2部分末。第1部分与4.2重复，但已单独逐段核验；第2部分面内取向与欧拉角的偏移不同，须保留。

下一批B297核第3部分p3—4：键系ξ/η/ζ、CH(1)/CH(2)变换、四面体及sp²角的三角函数、分子β张量和模式归属。旧译的幂次和根式不能直接复用。
''',encoding='utf-8')
p=root/'翻译管理/疑难与勘误.md'
with p.open('a',encoding='utf-8') as h:
    for q in range(146,149):
        lines=[x for x in (b295+'\n'+b296).splitlines() if x.startswith('>') and f'Q{q}' in x]
        h.write(f'\n\n## Q{q}｜4.3原文疑点\n\n状态：待核验。原式/原述保留，候选未采用。\n\n'+'\n'.join(lines)+'\n')
p=root/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text('# 当前进度与续接\n\n## 当前有效状态：B295—B296完成4.3前两部分（2026-10-21）\n\n已核26页底本原题、15条目录、引言及p1—3第1、2部分。恢复欧拉角与亚甲基局部坐标；原2-1的χ=π/2+χip与4.2的偏移不同，明确保留。Q146—Q148待核，未采用原文公式修正。第3部分起仍为旧译待核。\n\n下一批B297：p3—4第3部分，先核键系、根式及θ的幂与倍角，再核分子β和模式归属。以下为历史记录。\n\n'+s.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for r in rows:
    if r['编号']=='4.3':r.update({'暂定中文标题':'CH₂基团的取向与和频张量','状态':'B295—B296已核目录、引言及第1/2部分；第3部分起旧译待核','映射核验':'原题与26页底本确认；p1—3至第2部分已核','公式图表范围':'第1部分无编号变换式及2-1已核；Q146—Q148待核','导读状态':'依据已核前两部分更新，后续概括待核正文'})
with p.open('w',encoding='utf-8',newline='') as h:
    w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';s=p.read_text(encoding='utf-8');s=s[:s.index('## 后续')]+'''## 4.3 CH₂基团的取向与和频张量（校订中）

[进入4.3](4.3%20CH₂基团的取向与和频张量.md)。B295—B296完成原目录、引言及第1、2部分：先核欧拉角，再定义亚甲基内部旋转、倾斜与面内取向。式(2-1)采用χ=π/2+χip，区别于4.2。Q146—Q148保留待核。

## 后续

下一批B297处理4.3第3部分的键系与分子张量；第3部分起仍为旧译待核。
''';p.write_text(s,encoding='utf-8')
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8');s=re.sub(r'(?m)^- \[4\.3 .*$',lambda m:m[0].split('](')[0].replace('CH₂ 的取向与张量分量','CH₂基团的取向与和频张量')+']('+m[0].split('](')[1].split(')')[0]+')（前两部分已译校）：先明确欧拉角与亚甲基取向，区分内部旋转、倾斜与面内取向；原2-1的角度偏移与4.2不同。第3部分起仍为旧译待核。',s);p.write_text(s,encoding='utf-8')
for filename,txt in [('符号与约定.md','4.3前两部分：表面z向基板内部，c为亚甲基C₂轴；θ=π−θtilt、χ=π/2+χip（原2-1），与4.2的χ偏移不同。内部φ与面内χip分开。Q146—Q148保留待核。'),('分批执行与质量控制.md','B295—B296完成4.3原目录、引言及前两部分，跨页定义完整处理。B297续p3—4第3部分；旧译根式、希腊字母及θ幂次须逐项核验。')]:
    with (root/'翻译管理'/filename).open('a',encoding='utf-8') as h:h.write('\n\n## 4.3开始（2026-10-21）\n\n'+txt+'\n')
renderer=(out.parent/'4.2/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.2','校订记录/4.3').replace("startsWith('4.2 ')","startsWith('4.3 ')")
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print('B295—B296正文及管理记录已更新')

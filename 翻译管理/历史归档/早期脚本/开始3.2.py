from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parent.parent
out=root/'翻译管理/校订记录/3.2'
out.mkdir(exist_ok=True)
target=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
old=target.read_text(encoding='utf-8')
(out/'B228前旧译.md').write_text(old,encoding='utf-8')
start=old.index('$$')
end=old.index('**L 系数、电场振幅**')
formulas=old[start:end].strip()
# 每组关系拆行仅调整排版，不更改数学内容。
formulas=formulas.replace(', \\quad\n',', \\quad\n')
intro='''# 3.2 双层膜和频的一般式

> 原作：广瀬千秋（广濑千秋）
> 中文翻译：章力；本轮校订日期：2026-10-20。
> 底本：`日语原版/Chapter3/chap3-2.pdf`，共13页。B228已核第1页开篇及反射、透射系数组；L系数起仍为旧译待核。

## 阅读导引与校订范围

本节以矩阵级数整理二层系的多重反射。按原文文本层初查，第1部分为系数（p1—2），第2部分为二层系的和频：2.1概述（p2—4），2.2详论（p4—13）。后续单元的公式、页界及符号含义须逐页复核；以下未校订部分不能视为已验收。

## 引言

作为文件《膜产生的和频过程》的延伸，这里求出膜层数为两层时的表达式。（三层及以上会涉及张量的级数，过于复杂。）

## 1. 系数等

### 反射系数与透射系数

将电场表示为表面固定坐标系中的分量时，利用下列反射系数与透射系数关系来表示各坐标分量。

> **译者注（局部约定）：** 此处的$r$、$t$分别为电场振幅反射系数和透射系数。$s$、$p$标记偏振，$x$、$y$、$z$标记坐标分量；$z$分量与$p$偏振的反射系数之间保留原文的负号。不将它们改称光强反射率或透射率。

'''
batch=intro+formulas+'\n'
(out/'B228-本批译文.md').write_text(batch,encoding='utf-8')
target.write_text(batch+'\n<!-- B228止；以下为旧译待核 -->\n\n> **校订状态：** 从以下L系数定义起，尚未完成本轮逐页校订。\n\n'+old[end:],encoding='utf-8')
digest=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest()
record=dict(batch='B228',date='2026-10-20',pages=[1],units='原题、引言及9组无编号反射/透射关系',source_sha256=digest,source_images_visually_checked=True,source_formula_corrections_adopted=False,next='B229：L系数定义、方向与公共因子；接完整p1—2的L系数组')
(out/'B228-覆盖.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'B228.md').write_text('''# B228 校订记录

已逐项对照PDF p1图像核验开篇与9组无编号反射/透射关系，包括s/p分母、x/y/z转换、z反射负号、四组透射角度比及两组乘积恒等式。旧译此组数学内容可复用；修订中文表述并明确振幅系数含义。无原文公式修正采用，无新增已确认勘误。

原题为“二层膜产生的和频（SFG）光——一般式”，正文题名调整为“双层膜和频的一般式”，保留既有文件路径。全文未完成，不以旧译段落作为已核验语料。
''',encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 3.2 局部约定卡

- B228已核：表面固定坐标；s/p与x/y/z不可互换；z分量反射系数为相应p偏振系数的负值。r/t为电场振幅系数。
- 待核：L的方向、公共因子与界面薄片标记；a、b与α、β、γ的不同含义；a₀、b₀上星号的非共轭约定；矩阵E的单位矩阵含义、Z行列式、δ的局部定义。
- 3.1的符号与验收结论不得自动继承。以上待核项仅为文本层检索提示。
''',encoding='utf-8')
(out/'结构与复用核验表.md').write_text('''# 3.2 结构与复用核验表

底本13页。文本层初查：1.系数等p1—2；2.二层系(1/m′/m/2)的和频，自p2开始；2.1概述p2—4；2.2详论p4—13。此结构为分批定位，后续页界与全部公式须视觉核验。

| 单元 | 状态 | 批次 |
|---|---|---|
| 原题、引言、反射/透射9组关系，p1 | 已对照原页 | B228 |
| L定义与完整系数组，p1—2 | 旧译待核 | 下一批B229 |
| 2.1概述，p2—4 | 旧译待核 | 待分批 |
| 2.2详论，p4—13 | 旧译待核 | 待分批 |

旧译快照另存B228前旧译.md。不得用全节文本缓存代替公式图像核验。
''',encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'
s=progress.read_text(encoding='utf-8')
s=s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B228开始3.2（2026-10-20）\n\n已完成3.2原题、引言与PDF p1反射/透射9组无编号关系的页面对照。13页结构初查与局部约定卡已建；正文L系数起明确标为旧译待核。未采用原文公式修正，无新增已确认勘误。\n\n下一批B229：核L定义、上下方向、公共因子及p1—2完整L系数组；接完后再进入2.1矩阵定义。a/b、星号、δ等不得直接继承3.1。以下为历史记录。\n',1)
progress.write_text(s,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'
s=nav.read_text(encoding='utf-8').replace('[进入旧译](3.2%20双层膜和频的一般式.md)。13页，尚待本轮校订；下一步先核结构与局部定义。','[进入3.2](3.2%20双层膜和频的一般式.md)。13页；B228已核原题、引言及p1反射/透射关系。L系数起仍待校订，下一批核其定义与完整系数组。')
nav.write_text(s,encoding='utf-8')
# 同步清单的状态栏，保留其余全书调查数据。
listing=root/'翻译管理/章节清单.tsv'
lines=listing.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    if line.startswith('3.2\t'):
        cols=line.split('\t')
        cols[7]='本轮校订中：B228已核开篇与p1反射/透射关系；其余待核'
        lines[i]='\t'.join(cols)
listing.write_text('\n'.join(lines)+'\n',encoding='utf-8')
renderer=(root/'翻译管理/校订记录/3.1/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/3.1','校订记录/3.2').replace("startsWith('3.1 ')","startsWith('3.2 ')")
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print(json.dumps(record,ensure_ascii=False))

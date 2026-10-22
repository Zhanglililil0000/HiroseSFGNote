from pathlib import Path
import re,json,hashlib,csv,io
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.5 两个CH₃基团的张量分量.md'
snap=out/'B323前旧译.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snap.read_text(encoding='utf-8')
texts=[(out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(323,326)]
target.write_text('\n\n'.join(texts)+'\n\n<!-- B325止；第5部分及后续均为旧译待核，不视为本轮确认。 -->\n\n'+old[old.index('## 5. '):],encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-5.pdf').read_bytes()).hexdigest()
scopes=[(323,[1],'原题、原目录及第1部分绪论'),(324,[1,2],'第2部分两级坐标、内部旋转角、欧拉角及三角恒等式'),(325,[2,3],'第3部分振动谱带、共线极限排除及第4部分对称分类')]
for n,pages,scope in scopes:
 c={'batch':f'B{n}','date':'2026-10-21','pages':pages,'scope':scope,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False}
 (out/f'B{n}-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
 (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n{scope}已对照原页。旧译存在擅增应用场景、两级坐标混淆、将简并模式改为弯曲模式及对称分类错列，本批按原述重译；不沿用未核验张量表。Q168—Q170保留原述并就地说明，未采用原文修正。\n',encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 4.5局部约定卡（B323—B325）

- 甲基固定系为小写abc；双甲基基团固定系为小写xyz；空间固定系为大写XYZ。前两级的变换不是表面/空间取向变换。
- c沿甲基C₃轴从C朝H；z沿两条C₃轴角平分线从X指向甲基；x位于两轴所成平面内。
- α为CXC角一半，φA、φB为两个甲基各自内部旋转角；不能解释为两个CH键角。φ=0时三角形顶点朝表面，φ=π时一边靠近表面。
- 从甲基到基团固定系的欧拉角按原写为(χ,θ,φ)=(0,α,φ)或(π,α,φ)。原三元组未加A/B下标；b轴方向按该变换确定。
- 分子β为一阶超极化率，属于二阶场响应；单甲基的全对称/简并，与双甲基组合后的同相/反相要分开。不能把简并振动译作弯曲振动。
- θ的函数幂与倍角分别保留。后续空间固定系角度尚未核验，不套用4.4约定。
- Q168目录、Q169重复轴名与极限几何、Q170角度条件/群分类陈述保留原述待核。
''',encoding='utf-8')
(out/'术语卡.md').write_text('''# 4.5局部术语卡（B323—B325）

| 原文 | 中文 | 辨析 |
|---|---|---|
| (CH₃)₂X基 | (CH₃)₂X基团 | 双甲基模型，两个甲基也可空间分离 |
| 振動バンド | 振动谱带 | 不擅改为伸缩/弯曲分类 |
| 全対称／縮重モード | 全对称／简并模式 | 单甲基模式；组合后再区分同相与反相 |
| 対称／逆対称振動 | 对称／反对称振动 | 本段分别指同相与反相组合 |
| 内部回転 | 内部旋转 | 甲基绕其自身C₃轴旋转 |
| 軸性ベクトル | 轴矢量 | 原a₂扭转组合的描述，不擅换成坐标方向 |
| 置換・回転群 | 置换—旋转群 | 仅保留作者建议，未补充群论证明 |
''',encoding='utf-8')
(out/'结构与分批计划.md').write_text('''# 4.5结构与分批计划

底本78页，原题“(CH₃)₂X基团的处理”。目录含6个正文部分、第5部分5类旋转条件、第6部分4类表，以及附录A—F。目录页码先原样保留；正文/附录实际页界在处理时再逐项核验。

## 已完成

B323：p1原题、目录、绪论。B324：p1—2坐标与取向。B325：p2—3振动谱带及对称分类。三页已看页图，全部段落/条件覆盖；第3部分末段在p3，第4部分实际在p3，不按目录p2定位。

## 后续队列

1. B326从p3第5部分“自由旋转”开始，先核键系希腊下标、分子β及全对称/简并模式分组，再完成该条件的整组表。
2. 第5部分其余4类内部旋转逐类分批，完整保留每类的定义、相位约定、条件和模式表，不跨类省略重复式。
3. 第6部分先核大写XYZ的取向定义；每个取向条件再按模式及完整偏振分量组分批。
4. 附录A—F分别建立覆盖索引。正文与附录对应项逐项比较后才能复用，不能将原目录括号页码当成不同PDF页码制。
5. 全节结束才登记78页完成；此前正文以明确边界区分已校与旧译。每批同步疑难、局部约定、术语和续接，阶段结束再更新导读。

当前不以旧译表数推定原文工作量，也不因排版检查成功判定原文物理正确。
''',encoding='utf-8')
p=root/'翻译管理/疑难与勘误.md';s=p.read_text(encoding='utf-8')
for q in range(168,171):
 if re.search(rf'^## Q{q}\b',s,re.M):continue
 lines=[line for t in texts for line in t.splitlines() if line.startswith('>') and f'Q{q}' in line]
 assert lines,q
 s+=f'\n\n## Q{q}｜4.5原文疑点\n\n状态：待核验，原陈述保留，候选未采用。\n\n'+'\n\n'.join(lines)+'\n'
p.write_text(s,encoding='utf-8')
p=root/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8');marker='## 当前有效状态：B323—B325完成4.5第1—4部分（2026-10-21）'
if marker not in s:p.write_text('# 当前进度与续接\n\n'+marker+'\n\n已核78页底本原题、目录及PDF p1—3第1—4部分。两级分子坐标及空间固定系已区分；恢复全对称/简并及同相/反相的分类，修复旧译错误对称性表。Q168—Q170保留原述并加注，未采用原文修正。第5部分及附录仍为旧译待核。\n\n下一批B326：p3第5部分“自由旋转”，核全对称及简并模式的完整分子β表，先确认希腊键系下标及近似条件。4.5结构与分批计划见校订记录目录。以下为历史记录。\n\n'+s.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for r in rows:
 if r['编号']=='4.5':r.update({'状态':'本轮校订中：B323—B325完成第1—4部分；其后旧译待核','映射核验':'原目录及PDF p1—3已核；第4部分实际位于p3','公式图表范围':'已核第2部分三角恒等式及第4部分6类对称条件；第5部分表待核','导读状态':'已更新前三页导读、Preface及第四章导航；后续随进度补充','导读草案':'先定义两个甲基的局部坐标及内部旋转，区分单甲基模式与双甲基同相/反相组合，再按内部旋转分类对称性；后续张量表待核。'})
with p.open('w',encoding='utf-8',newline='') as h:
 w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';s=p.read_text(encoding='utf-8');s=s[:s.index('## 后续')]+'''## 4.5 (CH₃)₂X基团的处理（校订中）

[进入4.5](4.5%20两个CH₃基团的张量分量.md)。B323—B325完成原题、目录及第1—4部分（PDF p1—3）。先明确甲基abc、基团xyz和空间XYZ的层级，再区分全对称/简并与同相/反相模式，最后查看内部旋转对应的对称分类。原Q168—Q170保留待核。

## 后续

下一批B326进入4.5第5部分“自由旋转”，从完整分子β表开始。4.5共78页，第5部分以后及附录A—F仍为旧译待核。
''';p.write_text(s,encoding='utf-8')
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8')
s=re.sub(r'(?m)^- \[4\.5 .*$',lambda m:'- [4.5 (CH₃)₂X基团的处理]('+m[0].split('](')[1].split(')（')[0]+')（第1—4部分已译校）：先建立甲基与基团坐标及内部旋转角，再区分全对称/简并模式的组合与相对取向对称分类；后续分子、空间张量及附录待核。',s)
# Preserve the exact existing target, including its literal parentheses, when rewriting the link.
s=re.sub(r'(?m)^- \[4\.5 .*$', '- [4.5 (CH₃)₂X基团的处理](中文版本/第四章%20单层膜与多层膜的和频/4.5%20%28CH3%292X型分子的SFG.md)（第1—4部分已译校）：先建立甲基与基团坐标及内部旋转角，再区分全对称/简并模式的组合与相对取向对称分类；后续分子、空间张量及附录待核。',s)
p.write_text(s,encoding='utf-8')
for filename,txt in [('翻译管理/符号与约定.md','## 4.5初始约定（B323—B325）\n\nabc为甲基固定系、xyz为双甲基基团固定系、XYZ为空间固定系；α为CXC半角，φA/φB为内部旋转角。不得将简并模式译成弯曲模式。Q168—Q170保留原述，后续空间角度另核。'),('翻译管理/分批执行与质量控制.md','## 4.5启动（B323—B325）\n\n78页底本按完整条件及公式组分批。本轮只完成p1—3第1—4部分；B326续p3第5部分自由旋转。详细队列见4.5结构与分批计划，不将旧译尾部计入本轮完成。'),('中文版本/附件/原文勘误表.md','## 4.5阶段状态（B323—B325）\n\n已核p1—3第1—4部分。Q168—Q170保留原陈述，候选未采用；本阶段无新增已采用的原文修正。翻译中的坐标层级、简并模式及对称表误译已按原文修复，归校订记录。')]:
 p=root/filename;s=p.read_text(encoding='utf-8')
 if txt.split('\n')[0] not in s:p.write_text(s+'\n\n'+txt+'\n',encoding='utf-8')
renderer=(out.parent/'4.4/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.4','校订记录/4.5').replace("startsWith('4.4 ')","startsWith('4.5 ')")
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print('B323—B325已合并，管理记录已更新；旧译尾部保留明确边界。')

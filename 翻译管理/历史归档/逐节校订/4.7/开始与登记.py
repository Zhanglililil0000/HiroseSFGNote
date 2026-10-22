from pathlib import Path
import re,json,hashlib,csv,io
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.7 CH₂、平面HCCH及扭转HCCH的和频张量.md'
snap=out/'B365前旧译.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snap.read_text(encoding='utf-8')
texts=[(out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in [365,366]]
tail=old[old.index('### 3. 实验室固定'):]
target.write_text('\n\n'.join(texts)+'\n\n<!-- B366止；第3部分及后续旧译待核。 -->\n\n> **校订进度：** 以下第3部分及后续为旧译待核，尚未纳入本轮验收。\n\n'+tail,encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-7.pdf').read_bytes()).hexdigest()
asset=root/'中文版本/assets/4.7-p1-diamond-models.png'
for n,pages,scope in [(365,[1,2],'原题、局部导读、原结构图及完整第1部分绪论'),(366,[2],'第2部分三级坐标、分子轴与三个取向角')]:
 c={'batch':f'B{n}','date':'2026-10-21','pages':pages,'scope':scope,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False,'independent_figures':1 if n==365 else 0}
 (out/f'B{n}-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
 (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n{scope}，对照PDF p'+','.join(map(str,pages))+'。恢复原题中平面/扭转HCCH与CH₂的伸缩主题；旧译漏图已补回，原生RGB图像直接提取，不重绘。修复位阻存在的语气、CH₂避让机制被合并等译文问题。原图标签、尺寸数值与引用保留；Q180原称保留待核，未采用原文修正。\n',encoding='utf-8')
(out/'图像来源.json').write_text(json.dumps({'asset':str(asset.relative_to(root)),'source_pdf':'日语原版/Chapter4/chap4-7.pdf','page':1,'object':'IMcpdf0','original_pixels':[827,295],'method':'直接解码原嵌入RGB图像，未重绘','sha256':hashlib.sha256(asset.read_bytes()).hexdigest(),'caption':'(a) Diamond (100)-2x1; (b) Diamond (100)-1x1'},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 4.7局部约定卡（B365—B366）

- 主题含CH₂、平面HCCH(C₂ᵥ)及扭转HCCH(C₂)的和频张量，绪论讨论CH伸缩；旧文件名“CH₂弯曲振动”不作主题依据。
- monohydride为单氢化模型，CH单元配对成HCCH；dihydride为双氢化模型，对应CH₂。原生图1的(a)/(b)及重构2×1/未重构1×1标签保持。
- 分子固定abc、表面固定xyz、空间/实验室固定XYZ分开；CH₂及HCCH的c沿C₂轴向外，平面形a在分子面内，扭转形a按平分两个CCH面的参考面。
- φ为ac参考面相对于表面的扭转；θ=π−θtilt，χ=π/2+χip；z指向基板内部，外向法线为−z。面内随机和内部旋转随机分别定义。
- 原CCC面及扭转HCCH仍称ac为分子面的用语保留见Q180。后续τ另有局部定义，尚未核验，不能将θ/φ与τ互换。
- 第3部分χ还用作表面到实验室的方位旋转角，与前段欧拉χ的关系须随表核验。第3部分起旧译未确认。
''',encoding='utf-8')
(out/'术语卡.md').write_text('''# 4.7局部术语卡（B365—B366）

| 原文 | 本阶段译法 | 说明 |
|---|---|---|
| as cut表面 | 切割所得表面 | 原英文首次保留，与重构表面区分 |
| ダングリングボンド / dangling bond | 悬挂键 | 沿用旧译，不在此新增全书同义译法 |
| monohydride / dihydrideモデル | 单氢化／双氢化模型 | 首次保留英文，按每个表面C的氢化数理解 |
| 再構成表面 | 重构表面 | 原图(a)2×1 |
| 立体障害 | 位阻 | 旧译“立体障碍”本节统一为位阻，未据此重写其他章节 |
| 平面形／ねじれ形HCCH | 平面／扭转HCCH | C₂ᵥ／C₂条件分别保留 |
| 面内配向角 | 面内取向角 | χip与欧拉χ分开 |

响应系数命名沿用既定术语。新模型词保留英文便于后续集中审校。
''',encoding='utf-8')
(out/'结构与分批计划.md').write_text('''# 4.7结构与分批计划

底本24页。已看p1—3页图并核第1、2部分；p24仅已渲染，未据此登记完成。文本层定位：第3部分p3—11，第4部分p11—13，第5部分p13—16，附录A p16—24；后续实际页界须逐页图再核。

## 已完成

B365覆盖p1—2完整绪论、原题及原生结构图。B366覆盖p2第2部分三级坐标与三个角。图像直接从PDF嵌入对象提取，源像素827×295，无重绘。已发现原文CCC面/分子面用语歧义Q180，保留待核。

## 后续顺序

1. B367：p3第3部分引言及表(3a-1)，倾斜C₂ᵥ对称伸缩的27行×3个角度列。逐格核函数幂、τ、±号与χ列，不套旧译倍角。
2. p4表(3a-2)及p5扭转C₂的(3b-1)/(3b-2)，各表独立完整核验；零与none按原写分别记录。
3. p6—8的±45°/±135°表逐模式、逐角列拆分，保留原列的正负号，不因表面形式相似而复用。
4. p9—11一般方位角表及第4部分取向关系；先核τ是二面角，避免与欧拉θ和HCH角混淆。
5. 第4、5部分按具体取向分批；附录A按C₂ᵥ/C₂、对称/反对称模式及完整27分量组处理。旧译附录末尾用“参阅原文”替代表项，必须补齐可编辑公式。
6. 全节完成后才更新24页完成；此前主译文旧译尾部有明确边界。同步疑点、符号及页图覆盖，不以公式可渲染替代理论验证。
''',encoding='utf-8')
p=root/'翻译管理/疑难与勘误.md';s=p.read_text(encoding='utf-8')
if not re.search(r'^## Q180\b',s,re.M):
 note=next(line for line in texts[1].splitlines() if line.startswith('>') and 'Q180' in line)
 p.write_text(s+'\n\n## Q180｜4.7原文疑点\n\n状态：待核验，原称保留，候选未采用。\n\n'+note+'\n',encoding='utf-8')
p=root/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8');marker='## 当前有效状态：B365—B366完成4.7第1、2部分（2026-10-21）'
if marker not in s:p.write_text('# 当前进度与续接\n\n'+marker+'\n\n已核24页底本原题、p1—2完整绪论与坐标定义，补回原生表面结构图。主题为CH₂及平面/扭转HCCH的伸缩和频张量，已区分abc/xyz/XYZ与三个角；原Q180保留待核，未采用原文修正。第3部分及后续仍为旧译待核。\n\n下一批B367：p3第3部分引言与完整表(3a-1)，27分量×3个角度列，重点核函数幂、τ、±号及χ旋转定义。详见4.7结构与分批计划。以下为历史记录。\n\n'+s.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for r in rows:
 if r['编号']=='4.7':r.update({'暂定中文标题':'CH₂、平面HCCH及扭转HCCH的和频张量','状态':'本轮校订中：B365—B366完成第1、2部分；后续旧译待核','映射核验':'p1—2原题、图与第1/2部分已核；第3部分从p3开始','公式图表范围':'原生结构图1幅已恢复，三个角定义已核；后续张量表待逐格核验','导读状态':'已更新初始节首、Preface及第四章导航；后续随进度补充','导读草案':'比较氢化金刚石两种表面模型与位阻，定义CH₂及平面/扭转HCCH的坐标及取向；后续分角度、模式查表。'})
with p.open('w',encoding='utf-8',newline='') as h:
 w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';s=p.read_text(encoding='utf-8');s=s[:s.index('## 后续')]+'''## 4.7 CH₂、平面HCCH及扭转HCCH的和频张量（校订中）

[进入4.7](4.7%20CH₂、平面HCCH及扭转HCCH的和频张量.md)。B365—B366完成第1、2部分（PDF p1—2）并补回原生表面结构图。

先比较C(100)表面的单氢化/双氢化模型及位阻，再区分abc、xyz、XYZ和内部旋转/倾斜/面内取向角。Q180保留原称待核；第3部分起的取向张量表及附录仍为旧译待核。

## 后续

下一批B367进入p3第3部分，引言及完整表(3a-1)按角度列逐格核验。
''';p.write_text(s,encoding='utf-8')
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8');s=re.sub(r'(?m)^- \[4\.7 .*$',lambda m:'- [4.7 CH₂、平面HCCH及扭转HCCH的和频张量]('+m[0].split('](')[1].split(')')[0]+')（第1、2部分已译校）：比较氢化金刚石两种表面模型与位阻，定义分子、表面、空间坐标及取向角；原结构图已恢复，后续取向表与附录待核。',s);p.write_text(s,encoding='utf-8')
for filename,txt in [('翻译管理/符号与约定.md','## 4.7初始约定（B365—B366）\n\nabc为分子、xyz为表面、XYZ为空间固定系；z指向基板内部，θ=π−θtilt、χ=π/2+χip。CH₂与平面HCCH为C₂ᵥ，扭转HCCH为C₂。原CCC面及扭转形ac面用语见Q180；后续τ和实验室旋转χ尚须局部核验。'),('翻译管理/分批执行与质量控制.md','## 4.7启动（B365—B366）\n\n底本24页，本轮完成p1—2第1、2部分和1幅原生结构图。B367续p3表(3a-1)，按27行及角度列逐格核验；旧译幂/倍角错误及附录摘要替代表项须后续独立修复。详见4.7结构与分批计划。'),('中文版本/附件/原文勘误表.md','## 4.7阶段状态（B365—B366）\n\n第1、2部分已核。Q180原CCC面及分子面称法保留，候选未采用，无新增已采用的原文修正。旧译漏图、题目及语气/机制表达的修复归校订记录。')]:
 p=root/filename;s=p.read_text(encoding='utf-8')
 if txt.split('\n')[0] not in s:p.write_text(s+'\n\n'+txt+'\n',encoding='utf-8')
renderer=(out.parent/'4.6/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.6','校订记录/4.7').replace("startsWith('4.6 ')","startsWith('4.7 ')")
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print('B365—B366译文、图像与阶段管理已更新')

from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent; root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8'); start=s.index('<!-- B235止；'); a=s.index('因此，若将经过',start); end=s.index('**$E^+$ sources**',a)
batch=s[a:end]
batch=batch.replace('因此，若将经过 $n$ 次反转的光在出口正下方的电场设为：','因此，将经历$n$次反转的光在出口正下方的电场写为：')
batch=batch.replace('则经过 $(n+1)$ 次反转的光在出口正下方的电场可表示为：','则经历$(n+1)$次反转的光在出口正下方的电场可写为：')
batch=batch.replace('由附录可知，当右边矩阵的幂收敛于零时，净电场（在有零次项贡献时）为以下形式：','根据附录，当右端矩阵的幂趋于零时，合成电场（存在零次项贡献时）为：')
batch=batch.replace('\\begin{pmatrix}','\\begin{bmatrix}').replace('\\end{pmatrix}','\\end{bmatrix}')
batch=batch.replace("+ t_{m'm} (\\alpha r_{m2}","\\\\\n&\\qquad + t_{m'm} (\\alpha r_{m2}")
# 第一行方括号在分行后仍保持同一完整代数和，不改因子。
batch=batch.replace('E_{\\text{net}}','E_{\\mathrm{net}}')
batch+='> **译者注（递推与收敛条件）：** 本段保留原文“矩阵的幂趋于零”及“存在零次项贡献”的条件，不能将式(2.11)视为不附条件的级数恒等式。$y_n$、$y_n\'$为两类路径的递推分量；本段公式统一使用$x$，但未显式解释前式的$x\'$，故Q117仍保留待核。\n\n'
(p/'B236-本批译文.md').write_text(batch,encoding='utf-8')
s=s[:start]+batch+'<!-- B236止；以下为旧译待核 -->\n\n> **校订状态：** 以下从$E^+$源的反射和频光及光路图起仍待本轮逐页校订。\n\n'+s[end:]
s=s.replace('B228—B235已核第1部分、2.1全部及2.2开篇至式(2.10)；其后递推关系起仍为旧译待核。','B228—B236已核第1部分、2.1全部及2.2递推和式(2.11)；其后光路图与式(2.12)起仍为旧译待核。')
f.write_text(s,encoding='utf-8')
rec=dict(batch='B236',date='2026-10-20',pages=[4,5],tags=['2.11'],units='n次电场、n+1递推三行、矩阵幂及完整两行逆矩阵求和式',source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False,unresolved_carried_forward=['Q117'],next='B237：p5—6的E+源反射光，保留7幅光路子图与图下因子，核式2.12')
(p/'B236-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'B236.md').write_text('''# B236 校订记录

核PDF p4末—p5上部：n次反转电场、n+1展开、递推矩阵乘列向量及矩阵n+1次幂；核2.11逆矩阵与伴随矩阵展开两行、分母1−α−β−γ+αγ及初值列。无遗漏跨页行，旧译此组数学可复用，调整分行及矩阵括号外形。

递推矩阵的非对角元乘积等于αβ，故I减该矩阵的行列式可化为原分母；伴随矩阵的对角交换与非对角反号符合二阶求逆规则。此为辅助一致性核对，不改写原式。保留矩阵幂趋零和零次项条件；无新增原文疑点或原文修正。Q117的x′关系在此仍未显式定义，不能据本段统一x而反向消除。

下一批B237必须保留p5七幅光路子图及图下表达式，不能沿用旧译的纯文字代码块代替图。接p6完整式2.12，并核作者省略外部连接因子的上下文。
''',encoding='utf-8')
card=p/'局部约定卡.md'; card.write_text(card.read_text(encoding='utf-8')+'\n- B236：递推矩阵按原式展开，yₙ/yₙ′为两类路径分量；使用逆矩阵求和附带矩阵幂趋零及零次项条件。此矩阵非2.1直接列出的X，不能只因行列式相同就互换矩阵元素。Q117继续未决。\n',encoding='utf-8')
structure=p/'结构与复用核验表.md'; t=structure.read_text(encoding='utf-8').replace('| 2.2递推关系及后文，p4—13 | 旧译待核 | 下一批B236起 |','| 2.2反转次数递推与逆矩阵，p4—5，式2.11 | 已对照原页 | B236 |\n| E+反射光路图及式2.12起，p5—13 | 旧译待核 | 下一批B237起 |'); structure.write_text(t,encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'; t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：B236完成3.2递推与式2.11（2026-10-20）\n\n已核p4—5的n次电场、n+1递推、矩阵幂及逆矩阵两行展开，保留收敛和零次项条件。无新增原式疑点或修正，Q117继续待核。\n\n下一批B237：p5—6的E+源反射和频光；保留7幅原光路子图并核图下因子，再接完整式2.12。旧译代码块不能替代原图。其后仍待校订。以下为历史记录。\n',1); progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'; t=nav.read_text(encoding='utf-8').replace('下一批接反转次数递推。','B236已核反转次数递推及式2.11；下一批核反射光路图及式2.12。'); nav.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'; t=listing.read_text(encoding='utf-8').replace('本轮校订中：B228—B235已核至2.2式2.10；递推关系及后文待核','本轮校订中：B228—B236已核至2.2递推及式2.11；光路图及后文待核'); listing.write_text(t,encoding='utf-8')
print(json.dumps(rec,ensure_ascii=False))

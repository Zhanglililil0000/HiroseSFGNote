from pathlib import Path
import json, hashlib, csv, io
out=Path(__file__).resolve().parent
root=out.parents[2]
f=root/'中文版本/第四章 单层膜与多层膜的和频/4.2 CH₃基团的取向与和频张量.md'
s=f.read_text(encoding='utf-8')
(out/'B277前旧译.md').write_text(s,encoding='utf-8')
tail=s[s.index('## 2. CH基团的坐标变换'):]
batch=(out/'B277-本批译文.md').read_text(encoding='utf-8')
f.write_text(batch+'\n<!-- B277止；第2部分起为旧译待核，不视为本轮确认。 -->\n\n'+tail,encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-2.pdf').read_bytes()).hexdigest()
(out/'B277-覆盖.json').write_text(json.dumps({'batch':'B277','date':'2026-10-21','pages':[1,2],'scope':'原目录、引言、第1部分欧拉角；第2部分未校订','source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'B277.md').write_text('''# B277校订记录

完成原目录16条、引言、第1部分（PDF p1—2上半）。修复旧译将N轴当角度、混淆c/z/N旋转轴、交换角度范围、错译共面/垂直关系及删改作者负θ括注的问题。恢复原文正旋转的观察方向及旋转顺序；不添加矩阵可消除歧义等原文没有的论断。

原目录的甲基、冻结旋转、扭转角、二维随机取向、表面电场→极化→电场均重新译出；标题从旧译泛称改为原题，保留文件路径。原式无编号，χ及U照原页恢复，指标范围疑点记Q138，未采用候选，未增加原文勘误条目。

下一批B278：第2部分p2—3，完整核内部旋转角φ、倾斜角θtilt、面内角χip与欧拉角的关系。第2部分起仍为旧译待核。
''',encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 4.2局部约定卡

- B277：N为ab/xy交线轴；从旋转轴负侧看向正侧，顺时针为正。依次绕c、N、z使abc与xyz重合；φ∈[0,2π)，θ∈[0,π)，χ∈[0,2π)。作者负θ的限定和等价三元组照录。
- 第2部分预核：表面z指向基板内部，倾斜角以外向法线计量；具体三角关系待B278核验。
- U是坐标分量变换系数。分子β称一阶超极化率（二阶场响应）；第1部分原式χ不改为β。
- Q138：原式输出指标范围为a,b,c，与前文xyz叙述不一致。原式保留，候选未采用。
''',encoding='utf-8')
(out/'结构与复用核验表.md').write_text('''# 4.2结构与复用核验

原PDF共19页，主题为CH₃基团的取向与和频张量。原目录含七个正文部分，其中第4部分分a—d、第5部分分a—e；起始页见已译目录。目录页码与实际标题位置将在各批逐项核对，不将目录核查当作全节完成。

B277已核原目录、引言及第1部分。旧译存在概念性误译，后续仅作待核参考，不能直接纳入已核验语料。分批以完整小部分、张量公式组为界；密集表格另批逐项检查。
''',encoding='utf-8')
p=root/'翻译管理/疑难与勘误.md'
with p.open('a',encoding='utf-8') as h:h.write('\n\n## Q138｜4.2第1部分张量变换式的指标范围（PDF p2）\n\n状态：待核验，原式保留，候选未采用。原式χ_ijk=ΣU_ijk:abc χ_abc，式后(i,j,k=a,b,c)；正文称输出为xyz系。候选输出指标x,y,z，求和对象为分子指标。原文未给求和范围，不据候选重写。U为变换系数，旧译将其称分子超极化率已修复。无原文修正采用。\n')
p=root/'翻译管理/当前进度与续接.md'
old=p.read_text(encoding='utf-8'); p.write_text('# 当前进度与续接\n\n## 当前有效状态：B277开始4.2（2026-10-21）\n\n已核19页底本的原题、目录及p1—2第1部分欧拉角。恢复N交线轴、正旋转、三次操作及角度范围；Q138保留原式，无原文修正采用。第2部分起仍为旧译待核。\n\n下一批B278：p2—3第2部分甲基取向及三角对应关系，先完整核局部坐标，勿沿用旧译。以下为历史记录。\n\n'+old.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv'
rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t')); fields=list(rows[0])
for row in rows:
    if row['编号']=='4.2':
        row['暂定中文标题']='CH₃基团的取向与和频张量'
        row['状态']='B277已核目录、引言与第1部分；第2部分起旧译待核'
        row['映射核验']='原题及19页底本确认；已对照p1—2第1部分'
        row['公式图表范围']='第1部分无编号张量变换式已核；Q138待核验'
with p.open('w',encoding='utf-8',newline='') as h:
    w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md'
with p.open('a',encoding='utf-8') as h:h.write('\n\n### 4.2本轮进度（2026-10-21）\n\n原题为《CH₃基团的取向与和频张量》。B277完成引言与第1部分：先核欧拉角的轴、正方向和旋转次序，再进入甲基与表面坐标的角度对应。第2部分以后仍为旧译待核。\n')
renderer=(out.parent/'4.1/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.1','校订记录/4.2').replace("startsWith('4.1 ')","startsWith('4.2 ')").replace('2026-10-20','2026-10-21')
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print('B277正文及管理记录已更新')

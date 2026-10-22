from pathlib import Path
import json,hashlib,csv,io,re
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.4 CH基团的取向与和频张量.md'
old=target.read_text(encoding='utf-8');(out/'B314前旧译.md').write_text(old,encoding='utf-8')
first=(out/'B314-本批译文.md').read_text(encoding='utf-8');second=(out/'B315-本批译文.md').read_text(encoding='utf-8')
tail=old[old.index('## 4. 实验室'):]
target.write_text(first+'\n\n'+second+'\n\n<!-- B315止；第4部分起为旧译待核，不视为本轮确认。 -->\n\n'+tail,encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-4.pdf').read_bytes()).hexdigest()
for n,pages,scope in [(314,[1,2],'原题、12条目录、引言及第1部分双原子/直线分子欧拉角'),(315,[2,3],'第2部分CH取向定义与第3部分分子张量')]:
    (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','date':'2026-10-21','pages':pages,'scope':scope,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
    (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n{scope}已对照原页。原题为CH取向，伸缩振动及轴对称的两参数说明已恢复。删除旧译自行添加的弯曲振动、三参数及不等价变换“结果等价”等论述；修复旋转轴、正方向、角度符号与范围。原Q160—Q162保留，未采用原文修正。\n',encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 4.4局部约定卡（B314—B315）

- 主题为CH基团取向，原第3部分讨论沿c轴的CH伸缩，不是弯曲振动。保留文件路径以维持链接。
- 双原子/直线分子轴对称时，a/b等价，内部φ不提供独立取向；两角θ/χ即可。原汇总φ=φ保留，不解释为第三独立参数。
- N为ab/xy交线，沿旋转轴负侧向正侧看，顺时针为正；旋转顺序绕c、N、z。φ∈[0,2π)，θ∈[0,π)，χ∈[0,2π)。
- 表面z指向基板内部；CH的c轴从C向H，θtilt从外向法线量起。θ=π−θtilt，χ=π+χip，与4.3的π/2偏移区分。
- 分子β称一阶超极化率（二阶场响应），βccc、βaac=βbbc。原第1部分χ及指标范围保留，不换成β。
- Q160未定义k，Q161输出指标范围，Q162原C₃/三个H及N几何定义，均保留原述待核。第4部分起旧译待核。
''',encoding='utf-8')
(out/'结构与复用核验表.md').write_text('''# 4.4结构与复用核验

原题：CH基团的取向与和频张量。底本10页；原目录12项，七个正文部分，第5部分分a—e。目录页码按原表转录，后续实际位置按批次核对。

B314—B315完成p1—3至第3部分末。旧标题与正文将CH伸缩/取向误作弯曲，前部已重译；后续公式中的θ与χ/φ混写、幂与倍角、漏掉偏振分量均须独立核验，不直接复用旧译。

下一批B316：p3—4第4部分，先核φ相关项如何消去、三角恒等式和完整27分量，再进入第5部分表面对称。
''',encoding='utf-8')
with (root/'翻译管理/疑难与勘误.md').open('a',encoding='utf-8') as h:
    for q in range(160,163):
        lines=[line for line in (first+'\n'+second).splitlines() if line.startswith('>') and f'Q{q}' in line]
        h.write(f'\n\n## Q{q}｜4.4原文疑点\n\n状态：待核验，原式或原述保留，候选未采用。\n\n'+'\n'.join(lines)+'\n')
p=root/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text('# 当前进度与续接\n\n## 当前有效状态：B314—B315完成4.4前三部分（2026-10-21）\n\n已核10页底本原题、12条目录、引言及p1—3第1—3部分。主题恢复为CH基团取向与伸缩响应；轴对称只需θ/χ两参数，原θ=π−θtilt、χ=π+χip保留。Q160—Q162待核，无原文修正采用。第4部分起仍为旧译待核。\n\n下一批B316：p3—4第4部分，核三角恒等式、φ消去说明及完整27分量。旧译(spp)有漏项，不直接复用。以下为历史记录。\n\n'+s.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for r in rows:
    if r['编号']=='4.4':r.update({'暂定中文标题':'CH基团的取向与和频张量','状态':'B314—B315已核目录、引言及第1—3部分；第4部分起旧译待核','映射核验':'原题与10页底本确认；p1—3至第3部分已核','公式图表范围':'前部无编号变换及β关系已核；Q160—Q162待核','导读状态':'据核验前部更新，后续概括待正文校订'})
with p.open('w',encoding='utf-8',newline='') as h:
    w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';s=p.read_text(encoding='utf-8');s=s[:s.index('## 后续')]+'''## 4.4 CH基团的取向与和频张量（校订中）

[进入4.4](4.4%20CH基团的取向与和频张量.md)。B314—B315完成原目录、引言及前三部分：先说明双原子/直线分子的轴对称为何只需两个取向角，再定义CH取向与分子β分量。正文讨论CH键伸缩，旧文件名暂保留。Q160—Q162待核。

## 后续

下一批B316核4.4第4部分一般张量式；第4部分起仍为旧译待核。
''';p.write_text(s,encoding='utf-8')
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8');s=re.sub(r'(?m)^- \[4\.4 .*$',lambda m:m[0].split('](')[0].replace('CH 的取向与张量分量','CH基团的取向与和频张量')+']('+m[0].split('](')[1].split(')')[0]+')（前三部分已译校）：先说明轴对称CH取向只需两个角，再定义表面/分子坐标与伸缩振动β分量；旧文件名暂保留，第4部分起旧译待核。',s);p.write_text(s,encoding='utf-8')
for name,txt in [('符号与约定.md','4.4前部：CH的c轴从C向H，表面z朝基板内部；θ=π−θtilt，χ=π+χip。轴对称不需独立内部角φ；原汇总行φ=φ仍保留。Q160—Q162原述未改，详见局部约定卡。'),('分批执行与质量控制.md','B314—B315完成4.4原目录、引言及前三部分。B316续p3—4第4部分完整27分量，逐项核旧译缺项及θ幂次，不将文件名当作主题依据。')]:
    with (root/'翻译管理'/name).open('a',encoding='utf-8') as h:h.write('\n\n## 4.4开始（2026-10-21）\n\n'+txt+'\n')
renderer=(out.parent/'4.3/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.3','校订记录/4.4').replace("startsWith('4.3 ')","startsWith('4.4 ')")
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print('B314—B315正文与管理记录已更新')

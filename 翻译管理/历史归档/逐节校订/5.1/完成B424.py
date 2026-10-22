from pathlib import Path
import json,csv,io,hashlib
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
p=o/'B424验收.json';d=json.loads(p.read_text(encoding='utf-8'));render=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));b=next(x for x in render['results'] if x['batch']=='B424')
assert b['scrollWidth']==b['width'] and not b['overs']
assert hashlib.sha256((o/'B424-本批译文.md').read_text(encoding='utf-8').encode('utf-8')).hexdigest()==d['translation_sha256']
assert hashlib.sha256((r/'中文版本/第五章 张量与对称性/5.1 和频张量与对称性.md').read_bytes()).hexdigest()==d['合稿SHA256']
d.update({'已排版':True,'数学语法检查':'本批34片段；累计57片段通过KaTeX严格检查','显示复核':'B424截图已视觉核对，编号及9行基底公式可读，无横向溢出','复核性质':'模型原页对照及原式内部一致性检查；不是独立物理审校'})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
p=o/'B424.md';t=p.read_text(encoding='utf-8');line='\n排版验收：本批34个数学片段、累计57个片段语法检查通过；B424截图已视觉核对，页面/内容宽度均1100，无横向溢出。Q200原式保留，候选未采用，故原文勘误附件无新增已采用项。\n'
if line not in t:p.write_text(t+line,encoding='utf-8')
p=r/'翻译管理/章节清单.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['编号']=='5.1':row.update({'状态':'翻译中：B423—B424完成p1及p2至式(2)原页对照与参考排版；表1起待译','映射核验':'已核p1及p2上半；表1起待逐项译校','公式图表范围':'p1四个无编号式；p2式(1a)—(1c)及式(2)九个基底分量已核；表1/表2尚未翻译','导读草案':'已译对称性约束引言、线性极化及1+3+5个不可约基底；C3v特征标表和后续附录待译校。'})
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
p=o/'结构与分批计划.md';t=p.read_text(encoding='utf-8').replace('| 后续批次待登记 | p2上半 | 电场/基底定义、式(1a)—(1c)及式(2) | 待翻译 |','| B424 | p2上半 | 电场/基底定义、式(1a)—(1c)及式(2) | 已译、原页对照及排版验收通过 |').replace('后续批次从B424起顺序登记','后续批次从B425起顺序登记');p.write_text(t,encoding='utf-8')
p=r/'中文版本/第五章 张量与对称性/阅读导航.md';t=p.read_text(encoding='utf-8').replace('已完成PDF p1（B423），介绍指标数、不可约角动量阶数，以及对称性对极化率张量的约束。p2—7仍待翻译','已完成PDF p1及p2上半至式(2)（B423—B424），涵盖对称性约束、线性极化的三个分量及九个不可约基底的定义。p2表1起仍待翻译').replace('疑点Q198、Q199','疑点Q198—Q200');p.write_text(t,encoding='utf-8')
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8').replace('（翻译中，p1/7已对照）：从指标数及不可约角动量阶数入手，说明对称性对极化率张量的约束；后续C₃ᵥ实例及附录A—C尚待译校。','（翻译中，已至p2式(2)）：已译对称性约束、线性极化的三个分量及九个不可约基底定义；C₃ᵥ特征标表、后续实例及附录A—C尚待译校。');p.write_text(t,encoding='utf-8')
p=r/'翻译管理/符号与约定.md';t=p.read_text(encoding='utf-8');note='## 5.1式(1)—(2)约定（B424）\n\np2电场为极矢量；Vb(Vx)、Va(Vy)、V0(Vz)依原文。引言α的一阶下标b/a与公式1b/1a分别保留。式(2)共1+3+5个不可约基底分量；不预设αij=αji。Q200仅列式(1a)的Ez项负号候选，正文保留原式。'
if note not in t:p.write_text(t.rstrip()+'\n\n'+note+'\n',encoding='utf-8')
p=r/'翻译管理/当前进度与续接.md';t=p.read_text(encoding='utf-8');note='## 当前有效状态：5.1 B424完成（2026-10-21）\n\n已完成PDF p1及p2上半至式(2)，尚未处理p2的C₃ᵥ例子引言及表1/表2。B424逐项核对式(1a)—(1c)九个场系数及式(2)九个基底分量，共9个覆盖单元；本批34个数学片段、累计57个片段语法检查通过，参考渲染已视觉核对，无横向溢出。新疑点Q200保留原式，候选负号未采用；引言下标b/a与公式1b/1a差异分别保留。术语、约定、章节清单、导航及序言已更新。\n\n下一批B425：从p2“C₃ᵥ対称を例にとって”开始，处理表1、表下注释和表2；按完整表格控制批次，不能跳过p2余文。5.1尚未完成。\n\n以下为历史记录。\n\n'
if note not in t:p.write_text(t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+note,1),encoding='utf-8')
print('B424完成；下一批B425；原式与候选保持分列。')

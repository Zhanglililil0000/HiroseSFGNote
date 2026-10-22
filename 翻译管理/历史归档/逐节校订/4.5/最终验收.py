from pathlib import Path
import re,json,hashlib,collections,csv,io
from urllib.parse import unquote
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.5 两个CH₃基团的张量分量.md'
s=target.read_text(encoding='utf-8')
source=root/'日语原版/Chapter4/chap4-5.pdf'
sha=hashlib.sha256(source.read_bytes()).hexdigest()
batch=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
whole=json.loads((out/'整节渲染检查.json').read_text(encoding='utf-8'))
audit=json.loads((out/'覆盖一致性核验.json').read_text(encoding='utf-8'))
index=json.loads((out/'全节公式与覆盖索引.json').read_text(encoding='utf-8'))
assert len(batch['results'])==39
assert batch['math']==whole['math']==1577
assert all(not r['overs'] and r['width']==r['scrollWidth'] for r in batch['results']+whole['results'])
assert len(re.findall(r'^# ',s,re.M))==1
assert len(re.findall(r'^## [1-6]\. ',s,re.M))==6
assert len(re.findall(r'^## 附录[A-F]',s,re.M))==6
assert all(f'Q{q}' in s for q in range(168,176))
assert '旧译待核' not in s and 'B325止' not in s
assert not re.search(r'[\u3040-\u30ff]',s)
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
assert not any(x in s for x in ['SCRIPTPLACE','cid:','```','同上','参见前文的公式'])
assert not re.findall(r'\\tag\{([^}]+)\}',s)
assert all((out/f'原文p{n}.png').exists() for n in range(1,79))
assert not audit['unmapped_math_lines'] and not audit['duplicate_source_lines'] and not audit['math_round_trip_mismatches']
assert s.count('原式分组疑点Q174')==27
assert s.count('\n无。')==50
assert '\\varpi _{ZZZ}' in s
parts=re.split(r'<!-- source ([a-z0-9,]+) -->',s)
ids=[k for i in range(1,len(parts),2) for k in parts[i].split(',')]
assert len(ids)==len(set(ids))
assert all(k in ids for b in index['batches'] for f in b['formulas'] for k in f['source_lines'])
preface=(root/'Preface序言.md').read_text(encoding='utf-8')
link=re.search(r'^- \[4\.5[^\n]+?\]\(([^\n]+?)\)（',preface,re.M)[1]
assert (root/unquote(link)).resolve()==target.resolve()
records=list(csv.DictReader(io.StringIO((root/'翻译管理/章节清单.tsv').read_text(encoding='utf-8-sig')),delimiter='\t'))
assert '全78页' in next(r for r in records if r['编号']=='4.5')['映射核验']
issues=(root/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8')
assert all(re.search(rf'^## Q{q}\b',issues,re.M) for q in range(168,176))
pages=set()
for n in range(323,362):
 c=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'))
 pages.update(c['pages'])
 c.update({'source_sha256':sha,'source_images_visually_checked':True,'verification_method':'数字PDF字体/字形/基线转录及逐行覆盖核验，全部页图浏览，异常与跨页续式重点复核','source_corrections_adopted':False})
 (out/f'B{n}-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 rec={'batch':f'B{n}','date':'2026-10-21','scope':c['scope'],'pages':c['pages'],'source_sha256':sha,'translation_sha256':hashlib.sha256((out/f'B{n}-本批译文.md').read_bytes()).hexdigest(),'status':'本批译校、覆盖及参考排版验收完成','render':next(r for r in batch['results'] if r['batch']==f'B{n}'),'source_corrections_adopted':False,'scope_limit':'原文覆盖、转录与参考排版核验，不代表原文理论推导已获独立证明。'}
 (out/f'B{n}验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert pages==set(range(1,79))
report={'date':'2026-10-21','section':'4.5','status':'全节译校完成，原文疑点待核','source_pages':78,'source_sha256':sha,'translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'batches':'B323—B361','batch_count':39,'main_sections':6,'appendices':'A—F','numbered_equations':0,'chi_single_component_equalities':853,'beta_single_component_equalities':156,'math_fragments':1577,'math_syntax_errors':0,'formula_overflows':0,'post_B325_source_lines':2627,'math_physical_lines':2357,'no_signal_items':50,'math_round_trip_mismatches':0,'bracket_issue_locations':27,'open_source_issues':'Q168—Q175','source_corrections_adopted':False,'next_batch':'B362，4.6原题、实际页码及局部约定核验','verification_limit':'翻译覆盖、转录及参考排版完成；未决原文公式仍需专业核实。'}
(out/'整节完成复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'整节完成复核.md').write_text('''# 4.5整节完成复核

日期：2026-10-21。B323—B361共39批，原PDF全78页正文及附录A—F完成本轮译校。

- 第1—4部分：原题、目录、绪论、三级坐标层级、单甲基与双甲基模式、对称分类已恢复；旧译将简并模式改为弯曲模式和对称表错列均按原文修复。
- 第5部分p3—6：五类内部旋转条件，每类保留完整分子β表和±号定义。
- 第6部分p6—19：空间角及平均条件、四类内部角下面内随机取向表全部保留。φA/φB与整体φ分开；一般空间取向不能以随机表替代。
- 附录A p19—22：坐标定义、变换、一般分子β及简并四组；附录B p22—30、C p30—38、D p38—49、E p49—58：各保留两支全对称和三支简并模式，每支27个空间分量；附录F p58—78：一般式及交换对称前提、分子代入关系和三支简并空间表。
- 空间χ单分量等式共853个（正文178，附录B—F各135）；β单分量等式共156个，包含重复及代入关系。计数按出现位置，链式相等只计首个左式；和/差组合与求和关系另收于索引。原文无这些表式的编号，未补造原号。
- 第5部分起2627个原文物理行分批建索引，含2357个数学物理行及50个无信号项。数学转录回转比对零差异，未发现未映射或重复来源行；首三页另有已验收覆盖记录。
- 数字PDF字形、字体和基线用于识别希腊字母与上下标；全部页图浏览，异常与跨页续式重点复核。公式全部可编辑，未以截图、摘要或“同前”替代附录表。无独立插图遗漏。
- 1577个数学片段通过严格KaTeX语法检查；39个批次及合稿在1100像素视口未发现公式横向溢出。已查看空间定义、附录A、长表及连续首中尾预览。一次逐屏截图超时后，改为全稿公式检测加各正文部分/附录起点及首中尾抽查，重跑通过。
- Q168—Q175原式/原述保留，候选未采用：目录朝向、重复轴名/极限几何、对称条件、等角与正弦关系、投影面/角度复用、自比较近似条件、27处括号疑点（26处展示公式、1处代入关系），以及varpi字形。Q174具体位置见原式分组疑点位置；无已采用的原文修正。
- 已更新节首逐部分导读、Preface、第四章导航、章节清单、进度续接、分批记录、局部符号/术语、疑难、对照语料和勘误附件状态。旧文件路径保留以兼容链接。

本验收确认翻译覆盖、转录及参考排版，不等于独立证明原文所有物理推导。原式系数、符号、括号缺损及角度疑点仍需结合专业复核，不能将已译校误读为全部原式已获验证。

下一批B362进入4.6，先核原题、实际页码与局部约定。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

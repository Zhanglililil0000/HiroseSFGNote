from pathlib import Path
import re,json,hashlib,csv,io
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.4 CH基团的取向与和频张量.md'
s=target.read_text(encoding='utf-8')
batch=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
whole=json.loads((out/'整节渲染检查.json').read_text(encoding='utf-8'))
assert batch['math']==whole['math']==357
assert len(batch['results'])==9
for r in batch['results']+whole['results']:
 assert not r['overs'] and r['width']==r['scrollWidth']
assert len(re.findall(r'^# ',s,re.M))==1
assert '旧译待核' not in s
assert not re.search(r'(?<![A-Za-z\\])b_\{',s)
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
assert len(re.findall(r'^## [1-7]\. ',s,re.M))==7
assert len(re.findall(r'^### 5[a-e]\. ',s,re.M))==5
tags=re.findall(r'\\tag\{([^}]+)\}',s)
assert len(tags)==len(set(tags))==19
assert all(f'Q{i}' in s for i in range(160,168))
assert all((out/f'原文p{p}.png').exists() for p in range(1,11))
idx=json.loads((out/'全节公式与覆盖索引.json').read_text(encoding='utf-8'))
assert idx['table_component_occurrences']==89
pages=set()
for n in range(314,323):
 coverage=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'))
 pages.update(coverage['pages'])
 rec={**coverage,'status':'本批译校及参考排版验收完成',
 'render':next(r for r in batch['results'] if r['batch']==f'B{n}'),
 'translation_sha256':hashlib.sha256((out/f'B{n}-本批译文.md').read_bytes()).hexdigest(),
 'scope_limit':'确认原文覆盖、翻译转录与参考排版；原文理论疑点未因此得到验证。'}
 (out/f'B{n}验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert pages==set(range(1,11))
issues=(root/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8')
assert all(re.search(rf'^## Q{i}\b',issues,re.M) for i in range(160,168))
rows=list(csv.DictReader(io.StringIO((root/'翻译管理/章节清单.tsv').read_text(encoding='utf-8-sig')),delimiter='\t'))
assert '全10页' in next(r for r in rows if r['编号']=='4.4')['映射核验']
report={'date':'2026-10-21','section':'4.4','status':'全节译校完成，原文疑点待核',
 'source_pages':10,'source_sha256':hashlib.sha256((root/'日语原版/Chapter4/chap4-4.pdf').read_bytes()).hexdigest(),
 'translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'batches':'B314—B322','numbered_equations':19,'tensor_table_component_occurrences':89,
 'math_fragments':whole['math'],'math_syntax_errors':0,'formula_overflows':0,
 'open_source_issues':'Q160—Q167','source_formula_corrections_adopted':False,
 'next_batch':'B323，4.5原题、结构及局部约定核验'}
(out/'整节完成复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'整节完成复核.md').write_text('''# 4.4整节完成复核

日期：2026-10-21。状态：原PDF全10页完成本轮译校，原文疑点保留待核。

- B314—B322覆盖原目录、引言、七个正文部分、五种面内取向条件及作者末尾说明；页图与文本逐页对照。
- 19个编号式无重复：6.1—6.5c共7式，7.1a—7.5c共12式；无编号欧拉角、三角恒等式和取向求和关系另保留。
- 表内张量左式共89项：一般取向27、面内随机7、C₃ᵥ取向15、Cₛ取向27、C₂ᵥ取向13；C₄ᵥ/C₆ᵥ按原文指向随机表。无信号项与倾斜角条件保留，无独立插图遗漏。
- 修复旧译误题与擅加弯曲模式、β/χ及幂次转录、一般表(spp)漏项和信号出现/消失反译等问题。公式可编辑，未用摘要或截图替代表项。
- 357个数学片段通过严格KaTeX语法检查；9个批次和整节预览在1100像素视口无公式横向溢出。抽查镜面长表、6.3混用上标以及连续首中尾预览，未见显示缺损。
- Q160—Q167保留原式或原陈述并就地说明，候选未采用。随机χzzz与一般式差异、C₃ᵥ求和式和偏振组合、镜面表多余χ、反射场上标及L因子符号/Pz等仍待核验，无新增已采用的原文修正。
- 已同步节首逐部分概括、Preface、第四章导航、章节清单、进度续接、分批质量控制、局部符号/术语卡、疑难记录与勘误附件状态。旧文件名保留以兼容已有链接，正文题目按原题恢复。

验收确认原文覆盖、翻译转录与参考排版，不等于验证原文全部物理推导。应用各表时需保留局部角度、取向分布和求和条件。

下一批B323进入4.5，先独立核原题、结构和局部约定。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

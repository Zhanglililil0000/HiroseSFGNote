from pathlib import Path
import json, hashlib, re
from collections import Counter

root = Path('HiroseSFGNote')
out = root / '翻译管理/校订记录/4.1'
target = next((root / '中文版本/第四章 单层膜与多层膜的和频').glob('4.1 *.md'))
text = target.read_text(encoding='utf-8')
source = root / '日语原版/Chapter4/chap4-1.pdf'
sha = hashlib.sha256(source.read_bytes()).hexdigest()
assert sha == 'ddd8bdf08396ce91fbd9c8dd58f5c25ca86c6b6f7c6b8172db442fc06e25e07e'
batch = json.loads((out / '渲染检查.json').read_text(encoding='utf-8'))
whole = json.loads((out / '整节渲染检查.json').read_text(encoding='utf-8'))
for result in batch['results'] + whole['results']:
    assert not result['overs']
    assert result['scrollWidth'] == result['width']
    assert all(i['loaded'] for i in result['images'])
tags = re.findall(r'\\tag\{([^}]+)\}', text)
assert len(tags) == 108 and len(set(tags)) == 107
assert {k:v for k,v in Counter(tags).items() if v > 1} == {'1.9': 2}
assert '旧译待核' not in text
assert not any(ord(c)<32 and c not in '\n\r\t' for c in text)
pages = set()
for n in range(249, 277):
    coverage = json.loads((out / f'B{n}-覆盖.json').read_text(encoding='utf-8'))
    pages.update(coverage['pages'])
    if n >= 251:
        result = next(r for r in batch['results'] if r['batch'] == f'B{n}')
        record = {**coverage, 'status':'译校及排版验收完成', 'render':result,
                  'scope':'对照原文页图与文本；原文疑点保留并注释，验收不等于确认原文推导正确。'}
        (out / f'B{n}验收.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
assert pages == set(range(1,34))
report = {'date':'2026-10-20', 'section':'4.1', 'status':'全节译校完成，原文疑点待核',
          'source_sha256':sha, 'translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
          'source_pages':33, 'batches':'B249—B276', 'numbered_occurrences':108,
          'unique_labels':107, 'source_duplicate_label':'1.9，p6与p8，保留原号',
          'math_fragments':whole['math'], 'math_syntax_errors':0, 'formula_overflows':0,
          'assets_loaded':True, 'open_source_issues':'Q122—Q137', 'source_corrections_adopted':False,
          'next_batch':'B277，4.2结构与局部约定核验'}
(out / '整节完成复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out / '整节完成复核.md').write_text('''# 4.1整节完成复核

日期：2026-10-20。状态：全节译校完成；原文疑点保留待核。

- B249—B276覆盖原PDF全部33页：要点、四个正文部分、四个附录；逐页对照页图与文本。
- 公式、矩阵、嵌套分式及表格均以可编辑文本恢复；坐标图单独保留原图。共108处公式编号、107个不同标签。原文1.9在p6与p8重号，保留并注明位置。
- 全节853个数学片段通过严格KaTeX语法检查；28批及整节连续渲染均无公式横向溢出，坐标图正常载入。抽查表格、长矩阵、附录嵌套分式及首尾连续预览。
- 修复旧译漏项、串列、符号与公式转录错误；这些恢复不作为原文勘误。Q122—Q137均在相应位置注明并收入疑难记录，本节未采用原文公式修正。
- 已同步序言导读、第四章导航、章节清单、批次计划、局部约定、公式索引、单元覆盖、疑难及勘误状态、当前续接记录。

本次验收确认翻译覆盖、转录和参考排版；不表示已经验证原文全部物理推导。原文疑点按既定规则保留原式与候选说明，不能据此直接替换为候选式。

后续：B277进入4.2，先核原题、结构及局部符号。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

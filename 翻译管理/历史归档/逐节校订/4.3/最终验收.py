from 整节工具 import *
from collections import Counter
s=target.read_text(encoding='utf-8')
batch=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
whole=json.loads((out/'整节渲染检查.json').read_text(encoding='utf-8'))
assert batch['math']==whole['math']==899
assert len(batch['results'])==19
for r in batch['results']+whole['results']:
    assert not r['overs'] and r['width']==r['scrollWidth']
assert len(re.findall(r'^# ',s,re.M))==1
assert '旧译待核' not in s and '<!-- B296止' not in s
assert not re.search(r'(?<![A-Za-z\\])b_\{',s)
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
tags=re.findall(r'\\tag\{([^}]+)\}',s)
assert len(tags)==len(set(tags))==30
assert all(f'Q{i}' in s for i in range(146,160))
assert all((out/f'原文p{p}.png').exists() for p in range(1,27))
idx=json.loads((out/'全节公式与覆盖索引.json').read_text(encoding='utf-8'))
assert idx['table_component_occurrences']==356
pages=set()
for n in range(295,314):
    coverage=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'))
    pages.update(coverage['pages'])
    rec={**coverage,'status':'本批译校及参考排版验收完成',
         'render':next(r for r in batch['results'] if r['batch']==f'B{n}'),
         'translation_sha256':hashlib.sha256((out/f'B{n}-本批译文.md').read_bytes()).hexdigest(),
         'scope_limit':'确认原文覆盖及翻译转录；原文理论疑点未因此得到验证。'}
    (out/f'B{n}验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert pages==set(range(1,27))
source_hash=hashlib.sha256((root/'日语原版/Chapter4/chap4-3.pdf').read_bytes()).hexdigest()
report={'date':'2026-10-21','section':'4.3','status':'全节译校完成，原文疑点待核',
        'source_pages':26,'source_sha256':source_hash,'translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
        'batches':'B295—B313','numbered_equations':30,'tensor_table_component_occurrences':356,
        'math_fragments':whole['math'],'math_syntax_errors':0,'formula_overflows':0,
        'open_source_issues':'Q146—Q159','source_formula_corrections_adopted':False,
        'next_batch':'B314，4.4原题、结构及CH局部约定核验'}
(out/'整节完成复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'整节完成复核.md').write_text('''# 4.3整节完成复核

日期：2026-10-21。状态：原PDF全26页完成本轮译校，原文疑点保留待核。

- B295—B313覆盖原目录、引言、七个正文部分及作者末尾说明；全26页对照页图与文本。
- 30个编号式无重复，包含2-1、3-1至3-5b及6.1至7.5c；公式与覆盖索引保留原号。
- 共356个表内张量左式：4a、4b、4c各含三种模式的27分量表，共243项；5a为25项、5b为49项、5e为39项。无信号项明确保留，两处原Latin c照录。原无编号求和关系另行保留。
- 修复旧译将函数幂当作倍角、β/χ及键系希腊字母转录、根式、选择规则反译、漏掉条件及擅加说明等问题；表格公式全部可编辑。长式按运算项分行，未以图片或摘要替代。
- 899个数学片段通过严格KaTeX语法检查；19个批次及整节连续预览在1100像素视口无公式横向溢出。人工抽查数值根式、三角恒等式、长公式、冻结模式与连续首中尾预览。
- Q146—Q159保留原式或原陈述并就地说明，未采用原文公式修正。残缺右括号、孤立加号、重复张量因子与原文余弦L因子保留；其他已明示的定界符配对只作原分组范围内的排版整理。
- 已同步节首概括、序言、第四章导航、章节清单、分批计划、局部符号/术语卡、疑难记录及勘误状态；一条无关键未决问题的模式定义收入第四章对照语料。

验收确认翻译覆盖、转录与参考排版，不等于验证原文全部物理推导。角度偏移、模式条件、平均与归一化及原文不一致处不可省略。

下一批B314进入4.4，先独立核原题、结构与CH局部坐标/角度。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

from 整节工具 import *
from collections import Counter
s=target.read_text(encoding='utf-8')
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
whole=json.loads((out/'整节渲染检查.json').read_text(encoding='utf-8'))
assert whole['math']==668 and render['math']==668
for r in render['results']+whole['results']:
    assert not r['overs'] and r['width']==r['scrollWidth']
assert '旧译待核' not in s and '<!-- B277止' not in s
assert len(re.findall(r'^# ',s,re.M))==1
assert not any(ord(c)<32 and c not in '\r\n\t' for c in s)
labels=re.findall(r'\\tag\{([^}]+)\}',s)
expected=['6.1','6.2','6.3','6.4','6.5a','6.5b','6.5c','7.1a','7.1b','7.2a','7.2b','7.3a','7.3b','7.4a','7.4b','7.4c','7.5a','7.5b','7.5c']
assert labels==expected,labels
for i in range(138,146):assert f'Q{i}' in s
assert all((out/f'原文p{n}.png').exists() for n in range(1,20))
pages=set()
for n in range(277,295):
    coverage=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'))
    pages.update(coverage['pages'])
    record={**coverage,'status':'本批译校与参考排版验收完成','render':next(x for x in render['results'] if x['batch']==f'B{n}'),
            'translation_sha256':hashlib.sha256((out/f'B{n}-本批译文.md').read_bytes()).hexdigest(),
            'scope_limit':'确认原文覆盖及转录；不将原文疑点视为理论已验证。'}
    (out/f'B{n}验收.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert pages==set(range(1,20))
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-2.pdf').read_bytes()).hexdigest()
report={'date':'2026-10-21','section':'4.2','status':'全节译校完成，原文疑点待核','source_pages':19,'source_sha256':sha,
        'translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'batches':'B277—B294','numbered_equations':19,
        'tensor_table_component_occurrences':178,'math_fragments':668,'math_syntax_errors':0,'formula_overflows':0,
        'open_source_issues':'Q138—Q145','source_formula_corrections_adopted':False,'next_batch':'B295，4.3原题/结构/CH₂局部坐标核验'}
(out/'整节完成复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'整节完成复核.md').write_text('''# 4.2整节完成复核

日期：2026-10-21。状态：全部19页完成本轮译校；原文疑点保留待核。

- B277—B294覆盖原目录、引言、七个正文部分，包含4a—4d、5a—5e及作者末尾说明；全19页对照原页图和文本。
- 原19个编号式顺序完整，无重复。178个表内χ左式已按批次、原页与模式建立索引：4a全对称/简并、4b简并、4c简并各27项；5a为14项、5b为30项、5e为26项。
- 修复旧译欧拉轴角混淆、θ的幂误作倍角、β/χ及键系希腊字母转录、正负号、冻结旋转条件与选择规则反译。所有公式保留为可编辑数学文本。
- 668个数学片段通过严格KaTeX语法检查；18批及连续合稿在1100像素视口无公式横向溢出。已人工抽查长公式、数值行、对称性求和及合稿首中尾预览。
- Q138—Q145保留原式或原陈述并就地说明，未采用原文公式修正。原式孤立花括号保留；其他定界符配对的纯排版整理已有说明。旧译修复与原文勘误分开记录。
- 已同步节首与序言概括、第四章导航、章节清单、分批计划、局部符号/术语卡、疑难记录及勘误状态；两条无未决关键疑点的定义收入第四章对照语料。

本次验收确认覆盖、翻译转录及参考排版，不等于验证原文全部物理推导。各张量表的模式、旋转条件、归一化及原文不一致处不可省略。

下一批B295进入4.3，先独立核对原题、结构及CH₂局部坐标。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

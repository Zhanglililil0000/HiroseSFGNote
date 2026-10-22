from pathlib import Path
import json, hashlib, re

here = Path(__file__).resolve().parent
root = here.parents[2]
source = root / '日语原版/Chapter3/chap3-1.pdf'
target = root / '中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md'
digest = hashlib.sha256(source.read_bytes()).hexdigest()
assert digest == '3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
body = target.read_text(encoding='utf-8')
tags = re.findall(r'\\tag\{([^}]+)\}', body)
assert len(tags) == len(set(tags)) == 102
assert not any(ord(c) < 32 and c not in '\n\r\t' for c in body)
render = json.loads((here / '整节渲染检查.json').read_text(encoding='utf-8'))
assert render['math'] == 475
assert all(not r['overs'] and r['scrollWidth'] <= r['width'] for r in render['results'])
batch_render = json.loads((here / '渲染检查.json').read_text(encoding='utf-8'))
metrics = {r['batch']: r for r in batch_render['results']}
ids = list(range(178,191)) + list(range(210,228))
for n in ids:
    name = f'B{n}'
    coverage = json.loads((here / f'{name}-覆盖.json').read_text(encoding='utf-8'))
    assert not metrics[name]['overs']
    coverage.update(math_syntax_errors=0, display_overflows=0,
                    acceptance_scope='原页对照、完整转写、术语与数学语法、页面宽度；不代表原文推导疑点已解决',
                    source_formula_corrections_adopted=False,
                    next='3.2：先核对13页结构与局部约定' if n == 227 else '按全节公式编号索引续接')
    (here / f'{name}验收.json').write_text(json.dumps(coverage, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
report = dict(date='2026-10-20', section='3.1', source_pages=51,
              source_sha256=digest, unique_numbered_equations=102,
              math_fragments=475, math_syntax_errors=0, display_overflows=0,
              source_formula_corrections_adopted=False,
              unresolved_source_questions=['Q096—Q107','Q110—Q112'],
              next='B228：3.2，先核对原文结构、局部约定与跨节引用')
(here / '整节完成复核.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(here / '整节完成复核.md').write_text('''# 3.1 整节完成复核

日期：2026-10-20。原文51页的本轮翻译、旧译校订与公式转写完成。

- 原文PDF哈希与批次留档一致，未修改原文件。
- 共102个唯一编号式，编号无重复；475处数学内容通过严格语法检查。
- 整节连续预览及各批预览在1100像素视窗下均无页面横向溢出。已抽查整节首部、长式区域及末端截图。
- 已补回旧译省略的公式与推导段，清理旧译重复式；公式保留为可编辑数学文本。
- 原文疑点Q096—Q107、Q110—Q112保留原式并就地说明。本轮未采纳原文公式修正，未新增已确认勘误；推导正确性仍受这些待核问题限制。
- 已同步序言导读、第三章导航、章节清单、分批建议、符号约定、疑难记录及当前续接位置。

记录范围：B163—B190、B210—B227。B191—B209未使用，不代表缺失内容。编号对应关系见《全节公式编号索引》。验收记录中的“完成”指上述译校范围完成，不表示所有原文物理与代数疑点已经解决。

下一步：B228，进入3.2；先核对13页原文结构、局部约定，以及a、b、δ等符号的跨节含义。
''', encoding='utf-8')
rows = [('导读与反射/透射、L系数','1—3','B163—B164'),('二层系2.1','3—9','B165—B174'),('二层系2.2','9—13','B175—B182'),('2.3界面源','13—25','B183—B188'),('2.3的m′层体相源','25—32','B189'),('2.3的m层体相源','32—37','B190'),('三层系场乘积','37—45','B210—B218'),('三层系和频极化','45—51','B219—B227')]
(here / '全节单元覆盖.md').write_text('# 3.1 全节单元覆盖\n\n| 内容 | 原文页 | 批次 |\n|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows)+'\n\n共51页，102个唯一编号式。相邻单元页码有交叠，表示同页衔接；精确编号位置见全节公式编号索引。\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False))

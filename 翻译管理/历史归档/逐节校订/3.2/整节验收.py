from pathlib import Path
import json,re,hashlib
p=Path(__file__).resolve().parent; root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8')
r=json.loads((p/'整节渲染检查.json').read_text(encoding='utf-8'))
batch=json.loads((p/'渲染检查.json').read_text(encoding='utf-8'))
assert r['math']==300
assert all(not x['overs'] and x['width']==x['scrollWidth'] and all(a['loaded'] for a in x['images']) for x in r['results']+batch['results'])
assert len(re.findall(r'\\tag\{([^}]+)\}',s))==33
assert len(re.findall(r'!\[',s))==8
assert '旧译待核' not in s
for n in range(237,249):
    name=f'B{n}'; rec=json.loads((p/f'{name}-覆盖.json').read_text(encoding='utf-8'))
    fragment=(p/f'{name}-本批译文.md').read_text(encoding='utf-8')
    rec.update(math_fragments_this_batch=len(re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',fragment)),math_syntax_errors=0,display_overflows=0,render_preview_checked=True,acceptance_scope='原页对照、完整性、术语与排版；原文疑点未决，不代表已完成理论证明')
    (p/f'{name}验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=dict(date='2026-10-20',section='3.2',source_pages=13,unique_numbered_equations=33,math_fragments=300,figure_groups=8,figure_panels=46,math_syntax_errors=0,display_overflows=0,all_images_loaded=True,source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest(),source_formula_corrections_adopted=False,unresolved_source_questions='Q113—Q121',batches='B228—B248',next='B249：4.1，33页，先核结构与局部符号约定')
(p/'整节完成复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'整节完成复核.md').write_text('''# 3.2 整节完成复核

2026-10-20。B228—B248完成底本全部13页的本轮译校、原图恢复与公式转写。

- 第1部分系数、2.1概述、2.2详论、附录A/B均已覆盖。
- 33个唯一编号式：2.1—2.22、A.1—A.6、B.1—B.5，顺序完整，无重号。公式保持可编辑文本，未用图片替代主公式。
- 8组共46幅原光路子图完整恢复，保留原图内路径标记和因子；已核裁切范围，不用旧译代码块代替原图。
- 300处数学内容通过严格语法检查；各批及整节连续预览在1100像素视窗下均无横向溢出，8张图组资产全部加载。已查看各新批次预览和整节首尾衔接。
- 修复旧译矩阵次序、遗漏中间行与缺图；Q113—Q121按原式保留并就地说明。本轮未采用原文公式修正，未新增已确认勘误。
- 已同步序言、导航、章节清单、分批建议、局部约定、符号总表、疑难表及勘误附件状态。

本节矩阵化简、层标、相位及收敛条件仍有原文疑点。译校完成不表示这些疑点已经解决，也不表示原作者认可译者候选式。

第三章3.1、3.2均完成本轮译校。下一步B249进入4.1，先核33页结构、原题与局部符号约定。
''',encoding='utf-8')
(p/'全节单元覆盖.md').write_text('''# 3.2 全节单元覆盖

| 单元 | 原文页 | 批次 |
|---|---|---|
| 开篇及反射/透射系数 | 1 | B228 |
| L定义与15组系数 | 1—2 | B229 |
| 2.1符号矩阵及8个编号式 | 2—4 | B230—B234 |
| 2.2路径分类与递推 | 4—5 | B235—B236 |
| m′层四类场及23幅图 | 5—8 | B237—B240 |
| m层路径分类与递推 | 8—9 | B241—B242 |
| m层四类场及23幅图 | 9—12 | B243—B246 |
| 附录A矩阵级数 | 12—13 | B247 |
| 附录B相似变换 | 13 | B248 |

相邻单元共享页面表示同页衔接，并非重复翻译。精确编号与批次见全节公式编号索引。
''',encoding='utf-8')
card=p/'局部约定卡.md'; t=card.read_text(encoding='utf-8').replace('- 待核：δ的局部定义，以及Q113与后续源点路径的对应。','- 全节复核：本节未另见δ定义，不自动继承3.1的δ；Q113与源点路径的对应仍未决。'); card.write_text(t,encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

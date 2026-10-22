from pathlib import Path
import csv, io

root=Path(__file__).resolve().parents[3]
p=root/'翻译管理/术语表.tsv'
rows=list(csv.reader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'))
for row in rows[1:]:
    if row[0]=='T003':
        row[3]='分子极化率'
        row[5]+=' 2026-10-18用户确认用于分子α；首次出现说明为线性场响应。'
    elif row[0]=='T004':
        row[3]='超极化率（β为一阶，γ为二阶）'
        row[5]+=' 2026-10-18用户确认β为一阶超极化率、γ为二阶超极化率，分别对应二阶、三阶场响应；日语原词是否使用超分極率仍依底本，不因中文命名确认而改变。'
    elif row[0]=='T005':
        row[3]='线性极化率；二阶非线性极化率；三阶非线性极化率（按χ阶数）'
        row[5]+=' 2026-10-18用户确认χ⁽¹⁾与χ⁽³⁾名称；可能混淆时加宏观。'
    elif row[0]=='T070':
        row[5]='宏观χ⁽³⁾，对应三阶场响应；可能与分子γ混淆时加宏观。译名确认不代表三阶公式均已验证。'
    else:
        continue
    row[7]+='；2026-10-18用户明确确认项目中文命名'
    row[8]='项目中文译名已确定；底本符号及原词仍逐节核验'
    row[10]='用户已确定（2026-10-18）'
new=[
    ('T081','β（符号索引，非日文原词）','first hyperpolarizability','一阶超极化率','分子β；对应二阶场响应，通常有三个张量下标；命名阶数、场响应阶数和张量阶数分别说明。'),
    ('T082','γ（符号索引，非日文原词）','second hyperpolarizability','二阶超极化率','分子γ；对应三阶场响应，通常有四个张量下标；不与宏观χ⁽²⁾混淆。'),
    ('T083','χ⁽¹⁾（符号索引，非日文原词）','linear electric susceptibility','线性极化率','宏观线性响应；可能与分子α混淆时称宏观线性极化率。'),
]
ids={x[0] for x in rows[1:]}
for tid,ja,en,zh,definition in new:
    assert tid not in ids
    rows.append([tid,ja,en,zh,'',definition,'1.1式（1）—（3）；其他章节按定义核对','2026-10-18用户明确确认项目中文命名','项目中文译名已确定','符号定义参照B002；非新增日语字符串核验','用户已确定（2026-10-18）','英语为译者辅助释义，非声称作者原用词'])
assert all(len(x)==len(rows[0]) for x in rows)
buf=io.StringIO(newline='')
csv.writer(buf,delimiter='\t',lineterminator='\n').writerows(rows)
p.write_text(buf.getvalue(),encoding='utf-8-sig')
p=next((root/'中文版本/第一章 SFG快速入门').glob('1.1 *.md'))
s=p.read_text(encoding='utf-8')
s=s.replace('可用分子极化率张量 $\\alpha$、$\\beta$、$\\gamma$ 写成式（1）','可用分子极化率张量 $\\alpha$、一阶超极化率张量 $\\beta$ 和二阶超极化率张量 $\\gamma$ 写成式（1）')
s=s.replace('以高阶极化率张量 $\\beta$、$\\gamma$ 为系数','以超极化率张量 $\\beta$、$\\gamma$ 为系数')
marker='\\tag{1}\n$$\n'
assert marker in s
s=s.replace(marker,marker+'\n> **译者注（项目术语约定）：** 分子 $\\alpha$ 称“分子极化率”，对应线性场响应；$\\beta$ 称“一阶超极化率”，对应二阶场响应；$\\gamma$ 称“二阶超极化率”，对应三阶场响应。超极化率的命名阶数、场响应阶数与张量阶数应分别理解。此命名不改变原式系数或阶乘约定。\n',1)
old='> **译者注：** 式（2）中的 $\\chi^{(2)}$ 称为“二阶非线性极化率”；上下文明确时可简称“极化率”。这里的宏观响应与式（1）的分子极化率张量应加以区分。'
new='> **译者注（项目术语约定）：** 式（2）的 $\\chi^{(1)}$、$\\chi^{(2)}$、$\\chi^{(3)}$ 分别称“线性极化率”“二阶非线性极化率”“三阶非线性极化率”。可能与分子响应混淆时加“宏观”；上下文明确时，二阶非线性极化率可简称“极化率”。分子 $\\beta$ 对应二阶场响应，但名称为“一阶超极化率”，应与宏观 $\\chi^{(2)}$ 区分。'
assert old in s
p.write_text(s.replace(old,new),encoding='utf-8')
for name in ['翻译管理/翻译规范.md','翻译管理/符号与约定.md','翻译管理/第一章跨节约定检查.md','翻译管理/当前进度与续接.md']:
    p=root/name
    s=p.read_text(encoding='utf-8')
    note='\n## 响应系数命名已确认（2026-10-18）\n\n用户确认：分子α称分子极化率（线性场响应），β称一阶超极化率（二阶场响应），γ称二阶超极化率（三阶场响应）；宏观χ⁽¹⁾、χ⁽²⁾、χ⁽³⁾分别称线性极化率、二阶非线性极化率、三阶非线性极化率。可能与分子响应混淆时加“宏观”。首次出现说明超极化率命名阶数与场响应阶数，另与张量阶数区分。保留原式阶乘及系数约定。此决定覆盖本文件较早的同项“待确认”状态，不确认未决公式或日语原词。\n'
    if name.endswith('当前进度与续接.md'):
        note+='\n术语表T003/T004/T005/T070更新，新增T081—T083，现共83条；1.1式（1）、（2）附近定义及注释同步。此轮仅落实用户命名决定，未核验Q010/Q012/Q028/Q029，也未开展新章翻译。\n'
    p.write_text(s+note,encoding='utf-8')
print('术语83条，均保持12列及UTF-8 BOM；正文与四份管理文件已同步。')

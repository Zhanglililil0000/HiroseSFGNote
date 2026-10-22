from pathlib import Path
import csv,shutil
m=Path('HiroseSFGNote/翻译管理');p=m/'术语表.tsv';bak=m/'术语修订记录'/'术语表-v0.2.tsv'
if not bak.exists():shutil.copy2(p,bak)
rows=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));by={r['术语编号']:r for r in rows}
by['T005'].update({'推荐中文候选':'按阶数命名；χ⁽²⁾ 为二阶非线性极化率','别名或需辨析译法':'极化率（上下文明确时简称）；电极化率/电极化系数（旧表检索项，不作本项目首选）','定义与适用语境':'宏观 χ 的通用条目，不将所有阶数都称为二阶。二阶具体用法见 T049；简称不能与微观 α 混淆。','依据':'2026-10-16 用户指定二阶 χ 的全称与简称规则；其他阶数须按原文分别确认','状态':'二阶用法已确定；其他阶数待核验','译名决定状态':'部分已确定，详见 T049'})
by['T010'].update({'推荐中文候选':'菲涅尔因子','别名或需辨析译法':'菲涅尔系数；菲涅耳系数（保留检索，不作项目首选）','定义与适用语境':'Fresnel coefficient 的项目译名。具体反射、透射、局域场修正及复合 L 因子按原文定义，不因中文统一而合并不同物理量。','依据':'2026-10-16 用户明确指定：Fresnel coefficient → 菲涅尔因子','状态':'项目译名已确定（用户指定）','译名决定状态':'用户已确定'})
by['T026'].update({'推荐中文候选':'非线性极化率（阶数依原文）','别名或需辨析译法':'非线性电极化率（旧候选，不作项目首选）','定义与适用语境':'χ 的宏观非线性响应；二阶为二阶非线性极化率，见 T049，不能统一套用二阶名称。','依据':'2026-10-16 用户二阶 χ 决定的配套表述；其他阶数完整名称待原文核验'})
assert by['T026']['英语辅助释义']=='nonlinear susceptibility'
new={k:'' for k in rows[0]};new.update({'术语编号':'T049','日语候选':'二阶 χ 对应的感受率（原文写法依章节核对）','英语辅助释义':'second-order nonlinear susceptibility','推荐中文候选':'二阶非线性极化率','别名或需辨析译法':'极化率（明确上下文中的允许简称）','定义与适用语境':'χ⁽²⁾ 的完整名称；首次引入、定义、标题及有阶数/微观量混淆可能时用全称。上下文已明确为同一二阶宏观响应时允许简称极化率。保留原符号及单位制，不擅自补 ε₀。','原文位置':'1.1 PDF p2，式(2)–(3)；符号视觉核对在试译时执行','依据':'2026-10-16 用户明确决定','状态':'项目译名已确定（用户指定）','文本定位状态':'由通用 χ 条目拆分；原文写法和符号待逐节核验','译名决定状态':'用户已确定','英语来源说明':'译者辅助对应；不声称作者原文提供该英文'})
assert 'T049' not in by;rows.append(new)
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
check=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));assert len(check)==49 and len({r['术语编号'] for r in check})==49
assert next(r for r in check if r['术语编号']=='T010')['推荐中文候选']=='菲涅尔因子'
print('PASS: 49 terms; T005/T010/T026 updated; T049 added; v0.2 snapshot retained.')

from pathlib import Path
import csv,json
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.6 *.md'));old=P.read_text(encoding='utf-8');end=old.index('### 1.2.');assert not (O/'B146-修订前.md').exists();(O/'B146-修订前.md').write_text(old,encoding='utf-8')
prefix=old[old.index('## 1. 绪论'):end]
prefix=prefix.replace('例如，式 (4.66) 和式 (4.68) 有误。','作者指出，例如式（4.66）和式（4.68）有误。').replace('具体来说，','按作者的说明，').replace('物理意义更合理的','在处理界面连续条件时更合理的')
key='(2) Heavens'
i=prefix.index(key);prefix=prefix[:i]+'> **原文疑点（Q086，PDF p1，第1项）**：底本将 $kr-§omega t$ 与 $§omega t-kr$ 的差别称为“相差 $180^§circ$”。此处保留原说法；两者互为负值，并不能一般地推出恒定的 $§pi$ 相位差。候选解释为相位符号或复表示约定相反，尚未作为原文修正采用。\n\n'+prefix[i:]
prefix+='> **译者说明**：第2、3项对Heavens教材的批评，以及第4项对符号约定的说明，均为本手稿作者的论述；本批仅对照手稿译校，未独立核验所引教材的相应版本和公式。\n\n'
head='''# 2.6 薄膜内的电场

> 原作：广濑千秋（沿用项目作者归属；独立底本首页未列署名）  
> 中文翻译：章力
>
> **译校状态（2026-10-20）：** B146完成PDF p1的1.1引言，止于1.2标题前；后续为旧译待校订。
>
> **底本：** `日语原版/Chapter2/chap2-6.pdf`，12页。本节采用传播矩阵法，独立核验方向、相位和矩阵顺序，不从前节直接继承。

多层膜中的膜内电场（基于Born与Wolf传播矩阵法的表述）。

> **阅读导引（译者编写）：** 引言比较两套教材的相位、坐标与反射系数约定。本批已核引言；后续按标题包含传播关系、不同界面数的矩阵及单层至三层膜内电场，尚未逐项校订。

'''
text=(head+prefix).replace('§',chr(92));P.write_text(text+old[end:],encoding='utf-8');assert (text+old[end:])[(text+old[end:]).index('### 1.2.'):]==old[end:];(O/'B146-本批译文.md').write_text(text,encoding='utf-8')
(O/'结构与复用核验表.md').write_text('''# 2.6结构与复用核验入口

独立底本12页，SHA256：329e6cc656b6e143555bac82f6320e9dd051ee782f93151a1c743159f76f2f35。以下范围据文字层标题/分页定位；只有1.1已逐项对原页，其余尚未核验。

| 单元 | 原页范围 | 状态与分批边界 |
|---|---|---|
| 1.1引言 | p1 | B146完成；教材比较四项、作者论述与Q086注 |
| 1.2 Born与Wolf的思路 | p1—2 | B147下一批：完整核方向与1.1—1.5b，止于2标题前；不可截断跨页关系 |
| 2传播公式 | p2—4 | 待核；U/V连续量、正逆矩阵、偏振与相位 |
| 3界面数与传播矩阵 | p4—6 | 待核；一至三个界面，乘积次序与下标须另核 |
| 4层数与膜内电场总述 | p6—7 | 待核 |
| 4.1单层膜 | p7—8 | 待核 |
| 4.2双层膜 | p8—9 | 待核 |
| 4.3三层膜 | p9—12 | 待核；完整长式和末尾内容须逐项检查 |

与此前线性光学主题有重合，但引言说明了相位、入射面和p偏振符号差异，不能据前节公式直接认定一致。后续分界执行时须按完整段落/公式组复核。
''',encoding='utf-8')
(O/'局部约定卡.md').write_text('''# 2.6局部约定卡

B146仅核引言：B&W与Heavens采用相反相位记法、yz/xz入射面转换及p偏振反射系数的电场/磁场约定差别，均按作者论述保留。s对应TE、p对应TM。Q086对180°的说法只注不改。具体s方向、正负上标及矩阵传播约定待1.2及第2部分逐项核验，不套前节。
''',encoding='utf-8')
f=R/'翻译管理/当前进度与续接.md';s=f.read_text(encoding='utf-8');i=s.index('\n')+1;s=s[:i]+'''\n## 当前有效状态：2.6已开始，B146完成1.1引言（2026-10-20）

独立12页结构入口已建立；p1引言四项教材差异说明及结束语已逐项核验。新增Q086：两种相反相位被称相差180°，保留原话与候选解释；作者对教材的批评按手稿译出，不声明已独立核对教材。1.2及后续旧译逐字保持。

下一批B147：完整核1.2，含p1—2的方向定义、1.1/1.2与1.3—1.5b，止于第2部分前；特别注意原文1.5a右端字形和矢量积，不能按旧译预先规范化。不要重跑历史生成脚本。以下为历史记录。

'''+s[i:];f.write_text(s,encoding='utf-8')
for rel,col in [('翻译管理/章节清单.tsv','编号'),('翻译管理/全书调查/分批建议.tsv','节号')]:
 f=R/rel
 with f.open(encoding='utf-8-sig',newline='') as h:d=csv.DictReader(h,delimiter='\t');fields=d.fieldnames;rows=list(d)
 for row in rows:
  if row[col]!='2.6':continue
  if col=='编号':row['状态']='B146已核1.1引言，后续旧译待校订';row['映射核验']='独立12页结构定位完成；p1至1.2前逐项核验';row['公式图表范围']='本批无编号式，后续待逐组登记';row['导读状态']='已更新B146范围；后续概括仅结构定位'
  else:row['执行状态']='B146已核1.1；B147续跨p1—2的1.2至1.5b，后续未核'
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(rows)
f=R/'Preface序言.md';s=f.read_text(encoding='utf-8');lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith('- [2.6 '):lines[i]=line+'（B146已核1.1引言，后续待校订）：比较相位、坐标及偏振系数约定，再以传播矩阵处理多层膜内场；后段概括仅结构定位。'
f.write_text('\n'.join(lines)+'\n',encoding='utf-8')
f=D/'阅读导航.md';s=f.read_text(encoding='utf-8').replace('2.6以后仍待校订。','2.6已核1.1引言，其后及后续章节仍待校订。');s+='''\n## 2.6 薄膜内的电场

[进入正文](2.6%20薄膜内的电场.md)。独立12页。B146已核1.1引言：比较B&W与Heavens的相位、入射面、边界相位和p偏振反射系数约定；Q086保留并注。

后续按标题含1.2方向/场关系、第2部分传播矩阵、第3部分界面数与矩阵、第4部分单层至三层膜内电场，均尚待逐项校订。应先确认局部正负号、相位和矩阵顺序，再读后续计算。
''';f.write_text(s,encoding='utf-8')
f=R/'翻译管理/疑难与勘误.md';f.write_text(f.read_text(encoding='utf-8')+'\n| Q086 | 2.6 PDF p1，1.1第1项 | kr−ωt与ωt−kr称相差180° | 原值保留；两相位互为负值，不一般等于固定π差，候选为符号/复表示约定相反；未采用修正，B146。 |\n',encoding='utf-8')
(O/'B146.md').write_text('''# B146：2.6结构入口与1.1引言

2026-10-20，独立底本12页。原图核对p1的1.1全部文字、四项差异与结束语，止于1.2前。保留教材书名、作者、出版信息及原引用；Q086对180°说法只注不改。作者对教材的批评作为手稿论述处理，未声称独立验证外部教材。无编号式；后段逐字保持。下一批B147完整核跨p1—2的1.2。
''',encoding='utf-8')
(O/'B146-覆盖.json').write_text(json.dumps({'batch':'B146','date':'2026-10-20','pages':[1],'source_total_pages':12,'source_sha256':'329e6cc656b6e143555bac82f6320e9dd051ee782f93151a1c743159f76f2f35','numbered_equations':0,'unreviewed_tail_unchanged':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
c=(R/'翻译管理/校订记录/2.5/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/2.5','校订记录/2.6').replace("startsWith('2.5 ')","startsWith('2.6 ')");(O/'检查排版.cjs').write_text(c,encoding='utf-8');(O/'渲染检查.json').write_text('{"results":[]}',encoding='utf-8')
print('B146 written; 1.2 onward preserved')

from pathlib import Path
import re,json,hashlib,csv
root=Path('HiroseSFGNote');m=root/'翻译管理';o=m/'校订记录/3.1';p=root/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8-sig')
assert not (o/'B163-修订前.md').exists()
(o/'B163-修订前.md').write_text(old,encoding='utf-8')
toc=[('1. 系数等',2),('反射系数与透射系数',2),('L系数',2),('2. 二层系（1/m′/m/2）产生的和频光',3),('2.1 电场振幅的乘积',3),('1/m′界面',3),('m/2界面',4),('m′/m界面',5),('m′层中深度z₁处',6),('m层中距m′/m界面深度z₂处',7),('2.2 和频极化',9),('1/m′界面',9),('m/2界面',9),('m′/m界面',10),('m′层中深度z₁处',11),('m层中距m′/m界面深度z₂处',12),('2.3 和频电场',13),('1/m′界面的极化产生的和频光',13),('m/2界面的极化产生的和频光',17),('m′/m界面的极化产生的和频光',21),('m′层的极化产生的和频光',25),('m层的极化产生的和频光',32),('3. 三层系（1/m′/m/m″/2）产生的和频光',37),('3.1 电场振幅的乘积',38),('1/m′界面',38),('m″/2界面',38),('m′/m界面',39),('m/m″界面',41),('m′层中深度z₁处',42),('m层中距m′/m界面深度z₂处',43),('m″层中距m/m″界面深度z₃处',44),('3.2 和频极化',45),('1/m′界面',45),('m″/2界面',46),('m′/m界面',47),('m/m″界面',48),('m′层中深度z₁处',49),('m层中距m′/m界面深度z₂处',50),('m″层中距m/m″界面深度z₃处',51)]
header='''# 3.1 二层膜及三层膜产生的和频光

> 原作：广濑千秋（沿用项目作者归属；独立底本首页未列署名）  
> 中文翻译：章力
>
> **译校状态（2026-10-20）：** B163完成PDF p1—2的原目录、引言与反射/透射系数单元；L系数段起仍为旧译待逐项校订。
>
> **底本：** `日语原版/Chapter3/chap3-1.pdf`，51页。标题按底本同时列二层膜及三层膜；现有文件路径暂保留。

> **阅读导引（译者编写）：** 原目录按“激发电场振幅的乘积→和频极化→和频电场”组织二层系，再列三层系的场乘积与极化。后续内容目前仅完成目录定位，尚未完成公式校订。本批确认反射/透射系数及轴向分量关系；不直接套用2.6的L矩阵。

## 原目录

下列页码沿用原目录（PDF页码）；原目录跨p1—2。各后续单元的实际起止边界仍须随译校核实。

| 原目录项目 | 起页 |
| --- | ---: |
'''+''.join(f'| {name} | {page} |\n' for name,page in toc)
intro='''
作为文件《薄膜产生的和频过程》的延伸，这里求出膜层数为二时的表达式。（当膜层数达到三层或更多时，会形成维数与层数相同的矩阵级数，因而变得复杂。参照文件《嵌入发光层产生的电场》，可以将这里介绍的方法推广并加以公式化。）

> **译者注（范围说明）：** 上段“矩阵级数”的复杂性表述沿用作者原说法，不据此改写2.6的传播矩阵维数约定。两个文件名按此处原文译出，跨文件公式对应关系待后续逐项核对。

## 1. 系数等

### 反射系数与透射系数

将光电场表示为表面固定坐标系中的分量时，反射系数与透射系数如下。利用这些关系，将相应坐标分量表示为入射光电场偏振分量的形式。

'''
a=old.index('$$',old.index('### 反射系数'));b=old.index('### L系数'); coeff=old[a:b]
# Only regroup the two long coefficient identities; preserve every factor.
start=coeff.rfind('$$',0,coeff.rfind('$$'))
last=coeff[start:]; assert 't_{1m,\\alpha}t_{m1,\\alpha}' in last
newlast=r'''$$
\begin{aligned}
t_{1m,\alpha}t_{m1,\alpha}
 &=1+r_{1m,\alpha}r_{m1,\alpha}=1-r_{1m,\alpha}^2,\\
t_{2m,\alpha}t_{m2,\alpha}
 &=1+r_{2m,\alpha}r_{m2,\alpha}=1-r_{2m,\alpha}^2,
\qquad (\alpha=x,y,z).
\end{aligned}
$$

'''
coeff=coeff[:start]+newlast
checked=header+intro+coeff
tail=old[b:];p.write_text(checked+tail,encoding='utf-8');assert p.read_text(encoding='utf-8').endswith(tail)
(o/'B163-本批译文.md').write_text(checked,encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
coverage={'batch':'B163','date':'2026-10-20','pages':[1,2],'units':'跨页原目录39项、引言、反射/透射系数9组无编号式','numbered_equations':0,'unnumbered_display_groups':9,'toc_entries':len(toc),'source_images_visually_checked':True,'source_sha256':sha,'source_corrections_adopted':False,'unchanged_tail':'L系数段起与修订前逐字相同'}
(o/'B163-覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B163.md').write_text('# B163：3.1开篇译校\n\n2026-10-20。核对独立PDF p1—2；补回旧译遗漏的完整目录（含跨至p2的末两项），恢复底本同时包含二层及三层膜的标题。引言保留矩阵级数复杂性的原陈述，并注明不用于统一2.6矩阵维数。九组无编号反射/透射关系逐项核对，未采用原文修正；末组仅分行。L段起不变，下一批核p2—3的L定义与15条系数。\n',encoding='utf-8')
(o/'局部约定卡.md').write_text('''# 3.1局部约定卡

## 已核范围：B163，PDF p1—2反射/透射系数

- 入射介质与膜层用1、2、m；二层系1/m′/m/2、三层系1/m′/m/m″/2来自原目录，不能把2.6的层序自动移入。
- r、t为电场振幅反射、透射系数，非强度；保留本节p系数的符号与分母。r_x=r_p、r_y=r_s、r_z=−r_p；反向r取负。
- 轴向透射系数保留原式的cos或sin比；α=x,y,z，不解释为分子极化率。
- 原目录3.1/3.2等是本节内部标题，与全书节号3.1区别。
- L源点场连接定义、方向与公共因子：下一批p2—3核对，尚不能标为已完成。已定位其对象不同于2.6的基变换L。
- 时间因子、单位制、各膜局部深度原点与频率指标随正文逐项核实，不从前节自动继承。
''',encoding='utf-8')
(o/'结构与复用核验表.md').write_text('''# 3.1结构与复用核验表

独立底本51页，题为二层膜及三层膜产生的和频光。原目录p1—2已对照，后续页码为目录定位，未宣称逐页完成。

| 单元 | 目录页区间 | 状态/后续切分原则 |
| --- | --- | --- |
| 原目录、引言、反射/透射系数 | 1—2 | B163完成 |
| L系数定义及前/后/膜内系数 | 2—3 | 下一批完整处理；不可与2.6基变换L混用 |
| 二层系电场乘积 | 3—8 | 待核；按三个界面、两个体相位置分批，跨页式接全 |
| 二层系和频极化 | 9—12 | 待核；按同五类源点分批 |
| 二层系和频电场 | 13—36 | 待核；1/m′、m/2、m′/m、m′体相、m体相各自再分偏振/方向组 |
| 三层系过渡及电场乘积 | 37—44 | 待核；四个界面、三个体相位置 |
| 三层系和频极化 | 45—51 | 待核；同七类位置，目录延续至p2 |

## 复用限制

第二章只可作为候选对照，不整体复制已验收状态。逐式重核层标、相位、分母、源点内外侧及偏振；局部深度z₁/z₂/z₃的原点须由本节正文确认。每批优先一个完整推导/公式组；原目录给出起页而非批次硬边界。长公式跨页时先核下一页再结束。
''',encoding='utf-8')
# Management: update only this batch's verified scope.
progress=m/'当前进度与续接.md';t=progress.read_text(encoding='utf-8-sig');h,rest=t.split('\n',1);progress.write_text(h+'\n\n## 当前有效状态：B163完成3.1开篇（2026-10-20）\n\n已完成原目录39项、引言与p2反射/透射系数九组无编号式；标题按底本注明二层及三层膜，保留文件路径。L系数起旧译未改。\n\n下一批B164：完整核p2—3的L定义、记法、公共因子、正反方向及15条系数，再止于第2部分之前。特别核“电场坐标/极化偏振”文字与后文分量对象是否一致；疑点保留原文并注。后续按结构与复用核验表分批。以下为历史记录。\n'+rest,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:r=csv.DictReader(h,delimiter='\t');fields=r.fieldnames;rows=list(r)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163完成目录、引言与反射/透射系数；L系数起待校订','映射核验':'已对照p1—2至L系数前；51页结构据原目录登记','公式图表范围':'9组无编号系数已核；后续待核','导读状态':'已标明B163完成范围；后续仅目录定位','导读草案':'二层系按电场乘积、和频极化、和频电场组织；三层系列场乘积与极化，后段尚待逐项核验。'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
pref=root/'Preface序言.md';t=pref.read_text(encoding='utf-8-sig');t=re.sub(r'(^- \[3\.1[^\n]+?\.md\))[^\n]*',lambda a:a[1]+'（B163已核目录、引言及反射/透射系数；其余待校订）：原题包括二层及三层膜；按场乘积、极化及出射场组织，后段概括据原目录。',t,flags=re.M);pref.write_text(t,encoding='utf-8')
nav=p.parent/'阅读导航.md'
assert not nav.exists()
nav.write_text('''# 第三章阅读导航

本导航由译者编写。当前仅3.1开篇B163已完成本轮译校，后续旧译尚待校订。

## 3.1 二层膜及三层膜产生的和频光

[进入正文](3.1%20二层膜及三层膜产生的和频光.md)。独立51页，文件路径沿用旧名。

已核原目录、引言及反射/透射系数。完整目录位于正文开头，可定位二层系的三个界面和两个体相源点，以及三层系的四个界面和三个体相源点；这些后续单元仅完成目录定位。

建议依“激发场乘积→和频极化→辐射场”阅读，先确认层标、源点位置及局部坐标。L系数定义与全部后续推导仍待本轮逐项核对。
''',encoding='utf-8')
print(json.dumps(coverage,ensure_ascii=False))

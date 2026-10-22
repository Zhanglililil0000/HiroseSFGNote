from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B164-修订前.md').exists();(o/'B164-修订前.md').write_text(old,encoding='utf-8')
a=old.index('### L系数');b=old.index('## 2. 二层系');src=old[a:b];eqs=re.findall(r'\$\$([\s\S]*?)\$\$',src);assert len(eqs)==16
q='''> **原文疑点（Q096，PDF p2，L系数定义段）：** 原文此处将电场称为“坐标分量”、极化称为“偏振分量”，但随后说明及p3系数采用s/p电场与x/y/z极化的对应。这里保留原文措辞；候选为这两处分量名称互换，尚未采用原文修正。应结合下文的具体分量读取L系数。
'''
text=r'''### L系数

L系数是将和频极化与其产生的和频光电场振幅 $E_{SF}$ 联系起来的系数。如下式所示，电场按各坐标分量、极化按各偏振分量分别定义。

$$
E_{SF,\alpha}=\sum_{\beta}L_{\alpha\beta}P_{\beta}^{SF}
$$

'''+q+r'''
根据广义Snell折射公式，所产生的和频光同时包含向上（−）和向下（+）两个方向的光。此外，L系数的表达式随极化所在位置而不同。最初推导时，考虑的是无限薄的薄膜m发生极化，并向介质1和介质2出射光的情况，由此将s偏振、p偏振电场振幅与极化的x、y、z分量联系起来；这里将其推广。同时省略公共因子 $4\pi i\omega_{SF}/c$（以波矢代替折射率时，为 $4\pi i\omega_{SF}^{2}/c^{2}$）。向上（−）光指沿反射光方向（−z方向）传播的光，向下（+）光指沿入射光及透射光方向（+z方向）传播的光。

**L系数的记法：** $L_{i/j,s(p),\alpha}$ 表示极化片m′夹在i层与j层之间时，极化的α分量（α=x,y,z）与其产生的光的s或p偏振分量之间的系数。上标−、+分别区分向上光和向下光。

> **译校说明：** 此处按原页恢复 $E_{SF,\alpha}$ 的下标及 $L_{i/j,s(p),\alpha}$ 的下标结构，旧译把后者的层序、偏振及分量写成上标，属于转写错误。这里的L连接极化源与辐射电场，不是2.6的场基变换矩阵。上述公共因子按作者说明省略，不将其重新乘入本页系数；原式折射率比中省略的SF指标也不擅自补齐。

'''
def display(e):
 e=e.strip()
 # Split long two-step z-component equalities; no value or factor changes.
 if len(e)>220:
  parts=e.split(' = ');assert len(parts)==3
  e=r'\begin{aligned}'+'\n'+parts[0]+' &= '+parts[1]+r'\\'+'\n&= '+parts[2]+'\n'+r'\end{aligned}'
 return '$$\n'+e+'\n$$\n\n'
for title,lo,hi in [('介质1与叠层膜m之间的极化片m′产生和频光时，L系数如下。',1,7),('介质2与叠层膜m之间的极化片m″产生和频光时，L系数如下。',7,13),('叠层膜内部的极化片产生和频光时，L系数如下。',13,16)]:
 text+=title+'\n\n'+''.join(display(e) for e in eqs[lo:hi])
text+='上述电场与极化之间的关系不限于和频极化及和频光。对于振荡极化及其产生的电磁波，这些关系一般成立。\n\n'
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B164完成原目录、引言及第1部分系数（PDF p1—3）；第2部分起仍为旧译待校订。Q096保留原文并就地说明。',new);new=new.replace('本批确认反射/透射系数及轴向分量关系；不直接套用2.6的L矩阵。','已核反射/透射系数、轴向分量及L系数的源点、偏振与方向；L不等同2.6的基变换矩阵。');p.write_text(new,encoding='utf-8');assert new[new.index('## 2. 二层系'):]==old[b:]
(o/'B164-本批译文.md').write_text(text,encoding='utf-8')
sha=hashlib.sha256((r/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
coverage={'batch':'B164','date':'2026-10-20','pages':[2,3],'units':'L定义、记法、公共因子、方向、两侧各6条和膜内3条系数及段末一般性说明','numbered_equations':0,'unnumbered_display_groups':16,'L_coefficient_relations':15,'source_images_visually_checked':True,'unresolved':['Q096'],'source_corrections_adopted':False,'source_sha256':sha,'unchanged_tail':'第2部分起逐字保持'}
(o/'B164-覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B164.md').write_text('# B164：3.1的L系数单元\n\n2026-10-20，PDF p2—3。核对定义、方向、记法、公共因子及15条L系数：1/m六条、2/m六条、m/m三条。x、y的正反关系和z分量的负号、折射率比及平方逐项保留；不将原式未标SF的折射率比补标。长z分量等式仅分行。恢复E和L下标结构，属于旧译转写修复。段末振動分極译为“振荡极化”，指产生电磁波的时间变化极化。Q096保留原文，未采用修正；第2部分起未改。\n',encoding='utf-8')
def append(path,s):path.write_text(path.read_text(encoding='utf-8-sig')+'\n\n'+s+'\n',encoding='utf-8')
append(m/'疑难与勘误.md','## 3.1原文疑点（2026-10-20）\n\n'+q[2:])
append(o/'局部约定卡.md','## B164已核补充（覆盖上文L待核状态）\n\nL连接源极化与辐射电场；下标为层序i/j、出射s/p、源点坐标分量x/y/z，上标±仅表示方向。−为反射光同向的−z，+为入射/透射同向的+z。省略公共因子4πiωSF/c；以波矢代替折射率时为4πiωSF²/c²。1/m、2/m各六条，m/m三条；内部x/y正反相同，z反号。m′/m″为两侧极化片层标，不能统一成单一m。Q096只记录文字对象混用，不改系数。单位制及完整时间因子仍待本节后续核验。')
append(m/'符号与约定.md','## 3.1的L系数（B164，2026-10-20）\n\n本节L为极化源到辐射电场的连接系数，不是2.6基变换L。下标依次为i/j、出射s/p偏振、源极化x/y/z，上标±是沿±z传播的方向。公共因子按正文省略。定义段对象名称疑点Q096保留，具体对应参照15条系数；不跨章强行统一记号。')
append(o/'结构与复用核验表.md','## B164执行更新\n\np2—3的L完整单元已核：一个定义式、15条系数与所有文字说明。此前该行“下一批”为历史状态。第2部分开篇与式2.1跨p3—4，下一批需核到式尾并保留路径相位适用条件，不能止于p3页末。')
progress=m/'当前进度与续接.md';s=progress.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);progress.write_text(h+'\n\n## 当前有效状态：B164完成3.1第1部分（2026-10-20）\n\n原目录、引言、反射/透射系数及完整L单元已核至p3第2部分之前。B164新增16个无编号展示式（定义1、系数15），Q096保留原文并注；没有采用原文修正。\n\n下一批B165：核第2部分2.1引言与1/m′界面1侧的式2.1，跨p3—4接全。重点纠正旧译“最小侧面”为原文最外表面；核相位只包含外表面反射路径的限定、内部界面反射须另计、文献第4节引用。E±及n的物理含义须依本节原文，不自行借用2.6。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B164完成目录、引言及第1部分系数；第2部分起待校订','映射核验':'p1—3已核至第2部分前；其余结构据原目录定位','公式图表范围':'25组无编号展示式已核（9组反射/透射、L定义及15条L系数）；后续待核','导读状态':'已更新B164范围；其余仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
pref=r/'Preface序言.md';s=pref.read_text(encoding='utf-8-sig');s=s.replace('B163已核目录、引言及反射/透射系数；其余待校订','B163—B164已核目录、引言及第1部分全部系数；第2部分起待校订');pref.write_text(s,encoding='utf-8')
nav=p.parent/'阅读导航.md';s=nav.read_text(encoding='utf-8-sig').replace('当前仅3.1开篇B163已完成本轮译校','当前3.1开篇及第1部分B163—B164已完成本轮译校').replace('已核原目录、引言及反射/透射系数。','已核原目录、引言、反射/透射系数与完整L单元。').replace('L系数定义与全部后续推导仍待本轮逐项核对。','L系数定义、公共因子及15条系数已核；Q096保留定义段对象名称疑点。第2部分起仍待本轮逐项核对。');nav.write_text(s,encoding='utf-8')
print(json.dumps(coverage,ensure_ascii=False))

from pathlib import Path
import re,json,csv,hashlib
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.5 *.md'));bs=chr(92)
s=P.read_text(encoding='utf-8');s=re.sub(r'> \*\*译校状态（2026-10-20）：\*\*[^\n]+','> **译校状态（2026-10-20）：** B134—B145完成独立底本全部20页的本轮译校与可编辑数学排版：90个唯一编号式、全部无编号关系及附录D六条证明链齐备。原文疑点保留并加注；E-2.5-001为暂定文字补读。',s,count=1)
s=s.replace('后续含激发场、和频极化、反射/透射场与附录；这些后续概括目前仅据标题和结构定位，尚未逐项校订。','正文随后依次列出激发场、和频极化、L系数、反射与透射场及净场，附录A整理线性光学，附录D证明极化薄片的L系数；本轮均已逐项核验。')
P.write_text(s,encoding='utf-8')
tags=re.findall(re.escape(bs)+r'tag\{([^}]+)\}',s)
expected=['2.1','2.3']+['4.'+str(n) for n in [3,6,9,12,15,18,21,24,25]]+['4.26a','4.26b','4.27','4.28a','4.28b','4.29','4.30a','4.30b']+['5.'+str(n)+l for n in range(1,6) for l in 'abc']+['5.'+str(n)+l for n in range(6,12) for l in 'ab']+['5.'+str(n)+l for n in range(13,27) for l in 'ab']+['A.'+str(n) for n in range(1,6)]+['A.6a','A.6b','A.7','A.8','A.9a','A.9b','A.10a','A.10b','A.11a','A.11b','A.12']
assert tags==expected,(len(tags),len(expected),set(tags)^set(expected));assert len(tags)==len(set(tags))==90
sha=hashlib.sha256((R/'日语原版/Chapter2/chap2-5.pdf').read_bytes()).hexdigest();assert sha=='6dff0000c7d1d7672b10e8a43cf9d683ac5fb7602b50aba9d875dba4992c4094'
assert '§' not in s and not any(ord(c)<32 and c not in '\n\r\t' for c in s)
assert s.count(bs+'frac{i}{'+bs+'delta}')==4
assert 'r_{m2,ivis,'+bs+'alpha}' in s and 'E^0_{ir,'+bs+'gamma}e' in s
assert s.count('证毕。')==1
index=['# 2.5全节公式编号索引\n\n全部90个唯一编号式，无缺号重号。2.1→2.3、4.1标题的跳转及5.12缺号按底本保留，不补造编号。\n','| 编号 | 校订批次 | 原页范围 |','|---|---|---|']
rows=[]
for f in sorted(O.glob('B*-覆盖.json')):
 a=json.loads(f.read_text(encoding='utf-8'));tt=a.get('tags',a.get('equation_tags',[]));pages=a.get('pages',a.get('source_pages',[]))
 for t in tt:rows.append({'tag':t,'batch':a['batch'],'pages':pages});index.append('| '+t+' | '+a['batch']+' | '+','.join(map(str,pages))+' |')
assert len(rows)==90
(O/'全节公式编号索引.md').write_text('\n'.join(index)+'\n',encoding='utf-8');(O/'全节公式编号索引.json').write_text(json.dumps({'total':90,'tags':tags,'entries':rows},ensure_ascii=False,indent=2),encoding='utf-8')
coverage='''# 2.5全节单元覆盖

| 批次 | PDF范围 | 覆盖 |
|---|---|---|
| B134 | p1 | 引言、体系与全部定义 |
| B135 | p1—2 | 多重反射/透射说明及2.1/2.3 |
| B136 | p2 | 波长/复数说明、轴向r/t及乘积关系 |
| B137 | p2—4 | 4.1a—g全部激发场，含跨页4.21及膜内四项乘积 |
| B138 | p4—7 | 4.25—4.30b、完整薄膜与无编号场关系，跨页4.28b/4.30b |
| B139 | p7—8 | L定义、十五系数式及十二源点场关系 |
| B140 | p8—11 | 5.13—5.18各界面反射，含完整薄膜及跨页式 |
| B141 | p11—12 | 5.19a/b体相反射四积分项及净反射说明 |
| B142 | p12—14 | 透射范围与5.20—5.25各界面场，含完整薄膜及跨页式 |
| B143 | p15—16 | 5.26a/b体相透射全式，净透射说明跨页接全 |
| B144 | p16—18 | 附录A全式、轴分量、边界与强度关系 |
| B145 | p18—20 | 附录D六条完整证明链及适用范围说明，至证毕 |

独立底本无单独示意图；公式全为可编辑数学。编号式90个与无编号关系分别登记。前后界面内外侧、A/B源点、四种积分分母与p偏振x/z两支均保留；未用省略号、新物理缩记或公式截图替代。重合公式与附录对独立原页另核，2.4的Py(00+)未移入本节。
'''
(O/'全节单元覆盖.md').write_text(coverage,encoding='utf-8')
f=R/'翻译管理/当前进度与续接.md';v=f.read_text(encoding='utf-8');i=v.index('\n')+1;v=v[:i]+'''\n## 当前有效状态：2.5全节完成（2026-10-20）

B134—B145完成独立20页全部本轮译校与数学排版：90个唯一编号式、无编号关系及附录D六条证明链齐备。B136—B145续完4.1至附录D证毕；体相旧译iδ恢复为i/δ。Q085新增ivis与无下标h记号疑点，其余关联既有问题按原值保留；E-2.5-001为「べて」暂按「すべて」的文字补读，已就地说明及收入勘误附件。

管理清单、分批建议、序言、阅读导航、符号约定、复用入口、疑难表及全节覆盖/编号索引均更新。下一独立底本2.6尚未开始本轮校订；如继续，B146先核2.6结构及首个完整单元。不要重跑历史生成脚本覆盖正文。以下为历史记录。

'''+v[i:];f.write_text(v,encoding='utf-8')
for rel,key in [('翻译管理/章节清单.tsv','编号'),('翻译管理/全书调查/分批建议.tsv','节号')]:
 f=R/rel
 with f.open(encoding='utf-8-sig',newline='') as h:d=csv.DictReader(h,delimiter='\t');fields=d.fieldnames;data=list(d)
 hits=0
 for row in data:
  if row[key]!='2.5':continue
  hits+=1
  if key=='编号':
   row['状态']='本轮全节译校及可编辑数学排版完成；原式疑点保留';row['映射核验']='独立20页已按B134—B145逐项原图对照';row['公式图表范围']='90个唯一编号式及无编号关系、附录D六证明链齐备；独立底本无示意图';row['导读状态']='2026-10-20按全节已核内容更新';row['导读草案']='五类源点的激发场与二阶非线性极化、L连接、反射/透射净场及线性光学与极化薄片附录。'
  else:row['执行状态']='2026-10-20 B134—B145全节20页译校与数学排版完成；90编号式及无编号关系齐备；疑点保留'
 assert hits
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(data)
f=R/'Preface序言.md';v=f.read_text(encoding='utf-8');lines=v.splitlines()
for i,line in enumerate(lines):
 if line.startswith('- [2.5 '):lines[i]=line[:line.index('（B134')]+ '（全节译校完成）：从五类源点的激发电场推至二阶非线性极化、L系数及反射/透射净场，附录A整理线性光学、附录D给出六条出射场证明。20页、90个编号式；原式疑点保留。'
f.write_text('\n'.join(lines)+'\n',encoding='utf-8')
f=D/'阅读导航.md';v=f.read_text(encoding='utf-8').replace('2.5已核引言、定义及多重反射/透射，其后内容及2.6以后仍待校订。','2.5全部20页已完成本轮译校与数学排版；2.6以后仍待校订。');a=v.index('## 2.5 薄膜产生的和频（要点）');v=v[:a]+'''## 2.5 薄膜产生的和频（要点）

[进入正文](2.5%20多层膜的和频过程（SFG）：要点.md)。独立20页，B134—B145完成全节译校与数学排版；90个唯一编号式及全部无编号关系齐备。

1. 引言与准备（p1—2）：区分两界面各自两侧和膜内五类源点，规定膜厚、坐标、方向与振幅系数，并列多重反射/透射总场及边界条件。
2. 激发电场4.1（p2—4）：从普通双介质界面两侧，扩展到有膜体系的前后界面各侧以及膜内A/B源点；含波长、复数与轴向分量关系。
3. 和频极化4.2（p4—7）：以二阶非线性极化率连接两激发场与输出极化，逐一处理五类位置、完整薄膜和体相四项场乘积。
4. L系数5.1（p7—8）：将极化坐标分量连接到出射s/p偏振；给出两界面、膜内部系数与十二条源点场关系。
5. 反射场5.2（p8—12）：前后界面内外侧及完整薄膜逐组列式，体相分四种传播量组合，末尾按光路叠加得到净反射场。
6. 透射场5.3—5.4（p12—16）：计入新增源点范围，列出对应界面与体相场，再叠加得到净透射场。
7. 附录A（p16—18）：平面波复表示、复折射率、菲涅尔因子、轴向分量及边界/强度关系；局部采用正时间指数。
8. 附录D（p18—20）：计入无限薄极化片内的多重反射，完整证明向两侧出射的s(Py)、p(Px)、p(Pz)六个分量；外介质有限厚度的适用限制保留。

建议按源点、出射方向与偏振选式；用附录A核线性系数，再用D核L连接。编号跳跃、原下标、方向称谓及相位疑点均有就地说明。E-2.5-001为暂定文字补读；译校完成不表示未决原式已获代数认证。
''';f.write_text(v,encoding='utf-8')
f=R/'翻译管理/疑难与勘误.md';f.write_text(f.read_text(encoding='utf-8')+'''
## 2.5全节收尾（B136—B145，2026-10-20）

| 问题号 | 位置 | 原值与处理 |
|---|---|---|
| Q085 | p3式4.15及p5的4.2b标题 | 原写ivis、位置h+及无m下标的h；照录，vis及补膜下标仅候选 |
| Q044/Q047 | p3—4、p5及p18 | B源点坐标2(n+1)与相位2n+1不同；附录C、4.13及4.29—4.36引用与本文件编号不匹配；均保留并定位说明 |
| Q061/Q062/Q063/Q064 | p4—7 | 4.26a未配对右花括号、4.28a的wvis、4.29孤立e、4.30a交叉频率及额外相位保留；旧译无注规范化已恢复 |
| Q041/Q080/Q081/Q082/Q083/Q084 | p7—15 | 双称上行、m/1、反向层标及孤立括号、wvis/基线2/缺i、孤立e与缺方向上标、体相交叉频率及混合L层标照录；iδ转写误读修复为原文i/δ |
| Q053/Q072/Q073 | p16—20 | 时间因子与复折射率局部约定、ri与t21/t12下标、A.6额外角度平方等按独立原页保留；平方/模平方和原引用只注 |

没有新采用的原文公式修正。E-2.5-001仅为p15「べて」暂按「すべて」的文字补读，已就地标注并收入勘误附件；全节内容完成与原式疑点解决分开管理。
''',encoding='utf-8')
for rel,extra in [
 ('翻译管理/校订记录/2.5/局部约定卡.md','\n全节收尾：χ在正文为二阶非线性极化率，在附录A为线性极化率。求和β/γ为分量，β_m,频率是传播量；L输出为s/p而源为x/y/z。正文负时间因子与附录A正时间因子各自保留。体相前因子i/δ照原页，不沿用旧译iδ；缺标及异常相位不统一。附录D六证明链完整，末尾Pz中2n1因子已核。\n'),
 ('翻译管理/符号与约定.md','\n## 2.5全节（B134—B145，2026-10-20）\n\n独立20页已核。正文χ为二阶非线性极化率，附录Aχ为线性极化率；分量求和β/γ与传播β区分。L源坐标与输出偏振分开；时间与复折射率虚部按局部约定保留。体相i/δ、原层标与相位按原页，不从旧译或前节规范化代入。本节5.6—5.9位置省略两侧上标，不能移入2.4的00+字样。\n'),
 ('翻译管理/校订记录/2.5/结构与复用核验表.md','\n## 当前有效结论（2026-10-20）\n\n上表为起始调查历史状态。B134—B145已逐项核完全部20页，见全节单元覆盖及编号索引。与2.4/2.3重合数学对独立原页另核后使用，恢复本文件的90个编号和局部差异；不存在直接继承前节完成状态。后续全节验收另记。\n')]:
 f=R/rel;f.write_text(f.read_text(encoding='utf-8')+extra,encoding='utf-8')
f=R/'中文版本/附件/原文勘误表.md';v=f.read_text(encoding='utf-8');key='## 后续维护';v=v.replace(key,'''## 第2.5节：薄膜产生的和频（要点）

B134—B145于2026-10-20完成全部20页。未决公式与原引用照录；以下为本轮唯一采用的暂定文字补读。

| 编号 | 位置 | 原文 | 译本处理 | 依据与状态 |
|---|---|---|---|---|
| E-2.5-001 | PDF p15，5.4首段 | 「べての部分」 | 暂按「すべての部分」理解，译为“所有部位” | 句义及5.2f同类叠加说明支持；文字暂定补读，未经作者确认，2026-10-20；正文同编号说明。 |

'''+key);f.write_text(v,encoding='utf-8')
# Record the distinction between a source formula correction and a tentative textual reading.
f=O/'B143-覆盖.json';a=json.loads(f.read_text(encoding='utf-8'));a['tentative_textual_reading']='E-2.5-001';a['source_formula_corrections_adopted']=False;f.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
print('90 unique tags verified; management and errata synchronized')

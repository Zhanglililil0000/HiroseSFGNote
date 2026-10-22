from pathlib import Path
import json,re,hashlib,csv
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.4 *.md'));bs=chr(92)
s=P.read_text(encoding='utf-8')
s=re.sub(r'> \*\*译校状态（2026-10-19）：\*\*[^\n]+','> **译校状态（2026-10-20）：** B124—B133完成独立底本全部10页的本轮译校与数学排版。准备工作、全部L系数、各源点场及式（1a）—（14b）均已覆盖；未决原式照录并就地加注，译校完成不等于原式已获代数验证。',s,count=1)
s=s.replace('当前准备工作、L定义及前界面六系数已核；其后概括暂按标题与结构定位。','全文已核。阅读时可先查准备工作和L系数，再按源点所在界面、内外侧及反射/透射选式；体相长式在末尾完整列出。')
P.write_text(s,encoding='utf-8')
source=R/'日语原版/Chapter2/chap2-4.pdf';sha=hashlib.sha256(source.read_bytes()).hexdigest();assert sha=='3f6eeee4f3418c4a89181b0c0142b95aee1adda31fb6e94a7c100fd000f58be2'
scope={
 'B126':([3],[],'介质2/膜六个L系数、两个z等价链及膜内三条关系'),
 'B127':([3,4],[],'P(0)、P(h_m)、P(z)的十二个出射电场关系；跨p3—4接全'),
 'B128':([4,5],[str(n)+x for n in range(1,5) for x in 'ab'],'前界面外侧及完整表面膜的反射和透射'),
 'B129':([5,6],[str(n)+x for n in [5,6] for x in 'ab'],'前界面内侧反射/透射，6b跨页'),
 'B130':([6,7],[str(n)+x for n in range(7,11) for x in 'ab'],'背界面外侧及完整薄膜的反射和透射'),
 'B131':([7,8],[str(n)+x for n in [11,12] for x in 'ab'],'背界面内侧反射/透射，12b跨页'),
 'B132':([8,9],['13a','13b'],'体相坐标与反射p/s；每式四个积分分母，p含x/z两支'),
 'B133':([9,10],['14a','14b'],'体相透射p/s；14a的z支完整跨页接续')}
for batch,(pages,tags,desc) in scope.items():
 text=(O/(batch+'-本批译文.md')).read_text(encoding='utf-8');found=re.findall(re.escape(bs)+'tag\{([^}]+)\}',text);assert found==tags,(batch,found)
 a={'batch':batch,'date':'2026-10-20','source_pages':pages,'source_sha256':sha,'content':desc,'equation_tags':tags,'source_page_images_visually_checked':True,'render_screenshot_visually_checked':True,'adopted_source_corrections':False,'new_named_formula_abbreviations':False}
 (O/(batch+'-覆盖.json')).write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
 (O/(batch+'.md')).write_text(f'# {batch}：2.4译校\n\n2026-10-20；独立底本PDF p'+ '、'.join(map(str,pages))+'。\n\n'+desc+'。逐项核对原页和文字层；公式为可编辑LaTeX，无公式截图替代。\n\n编号：'+('、'.join(tags) or '本批均无原式编号')+'。不移植2.2/2.3编号。原文疑点只注不改；旧译误读的修复另记录，不作为原文勘误。数学严格检查及浏览器渲染已核；全节验收汇总见整节完成复核。\n',encoding='utf-8')
tags=re.findall(re.escape(bs)+'tag\{([^}]+)\}',s);expected=[str(n)+x for n in range(1,15) for x in 'ab'];assert tags==expected and len(set(tags))==28
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
assert s.count('$$')%2==0
assert not re.search(r'\\thetam|\\betam|E_SF|\.\.\. \(\d',s)
original=(O/'B126-修订前.md').read_text(encoding='utf-8');assert s[s.index('## 准备工作'):s.index('### 介质2与膜之间的极化片')]==original[original.index('## 准备工作'):original.index('对于媒质2与多层薄膜 m 之间的极化片')]
index=['# 2.4全节公式编号索引\n\n独立底本28个唯一编号式，均为可编辑数学；无编号关系另见单元覆盖。\n','| 编号 | PDF页 | 校订批次 |','|---|---|---|']
for batch,(pages,t,desc) in scope.items():
 for tag in t:index.append('| '+tag+' | '+({'3b':'5','4a':'5','4b':'5','6b':'6','9b':'7','10a':'7','10b':'7','12b':'8','13a':'8','13b':'9','14a':'9—10','14b':'10'}.get(tag,str(pages[0])))+' | '+batch+' |')
(O/'全节公式编号索引.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
(O/'全节公式编号索引.json').write_text(json.dumps({'tags':tags,'unique':28,'source_sha256':sha},ensure_ascii=False,indent=2),encoding='utf-8')
coverage='''# 2.4全节单元覆盖

| PDF范围 | 原文单元 | 完成批次 |
|---|---|---|
| p1—2 | 坐标、界面、方向；s/p反射透射、反向关系、轴分量与边界/强度关系 | B124 |
| p2—3 | 响应映射、公共因子、L记号与1/m六系数 | B125 |
| p3 | 2/m六系数及膜内三条关系 | B126 |
| p3—4 | 两界面和体相源点共十二个出射场关系 | B127 |
| p4—5 | 前界面外侧与完整表面膜，1a—4b | B128 |
| p5—6 | 前界面内侧，5a—6b | B129 |
| p6—7 | 背界面外侧与完整薄膜，7a—10b | B130 |
| p7—8 | 背界面内侧，11a—12b | B131 |
| p8—9 | 体相坐标及反射，13a—13b | B132 |
| p9—10 | 体相透射，14a—14b；14a的z支跨页接全 | B133 |

独立PDF全部10页逐项对照；原文件没有独立示意图，故无图形遗漏或公式图片替代。准备工作与L区的无编号等式、完整薄膜的两段说明文字和总标题均覆盖。28个编号式无缺号、无重号。公式断行及乘积/同分母分式拆分只为排版，不用新物理简记代替长式。
'''
(O/'全节单元覆盖.md').write_text(coverage,encoding='utf-8')
f=R/'翻译管理/当前进度与续接.md';v=f.read_text(encoding='utf-8');i=v.index('\n')+1
v=v[:i]+'''\n## 当前有效状态：2.4全节完成（2026-10-20）

B124—B133覆盖独立PDF全部10页：准备工作、三组L系数、十二个源点场关系与28个编号式（1a—14b），全部为可编辑数学。B126—B133本日续完；跨页6b、12b、14a完整衔接。Q077—Q084及Q041关联疑点原值保留并就地注；没有采用新的原文公式修正。体相旧译iΔ已按原页修复为i/δ，原文反射分母的交叉频率、混合L层标、缺配括号等不作无注改写。

管理清单、Preface、章节导航、局部符号卡、疑难登记、勘误附件状态与整节验收均已更新。下一节2.5尚未开始本轮校订；如用户继续，从独立20页底本结构/复用核验起步，下一批号B134。不能把2.4完成状态复制给2.5。历史生成脚本不要重跑覆盖当前正文。以下为历史记录。

'''+v[i:];f.write_text(v,encoding='utf-8')
for rel,key in [('翻译管理/章节清单.tsv','编号'),('翻译管理/全书调查/分批建议.tsv','节号')]:
 f=R/rel
 with f.open(encoding='utf-8-sig',newline='') as h:reader=csv.DictReader(h,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
 hits=0
 for row in rows:
  if row[key]!='2.4':continue
  hits+=1
  if key=='编号':
   row['状态']='本轮全节译校与可编辑数学排版完成；原式疑点保留'
   row['映射核验']='独立PDF全10页已按B124—B133逐项对照'
   row['公式图表范围']='28个唯一编号式（1a—14b）及全部无编号关系已覆盖；独立底本无示意图'
   row['导读状态']='2026-10-20按已核正文更新Preface及第二章导航'
   row['导读草案']='按界面内外侧、完整薄膜及体相列出反射/透射和频场；保留源点、L层标、频率相位及原式疑点。'
  else:row['执行状态']='2026-10-20 B124—B133全节10页译校与数学排版完成；28编号式及无编号关系齐备；疑点保留，见整节验收'
 assert hits>0
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(rows)
f=R/'Preface序言.md';v=f.read_text(encoding='utf-8');lines=v.splitlines()
for i,line in enumerate(lines):
 if line.startswith('- [2.4 '):
  link=line[:line.index('（B124')];lines[i]=link+'（全节译校完成）：先列界面、方向、菲涅尔因子与L系数，再按前后界面内外侧及完整薄膜给出反射/透射场，末尾完整列出体相结果。共28个编号式；原式疑点见就地注。'
f.write_text('\n'.join(lines)+'\n',encoding='utf-8')
f=D/'阅读导航.md';v=f.read_text(encoding='utf-8');v=v.replace('2.4已核准备工作及前界面L系数，其后及2.5以后仍待校订。','2.4全部10页已完成本轮译校与数学排版；2.5以后仍待校订。');a=v.index('## 2.4 薄膜产生的和频（表达式）')
v=v[:a]+'''## 2.4 薄膜产生的和频（表达式）

[进入正文](2.4%20多层膜的和频过程（SFG）：表达式.md)。独立底本10页，B124—B133已完成全节逐项译校与数学排版；28个编号式及无编号关系齐备。

1. 准备工作（p1—2）：坐标、界面和方向定义；s/p与轴向振幅系数、反向关系、边界条件及强度守恒。
2. L系数与源点场（p2—4）：区分极化坐标分量与出射s/p偏振，列两界面及膜内L系数，并连接P(0)、P(h_m)、P(z)与十二个出射场关系。
3. 前界面（p4—6，1a—6b）：依次给出界面外侧、已形成完整表面膜、界面内侧产生的反射与透射和频光，保留各自激发场和出射多重反射因子。
4. 背界面（p6—8，7a—12b）：依次处理外侧、完整薄膜及内侧源点；层标、方向与符号随原式保留。
5. 膜体相（p8—10，13a—14b）：定义A/B源点位置，完整列出四种传播量组合的积分项、反射p/s及透射p/s；14a的z支跨页接全。

建议先按源点选择界面内外侧，再选择反射或透射与偏振。原式疑点Q077—Q084及Q041关联项有就地说明；完成译校不表示已独立证明公式正确。本文不借用2.2/2.3编号，长式无省略或公式截图替代。
''';f.write_text(v,encoding='utf-8')
issues='''
## 2.4后续与整节收尾（B126—B133，2026-10-20）

| 问题号 | 原文位置 | 疑点 | 处理 |
|---|---|---|---|
| Q079 | p3，P(0)第四个场关系 | P_y(00+)多一个0 | 照录；候选P_y(0+)只在就地注 |
| Q080 | p4式2a/2b；p7式10a/10b | L用m/1而定义用1/m；部分场无方向上标 | 原标保留，不补上标，候选只注 |
| Q081 | p5式4a/4b | 和频分母末项方向下标与式3不同；未配对右圆括号 | 原式保留；候选同式3及删括号未采用 |
| Q082 | p6式7a/7b、8a/8b | wvis；7组分母基线数字2与指数缺i、7b出射分子缺i | 原页放大复核后照录；常规相位与分母候选只注 |
| Q083 | p7—8式12a/12b | 两入射场后孤立e；12a的z项以−1开头 | 孤立e和原号保留，删除e仅候选 |
| Q084 | p8—10式13a—14b | i/δ的δ本文件未在此定义；反射公共分母交叉频率相位、L层标混合；13的花括号闭合不齐 | iΔ为旧译误读已修复为i/δ；其余原值与可见括号照录，无补闭合；不臆补δ定义，参考2.2符号卡但不等同原文已定义 |

以上均未采用原文修正，无新增E-2.4公式勘误条目。全节文本、无编号关系和28个编号式已覆盖；数学转写完成与疑点解决分别管理。
'''
f=R/'翻译管理/疑难与勘误.md';f.write_text(f.read_text(encoding='utf-8')+issues,encoding='utf-8')
for rel,addition in [
 ('翻译管理/校订记录/2.4/局部约定卡.md','\n## 全节收尾（B126—B133）\n\n2/m六系数、m/m三关系及十二个源点场已核。χ为二阶非线性极化率，分量次序为输出/vis/ir；求和β/γ与传播β频率下标不同。1/m与m/1等层标随当地原式，方向缺标不补。体相i/δ照原文，δ在本文件此处未定义，不与旧译Δ等同。反射交叉频率相位和1/m、m/m混用不统一；时间、相位正负不跨节改写。\n'),
 ('翻译管理/符号与约定.md','\n## 2.4全节（B124—B133，2026-10-20）\n\n全部10页已核；L连接源极化x/y/z与出射s/p，χ采用二阶非线性极化率命名。频率下标β_m,SF/vis/ir是传播量，求和β、γ是分量指标。原式层标、方向、公共因子和i/δ保留；δ本独立文件此处未定义，不能把旧译iΔ作为约定。Q077—Q084只注未改，固定大小未配对括号保留可见原文而不补候选闭合。\n'),
 ('翻译管理/校订记录/2.4/结构与复用核验表.md','\n## 全节完成更新（2026-10-20）\n\n上表为起始调查历史状态，以下为当前有效结论：B124—B133已逐项核完所有单元，见全节单元覆盖.md。p1—10均对独立原图核验；28个编号式不是从母本状态直接认定。显著差异含P_y(00+)、m/1层标、7组基线2和缺i、12组孤立e、体相i/δ、交叉频率和混合L层标，全部有就地记录。\n')]:
 f=R/rel;f.write_text(f.read_text(encoding='utf-8')+addition,encoding='utf-8')
f=R/'中文版本/附件/原文勘误表.md';v=f.read_text(encoding='utf-8');key='## 后续维护';assert key in v
v=v.replace(key,'''## 第2.4节：薄膜产生的和频（表达式）

2026-10-20，B124—B133已完成独立底本全部10页。Q077—Q084及Q041关联项均保留原值、候选只放就地注，本轮没有采用原文修正，故不新增E编号。旧译iΔ修复为原文i/δ等属于转写校正，记录在本节校订与疑难表，不作为作者原文勘误。

'''+key);f.write_text(v,encoding='utf-8')
print('management updated; 28 tags and all scope assertions passed')

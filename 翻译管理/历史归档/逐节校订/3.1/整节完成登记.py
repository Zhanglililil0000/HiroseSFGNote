exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
import csv
s=P.read_text(encoding='utf-8');tags=re.findall(r'\\tag\{([^}]+)\}',s);expected=[f'2.{i}' for i in range(1,10)]+['2.10a','2.10b','2.11','2.12a','2.12b','2.13','2.14a','2.14b','2.15','2.16a','2.16b','2.17']+[f'2.{i}' for i in range(18,31)]+[f'2.{i}{x}' for i in range(31,47) for x in 'ab']+[f'3.{i}' for i in range(1,37)];assert tags==expected and len(tags)==len(set(tags))==102
summary='先规定振幅反射/透射系数及源点L系数，依次求二层系各界面与体相的电场乘积、和频极化及p/s出射场；随后推广到三层系的四个界面、三个体相位置，完整列出场乘积和极化，并给出可忽略中间层厚度时的替换关系。'
s=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** 全51页本轮译校与公式转写完成；B163—B190、B210—B227覆盖102个唯一编号式及无编号中间关系。旧译重复与省略已处理，原文疑点Q096—Q107、Q110—Q112保留并就地说明，未采用原文公式修正。',s)
s=re.sub(r'\*\*阅读导引（译者编写）：\*\*[^\n]+','**阅读导引（译者编写）：** '+summary+' 三层体系的完整辐射场作者未进一步求出；本译文保留这一范围限制，不把它计为漏译。',s)
# Make the new later issue notes mutually searchable in the global register.
qfile=M/'疑难与勘误.md';qtext=qfile.read_text(encoding='utf-8-sig')
for qid in ['Q106','Q107']:
 lines=[x[2:] for x in s.splitlines() if x.startswith('> **原文疑点（'+qid)]
 assert len(lines)==1
 if qid not in qtext:qtext+='\n\n'+lines[0]+'\n'
qfile.write_text(qtext,encoding='utf-8')
P.write_text(s,encoding='utf-8')
sourcehash=hashlib.sha256((R/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sourcehash=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
pagegroups={183:list(range(13,16)),184:list(range(15,18)),185:list(range(17,20)),186:list(range(19,22)),187:list(range(21,24)),188:list(range(23,26)),189:list(range(25,33)),190:list(range(32,38))}
for n,pages in zip(range(210,228),[[37,38],[38,39],[39,40],[40,41],[41],[41,42],[42,43],[43,44],[44,45],[45,46],[46],[46,47],[47,48],[48],[48,49],[49,50],[50,51],[51]]):pagegroups[n]=pages
batch_ids=[];index=[]
for f in sorted(O.glob('B*-覆盖.json')):
 c=json.loads(f.read_text(encoding='utf-8'));b=c['batch'];n=int(b[1:]);batch_ids.append(b)
 if n in pagegroups:c['pages']=pagegroups[n]
 c['source_sha256']=sourcehash
 fragment=(O/(b+'-本批译文.md')).read_text(encoding='utf-8');c['tags']=re.findall(r'\\tag\{([^}]+)\}',fragment);f.write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
 for tag in c['tags']:index.append({'tag':tag,'batch':b,'pages':c['pages']})
 # Final render acceptance is attached after continuous rendering is complete.
(O/'全节公式编号索引.json').write_text(json.dumps({'count':102,'tags':tags,'index':index},ensure_ascii=False,indent=2),encoding='utf-8')
(O/'全节公式编号索引.md').write_text('# 3.1全节公式编号索引\n\n共102个唯一编号式。2.1小节21式，2.2小节13式，2.3小节32式，三层系场乘积18式与极化18式。\n\n| 编号 | 批次 | PDF页范围 |\n| --- | --- | --- |\n'+''.join('| '+x['tag']+' | '+x['batch']+' | '+','.join(map(str,x['pages']))+' |\n' for x in index),encoding='utf-8')
append(O/'结构与复用核验表.md','## 全节最终状态（2026-10-20）\n\n全51页已覆盖。2.2余下由B178—B182接全；B183—B190重建二层系出射场，中间通式与四项积分展开保留；B210—B227补齐三层系36式。191—209未分配，不代表正文缺批。旧译8个重复编号及缺失公式已按原页处理。所有“待核/下一批”旧段落仅为历史记录。三层辐射场未被作者继续求出，按原文范围保留，不擅自补推导。')
append(O/'局部约定卡.md','## 全节约定汇总\n\n本节L为源极化到出射场的连接；保留公共因子省略及局部折射率条件。a/b及a0/b0按《一般式》引用使用；星号保留原记法，不泛化为共轭。体相部分作者重新说明相位路径处理，正文完整保留其声明与替换，不反向统一早先公式。无编号积分式的P定义与后续再次求和、δ归一化及印刷括号/字形疑点不自行消除。长式中指数乘积有分开书写、显式乘号与对齐分行，未引入新物理量简写；未将候选修正用于正文。')
append(M/'符号与约定.md','## 3.1全节衔接（2026-10-20）\n\n二层系1/m′/m/2与三层系1/m′/m/m″/2分别核对。2.3体相段作者指出早先相位路径处理欠缺并给出替换方式，应保留局部陈述；不据此静默修改2.1、2.2。a、b与a0/b0来自另篇《一般式》，后续3.2须独立核对。原P星号、δ及层坐标疑点仍按本节保留。')
f=M/'当前进度与续接.md';t=f.read_text(encoding='utf-8-sig');h,rest=t.split('\n',1);f.write_text(h+'\n\n## 当前有效状态：3.1全节完成（2026-10-20）\n\n全51页已完成本轮译校与公式转写：102个唯一编号式，所有界面、体相、积分通式及三层系36式齐备。补回旧译省略内容并消除重复编号。原文疑点Q096—Q107、Q110—Q112保留原值并就地说明，无原文公式修正采用。排版结果见3.1整节完成复核。\n\n下一批B228：进入3.2《双层膜和频的一般式》，13页，先核原文结构与局部约定、a/b及δ等定义和与3.1引用的对应，不能自动继承3.1已核状态。本次未开始3.2。以下为历史记录。\n'+rest,encoding='utf-8')
for f,key in [(M/'章节清单.tsv','编号'),(M/'全书调查/分批建议.tsv','节号')]:
 with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
 for row in rows:
  if row[key]=='3.1':
   if key=='编号':row.update({'状态':'本轮全51页译校与数学排版完成；原式疑点未决','映射核验':'全51页已按B163—B190、B210—B227对照','公式图表范围':'102个唯一编号式及无编号定义/中间推导已覆盖；无独立图表','导读状态':'已据全节内容更新Preface及第三章导航','导读草案':summary})
   else:row['执行状态']='2026-10-20全51页译校完成；102编号式与无编号推导齐备，见3.1整节完成复核；原式疑点保留'
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
f=R/'Preface序言.md';t=f.read_text(encoding='utf-8-sig');t=re.sub(r'(^- \[3\.1[^\n]+?\.md\))[^\n]*',lambda z:z[1]+'（全51页译校完成，102编号式）：'+summary,t,flags=re.M);f.write_text(t,encoding='utf-8')
f=P.parent/'阅读导航.md';t='''# 第三章阅读导航

本导航由译者编写。3.1全51页已完成本轮译校与数学排版；3.2仍待本轮校订。

## 3.1 二层膜及三层膜产生的和频光

[进入正文](3.1%20二层膜及三层膜产生的和频光.md)。102个唯一编号式及无编号推导齐备；文件路径沿用旧名。

1. 系数与源点场连接（p2—3）：s/p及轴向振幅反射/透射系数，L定义、方向和省略的公共因子。
2. 二层系电场乘积2.1（p3—9）：三个界面各自两侧，以及m′层、m层体相的正反向源，完整列单场和四项乘积。
3. 二层系和频极化2.2（p9—13）：按同样位置依次由二阶非线性极化率连接激发场，保留作者去相位振幅范围及P星号。
4. 二层系界面出射场2.3前部（p13—25）：依源点、反射/透射方向和p/s偏振选式；保留L连接的中间关系、局部折射率条件和上/下符号规则。
5. 二层系体相出射场2.3后部（p25—37）：作者说明早先相位路径处理的欠缺，重新给出积分路径、正反向贡献、通式及四项完整展开；两层各有反射与透射p/s表达式。
6. 三层系引入与薄中间层替换（p37—38）：说明未进一步求出完整三层辐射场，给出厚度可忽略层的系数替换。
7. 三层系电场乘积3.1（p38—45）：四个界面各侧及三个膜层体相的两种源分类，保留各处局部路径相位。
8. 三层系和频极化3.2（p45—51）：依同样位置完整列出18条极化式，至3.36结束。

建议先按层序、源点内外侧、传播方向与出射偏振选式，再核该组局部相位及L条件。原文疑点均保留并就地注明；译校完成不表示这些原式已经获得代数证明。

## 3.2 双层膜和频的一般式

[进入旧译](3.2%20双层膜和频的一般式.md)。13页，尚待本轮校订；下一步先核结构与局部定义。
''';f.write_text(t,encoding='utf-8')
f=R/'中文版本/附件/原文勘误表.md';t=f.read_text(encoding='utf-8-sig');marker='## 后续维护';t=t.replace(marker,'## 3.1全节疑点收录状态（2026-10-20）\n\n全51页已核；Q096—Q107、Q110—Q112均保留原式/原文，候选未采用，因此不新增已采用勘误条目。旧译漏式、重复、层标转写修复与长式排版见校订记录，不冒列为原文错误。后续确认后再按章节位置收录正式勘误。\n\n'+marker,1);f.write_text(t,encoding='utf-8')
print('102编号式与管理、导读已更新；待最终整节渲染验收')

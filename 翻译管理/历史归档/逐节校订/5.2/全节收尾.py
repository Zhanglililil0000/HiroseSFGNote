from pathlib import Path
from urllib.parse import unquote
import json,csv,io,re,hashlib
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
target=r/'中文版本/第五章 张量与对称性/5.2 主要点群的特征标表与基底.md'
idx=json.loads((o/'余部分批索引.json').read_text(encoding='utf-8'));audit=json.loads((o/'提取覆盖审计.json').read_text(encoding='utf-8'));render=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));full=json.loads((o/'全节排版检查.json').read_text(encoding='utf-8'))
assert len(idx)==38 and sum(x['表格'] for x in audit)==76
assert render['math']==3313 and len(render['results'])==39 and all(x['width']==x['scrollWidth'] and not x['overs'] for x in render['results'])
assert full['math']==3313 and len(full['tables'])==75 and full['width']==full['scrollWidth'] and not full['errors']
assert all(x['无丢失'] and x['无重复分配'] for x in audit)
body=target.read_text(encoding='utf-8');snapshot=(o/'B435前分批稿.md').read_text(encoding='utf-8')
oldbody=snapshot[snapshot.index('## 记号与适用范围'):].split('<!-- B434结束：')[0].strip();assert oldbody in body
src=r/'日语原版/Chapter5/chap5-2.pdf';sha=hashlib.sha256(src.read_bytes()).hexdigest();pagecoverage={1:['B434']}
for info in idx:
 b=info['批次'];bt=(o/(b+'-本批译文.md')).read_text(encoding='utf-8');assert bt.strip() in body
 p=o/(b+'验收.json');d=json.loads(p.read_text(encoding='utf-8'));assert hashlib.sha256(bt.encode('utf-8')).hexdigest()==d['translation_sha256'] and d['source_sha256']==sha
 d.update({'已排版':True,'数学片段':len(re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',bt)),'显示复核':'已查看批次排版总览；关键原式及末页另看原尺寸截图；合稿已检查，无横向溢出','复核性质':'模型原页及文字字形二次对照；不等同独立数学/物理认证'})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8');pagecoverage.setdefault(d['PDF页'],[]).append(b)
 (o/(b+'.md')).write_text('# '+b+'｜5.2 '+d['点群']+'\n\n日期：2026-10-21。PDF p'+str(d['PDF页'])+'，完整点群块。特征标表、基底分类表及其后全部分量/原注释已按原页对照。覆盖单元'+str(d['覆盖单元'])+'项，原字符记录'+str(d['字符数'])+'；源文件和译文摘要见验收JSON。\n\n数学显示检查通过，已查看参考排版。原空白、重复项、可疑下标和条件性分配说明分别保留，不将格式检查当作物理证明。各页原图及逐行覆盖JSON可追溯。无原文修正采用。\n',encoding='utf-8')
assert set(pagecoverage)==set(range(1,23))
qs=json.loads((o/'新增疑点.json').read_text(encoding='utf-8'));qs['Q210']['description']+=' p7 D₂d五字母下标及p14 C₃重复等式链另有就地续注。';qs['Q218']['description']+=' p18 Tₕ的平移/转动三元基底排在Eu行高度，保留原位置并另有续注。'
p=r/'翻译管理/疑难与勘误.md';t=p.read_text(encoding='utf-8')
for q,d in sorted(qs.items(),key=lambda x:int(x[0][1:])):
 if '## '+q+'｜' not in t:t+='\n\n## '+q+'｜5.2 PDF p'+str(d['page'])+' '+d['group']+'\n\n'+d['description']+'\n\n状态：待核验；原文保留，未采用修正。详见5.2正文就地说明及B435—B472覆盖记录。\n'
p.write_text(t,encoding='utf-8')
assert all('Q'+str(n) in body for n in range(209,221))
body=body.replace('数学显示及整节排版验收另见管理记录；原式疑点保留。','3313个数学片段及整节排版检查通过；Q209—Q220原文疑点保留，未采用修正。')
target.write_text(body,encoding='utf-8')
card='## 5.2全节约定补记（2026-10-21）\n\n特征标表使用xyz与T/R记号，分量表使用abc；本节未统一给出两者间的坐标映射，不直接将a/b/c等同x/y/z。E在特征标表头为恒等操作，在表示行可为简并表示；I为反演，g/u及撇号沿原表保留。V/D/Y/W上括号数字是不可约角动量阶数，β/γ按项目微观响应命名。基底副本未标编号者不补号。\n\n原空白、显式0、未列出、原省略号分别记录；原重复分量不合并。p18—20的distributed terms译“分配项（作者用语）”，并保留作者排除这些项的条件。p18 Tₕ和p21—22的列错位保留或分列记录，不作推测配对；p21拉丁P/D标签及p22全角ｇ均留原字形。p10/11角度中的点状字形按原印保留；圆圈角度符号用TeX角度记法显示。Q209—Q220未决，无原文修正采用。'
for p in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:
 t=p.read_text(encoding='utf-8')
 if card not in t:p.write_text(t.rstrip()+'\n\n'+card+'\n',encoding='utf-8')
p=r/'翻译管理/术语表.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['术语编号']=='T014' and '5.2全节' not in row['依据']:row['依据']+='；5.2全节特征标表原页及各点群名称已对照，中文沿用'
if not any(row['日语候选']=='distributed terms（底本英文）' for row in rows):
 n=max(int(re.search(r'\d+',x['术语编号']).group()) for x in rows)+1;row={f:'' for f in fields};row.update({'术语编号':f'T{n:03d}','日语候选':'distributed terms（底本英文）','英语辅助释义':'distributed terms','推荐中文候选':'分配项（作者用语）','定义与适用语境':'5.2高阶基底分配于多个不可约表示的条目；作者在随后的非零分量关系列表中明确不计这些项，不据此补全未给出的分配系数。','原文位置':'5.2 PDF p18—20 / B466—B470','依据':'原表及英文distributed over/terms已原页对照；非标准化命名声明','状态':'原词语境已核对；中文暂用','文本定位状态':'原页已对照','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'底本明确使用该英文，原引号未闭合已注'});rows.append(row)
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
(o/'术语卡.md').write_text('# 5.2术语卡\n\n沿用特征标表、基底张量、不可约表示、全对称表示，以及用户确定的极化率/超极化率命名。新增“分配项（作者用语）”的登记见主术语表。点群和表示字母为原符号，不以标准教材表静默改写原稿。全部g/u、撇号、星号、原空白及省略号与通常物理意义分开核对。\n',encoding='utf-8')
p=r/'翻译管理/章节清单.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['编号']=='5.2':row.update({'状态':'全22页完成本轮译校及参考排版（B434—B472）；Q209—Q220待核','映射核验':'22页均按原页对照；38点群块及76张原表已逐块记录','公式图表范围':'首页目录；38组特征标/基底及原分量关系；76原表，其中p21—22特征标表分列记录；3313数学片段排版通过','导读状态':'本轮正文核验后定稿；原表物理疑点未决','导读草案':'按点群查阅特征标、V/D/Y/W不可约基底及β/γ非零关系。保留高阶基底分配项的排除条件；p18和p21—22错位见Q218，不推测配对。'})
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8').replace('**本章导读（5.1已核，其余暂定）：** 5.1建立张量基底、对称性约束与坐标变换的阅读基础；后续5.2—5.6的表格及变换资料仍待逐节译校。','**本章导读（5.1—5.2已核，其余暂定）：** 5.1建立张量基底、对称性约束与坐标变换的基础；5.2按点群查阅特征标、基底归属及非零分量，5.3—5.6仍待译校。')
t=re.sub(r'(- \[5\.2 主要点群的特征标表与基底\]\([^\n]+?\))（翻译中，p1/22已完成）：[^\n]+',r'\1（全22页完成本轮译校）：含38个点群块的特征标、不可约基底及原有非零分量关系。高阶基底“分配项”的排除条件及错位表均有说明；Q209—Q220保留待核，p21—22按列记录，不能推测配对。',t);p.write_text(t,encoding='utf-8')
p=r/'中文版本/第五章 张量与对称性/阅读导航.md';t=p.read_text(encoding='utf-8').replace('本章5.1已完成本轮译校及排版，5.2已完成首页，5.3—5.6尚未开始；全章尚未完成。','本章5.1—5.2已完成本轮译校及排版；5.3—5.6尚未开始，全章尚未完成。')
t=re.sub(r'- \[5\.2 主要点群的特征标表与基底\][^\n]+','- [5.2 主要点群的特征标表与基底](5.2%20主要点群的特征标表与基底.md)：全22页完成，按38个点群块查特征标、V/D/Y/W基底及β/γ关系。p18—20保留高阶分配项限制；p18 Tₕ及p21—22列错位见Q218，末两页分列记录。Q209—Q220未决。',t)
t=t.replace('## 后续小节（标题级导读，待核验）','## 5.2及后续小节')
t+='\n\n### 5.2查阅建议（全节完成）\n\n先确认页首V/D/Y/W及响应阶数，再按原目录找点群。特征标与基底分类分别核验，abc与xyz不直接逐字母等同。空白不能当零，原重复项不能当独立分量数量的证明。p18—20的分配项条件及p21—22的分列记录尤其需要连同注释阅读。下一节5.3，共16页，尚未开始。\n';p.write_text(t,encoding='utf-8')
plan=['# 5.2分批记录（全节完成）','','底本22页。B434覆盖首页，其余按完整点群块分为B435—B472，共39批。完成仅指本轮翻译、原页对照及显示检查；不代表所有选择规则已获独立证明。','','| 批次 | PDF页 | 点群 | 状态 |','|---|---|---|---|','| B434 | 1 | 说明及完整目录 | 完成 |']
plan += ['| '+x['批次']+' | '+str(x['PDF页'])+' | '+x['点群']+' | 完成 |' for x in idx]
plan += ['','原表76张：38张特征标表、38张基底分类表；p21—22两张特征标表按原列独立记录，合稿因此为75个Markdown表格（含首页目录）及分列条目。全部原表有逐行覆盖记录。','','下一批B473属于5.3《从分子固定坐标系到空间固定坐标系》，先核首页与全节结构，不能将本节完成状态转移过去。']
(o/'结构与分批计划.md').write_text('\n'.join(plan)+'\n',encoding='utf-8')
coverage={'底本页数':22,'页覆盖':pagecoverage,'点群块':38,'原表格':76,'原表逐行覆盖记录':sum(x['覆盖单元'] for x in idx),'原字形数':sum(x['字形数'] for x in audit),'字形分配无漏无重':True,'数学片段':3313,'Markdown表格':75,'未决疑点':['Q'+str(n) for n in range(209,221)],'采用原文修正':False,'原稿限制':'高阶分配项系数未补；错位表未推测配对；空白未当零','说明':'字形覆盖审计保证转录对象有去向，不等同于独立物理审校。'}
(o/'全节覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
report=['# 5.2全节验收','','2026-10-21。全22页、B434—B472共39批，完成本轮翻译、原页对照与参考排版。','','- 首页说明、21页组目录完整；38个点群块均覆盖。','- 76张原表逐行记录，数学均为可编辑文字；p21—22错位特征标表分列，未推测重配。合稿75个Markdown表格含首页目录。','- 所有原示例、方向说明、非零分量关系、重复项及高阶分配条件均有去向。原字形分配无漏无重；完整性审计不代替物理证明。','- 3313个数学片段严格语法检查通过；全部批次排版已总览，关键表及合稿已抽查，页面无横向溢出。','- Q209—Q220均就地注明并登记问题表；原文保留，未采用候选修正，勘误附件无新增已采用项。','- 原稿存在反演标记、特征标符号、五字母下标、重复项、行位及高阶分配等未决问题。不能据译校完成状态直接采用所有表项计算。','','## 续接','','5.3《从分子固定坐标系到空间固定坐标系》，16页，尚未开始。下一批B473先核原题、结构及局部坐标约定。','','历史批次B434的哈希及状态保留其时点含义；最终合稿哈希见同名JSON。原表可通过页图、表格字形JSON、逐行覆盖及批次译文追溯。']
(o/'全节验收.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
final={'状态':'全22页完成本轮译校及参考排版','日期':'2026-10-21','source_sha256':sha,'canonical_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'批次':[f'B{n}' for n in range(434,473)],**coverage,'下一批':'B473，5.3首页及结构；5.3尚未开始'}
(o/'全节验收.json').write_text(json.dumps(final,ensure_ascii=False,indent=2),encoding='utf-8')
p=r/'翻译管理/当前进度与续接.md';t=p.read_text(encoding='utf-8');note='## 当前有效状态：5.2全节完成（2026-10-21）\n\n5.2《主要点群的特征标表与基底》全22页已按B434—B472共39批完成本轮译校及参考排版。本轮B435—B472覆盖38点群块、76原表及其后全部分量关系/注释；p21—22错位特征标表按列独立记录，未推测配对。3313数学片段语法通过，批次及合稿显示已复核，页面无横向溢出。Q209—Q220原文疑点保留，未采用原文修正；术语、符号、问题表、章节清单、序言和导航均已更新。详见校订记录/5.2/全节验收.md。\n\n下一节5.3《从分子固定坐标系到空间固定坐标系》，16页，尚未开始。下一批B473：先核首页及全节结构，登记分子/空间坐标和变换方向，再选择完整定义或公式组推进。用户本轮指定5.2已完成。\n\n以下为历史记录。\n\n'
if note not in t:p.write_text(t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+note,1),encoding='utf-8')
print(json.dumps({'状态':'5.2完成','点群':38,'原表':76,'覆盖行/注释':coverage['原表逐行覆盖记录'],'原字形':coverage['原字形数'],'数学':3313,'下一批':'B473，5.3'},ensure_ascii=False))

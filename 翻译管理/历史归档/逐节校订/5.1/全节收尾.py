from pathlib import Path
from urllib.parse import unquote
import json,re,csv,io,hashlib
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
p=r/'中文版本/第五章 张量与对称性/5.1 和频张量与对称性.md';t=p.read_text(encoding='utf-8')
assert '未翻译' not in t and '分批稿' not in t
manifest=json.loads((o/'式5逐项清单.json').read_text(encoding='utf-8'))
assert len(manifest)==27 and {x['component'] for x in manifest}=={a+b+c for a in 'xyz' for b in 'xyz' for c in 'xyz'}
expected=['1a','1b','1c','2','3','4a','4b','5a','5b','5c','B1','B2','C1','C2a','C2b','C2c']
assert re.findall(r'\\tag\{([^}]+)\}',t)==expected
assert all('Q'+str(q) in t for q in range(198,209))
assert all('## 附录'+x in t for x in 'ABC')
assert sum(line.startswith('|---') for line in t.splitlines())==2
full=json.loads((o/'全节排版检查.json').read_text(encoding='utf-8'));assert full['math']==200 and not full['errors'] and not full['overs'] and full['width']==full['scrollWidth']
for n in range(425,434):
 b=f'B{n}';bp=o/(b+'-本批译文.md');bt=bp.read_text(encoding='utf-8');rp=o/(b+'验收.json');d=json.loads(rp.read_text(encoding='utf-8'))
 assert hashlib.sha256(bt.encode('utf-8')).hexdigest()==d['translation_sha256']
 d.update({'已排版':True,'本批数学片段':len(re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',bt)),'显示复核':'已查看本批参考截图；合稿亦已检查；无横向溢出'})
 rp.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
 note='\n排版验收通过：本批参考截图已视觉核对；累计200数学片段严格语法检查通过，合稿含两张表，全部16个编号组保留，无横向溢出。\n'
 q=o/(b+'.md');old=q.read_text(encoding='utf-8')
 if note not in old:q.write_text(old+note,encoding='utf-8')
# All final outputs refer to the accepted canonical draft, not earlier batch snapshots.
t=t.replace('整节排版验收结果另见管理记录。','200个数学片段严格语法检查、批次及整节参考排版检查均已通过。')
p.write_text(t,encoding='utf-8')
pages={1:['B423'],2:['B424','B425'],3:['B426','B427'],4:['B427','B428','B429','B430'],5:['B430'],6:['B431','B432'],7:['B432','B433']}
coverage={'pages':[{'PDF页':k,'覆盖批次':v,'已原页对照':True} for k,v in pages.items()],'公式编号组':expected,'式5分量数':27,'式2基底分量数':9,'附录B基底数':9,'表格数':2,'附录':['A','B','C'],'书目':'Bunker 1979，位于附录A','原图数':0,'原文修正采用数':0,'疑点':['Q'+str(q) for q in range(198,209)]}
(o/'全节覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# 5.1全节验收','','日期：2026-10-21。底本7页，B423—B433完成。完成指本轮翻译、原页对照及排版复核，不表示所有原式均经独立物理认证。','','- 正文：引言及order/rank区分、线性极化与九个不可约基底、C₃ᵥ两张表、表示乘积与非零分量关系。','- 式(5a)—(5c)：每组9个分量，共27个xyz三指标组合，无重无漏；原跨页次序保留。','- 附录A—C：含Bunker书目、坐标及欧拉角变换、极／轴矢量及星号、九个二指标基底、绕z旋转和基底乘积规则。','- 200个数学片段严格语法检查通过；全部批次截图及合稿抽查已查看。两张表、16个公式编号组齐全，内容宽度1100与视口相同，无横向溢出。','- Q198—Q208均就地说明，保留原文，未采用候选；本轮无新增已采用原文修正，勘误附件不增列已确认项。缺括号、孤立竖线和原重复项均有说明。','- 本节指标数／不可约角动量阶数与响应阶数分开；I为反演矩阵，ε为行列式，左上星号表轴性变换。','- 历史B423/B424验收哈希保持当时批次及合稿含义；当前合稿摘要见全节验收JSON。','','## 分页覆盖','','| PDF页 | 批次 |','|---|---|']
lines += ['| '+str(k)+' | '+'、'.join(v)+' |' for k,v in pages.items()]
lines += ['','下一节：5.2《基底与特征标表》，22页。下一批编号B434，先核首页说明及页组结构；点群表原则上逐页核对。5.2尚未开始。']
(o/'全节验收.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
plan=['# 5.1结构与分批记录','','状态：全7页完成本轮译校及排版复核。页码为PDF页码；物理疑点保留。','','| 批次 | 原文范围 | 状态 |','|---|---|---|','| B423 | p1全页 | 完成 |','| B424 | p2首至式(2) | 完成 |','| B425 | p2 C₃ᵥ引言、表1/表2及注释 | 完成 |','| B426 | p3首至式(5)引言，含式(3)/(4) | 完成 |','| B427 | p3—4式(5a)九分量 | 完成 |','| B428 | p4式(5b)九分量 | 完成 |','| B429 | p4式(5c)九分量 | 完成 |','| B430 | p4附录A及p5附录B | 完成 |','| B431 | p6首欧拉角至基底前记号说明 | 完成 |','| B432 | p6—7二指标基底及末段引用 | 完成 |','| B433 | p7附录C至文末 | 完成 |','','详见全节覆盖JSON及全节验收。下一批B434属于5.2，不再扩展本节范围。']
(o/'结构与分批计划.md').write_text('\n'.join(plan)+'\n',encoding='utf-8')
# Glossary: keep provisional translation decisions distinct from user confirmation.
p=r/'翻译管理/术语表.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['术语编号']=='T093':row['定义与适用语境']=row['定义与适用语境'].replace('附录A尚未译校。','附录A p4已译校，说明等价构型与Hamilton算符不变。');row['原文位置']='5.1 p1及附录A p4 / B423、B430'
 if row['术语编号']=='T094':row['原文位置']='5.1 p2首段及附录B p6 / B424、B431';row['定义与适用语境']+=' B431已与轴矢量并列核对。'
 if row['术语编号'] in ['T014','T042','T076']:
  if '5.1本轮' not in row['依据']:row['依据']+='；5.1本轮B425—B426已对照相关原词与表格语境，中文继续沿用'
newterms=[('軸性ベクトル','axial vector','轴矢量','p6：角动量及磁场矢量；变换矩阵相对极矢量多乘ε，左上星号区分。'),('回映','rotoreflection','旋转反射','p6—7：与镜映并列，不能仅用正旋转欧拉角矩阵表示。'),('基底テンソル','basis tensor','基底张量','p2、p6—7：张量分量的不可约线性组合；原文另有同名文件引用。')]
n=max(int(re.search(r'\d+',x['术语编号']).group()) for x in rows)
for jp,en,zh,desc in newterms:
 if any(x['日语候选']==jp for x in rows):continue
 n+=1;row={x:'' for x in fields};row.update({'术语编号':f'T{n:03d}','日语候选':jp,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':desc,'原文位置':'5.1 / B425—B433，见定义中的页码','依据':'原词及语境已页面核对；中文为译者暂用','状态':'原词已核对；中文暂用','文本定位状态':'本轮原页对照完成','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'译者辅助对应，非底本本句所列英文'});rows.append(row)
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
card='## 5.1全节约定补记（2026-10-21）\n\n本节order为指标数，rank为不可约角动量阶数。β、γ上方括号数字为不可约阶数，不与一阶／二阶超极化率的响应命名混用。表2采用x轴含于镜面的题注，式4后另给x/y互换说明，均保留并见Q201。式5的02b,1前导0不删。附录B先给单轴矩阵，再给Rz(χ)Ry′(θ)RZ(φ)及原展开矩阵；展开九元素仅为排版拆分，不采纳常见欧拉角替换。I为反演矩阵、ε=det D，左上*表示变换矩阵额外乘ε。附录C保留m/n下标、C2的符号、孤立竖线及重复项，疑点Q207/Q208未决。'
for p in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:
 old=p.read_text(encoding='utf-8')
 if card not in old:p.write_text(old.rstrip()+'\n\n'+card+'\n',encoding='utf-8')
(o/'术语卡.md').write_text('# 5.1术语卡\n\n术语表是唯一登记处，此处只作索引。沿用特征标表、不可约表示、全对称表示；本节定义的指标数、不可约角动量阶数见T091/T092，置换反演群见T093，极矢量见T094。轴矢量、旋转反射、基底张量已补入术语表，均标译者暂用，未冒称用户确认。\n\n“2倍音”在p3译为“二倍频带”，不误作第二泛频。β/γ的张量指标数及不可约分量阶数与用户确认的分子响应命名分别处理。\n',encoding='utf-8')
p=r/'翻译管理/章节清单.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['编号']=='5.1':row.update({'状态':'全7页完成本轮译校及参考排版（B423—B433）；Q198—Q208待核','映射核验':'全7页已逐页对照日语原版；首次新译，无既有中文正文','公式图表范围':'两表；16个编号式组；式5共27分量；附录A—C及Bunker书目齐全；200数学片段排版通过','导读状态':'本轮正文核验后定稿；原式物理疑点未决','导读草案':'由线性极化的不可约基底说明C3v对称性约束，列出三指标张量27分量；附录A—C给出置换反演、坐标变换和基底乘积规则。使用欧拉矩阵及乘积规则时须并读Q204、Q207、Q208。'})
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8');t=t.replace('**本章导读（待正文核验）：** 集中阅读张量、对称性、基底和坐标变换。','**本章导读（5.1已核，其余暂定）：** 5.1建立张量基底、对称性约束与坐标变换的阅读基础；后续5.2—5.6的表格及变换资料仍待逐节译校。')
t=re.sub(r'(- \[5\.1 和频张量与对称性\]\([^\n]+?\))（翻译中，已至p2式\(2\)）：[^\n]+',r'\1（全7页完成本轮译校）：由不可约基底说明C₃ᵥ对称性约束，完整列出27个三指标张量分量；附录A—C说明置换反演群、坐标变换及基底乘积。Q198—Q208原式疑点保留，使用相关公式时须并读注释。',t)
p.write_text(t,encoding='utf-8')
p=r/'中文版本/第五章 张量与对称性/阅读导航.md';p.write_text('# 第五章阅读导航\n\n本章5.1已完成本轮译校及排版，5.2—5.6尚未开始；全章尚未完成。\n\n## 5.1 和频张量与对称性\n\n[进入正文](5.1%20和频张量与对称性.md)。全7页，B423—B433。\n\n1. 引言及线性极化：先区分指标数和不可约角动量阶数，理解对称性等价构型与全对称条件。\n2. 式(1)—(2)：连接笛卡尔分量与1+3+5个不可约基底；式(1a)符号疑点见Q200。\n3. C₃ᵥ实例：两张特征标／基底表及表示乘积，导出式(3)/(4)非零关系；镜面与振动分量范围见Q201/Q202。\n4. 式(5a)—(5c)：共27分量；保留原顺序、下标及可疑前导0。\n5. 附录A：置换反演群的出发点及Bunker书目。\n6. 附录B：坐标、单轴旋转、欧拉角、极／轴矢量及九个二指标基底。原欧拉矩阵和缺括号等问题见Q204—Q206。\n7. 附录C：绕z旋转及基底乘积；n/m下标与乘积符号疑点见Q207/Q208。\n\n本轮完成原页对照和数学显示检查；Q198—Q208仍未决，没有采用原文修正。不得据完成状态将所有公式视为已获独立物理证明。\n\n## 后续小节（标题级导读，待核验）\n\n- 5.2 基底与特征标表：22页，下一节；点群表按页核对。\n- 5.3 从分子固定坐标系到空间固定坐标系：待翻译。\n- 5.4 基底张量：待翻译。\n- 5.5 变换矩阵（基底）：待翻译。\n- 5.6 变换矩阵（xyz）：待翻译。\n',encoding='utf-8')
p=r/'翻译管理/当前进度与续接.md';t=p.read_text(encoding='utf-8');marker='## 当前有效状态：5.1全节完成（2026-10-21）\n\n5.1《和频张量与对称性》全7页已按B423—B433完成本轮译校、原页对照及参考排版。本轮B425—B433处理两张表、式(3)/(4)、式(5a)—(5c)全部27分量及附录A—C。全节200数学片段严格语法检查通过，16个编号组齐全，批次及合稿截图已复核，无横向溢出。Q198—Q208保留原文，候选未采用；本轮无新增已采用原文修正。术语、符号、问题表、章节清单、序言及第五章导航已更新。详见校订记录/5.1/全节验收.md。\n\n下一节5.2《基底与特征标表》，22页，尚未开始。下一批B434：先核首页说明和全节表格分组，再按完整点群表逐页推进；不要将5.1的完成状态转移到5.2。用户本轮指定范围5.1已完成。\n\n以下为历史记录。\n\n'
if marker not in t:p.write_text(t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+marker,1),encoding='utf-8')
final={'日期':'2026-10-21','状态':'全7页完成本轮译校及参考排版','批次':[f'B{n}' for n in range(423,434)],'source_sha256':hashlib.sha256((r/'日语原版/Chapter5/chap5-1.pdf').read_bytes()).hexdigest(),'canonical_sha256':hashlib.sha256((r/'中文版本/第五章 张量与对称性/5.1 和频张量与对称性.md').read_bytes()).hexdigest(),'math':200,'编号式组':expected,'页覆盖':pages,'未决疑点':['Q'+str(q) for q in range(198,209)],'采用原文修正':False,'下一批':'B434，5.2首页及表格结构；5.2尚未开始','限制':'译校及格式完成不代表独立物理审校；历史批次哈希保持时点含义。'}
(o/'全节验收.json').write_text(json.dumps(final,ensure_ascii=False,indent=2),encoding='utf-8')
print('5.1完成；7页、11批、27分量、2表、16编号组；Q198—Q208未决。')

from pathlib import Path
import json,hashlib,re,csv,io
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;target=r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md'
rec=json.loads((o/'B566验收.json').read_text(encoding='utf-8'));rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));chunk=(o/'B566-本批译文.md').read_text(encoding='utf-8');t=target.read_text(encoding='utf-8')
assert hashlib.sha256(chunk.encode('utf-8')).hexdigest()==rec['translation_sha256']
assert chunk in t and '\\tag{1.5}' not in t
assert hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest()==rec['source_sha256']
assert rr['math']==100 and next(x for x in rr['results'] if x['batch']=='B566')['overs']==[]
assert next(x for x in rr['results'] if x['batch']=='B566')['scrollWidth']==1100
assert len(json.loads((o/'B566-覆盖.json').read_text(encoding='utf-8')))==12
assert (o/'B566-目视1.png').exists()
rec.update({'已排版':True,'本批数学片段':28,'累计批次数学片段':100,'截图全幅目视':True,'横向溢出':False,'已完成整页p4':False})
(o/'B566验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
p=o/'B566.md';p.write_text(p.read_text(encoding='utf-8')+'\n排版验收：新增28个数学片段，累计100个片段语法通过；B566完整截图已目视，矩阵元上下标、式号和分母括号正常，无横向溢出。p4后段未计完成。\n',encoding='utf-8')
p=r/'翻译管理/疑难与勘误.md';s=p.read_text(encoding='utf-8')
qs=[('Q232','6.1 PDF p4式(1.3)及其后能量差句','底本前因子e²/h及hωng使用普通h字形。保留h；未改ħ、未加2π，常数约定待结合后文核验。原页与局部放大图已对照。'),('Q233','6.1 PDF p4式(1.4)前的r/q比较段','原文把量子论r视为与经典q“相同内容”，但未给出矩阵元乘积与q²的定量替换规则；还需考虑e²/h及ρg^(0)等。保留原文比较，不令r=q、不替换量纲。')]
for q,loc,desc in qs:
 assert not re.search(r'^## '+q+r'\b',s,re.M),q
 s+=f'\n\n## {q}｜{loc}\n\n{desc}\n\n状态：原文保留、待核验；未采用原文修正。正文有就地说明，来源B566。\n'
p.write_text(s,encoding='utf-8')
p=r/'中文版本/附件/原文勘误表.md';s=p.read_text(encoding='utf-8');s+='\n\n### 6.1 B566新增待核索引\n\n| 原位置 | 问题号 | 处理 |\n|---|---|---|\n| p4式(1.3)及能量差句 | Q232 | 保留普通h，不改ħ或增补2π |\n| p4式(1.4)前比较段 | Q233 | 保留r/q的原文形式比较，不作数值替换 |\n\n无新增已采用的原文修正；以上不分配E编号。两项均见[6.1正文](../第六章%20偶极间相互作用/6.1%20偶极间相互作用.md)就地说明。\n';p.write_text(s,encoding='utf-8')
p=o/'局部约定卡.md';s=p.read_text(encoding='utf-8');s+='\n\n## B566补充（PDF p4前两个论述单元）\n\n- 本处χij^(1)=Pi^(1)/Ej，称线性极化率；保留求和gn及ρg^(0)，N及归一化条件未自行补定。\n- 原文明确对应exp(-iωt)部分，与式(1.2a)第二项比较；幅度前因子与取实部归一化不自动省略。\n- h为普通h，见Q232；不默认改ħ。原r/q形式比较见Q233，不作数值等同或量纲替换。\n- Γng与γ分开保留；后续关系尚未译校。式(1.4)末分母为ω²−(ωng²+Γng²)+2iωΓng，括号内两项均受前方负号作用。\n';p.write_text(s,encoding='utf-8')
p=r/'翻译管理/符号与约定.md';s=p.read_text(encoding='utf-8');s+='\n\n### 6.1 p4量子/经典对应（B566）\n\nχij^(1)=Pi^(1)/Ej；式(1.3)含Ne²/h、Σgn及ρg^(0)。h按底本普通字形保留（Q232）；r/q仅按原文比较（Q233）。本处作者指定exp(-iωt)部分；经典式(1.2a)第二项与之对照，ωo仍依Q231保留。Γng与γ关系、N的计数/密度和前因子归一化待后文，不据形式相似先补相等式。\n';p.write_text(s,encoding='utf-8')
(o/'B566术语核对.md').write_text('# B566术语核对\n\n使用既有线性极化率命名（T005及用户响应阶数决定），未另建同义条目。分子β/γ超极化率条目不用于此处经典阻尼γ。没有新增需定稿的术语；h、r/q及Γng属于局部符号与待核问题，分别入约定卡和Q232—Q233，不把疑点存入已核验对照语料。\n',encoding='utf-8')
p=r/'中文版本/第六章 偶极间相互作用/阅读导航.md';s=p.read_text(encoding='utf-8').replace('B565完成p1—3，后续p4—55待译。','B565完成p1—3；B566完成p4中1.2的前两个论述单元。p4后段及p5—55待译。')
s=s.replace('## 后续目录级预览（尚待正文核验）','- p4的1.2前两部分：量子论线性极化率、原文Shen引书、exp(-iωt)约定和经典对应式(1.4)。Q232—Q233保留；普通h与r/q比较不自行改写。\n\n## 后续目录级预览（尚待正文核验）')
s=s.replace('1. 1.2—1.4（p4—13）：线性极化率，以及线性/非线性吸收和发光；下一批入口为1.2。','1. 1.2后段—1.4（p4—13）：量子/经典结果差异，以及线性/非线性吸收和发光；下一批从p4的结果差异小标题开始。')
s=re.sub(r'下一批B566：[\s\S]*$', '下一批B567：从p4“量子论与经典论结果的差异”起。式(1.5)及引出p5密度矩阵运动方程(1.6)的句子按完整跨页论述划界，不把p4半页视作整页完成。保留前批相位、幅度、h及Γ/γ约定。\n',s)
p.write_text(s,encoding='utf-8')
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('目前p1—3已译校。先用经典阻尼振子建立电场、偶极矩和频率约定；','目前p1—3及p4前两个论述单元已译校。先用经典阻尼振子建立电场、偶极矩和频率约定，再比较量子线性响应；')
s=s.replace('（翻译中，p1—3/55已完成）：原目录、引言和1.1经典模型已译校，包括正负频率及取实部脚注；注意β/γ的阻尼用法，Q229—Q231保留。','（翻译中，p1—3及p4部分完成）：原目录、引言、1.1及脚注已译校；1.2完成量子线性响应与经典对应式(1.3)—(1.4)。注意时间因子与阻尼符号，Q229—Q233保留。')
p.write_text(s,encoding='utf-8')
p=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='6.1':
  assert row['原文SHA256']==rec['source_sha256']
  row.update({'状态':'翻译中：B565完成p1—3；B566完成p4的1.2前两个论述单元，均已对照排版','映射核验':'原题/目录、引言、1.1及1.2量子式和经典对应部分已核；p4后段起待译','公式图表范围':'已核式(1.1a/b)、(1.2a/b)、(1.3)—(1.4)及对应无编号式；式(1.5)起待译','导读状态':'分批导读，更新至B566','导读草案':'从经典阻尼振子、正负频率和取实部约定推进到量子线性响应与经典形式比较。h、r/q及前因子保持原文；结果差异、相互作用及镜像部分待后文。'})
out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(out.getvalue().encode('utf-8'))
p=r/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8').replace('## 当前有效状态：6.1首批B565完成','## 历史状态：6.1首批B565完成',1)
intro='## 当前有效状态：6.1 B566完成，推进至p4部分（2026-10-21）\n\nB566完成1.2的“量子论给出的极化率公式”及“经典论公式与量子论公式的对应关系”，至式(1.4)后对应段末，共12个覆盖单元、2个编号式、1条原引文。新增28个数学片段、累计100个片段语法通过；本批完整排版截图已目视，无横向溢出。Q232普通h及Q233 r/q比较保留原文并就地说明，未采用原文修正。符号卡、问题表、勘误附件索引、序言、导航和章节清单已更新。\n\n累计完成p1—3及p4前两个论述单元；p4尚未全页完成。下一批B567：从同页“量子论与经典论结果的差异”起，式(1.5)及引出p5式(1.6)的句子按完整跨页论述处理；后续本节尚未完成。不得先把Γng=γ、h=ħ或r=q当成已确认约定，原Q229—Q231仍保留。\n\n'
s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+intro,1);p.write_text(s,encoding='utf-8')
p=o/'结构与分批计划.md';s=p.read_text(encoding='utf-8').replace('| 1.2线性极化率 | 4—9 | 待译 |','| 1.2线性极化率 | 4—9 | B566完成p4前两部分；结果差异小标题起待译 |');s+='\n\nB566完成后续接：B567自p4“量子论与经典论结果的差异”开始，式(1.5)和密度矩阵方程引句跨页；不能把“下式”引句截成已完成论述。已完成式(1.3)—(1.4)，未完成式(1.5)。\n';p.write_text(s,encoding='utf-8')
checks={'批次':'B566','本批完成':True,'新增覆盖单元':12,'新增编号式':2,'新增数学片段':28,'累计数学片段':100,'截图全幅目视':True,'源与批次摘要匹配':True,'批次内容在合稿中':True,'p4全页完成':False,'采用原文修正':False,'下一批':'B567'}
(o/'B566最终检查.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print('B566验收完成：p4前两个单元已译校；式(1.5)起待译。')

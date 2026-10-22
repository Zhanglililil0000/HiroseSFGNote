from pathlib import Path
import json,hashlib,csv,io,re
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;target=r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md';chunk=(o/'B567-本批译文.md').read_text(encoding='utf-8');a=json.loads((o/'B567验收.json').read_text(encoding='utf-8'));rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));metric=next(x for x in rr['results'] if x['batch']=='B567')
assert rr['math']==125 and not metric['overs'] and metric['scrollWidth']==1100
assert hashlib.sha256(chunk.encode('utf-8')).hexdigest()==a['translation_sha256']
assert hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest()==a['source_sha256']
assert len(json.loads((o/'B567-覆盖.json').read_text(encoding='utf-8')))==16
assert all((o/f'B567-目视{i}.png').exists() for i in [1,2])
t=target.read_text(encoding='utf-8');assert chunk in t and '\\tag{1.10}' not in t
t=t.replace('### 1.2 线性极化率（PDF p4起；本批为前两个论述单元）','### 1.2 线性极化率（PDF p4起；分批译稿）');target.write_text(t,encoding='utf-8')
a.update({'已排版':True,'本批数学片段':25,'累计数学片段':125,'截图全幅目视':True,'横向溢出':False,'累计页界':'p1—5完整；p6仅广濑笔记接续段','整节完成':False})
(o/'B567验收.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=o/'B567.md';p.write_text(p.read_text(encoding='utf-8')+'\n排版验收：新增25个数学片段、累计125个片段语法通过。完整排版截图分2段均已目视，编号、Γρ次序、撇号及文献行正常，无横向溢出。\n',encoding='utf-8')
p=r/'翻译管理/疑难与勘误.md';t=p.read_text(encoding='utf-8')
qs=[('Q234','p4式(1.5)后实部“一致”','按(1.5)形式替换，(1.4)末分母实部为ω²−ω0²；(1.2a)第二项为ωo²−ω²。若o与0对应，两者反号。保留原“一致”，不改分子负号；Q231仍未决。'),('Q235','p6广濑笔记首行普通算符乘积','原∑n″ Γn,n″ρn″,n的末下标为n，而前页弛豫式使用(n,n′)。若比较同一矩阵元，候选末项ρn″,n′；候选未采用。'),('Q236','p6广濑笔记括注乘积次序','原写(1/2)(Γρ+Γρ)，而(1.6)为(1/2)(Γρ+ρΓ)。重复Γρ及“物理完全相同”均照录，不自动互换第二项；逐元弛豫与算符乘积含义分开。')]
for q,loc,desc in qs:
 assert not re.search(r'^## '+q+r'\b',t,re.M)
 t+=f'\n\n## {q}｜6.1 {loc}\n\n{desc}\n\n状态：原文保留、待核验；未采用原文修正。正文有就地说明，来源B567。\n'
p.write_text(t,encoding='utf-8')
p=r/'中文版本/附件/原文勘误表.md';t=p.read_text(encoding='utf-8');t+='\n\n### 6.1 B567新增待核索引\n\n| 原位置 | 问题号 | 处理 |\n|---|---|---|\n| p4式(1.5)后 | Q234 | 保留分母实部“一致”的原文判断，注明符号差异 |\n| p6笔记普通乘积 | Q235 | 保留末下标n，候选n′未采用 |\n| p6笔记括注 | Q236 | 保留重复Γρ及原等价判断，不调换次序 |\n\n以上均未采用原文修正，不分配E编号；详见[6.1正文](../第六章%20偶极间相互作用/6.1%20偶极间相互作用.md)。\n';p.write_text(t,encoding='utf-8')
symbols='\n\n## B567补充：量子自由响应与笔记（p4—p6开头）\n\n- (1.5)为ω0²=Γng²+ωng²；分母实部“一致”的符号问题依Q234保留。\n- (1.6)按普通h及Γρ+ρΓ次序；(1.7)v=i(ρng−ρgn)，为布洛赫y分量，拉丁v不改为希腊ν。\n- (1.8)含2Γng乘一阶导数、ωng²+Γng²；(1.9)仅为原时间形式，未增补任意幅度或相位。\n- 原笔记给Γng=Γgn条件及纵向弛豫γ=2Γng。此γ不得先与1.1经典β/(2m)的γ视为同一参数；后续经典对应仍待原文核对。\n- 原笔记的逐元弛豫式(∂ρn,n′/∂t)relax=−Γn,n′ρn,n′不作普通算符乘法解释；原求和下标与重复Γρ依Q235—Q236保留。\n- FID沿原日语“自由誘導緩和”暂译自由感应弛豫；底本只列缩写。旋波近似、布洛赫矢量、刘维尔空间及纵/横向弛豫为暂用译名；作者关于近似的“我认为”等语气完整保留。\n'
for p in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:
 p.write_text(p.read_text(encoding='utf-8')+symbols,encoding='utf-8')
def save_tsv(p,fields,rows):
 b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(b.getvalue().encode('utf-8'))
p=r/'翻译管理/术语表.tsv';rd=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['术语编号']=='T082':row['定义与适用语境']+=' 6.1 p5笔记纵向弛豫γ亦非超极化率；与经典阻尼γ的关系另核。'
terms=[('T107','自由誘導緩和（FID）','FID（底本缩写；未列英文全称）','自由感应弛豫（按原词暂译）','6.1 p5式(1.7)前 / B567','外场消失后追踪受驱振子极化；原文引入旋波近似，不擅改作者用词。'),('T108','回転波近似','rotating-wave approximation','旋波近似','6.1 p5 / B567','作者在量子自由响应推导中引入；具体操作待后文，不把“只有此近似”升级为独立审校结论。'),('T109','ブロッホベクトル','Bloch vector','布洛赫矢量','6.1 p5式(1.7) / B567','本处y分量v=i(ρng−ρgn)；依原符号，不改变归一化。'),('T110','縦緩和','longitudinal relaxation','纵向弛豫','6.1 p5广濑笔记 / B567','笔记纵向弛豫常数γ=2Γng，与经典阻尼γ分开读取。'),('T111','横緩和','transverse relaxation','横向弛豫','6.1 p5广濑笔记 / B567','本批书目导读中出现；尚未在本段另给定义式。'),('T112','Liouville 空間','Liouville space','刘维尔空间','6.1 p5广濑笔记 / B567','本批为教材导读中的提及，不自行补定义或推导。')]
for id,jp,en,zh,loc,meaning in terms:
 assert not any(x['术语编号']==id for x in rows)
 row={f:'' for f in fields};row.update({'术语编号':id,'日语候选':jp,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':meaning,'原文位置':loc,'依据':'B567原页对照；中文暂用，非新增用户确认','状态':'原词语境已核；中文暂用','文本定位状态':'原页已对照','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'FID及Liouville为底本所列；其余英语为译者辅助对应'});rows.append(row)
assert len(rows)==112 and len({x['术语编号'] for x in rows})==112
save_tsv(p,fields,rows)
p=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='6.1':
  assert row['原文SHA256']==a['source_sha256']
  row.update({'状态':'翻译中：B565—B567完成p1—5及p6笔记首段，均已对照排版；p6经典自由衰减段起待译','映射核验':'原目录、1.1及1.2至量子自由响应和完整广濑笔记已核；非1.2整节完成','公式图表范围':'已核式(1.1a/b)—(1.9)、脚注及跨页笔记；(1.10)起待译','导读状态':'分批导读，更新至B567','导读草案':'经典阻尼及量子线性响应后，处理密度矩阵方程、旋波近似下自由响应和广濑笔记；纵向γ与经典γ分开，实部、下标和乘积次序疑点保留。'})
save_tsv(p,fields,rows)
p=r/'中文版本/第六章 偶极间相互作用/阅读导航.md';t=p.read_text(encoding='utf-8').replace('B565完成p1—3；B566完成p4中1.2的前两个论述单元。p4后段及p5—55待译。','B565—B567已完成p1—5及p6开头的完整广濑笔记；p6经典自由衰减段起待译。')
t=t.replace('## 后续目录级预览（尚待正文核验）','- p4后段—p6笔记末：式(1.5)—(1.9)、密度矩阵运动方程、自由感应弛豫及完整跨页笔记。注意作者近似判断的保留语气、纵向γ的局部含义及Q234—Q236。\n\n## 后续目录级预览（尚待正文核验）')
t=t.replace('下一批从p4的结果差异小标题开始。','下一批从p6的经典自由衰减段开始。')
t=re.sub(r'下一批B567：[\s\S]*$','下一批B568：p6“另一方面，在存在弛豫时的经典论中……”起，先处理式(1.10)—(1.12)的自由衰减和经典/量子对应。之后共振频率与近共振段另按完整单元推进；p6末段跨到p7，不能截成半段。\n',t);p.write_text(t,encoding='utf-8')
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8').replace('目前p1—3及p4前两个论述单元已译校。','目前p1—5及p6开头的广濑笔记已译校。')
t=t.replace('（翻译中，p1—3及p4部分完成）：原目录、引言、1.1及脚注已译校；1.2完成量子线性响应与经典对应式(1.3)—(1.4)。注意时间因子与阻尼符号，Q229—Q233保留。','（翻译中，p1—5及p6笔记首段完成）：原目录、1.1及1.2至式(1.9)和完整广濑笔记已译校；从线性响应进入自由演化与弛豫。注意时间因子及两处γ的含义，Q229—Q236保留。');p.write_text(t,encoding='utf-8')
p=o/'结构与分批计划.md';t=p.read_text(encoding='utf-8').replace('| 1.2线性极化率 | 4—9 | B566完成p4前两部分；结果差异小标题起待译 |','| 1.2线性极化率 | 4—9 | B566—B567完成至p6完整广濑笔记；经典自由衰减段起待译 |');t+='\n\nB567完成后续接：B568从p6经典自由衰减段与式(1.10)—(1.12)起。式(1.5)—(1.9)及p5—p6跨页广濑笔记已完成。\n';p.write_text(t,encoding='utf-8')
p=r/'翻译管理/当前进度与续接.md';t=p.read_text(encoding='utf-8').replace('## 当前有效状态：6.1 B566完成','## 历史状态：6.1 B566完成',1)
new='## 当前有效状态：6.1 B567完成，推进至p6笔记末（2026-10-21）\n\nB567完成p4结果差异小标题至p6广濑笔记分隔线，16个覆盖单元、5编号式(1.5)—(1.9)、1完整跨页笔记及4文献指引。新增25个数学片段、累计125个片段语法通过；本批完整截图分2段已目视，无横向溢出。Q234分母实部、Q235末下标、Q236重复乘积均保留原文并就地说明，未采用修正。术语T107—T112标为暂用；纵向γ=2Γng与经典阻尼γ分开，不先认定同一参数。管理、序言与导航已同步。\n\n累计p1—5完整及p6首段笔记完成，1.2仍未完成。下一批B568从p6“另一方面，在存在弛豫时的经典论中……”起，先处理式(1.10)—(1.12)的经典自由衰减与参数对应。共振频率段随后按完整单元另批；p6末近共振段跨至p7，不能截半段。\n\n'
t=t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+new,1);p.write_text(t,encoding='utf-8')
(o/'B567最终检查.json').write_text(json.dumps({'批次':'B567','源摘要匹配':True,'批次摘要匹配':True,'覆盖单元':16,'编号式':5,'完整笔记':1,'新增数学片段':25,'累计数学片段':125,'全幅截图目视':True,'p6全页完成':False,'1.2完成':False,'采用原文修正':False,'下一批':'B568'},ensure_ascii=False,indent=2),encoding='utf-8')
assert chunk in target.read_text(encoding='utf-8')
print('B567完成，累计至p6笔记末；下一批B568，1.2未完。')

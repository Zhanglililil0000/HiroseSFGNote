from pathlib import Path
import json,hashlib,csv,io,re
from urllib.parse import quote,unquote
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;target=r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md'
a=json.loads((o/'B565验收.json').read_text(encoding='utf-8'));rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'))
assert rr['math']==72 and len(rr['results'])==1 and not rr['results'][0]['overs'] and rr['results'][0]['scrollWidth']==1100
assert hashlib.sha256(target.read_text(encoding='utf-8').encode('utf-8')).hexdigest()==a['translation_sha256']
assert hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest()==a['source_sha256']
assert len(json.loads((o/'B565-覆盖.json').read_text(encoding='utf-8')))==55
assert all((o/f'B565-目视{n}.png').exists() for n in range(1,5))
a.update({'已排版':True,'数学片段':72,'截图全幅目视':True,'横向溢出':False,'验收说明':'原p1—3逐页对照；排版截图分4段全部目视，编号式及脚注正常显示。未独立验证原式正确性。'})
(o/'B565验收.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=o/'B565.md';p.write_text(p.read_text(encoding='utf-8')+'\n排版验收：72个数学片段通过语法检查，完整截图分4段均已目视。目录33条、编号式4及脚注1显示正常，无横向溢出。本批完成；6.1全节尚未完成。\n',encoding='utf-8')
questions=[('Q229','PDF p2位移实式、p3式(1.2b)与脚注','位移实式整体为负，p=qx的实式(1.2b)却无整体负号；脚注实部又为负并称与1.2b一致。候选为给(1.2b)加整体负号，仅就地列候选，正文照原正号保留。'),('Q230','PDF p3式(1.2b)后N分子段','原称p(t)表达式乘N即体系“分极率”。p、总极化与极化率之间还涉及E以及N的计数/密度约定。保留原称“极化率”，未自行除E或补体积因子；后续式需回查。'),('Q231','PDF p2指数位移式及p3式(1.2a)','底本指数式下标为Times-Italic字母o，而定义、实式等为数字0，视觉及文本字符交叉核对。分别保留ωo与ω0，不自行引入第二固有频率；排字对应待核。')]
p=r/'翻译管理/疑难与勘误.md';t=p.read_text(encoding='utf-8')
for q,loc,desc in questions:
 assert not re.search(r'^## '+q+r'\b',t,re.M)
 t+=f'\n\n## {q}｜6.1 {loc}\n\n{desc}\n\n状态：原文保留、待核验；候选未采用。正文有就地说明，来源B565。\n'
p.write_text(t,encoding='utf-8')
p=r/'中文版本/附件/原文勘误表.md';t=p.read_text(encoding='utf-8');t+='\n\n## 第六章首批待核索引（B565）\n\n| 小节与位置 | 问题 | 处理 |\n|---|---|---|\n| 6.1 p2—3位移式、式(1.2b)及脚注 | Q229整体符号 | 保留原式，候选负号未采用 |\n| 6.1 p2—3指数式与定义式 | Q231下标o/0 | 保留两种字形，不视为已确认同一符号 |\n| 6.1 p3式(1.2b)后的N分子段 | Q230极化率称呼 | 保留原称，不补E或密度因子 |\n\n以上为待核索引，不是新增已采用原文修正，不分配E编号。详见[6.1正文](../第六章%20偶极间相互作用/6.1%20偶极间相互作用.md)及管理问题表。\n';p.write_text(t,encoding='utf-8')
nav=r/'中文版本/第六章 偶极间相互作用/阅读导航.md'
nav.write_text('# 第六章阅读导航\n\n本章目前仅6.1一节，共55页。B565完成p1—3，后续p4—55待译。以下把已核正文与目录级预览分开说明，不把原目录的页数定位视为正文完成。\n\n[进入6.1正文](6.1%20偶极间相互作用.md)\n\n## 已核正文\n\n- p1：合作署名及33条原目录，保留内部编号和原页码。\n- p2引言：从光谱与极化的关系出发，说明经典、量子推导及近似差异。\n- p2—3的1.1：受迫阻尼振子、诱导偶极矩、复频率分量、相位与取实部脚注。四个编号式已核，Q229—Q231保留。β、γ在此为阻尼参数，不能当作前章超极化率。\n\n## 后续目录级预览（尚待正文核验）\n\n1. 1.2—1.4（p4—13）：线性极化率，以及线性/非线性吸收和发光；下一批入口为1.2。\n2. 第2部分（p14起）：从单个及两个带电振子的运动方程推进到相互作用、简正模、多偶极子及无序体系；继而按原目录讨论Scheffler、Person/Ryberg、覆盖度、同位素及镜像。\n3. 第3部分（p35起）：和频光谱与IRAS的差异及不同物种/激发条件；目录标“提纲”的项目仍保持提纲状态，不补成作者未写的完整推导。\n4. 第4部分（p40起）：作者要点；具体结论待译校。\n5. 附录A—F（p42—55）：偶极场、镜像电荷/偶极子、偶极子对响应、三层体系及数学公式、术语说明。标题译名与物理条件待各附录正文核验。\n\n## 续接\n\n下一批B566：p4的1.2，先处理量子论公式(1.3)和经典对应式(1.4)。式(1.5)后的差异讨论跨页，按完整论述另划批次；先核时间因子与分子/宏观量，不继承旧章单位制或法线约定。\n',encoding='utf-8')
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8').replace('**本章导读（待正文核验）：** 讨论偶极之间的相互作用。','**本章导读（分批更新）：** 6.1共55页，目前p1—3已译校。先用经典阻尼振子建立电场、偶极矩和频率约定；后续依原目录进入偶极相互作用、和频光谱及镜像附录，正文尚待核验。各部分概括见[第六章阅读导航](中文版本/第六章%20偶极间相互作用/阅读导航.md)。').replace('- 6.1 偶极间相互作用（待翻译）：阅读偶极相互作用问题。','- [6.1 偶极间相互作用](中文版本/第六章%20偶极间相互作用/6.1%20偶极间相互作用.md)（翻译中，p1—3/55已完成）：原目录、引言和1.1经典模型已译校，包括正负频率及取实部脚注；注意β/γ的阻尼用法，Q229—Q231保留。')
p.write_text(t,encoding='utf-8')
def write_tsv(p,fields,rows):
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
p=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='6.1':
  assert row['原文SHA256']==a['source_sha256'] and row['PDF页数']=='55'
  row.update({'现有译文路径':target.relative_to(r).as_posix(),'状态':'翻译中：B565完成p1—3/55原页对照及排版，p4起待译','映射核验':'原题、合作署名、33条目录、引言及1.1已原页核对','公式图表范围':'本批编号式(1.1a/b)、(1.2a/b)，无编号式及p3脚注已覆盖；其余待逐批登记','导读状态':'分批导读，p1—3已核','导读草案':'先从经典阻尼振子读取电场、诱导偶极矩和exp(±iωt)约定；β/γ为阻尼参数。后续极化率、相互作用和镜像部分按原目录预览，待正文核验。'})
write_tsv(p,fields,rows)
p=r/'翻译管理/术语表.tsv';rd=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;terms=list(rd)
for row in terms:
 if row['术语编号'] in ['T081','T082']:row['定义与适用语境']+=' 6.1 p2—3的同名β/γ为阻尼参数，不适用本超极化率条目，见B565局部约定。'
newterms=[('T102','減衰振動子モデル','damped oscillator model','阻尼振子模型','6.1 p2 / B565','由m、κ及β描述的经典模型；β/m=2γ。','原词与模型定义已页面对照；中文暂用'),('T103','換算質量','reduced mass','约化质量','6.1 p3式(1.2b)后 / B565','作者将粒子模型中的m解释为分子振动的约化质量；不改记μ。','原词与语境已页面对照；中文暂用'),('T104','own image（目录英文）','own image','自身镜像','6.1 p1目录2.6及3.5 / B565','仅目录暂译，具体镜像边界条件待p33及后文核验。','目录暂用；正文未核'),('T105','image charge（目录英文）','image charge','镜像电荷','6.1 p1附录B/D目录 / B565','仅目录暂译，具体符号与介质条件待附录。','目录暂用；正文未核'),('T106','image dipole（目录英文）','image dipole','镜像偶极子','6.1 p1附录B/C目录 / B565','仅目录暂译；不预设方向或反射系数。','目录暂用；正文未核')]
for id,jp,en,zh,loc,definition,status in newterms:
 assert not any(x['术语编号']==id for x in terms)
 row={f:'' for f in fields};row.update({'术语编号':id,'日语候选':jp,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':definition,'原文位置':loc,'依据':'B565原页对照；非新增用户确认','状态':status,'文本定位状态':'所列原页已对照','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'T104—T106为目录英文；T102—T103为译者辅助对应'});terms.append(row)
write_tsv(p,fields,terms)
p=r/'翻译管理/符号与约定.md';t=p.read_text(encoding='utf-8');t+='\n\n## 6.1 p2—3经典模型（B565）\n\nκ回复力系数；β阻力系数；γ=β/(2m)，并非本段分子超极化率。F为力，f=F/m。p=qx为单分子诱导偶极矩，原文称分极；N倍后原称极化率依Q230保留。指数式ωo与其他式ω0依Q231分别保留，实式整体符号依Q229保留。Ecosωt拆为两个半幅度复频率分量；两种exp时间符号均出现，后续不得未经确认固定其一。取实部为半个复数与共轭之和，归一化依原式。单位制、N的计数/密度含义及宏观量定义本批未补定。\n';p.write_text(t,encoding='utf-8')
p=r/'翻译管理/当前进度与续接.md';t=p.read_text(encoding='utf-8').replace('## 当前有效状态：第五章中文图式版完成','## 历史状态：第五章中文图式版完成',1)
new='## 当前有效状态：6.1首批B565完成（2026-10-21）\n\n6.1《偶极间相互作用》底本55页，原作广濑千秋、狩野觉合作。B565完成p1—3：33条目录、引言、1.1经典模型及p3脚注，共55个覆盖单元、4个编号式、1个原脚注。72个数学片段语法与显示通过，完整排版截图分4段已目视，无横向溢出。Q229整体符号、Q230极化率称呼、Q231下标o/0均保留原文并就地说明，未采用原文修正。β/γ阻尼用法、目录暂译、章节清单、序言和导航已同步。\n\n下一批B566：从p4的1.2线性极化率开始，先核量子论式(1.3)及经典对应式(1.4)和exp(-iωt)约定；式(1.5)后的差异讨论跨页，按完整论述另划单元。6.1 p4—55尚未翻译；第六章尚未完成。第五章中文图式版维持既有完成状态。\n\n'
t=t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+new,1);p.write_text(t,encoding='utf-8')
checks=[]
for p in [target,nav]:
 for targetpath in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if '://' in targetpath:continue
  resolved=p.parent/unquote(targetpath);assert resolved.exists(),resolved;checks.append(str(resolved))
assert len(terms)==106 and len({x['术语编号'] for x in terms})==106
assert (o/'B565-本批译文.md').read_text(encoding='utf-8')==target.read_text(encoding='utf-8')
(o/'B565最终检查.json').write_text(json.dumps({'批次':'B565','已起草':True,'已原页对照':True,'已排版':True,'覆盖单元':55,'目录条目':33,'编号式':4,'原脚注':1,'数学片段':72,'截图全幅目视':True,'源与译文摘要匹配':True,'正文与批次一致':True,'链接检查':checks,'本节完成':False,'下一批':'B566'},ensure_ascii=False,indent=2),encoding='utf-8')
print('B565完成：原页、排版、摘要及管理记录一致；6.1 p4起待译。')

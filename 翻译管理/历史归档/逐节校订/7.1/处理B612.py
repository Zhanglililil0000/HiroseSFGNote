from pathlib import Path
import json,re,hashlib,csv,io,sys
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;d=r/'中文版本/第七章 Heinz论文解读';p=d/'7.1 解读Tony F. Heinz的综述.md';chunk=(o/'B612-本批译文.md').read_text(encoding='utf-8');src=r/'日语原版/Chapter7/chap7-1.pdf'
if '--finish' not in sys.argv:
 t=p.read_text(encoding='utf-8');assert '\\tag{3}' not in t
 t=re.sub(r'\n<!-- B611结束：[\s\S]*?-->\s*$','\n',t)
 t=re.sub(r'> \*\*译校状态[^\n]*','> **译校状态（B609—B612，2026-10-22）：** 已完成PDF p1—2全页及p3至式(4)后的δ薄片表示，包括四条边界条件与跨页积分讨论。p3的路径积分论述起尚未翻译，2.2仍未完成。',t,count=1)
 p.write_text(t+'\n'+chunk,encoding='utf-8')
 units=[(2,'引句','Born & Wolf第1.1节引文'),(2,'条件1及其式','B法向连续'),(2,'条件2及其式','表面电荷与D法向跳跃、原ρ'),(2,'条件3及其式','E面内连续'),(2,'条件4及其式','H面内跳跃、原j及c因子'),(2,'代入段','两源定义及原四量连续判断'),(2,'跨页引句','与p3积分式完整接续'),(3,'式(3)','四种积分串联、无末项零、上下限0±'),(3,'式(4)引句及公式','D积分、−4πP积分、定义Ps,z'),(3,'薄片解释句','原用Ps,z指薄片'),(3,'δ函数表示','原P=P(x,y)δ(z)，不擅加s下标')]
 cov=[{'原文定位':f'PDF p{pn} / {loc}','对象':obj,'译文定位':'B612-本批译文.md对应段或式号','已翻译':True,'已原页对照':True} for pn,loc,obj in units]
 (o/'B612-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
 a={'批次':'B612','日期':'2026-10-22','范围':'p2边界条件至p3式(4)后δ函数表示','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'translation_sha256':hashlib.sha256(chunk.encode()).hexdigest(),'覆盖单元':11,'编号式':['3','4'],'独立无编号式':5,'原图':0,'新增疑点':['Q276','Q277'],'采用原文修正':False,'已原页对照':True,'已排版':False,'p2全页完成':True,'p3全页完成':False}
 (o/'B612验收.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8');print('B612登记，等待排版。');sys.exit()
a=json.loads((o/'B612验收.json').read_text(encoding='utf-8'));rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));m=next(x for x in rr['results'] if x['batch']=='B612');n=len(re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',chunk))
assert not m['overs'] and m['scrollWidth']==1100 and rr['math']==52+n
assert chunk in p.read_text(encoding='utf-8') and hashlib.sha256(chunk.encode()).hexdigest()==a['translation_sha256']
assert hashlib.sha256(src.read_bytes()).hexdigest()==a['source_sha256']
a.update({'已排版':True,'本批数学片段':n,'累计数学片段':rr['math'],'全幅截图目视':True,'横向溢出':False})
for name in ['B612验收.json','B612最终检查.json']:(o/name).write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B612.md').write_text(f'# B612｜四条边界条件及跨页积分\n\np2剩余全部及p3至式(4)后δ表示，11覆盖单元、2编号式、5独立无编号式。四条件、跨页引句、积分上下限、等号串联、Ps,z与P(x,y)δ(z)均照原页对照。\n\n本批{n}数学片段、累计{rr["math"]}严格语法通过；全幅参考截图已目视，无横向溢出。Q276面源密度/磁场方向与Q277积分链/薄片记号均保留原式，未采用修正。\n\n下一批B613处理p3路径积分跳跃条件至2.3前；原跳号5/7/9/10/11保留。\n',encoding='utf-8')
note='## 7.1 B612补充约定\n\n- z指向介质2，t表示面内分量；条件中的(1)/(2)是界面两侧标签。\n- 本段边界式ρ、j仍沿原符号；面/体密度以及H切向跳跃的法向叉乘含义见Q276，未补方向因子。\n- 式(3)四积分的原等号串联与无末项零完整保留，不能当作已经独立证明的连续条件。\n- 式(4)给出Ps,z=∫Pz dz；随后的原P=P(x,y)δ(z)两处P记号保留，不预改成后文Ps。相关表述边界见Q277。\n'
for f in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:f.write_text(f.read_text(encoding='utf-8')+'\n\n'+note,encoding='utf-8')
(o/'B612术语核对.md').write_text('# B612术语核对\n\n沿极化薄片、磁感应强度、电位移、面内/切向和法向用词。ρ、j的面源属性有待核说明，不据译名补原式。δ函数表示沿既有数学排版；无新增术语条目或用户确认译名。\n',encoding='utf-8')
f=r/'翻译管理/疑难与勘误.md';s=f.read_text(encoding='utf-8')
for q in [276,277]:
 assert f'## Q{q}｜' not in s
 noteq=next(x for x in chunk.splitlines() if x.startswith('> **') and f'Q{q}' in x)[2:]
 s+=f'\n\n## Q{q}｜7.1 PDF '+('p2四条边界条件' if q==276 else 'p2末至p3式(3)—(4)及δ表示')+'\n\n'+noteq+'\n\n状态：原文保留、待核；未采用修正。来源B612，正文有就地说明。\n'
f.write_text(s,encoding='utf-8')
f=r/'中文版本/附件/原文勘误表.md';f.write_text(f.read_text(encoding='utf-8')+'\n\n### 7.1 B612待核索引\n\n| 原位置 | 问题号 | 处理 |\n|---|---|---|\n| p2四条边界条件 | Q276 | 保留原ρ、j及H跳跃式；面密度与法向叉乘约定待核 |\n| p2末—p3式(3)—(4)及δ表示 | Q277 | 保留四积分等号链、无末项零及原P记号；论证与分布极限待核 |\n\n均未采用修正，不分配E编号。详见[7.1正文](../第七章%20Heinz论文解读/7.1%20解读Tony%20F.%20Heinz的综述.md)。\n',encoding='utf-8')
f=o/'结构与分批计划.md';s=f.read_text(encoding='utf-8').replace('B609—B611已核p1全页及p2至式(2d)；','B609—B612已核p1—2全页及p3至式(4)后δ表示；').replace('B610完成比较/一般方程/图；B611完成p2源关系及(2a)—(2d)；边界条件待译','B610—B612完成模型、源关系、四条件及式(3)—(4)；p3路径积分起待译')
s=re.sub(r'下一批B612[\s\S]*$','下一批B613从p3路径积分引句起，处理(5)、(7)、(9)—(11)、解释、(12a)—(12d)及ε′zz各向异性说明，止于2.3前。原跳号保留；2.2尚未完成。\n',s);f.write_text(s,encoding='utf-8')
f=d/'阅读导航.md';s=f.read_text(encoding='utf-8').replace('B609—B611完成p1全页及p2至式(2d)，2.2仍未完成。','B609—B612完成p1—2全页及p3至式(4)后δ表示，2.2仍未完成。').replace('边界条件及后续辐射、表面和体相响应尚待译校。','四条边界条件与跨页积分已核，Q276—Q277保留；p3路径积分跳跃式及后续辐射、表面和体相响应尚待译校。')
s=re.sub(r'下一批B612[^\n]*','下一批B613从p3路径积分论述起，处理跳跃条件及式(12)汇总，至2.3标题前。',s);f.write_text(s,encoding='utf-8')
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8').replace('已完成p1模型、一般场方程及p2源极化至式(2d)；边界条件、辐射与表面/体相响应待逐批译校','已完成p1—2及p3的边界积分至式(4)和δ表示；薄片跳跃条件、辐射与表面/体相响应待逐批译校').replace('（翻译中，B609—B611）：p1全页及p2至式(2d)已译校，包含模型、几何图、源电荷/电流及极化场方程。边界条件起待译，Q274—Q275保留。','（翻译中，B609—B612）：p1—2全页及p3至式(4)后的δ表示已译校，包含四条边界条件及跨页积分。路径积分跳跃式起待译，Q274—Q277保留。');f.write_text(s,encoding='utf-8')
f=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(f.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='7.1':row.update({'状态':'翻译中：B609—B612完成p1—2及p3至(4)后δ表示；Q274—Q277待核','映射核验':'四条边界式、跨页积分及δ薄片记号已核；路径积分起待译','公式图表范围':f'式(1)、(2a)—(2d)、(3)—(4)、无编号边界式及原图；累计{rr["math"]}数学片段排版通过','导读状态':'已据B609—B612正文更新','导读草案':'由面源模型、显式源方程进入四条件及跨页积分；面密度、H跳跃方向和积分链待核，路径积分薄片条件待译。'})
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);f.write_text(b.getvalue(),encoding='utf-8')
f=r/'翻译管理/当前进度与续接.md';s=f.read_text(encoding='utf-8').replace('## 当前有效状态：7.1 B611完成','## 历史状态：7.1 B611完成',1)
state=f'## 当前有效状态：7.1 B612完成，推进至p3式(4)后（2026-10-22）\n\n本批完成p2四条边界条件至p3式(3)—(4)及δ薄片表示，11覆盖单元、2编号式、5独立无编号式；新增{n}数学片段、累计{rr["math"]}严格语法通过，全幅截图已目视，无横向溢出。Q276保留面源密度/H方向，Q277保留积分链与薄片记号，均未采用修正。无新增术语，符号、勘误待核索引、导航、序言和清单同步。\n\n累计p1—2全页及p3至式(4)后完成，2.2未完成。下一批B613从“原论文巧妙使用路径积分……”起，处理(5)、(7)、(9)—(11)、解释及汇总(12a)—(12d)，再核各向异性ε′zz说明，止于2.3前。保留原跳号，不补(6)、(8)。\n\n'
s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+state,1);f.write_text(s,encoding='utf-8');print('B612验收及管理记录更新完成。')

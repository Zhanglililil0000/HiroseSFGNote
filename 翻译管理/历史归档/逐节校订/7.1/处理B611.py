from pathlib import Path
import json,re,hashlib,csv,io,sys
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;d=r/'中文版本/第七章 Heinz论文解读';p=d/'7.1 解读Tony F. Heinz的综述.md';chunk=(o/'B611-本批译文.md').read_text(encoding='utf-8');src=r/'日语原版/Chapter7/chap7-1.pdf'
if '--finish' not in sys.argv:
 t=p.read_text(encoding='utf-8');assert '\\tag{2a}' not in t
 t=re.sub(r'\n<!-- B610结束：[\s\S]*?-->\s*$','\n',t)
 t=re.sub(r'> \*\*译校状态[^\n]*','> **译校状态（B609—B611，2026-10-22）：** 已完成PDF p1全页及p2至式(2d)，包括首图、源电荷/电流与极化关系及原括注。p2的Born & Wolf边界条件引句起尚未翻译，2.2仍未完成。',t,count=1)
 t+='\n'+chunk;p.write_text(t,encoding='utf-8')
 units=[('图后首句','原文无净电荷/电流、仅有极化的限定'),('首段后半','整体中性与电荷偏移'),('无编号关系1','∂P/∂t=j'),('无编号关系2','ρ=−∇·P'),('原括注前半','电荷连续性及P的时间导数散度'),('原括注后半','P=∫rρdv与“或由此得到”'),('方程引句','将P作为源代入麦克斯韦方程'),('式(2a)','D散度与−4π∇·P'),('式(2b)','c乘E旋度及B时间导数'),('式(2c)','B散度为零'),('式(2d)','H旋度、D时间导数及4π∂P/∂t')]
 cov=[{'原文定位':'PDF p2 / '+loc,'对象':obj,'译文定位':'B611-本批译文.md对应段落或原式号','已翻译':True,'已原页对照':True} for loc,obj in units]
 (o/'B611-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
 a={'批次':'B611','日期':'2026-10-22','范围':'PDF p2图后首段、原括注及式(2a)—(2d)','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'translation_sha256':hashlib.sha256(chunk.encode()).hexdigest(),'覆盖单元':len(cov),'编号式':['2a','2b','2c','2d'],'独立无编号公式组':3,'原图':0,'原括注':1,'新增疑点':['Q275'],'采用原文修正':False,'已原页对照':True,'已排版':False,'p2全页完成':False}
 (o/'B611验收.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8');print('B611登记完成，等待排版。');sys.exit()
a=json.loads((o/'B611验收.json').read_text(encoding='utf-8'));rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));m=next(x for x in rr['results'] if x['batch']=='B611');n=len(re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',chunk))
assert not m['overs'] and m['scrollWidth']==1100 and all(i['loaded'] for i in m['images']) and rr['math']==31+n
assert chunk in p.read_text(encoding='utf-8') and hashlib.sha256(chunk.encode()).hexdigest()==a['translation_sha256']
assert hashlib.sha256(src.read_bytes()).hexdigest()==a['source_sha256']
a.update({'已排版':True,'本批数学片段':n,'累计数学片段':rr['math'],'全幅参考截图目视':True,'横向溢出':False})
for name in ['B611验收.json','B611最终检查.json']:(o/name).write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B611.md').write_text(f'# B611｜源极化与麦克斯韦方程\n\np2首段、原括注及(2a)—(2d)，11覆盖单元、4编号式、3无编号公式组；无原图。完整原括注保留，Q275记录总偶极矩与局部极化的量纲/归一化及静态条件疑点，未采用修正。\n\n本批{n}数学片段、累计{rr["math"]}严格语法通过，全幅截图已目视，无横向溢出。未独立重导原文物理。\n\n下一批B612从Born & Wolf边界条件引句起，跨p2—p3的积分引句连同式(3)—(4)和δ薄片表示处理，止于路径积分论述前。\n',encoding='utf-8')
note='## 7.1 B611补充约定\n\n- 本段ρ、j由P给出：ρ=−∇·P，j=∂P/∂t；整体中性不代表局部两源处处为零。\n- P为本段显式源量，Ps为先前面源极化，暂不补薄片积分或δ系数；不把同一个P重复计入D=εE。\n- 原括注P=∫rρdv与局部P之间的归一化、边界及静态条件见Q275；保留原式，不补因子。\n- (2a)—(2d)沿高斯形式，旋度、散度和时间导数均保持原号；坐标沿B610图。\n'
for f in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:f.write_text(f.read_text(encoding='utf-8')+'\n\n'+note,encoding='utf-8')
(o/'B611术语核对.md').write_text('# B611术语核对\n\n沿既有“极化”“电荷密度”“电流密度”和“面源极化”。不把P=∫rρdv的原符号擅改成p，也不把P与Ps合并。无新增术语条目；Q275为原文待核，非术语已确认结论。\n',encoding='utf-8')
f=r/'翻译管理/疑难与勘误.md';s=f.read_text(encoding='utf-8');assert '## Q275｜' not in s
qnote=next(x for x in chunk.splitlines() if x.startswith('> **原文疑点'))[2:]
f.write_text(s+'\n\n## Q275｜7.1 PDF p2首段原括注\n\n'+qnote+'\n\n状态：原文保留、待核；未采用修正。来源B611，正文已就地说明。\n',encoding='utf-8')
f=r/'中文版本/附件/原文勘误表.md';f.write_text(f.read_text(encoding='utf-8')+'\n\n### 7.1 B611待核索引\n\n| 原位置 | 问题号 | 处理 |\n|---|---|---|\n| p2图后首段原括注 | Q275 | 保留P=∫rρdv，记录总偶极矩与局部极化的对应、归一化及静态条件待核；未采用修正 |\n\n详见[7.1正文](../第七章%20Heinz论文解读/7.1%20解读Tony%20F.%20Heinz的综述.md)。本项未分配E编号。\n',encoding='utf-8')
f=o/'结构与分批计划.md';s=f.read_text(encoding='utf-8').replace('B609—B610已核p1全页与p2首图；','B609—B611已核p1全页及p2至式(2d)；').replace('B610完成模型比较、一般方程及p2图；p2正文起待译','B610完成比较/一般方程/图；B611完成p2源关系及(2a)—(2d)；边界条件待译')
s=re.sub(r'下一批B611[\s\S]*$','下一批B612从p2的Born & Wolf边界条件引句起，含四条边界式、页末引句及p3式(3)—(4)、δ函数薄片表示，止于路径积分论述前。p2—p3的跨页句不截断。\n',s);f.write_text(s,encoding='utf-8')
f=d/'阅读导航.md';s=f.read_text(encoding='utf-8').replace('B609—B610完成p1全页及p2首图，2.2仍未完成。','B609—B611完成p1全页及p2至式(2d)，2.2仍未完成。').replace('p2源极化及后续边界条件、辐射、表面和体相响应尚待译校。','p2源关系及式(2a)—(2d)已核；Q275保留原括注的局部极化/总偶极矩疑点。边界条件及后续辐射、表面和体相响应尚待译校。')
s=re.sub(r'下一批B611[^\n]*','下一批B612从p2四条边界条件起，连同跨页引句及p3式(3)—(4)、δ薄片表示完整处理。',s);f.write_text(s,encoding='utf-8')
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8').replace('已完成p1模型、一般场方程及p2几何图；源极化、边界条件、辐射与表面/体相响应待逐批译校','已完成p1模型、一般场方程及p2源极化至式(2d)；边界条件、辐射与表面/体相响应待逐批译校').replace('（翻译中，B609—B610）：p1全页及p2首图已译校，包含唯象模型、极化薄片与有限厚膜比较及一般场方程。p2源极化讨论起待译，Q274保留。','（翻译中，B609—B611）：p1全页及p2至式(2d)已译校，包含模型、几何图、源电荷/电流及极化场方程。边界条件起待译，Q274—Q275保留。');f.write_text(s,encoding='utf-8')
f=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(f.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='7.1':row.update({'状态':'翻译中：B609—B611完成p1全页及p2至(2d)；Q274—Q275待核','映射核验':'已核模型、几何图、源电荷/电流关系及(2a)—(2d)；边界条件起待译','公式图表范围':f'式(1)、(2a)—(2d)、一般场关系及p2原图；累计{rr["math"]}数学片段排版通过','导读状态':'已据B609—B611正文更新','导读草案':'由面源模型进入ρ=−∇·P、j=∂P/∂t及显式源场方程；总偶极矩括注有待核，边界条件待译。'})
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);f.write_text(b.getvalue(),encoding='utf-8')
f=r/'翻译管理/当前进度与续接.md';s=f.read_text(encoding='utf-8').replace('## 当前有效状态：7.1 B610完成','## 历史状态：7.1 B610完成',1)
state=f'## 当前有效状态：7.1 B611完成，推进至p2式(2d)（2026-10-22）\n\n本批完成p2图后首段、原括注及(2a)—(2d)，11覆盖单元、4编号式、3无编号组；新增{n}数学片段、累计{rr["math"]}严格语法通过，完整参考截图已目视，无横向溢出。Q275保留P=∫rρdv及局部极化/静态条件疑点，未采用修正。无新增术语条目；符号、勘误待核附件、导航、序言与清单均同步。\n\n累计p1全页及p2至(2d)已译，p2尚未全页、2.2未完成。下一批B612从Born & Wolf第1.1节边界条件引句开始，四条条件及p2末跨页引句须与p3式(3)—(4)、随后δ薄片表示完整处理，止于“原论文巧妙使用路径积分……”前。\n\n'
s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+state,1);f.write_text(s,encoding='utf-8');print('B611验收与管理记录更新完成。')

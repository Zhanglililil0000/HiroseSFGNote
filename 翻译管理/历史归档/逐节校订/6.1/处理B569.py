from pathlib import Path
import json,hashlib,re,csv,io,sys
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;p=r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md';chunk=(o/'B569-本批译文.md').read_text(encoding='utf-8')
if '--finish' not in sys.argv:
 t=p.read_text(encoding='utf-8');assert '\\tag{1.13}' not in t
 t=re.sub(r'\n<!-- B568结束：[\s\S]*?-->\s*$','\n',t)
 t=re.sub(r'> \*\*译校状态[^\n]*', '> **译校状态（B565—B569，2026-10-21）：** 已完成PDF p1—6及p7首段，包含式(1.1a)—(1.15)、相应脚注及完整广濑笔记。p7“概括起来，经典论与量子论的差异……”起尚未翻译，1.2仍未完成。',t,count=1)
 t+='\n'+chunk+'\n<!-- B569结束：PDF p7首段近共振说明末“即ω=ω0”。下一批B570从“概括起来，经典论与量子论的差异……”起，处理总结、方括号内广濑备忘和阻尼常数讨论，至“作为出发点的极化率公式”小标题前；后者及式(1.16)另批。 -->\n';p.write_text(t,encoding='utf-8')
 units=[(6,'共振段首句','弛豫下最大振幅定义及量子分母的模'),(6,'式(1.13)','括号内ωng²+Γng²及外减2Γng²'),(6,'经典式引句','经典频率响应'),(6,'式(1.14)','ωo²−ω²−2iγω及方括号'),(6,'式(1.15)及其引句','函数模的最大值与ω0²−2γ²'),(6,'对应段前半','对1.15作1.11/1.12替换'),(6,'对应段后半','两理论均低频偏移，跃迁/固有频率限定'),(6,'近共振段及无编号式','ω≈ω0、ω+ω0→2ω0、[(ω−ω0)−iγ]倒数'),(7,'首段接续','或复共轭，不遗漏跨页短语'),(7,'首段末','虚部不含ω、纯虚分母、ω=ω0')]
 cov=[{'原文定位':f'PDF p{pn} / {loc}','对象':obj,'译文定位':'B569-本批译文.md对应段落/原式号','已翻译':True,'已原页对照':True} for pn,loc,obj in units]
 (o/'B569-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
 a={'批次':'B569','范围':'PDF p6共振频率段至p7首段末ω=ω0','source_sha256':hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest(),'translation_sha256':hashlib.sha256(chunk.encode('utf-8')).hexdigest(),'覆盖单元':10,'编号式':['1.13','1.14','1.15'],'独立无编号式':1,'原图':0,'原脚注':0,'已起草':True,'已原页对照':True,'已排版':False,'新增疑点':[],'承接疑点':['Q231'],'采用原文修正':False,'下一批':'B570，p7总结与阻尼常数讨论至出发点极化率小标题前'}
 (o/'B569验收.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8');print('B569登记，待排版。');sys.exit()
a=json.loads((o/'B569验收.json').read_text(encoding='utf-8'));rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));metric=next(x for x in rr['results'] if x['batch']=='B569');n=len(re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',chunk))
assert not metric['overs'] and metric['scrollWidth']==1100 and rr['math']==130+n
assert hashlib.sha256(chunk.encode('utf-8')).hexdigest()==a['translation_sha256']
assert hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest()==a['source_sha256']
assert chunk in p.read_text(encoding='utf-8') and '\\tag{1.16}' not in p.read_text(encoding='utf-8')
a.update({'已排版':True,'本批数学片段':n,'累计数学片段':rr['math'],'全幅截图目视':True,'p6全页完成':True,'p7全页完成':False})
(o/'B569验收.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B569.md').write_text(f'# B569｜共振频率与近共振近似\n\np6后段至p7首段末，10覆盖单元、3编号式和1独立无编号式；无原图、原脚注或书目。跨页“或复共轭”与纯虚分母、ω=ω0说明已合并译校。\n\n本批{n}个数学片段语法及显示通过，全幅截图已目视，无横向溢出。括号、负号、o/0与量子/经典参数对应已原页核对。无新增疑点或采用修正，Q231继续保留；不补近共振式前因子。\n\n下一批B570：p7总结和阻尼常数讨论，式(1.16)尚未翻译。\n',encoding='utf-8')
note='\n\n## B569补充：共振与近共振（p6后段—p7首段）\n\n本段“共振频率”明确按最大振幅定义，(1.13)与(1.15)按原式保留，未与自由演化频率合并。(1.14)继续ωo；近共振段另用ω0、ω≈ω0及ω+ω0→2ω0，响应写1/[(ω−ω0)−iγ]或其复共轭。未补归一化前因子或把它写成与完整响应严格相等，p7解释虚部不再依赖ω及峰值ω=ω0的限定完整保留。\n'
for f in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:f.write_text(f.read_text(encoding='utf-8')+note,encoding='utf-8')
(o/'B569术语核对.md').write_text('# B569术语核对\n\n沿既有“弛豫”“共振频率”用法；本段按作者括注限定为最大振幅对应频率。“近共振近似”为本段暂用中文，依原ω≈ω0条件解释，不与前段旋波近似自动等同。无新增已确认术语、原文疑点或采用勘误；Q229—Q236状态不变。\n',encoding='utf-8')
f=r/'中文版本/第六章 偶极间相互作用/阅读导航.md';t=f.read_text(encoding='utf-8');t=re.sub(r'本章目前仅6.1一节[^\n]*','本章目前仅6.1一节，共55页。B565—B569已完成p1—6及p7首段；p7总结段起待译。已核正文与目录预览的状态如下。',t,count=1)
t=t.replace('## 后续目录级预览（尚待正文核验）','- p6后段—p7首段：式(1.13)—(1.15)、量子/经典峰位偏移、近共振式及其复共轭；明确区分峰值频率与自由演化频率。\n\n## 后续目录级预览（尚待正文核验）').replace('下一批从p6的共振频率讨论开始。','下一批从p7的总结及阻尼常数讨论开始。')
t=re.sub(r'下一批B569：[\s\S]*$','下一批B570：p7“概括起来，经典论与量子论的差异……”起，连同作者方括号备忘及阻尼常数的完整论述，止于“作为出发点的极化率公式”小标题前。式(1.16)及随后跨页变形另批。\n',t);f.write_text(t,encoding='utf-8')
f=r/'Preface序言.md';t=f.read_text(encoding='utf-8').replace('目前p1—5及p6至式(1.12)的讨论已译校。','目前p1—6及p7首段已译校。').replace('（翻译中，p1—5及p6部分完成）：原目录、1.1及1.2至式(1.12)已译校，涵盖完整广濑笔记、经典自由衰减及量子/经典参数对应。','（翻译中，p1—6及p7首段完成）：原目录、1.1及1.2至式(1.15)和近共振跨页说明已译校，涵盖自由衰减、参数对应及峰位偏移。');f.write_text(t,encoding='utf-8')
f=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(f.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='6.1':row.update({'状态':'翻译中：B565—B569完成p1—6及p7首段，均已对照排版','映射核验':'已核至近共振跨页说明；p7总结段起待译','公式图表范围':'式(1.1a/b)—(1.15)、近共振无编号式及脚注/笔记已核；(1.16)起待译','导读状态':'分批导读，更新至B569','导读草案':'经典/量子响应、密度矩阵及自由衰减后，比较峰值频率与近共振形式；p7总结和后续相互作用待译。'})
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);f.write_bytes(b.getvalue().encode('utf-8'))
f=o/'结构与分批计划.md';f.write_text(f.read_text(encoding='utf-8')+'\n\nB569完成p6共振频率至p7首段末，已核式(1.13)—(1.15)和近共振跨页说明。B570自p7总结段起，至“出发点的极化率公式”小标题前；1.2未完成。\n',encoding='utf-8')
f=r/'翻译管理/当前进度与续接.md';t=f.read_text(encoding='utf-8').replace('## 当前有效状态：6.1 B568完成','## 历史状态：6.1 B568完成',1)
new=f'## 当前有效状态：6.1 B569完成，推进至p7首段（2026-10-21）\n\n本批完成p6共振频率至p7首段近共振说明：10覆盖单元、3编号式(1.13)—(1.15)、1独立无编号式；新增{n}个数学片段，累计{rr["math"]}个片段语法通过。全幅截图已目视，无横向溢出。无新增疑点或采用修正，o/0仍按Q231保留；近共振式不补前因子。符号、序言、导航和清单已同步。\n\n累计p1—6完整及p7首段完成，1.2未完。下一批B570从p7“概括起来，经典论与量子论的差异……”起，包含原文方括号备忘和阻尼常数讨论，至“作为出发点的极化率公式”小标题前。式(1.16)及后续跨页变形另批，不从半个公式开始。\n\n'
t=t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+new,1);f.write_text(t,encoding='utf-8')
(o/'B569最终检查.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8');print('B569验收与管理更新完成。')

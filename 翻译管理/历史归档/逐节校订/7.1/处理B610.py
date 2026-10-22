from pathlib import Path
import json,re,hashlib,csv,io,sys
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;d=r/'中文版本/第七章 Heinz论文解读';p=d/'7.1 解读Tony F. Heinz的综述.md';f=o/'B610-本批译文.md';chunk=f.read_text(encoding='utf-8');src=r/'日语原版/Chapter7/chap7-1.pdf'
if '--finish' not in sys.argv:
 t=p.read_text(encoding='utf-8');assert '### 2.2 极化薄片' not in t
 t=re.sub(r'\n<!-- B609结束：[\s\S]*?-->\s*$','\n',t)
 t=re.sub(r'> \*\*译校状态[^\n]*','> **译校状态（B609—B610，2026-10-22）：** 已完成PDF p1全页及p2首幅示意图，包含引言、2.1及2.2的模型比较和一般麦克斯韦方程。p2图后源电荷/电流讨论起尚未翻译；2.2未完成。',t,count=1)
 t+='\n'+chunk;p.write_text(t,encoding='utf-8')
 import pypdfium2 as pdf
 doc=pdf.PdfDocument(str(src));im=doc[1].render(scale=3).to_pil();asset=r/'中文版本/assets/7.1';asset.mkdir(parents=True,exist_ok=True);im.crop((477,261,1281,927)).save(asset/'p2-极化薄片几何.png');doc.close()
 units=[('p1的2.2标题','英文标题及内部编号'),('p1首段前半','B & P有限厚膜和体极化体积元'),('p1首段中部','相对波长的无穷薄极限及低覆盖度实验比较'),('p1首段末','Heintz原拼法、二维极化面元'),('p1第二段','两侧电磁场匹配及和频光表达'),('p2首图','全部坐标轴、介质标记、四条波矢及箭头方向'),('p1麦克斯韦方程引句','Born & Wolf第1章引文'),('p1无编号方程组1','D散度及4πρ'),('p1无编号方程组2','E旋度与B时间导数'),('p1无编号方程组3','B散度'),('p1无编号方程组4','H旋度、D时间导数与4πj'),('p1附带关系','D=εE、H=μ逆B'),('p1末两关系','j散度恒等式及电荷连续性方程')]
 cov=[{'原文定位':'PDF '+loc,'对象':obj,'译文定位':'B610-本批译文.md对应段或方程','已翻译':True,'已原页对照':True} for loc,obj in units]
 (o/'B610-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
 a={'批次':'B610','日期':'2026-10-22','范围':'p1的2.2开头至页末一般方程，含p2首图','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'translation_sha256':hashlib.sha256(chunk.encode()).hexdigest(),'覆盖单元':13,'新编号式':[],'独立无编号公式组':3,'原图':1,'新增疑点':['Q274'],'新增已采用修正':False,'已原页对照':True,'已排版':False,'p1全页完成':True,'p2全页完成':False}
 (o/'B610验收.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8');print('B610登记，等待排版。');sys.exit()
rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));m=next(x for x in rr['results'] if x['batch']=='B610');a=json.loads((o/'B610验收.json').read_text(encoding='utf-8'))
assert not m['overs'] and m['scrollWidth']==1100 and len(m['images'])==1 and all(i['loaded'] for i in m['images'])
assert chunk in p.read_text(encoding='utf-8') and hashlib.sha256(chunk.encode()).hexdigest()==a['translation_sha256']
assert hashlib.sha256(src.read_bytes()).hexdigest()==a['source_sha256']
n=len(re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',chunk));assert rr['math']==12+n
a.update({'已排版':True,'本批数学片段':n,'累计数学片段':rr['math'],'全幅截图目视':True,'原图裁切目视':True,'横向溢出':False})
for name in ['B610验收.json','B610最终检查.json']:(o/name).write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B610.md').write_text(f'# B610｜2.2模型比较、跨页图与一般场方程\n\n13覆盖单元、3无编号公式组、1原图；p1全页及p2首图已译校，p2正文未译。图紧接引句前移排版，不改变图形。{n}个新数学片段、累计{rr["math"]}个严格语法通过；原图裁切及完整参考截图已目视，无缺图/横向溢出。Q274保留薄膜极限判断与Heintz原拼法，未采用原文修正。\n\n下一批B611从p2净电荷/电流与极化讨论起，原括注和(2a)—(2d)完整处理。边界条件及跨至p3的积分组另批。\n',encoding='utf-8')
note='## 7.1 B610补充约定\n\n- 图中x沿界面、z沿法向指向介质2；不套用6.1的坐标或法线方向。ε1、ε′、ε2对应两侧介质与膜。\n- 一般麦克斯韦方程为带4π、c的高斯形式；μ保留，ρ为电荷密度，j为电流密度。源P与D的具体拆分待p2定义，暂不混入ε。\n- volume polarization暂用“体极化”，与体二阶非线性极化率χ和第2.5节体相响应概念分开；薄膜极限条件见Q274。\n- 原p2图移至p1引句之后，属版面重排，不改变原图；Heintz原拼法在正文可见，未静默改写。\n'
for name in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:
 name.write_text(name.read_text(encoding='utf-8')+'\n\n'+note,encoding='utf-8')
(o/'B610术语核对.md').write_text('# B610术语核对\n\n沿T129极化薄片及既有和频/覆盖度用词。volume polarization依原英文暂用“体极化”，指体积元模型中的极化，不替换为χ。D电位移、B磁感应、H磁场按后续边界公式保留；本批不增加用户已确认译名。T132登记体极化暂译。\n',encoding='utf-8')
f=r/'翻译管理/疑难与勘误.md';s=f.read_text(encoding='utf-8');assert '## Q274｜' not in s
noteq=next(x for x in chunk.splitlines() if x.startswith('> **原文疑点'))[2:]
s+='\n\n## Q274｜7.1 PDF p1的2.2首段\n\n'+noteq+'\n\n状态：原文保留、待核；未采用修正。来源B610，正文已就地说明。\n';f.write_text(s,encoding='utf-8')
f=r/'中文版本/附件/原文勘误表.md';f.write_text(f.read_text(encoding='utf-8')+'\n\n### 7.1 B610待核索引\n\n| 原位置 | 问题号 | 处理 |\n|---|---|---|\n| p1的2.2首段 | Q274 | 薄膜厚度趋零所固定的源量未说明；保留原判断及Heintz原拼法，未采用修正 |\n\n详见[7.1正文](../第七章%20Heinz论文解读/7.1%20解读Tony%20F.%20Heinz的综述.md)。本项未分配E编号。\n',encoding='utf-8')
f=o/'结构与分批计划.md';s=f.read_text(encoding='utf-8').replace('B609仅核p1原题、引言及2.1；','B609—B610已核p1全页与p2首图；').replace('B609完成，p1未全页','B609完成；p1余下由B610完成').replace('待译，图跨至p2','B610完成模型比较、一般方程及p2图；p2正文起待译')
s=re.sub(r'下一批B610[\s\S]*$','下一批B611从p2图后净电荷/电流与极化讨论起，处理原括注及(2a)—(2d)，止于Born & Wolf边界条件引句前。后续边界条件和跨页积分组另批。\n',s);f.write_text(s,encoding='utf-8')
f=d/'阅读导航.md';s=f.read_text(encoding='utf-8').replace('B609完成p1引言及2.1，尚未完成全页。','B609—B610完成p1全页及p2首图，2.2仍未完成。').replace('后续边界条件、辐射、表面和体相响应尚待译校。','2.2模型比较、图中坐标和一般麦克斯韦方程已核；Q274保留薄膜极限条件疑点。p2源极化及后续边界条件、辐射、表面和体相响应尚待译校。')
s=re.sub(r'下一批B610[^\n]*','下一批B611从p2图后的源电荷/电流与极化讨论开始，连同原括注及式(2a)—(2d)完整处理。',s);f.write_text(s,encoding='utf-8')
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8').replace('首批建立界面非线性源极化薄片及膜内场模型；边界条件、辐射与表面/体相响应待逐批译校','已完成p1模型、一般场方程及p2几何图；源极化、边界条件、辐射与表面/体相响应待逐批译校').replace('（翻译中，B609）：p1引言及2.1唯象模型已译校，说明面二阶非线性极化率、膜内电场与ε′的波长依赖。p1的2.2起待译。','（翻译中，B609—B610）：p1全页及p2首图已译校，包含唯象模型、极化薄片与有限厚膜比较及一般场方程。p2源极化讨论起待译，Q274保留。');f.write_text(s,encoding='utf-8')
f=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(f.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='7.1':row.update({'状态':'翻译中：B609—B610完成p1全页及p2首图；Q274待核','映射核验':'已核2.2模型比较、一般场方程和几何图；p2图后正文待译','公式图表范围':f'式(1)、3组一般场/附带关系及p2原图；累计{rr["math"]}数学片段排版通过','导读状态':'已根据B609—B610正文更新','导读草案':'面源极化、膜内场、薄膜极限的条件及一般麦克斯韦方程；后续源电荷/电流及边界条件待译。'})
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);f.write_text(b.getvalue(),encoding='utf-8')
tf=r/'翻译管理/术语表.tsv';rd=csv.DictReader(io.StringIO(tf.read_text(encoding='utf-8-sig')),delimiter='\t');ff=rd.fieldnames;rs=list(rd);assert not any(x['术语编号']=='T132' for x in rs)
rs.append(dict(zip(ff,['T132','volume polarization（底本英文）','volume polarization','体极化','','此段有限厚膜按体积元表示的极化，区别面极化及体二阶非线性极化率。','7.1 PDF p1的2.2 / B610','B610原页对照；非用户新确认','本段语境已核；中文暂用','原页已对照','译者暂用；非用户新确认','底本原列英文'])))
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=ff,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rs);tf.write_text(b.getvalue(),encoding='utf-8')
f=r/'翻译管理/当前进度与续接.md';s=f.read_text(encoding='utf-8').replace('## 当前有效状态：7.1首批B609完成','## 历史状态：7.1首批B609完成',1)
state=f'## 当前有效状态：7.1 B610完成，p1全页及p2首图完成（2026-10-22）\n\n本批13覆盖单元、3无编号公式组、1原图，完成2.2模型比较、跨页图及p1末麦克斯韦方程/附带关系。新增{n}数学片段、累计{rr["math"]}片段严格语法通过；原图及全幅排版已目视，无缺图/横向溢出。Q274保留薄膜极限条件与Heintz原拼法，无新增已采用修正。T132体极化暂译登记；符号、勘误索引、导航、序言和清单已更新。\n\n累计p1全页、p2仅首图已译，2.2未完成。下一批B611从p2“这里考虑的体系没有净电荷或电流，只具有极化P”起，处理源电荷/电流关系、原括注及式(2a)—(2d)，止于Born & Wolf边界条件引句前；跨p2—p3的边界积分论述另批，不截断半句。\n\n'
s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+state,1);f.write_text(s,encoding='utf-8');print('B610验收及全部管理记录更新完成。')

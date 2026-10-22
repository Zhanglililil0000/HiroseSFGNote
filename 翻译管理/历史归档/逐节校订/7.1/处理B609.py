from pathlib import Path
import json,hashlib,re,csv,io,sys
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;d=r/'中文版本/第七章 Heinz论文解读';d.mkdir(exist_ok=True)
src=r/'日语原版/Chapter7/chap7-1.pdf';p=d/'7.1 解读Tony F. Heinz的综述.md';f=o/'B609-本批译文.md'
t=f.read_text(encoding='utf-8').replace('片层','薄片');f.write_text(t,encoding='utf-8')
if '--finish' not in sys.argv:
 assert not p.exists();p.write_text(t,encoding='utf-8')
 units=['原题及引文的篇名、书名、编者、出版社、年份和章号','以和频应用为目的的解读范围','原内部第2章和2.1标题','界面与体相的区分','中心对称/各向同性并列及数埃厚度','电流薄片与广义非线性源极化薄片','Js=∂Ps/∂t','负时间因子与复共轭','式(1)全部下标、和频条件及张量缩并符号','膜介电常数ε′与膜内电场','非线性源辐射仍经同一线性介电响应','ε′的波长依赖及三频不同值']
 cov=[{'原文定位':'PDF p1 / 原题、引言与2.1','对象':v,'译文定位':'B609-本批译文.md对应段落或式(1)','已原页对照':True,'已翻译':True} for v in units]
 (o/'B609-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
 a={'批次':'B609','日期':'2026-10-22','范围':'PDF p1原题、引言、2.1全段；止于2.2标题前','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'translation_sha256':hashlib.sha256(t.encode()).hexdigest(),'覆盖单元':len(cov),'编号式':['1'],'原图':0,'新增原文疑点':[],'新增已采用修正':False,'已原页对照':True,'已排版':False,'p1全页完成':False}
 (o/'B609验收.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
 ren=(r/'翻译管理/校订记录/6.1/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/6.1','校订记录/7.1').replace('中文版本/第六章 偶极间相互作用','中文版本/第七章 Heinz论文解读').replace("startsWith('6.1 ')","startsWith('7.1 ')")
 (o/'检查排版.cjs').write_text(ren,encoding='utf-8');print('B609登记完成，等待排版。');sys.exit()
a=json.loads((o/'B609验收.json').read_text(encoding='utf-8'));rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));m=rr['results'][0]
assert not m['overs'] and m['scrollWidth']==1100 and all(i['loaded'] for i in m['images'])
assert t==p.read_text(encoding='utf-8') and hashlib.sha256(t.encode()).hexdigest()==a['translation_sha256']
a.update({'已排版':True,'数学片段':rr['math'],'全幅截图已目视':True,'横向溢出':False})
for name in ['B609验收.json','B609最终检查.json']:(o/name).write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B609.md').write_text(f'# B609｜7.1首批\n\np1原题、引言及2.1完整译校，12覆盖单元、1编号式、0原图。{rr["math"]}数学片段严格语法通过；全幅参考截图已目视，无横向溢出。未读入Heinz原章内容代替广濑笔记。\n\n无新增Q项或采用修正。下一批B610从2.2首段开始，注意图引句跨至p2示意图，不截断论述。\n',encoding='utf-8')
note='## 7.1首批局部约定（B609）\n\n- 负时间因子exp(-iωt)，加复共轭构成实场。\n- Js=∂Ps/∂t，Ps为广义非线性面源极化；χs²全称“面二阶非线性极化率”。沿T089，不补膜厚、ε0或体积因子。\n- ε′为膜/界面区域的线性介电常数，不是取实部符号；随频率变化。膜内场不同于外加场，具体边界条件待后续。\n- 原文内部第2章及2.1编号按Heinz解读结构保留，区别项目7.1。\n- p1只列两介质中心对称（或各向同性），不定义二者等价；此时尚未定完整坐标、法向或单位制。\n- 本稿是广濑解读笔记，所引Heinz书章尚未独立对照；后文原作省略保持省略。\n'
(o/'局部约定卡.md').write_text('# 7.1局部约定卡\n\n'+note,encoding='utf-8')
f=r/'翻译管理/符号与约定.md';f.write_text(f.read_text(encoding='utf-8')+'\n\n'+note,encoding='utf-8')
(o/'结构与分批计划.md').write_text('# 7.1结构与分批计划\n\n底本14页。B609仅核p1原题、引言及2.1；以下后续结构按文本缓存定位，尚未逐页译校。内部编号沿原。\n\n| 原部分 | PDF起页 | 状态 |\n|---|---|---|\n| 原题、引言、2.1唯象模型 | 1 | B609完成，p1未全页 |\n| 2.2极化薄片的边界条件 | 1 | 待译，图跨至p2 |\n| 2.3极化薄片的辐射 | 3 | 待译 |\n| 2.4表面非线性响应 | 7 | 待译 |\n| 2.5体相非线性响应 | 10（缓存定位） | 待译 |\n| 2.6讨论与第3章实验 | 14 | 原文多处省略，待按原页登记 |\n| 3.1各向同性、3.2各向异性介质 | 14 | 待译 |\n\n下一批B610先处理2.2开头的模型比较、示意图及其引句；麦克斯韦方程按完整公式组另选边界。常规“继续”按完整批次推进。\n',encoding='utf-8')
(d/'阅读导航.md').write_text('# 第七章阅读导航\n\n[7.1 解读Tony F. Heinz的综述](7.1%20解读Tony%20F.%20Heinz的综述.md)共14页。B609完成p1引言及2.1，尚未完成全页。\n\n已核部分：介绍所解读的Heinz综述；将界面与体相分开，采用面电流/非线性源极化薄片，用膜内场及随频率变化的ε′建立式(1)。后续边界条件、辐射、表面和体相响应尚待译校。\n\n7.2—7.5是独立附录文件，尚未翻译；不能因7.1内出现附录指引就视为这些文件完成。\n\n下一批B610从7.1 p1的2.2开始；首段与图引句应接到p2图后完整处理。\n',encoding='utf-8')
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8').replace('**本章导读（待正文核验）：** 结合正文与附录阅读 Heinz 论文的相关推导。','**本章导读（分批更新）：** 已启动7.1。首批建立界面非线性源极化薄片及膜内场模型；边界条件、辐射与表面/体相响应待逐批译校，独立附录7.2—7.5尚未开始。见[第七章阅读导航](中文版本/第七章%20Heinz论文解读/阅读导航.md)。').replace('- 7.1 Heinz 论文解读（待翻译）：进入论文解读正文。','- [7.1 解读Tony F. Heinz的综述](中文版本/第七章%20Heinz论文解读/7.1%20解读Tony%20F.%20Heinz的综述.md)（翻译中，B609）：p1引言及2.1唯象模型已译校，说明面二阶非线性极化率、膜内电场与ε′的波长依赖。p1的2.2起待译。');f.write_text(s,encoding='utf-8')
f=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(f.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='7.1':row.update({'中文工作名':'解读Tony F. Heinz的综述'} if '中文工作名' in fields else {})
 if row['编号']=='7.1':
  # 依现有列名更新，不增加新列。
  row[fields[2]]='解读Tony F. Heinz的综述';row[fields[6]]=p.relative_to(r).as_posix()
  row.update({'状态':'翻译中：B609完成p1引言及2.1；p1未全页','映射核验':'原题和2.1已原页核对，2.2起待译','公式图表范围':f'式(1)及局部定义已核；{rr["math"]}数学片段排版通过','导读状态':'已据首批正文更新','导读草案':'从非线性面源极化与膜内场模型开始，强调膜介电常数随频率变化；后续边界、辐射及体相响应待核。'})
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);f.write_text(b.getvalue(),encoding='utf-8')
f=r/'翻译管理/当前进度与续接.md';s=f.read_text(encoding='utf-8').replace('## 当前有效状态：6.1全节本轮完成','## 历史状态：6.1全节本轮完成',1)
state=f'## 当前有效状态：7.1首批B609完成（2026-10-22）\n\n7.1按原题命名《解读Tony F. Heinz的综述》，底本14页。完成PDF p1原题、引文、引言及2.1唯象模型，12覆盖单元、1编号式，{rr["math"]}数学片段严格语法与显示通过，全幅截图已目视，无横向溢出。无新增疑点或采用原文修正。局部约定、章节清单、序言及第七章导航已更新；术语沿T089面二阶非线性极化率，薄片/源极化/唯象模型为暂用，未作用户确认。\n\np1尚未全页完成。下一批B610从2.2“极化薄片的边界条件”开始，首段模型比较和图引句须接到p2示意图后，不能把“如下图”截成完整论述。后续原作省略按原文登记，不能补造。第七章及7.1均未完成；7.2—7.5未开始。\n\n'
s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+state,1);f.write_text(s,encoding='utf-8')
(o/'B609术语核对.md').write_text('# B609术语核对\n\n沿T089“面二阶非线性极化率”、T012“局域场”相关边界。polarization sheet暂用“极化薄片”，与既有T089说明统一；generalized nonlinear source polarization暂用“广义非线性源极化”；phenomenological model暂用“唯象模型”。均依本段语境，非用户新确认。ε′为介电常数，不改称极化率；Ps为面源极化，不改成χ。新术语登记见T129—T131。\n',encoding='utf-8')
tf=r/'翻译管理/术语表.tsv';rd=csv.DictReader(io.StringIO(tf.read_text(encoding='utf-8-sig')),delimiter='\t');ff=rd.fieldnames;rs=list(rd)
new=[('T129','分極のシート','polarization sheet','极化薄片','广义面源极化的薄片模型；与既有T089极化薄片用词衔接，非有限厚体极化。'),('T130','非線形ソース分極','nonlinear source polarization','非线性源极化','本段Ps，位于界面；与χs²分开，不补厚度或ε0。'),('T131','Phenomenological model','phenomenological model','唯象模型','原文2.1英文小标题，中文暂用。')]
for tid,ja,en,zh,context in new:
 row=dict(zip(ff,[tid,ja,en,zh,'',context,'7.1 PDF p1 / B609','B609原页对照；非用户新确认','本批语境已核；译名暂用','原页已对照','译者暂用；非用户新确认','英语对应原英文标题或译者辅助释义；按实际原文区分']))
 assert not any(x['术语编号']==tid for x in rs);rs.append(row)
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=ff,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rs);tf.write_text(b.getvalue(),encoding='utf-8')
print('B609完成验收及管理更新。')

from pathlib import Path
import json,hashlib,re,csv,io,sys
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;p=r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md';chunk=(o/'B568-本批译文.md').read_text(encoding='utf-8')
if '--finish' not in sys.argv:
 t=p.read_text(encoding='utf-8');assert '\\tag{1.10}' not in t
 t=re.sub(r'\n<!-- B567结束：[\s\S]*?-->\s*$','\n',t)
 t=t.replace('译校状态（B565—B567，2026-10-21）','译校状态（B565—B568，2026-10-21）').replace('包含式(1.1a)—(1.9)及相应脚注、笔记。p6“另一方面，在存在弛豫时的经典论中……”起尚未翻译，1.2仍未完成。','并已完成p6经典自由衰减及式(1.10)—(1.12)，累计含式(1.1a)—(1.12)及相应脚注、笔记。p6共振频率讨论起待译，1.2仍未完成。')
 t+='\n'+chunk+'\n<!-- B568结束：PDF p6式(1.12)后“对应关系成立”的段末。下一批B569自“接下来考察有弛豫时的共振频率（给出最大振幅的频率）”起，式(1.13)—(1.15)及近共振无编号式的段落跨至p7首段，应完整处理。 -->\n';p.write_text(t,encoding='utf-8')
 units=[('经典自由响应段','将(1.1b)右侧置零、位移及时间依赖'),('式(1.10)','e负γt、根式ω0²−γ²、根号外时间t'),('对应前提段','1.9/1.10应描述同一现象，稳态及瞬态两种响应'),('式(1.11)','γ双向箭头Γng，不改恒等号或倍数'),('式(1.12)及连接语','ω0²对应Γng²+ωng²'),('式后结句','对应关系成立的作者判断')]
 cov=[{'原文定位':'PDF p6 / '+a,'对象':b,'译文定位':'B568-本批译文.md对应段落或原式号','已翻译':True,'已原页对照':True} for a,b in units]
 (o/'B568-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
 rec={'批次':'B568','范围':'PDF p6经典自由衰减段至式(1.12)后对应关系句末','source_sha256':hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest(),'translation_sha256':hashlib.sha256(chunk.encode('utf-8')).hexdigest(),'覆盖单元':6,'编号式':['1.10','1.11','1.12'],'已起草':True,'已原页对照':True,'已排版':False,'新增疑点':[],'采用原文修正':False,'下一批':'B569，p6共振频率至p7首段近共振讨论'}
 (o/'B568验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8');print('B568已登记，待排版。');sys.exit()
rec=json.loads((o/'B568验收.json').read_text(encoding='utf-8'));rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));metric=next(x for x in rr['results'] if x['batch']=='B568')
assert not metric['overs'] and metric['scrollWidth']==1100
assert chunk in p.read_text(encoding='utf-8') and '\\tag{1.13}' not in p.read_text(encoding='utf-8')
assert hashlib.sha256(chunk.encode('utf-8')).hexdigest()==rec['translation_sha256']
assert hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest()==rec['source_sha256']
count=len(re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',chunk));assert rr['math']==125+count
rec.update({'已排版':True,'本批数学片段':count,'累计数学片段':rr['math'],'截图全幅目视':True,'p6全页完成':False})
(o/'B568验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B568.md').write_text(f'# B568｜经典自由衰减及参数对应\n\np6所列范围6个覆盖单元、3编号式；原图/脚注/书目均为0。根号范围、t位置、双向箭头及稳态/瞬态限定已对照；本批{count}个数学片段通过语法与显示检查，全幅截图已目视，无横向溢出。\n\n无新增原文疑点及已采用修正。两处γ按局部含义区分，未改(1.11)因子。p6共振频率段尚未译，下一批B569。\n',encoding='utf-8')
note='\n\n## B568补充（p6式1.10—1.12）\n\n(1.10)经典自由响应的指数率为γ，余弦频率为√(ω0²−γ²)，t在根号外。(1.11)保留γ↔Γng；(1.12)保留ω0²↔Γng²+ωng²。它们是作者在所比较稳态及瞬态响应之间的参数对应，不将箭头改为一般恒等号；前页笔记纵向γ=2Γng仍按其局部语境保存，不反改本式。\n'
for f in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:f.write_text(f.read_text(encoding='utf-8')+note,encoding='utf-8')
(o/'B568术语核对.md').write_text('# B568术语核对\n\n弛豫沿T053；经典阻尼γ仍与T082分子超极化率γ区分。稳态响应、瞬态响应依本句对应暂用；无新增需要定稿的概念条目。Q229—Q236维持原状态；本批无新增已采用勘误，勘误附件无需新增E条目。\n',encoding='utf-8')
f=r/'中文版本/第六章 偶极间相互作用/阅读导航.md';t=f.read_text(encoding='utf-8').replace('p6经典自由衰减段起待译。','另已完成p6经典自由衰减与式(1.10)—(1.12)，共振频率段起待译。',1)
t=t.replace('## 后续目录级预览（尚待正文核验）','- p6经典自由衰减及式(1.10)—(1.12)：根式频率、稳态/瞬态比较与γ↔Γng参数对应；纵向弛豫γ的笔记用法另保留。\n\n## 后续目录级预览（尚待正文核验）').replace('下一批从p6的经典自由衰减段开始。','下一批从p6的共振频率讨论开始。')
t=re.sub(r'下一批B568：[\s\S]*$','下一批B569：从p6“接下来考察有弛豫时的共振频率（给出最大振幅的频率）”起，完整处理式(1.13)—(1.15)及延续至p7首段的近共振无编号式和说明，不截半段。\n',t);f.write_text(t,encoding='utf-8')
f=r/'Preface序言.md';t=f.read_text(encoding='utf-8').replace('目前p1—5及p6开头的广濑笔记已译校。','目前p1—5及p6至式(1.12)的讨论已译校。').replace('（翻译中，p1—5及p6笔记首段完成）：原目录、1.1及1.2至式(1.9)和完整广濑笔记已译校；从线性响应进入自由演化与弛豫。','（翻译中，p1—5及p6部分完成）：原目录、1.1及1.2至式(1.12)已译校，涵盖完整广濑笔记、经典自由衰减及量子/经典参数对应。');f.write_text(t,encoding='utf-8')
f=r/'翻译管理/章节清单.tsv';rd=csv.DictReader(io.StringIO(f.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='6.1':row.update({'状态':'翻译中：B565—B568完成p1—5及p6至式(1.12)，均已对照排版','映射核验':'已核至经典自由衰减及参数对应；p6共振频率段起待译','公式图表范围':'式(1.1a/b)—(1.12)、脚注及完整广濑笔记已核；(1.13)起待译','导读状态':'分批导读，更新至B568'})
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);f.write_bytes(b.getvalue().encode('utf-8'))
f=o/'结构与分批计划.md';f.write_text(f.read_text(encoding='utf-8')+'\n\nB568完成p6经典自由衰减及式(1.10)—(1.12)；B569从共振频率讨论起，近共振段跨至p7首段须完整处理。\n',encoding='utf-8')
f=r/'翻译管理/当前进度与续接.md';t=f.read_text(encoding='utf-8').replace('## 当前有效状态：6.1 B567完成','## 历史状态：6.1 B567完成',1)
new=f'## 当前有效状态：6.1 B568完成，推进至式(1.12)（2026-10-21）\n\n本批p6经典自由衰减及参数对应，6个覆盖单元、3编号式；新增{count}个数学片段，累计{rr["math"]}个片段语法通过，全幅排版已目视，无横向溢出。无新增疑点或已采用原文修正；γ↔Γng与前页纵向弛豫γ的局部用法分别保留。序言、导航、符号和章节清单已同步。\n\n累计p1—5完整及p6至式(1.12)完成，p6尚未全页、1.2未完。下一批B569从p6共振频率讨论起，式(1.13)—(1.15)及近共振无编号式延续至p7首段，应完整处理，不在页末截断。\n\n'
t=t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+new,1);f.write_text(t,encoding='utf-8')
(o/'B568最终检查.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8');print('B568验收及管理更新完成。')

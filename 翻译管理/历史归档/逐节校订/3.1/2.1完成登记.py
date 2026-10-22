from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';s=p.read_text(encoding='utf-8');checked=s[:s.index('### 2.2 SFG极化')];sec=checked[checked.index('## 2. 二层系'):]
expected=[f'2.{n}' for n in range(1,10)]+['2.10a','2.10b','2.11','2.12a','2.12b','2.13','2.14a','2.14b','2.15','2.16a','2.16b','2.17'];tags=re.findall(r'\\tag\{([^}]+)\}',sec);assert tags==expected and len(tags)==21
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
prior=(o/'B170-修订前.md').read_text(encoding='utf-8');key='### 2.2 SFG极化';assert s[s.index(key):]==prior[prior.index(key):]
v=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));assert all(not x['overs'] for x in v['results'])
def append(f,t):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
q=(o/'2.1-疑点登记待同步.md').read_text(encoding='utf-8');append(m/'疑难与勘误.md','## 3.1的2.1剩余原文疑点（2026-10-20）\n\n'+q)
append(o/'局部约定卡.md','## B170—B174及2.1完成约定\n\n三界面两侧及m′/m两体相位置的正反向源均已核。保留2.8红外因子与2.9差异（Q098）；2.10b/2.12b单场红外相位中vis指标不改（Q099）。m层场位置hm+z2及反向B源上标m′均按原文（Q100）。2.15/2.17重复左花括号无闭合保留（Q101）；圆括号经文字层确认完整，无圆括号勘误。所有传播指数中的i经原图与文字层核实存在，不登记为缺i。正反向A/B源标签按原式保留，n计数定义仍不得补作已确认。')
append(o/'结构与复用核验表.md','## 2.1最终覆盖（2026-10-20）\n\nB165—B174完成PDF p3—9至式2.17：三个界面两侧共9式，两体相位置各两组单场及四项乘积共12式，合计21个唯一编号。所有跨页接全，无图表或省略。B163—B164开篇与第1部分完成状态继续有效。第2.2起未改，下一批B175。')
f=m/'当前进度与续接.md';t=f.read_text(encoding='utf-8-sig');h,rest=t.split('\n',1);f.write_text(h+'\n\n## 当前有效状态：3.1内2.1全小节完成（2026-10-20）\n\nB165—B174完成p3—9至式2.17，21个唯一编号式：三界面两侧、两膜体相的正反向源单场及四项乘积全部覆盖。B163—B164原目录/引言/第1部分仍已完成。Q098—Q101保留原文并就地说明，无原文公式修正采用。\n\n下一批B175：从PDF p9的2.2和频极化引言及1/m′界面1侧式2.18开始。确认χ为二阶非线性极化率、P星号是本节原符号而非自动视作共轭、作者只列去相位振幅的范围；逐项核对与2.1的对应，不直接复制已验收状态。第2.2起仍为旧译，未开始本轮校订。以下为历史记录。\n'+rest,encoding='utf-8')
for f,keyfield in [(m/'章节清单.tsv','编号'),(m/'全书调查/分批建议.tsv','节号')]:
 with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
 for row in rows:
  if row[keyfield]=='3.1':
   if keyfield=='编号':row.update({'状态':'B163—B174完成开篇、第1部分及2.1全小节；2.2起待校订','映射核验':'p1—9已核至2.1式2.17末；2.2起仍待逐项校订','公式图表范围':'25组无编号系数展示式及2.1的21个唯一编号式均已核；后续待核','导读状态':'已按2.1全部内容更新；2.2起仅目录定位'})
   elif int(row['PDF起页'])<=8:row['执行状态']='2026-10-20 B163—B174完成开篇、第1部分及2.1全小节（p3—9至2.17，21编号式）；2.2起未校订，不按页整体认定完成'
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
f=r/'Preface序言.md';t=f.read_text(encoding='utf-8-sig');t=t.replace('B163—B169已核第1部分及2.1引言、式2.1—2.7；后续待校订','B163—B174完成第1部分及2.1全小节；2.2起待校订');f.write_text(t,encoding='utf-8')
f=p.parent/'阅读导航.md';t=f.read_text(encoding='utf-8-sig');t=t.replace('当前3.1开篇、第1部分及2.1前七式B163—B169已完成本轮译校','当前3.1开篇、第1部分及2.1全小节B163—B174已完成本轮译校');t+='\n\n### 2.1完成范围（2026-10-20）\n\np3—9至式2.17，共21个唯一编号式。三界面两侧按1/m′、m/2、m′/m依次列出，继而处理m′层深度z1与m层距内部界面深度z2处的正反向源；每组均保留单频场和完整四项乘积。Q098—Q101分别说明红外因子、相位指标、局部坐标/层标及括号疑点，未采用原式修正。下一步为2.2和频极化，正文该段仍是待校订旧译。\n';t=t.replace('m侧式2.8起仍待逐项核对。','m侧式2.8—2.9及两个体相位置至2.17均已核，详见下方完成范围。');f.write_text(t,encoding='utf-8')
f=r/'中文版本/附件/原文勘误表.md';t=f.read_text(encoding='utf-8-sig');mark='## 后续维护';assert mark in t;t=t.replace(mark,'## 3.1至2.1的疑点状态（2026-10-20）\n\nQ096—Q101均保留原式或原文，候选未采用；不新增已采用勘误编号。恢复旧译自行统一的B源层标属于转写修复。具体疑点见正文与管理记录；后续确认后再按顺序收录正式勘误。\n\n'+mark,1);f.write_text(t,encoding='utf-8')
for n in range(170,175):
 b=f'B{n}';c=json.loads((o/(b+'-覆盖.json')).read_text(encoding='utf-8'));c.update({'math_syntax_errors':0,'display_overflows':0,'render_preview_checked':True});(o/(b+'验收.json')).write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'2.1-公式编号索引.json').write_text(json.dumps({'count':21,'tags':tags},ensure_ascii=False,indent=2),encoding='utf-8')
(o/'2.1-完整译校文本.md').write_text(checked,encoding='utf-8')
result={'date':'2026-10-20','section':'3.1内2.1','status':'小节页面对照、译校与分批排版完成','pages':[3,4,5,6,7,8,9],'batches':'B165—B174','unique_numbered_equations':21,'source_formula_corrections_adopted':False,'unresolved':'Q097—Q101；Q096属前段L定义','next':'B175 / 2.2引言与式2.18','later_text_unchanged':True}
(o/'2.1-完成复核.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');(o/'2.1-完成复核.md').write_text('# 3.1中2.1完整小节复核\n\n2026-10-20；B165—B174，PDF p3—9至式2.17，21个唯一编号式，顺序、完整性、跨页接续均已检查。三个界面两侧、两个体相位置四组正反向源及其四项乘积全部保留。前段B163—B164已核25个无编号系数展示式。\n\n五批剩余公式原页逐项核对，14个编号式仅合并显示与分行，未采用任何源式候选修正。B174恢复原B源层标m′，与原文勘误分开。Q097—Q101保留并注；i字形复核存在，圆括号文字层确认完整，不作为勘误。所有批次KaTeX严格语法和横向溢出检查通过，B170—B174渲染图逐批查看。\n\n2.2起与B170修订前逐字一致，未冒记完成。下一批B175核2.2引言与2.18。译校完成不等于未决原式已获得代数认证。\n',encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

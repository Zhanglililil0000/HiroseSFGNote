from pathlib import Path
import re,json,csv,hashlib,io
from PIL import Image
root=Path('HiroseSFGNote'); m=root/'翻译管理'; out=m/'校订记录/2.6'; chapter=root/'中文版本/第二章 薄膜产生的SFG'; p=chapter/'2.6 薄膜内的电场.md'
s=p.read_text(encoding='utf-8'); tags=re.findall(r'\\tag\{([^}]+)\}',s)
assert len(tags)==len(set(tags))==86
expected=['1.1','1.2']+[f'1.{n}{a}' for n in [3,4] for a in 'abc']+['1.5a','1.5b','2.1','2.2a','2.2b']+[f'2.{n}{a}' for n in range(3,10) for a in 'ab']+[f'3.{n}{a}' for n in range(1,5) for a in 'ab']+['4.1a','4.2a','4.1b','4.2b','4.3a','4.4a','4.5a','4.3b','4.4b','4.5b','4.6a','4.6b','4.6c']+[f'4.{n}{a}' for start,end in [(7,11),(11,15),(15,20)] for a in 'ab' for n in range(start,end)]+['4.20a','4.20b']+[f'4.{n}' for n in range(21,25)]+['4.25a','4.25b']+[f'4.{n}' for n in range(26,30)]
assert tags==expected,(tags,expected)
summary='比较相位、坐标与偏振约定；建立传播矩阵及电场幅基变换，展开一至四个界面的矩阵，并给出单层、双层、三层膜各区电场及零厚度极限。'
s=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B146—B162完成独立PDF全12页的页面对照、译校与数学排版；86个唯一编号式及无编号定义/推导均已覆盖。原文疑点Q086—Q095保留原值并就地说明，未采用原文公式修正。',s)
s=re.sub(r'\*\*阅读导引（译者编写）：\*\*[^\n]+','**阅读导引（译者编写）：** '+summary+' 阅读时先核本节局部方向、相位与矩阵顺序；原式疑点不因译校完成而视为已解决。',s)
p.write_text(s,encoding='utf-8')
def append(path,text):
 path.write_text(path.read_text(encoding='utf-8-sig')+'\n\n'+text+'\n',encoding='utf-8')
for f,key in [(m/'章节清单.tsv','编号'),(m/'全书调查/分批建议.tsv','节号')]:
 with f.open(encoding='utf-8-sig',newline='') as h: reader=csv.DictReader(h,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
 for row in rows:
  if row[key]=='2.6':
   if key=='编号': row.update({'状态':'本轮全节页面对照及排版整理完成；原式疑难未决','映射核验':'全12页已按B146—B162对照','公式图表范围':'86个唯一编号式及无编号项目已覆盖；无独立图表','导读状态':'已根据全节正文更新；见Preface与第二章阅读导航','导读草案':summary})
   else: row['执行状态']='2026-10-20全12页已按B146—B162完成译校及排版；86编号式，Q086—Q095保留，见2.6整节完成复核'
 with f.open('w',encoding='utf-8-sig',newline='') as h: w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
pref=root/'Preface序言.md'; t=pref.read_text(encoding='utf-8-sig'); t=re.sub(r'(^- \[2\.6[^\n]+?\.md\))[^\n]*',lambda a:a[1]+'（全12页译校完成，B146—B162）：'+summary,t,flags=re.M); pref.write_text(t,encoding='utf-8')
nav=chapter/'阅读导航.md';t=nav.read_text(encoding='utf-8-sig');t=t[:t.index('## 2.6 薄膜内的电场')]+'''## 2.6 薄膜内的电场

[进入正文](2.6%20薄膜内的电场.md)。独立12页，B146—B162完成全节译校与数学排版；86个唯一编号式及无编号关系齐备。

1. 绪论（p1—2）：比较教材的相位、坐标及偏振约定，定义方向和电磁场关系。
2. 传播矩阵（p2—4）：由总电磁场转到正反电场幅；M与N连接方向相反，逐层乘积顺序相反。
3. 界面数与矩阵（p4—6）：展开一至四个界面的s/p矩阵，四界面情形逐项保留四个矩阵元素。
4. 层数与电场（p6）：先给普通双介质界面及末介质仅正向波的边界条件。
5. 单层膜（p7—8）：各区域正反场、和差场及零厚度极限，并说明轴向分量。
6. 双层膜（p8—9）：各区场及前、后膜层分别趋零的极限。
7. 三层膜（p9—12）：五处电场及和差场，继而取表面层趋零和前后表面层同时趋零两种极限。

本节L为基变换矩阵，区别于前节极化源出射L系数；β为传播参数。Q086—Q095均保留原文并就地列疑点与候选，未采用原式修正。长式仅分行，无省略或公式截图替代。
''';nav.write_text(t,encoding='utf-8')
progress=m/'当前进度与续接.md';t=progress.read_text(encoding='utf-8-sig'); first,rest=t.split('\n',1);progress.write_text(first+'\n\n## 当前有效状态：2.6全节完成（2026-10-20）\n\nB146—B162完成全12页译校、86个唯一编号式和无编号关系的覆盖与排版检查。Q086—Q095保留原式并就地说明，未采用原文公式修正。序言、导航、章节清单和疑难记录已同步。\n\n下一批为B163；按全书顺序进入3.1（二层与三层膜，51页），应先核结构、局部约定和与第二章复用边界，按完整推导小批推进。本次未开始3.1翻译。以下为历史记录。\n'+rest,encoding='utf-8')
notes=re.findall(r'> \*\*原文疑点（(Q0(?:88|89|90|91|92|93|94|95))[^\n]*',s)
globalq=m/'疑难与勘误.md';t=globalq.read_text(encoding='utf-8-sig');t+='\n\n## 2.6剩余原文疑点（2026-10-20）\n\n'
for q in range(88,96):
 qid=f'Q{q:03}'; lines=[x[2:] for x in s.splitlines() if x.startswith('> **原文') and ('（'+qid) in x]
 assert lines
 t+='\n\n'.join(lines)+'\n\n'
globalq.write_text(t,encoding='utf-8')
convention='## 2026-10-20全节约定补充\n\n本节L^x/L^y是总电磁场与正反电场幅之间的基变换，不能与2.5的极化源出射L因子互换。β=k cosθ为传播参数，不是分子一阶超极化率。M从末端连起点、N从起点连末端；层索引置下标、偏振置上标。粗体M/N与花体M/N区分两套基底的矩阵；原页局部符号差异见Q088—Q095，不作跨式静默统一。'
append(out/'局部约定卡.md',convention);append(m/'符号与约定.md',convention)
append(out/'结构与复用核验表.md','## 最终覆盖状态（2026-10-20）\n\nB146—B162覆盖全12页及结语，86个唯一编号式。第2、3、4部分及三层膜两种零厚度极限均已逐项处理；此前“待核”为历史状态。无独立图表，无原文公式修正采用。')
err=root/'中文版本/附件/原文勘误表.md';t=err.read_text(encoding='utf-8-sig');marker='## 后续维护';add='## 2.6 原文疑点的收录状态（2026-10-20）\n\n全12页已核。Q086—Q095为未确认疑点，均在正文保留原文并注明候选；本轮未采用原文公式修正，因此不新增已采用勘误编号。详见翻译管理疑难记录及正文相应位置。旧译转写修复与原文勘误分别记录。\n\n';assert marker in t;t=t.replace(marker,add+marker,1);err.write_text(t,encoding='utf-8')
index=[]
for n in range(146,163):
 b=f'B{n}';cover=json.loads((out/(b+'-覆盖.json')).read_text(encoding='utf-8'))
 for tag in cover.get('tags',[]): index.append({'tag':tag,'batch':b,'pages':cover.get('pages')})
 if n>=151:
  (out/(b+'验收.json')).write_text(json.dumps({'batch':b,'date':'2026-10-20','coverage':cover,'math_syntax_errors':0,'display_overflows':0,'render_preview_checked':True,'source_formula_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'全节公式编号索引.json').write_text(json.dumps({'count':86,'tags':tags,'batch_map':index},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'全节公式编号索引.md').write_text('# 2.6全节公式编号索引\n\n共86个唯一编号式，按正文顺序；无缺号、重复或空编号占位。\n\n'+', '.join(tags)+'\n',encoding='utf-8')
(out/'全节单元覆盖.md').write_text('# 2.6全节单元覆盖\n\n'+ '\n'.join(f'- B{n}：'+json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8')).get('units','见本批覆盖记录') for n in range(146,163))+'\n\n全12页及结语已接全；跨页矩阵、分母与公式组不以页末截断。无独立图表。\n',encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter2/chap2-6.pdf').read_bytes()).hexdigest();assert sha=='329e6cc656b6e143555bac82f6320e9dd051ee782f93151a1c743159f76f2f35'
metrics=json.loads((out/'整节渲染检查.json').read_text(encoding='utf-8'));assert not metrics['results'][0]['overs']
result={'date':'2026-10-20','status':'本轮全节译校与排版完成；原式疑点未决','pages':12,'batches':'B146—B162','unique_numbered_equations':86,'math_fragments':metrics['math'],'math_syntax_errors':0,'display_overflows':0,'unresolved':'Q086—Q095','source_formula_corrections_adopted':False,'source_sha256':sha,'next_batch':'B163 / 3.1结构核验'}
(out/'整节完成复核.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'整节完成复核.md').write_text('# 2.6整节完成复核\n\n2026-10-20；独立PDF全12页，B146—B162。原页逐项对照、旧译校订、跨页接续与可编辑数学排版完成。\n\n86个唯一编号式已按预期顺序逐一核对；无编号定义及中间推导保留。227处数学片段严格语法检查通过，整节和批次均无横向溢出。批次参考图已检查；长矩阵与分式仅作等值分行，无物理量简写和公式截图。\n\nQ086—Q095仍未确认，正文原值及候选说明保留；未采用原文公式修正。已恢复的旧译转写错误不计为原文勘误。完成译校不表示已独立证明所有原式正确。\n\n底本SHA256：`'+sha+'`，未改动。管理、导航、序言及附件状态同步。下一批B163先调查3.1局部结构与约定。\n',encoding='utf-8')
tile=json.loads((out/'全文分屏.json').read_text()); canvas=Image.new('RGB',(1100,tile['height']),'white')
for row in tile['tiles']:canvas.paste(Image.open(out/row['file']),(0,row['y']))
canvas.save(out/'整节-参考渲染.png')
print(json.dumps(result,ensure_ascii=False))

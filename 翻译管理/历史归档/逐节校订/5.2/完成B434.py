from pathlib import Path
from urllib.parse import unquote
import json,csv,io,hashlib,re
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
p=o/'B434验收.json';d=json.loads(p.read_text(encoding='utf-8'));check=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'))
assert check['math']==38 and len(check['results'])==1
assert check['results'][0]['scrollWidth']==check['results'][0]['width'] and not check['results'][0]['overs']
target=r/'中文版本/第五章 张量与对称性/5.2 主要点群的特征标表与基底.md'
assert hashlib.sha256(target.read_text(encoding='utf-8').encode('utf-8')).hexdigest()==d['translation_sha256']
d.update({'已排版':True,'数学片段':38,'显示复核':'参考截图已查看；21页组目录完整、星号可见，无横向溢出','复核性质':'模型原页二次对照，不作为选择规则的独立物理认证'})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
p=o/'B434.md';t=p.read_text(encoding='utf-8');note='\n排版验收：38个数学片段严格语法检查通过；参考截图已查看，目录21行及原星号可见，视口与内容宽度均1100，无横向溢出。无新增已采用原文修正，勘误附件不新增已确认项。\n'
if note not in t:p.write_text(t+note,encoding='utf-8')
p=r/'翻译管理/章节清单.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['编号']=='5.2':row['状态']='翻译中：B434完成p1/22原页对照及参考排版；p2—22待译'
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8');t=t.replace('- 5.2 基底与特征标表（待翻译）：阅读基底和特征标表。','- [5.2 主要点群的特征标表与基底](中文版本/第五章%20张量与对称性/5.2%20主要点群的特征标表与基底.md)（翻译中，p1/22已完成）：已译张量记号、非零分量及拉曼规则说明和完整查表目录；p2—22各点群表仍待核验，目录星号见Q209。');p.write_text(t,encoding='utf-8')
p=r/'中文版本/第五章 张量与对称性/阅读导航.md';t=p.read_text(encoding='utf-8').replace('本章5.1已完成本轮译校及排版，5.2—5.6尚未开始；全章尚未完成。','本章5.1已完成本轮译校及排版，5.2已完成首页，5.3—5.6尚未开始；全章尚未完成。').replace('- 5.2 基底与特征标表：22页，下一节；点群表按页核对。','- [5.2 主要点群的特征标表与基底](5.2%20主要点群的特征标表与基底.md)：B434完成首页的记号、适用规则及全节目录。全22页，p2—22各点群表尚待逐项核验；目录星号Q209保留。下一批从p2 Cs块开始。');p.write_text(t,encoding='utf-8')
card='## 5.2初始约定（B434，p1）\n\nV/D/Y/W分别为1/2/3/4指标张量；abc为分子固定系。D不沿用5.1的变换矩阵含义。SHG/SFG二阶响应、CARS/CSRS/THG三阶响应与张量指标数区分；后续分子β/γ仍按用户确认命名。无分子激发的非零分量规则与拉曼模式规则分开；abba次序原样保留。目录星号表示作者标记的和频活性，与5.1附录B左上星号含义不同；Q209保留待核，不据星号预先修订后续表格。'
p=r/'翻译管理/符号与约定.md';t=p.read_text(encoding='utf-8')
if card not in t:p.write_text(t.rstrip()+'\n\n'+card+'\n',encoding='utf-8')
(o/'术语卡.md').write_text('# 5.2首批术语索引\n\n沿用术语表的特征标表、基底张量、不可约表示、全对称表示及用户确认的非线性极化率/超极化率命名，无新增关键译名。作者本节V/D/Y/W与前节记号差异见局部约定卡。首批未核验p2起的点群表，不升级其表项状态。\n',encoding='utf-8')
p=r/'翻译管理/当前进度与续接.md';t=p.read_text(encoding='utf-8');marker='## 当前有效状态：5.2首批B434完成（2026-10-21）\n\n5.2按底本原题命名为《主要点群的特征标表与基底》。全22页，本批只完成p1全页：张量记号、适用过程、非零分量与拉曼规则说明、两栏完整目录；目录转为21个页组单栏表。26个覆盖单元，38个数学片段语法检查通过，参考截图已视觉核对，无横向溢出。Q209保留原星号，不作选择规则认证；无新增已采用原文修正。章节清单、序言、导航及符号记录已更新。\n\n下一批B435：PDF p2的Cs特征标表、分子示例、基底分类及非零分量完整块；Ci/C2按表格密度另批处理。p2—22尚未译校，5.2未完成。\n\n以下为历史记录。\n\n'
if marker not in t:p.write_text(t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+marker,1),encoding='utf-8')
# Final checks: source identity, full catalog, and newly published reader links.
assert hashlib.sha256((r/d['底本']).read_bytes()).hexdigest()==d['source_sha256']
body=target.read_text(encoding='utf-8');assert len(re.findall(r'^\| \d+ \|',body,re.M))==21
assert len(json.loads((o/'B434-覆盖.json').read_text(encoding='utf-8')))==26
for doc in [r/'Preface序言.md',r/'中文版本/第五章 张量与对称性/阅读导航.md']:
 for raw in re.findall(r'\]\(([^\n)]+)\)',doc.read_text(encoding='utf-8')):
  if raw.startswith(('http:','https:','#')):continue
  assert (doc.parent/unquote(raw.split('#')[0])).exists(),raw
(o/'B434最终检查.json').write_text(json.dumps({'状态':'通过','p1覆盖单元':26,'目录页组':21,'数学片段':38,'源摘要匹配':True,'新导航链接有效':True,'疑点':'Q209原标记保留，候选未采用','完成范围':'仅p1；p2—22待译'},ensure_ascii=False,indent=2),encoding='utf-8')
print('B434完成：5.2 p1/22；下一批B435从p2 Cs块开始。')

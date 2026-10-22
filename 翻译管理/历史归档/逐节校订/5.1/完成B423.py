from pathlib import Path
import json,csv,io,re
r=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
p=out/'B423验收.json';d=json.loads(p.read_text(encoding='utf-8')); check=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert check['math']==23 and all(x['scrollWidth']==x['width'] and not x['overs'] for x in check['results'])
d.update({'已排版':True,'数学语法检查':'23个数学片段通过KaTeX严格检查','显示复核':'已查看B423参考截图，段落及公式可读；无横向溢出','复核性质':'模型原页二次对照，不是独立物理审校'})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
p=r/'翻译管理/章节清单.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['编号']=='5.1':row['状态']='翻译中：B423完成p1/7原页对照及参考排版；p2起待译'
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
p=r/'翻译管理/术语表.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;terms=list(reader);n=max(int(re.search(r'\d+',x['术语编号']).group()) for x in terms)
for jp,en,zh,note in [
 ('次元数','order','指标数（本节定义）','5.1明确解释为表示张量分量所需下标数；与矩阵维数及电场响应阶数区分。'),
 ('階数','rank','不可约角动量阶数（本节定义）','5.1定义为最小混合分量数2n+1对应的n；不是矩阵秩。不向前章全局替换。'),
 ('置換反転群','permutation-inversion group','置换反演群','正文明确列英语；用于柔性分子对称性。附录A尚未译校。')]:
 if any(x['日语候选']==jp and x['推荐中文候选']==zh for x in terms):continue
 n+=1;row={k:'' for k in fields};row.update({'术语编号':f'T{n:03d}','日语候选':jp,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':note,'原文位置':'5.1 PDF p1 / B423','依据':'本页原词、英文及作者定义已视觉核对；中文为译者暂用','状态':'原词及定义已页面对照；中文暂用','文本定位状态':'B423已核对原页','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'底本本页明确提供英文'});terms.append(row)
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(terms);p.write_bytes(s.getvalue().encode('utf-8'))
p=r/'翻译管理/当前进度与续接.md';t=p.read_text(encoding='utf-8');marker='## 当前有效状态：5.1首批B423完成（2026-10-21）\n\n第五章已启动。5.1《和频张量与对称性》全7页，本批完成PDF p1全页：9个覆盖单元、4个无编号独立公式及C₃ᵥ两个基底符号。23个数学片段严格语法检查通过，参考渲染已视觉核对，无横向溢出。Q198、Q199保留原文，未采用任何原文修正；勘误附件无新增已采用项。术语、局部约定、序言、第五章导航及章节清单已同步更新。\n\n下一批B424：从PDF p2首“電場成分Ej”开始，先完整处理电场/不可约基底定义、式(1a)—(1c)及式(2)；表1另批。p2—7尚未翻译，不将本节或本章标为完成。\n\n以下为历史记录。\n\n';
if marker not in t:p.write_text(t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+marker,1),encoding='utf-8')
p=out/'B423.md';t=p.read_text(encoding='utf-8');t+='\n排版验收：23个数学片段KaTeX严格检查通过；参考截图已查看，页面宽度1100，内容宽度1100，无公式横向溢出。首批完成；下一批B424。无新增已采用的原文修正，附件无需新增修正条目。\n';p.write_text(t,encoding='utf-8')
# Verify coverage, source identity, and the canonical file match the accepted batch.
import hashlib
assert hashlib.sha256((r/d['底本']).read_bytes()).hexdigest()==d['source_sha256']
assert hashlib.sha256((r/d['译文']).read_text(encoding='utf-8').encode('utf-8')).hexdigest()==d['translation_sha256']
assert len(json.loads((out/'B423-覆盖.json').read_text(encoding='utf-8')))==9
print('B423完成：p1/7；覆盖9项；数学片段23；已核对显示；下一批B424。')

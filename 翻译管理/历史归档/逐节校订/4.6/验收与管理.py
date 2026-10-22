from pathlib import Path
import re,json,hashlib,csv,io
from urllib.parse import unquote
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.6 CH₃基团的C₃ᵥ对称性破缺时的处理.md'
s=target.read_text(encoding='utf-8')
b=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));w=json.loads((out/'整节渲染检查.json').read_text(encoding='utf-8'))
assert b['math']==w['math']==92
assert len(b['results'])==3
assert all(not r['overs'] and r['width']==r['scrollWidth'] for r in b['results']+w['results'])
assert len(re.findall(r'^# ',s,re.M))==1 and len(re.findall(r'^## [1-3]\. ',s,re.M))==3
assert all(f'Q{q}' in s for q in range(176,180))
assert not re.search(r'[\u3040-\u30ff]',s)
assert not any(ord(c)<32 and c not in '\r\n\t' for c in s)
assert len(re.findall(r'\\begin\{bmatrix\}',s))==7
assert not re.findall(r'\\tag\{',s)
assert r'\dfrac{G_1}{[(E_1-E_2)/2-' in s
assert r's=\sqrt{2/3}' in s and r't=\sqrt{1/3}' in s
assert r'Q_1\approx(1\sqrt3)' in s and r'Q_2\approx(1\sqrt6)' in s
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-6.pdf').read_bytes()).hexdigest()
pages=set();index=[]
for n in range(362,365):
 c=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'));pages.update(c['pages'])
 t=(out/f'B{n}-本批译文.md').read_text(encoding='utf-8')
 rec={**c,'status':'本批译校及参考排版验收完成','render':next(r for r in b['results'] if r['batch']==f'B{n}'),'translation_sha256':hashlib.sha256(t.encode()).hexdigest(),'scope_limit':'覆盖、转录及参考排版核验；原文推导和适用范围疑点仍待核。'}
 (out/f'B{n}验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 index.append({'batch':f'B{n}','pages':c['pages'],'scope':c['scope'],'display_blocks':c['display_blocks']})
assert pages=={1,2,3}
(out/'全节公式与覆盖索引.json').write_text(json.dumps({'batches':index,'display_blocks':sum(x['display_blocks'] for x in index),'numbered_equations':0,'matrix_groups':5,'bmatrix_occurrences':7},ensure_ascii=False,indent=2),encoding='utf-8')
report={'date':'2026-10-21','section':'4.6','status':'全节译校完成，原文疑点待核','source_pages':3,'printed_page_labels':[1,2,3],'source_sha256':sha,'translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'batches':'B362—B364','matrix_groups':5,'display_blocks':sum(x['display_blocks'] for x in index),'numbered_equations':0,'math_fragments':92,'math_syntax_errors':0,'formula_overflows':0,'open_source_issues':'Q176—Q179','source_corrections_adopted':False,'next_batch':'B365，4.7原题、结构及局部约定核验'}
(out/'整节完成复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'整节完成复核.md').write_text('''# 4.6整节完成复核

2026-10-21，B362—B364，原PDF全3页完成本轮译校。

- 原题为CH₃基团C₃ᵥ对称性破缺时的处理，主题由旧文件名“CH₂弯曲振动”恢复；路径保留以兼容链接。
- p1三段对称性/模式说明、S定义、GR/FR/GS及全部参数与单位；p2 FS、GF五分量、本征值与D展开、谱带分裂/位移及Td近似；p3 L矩阵、双层分式、归一化、Q1/Q2和结论均逐页核对，无独立插图遗漏。
- 五个矩阵组（S/Ls定义、GR、FR、GS、FS）和全部无编号关系可编辑；没有为原文补造公式编号。公式展示块及页界见覆盖索引。
- 旧译√2误作2、Td根号范围及L11²/L22²内部除法误作乘法均按原页修复。原c/C、S/s、tilde Ls与转置t记法分别保留，斜线范围未自行确定。
- Q176活性结论的实验条件范围、Q177斜线分母范围、Q178对角记号/质量归一化、Q179末两模式根号前缺斜线，均原式或原述保留并就地说明；候选未采用，无新增已采用的原文修正。
- 92个数学片段通过严格KaTeX语法检查；3批及合稿在1100像素视口无公式横向溢出。已检查矩阵、长式、嵌套分式与连续预览。
- 全3页页脚实核为1、2、3，已纠正旧结构调查“非连续页码”的管理备注；这是管理记录修复，不是原文勘误。
- 已同步序言、章节导航、章节清单、进度、局部术语/符号、疑难及勘误附件状态。

验收确认翻译覆盖、转录与参考排版，不等于独立证明原文推导。未决公式和选择规则适用范围仍需专业核实。

下一批B365进入4.7，先核原题、结构与局部约定。
''',encoding='utf-8')
p=root/'翻译管理/当前进度与续接.md';old=p.read_text(encoding='utf-8');mark='## 当前有效状态：4.6全节译校完成（2026-10-21）'
if mark not in old:p.write_text('# 当前进度与续接\n\n'+mark+'\n\nB362—B364覆盖原PDF全3页及5个矩阵组、本征值/谱带/模式的全部关系。恢复CH₃对称性破缺主题，修复√2、Td根号范围及L矩阵嵌套分式；原Q176—Q179保留并就地说明，未采用原文修正。92个数学片段及合稿排版通过。旧调查页脚非连续的备注已据页图改为1—3。\n\n下一批B365：进入4.7，先核原题、结构、局部坐标及公式条件。以下为历史记录。\n\n'+old.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for r in rows:
 if r['编号']=='4.6':r.update({'暂定中文标题':'CH₃基团的C₃ᵥ对称性破缺时的处理','状态':'本轮全节页面对照及参考排版完成；原文疑点待核','映射核验':'全3页按B362—B364对照，实际页脚为1、2、3','公式图表范围':'5个矩阵组、GF五分量、本征值与近似、L及模式关系完整覆盖；92个数学片段','导读状态':'节首、Preface及第四章导航已更新','导读草案':'从甲基与表面相互作用引起的对称性降低出发，建立S及GF矩阵，求本征值与谱带变化，再通过L矩阵联系简正模式。','调查备注':'本轮原页实核：主题为CH₃的C₃ᵥ对称性破缺，3个PDF页的页脚为1、2、3；旧调查“页码非连续”备注已纠正。'})
with p.open('w',encoding='utf-8',newline='') as h:
 writer=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';old=p.read_text(encoding='utf-8');old=old[:old.index('## 后续')]+'''## 4.6 CH₃基团的C₃ᵥ对称性破缺时的处理

[进入4.6](4.6%20CH₃基团的C₃ᵥ对称性破缺时的处理.md)。全3页完成本轮译校。旧文件名保留，正文按原题恢复甲基对称性破缺主题。

p1说明模式混合并建立对称坐标与GF矩阵；p2求本征值、分裂、位移及Td近似；p3用L矩阵联系简正模式。先分清Ls与L、几何t与转置上标t，再读矩阵和近似解。

Q176—Q179保留待核，尤其注意原斜线分母范围、质量归一化及末两模式根号前缺斜线。旧译√2、根号范围与双层分式的转录错误已修复。

## 后续

下一批B365进入4.7，先核原题、结构与局部约定。
''';p.write_text(old,encoding='utf-8')
p=root/'Preface序言.md';old=p.read_text(encoding='utf-8')
old=re.sub(r'(?m)^- \[4\.6 .*$',lambda m:'- [4.6 CH₃基团的C₃ᵥ对称性破缺时的处理]('+m[0].split('](')[1].split(')')[0]+')（全节译校完成）：从表面相互作用引起的对称性降低与模式混合出发，建立对称坐标及GF矩阵，求谱带分裂和位移，再以L矩阵联系简正模式；原文疑点就地保留。',old)
p.write_text(old,encoding='utf-8')
for filename,txt in [('翻译管理/符号与约定.md','## 4.6局部约定（2026-10-21）\n\nS为对称坐标、R为内坐标、Q为简正坐标；Ls与S=LQ中的L分开，本节L不是菲涅尔因子。μc/μC、矩阵S/本征值s及原转置记法分别保留。Td角下s=√(2/3)、t=√(1/3)，原斜线分母范围及Q1/Q2归一化疑点未改，详见局部约定卡。'),('翻译管理/分批执行与质量控制.md','## 4.6全节完成（2026-10-21）\n\nB362—B364按原PDF三页完整矩阵及推导组处理。五个矩阵组和全部本征值、L及模式关系已覆盖；92个数学片段与合稿排版通过。原疑点Q176—Q179保留。下一批B365进入4.7。'),('中文版本/附件/原文勘误表.md','## 4.6本轮状态（2026-10-21）\n\n全3页完成译校。Q176—Q179原式或原陈述保留，候选未采用，暂无新增已采用的原文修正。末尾Q1/Q2中缺斜线的根式按原页保留；旧译直接补除号已撤回。矩阵√2、Td根号范围、L矩阵嵌套分式的修复均归译文校订。'),('翻译管理/全书调查/全书结构记录.md','## 4.6页码复核补记（2026-10-21）\n\n本轮已对照全3页原图，页脚实际为1、2、3，纠正旧调查所记“印刷页码非连续1—3”。以后以本条及4.6全节覆盖为准。主题为CH₃基团C₃ᵥ对称性破缺，旧文件名不作主题判断依据。')]:
 p=root/filename;old=p.read_text(encoding='utf-8')
 if txt.split('\n')[0] not in old:p.write_text(old+'\n\n'+txt+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

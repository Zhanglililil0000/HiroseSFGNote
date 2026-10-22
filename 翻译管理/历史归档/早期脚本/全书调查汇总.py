from pathlib import Path
import csv, json, re, math, hashlib, importlib.util, difflib
root=Path('HiroseSFGNote').resolve(); m=root/'翻译管理'; base=m/'全书调查'
spec=importlib.util.spec_from_file_location('config',m/'全书调查结构配置.py');cfg=importlib.util.module_from_spec(spec);spec.loader.exec_module(cfg)
D=json.loads((base/'提取数据.json').read_text(encoding='utf-8'))
C=list(csv.DictReader((m/'章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t')); CM={r['编号']:r for r in C}
blocks={d['id']:[] for d in D}
for line in cfg.STRUCTURE.strip().splitlines():
 sid,start,title=line.split('|',2);blocks[sid].append((int(start),title))
assert set(cfg.KINDS)==set(blocks)
def clean(t):
 t=re.sub(r'\(cid:\d+\)','',t);t=re.sub(r'[\ue000-\uf8ff\ufffd]','',t)
 return re.sub(r'\s','',t)
def put_tsv(name,rows):
 assert rows
 with (base/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
page_rows=[];section_rows=[];block_rows=[];plans=[];nplan=0
for d in D:
 sid=d['id'];pages=d['pages'];n=len(pages);kind=cfg.KINDS[sid]
 assert blocks[sid][0][0]==1
 for p in pages:
  text='\n'.join(l['text'] for l in p['lines']); p['clean_chars']=len(clean(text));p['pua_count']=len(re.findall(r'[\ue000-\uf8ff]',text))
  flag=[]
  if p['chars']<150:flag.append('低文本量；需看页面，不能直接判为空白')
  if p['cid_count']:flag.append('缺字CID占位')
  if p['pua_count']:flag.append('私用区字符')
  if sid=='5.4' and p['page']==15:flag=['视觉已核实：仅页脚空白尾页']
  if sid=='4.9' and p['page']==5:flag.insert(0,'视觉已核实：少量公式，非空白')
  lead=' | '.join(l['text'] for l in p['lines'][:3])[:280]
  page_rows.append({'节号':sid,'PDF页':p['page'],'原始非空白字符数':p['chars'],'清洗可提取字符数':p['clean_chars'],'汉字假名字符数':p['ja_chars'],'提取行数':p['line_count'],'含数学符号行数_代理指标':p['math_lines'],'栅格图对象数_非图数':p['images'],'CID占位数':p['cid_count'],'私用区字符数':p['pua_count'],'页面尺寸pt':f'{p["width"]}x{p["height"]}','页首提取片段':lead,'提取风险':';'.join(flag)})
 starts=blocks[sid];dense=('表' in kind or '清单' in kind or sid=='4.5');step=1 if dense else (3 if sid=='1.5' else 2)
 bmin=bmax=0
 for k,(start,title) in enumerate(starts):
  end=starts[k+1][0]-1 if k+1<len(starts) else n
  assert start<=end<=n
  ps=pages[start-1:end];empty=sid=='5.4' and start==15
  lo=0 if empty else math.ceil(len(ps)/(3 if sid=='1.5' else 2));hi=0 if empty else (math.ceil(len(ps)/2) if sid=='1.5' else len(ps))
  bmin+=lo;bmax+=hi
  bid=f'{sid}-U{k+1:02}'
  block_rows.append({'单元编号':bid,'节号':sid,'PDF起页':start,'PDF止页':end,'页数':len(ps),'结构概括_调查归纳':title,'清洗可提取字符数':sum(p['clean_chars'] for p in ps),'汉字假名字符数':sum(p['ja_chars'] for p in ps),'建议执行批数下限':lo,'建议执行批数上限':hi,'边界说明':'按页非重叠统计；同页小节合并，段落边界在执行时细化','内容性质':kind,'核验层级':'全页文本检索＋首尾及选定关键页视觉抽查；非逐页校订'})
  if empty:continue
  for a in range(start,end+1,step):
   z=min(a+step-1,end);nplan+=1
   plans.append({'预排编号':f'P{nplan:03}','节号':sid,'结构单元':bid,'PDF起页':a,'PDF止页':z,'内容':title,'清洗可提取字符数':sum(p['clean_chars'] for p in pages[a-1:z]),'处理方式':'书目条目核验' if sid=='1.5' else ('表格/长公式逐项复录核对' if dense else '翻译或旧译校订＋公式检查'),'边界状态':'页级预排；执行前确认首尾段落与推导，不保证在页末结束','执行状态':'尚未开始'})
 trans=CM[sid]['现有译文路径'];old=(root/trans).read_text(encoding='utf-8') if trans else ''
 section_rows.append({'节号':sid,'网页标题':d['web_title'],'PDF首页标题提取_上下标可能错序':pages[0]['lines'][0]['text'] if pages[0]['lines'] else '', '暂定中文标题':d['title_zh'],'PDF页数':n,'仅页脚空白页数':int(sid=='5.4'),'结构页组数':len(starts),'清洗可提取字符数':sum(p['clean_chars'] for p in pages),'原始非空白字符数':sum(p['chars'] for p in pages),'汉字假名字符数':sum(p['ja_chars'] for p in pages),'CID占位总数':sum(p['cid_count'] for p in pages),'私用区字符总数':sum(p['pua_count'] for p in pages),'含栅格图对象的页数':sum(bool(p['images']) for p in pages),'内容类型':kind,'相对工作难度':'中：书目核验' if sid=='1.5' else ('高：表格或公式校核为主' if dense else '中高：科学推导与文字对照'),'旧译Markdown非空白字符数_含公式标记':len(re.sub(r'\s','',old)),'旧译状态':'存在；完整性未核验' if trans else '无','建议批数下限':bmin,'建议批数上限':bmax,'当前保守预排批数':sum(p['节号']==sid for p in plans),'结构注意事项':cfg.NOTES.get(sid,'按实际 PDF 页面划分；符号与公式需页面核对。'),'原文路径':d['source'],'原文SHA256':d['sha256'],'原文视觉抽查页':','.join(map(str,sorted(set([1,n]+({'1.2':[8],'4.1':[30],'4.5':[22],'4.8':[30],'4.9':[5],'4.6':[2],'5.4':[2,15],'5.5':[8],'6.1':[31],'8.1':[9],'8.3':[8]}.get(sid,[]))))))})
put_tsv('逐页工作量.tsv',page_rows);put_tsv('逐节工作量.tsv',section_rows);put_tsv('内部结构与页组.tsv',block_rows);put_tsv('分批建议.tsv',plans)
chapter_rows=[]
chapter_names=['SFG 快速入门','薄膜产生的 SFG','双层及三层膜的和频','CH 伸缩振动与取向张量','张量与对称性','偶极–偶极相互作用','Heinz 论文解读','光谱线形与拟合']
for c in range(1,9):
 rs=[r for r in section_rows if r['节号'].split('.')[0]==str(c)]
 chapter_rows.append({'章':c,'调查主题':chapter_names[c-1],'PDF份数':len(rs),'PDF页数':sum(r['PDF页数'] for r in rs),'清洗可提取字符数':sum(r['清洗可提取字符数'] for r in rs),'汉字假名字符数':sum(r['汉字假名字符数'] for r in rs),'结构页组数':sum(r['结构页组数'] for r in rs),'旧译份数':sum(r['旧译状态'].startswith('存在') for r in rs),'建议批数下限':sum(r['建议批数下限'] for r in rs),'建议批数上限':sum(r['建议批数上限'] for r in rs),'当前保守预排批数':sum(r['当前保守预排批数'] for r in rs)})
put_tsv('分章工作量.tsv',chapter_rows)
# 只对有明显关系的指定材料做重复候选比对，不宣称全书排重完成。
lookup={d['id']:d for d in D}; dup=[]
for s1,s2,offset in [('2.2','2.3',34),('4.1','4.6',29)]:
 for p2 in lookup[s2]['pages']:
  b=clean('\n'.join(l['text'] for l in p2['lines']))
  candidates=lookup[s1]['pages'][offset:]
  scored=[(difflib.SequenceMatcher(None,clean('\n'.join(l['text'] for l in p['lines'])),b,autojunk=False).ratio(),p) for p in candidates]
  score,p1=max(scored,key=lambda x:x[0])
  dup.append({'材料A':s1,'PDF页A':p1['page'],'材料B':s2,'PDF页B':p2['page'],'提取字符串相似度':round(score,4),'结论':'内容重叠候选；公式与页内位置仍需视觉对照，不能直接合并'})
put_tsv('重复内容候选.tsv',dup)
# 逐节结构说明，提供每个部分的大致文本量；所有页组无重叠可相加。
visual_count=sum(len(r['原文视觉抽查页'].split(',')) for r in section_rows)
lines=['# 全书结构记录','', f'日期：2026-10-16。覆盖 39 份 PDF 的 717 页文本层；已视觉抽查全部材料首页、末页及选定关键位置，共 {visual_count} 个不同页面。不是 717 页逐页视觉审校。', '', '各部分为调查归纳标题，未替代原文标题；原始页面文字可查文本缓存。页组使用非重叠 PDF 页范围，便于加总；同页开始的小节可能合并，跨页段落需在执行时细化。公式、表格、英文、页眉页脚均可能计入可提取字符，不能将其当作日语正文净字数。','']
for r in section_rows:
 sid=r['节号'];lines += [f'## {sid} {r["暂定中文标题"]}', '',f'- 原文：[{Path(r["原文路径"]).name}](../../{r["原文路径"]})；PDF {r["PDF页数"]} 页；清洗可提取字符 {r["清洗可提取字符数"]:,}，汉字假名 {r["汉字假名字符数"]:,}。',f'- 类型：{r["内容类型"]}；旧译：{r["旧译状态"]}。',f'- 注意：{r["结构注意事项"]}',f'- 视觉抽查：PDF p{r["原文视觉抽查页"]}；余页为提取文本结构调查。','', '| PDF 页组 | 结构归纳 | 可提取字符 | 建议批数 |','|---|---|---:|---:|']
 for b in block_rows:
  if b['节号']==sid:lines.append(f'| {b["PDF起页"]}–{b["PDF止页"]} | {b["结构概括_调查归纳"]} | {b["清洗可提取字符数"]:,} | {b["建议执行批数下限"]}–{b["建议执行批数上限"]} |')
 lines+=['']
(base/'全书结构记录.md').write_text('\n'.join(lines),encoding='utf-8')
# 保留章节清单既有状态，只附加本轮调查字段。
for r in C:
 s=next(s for s in section_rows if s['节号']==r['编号'])
 r['结构调查状态']='已完成文本层全量调查与首尾/关键页视觉抽查；非逐页校订'
 r['清洗可提取字符数']=s['清洗可提取字符数'];r['汉字假名字符数']=s['汉字假名字符数'];r['结构记录']='全书调查/全书结构记录.md';r['调查备注']=s['结构注意事项']
 r['映射核验']='PDF 首页主题与编号已核对；旧译正文逐段对应仍待核验'
with (m/'章节清单.tsv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(C[0]),delimiter='\t');w.writeheader();w.writerows(C)
# 摘要数据供报告与验收复用。
summary={'files':len(D),'pages':len(page_rows),'clean_chars':sum(r['清洗可提取字符数'] for r in section_rows),'cjk_chars':sum(r['汉字假名字符数'] for r in section_rows),'blocks':len(block_rows),'plans':len(plans),'min_batches':sum(r['建议批数下限'] for r in section_rows),'max_batches':sum(r['建议批数上限'] for r in section_rows),'cid_pages':sum(bool(r['CID占位数']) for r in page_rows),'pua_pages':sum(bool(r['私用区字符数']) for r in page_rows),'image_pages':sum(bool(r['栅格图对象数_非图数']) for r in page_rows),'low_pages':[(r['节号'],r['PDF页']) for r in page_rows if r['原始非空白字符数']<150]}
(base/'调查摘要数据.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False));print(json.dumps(chapter_rows,ensure_ascii=False,indent=2))

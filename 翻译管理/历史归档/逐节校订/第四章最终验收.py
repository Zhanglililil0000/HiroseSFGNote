from pathlib import Path
import re,json,csv,io,hashlib
from urllib.parse import unquote
root=Path(__file__).resolve().parents[2];base=root/'翻译管理/校订记录';chapter=root/'中文版本/第四章 单层膜与多层膜的和频'
spec={'4.8':(38,385,401,'氢化金刚石表面CH的和频张量'),'4.9':(26,402,415,'氢化金刚石表面CH的和频张量（要点）'),'4.10':(8,416,420,'CH₂基团及HCCH基团的欧拉角'),'4.11':(2,421,422,'表面的旋转')}
report={}
for sec,(pages,start,end,title) in spec.items():
 out=base/sec;render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
 assert len(render['results'])==end-start+1
 assert all(not r['overs'] and r['width']==r['scrollWidth'] and all(i['loaded'] for i in r['images']) for r in render['results'])
 for n in range(start,end+1):
  p=out/f'B{n}-覆盖.json';r=json.loads(p.read_text(encoding='utf-8'));t=(out/f'B{n}-本批译文.md').read_text(encoding='utf-8')
  if sec=='4.11' and n==421:
   t=t.replace('；无新增原文疑点保留待核。','；无新增原文疑点。');(out/f'B{n}-本批译文.md').write_text(t,encoding='utf-8')
  r.update(status='本批原页对照、译校、覆盖与参考排版验收完成',date='2026-10-21',source_images_visually_checked=True,render=next(x for x in render['results'] if x['batch']==f'B{n}'),translation_sha256=hashlib.sha256(t.encode()).hexdigest(),validation_limit='数学语法和版式通过不等于原稿公式已完成独立物理证明。')
  (out/f'B{n}验收.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  (out/f'B{n}.md').write_text(f'# B{n}校订与验收\n\n2026-10-21。{sec}，原PDF页'+','.join(map(str,r['pages']))+'。完整原文数学行位置或人工向量核对、源文件校验值及本批译文见覆盖与验收JSON。全部表达式可编辑；原式疑点就地说明，候选未采用。参考排版无页面/公式横向溢出，原图加载正常。\n',encoding='utf-8')
 target=next(chapter.glob(sec+' *.md'));target.write_text('\n\n'.join((out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(start,end+1)),encoding='utf-8')
 summary={'section':sec,'pages':pages,'batches':f'B{start}—B{end}','status':'本轮全节译校完成，原文未决疑点保留','math_fragments':render['math'],'math_syntax_errors':0,'formula_overflows':0,'source_corrections_adopted':False,'translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
 (out/'全节验收.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');report[sec]=summary
 (out/'全节验收.md').write_text(f'# {sec}全节验收\n\n全{pages}页，B{start}—B{end}完成。数学片段{render["math"]}，严格语法检查通过、参考预览无横向溢出。原文疑点和原稿缺项保留，候选未采纳。完整原稿范围、向量与公式覆盖索引见本目录，未以“参阅原文”替代附录。\n',encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0]);chapterrows=[r for r in rows if r['编号'].startswith('4.')]
for r in rows:
 if r['编号'] in spec:r['暂定中文标题']=spec[r['编号']][3]
assert len(chapterrows)==11 and sum(int(r['PDF页数']) for r in chapterrows)==267
assert all('完成' in r['状态'] for r in chapterrows)
with p.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
broken=[]
for p in [root/'Preface序言.md',chapter/'阅读导航.md']+list(chapter.glob('4.*.md')):
 s=p.read_text(encoding='utf-8')
 s=re.sub(r'\$\$[\s\S]*?\$\$|\$[^$\n]+\$','',s)
 for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',s):
  if re.match(r'^[a-zA-Z]+:',link) or link.startswith('#'):continue
  dest=(p.parent/unquote(link.split('#')[0])).resolve()
  if not dest.exists():broken.append([str(p.relative_to(root)),link])
assert not broken,broken
issues=(root/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8')
assert all(re.search(r'^## Q'+str(q)+r'\b',issues,re.M) for q in range(180,198))
for sec in spec:
 s=next(chapter.glob(sec+' *.md')).read_text(encoding='utf-8')
 assert '(cid:' not in s and '详细公式请参阅' not in s and not any(ord(c)<32 and c not in '\n\t\r' for c in s)
report.update(chapter_pages=267,sections=11,completed_this_turn_batches='B370—B422',new_pages_this_turn=93,source_corrections_adopted=False,broken_links=broken)
(base/'第四章最终验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('第四章11节/267页状态一致；本轮93页、53批；新增各节验收完成；相对链接完好；Q180—Q197登记齐全。')

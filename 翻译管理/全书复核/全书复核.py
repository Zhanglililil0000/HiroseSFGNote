"""B665: repeatable structural audit and review-manuscript assembly (no physics edits)."""
from pathlib import Path
import csv, re, json, hashlib, urllib.parse, os, sys, runpy
R=Path(__file__).resolve().parents[2]
BATCH=sys.argv[1] if len(sys.argv)>1 else (json.loads((R/'合稿准备/合稿清单.json').read_text(encoding='utf-8')).get('batch','B678') if (R/'合稿准备/合稿清单.json').exists() else 'B678')
OUT=R/'翻译管理/全书复核'; MERGE=R/'合稿准备'
OUT.mkdir(exist_ok=True); MERGE.mkdir(exist_ok=True)
rows=list(csv.DictReader((R/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):
 if isinstance(x,dict) and 'batch' in x:x['batch']=BATCH
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
mathpat=re.compile(r'\$\$([\s\S]*?)\$\$|(?<![\\$])\$(?!\$)((?:\\.|[^$\n])+)\$')
def mask(s):
 s=re.sub(r'```[\s\S]*?```|<!--[\s\S]*?-->',lambda m:re.sub(r'[^\n]',' ',m[0]),s)
 return mathpat.sub(lambda m:re.sub(r'[^\n]',' ',m[0]),s)
docs=[R/r['现有译文路径'] for r in rows]
extras=[R/'Preface序言.md',R/'README.md',R/'中文版本/附件/原文勘误表.md',*sorted((R/'中文版本').glob('*/阅读导航.md'))]
manifest=[]; maths=[]; links=[]; variants=[]; question_refs=set(); terms={}
patterns=['菲涅耳','菲涅尔系数','和频发生','和频产生','二阶极化率','二阶超极化率','一阶超极化率','半高全宽']
for p in docs+extras:
 s=p.read_text(encoding='utf-8-sig'); rel=p.relative_to(R).as_posix()
 for m in mathpat.finditer(re.sub(r'```[\s\S]*?```','',s)):
  maths.append({'file':rel,'line':s[:m.start()].count('\n')+1,'tex':m[1] if m[1] is not None else m[2],'display':m[1] is not None})
 for m in re.finditer(r'!?\[([^\]\n]*)\]\(([^\n]*?)\)',mask(s)):
  href=m[2].strip().split(' "')[0].strip('<>'); u=urllib.parse.urlsplit(href)
  if u.scheme or href.startswith('#'): continue
  target=(p.parent/urllib.parse.unquote(u.path)).resolve()
  links.append({'file':rel,'line':s[:m.start()].count('\n')+1,'href':href,'exists':target.exists(),'image':m[0].startswith('!')})
 for n,line in enumerate(s.splitlines(),1):
  for term in patterns:
   if term in line: variants.append({'file':rel,'line':n,'term':term,'text':line})
 if p in docs: question_refs.update(re.findall(r'Q\d{3}',s))
for r,p in zip(rows,docs):
 src=R/r['原文路径']; s=p.read_text(encoding='utf-8-sig')
 manifest.append({'section':r['编号'],'title':p.stem,'path':r['现有译文路径'],'sha256':sha(p),'source':r['原文路径'],'source_sha256':sha(src),'source_unchanged':sha(src)==r['原文SHA256'],'pages':int(r['PDF页数']),'chars':len(s),'anchor':'sec-'+r['编号'].replace('.','-'),'status':r['状态']})
qtext=(R/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8-sig')
qids=set(re.findall(r'Q\d{3}',qtext))-{'Q108','Q109'}; qlines=[x for x in qtext.splitlines() if re.match(r'\| Q\d{3}',x)]
save(OUT/'数学片段.json',maths); save(OUT/'术语用法候选.json',variants)
save(OUT/'全书验收.json',{'batch':'B665','sections':len(rows),'pages':sum(x['pages'] for x in manifest),'math_fragments':len(maths),'local_links':len(links),'image_references':sum(x['image'] for x in links),'broken_links':[x for x in links if not x['exists']],'source_hash_mismatches':[x['section'] for x in manifest if not x['source_unchanged']],'body_questions_not_registered':sorted(question_refs-qids),'registered_question_ids':len(qids),'scope':'结构、资源、已约定术语的候选检索；非717页再次逐页对照或独立推导认证'})
save(OUT/'链接与图像清单.json',links)
save(MERGE/'合稿清单.json',{'batch':'B665','order':['Preface序言.md',*[x['path'] for x in manifest],'中文版本/附件/原文勘误表.md'],'sections':manifest,'equation_policy':'保留各节原编号；以节号+原式号引用，不全局重编号','status':'审阅稿，原文疑点及暂译未解除'})
(OUT/'问题状态汇总.md').write_text('# 全书问题状态汇总（B665）\n\n从问题总表抽取的原始状态，不因翻译完成自动关闭。部分问题有后续补充，应结合总表上下文和正文注释判断。\n\n| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |\n|---|---|---|---|---|\n'+'\n'.join(qlines)+'\n',encoding='utf-8')
def rewrite(s,p):
 # Only rewrite Markdown links outside math/code; preserve all source prose and TeX.
 masked=mask(s); matches=list(re.finditer(r'!?\[([^\]\n]*)\]\(([^\n]*?)\)',masked))
 for m in reversed(matches):
  raw=s[m.start():m.end()]; href=m[2].strip(); u=urllib.parse.urlsplit(href)
  if u.scheme or href.startswith('#'): continue
  dest=(p.parent/urllib.parse.unquote(u.path)).resolve()
  new=urllib.parse.quote(os.path.relpath(dest,MERGE).replace('\\','/'),safe='/.-_')
  if u.fragment:new+='#'+u.fragment
  s=s[:m.start()]+raw.replace(href,new)+s[m.end():]
 return s
parts=['# Hirose SFG 中文译本·审阅合稿\n\n> B665，2026-10-22。保留各节原公式编号、原文疑点、暂译和图片公式；本稿用于审阅，尚非最终定稿。引用公式请同时写节号。\n\n## 合稿目录\n']
parts += [f"- [{x['title']}](#{x['anchor']})" for x in manifest]
parts+=['- [附件：原文勘误表](#errata)\n','<a id="preface"></a>\n\n'+rewrite((R/'Preface序言.md').read_text(encoding='utf-8-sig'),R/'Preface序言.md')]
for x,p in zip(manifest,docs):
 parts.append(f'\n\n---\n\n<a id="{x["anchor"]}"></a>\n\n'+rewrite(p.read_text(encoding='utf-8-sig'),p))
p=R/'中文版本/附件/原文勘误表.md'
parts.append('\n\n---\n\n<a id="errata"></a>\n\n'+rewrite(p.read_text(encoding='utf-8-sig'),p))
(MERGE/'全书审阅稿.md').write_text('\n'.join(parts),encoding='utf-8')
for p in [MERGE/'全书审阅稿.md',OUT/'问题状态汇总.md']:
 p.write_text(p.read_text(encoding='utf-8').replace('B665',BATCH),encoding='utf-8')
print(json.dumps({'sections':len(manifest),'pages':sum(x['pages'] for x in manifest),'math':len(maths),'broken':sum(not x['exists'] for x in links),'variant_hits':len(variants),'question_ids':len(qids)},ensure_ascii=False))
# B676: never leave the former table-only, incomplete question index as current.
if (OUT/'问题现状生成.py').exists():runpy.run_path(str(OUT/'问题现状生成.py'),run_name='__main__')

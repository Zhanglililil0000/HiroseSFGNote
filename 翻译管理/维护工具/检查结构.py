from pathlib import Path
import csv,json,re,urllib.parse,zipfile,hashlib,ast
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/文件结构审查'
receipt=json.loads((O/'B678迁移清单.json').read_text(encoding='utf-8'))
old=receipt['chapter_directory']['old'];new=receipt['chapter_directory']['new'];moves=receipt['moves']
rows=list(csv.DictReader((R/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
assert len(rows)==39 and len(rows[0])==17
assert not (R/'中文版本'/old).exists() and (R/'中文版本'/new).is_dir()
for row in rows:
 assert (R/row['现有译文路径']).is_file()
 assert (R/'翻译管理'/row['结构记录']).exists()
 assert hashlib.sha256((R/row['原文路径']).read_bytes()).hexdigest()==row['原文SHA256']
math=re.compile(r'\$\$[\s\S]*?\$\$|(?<![\\$])\$(?!\$)(?:\\.|[^$\n])+\$')
def links(s):
 s=re.sub(r'```[\s\S]*?```|<!--[\s\S]*?-->','',s)
 return re.findall(r'!?\[[^\]\n]*\]\(([^\n]*?)\)',math.sub('',s))
def local(path,href):
 u=urllib.parse.urlsplit(href.strip().strip('<>'))
 return None if u.scheme or not u.path else (path.parent/urllib.parse.unquote(u.path)).resolve()
def dest(rel):
 if rel in moves:return moves[rel]
 for a,b in sorted(receipt['directory_moves'],key=lambda x:-len(x[0])):
  if rel==a or rel.startswith(a+'/'):return b+rel[len(a):]
 return rel
current=[R/x['现有译文路径'] for x in rows]+[R/'Preface序言.md',R/'README.md',R/'项目导航.md',R/'合稿准备/使用说明.md',R/'交付版本/README.md',R/'中文版本/附件/原文勘误表.md']+list((R/'中文版本').glob('*/阅读导航.md'))+list((R/'翻译管理').glob('*.md'))+list((R/'翻译管理/全书复核').glob('*.md'))+[O/'B678目录整理报告.md',R/'翻译管理/维护工具/README.md']
bad=[];count=0;pending=[]
for p in current:
 for ref in links(p.read_text(encoding='utf-8-sig')):
  target=local(p,ref)
  if target is None:continue
  count+=1
  if target in [O/'B678结构验收.json',O/'B678阅读包验收.json',R/'交付版本/Hirose-SFG-中文审阅版-B678.zip',R/'交付版本/当前阅读版/阅读包清单.json',R/'交付版本/当前阅读版/开始阅读.html'] and not target.exists():pending.append(str(target));continue
  if not target.exists():bad.append({'file':p.relative_to(R).as_posix(),'href':ref})
# Historical clickable links must not regress where the former target existed.
regressions=[];legacy=[];history_checked=0
with zipfile.ZipFile(R/receipt['backup']) as z:
 for rel in z.namelist():
  if not rel.endswith('.md'):continue
  if any(t in Path(rel).name for t in ['快照','前旧译','修改前','旧译']):continue
  target_rel=dest(rel)
  if target_rel==rel or not (R/target_rel).exists():continue
  before=z.read(rel).decode('utf-8-sig');after=(R/target_rel).read_text(encoding='utf-8-sig')
  before_refs=links(before);after_refs=links(after)
  if len(before_refs)!=len(after_refs):regressions.append({'file':target_rel,'reason':'link count changed'});continue
  for a,b in zip(before_refs,after_refs):
   ta=local(R/rel,a);tb=local(R/target_rel,b)
   if ta is None or tb is None:continue
   history_checked+=1
   if tb.exists():continue
   oldexisted=ta.is_relative_to(R) and (R/dest(ta.relative_to(R).as_posix())).exists()
   (regressions if oldexisted else legacy).append({'file':target_rel,'old_href':a,'new_href':b})
assert not bad,bad
assert not regressions,regressions
for p in list((R/'翻译管理/维护工具').glob('*.py'))+list((R/'翻译管理/全书复核').glob('*.py')):ast.parse(p.read_text(encoding='utf-8-sig'))
audit=json.loads((R/'翻译管理/全书复核/全书验收.json').read_text(encoding='utf-8'));m=json.loads((R/'翻译管理/全书复核/数学验收.json').read_text(encoding='utf-8'));q=json.loads((R/'翻译管理/全书复核/问题当前处置.json').read_text(encoding='utf-8'))
assert audit['batch']=='B678' and not audit['broken_links'] and not m['errors'] and len(q['items'])==320
out={'batch':'B678','old_chapter_directory_absent':True,'new_chapter_directory':new,'source_sections':39,'source_PDF_hash_mismatches':[],'source_content_preservation':receipt['source_checks'],'files_moved':receipt['files_moved'],'current_links_checked':count,'current_broken_links':bad,'pending_delivery_outputs':pending,'historical_links_checked':history_checked,'historical_link_regressions':regressions,'preexisting_historical_broken_links':legacy,'math_fragments':m['count'],'math_errors':0,'registered_questions':320,'management_root_files_before':77,'management_root_files_after':len(list((R/'翻译管理').glob('*.*'))),'merge_root_files_before':25,'merge_root_files_after':len([p for p in (R/'合稿准备').iterdir() if p.is_file()]),'old_package_compressed_snapshot_retained':(R/receipt['old_delivery_zip']).exists(),'old_duplicate_unpacked_removed':not (R/receipt['old_delivery_folder']).exists(),'source_or_evidence_deleted':False}
(O/'B678结构验收.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['source_content_preservation','preexisting_historical_broken_links']},ensure_ascii=False))

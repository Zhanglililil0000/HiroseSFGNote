"""B678: reversible migration, immutable evidence, link-aware maintenance."""
from pathlib import Path
import csv,re,json,hashlib,urllib.parse,os,zipfile
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/文件结构审查';O.mkdir(exist_ok=True)
old='第四章 单层膜与多层膜的和频';new='第四章 CH伸缩振动与取向张量'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def safe(p):
 p=p.resolve();assert p.is_relative_to(R) and p!=R;return p
def write(rel,s):
 p=safe(R/rel);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
assert (R/'中文版本'/old).is_dir() and not (R/'中文版本'/new).exists(),'Migration is one-shot; use receipt to inspect current state'
rows=list(csv.DictReader((R/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
source_before={x['编号']:{'path':x['现有译文路径'],'bytes':(R/x['现有译文路径']).read_text(encoding='utf-8-sig'),'pdf':x['原文路径'],'pdf_sha256':sha(R/x['原文路径'])} for x in rows}
plans=[]
def move(a,b):
 a=safe(R/a);b=safe(R/b)
 if a.exists():assert not b.exists(),str(b);plans.append((a,b))
move('中文版本/'+old,'中文版本/'+new)
for name,target in [('校订记录','逐节校订'),('基线快照','基线快照'),('全书调查','全书调查'),('术语修订记录','术语修订记录'),('来源记录','来源记录'),('__pycache__','脚本缓存')]:move('翻译管理/'+name,'翻译管理/历史归档/'+target)
for p in list((R/'翻译管理').iterdir()):
 if not p.is_file():continue
 if p.suffix=='.py':move(p.relative_to(R),'翻译管理/历史归档/早期脚本/'+p.name)
 elif p.name.startswith(('第一章','第四章','第五章','第八章','文件命名','基线快照清单','准备验收记录')):move(p.relative_to(R),'翻译管理/历史归档/阶段报告/'+p.name)
F=R/'翻译管理/全书复核'
for p in list(F.iterdir()):
 m=re.match(r'B(\d{3})',p.name)
 if m and (int(m[1])<=675 or p.suffix in ['.py','.cjs']):move(p.relative_to(R),'翻译管理/全书复核/历史批次/B'+m[1]+'/'+p.name)
 elif p.name.startswith(('盘点阅读','全量问题盘点','初查_')):move(p.relative_to(R),'翻译管理/全书复核/历史批次/盘点中间产物/'+p.name)
 elif p.name.endswith('-首屏.png') or p.name in ['全书首屏总览.png','浏览验收.json']:move(p.relative_to(R),'翻译管理/全书复核/验收快照/'+p.name)
for p in (R/'合稿准备').glob('B*阅读提示.html'):move(p.relative_to(R),'翻译管理/历史归档/验收页面/'+p.name)
for p in list(O.iterdir()):move(p.relative_to(R),'翻译管理/历史归档/结构整理/B677/'+p.name)
move('EnglishVersion','翻译管理/历史归档/未使用目录/EnglishVersion')
move('交付版本/Hirose-SFG-中文审阅版-B676.zip','交付版本/历史版本/Hirose-SFG-中文审阅版-B676.zip')
filemap={};beforehash={};original={}
for a,b in plans:
 for p in ([a] if a.is_file() else [x for x in a.rglob('*') if x.is_file()]):
  dest=b if a.is_file() else b/p.relative_to(a)
  key=p.relative_to(R).as_posix();filemap[key]=dest.relative_to(R).as_posix();beforehash[key]=sha(p)
roots=[(a.relative_to(R).as_posix(),b.relative_to(R).as_posix()) for a,b in plans]
def mapped(rel):
 rel=rel.replace('\\','/')
 if rel in filemap:return filemap[rel]
 for a,b in sorted(roots,key=lambda x:-len(x[0])):
  if rel==a or rel.startswith(a+'/'):return b+rel[len(a):]
 return rel
def frozen(rel):
 return '基线快照/' in rel or any(x.endswith('修改前') for x in Path(rel).parts) or rel.startswith('日语原版/')
def archived(rel):return rel.startswith('翻译管理/历史归档/') or '/全书复核/历史批次/' in rel
allfiles=[p for p in R.rglob('*') if p.is_file() and not any(x in p.relative_to(R).parts for x in ['.git','交付版本'])]
# Preserve every file which will be edited, then perform only validated moves.
texts={}
for p in allfiles:
 rel=p.relative_to(R).as_posix();dest=mapped(rel)
 if frozen(dest) or p.suffix not in ['.md','.html','.json','.tsv','.py','.cjs','.css','.txt']:continue
 if rel.startswith('合稿准备/') and p.suffix=='.html' and rel==dest:continue
 if archived(dest) and p.suffix in ['.json','.tsv','.py','.cjs','.txt']:continue
 try:texts[rel]=p.read_text(encoding='utf-8-sig')
 except UnicodeError:pass
backup=R/'翻译管理/历史归档/迁移前/B678文档原稿.zip';backup.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(backup,'w',zipfile.ZIP_DEFLATED) as z:
 for rel in texts:z.write(R/rel,rel)
for a,b in plans:b.parent.mkdir(parents=True,exist_ok=True);a.rename(b)
math=re.compile(r'\$\$[\s\S]*?\$\$|(?<![\\$])\$(?!\$)(?:\\.|[^$\n])+\$')
changed=[]
def relocate(href,src,dst):
 u=urllib.parse.urlsplit(href.strip('<>'))
 if u.scheme or not u.path:return href
 target=(R/src).parent/urllib.parse.unquote(u.path);target=target.resolve()
 if not target.is_relative_to(R):return href
 out=R/mapped(target.relative_to(R).as_posix())
 # Preserve unchanged links byte for byte.
 if src==dst and out==target:return href
 newhref=urllib.parse.quote(os.path.relpath(out,(R/dst).parent).replace('\\','/'),safe='/.-_')
 if u.query:newhref+='?'+u.query
 if u.fragment:newhref+='#'+u.fragment
 return newhref
for rel,s in texts.items():
 dest=mapped(rel);p=R/dest;t=s
 if p.suffix=='.md':
  masked=math.sub(lambda m:' '*len(m[0]),re.sub(r'```[\s\S]*?```|<!--[\s\S]*?-->',lambda m:' '*len(m[0]),s))
  for m in reversed(list(re.finditer(r'!?\[[^\]\n]*\]\(([^\n]*?)\)',masked))):
   start,end=m.span(1);t=t[:start]+relocate(s[start:end],rel,dest)+t[end:]
 elif p.suffix=='.html':t=re.sub(r'((?:href|src)=")([^"]+)(")',lambda m:m[1]+relocate(m[2],rel,dest)+m[3],s)
 # Current code/metadata use root-relative paths; archive raw evidence stays untouched.
 if not archived(dest):
  t=t.replace(old,new).replace(urllib.parse.quote(old),urllib.parse.quote(new))
  for a,b in sorted(roots,key=lambda x:-len(x[0])):
   if a.startswith('中文版本/'):continue
   t=t.replace(a,b)
   t=t.replace(urllib.parse.quote(a,safe='/.-_'),urllib.parse.quote(b,safe='/.-_'))
 if t!=s:p.write_text(t,encoding='utf-8');changed.append({'old':rel,'new':dest,'before_sha256':hashlib.sha256(s.encode('utf-8')).hexdigest(),'after_sha256':sha(p)})
# Every moved file, and all frozen evidence, is traceable.
frozen_checks=[]
for rel,dest in filemap.items():
 if frozen(dest) or (archived(dest) and Path(dest).suffix in ['.json','.py','.cjs','.txt','.tsv']):
  assert sha(R/dest)==beforehash[rel],dest;frozen_checks.append(dest)
checks=[]
for id,v in source_before.items():
 p=R/mapped(v['path']);s=p.read_text(encoding='utf-8-sig')
 # Body content may change only in Markdown link targets; all math is identical.
 strip=lambda s:re.sub(r'(!?\[[^\]\n]*\]\()[^\n]*?(\))',r'\1LINK\2',s)
 assert math.findall(v['bytes'])==math.findall(s),id
 assert strip(v['bytes'])==strip(s),id
 assert sha(R/v['pdf'])==v['pdf_sha256']
 checks.append({'section':id,'path':mapped(v['path']),'math_unchanged':True,'body_except_links_unchanged':True,'PDF_unchanged':True})
# Only a byte-exact recoverable old unpacked delivery may be removed later.
oldpack=R/'交付版本/中文审阅版-B676';oldzip=R/'交付版本/历史版本/Hirose-SFG-中文审阅版-B676.zip';reclaim=False
if oldpack.exists():
 with zipfile.ZipFile(oldzip) as z:
  disk={p.relative_to(oldpack.parent).as_posix():p for p in oldpack.rglob('*') if p.is_file()}
  assert set(disk)=={n for n in z.namelist() if not n.endswith('/')}
  for n,p in disk.items():assert hashlib.sha256(z.read(n)).hexdigest()==sha(p),n
  assert z.testzip() is None
  reclaim=True
receipt={'batch':'B678','chapter_directory':{'old':old,'new':new},'moves':filemap,'directory_moves':roots,'files_moved':len(filemap),'edited_text_files':changed,'frozen_evidence_byte_identical':len(frozen_checks),'source_checks':checks,'backup':backup.relative_to(R).as_posix(),'old_unpacked_delivery_verified_recoverable':reclaim,'old_delivery_zip':oldzip.relative_to(R).as_posix(),'old_delivery_folder':oldpack.relative_to(R).as_posix()}
(O/'B678迁移清单.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files_moved':len(filemap),'text_files_updated':len(changed),'frozen_evidence_identical':len(frozen_checks),'source_sections_verified':len(checks),'old_package_recoverable':reclaim},ensure_ascii=False))

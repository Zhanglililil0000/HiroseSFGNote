"""Generate a self-contained reading snapshot; never modify source files."""
from pathlib import Path
import csv,json,re,urllib.parse,zipfile,hashlib
from html.parser import HTMLParser
from collections import deque
import argparse
args=argparse.ArgumentParser();args.add_argument('--batch',default='B678');batch=args.parse_args().batch
assert re.fullmatch(r'B\d{3}',batch)
R=Path(__file__).resolve().parents[2];D=R/'交付版本/当前阅读版';O=R/'翻译管理/文件结构审查'
previous_manifest=D/'阅读包清单.json'
previous_files={}
if previous_manifest.exists():
 previous_files={x['path']:x for x in json.loads(previous_manifest.read_text(encoding='utf-8'))['files']}
 actual_previous={p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file()}
 assert actual_previous==set(previous_files)|{'阅读包清单.json'},'阅读目录含未登记文件，请先另存。'
 for rel,item in previous_files.items():
  assert hashlib.sha256((D/rel).read_bytes()).hexdigest()==item['sha256'],'阅读副本已被修改，请先另存：'+rel
rows=list(csv.DictReader((R/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
assert json.loads((R/'合稿准备/合稿清单.json').read_text(encoding='utf-8'))['batch']==batch,'请先按同一批号重建合稿，再打包。'
def sha(data):return hashlib.sha256(data).hexdigest()
overrides={
'README.md':f'''# Hirose SFG 中文审阅版 {batch}

打开[开始阅读.html](开始阅读.html)或[全书目录](合稿准备/index.html)。请整体保留目录；图片及WOFF2字体可离线读取，外部文献仍需联网。正文理论核查基线B676，目录及交付版本{batch}；原文疑点、暂译及作者未完成的内容保留。

本包是生成快照。请返回工作项目的“中文版本”修改39节稿源，再重建合稿和阅读包，不在副本上开展平行修订。版权信息及LICENSE保留。本包不含全部底本、历史快照或维护运行环境，JSON中的追溯路径可回工作项目查询。
''',
'开始阅读.html':f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>Hirose SFG 中文审阅版 {batch}</title><style>body{{max-width:850px;margin:60px auto;padding:20px;font:20px/1.9 sans-serif}}</style><h1>Hirose SFG 中文审阅版 {batch}</h1><p><a href="合稿准备/index.html">打开全书目录</a></p><p><a href="Preface序言.md">序言与逐节导读</a> · <a href="README.md">使用说明</a></p><p>原文疑点和暂译保留。</p></html>'}
overrides['合稿准备/使用说明.md']=f'''# 阅读说明

打开[index.html](index.html)阅读；也可使用[单文件Markdown](全书审阅稿.md)。请整体保留本包目录。当前阅读版{batch}，理论核查基线B676；原文疑点及暂译保留。详见[包内说明](../README.md)。
'''
cssrel='翻译管理/排版工具/katex.min.css';css=(R/cssrel).read_text(encoding='utf-8')
overrides[cssrel]=re.sub(r',url\(fonts/[^)]+\.(?:woff|ttf)\) format\("(?:woff|truetype)"\)','',css)
class HTML(HTMLParser):
 def __init__(self):super().__init__();self.refs=[]
 def handle_starttag(self,tag,attrs):self.refs.extend(v for k,v in attrs if k in ['href','src'] and v)
math=re.compile(r'\$\$[\s\S]*?\$\$|(?<![\\$])\$(?!\$)(?:\\.|[^$\n])+\$')
def refs(p,s):
 if p.suffix=='.html':h=HTML();h.feed(s);return h.refs
 if p.suffix=='.md':return re.findall(r'!?\[[^\]\n]*\]\(([^\n]*?)\)',math.sub('',re.sub(r'```[\s\S]*?```','',s)))
 if p.suffix=='.css':return re.findall(r'url\([\'"]?([^\)\'"\s]+)',s)
 return []
roots=['开始阅读.html','README.md','LICENSE','Preface序言.md','合稿准备/index.html','合稿准备/序言.html','合稿准备/附件.html','合稿准备/使用说明.md','合稿准备/全书审阅稿.md','合稿准备/合稿清单.json','翻译管理/术语表.tsv','翻译管理/章节清单.tsv',*[f'合稿准备/第{i}章.html' for i in range(1,9)],*[x['现有译文路径'] for x in rows]]
queue=deque(roots);seen=set();files=[];edges=[]
while queue:
 rel=queue.popleft()
 if rel in seen:continue
 seen.add(rel);p=R/rel
 if p.is_dir():queue.extend(x.relative_to(R).as_posix() for x in p.rglob('*') if x.is_file());continue
 assert rel in overrides or p.is_file(),rel
 data=overrides[rel].encode('utf-8') if rel in overrides else p.read_bytes()
 out=D/rel;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
 files.append({'path':rel,'bytes':len(data),'sha256':sha(data),'package_override':rel in overrides})
 if p.suffix not in ['.md','.html','.css']:continue
 for href in refs(p,data.decode('utf-8-sig')):
  u=urllib.parse.urlsplit(href.strip().strip('<>'))
  if u.scheme or not u.path:continue
  dest=(p.parent/urllib.parse.unquote(u.path)).resolve();assert dest.is_relative_to(R),href
  dep=dest.relative_to(R).as_posix();assert not dep.startswith(('交付版本/','.git/')),dep
  edges.append({'from':rel,'to':dep});queue.append(dep)
assert len(files)<1000,'Unexpected dependency expansion'
assert all((D/x['to']).exists() for x in edges)
for row in rows:assert (D/row['现有译文路径']).read_bytes()==(R/row['现有译文路径']).read_bytes()
actual={p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file()}
stale=actual-({x['path'] for x in files}|{'阅读包清单.json'})
for rel in stale:
 assert rel in previous_files,'未登记旧文件：'+rel
 target=(D/rel).resolve();assert target.is_relative_to(D.resolve()) and target.is_file()
 assert sha(target.read_bytes())==previous_files[rel]['sha256'],'旧生成文件已修改，不能自动回收：'+rel
 target.unlink()
manifest={'batch':batch,'theory_review_baseline':'B676','source_sections':39,'files':files,'local_dependencies':edges,'all_local_dependencies_present':True}
(D/'阅读包清单.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
zipout=R/f'交付版本/Hirose-SFG-中文审阅版-{batch}.zip'
with zipfile.ZipFile(zipout,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(D.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(D.parent).as_posix())
with zipfile.ZipFile(zipout) as z:assert z.testzip() is None
result={'batch':batch,'files':len(files)+1,'local_dependencies':len(edges),'missing_dependencies':[],'39_source_sections_byte_identical':True,'owned_unchanged_stale_generated_files_removed':sorted(stale),'zip_bytes':zipout.stat().st_size,'zip_sha256':sha(zipout.read_bytes()),'zip_integrity_passed':True}
(O/(batch+'阅读包验收.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False))

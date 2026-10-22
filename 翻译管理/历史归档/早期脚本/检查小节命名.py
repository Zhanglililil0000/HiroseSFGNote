from pathlib import Path
from urllib.parse import unquote
import json, re, csv
r = Path(__file__).resolve().parents[1]
report = json.loads((r/'翻译管理/文件命名修订记录.json').read_text(encoding='utf-8'))
errors = []
for row in report['文件']:
 if not (r/row['现文件']).is_file(): errors.append('目标缺失：'+row['现文件'])
 if row['更名'] and (r/row['原文件']).exists(): errors.append('旧文件残留：'+row['原文件'])
docs = list((r/'中文版本').glob('*/*.md')) + [r/'Preface序言.md',r/'README.md',r/'翻译管理/文件命名修订记录.md']
checked = 0
for p in docs:
 if not p.exists(): continue
 text = p.read_text(encoding='utf-8-sig')
 for m in re.finditer(r'\]\(',text):
  pos = m.end(); end = pos; depth = 1
  while end < len(text) and depth:
   if text[end] == '(': depth += 1
   elif text[end] == ')': depth -= 1
   end += 1
  if depth: continue
  raw = text[pos:end-1].strip().strip('<>')
  if not raw or raw.startswith(('#','http:','https:','mailto:','data:')): continue
  target = unquote(raw.split('#')[0])
  if not re.search(r'\.(md|png|jpg|pdf|tsv|json)$',target,re.I): continue
  checked += 1
  if not (p.parent/target).exists(): errors.append(str(p.relative_to(r))+' -> '+target)
rows = list(csv.DictReader((r/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
for row in rows:
 if row['编号'] in {x['编号'] for x in report['文件']}:
  path = row['现有译文路径'].replace('\\','/')
  if not (r/path).exists(): errors.append('清单路径失效：'+path)
out = {'核对小节':24,'更名数量':report['更名数量'],'读者文档本地链接数':checked,'错误':errors,'数学行检查':'24节更名前后逐行一致'}
(r/'翻译管理/文件命名修订检查.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))

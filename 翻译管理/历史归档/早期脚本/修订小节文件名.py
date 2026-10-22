from pathlib import Path
from urllib.parse import quote
import csv, io, json, re, hashlib

r = Path(__file__).resolve().parents[1]
if (r/'翻译管理/文件命名修订记录.json').exists():
 raise SystemExit('本次迁移已有记录；停止重复执行，防止覆盖原文件名及迁移前哈希。')
titles = {
 '1.1':'红外-可见光和频振动光谱（SFG）入门', '1.2':'振动共振、费米共振与双原子分子',
 '1.3':'光电场、极化与菲涅尔因子', '1.4':'电偶极子的电场与辐射', '1.5':'SFG光谱的早期工作整理（1983—1995）',
 '2.1':'嵌入层内的发光膜产生的光电场', '2.2':'多层膜的和频过程（SFG）',
 '2.3':'多层膜的和频过程（SFG）：附录集', '2.4':'多层膜的和频过程（SFG）：表达式',
 '2.5':'多层膜的和频过程（SFG）：要点', '2.6':'薄膜内的电场',
 '3.1':'二层膜及三层膜产生的和频光', '3.2':'双层膜和频的一般式',
 '4.1':'CH、CH₂、CH₃基团CH伸缩振动的和频极化率', '4.2':'CH₃基团的取向与和频张量',
 '4.3':'CH₂基团的取向与和频张量', '4.4':'CH基团的取向与和频张量',
 '4.5':'两个CH₃基团的张量分量', '4.6':'CH₃基团的C₃ᵥ对称性破缺时的处理',
 '4.7':'CH₂、平面HCCH及扭转HCCH的和频张量', '4.8':'氢化金刚石表面CH的和频张量',
 '4.9':'氢化金刚石表面CH的和频张量（要点）', '4.10':'CH₂基团及HCCH基团的欧拉角',
 '4.11':'表面坐标系到实验室坐标系的张量旋转',
}
root = r/'中文版本'
files = {p.name.split(' ')[0]:p for p in root.glob('*/*.md') if re.match(r'^\d+\.\d+ ',p.name)}
assert set(files) == set(titles)
rows, replacements, originals = [], {}, {}
for k in sorted(titles, key=lambda x:tuple(map(int,x.split('.')))):
 p = files[k]; q = p.with_name(k+' '+titles[k]+'.md')
 assert p.resolve().is_relative_to(r) and q.resolve().is_relative_to(r)
 assert p == q or not q.exists(), q
 old = p.read_bytes(); originals[k] = old
 rows.append({'编号':k,'原文件':p.relative_to(r).as_posix(),'现文件':q.relative_to(r).as_posix(),'原SHA256':hashlib.sha256(old).hexdigest(),'更名':p != q})
 if p != q:
  replacements[p.name] = q.name
  for safe in ['/', '', '/()', '()']:
   replacements[quote(p.name,safe=safe)] = quote(q.name,safe=safe)
  replacements[p.name.replace(' ','%20')] = q.name.replace(' ','%20')
for row in rows:
 if row['更名']: (r/row['原文件']).rename(r/row['现文件'])
changed = []
for p in r.rglob('*'):
 if not p.is_file() or p == Path(__file__).resolve() or p.suffix.lower() not in {'.md','.tsv','.json','.py','.cjs','.js','.txt','.yaml','.yml'}: continue
 rel = p.relative_to(r)
 if any(x in {'基线快照','来源记录','.git','node_modules','__pycache__'} for x in rel.parts) or any(x in p.name for x in ['前旧译','修订前','本批译文']): continue
 try: t = p.read_bytes().decode('utf-8')
 except UnicodeDecodeError: continue
 new = t
 for a,b in sorted(replacements.items(),key=lambda x:-len(x[0])): new = new.replace(a,b)
 if new != t: p.write_bytes(new.encode('utf-8')); changed.append(rel.as_posix())
fixes = {
 '原文件名保留以兼容链接。':'文件名已按本节内容修订（2026-10-21）。',
 '旧文件名保留以兼容链接，正文题目按原文校正。':'文件名与正文题目均已按本节内容校正。',
 '旧文件名保留，正文按原题恢复甲基对称性破缺主题。':'文件名与正文均按原题恢复甲基对称性破缺主题。',
 '文件名暂保留历史译名。':'文件名已与本节内容对齐（2026-10-21）。',
}
for p in root.rglob('*.md'):
 t = p.read_bytes().decode('utf-8'); n = t
 for a,b in fixes.items(): n = n.replace(a,b)
 if n != t: p.write_bytes(n.encode('utf-8')); changed.append(p.relative_to(r).as_posix())
p = r/'翻译管理/章节清单.tsv'
reader = csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t')
fields = reader.fieldnames; data = list(reader)
for row in data:
 if row['编号'] in titles: row['暂定中文标题'] = titles[row['编号']]
s = io.StringIO(newline=''); w = csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(data)
p.write_bytes(s.getvalue().encode('utf-8'))
for row in rows:
 after = (r/row['现文件']).read_bytes(); row['现SHA256'] = hashlib.sha256(after).hexdigest()
 def mathlines(b): return [x for x in b.decode('utf-8-sig').splitlines() if '$' in x or '\\[' in x or '\\]' in x]
 assert mathlines(originals[row['编号']]) == mathlines(after), row['编号']
 row['数学行未改变'] = True
report = {'日期':'2026-10-21','核对数量':24,'更名数量':sum(x['更名'] for x in rows),'文件':rows,'更新引用的文件':sorted(set(changed)), '历史记录处理':'基线快照、来源记录及旧译/修订前/本批译文快照原样保留；其他管理记录及脚本的路径引用同步迁移。历史验收哈希不改写。'}
(r/'翻译管理/文件命名修订记录.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
lines = ['# 小节文件命名修订记录','','日期：2026-10-21。按正文主题、已校订标题、原文题名及导读核对第一至第四章全部24节。保留节号及章节文件夹。','','共修正'+str(report['更名数量'])+'个文件名。1.1、1.2、1.4、2.6保留原名。目录、序言、管理清单及相关脚本的路径引用同步更新。基线、来源记录和旧译快照保留原样；历史路径可通过下表追溯。','','| 节号 | 原文件名 | 现文件名 |','|---|---|---|']
for row in rows:
 lines.append('| '+row['编号']+' | '+Path(row['原文件']).name+' | ['+Path(row['现文件']).name+']('+quote('../'+row['现文件'],safe='/')+') |')
lines += ['','命名说明：2.3—2.5保留附录集、表达式、要点的独立版本性质；3.1体现二层及三层膜；4.5体现两个甲基的张量分量；4.6恢复甲基对称性破缺主题；4.7—4.9恢复HCCH及氢化金刚石表面主题；4.10、4.11分别体现欧拉角和坐标系之间的张量旋转。','','本轮未修改公式、译校完成状态或原文疑点结论。24节所有含数学标记的行与更名前逐行一致。少数导言中过时的“保留旧文件名”说明已更新；详细路径、迁移前后文件哈希和引用更新清单见同名JSON。历史验收哈希保留其当时含义，不作为本轮文件哈希。']
(r/'翻译管理/文件命名修订记录.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
p = r/'翻译管理/当前进度与续接.md'; t = p.read_text(encoding='utf-8')
marker = '## 文件命名维护（2026-10-21）\n\n已核对第一至第四章24节，修正'+str(report['更名数量'])+'个文件名，同步迁移目录、序言、管理清单及相关脚本的路径引用。详见[文件命名修订记录](文件命名修订记录.md)。译校状态及下一阶段仍以下列第四章完成记录为准。\n\n'
p.write_text(t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+marker,1),encoding='utf-8')
print(json.dumps({'核对':24,'更名':report['更名数量'],'引用更新文件':len(set(changed))},ensure_ascii=False))

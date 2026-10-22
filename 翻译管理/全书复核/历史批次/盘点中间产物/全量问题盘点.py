from pathlib import Path
import re,json,csv
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核'
q=(R/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8-sig')
rows=list(csv.DictReader((R/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
ids=sorted(set(re.findall(r'Q\d{3}',q)))
items=[]
for id in ids:
 headings=[m for m in re.finditer(r'(?m)^#{2,3} '+id+r'[^\n]*',q)]
 table=[l for l in q.splitlines() if re.match(r'^\| '+id+r'\s*\|',l)]
 reg=[]
 for m in headings:
  stop=re.search(r'(?m)^## ',q[m.end():]);end=m.end()+stop.start() if stop else len(q)
  reg.append(q[m.start():end].strip())
 locations=[];notes=[]
 for row in rows:
  p=R/row['现有译文路径'];s=p.read_text(encoding='utf-8-sig')
  matches=[(n,line) for n,line in enumerate(s.splitlines(),1) if re.search(id+r'(?!\d)',line)]
  for n,line in matches:
   locations.append({'section':row['编号'],'path':row['现有译文路径'],'line':n})
   if line.startswith('>') or '**' in line:notes.append(line)
 title=headings[0][0].lstrip('# ') if headings else (table[0] if table else next((l for l in q.splitlines() if id in l),id))
 items.append({'id':id,'title':title,'registration':reg,'table_history':table,'locations':locations,'body_notes':list(dict.fromkeys(notes))})
(O/'全量问题盘点.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
for a,b in [(1,80),(81,160),(161,240),(241,322)]:
 selected=[x for x in items if a<=int(x['id'][1:])<=b]
 lines=[]
 for x in selected:
  first=x['body_notes'][0] if x['body_notes'] else x['title']
  lines.append(x['id']+' | '+','.join(dict.fromkeys(z['section'] for z in x['locations']))+' | '+first[:205])
 (O/f'盘点阅读-{a:03}-{b:03}.txt').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps({'questions':len(items),'without_body_locations':[x['id'] for x in items if not x['locations']],'body_notes':sum(len(x['body_notes']) for x in items)},ensure_ascii=False))

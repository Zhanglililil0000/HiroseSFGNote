from pathlib import Path
import re,json
r=Path('HiroseSFGNote');src=(r/'翻译管理/全书调查/文本缓存/1.5.txt').read_text(encoding='utf-8');s=re.sub(r'===== PDF p\.\d+ =====','',src);s=re.sub(r'(?m)^-\d+-\s*$','',s);s=re.sub(r'(?m)^(?:VSFG|\(pre-VSFG\))\s*$','',s);ms=list(re.finditer(r'(?m)^(\d{2}-\d+)\.?\s+',s));rows=[]
for j,z in enumerate(ms):
 body=s[z.end():ms[j+1].start() if j+1<len(ms) else len(s)].strip();a=body.find('"');citation=re.sub(r'\s+',' ',body[:a]).strip();title=re.sub(r'\s+',' ',body[a:]).strip().strip('".\n ');page=int(re.findall(r'===== PDF p\.(\d+) =====',src[:src.index(z.group(1))])[-1]);rows.append(dict(id=z.group(1),page=page,citation=citation,title=title))
(r/'翻译管理/校订记录/1.5/书目提取.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
for x in rows:
 if x['id'] in ['89-1','90-6','91-4','92-2','93-1','93-9','93-17','94-8','95-1']: print(x['id'],x['citation'],x['title'])
print(len(rows))

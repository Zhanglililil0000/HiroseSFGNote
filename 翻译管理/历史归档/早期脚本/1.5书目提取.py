from pathlib import Path
import re,json
r=Path('HiroseSFGNote');s=(r/'翻译管理/全书调查/文本缓存/1.5.txt').read_text(encoding='utf-8');parts=re.split(r'===== PDF p\.(\d+) =====',s);pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)};all=[]
for n,txt in pages.items():
 txt=re.sub(r'(?m)^-\d+-\s*$','',txt).strip();matches=list(re.finditer(r'(?m)^(\d{2}-\d+)\.?\s+',txt))
 for j,z in enumerate(matches):
  body=txt[z.end():matches[j+1].start() if j+1<len(matches) else len(txt)].strip();a=body.find('"');citation=body[:a].strip();title=body[a:].strip().strip('".\n ');title=re.sub(r'\s+',' ',title);all.append({'id':z.group(1),'page':n,'citation':citation,'title':title})
(r/'翻译管理/校订记录/1.5/书目提取.json').write_text(json.dumps(all,ensure_ascii=False,indent=2),encoding='utf-8')
for x in all:print(x['id']+' | '+x['title'])
print('COUNT',len(all))

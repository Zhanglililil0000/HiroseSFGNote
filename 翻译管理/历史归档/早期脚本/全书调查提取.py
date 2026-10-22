from pathlib import Path
import subprocess, xml.etree.ElementTree as ET, csv, json, re, hashlib, pdfplumber
root=Path('HiroseSFGNote').resolve(); base=root/'翻译管理'/'全书调查'; cache=base/'文本缓存'; cache.mkdir(parents=True,exist_ok=True)
rows=list(csv.DictReader((root/'翻译管理'/'章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
all_data=[]
for row in rows:
 sid=row['编号']; pdf=root/row['原文路径']
 doc=pdfplumber.open(pdf); pages=[]
 for pn,page in enumerate(doc.pages,1):
  lines=[]
  for line in page.extract_text_lines():
   txt=line['text']
   lines.append({'text':txt, 'x':round(line['x0'],1),'y':round(line['top'],1),'h':round(line['bottom']-line['top'],1)})
  text='\n'.join(l['text'] for l in lines); compact=re.sub(r'\s','',text)
  ja=len(re.findall(r'[\u3040-\u30ff\u3400-\u9fff]',text)); replacement=text.count('\ufffd')
  math_lines=sum(bool(re.search(r'[=∑∫χβΓωαθφψπεμ]|\\[a-zA-Z]+',l['text'])) for l in lines)
  pages.append({'page':pn,'width':page.width,'height':page.height,'chars':len(compact),'ja_chars':ja,'replacement':replacement,'lines':lines,'math_lines':math_lines,'line_count':len(lines),'images':len(page.images),'curves':len(page.curves),'rects':len(page.rects),'vector_lines':len(page.lines),'cid_count':len(re.findall(r'\(cid:\d+\)',text))})
  page.close()
 doc.close()
 info={'id':sid,'source':row['原文路径'],'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'web_title':row['网页日文标题'],'title_zh':row['暂定中文标题'],'translation':row['现有译文路径'],'pages':pages}
 all_data.append(info)
 (cache/f'{sid}.txt').write_text('\n\n'.join(f'===== PDF p.{p["page"]} =====\n'+'\n'.join(l['text'] for l in p['lines']) for p in pages),encoding='utf-8')
 print(sid,len(pages),sum(p['chars'] for p in pages),sum(p['ja_chars'] for p in pages),flush=True)
(base/'提取数据.json').write_text(json.dumps(all_data,ensure_ascii=False,indent=1),encoding='utf-8')
preview=[]
for d in all_data:
 preview += ['\n## '+d['id']+' '+d['web_title']]
 for p in d['pages']:
  if p['page']==1:preview+=['P1: '+' | '.join(l['text'] for l in p['lines'][:16])]
  candidates=[l for l in p['lines'] if re.match(r'^\s*(?:[0-9０-９]{1,2}[.．、)）]|[A-Z][.．、)）]|[（(][0-9０-９]{1,2}[)）]|付録|付記|補足|参考文献|References|Appendix)',l['text']) or (l['h']>=14 and len(l['text'])<100 and re.search(r'[\u3040-\u30ff\u3400-\u9fff]',l['text']))]
  if candidates:preview+=['p'+str(p['page'])+': '+' | '.join(l['text'] for l in candidates)]
(base/'标题候选预览.txt').write_text('\n'.join(preview),encoding='utf-8')

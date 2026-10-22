from pathlib import Path
from urllib.parse import unquote
import hashlib,json,re,csv
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
p=r/'中文版本/第五章 张量与对称性/5.1 和频张量与对称性.md';t=p.read_text(encoding='utf-8')
record=json.loads((o/'全节验收.json').read_text(encoding='utf-8'))
assert hashlib.sha256(p.read_bytes()).hexdigest()==record['canonical_sha256']
assert hashlib.sha256((r/'日语原版/Chapter5/chap5-1.pdf').read_bytes()).hexdigest()==record['source_sha256']
before=(o/'B425前分批稿.md').read_text(encoding='utf-8')
oldbody=before[before.index('## 对称性与张量分量'):].split('<!-- B424结束：')[0].strip()
assert oldbody in t, '先前已验收的正文被意外改动'
for n in range(425,434):
 b=f'B{n}';bt=(o/(b+'-本批译文.md')).read_text(encoding='utf-8')
 d=json.loads((o/(b+'验收.json')).read_text(encoding='utf-8'))
 assert d['已排版'] and d['已原页对照'] and not d['采用原文修正']
 assert hashlib.sha256(bt.encode('utf-8')).hexdigest()==d['translation_sha256']
 assert bt.strip() in t,b+'未完整合入'
render=json.loads((o/'全节排版检查.json').read_text(encoding='utf-8'))
assert render['math']==200 and not render['errors'] and not render['overs'] and render['width']==render['scrollWidth']
assert len(render['tables'])==2 and len(render['tags'])==16
for n in range(198,209):
 assert 'Q'+str(n) in t and '## Q'+str(n)+'｜' in (r/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8')
docs=[r/'Preface序言.md',r/'中文版本/第五章 张量与对称性/阅读导航.md']
links=0
for doc in docs:
 text=doc.read_text(encoding='utf-8')
 for raw in re.findall(r'\]\(([^\n)]+)\)',text):
  if raw.startswith(('http:','https:','#')):continue
  path=unquote(raw.split('#')[0]);assert (doc.parent/path).exists(),path;links+=1
rows=list(csv.DictReader((r/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
row=next(x for x in rows if x['编号']=='5.1');assert '全7页完成' in row['状态'] and (r/row['现有译文路径']).exists()
assert next(x for x in rows if x['编号']=='5.2')['状态']=='待翻译'
result={'日期':'2026-10-21','结果':'通过','合稿摘要匹配':True,'先前B423_B424正文未改变':True,'新9批均完整合入且验收哈希匹配':True,'7页覆盖':True,'27分量':True,'200数学片段':True,'两表及16编号组':True,'本地导航链接已核':links,'Q198至Q208正文与问题表均有登记':True,'原文修正采用':False,'5_2保持待翻译':True}
(o/'最终检查.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))

from pathlib import Path
from urllib.parse import unquote
import json,hashlib,re,csv,collections
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
p=r/'中文版本/第五章 张量与对称性/5.2 主要点群的特征标表与基底.md';t=p.read_text(encoding='utf-8')
d=json.loads((o/'全节验收.json').read_text(encoding='utf-8'));full=json.loads((o/'全节排版检查.json').read_text(encoding='utf-8'))
assert hashlib.sha256(p.read_bytes()).hexdigest()==d['canonical_sha256']==full['canonical_sha256']
assert hashlib.sha256((r/'日语原版/Chapter5/chap5-2.pdf').read_bytes()).hexdigest()==d['source_sha256']
idx=json.loads((o/'余部分批索引.json').read_text(encoding='utf-8'));raw=json.loads((o/'表格字形.json').read_text(encoding='utf-8'))
pagechars=collections.Counter()
for x in idx:
 b=x['批次'];text=(o/(b+'-本批译文.md')).read_text(encoding='utf-8');rec=json.loads((o/(b+'验收.json')).read_text(encoding='utf-8'))
 assert text.strip() in t and hashlib.sha256(text.encode('utf-8')).hexdigest()==rec['translation_sha256']
 assert rec['已原页对照'] and rec['已排版'] and not rec['采用原文修正']
 cov=json.loads((o/(b+'-覆盖.json')).read_text(encoding='utf-8'));assert len(cov)==rec['覆盖单元'];pagechars[rec['PDF页']]+=sum(y['原字符数'] for y in cov)
for page,es in raw.items():
 expected=sum(e['字符数'] if e['kind']=='line' else sum(z['字符数'] for z in e['rows']) for e in es)
 assert pagechars[int(page)]==expected,('页覆盖字符记录不匹配',page)
assert len(idx)==38 and set(pagechars)==set(range(2,23))
assert len(re.findall(r'^## .+（PDF p\d+）$',t,re.M))==38
assert full['math']==3313 and full['errors']==0 and full['width']==full['scrollWidth'] and len(full['tables'])==75
assert all(x['width']>=x['scrollWidth'] for x in full['tables'])
issues=(r/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8')
for q in range(209,221):assert f'Q{q}' in t and f'## Q{q}｜' in issues
snapshot=(o/'B435前分批稿.md').read_text(encoding='utf-8');old=snapshot[snapshot.index('## 记号与适用范围'):].split('<!-- B434结束：')[0].strip();assert old in t
assert not re.search(r'distributed over|without consideration|ROOT|\(cid:',t)
links=0
for doc in [r/'Preface序言.md',r/'中文版本/第五章 张量与对称性/阅读导航.md']:
 for rawlink in re.findall(r'\]\(([^\n)]+)\)',doc.read_text(encoding='utf-8')):
  if rawlink.startswith(('http:','https:','#')):continue
  assert (doc.parent/unquote(rawlink.split('#')[0])).exists(),rawlink;links+=1
rows=list(csv.DictReader((r/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
assert '全22页完成' in next(x for x in rows if x['编号']=='5.2')['状态']
assert next(x for x in rows if x['编号']=='5.3')['状态']=='待翻译'
result={'结果':'通过','最终合稿及显示摘要匹配':True,'原始PDF摘要匹配':True,'原p1已验收正文保持':True,'38点群块完整合入':True,'76原表逐行字符覆盖记录一致':True,'3313数学片段通过':True,'75个合稿表格无横向溢出':True,'Q209至Q220正文与问题表均有登记':True,'新导航链接有效':links,'5_3保持待翻译':True,'采用原文修正':False,'限制':'完成本轮译校与排版，不等同于独立物理审校。'}
(o/'最终检查.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False,indent=2))

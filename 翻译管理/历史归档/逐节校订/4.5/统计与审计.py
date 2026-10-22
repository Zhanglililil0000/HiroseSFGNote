from pathlib import Path
import json,re,collections
out=Path(__file__).resolve().parent
d=json.loads((out/'全节公式与覆盖索引.json').read_text(encoding='utf-8'))
for x in d['batches']:
 c=collections.Counter(y['symbol'] for y in x['tensor_components'])
 print(x['batch'],dict(c))
cnt=collections.Counter(y['symbol'] for x in d['batches'] for y in x['tensor_components'])
print('total',dict(cnt))
rows=[r for p in json.loads((out/'逐行提取.json').read_text(encoding='utf-8')) for r in p['lines']]
print('unusual Greek',[(r['id'],r['raw']) for r in rows if r['id']>='p03l14' and re.search(r'[ΦΓΔΩΨΞ]|cid:',r['raw'])])
print('oddscript',[(r['id'],r['raw']) for r in rows if r['id']>='p03l14' and re.search(r'[_^]\{[^}]*[+=()\[\]]',r['raw'])][:20])

from pathlib import Path
import json,re,collections
out=Path(__file__).resolve().parent
d=json.loads((out/'全节公式与覆盖索引.json').read_text(encoding='utf-8'))
odd=[]
for x in d['batches']:
 print(x['batch'],x['scope'],len(x['tensor_components']),len(x['formulas']))
 for f in x['formulas']:
  t=' '.join(f['latex_lines'])
  pairs=[(a,b,t.count(a),t.count(b)) for a,b in [('(',')'),('[',']'),(r'\{',r'\}')] if t.count(a)!=t.count(b)]
  if pairs:odd.append({'batch':x['batch'],'source':f['source_lines'][0],'pairs':pairs,'latex':t})
(out/'原式分组疑点.json').write_text(json.dumps(odd,ensure_ascii=False,indent=2),encoding='utf-8')
print('group anomalies',len(odd));print([(x['source'],x['pairs']) for x in odd])

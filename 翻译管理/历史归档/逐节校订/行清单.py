from pathlib import Path
import json,re,sys
root=Path(__file__).parent
sec=sys.argv[1];d=json.loads((root/sec/'字形行.json').read_text(encoding='utf-8'))
for p,ls in d.items():
 for l in ls:
  if re.search('[ぁ-んァ-ン一-龯]',l['tex']):print(p,l['y'],l['tex'])

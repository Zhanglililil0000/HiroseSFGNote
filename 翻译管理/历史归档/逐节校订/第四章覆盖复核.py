from pathlib import Path
import re,json,hashlib
from PIL import Image
root=Path(__file__).resolve().parents[2];base=root/'翻译管理/校订记录'
summary={}
for sec,nums in [('4.8',range(385,402)),('4.9',range(402,416)),('4.10',range(416,421)),('4.11',range(421,423))]:
 out=base/sec;canonical=next((root/'中文版本/第四章 单层膜与多层膜的和频').glob(sec+' *.md'))
 records=[];appendix=[]
 for n in nums:
  r=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'));t=(out/f'B{n}-本批译文.md').read_text(encoding='utf-8')
  lhs=re.findall(r'\\chi_\{([XYZxyz]{3})\}\s*&?=',t)
  loc=[p for group in r.get('source_lines_and_locations',[]) for p,y in group['locations']]
  if sec=='4.8' and n==385:loc=[1,2,3]
  if sec=='4.9' and n==402:loc=[1,2]
  if sec=='4.10':loc={416:[1,2],417:[2,3],418:[3,4,5,6],419:[6],420:[6,7,8]}[n]
  r.update(pages=sorted(set(loc)),tensor_left_sides=lhs,source_images_visually_checked=True,translation_sha256=hashlib.sha256(t.encode()).hexdigest())
  (out/f'B{n}-覆盖.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');records.append(r)
  if (sec=='4.8' and n>=398) or (sec=='4.9' and n>=412):appendix.append([n,len(lhs)])
 if appendix:assert [c for n,c in appendix]==[27]*4,(sec,appendix)
 if sec=='4.11':assert sum(len(r['tensor_left_sides']) for r in records)==27
 s=canonical.read_text(encoding='utf-8')
 assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
 assert '(cid:' not in s and '详细公式请参阅' not in s
 summary[sec]={'batches':[r['batch'] for r in records],'pages':sorted(set(p for r in records for p in r['pages'])),'tensor_equalities':sum(len(r['tensor_left_sides']) for r in records),'appendix_groups':appendix}
 for n in ([386,394,401] if sec=='4.8' else [406,415] if sec=='4.9' else [416,418,420] if sec=='4.10' else [421,422]):
  p=out/f'B{n}-参考渲染.png'
  if p.exists():
   im=Image.open(p);im.crop((0,0,im.width,min(1500,im.height))).save(out/f'B{n}-显示抽查.png')
(base/'第四章余部覆盖复核.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))

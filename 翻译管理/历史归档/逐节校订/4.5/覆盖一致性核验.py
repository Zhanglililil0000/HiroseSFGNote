from pathlib import Path
import json,re,collections,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
pages=json.loads((out/'逐行提取.json').read_text(encoding='utf-8'))
rows={r['id']:r for p in pages for r in p['lines'] if r['id']>='p03l14'}
idx=json.loads((out/'全节公式与覆盖索引.json').read_text(encoding='utf-8'))
prose=json.loads((out/'叙述译文映射.json').read_text(encoding='utf-8'))
source_ids=[k for b in idx['batches'] for k in b['source_lines']]
assert source_ids==list(rows)
assert len(source_ids)==len(set(source_ids))==2627
math_ids=[k for b in idx['batches'] for f in b['formulas'] for k in f['source_lines']]
none_ids=[k for k,r in rows.items() if not r['jp'] and re.fullmatch(r'\([ps]{3}\)\s*\(none\)',r['raw'])]
assert len(none_ids)==50,len(none_ids)
assert set(math_ids).isdisjoint(none_ids)
assert set(math_ids)|set(none_ids)=={k for k,r in rows.items() if not r['jp']}
assert len(math_ids)==len(set(math_ids))
assert {k for k,r in rows.items() if r['jp']}<=set(prose['translation'])|set(prose['skip'])
inverse={'alpha':'α','beta':'β','gamma':'γ','delta':'δ','epsilon':'ε','zeta':'ζ','eta':'η','theta':'θ','kappa':'κ','lambda':'λ','mu':'μ','nu':'ν','xi':'ξ','pi':'π','varpi':'ϖ','rho':'ρ','sigma':'σ','tau':'τ','upsilon':'υ','phi':'φ','chi':'χ','psi':'ψ','omega':'ω','Delta':'Δ','Phi':'Φ','Theta':'Θ','Omega':'Ω','Gamma':'Γ','Pi':'Π','Sigma':'Σ','sum':'Σ','Xi':'Ξ','Psi':'Ψ','ne':'≠','infty':'∞','times':'×','pm':'±','sqrt':'√','gg':'>>','sim':'~','sin':'sin','cos':'cos'}
def canonical(t):return re.sub(r'\s+','',t)
reverse_fail=[]
for b in idx['batches']:
 for f in b['formulas']:
  for k,latex in zip(f['source_lines'],f['latex_lines']):
   text=re.sub(r'\\([A-Za-z]+)',lambda m:inverse.get(m[1],m[0]),latex).replace(r'\{','{').replace(r'\}','}')
   raw=re.sub(r'^\([ps]{3}\)\s*','',rows[k]['raw'])
   raw=re.sub(r'^\([ab]_\{[12]\}\)\s*','',raw)
   if canonical(text)!=canonical(raw):reverse_fail.append({'source':k,'raw':raw,'reversed':text})
assert not reverse_fail,reverse_fail[:5]
counts=collections.Counter(c['symbol'] for b in idx['batches'] for c in b['tensor_components'])
assert counts=={'beta':156,'chi':853},counts
for low,high in [(341,344),(345,348),(349,352),(353,356),(357,361)]:
 chi=[c for b in idx['batches'] if low<=int(b['batch'][1:])<=high for c in b['tensor_components'] if c['symbol']=='chi']
 assert len(chi)==135,(low,len(chi))
 # Each full component table retains every one of the 27 ordered triples.
 counter=collections.Counter(c['indices'] for c in chi)
 assert len(counter)==27 and set(counter.values())=={5},(low,counter)
anomalies=json.loads((out/'原式分组疑点位置.json').read_text(encoding='utf-8'))
assert len(anomalies)==27
source=root/'日语原版/Chapter4/chap4-5.pdf'
audit={'date':'2026-10-21','source_pages':78,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'post_B325_source_lines':len(source_ids),'math_physical_lines':len(math_ids),'none_items':len(none_ids),'unmapped_math_lines':0,'duplicate_source_lines':0,'prose_mapping_complete':True,'math_round_trip_mismatches':len(reverse_fail),'chi_component_equalities':counts['chi'],'beta_component_equalities':counts['beta'],'appendix_B_to_F_each_chi_tables':'5×27=135','bracket_issue_locations':len(anomalies),'verification_limit':'数字字形与基线转录、逐页图浏览及异常重点复核；不表示原文理论推导已经独立证明。'}
(out/'覆盖一致性核验.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(audit,ensure_ascii=False,indent=2))

from pathlib import Path
import json,csv,re
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md'
old=(o/'B163-修订前.md').read_text(encoding='utf-8');new=p.read_text(encoding='utf-8')
assert new[new.index('### L系数'):]==old[old.index('### L系数'):]
metrics=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));assert metrics['math']==9 and not metrics['results'][0]['overs']
assert len(re.findall(r'(?m)^\$\$$',(o/'B163-本批译文.md').read_text(encoding='utf-8')))==18
(o/'B163验收.json').write_text(json.dumps({'batch':'B163','date':'2026-10-20','source_pages':[1,2],'toc_entries':39,'unnumbered_formula_groups':9,'math_syntax_errors':0,'display_overflows':0,'render_preview_checked':True,'tail_unchanged_from_L_section':True,'source_corrections_adopted':False,'next':'B164：p2—3完整L系数单元'},ensure_ascii=False,indent=2),encoding='utf-8')
f=m/'全书调查/分批建议.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:reader=csv.DictReader(h,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
found=False
for row in rows:
 if row['节号']=='3.1' and not found:
  row['执行状态']='2026-10-20 B163已核p1—2目录、引言及反射/透射系数；仅此子单元完成，L系数起及后续待核，见3.1结构与复用核验表';found=True
assert found
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('B163验收通过；L系数起保持原样；分批建议已更新。')

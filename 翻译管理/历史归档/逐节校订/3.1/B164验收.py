from pathlib import Path
import json,csv,re
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md'
old=(o/'B164-修订前.md').read_text(encoding='utf-8');new=p.read_text(encoding='utf-8');key='## 2. 二层系';assert new[new.index(key):]==old[old.index(key):]
metrics=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));row=next(x for x in metrics['results'] if x['batch']=='B164');assert not row['overs']
fragment=(o/'B164-本批译文.md').read_text(encoding='utf-8');assert len(re.findall(r'\$\$([\s\S]*?)\$\$',fragment))==16
# All 15 coefficient strings agree with the preexisting transcription after whitespace removal.
a=old.index('### L系数');b=old.index(key);before=re.findall(r'\$\$([\s\S]*?)\$\$',old[a:b])[1:];after=re.findall(r'\$\$([\s\S]*?)\$\$',fragment)[1:]
norm=lambda s:re.sub(r'\s+','',s)
assert [norm(x) for x in before]==[norm(x) for x in after]
(o/'B164验收.json').write_text(json.dumps({'batch':'B164','date':'2026-10-20','source_pages':[2,3],'display_groups':16,'L_relations':15,'math_syntax_errors':0,'display_overflows':0,'render_preview_checked':True,'coefficient_transcription_matches_verified_source':True,'section2_onward_unchanged':True,'unresolved':['Q096'],'source_corrections_adopted':False,'next':'B165：2.1引言及跨页式2.1'},ensure_ascii=False,indent=2),encoding='utf-8')
f=o/'B164.md';s=f.read_text(encoding='utf-8').replace('长z分量等式仅分行。','长z分量等式保留全部项，均为可编辑数学且无横向溢出。');f.write_text(s,encoding='utf-8')
f=m/'全书调查/分批建议.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['节号']=='3.1' and 'B163' in row['执行状态']:
  row['执行状态']='2026-10-20 B163—B164完成原目录、引言、第1部分反射/透射及完整L系数；第2部分起待核；Q096保留原文，见3.1校订记录'
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('B164验收通过：16展示式、15条L关系，语法及排版通过，后文未变。')

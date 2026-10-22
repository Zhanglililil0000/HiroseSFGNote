from pathlib import Path
import re,json,csv
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md'
old=(o/'B165-修订前.md').read_text(encoding='utf-8');new=p.read_text(encoding='utf-8');key="**1/m' 界面的 m' 侧：**";assert new[new.index(key):]==old[old.index(key):]
before=old[old.index('## 2. 二层系'):old.index(key)];frag=(o/'B165-本批译文.md').read_text(encoding='utf-8');x=''.join(re.findall(r'\$\$([\s\S]*?)\$\$',before));y=''.join(re.findall(r'\$\$([\s\S]*?)\$\$',frag))
def norm(s):
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s)
 s=re.sub(r'\\\\(?:\[[^\]]*\])?','',s)
 s=re.sub(r'\\hspace\{[^}]*\}','',s)
 s=re.sub(r'\\(?:quad|qquad|times|Bigl|Bigr)','',s)
 s=re.sub(r'\\[,!]','',s)
 return re.sub(r'[\s{}&]','',s)
assert norm(x)==norm(y),(norm(x),norm(y))
metrics=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));assert not next(x for x in metrics['results'] if x['batch']=='B165')['overs']
(o/'B165验收.json').write_text(json.dumps({'batch':'B165','date':'2026-10-20','pages':[3,4],'tags':['2.1'],'cross_page_formula_complete':True,'formula_factors_match_previous_transcription_after_layout_normalization':True,'source_pages_visually_checked':True,'syntax_errors':0,'display_overflows':0,'render_preview_checked':True,'unchanged_tail_from':'1/m′界面m′侧','unresolved':['Q097'],'source_corrections_adopted':False,'next':'B166 / p4式2.2'},ensure_ascii=False,indent=2),encoding='utf-8')
f=m/'全书调查/分批建议.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
found=False
for row in rows:
 if row['节号']=='3.1' and ('B163' in row['执行状态'] or (not found and int(row['PDF起页'])<=3<=int(row['PDF止页']))):
  row['执行状态']='2026-10-20 B163—B165已核目录、第1部分及2.1引言/跨p3—4式2.1；式2.2起待核，Q096—Q097保留原文，详见3.1校订记录';found=True
assert found
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('B165验收通过：公式因子逐字归一化一致，跨页接全，排版通过，后文保持。')

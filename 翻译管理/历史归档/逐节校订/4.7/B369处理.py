from pathlib import Path
import json,hashlib,csv,io,re
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.7 CH₂、平面HCCH及扭转HCCH的和频张量.md'
old=target.read_text(encoding='utf-8')
snap=out/'B369前旧译.md'
if not snap.exists():snap.write_text(old,encoding='utf-8')
tables=[('3b-1','对称伸缩振动',[
('ppp','XXZ','aac','bbc'),('ppp','ZZZ','ccc','ccc'),('spp','YXZ','abc','-abc'),('ssp','YYZ','bbc','aac'),('psp','XYZ','abc','-abc'),('sps',None,None,None),('pps',None,None,None),('pss',None,None,None),('sss',None,None,None)]),
('3b-2','反对称伸缩振动',[
('ppp','XZX','caa','cbb'),('ppp','ZXX','caa','cbb'),('spp','YZX','bca','-cab'),('ssp',None,None,None),('psp','ZYX','bca','-cab'),('sps','YZY','caa','cbb'),('pps','XZY','bca','-cab'),('pps','ZXY','bca','-cab'),('pss','ZYY','caa','cbb'),('sss','YYY','0','0')])]
text='### C₂分子（扭转HCCH基团）\n\n原表将$\\chi=0^\\circ$与$180^\\circ$共用一列，另列$90^\\circ$和$-90^\\circ$。以下保留原列和原有分量范围。\n\n'
records=[]
def beta(x):return '0' if x=='0' else ('-' if x.startswith('-') else '')+r'\beta_{'+x.lstrip('-')+'}'
for label,mode,rows in tables:
 text+=f'#### {mode}——表({label})\n\n| 偏振组合 | 分量 | $\\chi=0^\\circ/180^\\circ$ | $\\chi=90^\\circ$ | $\\chi=-90^\\circ$ |\n|---|---|---|---|---|\n'
 components=[];none=[]
 for pol,idx,a,b in rows:
  if idx is None:
   text+=f'| ({pol}) | 无 | — | — | — |\n';none.append(pol)
  else:
   vals=[beta(a),beta(b),beta(b)]
   text+=f'| ({pol}) | $\\chi_{{{idx}}}$ | '+' | '.join('$'+v+'$' for v in vals)+' |\n'
   components.append({'polarization':pol,'indices':idx,'values':vals})
 records.append({'label':label,'components':components,'none_polarizations':none})
 text+='\n'
text+='> **译者注（表项范围）：** “无”对应原文“none”，表示原表该偏振组合未列分量；破折号仅用于排版，不补写为零。表(3b-2)的(sss)项则明确列出$\\chi_{YYY}=0$，三个角度列均保留该零值。原表在相应角度列使用$\\beta_{bca}$或$-\\beta_{cab}$，两者的指标与符号照录，不预设它们相等。\n'
(out/'B369-本批译文.md').write_text(text,encoding='utf-8')
prefix=old.split('<!-- B368止；')[0].rstrip()
prefix=prefix.replace('B365—B368完成原题、原图、第1、2部分及第3部分引言与表(3a-1)/(3a-2)（PDF p1—4）；表(3b-1)及后续仍为旧译待核。','B365—B369完成原题、原图、第1、2部分及第3部分表(3a-1)/(3a-2)、(3b-1)/(3b-2)（PDF p1—5）；表(3a-3)及后续仍为旧译待核。')
prefix=prefix.replace('第3部分（p3—4已核）','第3部分（p3—5已核）').replace('后续扭转C₂及其他角度表待核。','另已核扭转C₂的表(3b-1)/(3b-2)，保留原none项与显式零值；其他角度表待核。')
end=old.index('*(3b-2)*')+len('*(3b-2)*')
target.write_text(prefix+'\n\n'+text+'\n<!-- B369止；表(3a-3)及后续旧译待核。 -->\n\n> **校订进度：** 以下表(3a-3)及后续为旧译待核，尚未纳入本轮验收。\n\n'+old[end:].strip()+'\n',encoding='utf-8')
rec={'batch':'B369','date':'2026-10-21','pages':[5],'source_sha256':hashlib.sha256((root/'日语原版/Chapter4/chap4-7.pdf').read_bytes()).hexdigest(),'source_images_visually_checked':True,'tables':records,'component_rows':14,'angle_cells':42,'nonzero_cells':39,'zero_cells':3,'none_polarization_items':5,'source_corrections_adopted':False,'next':'B370，p6表(3a-3)'}
(out/'B369-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('B369：两表14分量行、42单元，39非零/3零，另有5个none项。')

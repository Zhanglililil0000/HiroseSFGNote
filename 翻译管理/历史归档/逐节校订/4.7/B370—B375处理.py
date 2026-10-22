from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.7 CH₂、平面HCCH及扭转HCCH的和频张量.md'
snap=out/'B370前旧译.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snap.read_text(encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-7.pdf').read_bytes()).hexdigest()
def powers(s):
 return re.sub(r'\\(sin|cos) ([23])\\(tau|chi)',lambda m:'\\'+m[1]+'^'+m[2]+'\\'+m[3],s)
for batch,tags,page in [(370,['3a-3'],6),(371,['3a-4'],7),(372,['3b-3','3b-4'],8),(373,['3a-5'],9),(374,['3a-6'],10),(375,['3b-5','3b-6'],11)]:
 text='';records=[]
 for tag in tags:
  end=old.index('*('+tag+')*')
  text+='### '+('倾斜C₂ᵥ分子（平面HCCH基团、CH₂基团）' if tag.startswith('3a') else 'C₂分子（扭转HCCH基团）')+'\n\n#### '+('对称伸缩振动' if int(tag[-1])%2 else '反对称伸缩振动')+'——表('+tag+')\n\n'
  if batch<=372:
   start=old.rfind('|  |',0,end);pol='';rows=[];none=[]
   for line in old[start:end].splitlines():
    if not line.startswith('|'):continue
    cells=[x.strip() for x in line.strip('|').split('|')]
    pm=re.search(r'\*\*\(([ps]{3})\)\*\*',cells[0])
    if pm:
     pol=pm[1]
     if 'none' in line:none.append(pol)
     continue
    m=re.search(r'\\chi_\{([XYZ]{3})\}',cells[0])
    if m:rows.append({'polarization':pol,'indices':m[1],'values':[powers(c.strip('$').strip()) for c in cells[1:]]})
   assert len(rows)==(27 if tag.startswith('3a') else (5 if tag=='3b-3' else 9))
   for col,angle in enumerate([r'\chi=\pm45^\circ',r'\chi=\pm135^\circ']):
    text+='##### $'+angle+'$\n\n| 偏振组合 | 分量 | 表达式 |\n|---|---|---|\n'
    for row in rows:text+='| ('+row['polarization']+') | $\\chi_{'+row['indices']+'}$ | $'+row['values'][col]+'$ |\n'
    for pol in none:text+='| ('+pol+') | 无（原文none） | — |\n'
    text+='\n'
   records.append({'label':tag,'rows':rows,'angle_cells':len(rows)*2,'none_polarizations':none})
  else:
   start=old.rfind('\\begin{aligned}',0,end);stop=old.index('\\end{aligned}',start)
   eqs=[]
   for line in old[start:stop].splitlines()[1:]:
    m=re.match(r'\\chi_\{([XYZ]{3})\}\s*&=\s*(.*)',line)
    if m:
     val=re.sub(r'\\\\(?:\[6pt\])?\s*$','',m[2]).strip();val=powers(val)
     eqs.append({'indices':m[1],'expression':val})
   assert len(eqs)==(27 if tag.startswith('3a') else (5 if tag=='3b-5' else 9))
   text+='一般方位角$\\chi$下的原表分量如下。\n\n'
   for eq in eqs:text+='$$\n\\chi_{'+eq['indices']+'}='+eq['expression']+'\n$$\n\n'
   if tag=='3b-5':text+='(sps)、(pps)、(pss)、(sss)：无（原文none）。\n\n'
   if tag=='3b-6':text+='(ssp)：无（原文none）；(sss)的零分量已在上式照录。\n\n'
   records.append({'label':tag,'equations':eqs})
 if batch==370:text+='> **译者注（原文疑点Q182，PDF p6）：** 表(3a-3)的$\\chi_{XXZ}$在$\\pm45^\\circ$列原为$\\tfrac12[(\\beta_{bbc}-\\beta_{ccc})\\cos^2\\tau+(\\beta_{bbc}+\\beta_{aac})]\\sin\\tau$，而$\\pm135^\\circ$列为$\\tfrac12[(\\beta_{bbc}-\\beta_{ccc})\\cos^2\\tau+(\\beta_{aac}+\\beta_{ccc})]\\cos\\tau$。两列括号内常数项和末尾三角因子不同，均照录；若参照后续一般式，前一列可能应与后一列同形，但候选未采用。表中$\\pm$及$-(\\pm)$仍按原共享列保留，不自行指定上下号。\n'
 rec={'batch':f'B{batch}','pages':[page],'tables':records,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False}
 (out/f'B{batch}-本批译文.md').write_text(text,encoding='utf-8')
 (out/f'B{batch}-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
prefix=old.split('<!-- B369止；')[0].rstrip()
tail=old[old.index('### 4. 分子固定'):]
target.write_text(prefix+'\n\n'+'\n\n'.join((out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(370,376))+'\n\n<!-- B375止；第4部分及后续旧译待核。 -->\n\n> **校订进度：** 第3部分全部表已核；以下第4部分及后续为旧译待核。\n\n'+tail,encoding='utf-8')
print('B370—B375：p6—11第3部分八张完整表完成转录核对。')

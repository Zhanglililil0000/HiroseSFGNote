from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.7 CH₂、平面HCCH及扭转HCCH的和频张量.md'
snap=out/'B367前旧译.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snap.read_text(encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-7.pdf').read_bytes()).hexdigest()
angles=[r'\chi=0^\circ/180^\circ',r'\chi=90^\circ',r'\chi=-90^\circ']
all_index=[]
for n,tag,mode,page in [(367,'3a-1','对称伸缩振动',3),(368,'3a-2','反对称伸缩振动',4)]:
 end=old.index('*('+tag+')*');start=old.rfind('|  |',0,end)
 table=old[start:end];rows=[];pol=''
 for line in table.splitlines():
  if not line.startswith('|'):continue
  cells=[x.strip() for x in line.strip('|').split('|')]
  m=re.search(r'\*\*\(([ps]{3})\)\*\*',cells[0])
  if m:pol=m[1];continue
  m=re.search(r'\\chi_\{([XYZ]{3})\}',cells[0])
  if not m:continue
  assert len(cells)==4,line
  vals=[x.strip('$').strip() for x in cells[1:]]
  if n==367:
   vals=[v.replace(r'\sin 2\tau',r'\sin^2\tau').replace(r'\cos 2\tau',r'\cos^2\tau') for v in vals]
  rows.append({'polarization':pol,'indices':m[1],'values':vals})
 assert len(rows)==len(set(r['indices'] for r in rows))==27
 zeros=sum(v=='0' for r in rows for v in r['values'])
 assert zeros==(51 if n==367 else 75),(tag,zeros)
 if n==367:
  text=r'''## 3. 实验室固定$(XYZ)$系中的张量分量

下面推导按光路定义的实验室固定$(XYZ)$坐标系中的张量分量。设$(XYZ)$系由表面固定$(xyz)$系绕$z$轴旋转角$\chi$得到，参见《表面的旋转》。列式时去掉分子固定系中因对称性为零的分量。

> **译者注（局部角度）：** 本段$\chi$用于表面系到实验室系的方位旋转；与第2部分的欧拉角记法须结合变换层级辨认。本表用$\tau$而非$\theta$；其几何含义将在后文具体取向处再核，不能先按旧译当作倍角或直接换成倾斜角。表内实验室分量为零的单元仍完整列出。

### 倾斜C₂ᵥ分子（平面HCCH基团、CH₂基团）

#### 对称伸缩振动——表(3a-1)

原表角度为$\chi=0^\circ,180^\circ,90^\circ,-90^\circ$。为便于阅读，以下按原三个角度列分别排表；分量及正负号逐格保留。

'''
 else:
  text='#### 反对称伸缩振动——表(3a-2)\n\n倾斜C₂ᵥ分子（平面HCCH基团、CH₂基团）。原表角度与表(3a-1)相同，以下仍按原三个角度列分别排表。\n\n'
 for col,angle in enumerate(angles):
  text+='##### $'+angle+'$\n\n| 偏振组合 | 分量 | 表达式 |\n|---|---|---|\n'
  for r in rows:
   text+='| ('+r['polarization']+') | $\\chi_{'+r['indices']+'}$ | $'+r['values'][col]+'$ |\n'
  text+='\n'
 if n==367:
  text+=r'''> **译者注（原文疑点Q181，PDF p3）：** $0^\circ/180^\circ$共享列中有$\pm$及$-(\pm)$，但本页未明确上下号分别对应哪个角度，原符号与共享列保留，不拆成自行指定正负号的两列。$\chi_{ZZX}$在$90^\circ$与$-90^\circ$两列原写相同正号，也照录；不据旋转直觉改号。旧译把本表$\sin^2\tau$、$\cos^2\tau$写成$\sin2\tau$、$\cos2\tau$，现按原页恢复函数幂。
'''
 (out/f'B{n}-本批译文.md').write_text(text,encoding='utf-8')
 rec={'batch':f'B{n}','date':'2026-10-21','pages':[page],'scope':f'第3部分{mode}完整表({tag})'+('及引言' if n==367 else ''),'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False,'original_table_label':tag,'rows':27,'angle_columns':angles,'cells':81,'zero_cells':zeros,'nonzero_cells':81-zeros,'components':rows}
 (out/f'B{n}-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');all_index.append(rec)
 (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n原PDF p{page}，{mode}表({tag})，完整27分量×3列，共81单元（零{zeros}、非零{81-zeros}）。逐格对照原页，按角度列拆成三个窄表以避免横向长表；全部零值保留。'+('恢复sin²τ/cos²τ，保留原±、−(±)及ZZX两列同号，Q181未采用候选修正。' if n==367 else '仅βcaa cosτ六个单元非零，其余75个零；未将零项略去。')+'\n',encoding='utf-8')
first=(out/'B365-本批译文.md').read_text(encoding='utf-8').replace('B365—B366完成原题、原图和第1、2部分（PDF p1—2）；第3部分及后续仍为旧译待核。','B365—B368完成原题、原图、第1、2部分及第3部分引言与表(3a-1)/(3a-2)（PDF p1—4）；表(3b-1)及后续仍为旧译待核。')
first=first.replace('- 后续安排：第3部分从p3开始列实验室系张量，','- 第3部分（p3—4已核）：已完成引言及C₂ᵥ对称/反对称伸缩表(3a-1)/(3a-2)，各27行×3角度列。后续扭转C₂及其他角度表待核。\n- 后续安排：第3部分从p3开始列实验室系张量，')
second=(out/'B366-本批译文.md').read_text(encoding='utf-8')
end=old.index('*(3a-2)*')+len('*(3a-2)*')
tail=old[end:].strip()
joined='\n\n'.join([first,second]+[(out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in [367,368]])
target.write_text(joined+'\n\n<!-- B368止；表(3b-1)及后续旧译待核。 -->\n\n> **校订进度：** 以下扭转C₂表(3b-1)及后续为旧译待核，尚未纳入本轮验收。\n\n'+tail+'\n',encoding='utf-8')
(out/'B367—B368公式与覆盖索引.json').write_text(json.dumps({'table_rows':54,'table_cells':162,'zero_cells':126,'nonzero_cells':36,'batches':all_index},ensure_ascii=False,indent=2),encoding='utf-8')
print('两表54行、162单元已合并；126零值、36非零值；旧译尾部从3b-1起保留。')

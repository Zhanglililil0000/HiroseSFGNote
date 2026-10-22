from pathlib import Path
import json,re,hashlib,runpy
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.9 氢化金刚石表面CH的和频张量（要点）.md'
if not (out/'重建前旧译.md').exists():(out/'重建前旧译.md').write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
src8=(out.parent/'4.8/重建译文.py').read_text(encoding='utf-8')
ns=runpy.run_path(str(out.parent/'4.8/重建译文.py'))
prose8={(e['page'],e['y']):e['text'] for e in ns['events'] if e['kind']=='prose'}
events=[]
def event(p,y,text):events.append({'page':p,'y':y,'kind':'prose','text':text})
def reuse(p,y,a,b):event(p,y,next(v for (pp,yy),v in prose8.items() if pp==a and abs(yy-b)<1))
for p,y,a,b in [(2,690,22,385),(3,74,22,466),(4,407,25,450),(6,74,27,90),(7,440,3,303),(7,757,3,613),(8,91,3,646),(8,207,4,74),(8,240,4,107),(8,407,4,270),(8,523,4,385),(8,557,4,417),(9,274,5,139),(9,473,5,335),(9,657,5,515),(9,740,5,597),(10,174,5,728),(10,590,6,450),(11,307,7,172),(11,424,7,286),(12,157,7,712),(12,573,8,434),(12,590,8,450),(12,723,8,581),(13,457,9,319),(14,174,9,728),(14,307,10,172),(14,757,10,613),(15,473,13,156),(15,673,13,352),(16,573,14,254),(18,91,30,156),(18,157,30,221),(21,140,33,188)]:reuse(p,y,a,b)
data=json.loads((out/'字形行.json').read_text(encoding='utf-8'))
for p,ls in data.items():
 p=int(p)
 if p<3:continue
 for l in ls:
  y=l['y'];s=l['tex'].replace('(cid:160)','').strip()
  if not s:continue
  if re.search('[ぁ-んァ-ン一-龯]',s):
   if '［対称伸縮振動］' in s:event(p,y,'#### 对称伸缩振动')
   elif '［逆対称伸縮振動］' in s:event(p,y,'#### 反对称伸缩振动')
   continue
  if chr(92) in s or '=' in s or 'none' in s or re.fullmatch(r'\([0-9a-z-]+\)',s):events.append({'page':p,'y':y,'kind':'math','text':s})
events.sort(key=lambda e:(e['page'],e['y']))
bounds=[(402,1,0),(403,3,74),(404,4,407),(405,6,74),(406,7,440),(407,9,657),(408,11,307),(409,12,573),(410,14,174),(411,15,473),(412,18,91),(413,19,723),(414,21,140),(415,23,523)]
# 仅复用排版处理函数；所有数学行均取自4.9自身的PDF。
part=src8[src8.index('texts={n:'):src8.index('intro=')].replace('batch=386','batch=403')
exec(part)
intro=ns['texts'][385].split('## 1. 绪论')[1].replace('Q189','Q194')
texts[402]='# 4.9 氢化金刚石表面CH的和频张量（要点）\n\n> 原作：广瀬千秋；中文翻译：章力。按26页原稿译校。\n\n## 阅读引导与目录\n\n原稿先列第6部分，再回到第3—5部分；以下保留该顺序。\n\n| 原部分 | 实际PDF页 | 内容概括 |\n|---|---|---|\n| 1—2 | 1—2 | 位阻、平面/扭转构型、坐标及欧拉角 |\n| 6a—6c | 2—7 | 先查实验室系中平面HCCH、扭转HCCH与后仰CH₂的分量 |\n| 3 | 7—9 | 回到CH键张量的叠加及四面体角近似 |\n| 4a—4b | 9—12 | 平面倾斜和扭转HCCH的表面系张量 |\n| 5a、5b、5d | 12—18 | CH₂扭转、后仰以及组合取向 |\n| 附录A | 18—26 | 四组完整一般取向表达式 |\n\n## 1. 绪论'+intro
texts[406]+='\n> **原文疑点Q194（p8—9）：** 与4.8同类内容的分母37、孤立数字1、重复(Eu-10)引用及局部指标原样保留；不因要点版与完整版重叠而自动统一。\n'
texts[407]+='\n> **Q194续（p9—10）：** τ的几何定义与旋转角关系存在同类歧义，参见4.8的Q191；各处按本稿原式保留。\n'
texts[409]+='\n> **Q194续（p12）：** χ=±γ后仍列cos2χ=−cos2γ，原负号保留，候选去负号未采用。\n'
texts[411]+='\n> **Q194续（p15—16）：** sin3χ、1+cosφ和负号组的首项等原写疑点，与4.8相同者也分别保留，不默改。\n'
texts[414]+='\n> **Q194续（附录）：** 原式未配对括号、未定义字母及同类分量差异按各自原页保留；正文每处括号提示关联的Q193记录也适用于本稿对应位置。\n'
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-9.pdf').read_bytes()).hexdigest()
for n,_,_ in bounds:
 (out/f'B{n}-本批译文.md').write_text(texts[n],encoding='utf-8')
 (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','source_sha256':sha,'source_lines_and_locations':records[n],'source_corrections_adopted':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
target.write_text('\n\n'.join(texts[n] for n,_,_ in bounds),encoding='utf-8')
renderer=(out.parent/'4.7/检查排版.cjs').read_text(encoding='utf-8').replace('4.7','4.9');(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print('4.9按独立原稿数学行重建完成，保留6→3→4→5→附录的原顺序。')

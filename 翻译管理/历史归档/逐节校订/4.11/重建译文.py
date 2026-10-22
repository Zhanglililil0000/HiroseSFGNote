from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.11 表面坐标系到实验室坐标系的张量旋转.md'
if not (out/'重建前旧译.md').exists():(out/'重建前旧译.md').write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
events=[{'page':1,'y':0,'kind':'prose','text':r'''# 4.11 表面的旋转

> 原作：广瀬千秋；中文翻译：章力。按2页原稿译校；原文件名保留以兼容链接。

## 阅读引导

本节将表面固定$(xyz)$系中的和频张量变换为绕法线旋转后的实验室$(XYZ)$系张量。按八类偏振组合列出全部27个分量，可作为4.7—4.9中面内旋转的查表依据。大写指标表示实验室系，小写指标表示表面系；角度χ与分量符号χ须按有无指标区分。

## 坐标与变换条件

表面固定系的$z$轴取外向法线；$x$轴取无位阻时CH₂或HCCH分子面相互对齐并排列的方向。实验室系由表面系绕$z$轴旋转$\chi$得到。在《变换矩阵(xyz).doc》中令$\phi=0,\theta=0$，得到以下关系。

> **局部约定：** 本节法线向外，与4.8、4.9第2部分的向内法线记法不同。以下严格按本稿原系数、指标和正负号转录，不据相邻稿的取向表改写。
'''}]
data=json.loads((out/'字形行.json').read_text(encoding='utf-8'))
for p,ls in data.items():
 for l in ls:
  s=l['tex'];p=int(p)
  if (p==1 and l['y']<350) or re.search('[ぁ-んァ-ン一-龯]',s):continue
  if chr(92) in s or '=' in s:events.append({'page':p,'y':l['y'],'kind':'math','text':s})
events.sort(key=lambda e:(e['page'],e['y']))
bounds=[(421,1,0),(422,2,0)]
src8=(out.parent/'4.8/重建译文.py').read_text(encoding='utf-8')
exec(src8[src8.index('texts={n:'):src8.index('intro=')].replace('batch=386','batch=421'))
assert sum(bool(re.match(r'^(?:\([ps]{3}\))?\s*\\chi_\{[XYZ]{3}\}',l['tex'])) for ls in data.values() for l in ls)==27
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-11.pdf').read_bytes()).hexdigest()
for n,_,_ in bounds:
 (out/f'B{n}-本批译文.md').write_text(texts[n],encoding='utf-8')
 (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','pages':[n-420],'source_sha256':sha,'source_lines_and_locations':records[n],'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
target.write_text('\n\n'.join(texts.values()),encoding='utf-8')
(out/'检查排版.cjs').write_text((out.parent/'4.7/检查排版.cjs').read_text(encoding='utf-8').replace('4.7','4.11'),encoding='utf-8')
print('4.11两页、八类偏振组合的全部27分量已重建。')

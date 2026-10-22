from pathlib import Path
import json, hashlib, csv, io
r=Path(__file__).resolve().parents[3]; o=Path(__file__).resolve().parent
target=r/'中文版本/第五章 张量与对称性/5.3 从分子固定系到空间固定系的和频张量变换.md'
rec=json.loads((o/'B473验收.json').read_text(encoding='utf-8'))
render=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'))
assert render['math']==29 and all(not x['overs'] for x in render['results'])
assert hashlib.sha256(target.read_text(encoding='utf-8').encode('utf-8')).hexdigest()==rec['translation_sha256']
assert hashlib.sha256((r/'日语原版/Chapter5/chap5-3.pdf').read_bytes()).hexdigest()==rec['source_sha256']
assert len(json.loads((o/'B473-覆盖.json').read_text(encoding='utf-8')))==13
rec.update({'已排版':True,'数学片段数':29,'截图目视检查':True,'横向溢出':False,'检查说明':'标题、目录、三条独立式、角度定义及疑点注释显示正常；不代表独立物理推导验证。'})
(o/'B473验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
p=o/'B473.md'; p.write_text(p.read_text(encoding='utf-8')+'\n排版验收：29个数学片段通过语法检查，已目视核对整页截图，标题、表格及角度公式显示正常，无横向溢出。B473完成；5.3全节仍在翻译中。\n',encoding='utf-8')
p=r/'翻译管理/章节清单.tsv'; reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
for row in rows:
 if row['编号']=='5.3': row['状态']='翻译中：B473完成p1/16原页对照及排版；p2起待译'
s=io.StringIO(newline=''); w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows); p.write_bytes(s.getvalue().encode('utf-8'))
link='[5.3 从分子固定系到空间固定系的和频张量变换](中文版本/第五章%20张量与对称性/5.3%20从分子固定系到空间固定系的和频张量变换.md)'
p=r/'Preface序言.md'; t=p.read_text(encoding='utf-8'); lines=t.splitlines()
for i,line in enumerate(lines):
 if line.startswith('- 5.3 '): lines[i]='- '+link+'（翻译中，p1/16已译校）：先确认张量前两指标互换的适用条件及三个取向角。本节Z轴指向基板内部；p2起分量展开待译。'
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
p=r/'中文版本/第五章 张量与对称性/阅读导航.md'; t=p.read_text(encoding='utf-8').replace('本章5.1—5.2已完成本轮译校及排版；5.3—5.6尚未开始，全章尚未完成。','本章5.1—5.2已完成本轮译校及排版；5.3已完成p1/16，5.4—5.6尚未开始，全章尚未完成。').replace('- 5.3 从分子固定坐标系到空间固定坐标系：待翻译。','- [5.3 从分子固定系到空间固定系的和频张量变换](5.3%20从分子固定系到空间固定系的和频张量变换.md)：p1/16已译校。先读β前两指标对称的适用条件、坐标系及三个角的定义；Z向内。p2起分量展开待译。').replace('下一节5.3，共16页，尚未开始。','5.3共16页，目前首页已译校；后续分量展开待译。')
p.write_text(t,encoding='utf-8')
p=r/'翻译管理/符号与约定.md'; t=p.read_text(encoding='utf-8'); t+='\n\n## 5.3首页局部约定（B473）\n\n分子系abc、空间系XYZ；原文另称分子固定xyz，依Q221保留。Z指向基板内部，外法线为−Z；θ=π−θtilt，χ=π/2+χip。φ为内部旋转角；原文ab面及绕c旋转的几何疑点依Q222保留。N轴方向本页未定义，不自行补足。φ与χip随机均匀的条件分别成立，不互相推定。β为一阶超极化率，对应二阶场响应；前两指标可互换是本稿适用条件。详见校订记录/5.3/局部约定卡.md。\n'; p.write_text(t,encoding='utf-8')
p=r/'翻译管理/当前进度与续接.md'; t=p.read_text(encoding='utf-8'); t=t.replace('## 当前有效状态：5.2全节完成','## 历史状态：5.2全节完成',1)
new='## 当前有效状态：5.3首页完成，B473验收通过（2026-10-21）\n\n5.3《从分子固定系到空间固定系的和频张量变换》已完成p1/16原目录及第1—3部分，共13个覆盖单元、3条独立无编号式；29个数学片段通过语法和参考排版检查，截图已目视检查，无横向溢出。Q221（abc/xyz记号）与Q222（ab面及绕c旋转几何）保留原文并就地说明，未采用原文修正。章节清单、序言、导航及符号约定已同步。\n\n下一批B474：从PDF p2第4部分引言、分子张量非零/相等关系及c轴振动组首个完整空间分量式开始。p2—p3的ZXX跨页公式必须完整处理，不能截断；未完成的后续公式不计入覆盖。5.3全节尚未完成。\n\n'
t=t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+new,1); p.write_text(t,encoding='utf-8')
checks={'批次':'B473','底本摘要匹配':True,'译文摘要匹配':True,'覆盖单元':13,'数学片段':29,'排版目视通过':True,'5.3全节完成':False,'下一批':'B474','采用原文修正':False}
assert target.exists() and (r/'中文版本/第五章 张量与对称性/阅读导航.md').exists()
(o/'B473最终检查.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print('B473验收及管理更新完成。')

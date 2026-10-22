from pathlib import Path
import json,csv,io,hashlib
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
src=r/'日语原版/Chapter5/chap5-3.pdf';target=r/'中文版本/第五章 张量与对称性/5.3 从分子固定系到空间固定系的和频张量变换.md';t=target.read_text(encoding='utf-8')
(o/'B473-本批译文.md').write_text(t,encoding='utf-8')
units=[('原题及目录','四项标题及原页码'),('第1部分第1段','分子到空间变换及前两指标交换适用条件'),('第1部分第2段','拉曼部分实且对称、非共振语境及三个例外'),('第2部分第1—2项','abc分子系、XYZ空间系'),('第2部分第3项','xyz记号与欧拉角重合方向，Q221'),('欧拉角引言','χ/θ/φ顺序'),('内部旋转角第1段','ab面、c轴、−Z投影及内积取正'),('内部旋转角第2段','四个零/正交角条件及φ随机均匀权重，Q222'),('倾斜角段','c与外法线、N轴及正旋转方向'),('倾斜角末','θ=π−θtilt'),('面内取向角段','缩写、Z旋转、投影和正方向'),('面内角末','Z向内、χ=π/2+χip及独立随机条件'),('第3部分','沿三轴分组及多轴分量警示')]
cov=[{'原文定位':'PDF p1 / '+a,'对象':b,'译文定位':a,'已翻译':True,'已原页对照':True} for a,b in units]
(o/'B473-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
rec={'批次':'B473','范围':'PDF p1全页，原题及目录至第3部分末','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'translation_sha256':hashlib.sha256(t.encode('utf-8')).hexdigest(),'覆盖单元':len(cov),'独立无编号式':3,'图':0,'已起草':True,'已原页对照':True,'已排版':False,'疑点':['Q221','Q222'],'采用原文修正':False,'下一批':'B474，p2第4部分引言/分子分量关系及首个完整c轴组空间分量式'}
(o/'B473验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B473.md').write_text('# B473｜5.3 PDF p1\n\n2026-10-21。13个覆盖单元，含原目录四行、第1—3部分及全部括注，三条独立无编号式；无图、无脚注或独立书目。已对照β前两指标互换、三类例外、三个角及随机条件的主语和限定。\n\nQ221保留xyz，Q222保留ab面，不补N轴方向；Z向内、−Z向外已单独登记。章节标题按本底本原题采用完整的和频张量变换题名。后续公式未计完成；下一批B474。数学显示状态另见验收记录。\n',encoding='utf-8')
p=r/'翻译管理/疑难与勘误.md';old=p.read_text(encoding='utf-8')
for q,desc in [('Q221','5.3 p1第2部分前两项定义分子系abc、空间系XYZ，第3项却写“分子固定xyz”。p2缓存的第4部分引言亦如此。本批保留xyz，不改作abc，也不自行新增表面坐标系。两种记号对应待核。'),('Q222','5.3 p1内部旋转角φ定义多次写ab面，并称绕c使该面垂直表面。通常正交坐标下绕c不改变ab面的方向，面名与几何关系待核。保留各处ab，不采用ac/bc等候选替换，不改零角条件。')]:
 if '## '+q+'｜' not in old:old+='\n\n## '+q+'｜5.3首页约定疑点\n\n'+desc+'\n\n状态：原文保留、待核验，未采用原文修正。来源：B473。\n'
p.write_text(old,encoding='utf-8')
renderer=(r/'翻译管理/校订记录/5.2/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/5.2','校订记录/5.3').replace("startsWith('5.2 ')","startsWith('5.3 ')")
(o/'检查排版.cjs').write_text(renderer,encoding='utf-8')
p=r/'翻译管理/章节清单.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['编号']=='5.3':
  assert row['原文SHA256']==rec['source_sha256']
  row.update({'暂定中文标题':'从分子固定系到空间固定系的和频张量变换','现有译文路径':target.relative_to(r).as_posix(),'状态':'翻译中：B473已完成p1原页对照，排版待验收','映射核验':'原题、目录及第1—3部分已原页核对；第4部分待译校','公式图表范围':'p1三条无编号独立关系式及角度条件；p2起分量表待逐式登记','导读状态':'临时导读；p1已核','导读草案':'先限定β前两指标可互换的适用范围，定义分子/空间坐标和φ、θtilt、χip；Z向内。后续按c/a/b轴振动列张量展开，尚待逐式核验。'})
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
print('B473登记，底本16页摘要匹配；等待排版。')

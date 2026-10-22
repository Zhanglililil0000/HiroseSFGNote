from pathlib import Path
import re
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B083-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes())
start=s.index('![式（4.19）—（4.21）');end=s.index('再考虑 $A_n$',start)
old=s[start:end];new=(out/'B083-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B083-原式图对照.md').write_text('# B083原式图对照\n\n底本2.2 PDF p8上半部，B类源点。\n\n'+old,encoding='utf-8')
s=s[:start]+new+s[end:]
old_note='4.1g的B点小标题使用 $2(n+1)h_m-z$，但式（4.19）—（4.21）中的相位使用 $2n+1$；4.2e及5.2e标题的B点坐标也使用后者。这里分别照录，尚不统一改写。'
new_note='4.1g的B点小标题使用 $2(n+1)h_m-z$；高清复核确认式（4.19）、（4.20）的整体相位同样使用 $2(n+1)$，而式（4.21）使用 $2n+1$。4.2e及5.2e标题的B点坐标也使用后者。这里分别照录，尚不统一改写（B083细化原注）。'
assert old_note in s;s=s.replace(old_note,new_note,1)
s=s.replace('式（4.10）—（4.18）已在B082转为可编辑数学；','式（4.10）—（4.21）已在B082—B083转为可编辑数学；',1)
p.write_text(s,encoding='utf-8')
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s+='''
## 第2.2节B类源点公式转写续记（B083，2026-10-19）

Q044细化：PDF p8高清原页显示，4.19/4.20整体相位写2(n+1)，4.21却写2n+1。此前正文注释曾将三式概称为2n+1，本次纠正该译校说明；原式均分别照录，并未修改作者公式。既有B点坐标差异继续保留。未新增疑难编号、未新增采用原文修正或勘误附件条目。
''';p.write_text(s,encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B083：B类源点公式\n\n4.19/4.20整体相位为−i·2(n+1)·k h_m tanθ_SF sinθ，4.21整体相位为−i·(2n+1)·h_m tanθ_SF(两激发光切向波矢之和)，不强行统一。乘积保留四个展开项及各自的r、往返相位和z相位；Q044旧概括已细化。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8');s=s.replace('数学转写已推进至式（4.18）','数学转写已推进至式（4.21）');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B083完成2.2式（4.19）—（4.21）可编辑转写（2026-10-19）

已转写4.1g的B类源点三式，替换正文一幅公式影像，保留全部四个乘积展开项与原编号。高清复核将Q044说明细化为：4.19/4.20整体相位2(n+1)，4.21整体相位2n+1；原式分别照录，不统一改写。未新增原文采用修正，勘误附件无新增。

下一批B084：A类源点式（4.22）—（4.24），注意4.24的编号在p9页首。2.2的文字已补齐，复杂公式可编辑转写继续分批；本轮未进入2.3。勿重跑历史B069—B081合入/生成脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B083.md').write_text('''# B083：4.1g的B类源点可编辑公式

日期：2026-10-19。底本：2.2 PDF p8上半部。范围：4.19—4.21完整公式组，不进入A类源点。

| 定位 | 对象 | 已转写 | 已对照 | 备注 |
|---|---|---|---|---|
| p8，4.19 | 可见光场 | 是 | 高清原式图及原页 | 2(n+1)整体相位，两项z相位 |
| p8，4.20 | 红外光场 | 是 | 同上 | 2(n+1)整体相位，两项z相位 |
| p8，4.21 | 两激发场乘积 | 是 | 同上 | 2n+1整体相位，四项逐一保留 |

核对字段：vis/ir与α/β、r/t界面方向、往返指数2iβh、z相位的正负号与1±tanθ_SF tanθ、四项反射权重及原编号。为排版在指数和内断行，没有引入辅助记号或代数化简。高清复核细化Q044的旧概括，未把候选修正用于原式。原图保留于B083-原式图对照.md，原正文备份B083-修订前.md。

排版及范围验收见B083验收.json。后续从A类源点4.22—4.24开始；历史批次草稿不覆盖现正文。
''',encoding='utf-8')
print('B083 merged; 3 equations; Q044 clarified')

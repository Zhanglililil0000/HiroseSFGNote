from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B089-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（4.28b）：');b=s.index('> **译校注（Q046，',a)
old=s[a:b];new=(out/'B089-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B089-原式图对照.md').write_text('# B089原式图对照\n\n底本2.2 PDF p10：4.28b及其后无编号可见光场。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
old_status='式（4.10）—（4.28a）及4.26b前的无编号场乘积已在B082—B088推进可编辑数学转写'
new_status='式（4.10）—（4.28b）及4.26b前、4.28b后的无编号式已在B082—B089推进可编辑数学转写'
assert old_status in s;s=s.replace(old_status,new_status,1);p.write_text(s,encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'''\n## B089：背面极化膜及无编号场式\n\n4.28b使用m″层的t_mm″、r_mm″和r_m″2，传播相位仍用β_m与h_m。其后无编号式按原文使用m′、t_1m′、t_m′m、r_m′m、β_m′与h_m′，不据段落主题改成m″或m。Q046保留；两式不合并为同一层模型。\n''',encoding='utf-8')
p=m/'疑难与勘误.md';p.write_text(p.read_text(encoding='utf-8')+'''\n## 第2.2节背面极化膜分支转写续记（B089，2026-10-19）\n\nQ046续：p10的4.28b按m″转写，其后无编号场式确实沿用m′层记号，包含β_m′、h_m′及t_1m′、t_m′m、r_m′m。分别照录，没有按段落主题全改成m″。既有就地说明保持，无新增问题号或原文采用修正，勘误附件无新增。\n''',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.28a），含4.26b前的无编号场乘积','数学转写已推进至式（4.28b），含4.26b前及4.28b后的无编号式');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B089完成2.2背面极化膜分支（2026-10-19）

已转写4.28b及其后无编号可见光场式，替换正文两幅影像。4.28b按m″层、无编号式按原有m′层与β_m′/h_m′分别照录，保留Q046就地说明，不将不同层记号机械统一。无新增问题号、原文采用修正或勘误附件条目。

下一批B090：4.2d式4.29，继而按B/A两类分别推进4.30a/b。2.2复杂公式转写尚未全部完成，未进入2.3。渲染脚本后续批次需覆盖B090及以上；勿用历史合入/生成脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B089.md').write_text('''# B089：完整背面极化膜分支

日期：2026-10-19。底本2.2 PDF p10，完整4.28b及其后无编号场式；止于Q046说明之前，原说明保持。

| 定位 | 对象 | 已转写 | 已对照 | 核对要点 |
|---|---|---|---|---|
| p10，4.28b | m″极化层与n=0关系 | 是 | 高清原式图及原页 | χ求和、两分式、t_mm″/r_mm″/r_m″2、β_m和h_m |
| p10，紧接4.28b后 | 无编号可见光场 | 是 | 高清原式图 | m′层、两透射因子、β_m′与h_m′、无位移相位 |

仅断行，无辅助记号或代数替换。各m′/m″记号按底本保留，Q046继续未决；无新增原文修正及勘误附件条目。原图及旧全文备份保留。验收见B089验收.json。下一批4.29。
''',encoding='utf-8')
print('B089 merged; 4.28b and unnumbered field; Q046 retained')

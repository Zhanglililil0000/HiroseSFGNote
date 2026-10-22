from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B086-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（4.26b）之前');b=s.index('#### 4.2b.',a)
old=s[a:b];new=(out/'B086-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B086-原式图对照.md').write_text('# B086原式图对照\n\n底本2.2 PDF p9：无编号场乘积与4.26b。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
s=s.replace('式（4.10）—（4.26a）已在B082—B085推进可编辑数学转写（4.25原已有数学格式）；','式（4.10）—（4.26b）及其前的无编号场乘积已在B082—B086推进可编辑数学转写（4.25原已有数学格式）；',1)
wrong='4.26b前的电场乘积左端也使用 $h_m$。'
correct="4.26b前的电场乘积左端使用 $h_{m'}$（B086高清复核；更正此前说明中的 $h_m$）。"
assert wrong in s;s=s.replace(wrong,correct,1);p.write_text(s,encoding='utf-8')
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8')
s=s.replace('| 位置h_m和m′标签与对应界面/极化层名称不一致 |', '| 位置h_m′和m′标签与对应界面/极化层名称不一致（h_m′为B086复核结果） |',1)
s+='''
## 第2.2节完整表面膜公式转写续记（B086，2026-10-19）

Q046细化：p9无编号电场乘积左端的两处自变量经六倍渲染确认是h_m′，此前译校说明误记h_m，本次更正该说明与问题表，并按底本转写h_m′。此为译者原记号识别记录的修复，不是更改作者原式。其与z=0−的对应关系仍未决；p10的m′/m″标签疑点继续保留。无新增问题号，无新增原文采用修正或勘误附件条目。
''';p.write_text(s,encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'''\n## B086：完整表面膜极化\n\n无编号场乘积使用α/β坐标指标，4.26b极化使用χ_αβγ及β/γ求和。区分薄层m′与主体膜m：t_1m′、r_m′m、r_1m′、r_m2分别保留，传播参数和厚度仍属m。无编号式左端为h_m′，Q046已修复旧识别说明；4.26b首行P(0−)不擅补n，末行保留n=0。\n''',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.26a）','数学转写已推进至式（4.26b），含前置无编号场乘积');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B086完成2.2完整表面膜分支（2026-10-19）

已转写4.2a中4.26b前的无编号电场乘积与4.26b（含n=0关系），替换正文两幅影像。高清复核修复Q046旧说明：无编号式左端为h_m′，不是h_m；公式按底本保留，不据z=0−改写。无新增问题号、原文采用修正或勘误附件条目。

下一批B087：4.2b式4.27，保留原引用4.13及Q045候选说明；随后按4.2c处理4.28a/b及其后无编号式。2.2复杂公式可编辑转写尚未完成，未进入2.3。勿运行历史合入/生成脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B086.md').write_text('''# B086：4.2a完整表面薄膜分支

日期：2026-10-19。底本2.2 PDF p9。范围从4.26b前无编号场乘积至4.26b末；止于4.2b之前。

| 定位 | 对象 | 已转写 | 已对照 | 核对项 |
|---|---|---|---|---|
| p9，4.26b前 | 无编号电场乘积 | 是 | 原高清图及六倍左端图 | h_m′、α/β、两场分式、m′/m、相位 |
| p9，4.26b | 界面极化与n=0关系 | 是 | 原高清图及原页 | χ与β/γ求和、两个分母、P标签、相位和原编号 |

只断行，无辅助因子、无代数改写。Q046旧说明误认h_m，本次按高清原字修复为h_m′；不是采用作者公式候选修正。原图及正文备份保留。下一批4.27，原引用与Q045不改。验收见B086验收.json。
''',encoding='utf-8')
print('B086 merged; unnumbered product and 4.26b; Q046 clarified')

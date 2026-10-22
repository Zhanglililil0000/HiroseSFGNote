from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B087-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（4.27）：');b=s.index('> **译校注（Q045，',a)
old=s[a:b];new=(out/'B087-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B087-原式图对照.md').write_text('# B087原式图对照\n\n底本2.2 PDF p10页首；4.2b界面薄膜侧极化。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
old_status='式（4.10）—（4.26b）及其前的无编号场乘积已在B082—B086推进可编辑数学转写'
new_status='式（4.10）—（4.27）及4.26b前的无编号场乘积已在B082—B087推进可编辑数学转写'
assert old_status in s;s=s.replace(old_status,new_status,1);p.write_text(s,encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B087：前界面薄膜侧极化\n\n4.27的首行P(0+)与末行P(0+,n=0)均按原记号；β/γ为两激发光坐标求和指标。r/t均不含m′层，两个分子(1+r)及两个往返分母分开保留，六倍局部核对指数中的i。原引4.13及Q045候选4.12不变，未采用引用修正。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.26b），含前置无编号场乘积','数学转写已推进至式（4.27），含4.26b前的无编号场乘积');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B087完成2.2式（4.27）可编辑转写（2026-10-19）

已转写4.2b前界面薄膜侧极化，替换正文一幅影像。核对χ的β/γ求和、t_1m场幅、两个(1+r)因子、两个往返分母、相位及n=0关系；指数i经六倍局部图复核。原文引用4.13和Q045候选说明保持不变。无新增疑难、原文采用修正或勘误附件条目。

下一批B088：4.2c式4.28a，之后另按完整极化膜分支处理4.28b及其后无编号式，保留Q046的m′/m″疑点。2.2复杂公式转写尚未全部完成；不进入2.3。勿用历史脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B087.md').write_text('''# B087：4.2b前界面薄膜侧极化

日期：2026-10-19。底本2.2 PDF p10页首；完整式4.27，不进入4.2c。

| 定位 | 对象 | 已转写 | 已对照 | 核对要点 |
|---|---|---|---|---|
| p10，4.27展开 | 二阶极化 | 是 | 高清原式及六倍指数局部 | χ、β/γ求和、两个E0、两个t、分子分母及i |
| p10，4.27末行 | n=0关系 | 是 | 高清原式 | 0+侧别、相同位移相位与原编号 |

仅断行，无辅助记号或代数改写。正文引4.13与Q045候选4.12说明保持，未擅改引用；无新增疑难或勘误附件条目。原图与旧全文备份保留。验收见B087验收.json。下一批4.28a。
''',encoding='utf-8')
print('B087 merged; 4.27; Q045 unchanged')

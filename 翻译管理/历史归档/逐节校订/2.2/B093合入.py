from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B093-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（5.1a）—（5.2c）');b=s.index('介质2与薄膜 $m$ 之间',a)
old=s[a:b];new=(out/'B093-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B093-原式图对照.md').write_text('# B093原式图对照\n\n底本2.2 PDF p12，1/m界面的六个L系数；z分量另见高清局部图。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
marker='（4.25原已有数学格式）；'
assert marker in s;s=s.replace(marker,'（4.25原已有数学格式）；第5部分已转写至式（5.2c）；',1);p.write_text(s,encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B093：1/m界面L系数\n\n5.1a—c为L−，5.2a—c为L+；p,x和p,z的分母交叉搭配介质折射率与对侧角度，s,y分母为各介质自身角度。z分量保留m′薄片折射率、原式两种表示及比值平方；L+的z分量两式均带负号。公共因子仍依5.1引言省略，不补入。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已完成第4部分至式（4.30b）','数学转写已完成第4部分，并推进至式（5.2c）');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B093完成1/m界面L系数转写（2026-10-19）

已转写5.1a—5.2c六个L系数，替换正文一幅影像；按两个出射方向核对p,x、s,y、p,z。保留不同分母的角度搭配、m′层折射率、z分量两种表示与平方比，以及L+的z分量负号。无新增疑难、原文采用修正或勘误附件条目。

下一批B094：5.1中m/2界面极化薄片的5.3a—5.4c，仍按两个出射方向和三个坐标分量成组处理。第4部分数学转写已完成，第5部分及附录继续分批；未进入2.3。勿用历史脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B093.md').write_text('''# B093：1/m界面极化薄片的L系数

日期：2026-10-19。底本2.2 PDF p12，5.1a—5.2c；不进入m/2界面系数。

| 定位 | 对象 | 已转写 | 已对照 | 核对要点 |
|---|---|---|---|---|
| p12，5.1a—c | L−三个分量 | 是 | 高清原图/原页 | x/s分母角度不同、z的m′角及平方比 |
| p12，5.2a—c | L+三个分量 | 是 | 高清原图/z分量局部 | x分子为θ1、z两行均负号、n1/n_m′及平方 |

六式各保留原编号，z分量两种表达式均完整转写；未定义辅助分母，未作代数替换。沿用5.1引言省略公共因子的原约定。无新增疑难或原式修正，勘误附件无新增。原图及备份保留；验收见B093验收.json。下一批5.3a—5.4c。
''',encoding='utf-8')
print('B093 merged; six L coefficients; no new issues')

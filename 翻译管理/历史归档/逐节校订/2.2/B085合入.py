from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B085-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（4.26a）');b=s.index('如果表面已经形成完整薄膜',a)
old=s[a:b];new=(out/'B085-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B085-原式图对照.md').write_text('# B085原式图对照\n\n底本2.2 PDF p9，4.2a稀疏或突出表面分子的极化。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
s=s.replace('式（4.10）—（4.24）已在B082—B084转为可编辑数学；','式（4.10）—（4.26a）已在B082—B085推进可编辑数学转写（4.25原已有数学格式）；',1)
p.write_text(s,encoding='utf-8')
p=m/'疑难与勘误.md';p.write_text(p.read_text(encoding='utf-8')+'''
## 第2.2节界面极化公式转写续记（B085，2026-10-19）

| 编号 | 原文位置 | 疑点 | 类别/优先级 | 处理与状态 |
|---|---|---|---|---|
| Q061 | 2.2 PDF p9，式4.26a两行相位式末 | 两处右花括号未见配对的左花括号 | 原式括号/P2 | 保留两个原有右花括号，候选删除未采用；未新增原文修正或勘误附件条目。 |
''',encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B085：4.26a界面极化\n\nχ下标为SF/vis/ir的α/β/γ；β、γ为场坐标指标，β_m,vis/ir为传播参数。对β、γ求和，保留n与n=0两种P标签及相同位移相位。两处原有右花括号照录，Q061；未删符号。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.24）','数学转写已推进至式（4.26a）').replace('Q039—Q060尚有未决项','Q039—Q061尚有未决项');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B085完成2.2式（4.26a）可编辑转写（2026-10-19）

已转写4.2a中稀疏或突出表面分子的极化，替换正文一幅影像。核对χ的β/γ求和、四个(1+r)因子、两个多重反射分母、位移相位和n=0关系。新增Q061：两行末原有未配对右花括号均保留，未删符号；未采用原文修正，勘误附件无新增。

下一批B086：同一4.2a中“如果表面已经形成完整薄膜”之后的无编号电场乘积与4.26b，完整处理这一分支。2.2文字已补齐，复杂公式转写尚未完成；不进入2.3。历史合入/生成脚本不覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B085.md').write_text('''# B085：4.2a稀疏表面分子的极化

日期：2026-10-19。底本2.2 PDF p9，式4.26a；范围止于该式及就地注，完整表面膜分支留待B086。

| 定位 | 对象 | 已转写 | 已对照 | 核对项 |
|---|---|---|---|---|
| p9，4.26a第一等式 | 界面极化展开 | 是 | 原页及高清公式图 | χ的β/γ求和、E0、四个1+r与两个分母、i·2n相位 |
| p9，4.26a第二等式 | n=0关系 | 是 | 同上 | P(0−,n=0)、相同位移相位、原编号 |

仅作断行和可编辑转写，无代数化简、无辅助因子定义。两处未配对右花括号按底本保留，Q061，不将其作为译者排版错误静默删除。原图及旧全文备份保留。显示与范围验收见B085验收.json。下一批处理完整膜的无编号场乘积与4.26b。
''',encoding='utf-8')
print('B085 merged; 4.26a; Q061 retained')

from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B091-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（4.30a）：');b=s.index('由式（4.24），得到A类源点',a)
old=s[a:b];new=(out/'B091-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B091-原式图对照.md').write_text('# B091原式图对照\n\n底本2.2 PDF p11，4.30a；首部另见B091-首部局部.png。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
old_status='式（4.10）—（4.29）及4.26b前、4.28b后的无编号式已在B082—B090推进可编辑数学转写'
new_status='式（4.10）—（4.30a）及4.26b前、4.28b后的无编号式已在B082—B091推进可编辑数学转写'
assert old_status in s;s=s.replace(old_status,new_status,1);p.write_text(s,encoding='utf-8')
p=m/'疑难与勘误.md';p.write_text(p.read_text(encoding='utf-8')+'''
## 第2.2节B类体相极化转写续记（B091，2026-10-19）

| 编号 | 原文位置 | 疑点 | 类别/优先级 | 处理与状态 |
|---|---|---|---|---|
| Q064 | 2.2 PDF p11，4.30a分母与整体相位 | 两分母β的vis/ir与各自反射系数标签相反；首相位不含n，四项后另乘含n相位 | 原式频率/相位/P1 | 六倍首部与全式复核后逐项照录；与4.21及零阶定义的衔接未决，不换标签、不补n、不删或合并相位。无原文采用修正，勘误附件无新增。 |
''',encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B091：B类体相极化\n\n4.30a保留P(z)及末行P(z,n=0)、χ的β/γ求和；分母传播参数vis/ir交叉、首部不含n相位及四项后的含n相位按原文保留，Q064。四项z相位的1±tanθ_SF tanθ和反射权重逐项转写，不由4.21自动生成或统一。Q044坐标差异仍未决。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.29）','数学转写已推进至式（4.30a）').replace('Q039—Q063尚有未决项','Q039—Q064尚有未决项');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B091完成2.2式（4.30a）可编辑转写（2026-10-19）

已转写4.2e的B类体相极化，替换正文一幅影像，保留四项展开、全部相位与n=0关系。新增Q064：两分母传播参数的频率标签交叉；首部相位不含n，四项后另有含n相位。经六倍首部与高清全式确认，分别照录，未按4.21重排。无原文采用修正，勘误附件无新增。

下一批B092：A类体相极化4.30b，按原式独立核对，不把B类改符号后直接套用。之后进入5.1的L系数可编辑转写。2.2复杂公式转写尚未全部完成，未进入2.3；勿用历史脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B091.md').write_text('''# B091：4.2e的B类体相极化

日期：2026-10-19。底本2.2 PDF p11上半部，完整4.30a；不进入4.30b。

| 定位 | 对象 | 已转写 | 已对照 | 核对要点 |
|---|---|---|---|---|
| p11首部 | χ求和与公共因子 | 是 | 高清全式、六倍首部 | E0、t、两分母交叉频率、首部无n相位 |
| p11中部 | 四项z相位展开 | 是 | 高清全式 | 权重1/r_ir/r_vis/r_vis r_ir、各β与1±tan角项 |
| p11末部 | 外乘相位及零阶关系 | 是 | 高清全式 | 额外含n相位、P(z,n=0)和原编号 |

仅断行，无辅助记号或代数化简。所有相位及交叉频率按底本保留，Q064；未采用修正、无新增勘误附件条目。原图与旧全文备份保留。验收见B091验收.json。下一批4.30b独立核对。
''',encoding='utf-8')
print('B091 merged; 4.30a; Q064 retained')

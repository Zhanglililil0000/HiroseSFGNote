from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B090-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（4.29）：');b=s.index('#### 4.2e.',a)
old=s[a:b];new=(out/'B090-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B090-原式图对照.md').write_text('# B090原式图对照\n\n底本2.2 PDF p10，式4.29；首行另见B090-首行局部.png。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
old_status='式（4.10）—（4.28b）及4.26b前、4.28b后的无编号式已在B082—B089推进可编辑数学转写'
new_status='式（4.10）—（4.29）及4.26b前、4.28b后的无编号式已在B082—B090推进可编辑数学转写'
assert old_status in s;s=s.replace(old_status,new_status,1);p.write_text(s,encoding='utf-8')
p=m/'疑难与勘误.md';p.write_text(p.read_text(encoding='utf-8')+'''
## 第2.2节背界面薄膜侧公式转写续记（B090，2026-10-19）

| 编号 | 原文位置 | 疑点 | 类别/优先级 | 处理与状态 |
|---|---|---|---|---|
| Q063 | 2.2 PDF p10，式4.29首行分式前 | 两束E0之后另有无指数e | 原式因子/P1 | 六倍局部确认，作为原有独立因子照录；是否排版遗留未决，不删除或补指数。无新增原文采用修正或勘误附件条目。 |
''',encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B090：背界面薄膜侧极化\n\n4.29使用h_m−侧别，两个t_1m与两个(1+r_m2)因子；分子传播相位i(β_m,ir+β_m,vis)h_m、展开式i(2n+1)及相对n=0的i·2n分别保留。首行无指数e按原因子照录，Q063；不解释或补写其物理含义。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.28b）','数学转写已推进至式（4.29）').replace('Q039—Q062尚有未决项','Q039—Q063尚有未决项');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B090完成2.2式（4.29）可编辑转写（2026-10-19）

已转写4.2d背界面薄膜侧极化，替换正文一幅影像。新增Q063：首行E0之后、分式之前有一个无指数e，六倍局部确认后作为原有独立因子照录，不删、不补指数。相位、h_m−及n=0关系均按原式保留。无原文采用修正或勘误附件新增。

下一批B091：4.2e的B类体相极化4.30a，之后另组处理A类4.30b；注意Q044坐标/相位差异及原式逐行结构。2.2复杂公式转写尚未全部完成，未进入2.3。渲染脚本已支持B090及后续三位批号；勿用历史合入/生成脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B090.md').write_text('''# B090：4.2d背界面薄膜侧极化

日期：2026-10-19。底本2.2 PDF p10，完整式4.29；不进入4.2e。

| 定位 | 对象 | 已转写 | 已对照 | 核对项 |
|---|---|---|---|---|
| p10，4.29首式 | 薄膜侧极化展开 | 是 | 高清原式及六倍首行局部 | χ求和、E0后无指数e、两个t、两个1+r、分母及相位 |
| p10，4.29末式 | n=0关系 | 是 | 高清原式 | h_m−、i·2n位移相位、原编号 |

仅断行，无辅助记号或代数替换。无指数e原样保留并登记Q063，未采用候选修正；无新增勘误附件条目。原图及全文备份保留，验收见B090验收.json。下一批4.30a。
''',encoding='utf-8')
print('B090 merged; 4.29; Q063 retained')

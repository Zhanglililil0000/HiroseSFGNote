from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B088-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（4.28a）：');b=s.index("当薄膜 $m''$",a)
old=s[a:b];new=(out/'B088-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B088-原式图对照.md').write_text('# B088原式图对照\n\n底本2.2 PDF p10，式4.28a。下标另见B088-分母局部.png。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
old_status='式（4.10）—（4.27）及4.26b前的无编号场乘积已在B082—B087推进可编辑数学转写'
new_status='式（4.10）—（4.28a）及4.26b前的无编号场乘积已在B082—B088推进可编辑数学转写'
assert old_status in s;s=s.replace(old_status,new_status,1);p.write_text(s,encoding='utf-8')
p=m/'疑难与勘误.md';p.write_text(p.read_text(encoding='utf-8')+'''
## 第2.2节背界面外侧公式转写续记（B088，2026-10-19）

| 编号 | 原文位置 | 疑点 | 类别/优先级 | 处理与状态 |
|---|---|---|---|---|
| Q062 | 2.2 PDF p10，式4.28a可见光分母 | r_m2的频率下标写wvis，多一字母w | 原式下标/P2 | 六倍局部图确认，正文照录wvis；候选vis仅入注，未采用。无新增原文修正或勘误附件条目。 |
''',encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B088：背界面介质2侧极化\n\n4.28a位于h_m+。保留四个t系数、分子i(β_m,ir+β_m,vis)h_m以及两种n相位：展开式i(2n+1)，相对n=0因子2in。可见光分母r_m2,wvis,β按原下标照录，Q062，未统一改为vis。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.27）','数学转写已推进至式（4.28a）').replace('Q039—Q061尚有未决项','Q039—Q062尚有未决项');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B088完成2.2式（4.28a）可编辑转写（2026-10-19）

已转写4.2c突出于背面的分子极化，替换正文一幅影像，保留四个透射因子、分子相位与n=0关系。新增Q062：可见光分母一处原下标wvis经六倍局部确认，正文照录，候选vis仅注。未采用原文修正，勘误附件无新增。

下一批B089：同一4.2c的完整背面极化膜分支，式4.28b及其后无编号可见光电场式；保留Q046的m′/m″标签疑点。2.2复杂公式转写尚未全部完成，未进入2.3。勿用历史脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B088.md').write_text('''# B088：4.2c背界面介质2侧极化

日期：2026-10-19。底本2.2 PDF p10，完整式4.28a；止于完整背面极化膜分支之前。

| 定位 | 对象 | 已转写 | 已对照 | 核对要点 |
|---|---|---|---|---|
| p10，4.28a展开 | 介质2侧分子极化 | 是 | 高清原式及六倍分母局部 | χ与β/γ求和、四个t、分子相位、两个往返分母 |
| p10，4.28a末行 | n=0关系 | 是 | 高清原式 | h_m+侧别、2in相位及原编号 |

仅断行，无代数替换。六倍局部确认原下标wvis，照录并登记Q062，未采用候选vis；无新增勘误附件条目。原图及全文备份保留。显示与范围验收见B088验收.json。下一批4.28b及其后无编号式。
''',encoding='utf-8')
print('B088 merged; 4.28a; Q062 retained')

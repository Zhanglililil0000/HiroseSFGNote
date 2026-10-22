from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
target=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=target.read_text(encoding='utf-8');backup=out/'B082-修订前.md'
assert not backup.exists(),'One-time mutation: do not rerun'
backup.write_bytes(target.read_bytes())
start=s.index('#### 4.1d.');end=s.index('#### 4.1g.',start)
old=s[start:end];new=(out/'B082-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B082-原式图对照.md').write_text('# B082原式图对照（PDF p7）\n\n'+old,encoding='utf-8')
s=s[:start]+new+s[end:]
s=s.replace('4.1d以后复杂公式采用底本高清影像，保留全部推导和原编号；可编辑数学转写尚待后续专项处理。','式（4.10）—（4.18）已在B082转为可编辑数学；其余复杂长式仍保留底本高清影像与原编号，可编辑转写继续分批进行。')
assert s[s.index('#### 4.1g.'):]==backup.read_text(encoding='utf-8')[end:]
assert all(s.count(r'\tag{4.'+str(n)+'}')==1 for n in range(10,19))
assert not re.search(r'B069-p07-0[123]\.png',s)
target.write_text(s,encoding='utf-8')
p=m/'疑难与勘误.md';q=p.read_text(encoding='utf-8')
q+='''
## 第2.2节公式转写续记（B082，2026-10-19）

| 编号 | 原文位置 | 疑点 | 类别/优先级 | 处理与状态 |
|---|---|---|---|---|
| Q059 | 2.2 PDF p7，式（4.17）分子 | 指数为β_m,ir h_m，未写i；与4.16及4.18的相位形式不同 | 原式相位/P1 | 原式无i照录；候选补i仅列就地注，未确认、未采用。原图保留于B082对照记录；不是译者漏转。 |
'''
p.write_text(q,encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B082：4.1d—4.1f可编辑公式\n\n4.10—4.18逐式转写。α/β为电场坐标指标，β_m,vis/ir为法线传播参数；保留2nh_m与(2n+1)h_m的区别。4.17分子原无i，照录并登记Q059；未改原式，勘误附件无新增采用修正。\n',encoding='utf-8')
header='''## 最新续接：B082完成2.2式（4.10）—（4.18）可编辑转写（2026-10-19）

用户在2.2文字补齐后要求“继续”，本轮优先收尾公式转写，未进入2.3。已完成4.1d—4.1f的九个编号式，按p7及高清公式图逐项对照；原三幅公式图从正文替换，仍保留在历史资产和B082-原式图对照.md。4.1g起正文内容保持不变。

新增Q059：4.17分子原式指数未写i，正文保留原式，候选仅注；未新增原文采用修正，无新增勘误附件条目。全节译文已补齐，复杂公式可编辑转写仍未全部完成。

下一批B083：从4.1g的B类源点式（4.19）—（4.21）开始，逐式核对后转写；A类（4.22）—（4.24）另作完整公式组推进。不要重跑B069—B081的合入/生成脚本覆盖现正文；那些脚本及草稿是历史批次快照。当前正文为唯一继续编辑的工作版本。

'''
p=m/'当前进度与续接.md';q=p.read_text(encoding='utf-8');p.write_text(q.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    q=p.read_text(encoding='utf-8')
    if p.name=='Preface序言.md':q=q.replace('数学转写待专项，原式疑点保留。','数学转写已推进至式（4.18），其余复杂长式继续分批处理；原式疑点保留。',1)
    else:q=q.replace('可编辑数学转写尚待专项处理。','可编辑数学转写已推进至式（4.18），其余复杂长式继续分批处理。',1);q=q.replace('Q039—Q058尚有未决项','Q039—Q059尚有未决项')
    p.write_text(q,encoding='utf-8')
(out/'B082.md').write_text('''# B082：4.1d—4.1f公式可编辑转写

日期：2026-10-19。底本2.2 PDF p7；源摘要沿原记录，PDF未修改。本批从三个界面场完整公式组划界，不进入p8体相场。

| 原文定位 | 对象 | 译文定位 | 已转写 | 已页面对照 | 备注 |
|---|---|---|---|---|---|
| p7，4.1d | 4.10—4.12 | 同名小节 | 是 | 是 | 0+；2nh_m；两个场及乘积 |
| p7，4.1e | 4.13—4.15 | 同名小节 | 是 | 是 | h_m+；(2n+1)h_m；两透射因子及相位 |
| p7，4.1f | 4.16—4.18 | 同名小节 | 是 | 是 | h_m−；各(1+r)因子；4.17原无i，Q059 |

逐项核对：E0与位置侧别、vis/ir与α/β下标、r/t方向、分子分母、正负号、2与2n+1、虚数单位、指数膜厚和原编号。数学仅断行，无因式重定义、无代数替换。新疑点保留，不将候选补i写入公式，不新增采用修正的勘误条目。原式影像在B082-原式图对照.md，修订前全文在B082-修订前.md。

显示与范围验收见B082验收.json及参考渲染。全节公式编号索引更新表示方式；B069—B081记录为当时影像交付的历史快照，不重建覆盖现正文。下一批从4.19—4.21的完整B类源点公式组开始。
''',encoding='utf-8')
print('B082 merged; 9 equations; Q059 retained')

from pathlib import Path
import csv,json,hashlib,re
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1'
(o/'B011.md').write_text('''# B011：式（13）定位及前两组页面对照

日期：2026-10-16。来源：1.1原PDF p7—8；p9开头为后续解释段，不属于式（13）。沿用PDF技能的页面视觉核对方式，不根据提取文本猜回数学字符。

## 范围与结果

整式六主组、每组四子项，共24子项。p7为定义和第1、2组；p8为第3—6组及式号13。本批仅逐项对照p7的8子项。页8只作范围定位，未宣称逐项核验；页9只确认后续解释段边界。

定义输出2ω₁−ω₂，输入E_j(ω₁)E_k(ω₁)E_l(−ω₂)；公共−Ne⁴/ℏ³，求和g,n,n′,n″。原定义只出现一次χ，旧译重复χ等式，留待整式统一替换时删除。

| 对象 | 外因子 | 核对情况 |
|---|---|---|
| 第1组 | (r_l)_{gn″}/(ω₂−ω_n″g+iΓ_n″g) | 4子项；Q016暂拟读，Q017照录原文正号 |
| 第2组 | (r_l)_{ng}/(ω₂+ω_ng+iΓ_ng) | 4子项；未发现旧译实质符号差异 |

各组4项相加，内括号A−B；两组26个分式，iΓ均正。工作稿另外有定义比值；公共因子以行内式记录。T₁、T₂为管理标识，不是作者符号。

## 疑点

- Q016：首组第3子项中间分母的ω、Γ下标与旧译nn′不符，原图可见双撇形及异常附加字形。工作稿暂拟nn″，明确标为未确定；不据对称性宣称修正完成，不静默写回正文。
- Q017：首组第4子项中间分母原文及旧译均为ω₁＋ω₂−ω_nn″＋iΓ_nn″；保留加号。此处与邻项的频率结构不同，但未作独立推导，不认定原式错误。

## 质量检查与交付

工作稿参考渲染5个数学片段，无解析错误；窗口/文档宽均1100像素，高1714像素。已查看截图，两组与附注完整可见。正式译文只插入式13工作进度提示，公式、前文及后文均与B011备份相同；源PDF哈希未变。术语仍70条、语言对照语料仍12条。Q013、Q015等旧疑点未关闭。

[工作稿](B011-式13工作稿.md) · [渲染检查图](B011-参考渲染.png) · [定义及首组原图](B011-定义及首组原文.png) · [第2组原图](B011-式13首组原文.png) · [原p8](B011-原文p8.png)

下一批B012：p8第3、4主组，各4子项。后续批次核第5、6组并整式合并检查；疑点无法解决时保留译者注及状态，不宣布原式理论正确。
''',encoding='utf-8')
(o/'式13-核对进度.md').write_text('''# 式（13）核对进度

2026-10-16：已页面对照2/6主组（8/24子项），首组Q016尚为拟读。整式未完成，未替换正文旧式。

| 范围 | PDF页 | 状态 |
|---|---|---|
| 定义、公共系数与求和 | 7 | B011已对照；旧译重复χ待最终删除 |
| 第1、2主组 | 7 | [B011记录](B011.md)、[工作稿](B011-式13工作稿.md)；Q016/Q017未决 |
| 第3、4主组 | 8上半 | 待B012 |
| 第5、6主组 | 8下半 | 待后续批次 |
| 整体顺序、括号、编号及正式替换 | 7—8 | 待分组结束后处理 |

旧式备份：式13-旧译候选.txt；T₁等不属于作者符号。下一解释段从p9开始，另批处理。
''',encoding='utf-8')
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s+='\n| Q016 | 1.1 PDF p7 式(13)首组第3子项中间分母 | ω及Γ下标旧译nn′，底本可见双撇形及异常字形 | 底本字形/转录/P1 | B011工作稿暂拟nn″，明确未定；正文旧式未改。见定义及首组原图，待清晰底本或推导复核 |\n| Q017 | 1.1 PDF p7 式(13)首组第4子项中间分母 | 原文明确为ω₁＋ω₂，邻项为ω₁−ω₂；旧译照原文 | 原式公式疑点/P1 | B011保留原文加号，不以邻项推改；待推导或外证，未认定原式错误 |\n';p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');a=s.index('## 下一批B011');b=s.index('沿用和频过程',a);s=s[:a]+'''## 最新工作稿与下一批B012

B011已定位式（13）范围为p7—8，六组24子项；定义及p7前两组已页面对照（8/24子项）。第1组Q016下标暂拟nn″，Q017照录原文ω₁＋ω₂，均未解决。工作稿5个数学片段参考渲染通过，无水平溢出。正式正文只加工作进度提示，旧式（13）未替换，正式完成断点仍为式（12）末。

读取[式13总表](校订记录/1.1/式13-核对进度.md)、[B011记录](校订记录/1.1/B011.md)及工作稿。B012核p8第3、4组（各4子项），复用B011-原文p8.png，按需生成高分辨率裁图。第5、6组及全式检查留后批；p9解释段另批。不要仅把式12的ω₂换号后复制，按原页逐项核对。

'''+s[b:];p.write_text(s,encoding='utf-8')
for file,key,value,updates in [('章节清单.tsv','编号','1.1',{'状态':'校订中：正文至式12末；式13前2组已对照工作稿，Q016/Q017未决','公式图表范围':'式1—12已对照（原式疑难未结）；式13工作稿2/6组，未替换正文'}),('全书调查/分批建议.tsv','预排编号','P004',{'执行状态':'B010完成p7式12末；B011对照式13定义及前2组工作稿，Q016/Q017未决；整式未完成'})]:
 p=m/file;rows=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));next(x for x in rows if x[key]==value).update(updates)
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('式（13）起待校订；原式指标及Q015字形仍待核验','式（13）前两组已有部分核对工作稿、整式未完；原式指标及字形疑点仍待核验');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('下一批B011先定位式（13）全范围，再分组处理。','B011已定位式（13）p7—8并对照前两组工作稿，Q016/Q017未决；下一批B012核p8第3、4组，整式暂不替换。');p.write_text(s,encoding='utf-8')
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='\n## B011：式（13）部分工作稿\n\n负频输入保留E_l(−ω₂)。首组第3子项中间分母下标为Q016拟读，不作为已确定符号；第4子项中间分母ω₁＋ω₂按底本保留（Q017），不得仅靠输出频率替换正负号。定义χ重复是旧译转录问题，整式合并时删除。\n';p.write_text(s,encoding='utf-8')
p=m/'排版工具/README.md';s=p.read_text(encoding='utf-8')+'\n`--b011`检查式（13）定义及前两组的部分工作稿，不代表整式完成。\n';p.write_text(s,encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');prior=(o/'B011-修订前.md').read_text(encoding='utf-8');assert re.sub(r'> \*\*式（13）工作进度：\*\*[^\n]*\n\n','',s)==prior
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
d=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'));v=next(x for x in d['results'] if x['batch']=='B011');assert v['width']==v['scrollWidth'] and v['formulas']==5
print('PASS: B011 records synchronized; only formal progress notice changed; PDF unchanged; reference rendering verified.')

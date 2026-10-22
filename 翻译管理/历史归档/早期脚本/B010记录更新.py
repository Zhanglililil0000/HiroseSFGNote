from pathlib import Path
import csv,re,hashlib,json
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');before=(o/'B010-修订前.md').read_text(encoding='utf-8')
# Verify all following unreviewed content is unchanged.
needle=r'\chi^{(3)}_{ijkl}(\omega = 2\omega_1 - \omega_2)';assert s[s.index(needle):]==before[before.index(needle):]
note='> **译者注（Q015）：** 原文式（12）第五主组末项的外分母中，Γ 的下标末端字形不清；此处暂沿旧译记作 $\\Gamma_{n n\prime\prime}$，待复查，未将该字形视为已确定。\n\n'
pos=s.index(r'\tag{12}');end=s.index('$$',pos)+2;s=s[:end]+'\n\n'+note+s[end:].lstrip('\n');p.write_text(s,encoding='utf-8')
(o/'B010.md').write_text('''# B010 校订记录

日期：2026-10-16。范围：1.1 PDF p6末第5主组、p7首第6主组，并合并检查p5—7完整式（12）。未处理式（13）。

- 第5组外因子为(r_j)_{gn″}/(ω₁+ω_n″g+iΓ_n″g)，第6组为同分母的(r_k)_{gn″}。各4子项；逐项核对矩阵元顺序、频率及衰减下标、正负号。
- 两组每个子项内均为A−B，组内四项相加。连同B008、B009，六组共24子项、78个组内分式；另有定义的场比值和公共e⁴/ℏ³，总80个分式。
- 输出2ω₁+ω₂；输入E_j(ω₁)E_k(ω₁)E_l(ω₂)；公共−Ne⁴/ℏ³；求和g,n,n′,n″。原式末尾没有另列ρ，未自行补入。
- 原文第6组在第3、4子项外另有一层方括号，旧译省略；本次恢复。该层仅将两加项组合，不改变代数值。
- Q015：第5组第4子项外分母Γ下标末端字形异常，暂沿旧译nn″，正文明确加注；不是已获确认的原文修正。其余本批未发现实质指标差异。
- 四波混合按术语表T069统一为四波混频。正式正文替换整式，去掉工作稿进度提示；T₁等管理标识未进入正文。
- 参考渲染：1个数学片段，1100像素窗口、文档宽1100，无水平溢出；已查看完整截图，式号12、六组及闭合括号可见。参考环境不代表所有Markdown阅读器。
- 式（13）及其后内容与批前逐字相同。源PDF SHA256保持不变。术语70条、语言语料12条；未增加未定公式语料。Q013等旧疑难继续保留。

证据：[第5组原文](B010-第5组原文.png)、[第6组原文](B010-第6组原文.png)、[完整转录](B010-式12定稿.md)、[参考渲染](B010-参考渲染.png)、[批前备份](B010-修订前.md)。

下一批B011：先定位p7起式（13）的完整范围，再按主组拆分；不将整节1.1标为完成。
''',encoding='utf-8')
p=m/'疑难与勘误.md';t=p.read_text(encoding='utf-8');t+='\n| Q015 | 1.1 PDF p6 式(12)第5主组第4子项外分母 | Γ下标末端字形异常，无法仅凭该字形完全确定 | 底本字形/P2 | B010保留旧译Γ_nn″并在正文加注；见B010-第5组原文.png，待更清晰底本或推导交叉复核，未宣称已解决 |\n';p.write_text(t,encoding='utf-8')
p=o/'式12-核对进度.md';p.write_text('''# 式（12）核对进度

2026-10-16：六组24子项均已页面对照，完整正文已替换并通过参考渲染。Q015字形待复查，故不宣称所有原式疑难已解决。

| 范围 | 来源 | 记录 |
|---|---|---|
| 定义、公共系数、求和及第1组 | p5 | B008 |
| 第2—4组 | p6 | B009 |
| 第5—6组、整体顺序/括号/编号 | p6末—p7首 | [B010](B010.md) |

[B010完整转录](B010-式12定稿.md)、[参考渲染](B010-参考渲染.png)。旧工作稿保留为历史证据，T₁等不是作者符号，不用于正式正文。完成转录复核不等于独立验证理论推导。
''',encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- B001—B010：1.1正式正文已校订至PDF p7式（12）末。六组24子项已逐组页面对照，整式已替换并通过参考渲染。整节及第三部分尚未完成。
- 最新记录：[B010](校订记录/1.1/B010.md)、[式12总表](校订记录/1.1/式12-核对进度.md)。历史工作稿的T₁等只作管理标识。
- Q015为式12第5组末项Γ下标字形疑点，正文暂沿旧译nn″并注，待复查；Q013式11指标及其余未决问题继续保留。源式末无另列ρ，未补入。
- 全书39份717页；23份旧译未重新校订，1.1部分校订，15节待译。P003覆盖完成，P004仅覆盖p7式12结尾。术语70条，语言对照语料12条。
- 模型页面复核及本地marked/KaTeX/Edge渲染不等于独立专业人工审校或作者理论确认。

## 下一批B011

从p7式（13）开始。先确定整式终点，再按主组拆为小批；不连同后续解释段一次处理。复用已有p7页面及文本缓存，只按需补图。式（13）及后文当前仍是原有待校订译文，本批未改。

沿用和频过程、二阶非线性极化率（明确语境可简称极化率）、菲涅尔因子。继续更新备份、批次记录及续接断点。

底本：日语原版/Chapter1/chap1-1Japanese.pdf；SHA256 55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
''',encoding='utf-8')
for file,key,updates in [('章节清单.tsv','编号',{'1.1':{'状态':'校订中：正文至p7式12末；Q015字形待查，式13起未校','公式图表范围':'式1—12已对照；Q013/Q015等待查；式13起未校'}}),('全书调查/分批建议.tsv','预排编号',{'P003':{'执行状态':'B007—B010覆盖p5—6；式12第5组Γ字形Q015待查'},'P004':{'执行状态':'B010仅覆盖p7式12末；式13及其余待分批'}})]:
 p=m/file;rows=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'))
 for row in rows:
  if row[key] in updates:row.update(updates[row[key]])
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8').replace('正文至第5页三阶段之前；式（12）第1—4组工作稿已核，整式未完；原式指标仍待核验','正文至第7页式（12）末；式（13）起待校订；原式指标及Q015字形仍待核验');p.write_text(t,encoding='utf-8')
p=m/'执行方案.md';t=p.read_text(encoding='utf-8');t=re.sub(r'当前阶段：[^\n]+','当前阶段：试点校订；B001—B010正文至1.1 p7式（12）末，式（13）起待校订。Q013/Q015等未决，整节未完成。',t,count=1);t=re.sub(r'式\(12\)已定位p5—7共6主组24子项，.*?完成翻译、复核和批次收尾后即结束该批。','式（12）六组24子项已对照并整式替换；Q015字形待复查。下一批B011先定位式（13）全范围，再分组处理。完成翻译、复核和批次收尾后即结束该批。',t);p.write_text(t,encoding='utf-8')
p=m/'符号与约定.md';t=p.read_text(encoding='utf-8');t+='\n## B010：式（12）整式合并\n\n保留−Ne⁴/ℏ³、四重态求和、六组24子项和原第6组末两项的额外方括号，不补ρ。Q015的Γ下标字形暂沿旧译nn″并注，尚未确认；详见B010记录。\n';p.write_text(t,encoding='utf-8')
p=m/'排版工具/README.md';t=p.read_text(encoding='utf-8');t+='\n`--b010`检查式（12）完整转录；结果和截图保存在1.1校订记录目录。\n';p.write_text(t,encoding='utf-8')
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('B010 records synchronized; eq13 onward unchanged; source hash verified; Q015 retained.')

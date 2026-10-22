from pathlib import Path
import shutil,re
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B014-修订前.md');a=s.index('532 nm 光');a=s.rfind('\n',0,a)+1;b=s.index('**（三阶极化－2',a)
t='''当 $532\\,\\mathrm{nm}$ 光与红外光产生的 SFG 和 $2\\times1064\\,\\mathrm{nm}$ 光与红外光产生的四波混频（4WM）光出现在同一波长时，可使用式（12）。此外，由上述各式可知，增强振动共振的电子共振项，除生成光之外，也可能涉及中间过程中经历的和频能量（差频能量）以及二倍频能量所引起的共振。尤其要注意，前一种共振发生在生成光能量的一半处，因此，共振激发能级位于较低能量处时，也可能出现这种共振。可见光引起的电子共振也可作同样的说明。

> **译者注（Q019）：** 本段原文引用式（12），并称“前者”发生在生成光能量的一半处，此处按原文保留；具体对应的能量组合及适用条件尚未独立核验。

'''
s=s[:a]+t+s[b:];p.write_text(s,encoding='utf-8');(o/'B014-本批译文.md').write_text('# B014：式（13）后的说明\n\n'+t,encoding='utf-8')
(o/'B014.md').write_text('''# B014 校订记录

2026-10-16；范围：1.1 PDF p9首段，止于“三阶极化−2”标题之前。原文一段、五句，无新增公式或图表。

已逐句页面对照：保留532nm与2×1064nm比较、式12引用、和/差频及倍频能量、前者为生成光能量一半、可见光共振末句。旧译误将“增强振动共振的电子共振项”译成“振动共振增强的电子共振项”，已改正；删除原文没有的“更为显著”，修正为低能激发态也可能出现共振。清除字面转义\\u00d7及零宽字符。

Q019登记原式12引用和“前者/一半”的物理对应未独立确认，按原文翻译并注，不擅改式号。原文证据复用B011-原文p9.png。式14及以后未改。

本批译文另存以供渲染；下一批从p9式14开始，先核前三主组（12子项），再核p10后三组并整式整理。
''',encoding='utf-8')
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8')+'\n| Q019 | 1.1 p9式13后说明 | 原文引用式12，并称“前者”在生成光半能量处共振；具体能量组合及条件需复核 | 原文表述/P2 | B014按原文保留并加注，未以推测更换式号或能量关系 |\n';p.write_text(s,encoding='utf-8')
p=m/'已核验对照语料/第1章.md';s=p.read_text(encoding='utf-8')+'\n## C013：共振增强关系（B014）\n\n- 来源：1.1 PDF p9首段“振動共鳴を増強する電子共鳴項”。\n- 中文：增强振动共振的电子共振项。\n- 保留施事关系，不译成振动共振增强电子共振；只收该语言片段，不收Q019未决物理解释。模型页面对照。\n';p.write_text(s,encoding='utf-8')
p=m/'第一章持续执行.md';p.write_text('''# 第一章持续执行授权与安排

2026-10-16用户要求：“继续，逐步完成，直到完成第一章”。这覆盖1.1—1.5；可在同一轮连续执行多个小批次，不再采用每批默认结束的节奏。每批仍独立核对、备份、渲染、记录；不因章级目标放宽质量标准。

总量：5节61页。当前1.1先完成剩余正文及附录，再依次1.2（12页）、1.3（5页）、1.4（9页）、1.5（12页英文书目）。章末统一术语、引用及Preface章/节导读。涉及未决公式的部分可保留明确候选和原文证据，不标为无疑点定稿。

会话资源不足时保留真实进度与下一批入口，不宣称第一章完成；后续继续本授权范围。
''',encoding='utf-8')
# Generic renderer input lets each small batch verify only its own deliverable.
p=m/'排版工具/检查译文.cjs';s=p.read_text(encoding='utf-8');s=s.replace(' const exe=['," const custom=process.argv.find(x=>x.startsWith('--draft='));if(custom){const [id,...parts]=custom.slice(8).split(':');sections.length=0;sections.push([id,fs.readFileSync(path.join(base,parts.join(':')),'utf8')]);}\n const exe=[");p.write_text(s,encoding='utf-8')
print('B014 paragraph revised and source ambiguity retained; chapter-wide authorization saved.')

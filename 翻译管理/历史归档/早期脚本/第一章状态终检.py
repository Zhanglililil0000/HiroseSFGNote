from pathlib import Path
import csv,re,json
r=Path('HiroseSFGNote');m=r/'翻译管理'
p=m/'全书调查/分批建议.tsv';rows=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'))
for x in rows:
 if x['节号'] in ['1.1','1.2','1.3','1.4','1.5']:x['执行状态']='2026-10-18第一章本轮页面对照及排版整理已覆盖；原式/书目疑难保留，见B001—B049及第一章完成复核'
with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
p=m/'执行方案.md';s=p.read_text(encoding='utf-8');a=s.index('## 下一批具体任务');b=s.index('来源：',a);s=s[:a]+'''## 后续入口

2026-10-18第一章已完成本轮页面对照、译文修订及排版整理，见《第一章完成复核》。用户本轮要求的章级范围已收尾；此前B014及4.4试点的续接安排由此状态替代。Q013/Q015—Q030等未决，仍需原式专项核验；后续可在新的指令下进入第二章或优先处理疑点。第一章不是无疑点定稿，不因章节收尾自动关闭问题。

'''+s[b:];p.write_text(s,encoding='utf-8')
p=m/'第一章持续执行.md';s=p.read_text(encoding='utf-8')+'\n2026-10-18收尾：B001—B049已完成第一章本轮页面对照及排版整理，详见第一章完成复核.md；原式疑点保留。本授权范围不自动扩展到第二章。\n';p.write_text(s,encoding='utf-8')
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8')+'\n## 第一章章末回查（2026-10-18）\n\n微观p/β与宏观P/χ按原文区分；用户指定χ二阶用二阶非线性极化率。1.3的正时间指数与1.4的负时间指数及cgs高斯单位制均保留，跨节不可机械拼接。简并振动归一化、衰减符号、原式方向余弦等疑点见Q025—Q029。新增术语为译者暂用，不升级为用户确认。\n';p.write_text(s,encoding='utf-8')
p=m/'第一章完成复核.md';s=p.read_text(encoding='utf-8')+'\n最终数学语法复查：五个正文文件共916个行内/独立数学片段全部通过KaTeX严格解析；结果见校订记录/第一章最终数学检查.json。编号计数与语法通过不代表原式物理正确。\n';p.write_text(s,encoding='utf-8')
# Verify navigation local links and the final glossary/corpus counts.
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8');from urllib.parse import unquote
for target in re.findall(r'\]\(([^)]+)\)',s):
 if target.startswith('http'):continue
 assert (r/unquote(target)).exists(),target
assert len(list(csv.DictReader((m/'术语表.tsv').open(encoding='utf-8-sig'),delimiter='\t')))==80
assert len(re.findall(r'^## C\d+', (m/'已核验对照语料/第1章.md').read_text(encoding='utf-8'),re.M))==16
print('PASS: first-chapter page windows and next-step records updated; all Preface local links valid; glossary80/corpus16.')

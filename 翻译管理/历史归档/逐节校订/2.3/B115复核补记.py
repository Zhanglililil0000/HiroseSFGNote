from pathlib import Path
import re,json
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];M=ROOT/'翻译管理';D=ROOT/'中文版本/第二章 薄膜产生的SFG'
note=r'> **译校注（Q073，保留原式）：** 本底本式（A.6a、b）的四处角度项均印为 $sin^2	heta_1^{2}$，即角度符号本身还带上标2；此处保留该字形。额外的2是否为排版遗留未决，候选 $sin^2	heta_1$ 未采用。第2.2节PDF p35亦有相同字形，已同步修复先前转写漏字；这属于转写修复，不是对原文公式作修正。'
files=[next(D.glob('2.3 *.md')),OUT/'B115-本批译文.md',next(D.glob('2.2 *.md')),OUT.parent/'2.2/B111-本批译文.md']
for p in files:
 s=p.read_text(encoding='utf-8')
 if p.name.startswith('2.2 '):(OUT/'B115-2.2关联修订前.md').write_text(s,encoding='utf-8')
 def edit(m):
  block=m.group()
  if r'\tag{A.6a}' in block or r'\tag{A.6b}' in block:
   block=re.sub(r'\\sin\^2\\theta_1(?!\^)',lambda _:r'\sin^2\theta_1^{2}',block)
   if r'\tag{A.6b}' in block:block+='\n\n'+note
  return block
 s=re.sub(r'\$\$[\s\S]*?\$\$',edit,s)
 s=s.replace('区别于正文SFG中的二阶非线性极化率','区别于第2.2节SFG正文中的二阶非线性极化率') if p.parent==OUT or p.name.startswith('2.3 ') else s
 p.write_text(s,encoding='utf-8')
p=M/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s+='\n## Q073：附录A.6额外角度平方（B115复核）\n\n2.3 PDF p1与2.2 PDF p35，A.6a/b四处均印sin²θ₁²。局部放大图已确认；两译文保留额外上标2，并修复原先转写漏字。候选去除角度上标2尚未采用；无原文公式修正及新增E编号。图像凭据见2.3/A6局部.png及2.2原式图B077-p35-04.png。\n';p.write_text(s,encoding='utf-8')
p=OUT/'B115.md';s=p.read_text(encoding='utf-8');s+='\n## 最终局部复核补记\n\n放大A.6后确认四处sin²θ₁²中角度本身的额外上标2。独立PDF与母本原式图均同样印出，作为Q073保留；两份正文与B111/B115片段同步修复转写漏字。母本关联修订前另存B115-2.2关联修订前.md，未将该转写修复混入原文勘误附件。\n';p.write_text(s,encoding='utf-8')
p=OUT/'2.2与2.3复用核验表.md';s=p.read_text(encoding='utf-8');s+='\n局部复核新增Q073：两底本A.6四处均有额外角度上标2，现逐字保留；母本转写漏字也同步修复。此例说明同源译文仍需逐式对独立原图核验。\n';p.write_text(s,encoding='utf-8')
p=ROOT/'中文版本/附件/原文勘误表.md';s=p.read_text(encoding='utf-8');s=s.replace('## 后续维护','## 第2.3节：当前登记状态\n\nB115已校订引言与附录A，关联第2.2节Q053/Q072，并新增Q073（两底本A.6角度额外上标2）。原式均保留，未采用候选修正，暂无E-2.3条目。旧译的振幅比叙述修复与转写漏字修复只入校订记录。\n\n## 后续维护');p.write_text(s,encoding='utf-8')
p=OUT.parent/'2.2/全节数学收尾验收.md';s=p.read_text(encoding='utf-8');s+='\n后续复核（B115）：在独立2.3的A.6局部核验时发现母本同式角度上标2转写遗漏，已对2.2 PDF p35原图确认并修复；保留原式而非采用候选删字，登记Q073。两式编号及整节覆盖范围不变，修订前快照在2.3批次目录。\n';p.write_text(s,encoding='utf-8')
p=M/'当前进度与续接.md';s=p.read_text(encoding='utf-8');s=s.replace('16个唯一编号式及无编号关系已核；母本复用前逐项对独立PDF核验。','16个唯一编号式及无编号关系已核；母本复用前逐项对独立PDF核验。新增Q073：A.6角度额外上标2照录，2.2对应转写漏字同步修复。',1);p.write_text(s,encoding='utf-8')
print('Q073 recorded; two canonical texts and batch fragments corrected')

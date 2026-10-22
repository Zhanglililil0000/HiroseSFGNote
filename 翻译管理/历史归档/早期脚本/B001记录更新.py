from pathlib import Path
import csv,re,hashlib
root=Path('HiroseSFGNote').resolve();m=root/'翻译管理'
text='''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- B001 已对照校订 1.1“引言”的六段与五组无编号公式；Markdown 数学实际渲染待验证，整节未完成。
- 校订记录见 [B001](校订记录/1.1/B001.md)，修订前全文与底本摘要在同目录。
- 39 份原文共 717 页；23 份旧译未开始重新校订，1.1 部分校订；15 节待翻译。
- 全书 200 个结构页组、488 个 P 编号页级预排窗口均为计划；P001 仅其中 p1 引言进入 B001，不可标为整窗完成。
- Preface 整节概括仍为草案，仅调整 1.1 进度提示。已有两条模型页面对照语料，未经独立专业人工审校。
- 用户决定：SFG 为“和频过程”；χ⁽²⁾ 全称“二阶非线性极化率”，上下文明确可简称“极化率”；Fresnel coefficient 为“菲涅尔因子”。

## 续接断点

- 最后批次：B001，已对照、待排版验证。
- 当前节：1.1；底本 SHA256：55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 已起草/已对照：PDF p1“１．はじめに”全部六段，至“双極子−双極子相互作用に関する式はかなり複雑な無限級数である。”
- 已实际验证排版范围：无；已检查引言源码分隔符与隐藏字符。
- 下一批 B002：先处理 Q009 验证 B001 数学显示，然后才开新范围。
- 下一段：PDF p1“２．SFG分極と和周波発生”，首句“電場 E とそれによって誘起される双極子モーメント（分極）p との関係は…”。跨页到 p2，准确终点在阅读原文后登记。
- 前文约定：引言 p 为电偶极矩，N 在受力式中为力矩；ε 沿用原式，不补 ε₀；此处宏观极化未给出单位体积归一化。
- 未决问题：Q008 原文疑似脱字已有译者注；Q009 数学渲染待验证；Q004（式4旧译括号）在后续范围，尚未处理。其他见[疑难与勘误](疑难与勘误.md)。
- 术语变更回查：已确定译名随批次回查其余旧译，尚未全局替换。

## 工作入口

读取本文件、B001 记录、现行规范及相关术语，先检查用户工作区变更。不重新扫描全书，不把页级 P001 当成已完成；第 2 部分以后的正文保持旧译，待对应批次校订。
'''
(m/'当前进度与续接.md').write_text(text,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8');s=s.replace('当前阶段：翻译前准备；正文尚未重新校订。','当前阶段：试点校订；B001 已对照校订 1.1 引言，数学渲染待验证，整节未完成。');s=s.replace('先核验 1.1 的标题与正文结构，再处理其第一个完整小单元；','B001 已核对 1.1 引言；下一批先验证数学渲染，再从 PDF p1 第二部分开始；');p.write_text(s,encoding='utf-8')
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));r=next(r for r in R if r['编号']=='1.1');r['状态']='校订中：B001引言已对照，排版待验证';r['映射核验']='PDF p1引言六段已逐段对照；其余待核验';r['公式图表范围']='B001：引言5组无编号公式已视觉核对；无图表，余文待登记';r['导读状态']='整节导读仍为草案；B001仅完成引言内容对照'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8');s='\n'.join(l.replace('（旧译待校订）','（部分校订：引言已对照，排版待验证）') if l.startswith('- [1.1 ') else l for l in s.splitlines())+'\n';p.write_text(s,encoding='utf-8')
p=m/'术语表.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'))
for r in R:
 if r['术语编号'] in ['T012','T016','T021','T023']:
  r['文本定位状态']='B001 已对照 PDF p1 的用词及语境（模型页面核对）';r['状态']='本批用法已页面核对；项目译名暂用';r['原文位置']='1.1 PDF p1 引言';r['依据']='B001 页面对照；未进行独立专业人工审校';r['译名决定状态']='译者暂用；非用户新确认'
  if r['术语编号']=='T012':r['定义与适用语境']='固体或液体内分子实际感受到的电场；不等同于外加电场'
  if r['术语编号']=='T016':r['日语候选']='双極子−双極子相互作用';r['定义与适用语境']='偶极产生的场使分子响应互相影响；引言以反复传球比喻说明'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
# 历史调查保留，不把调查预排视为译文完成；只更新窗口执行提示。
p=m/'全书调查'/'分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));R[0]['执行状态']='部分进入B001：仅p1引言已对照、排版待验证；第二部分及p2未执行'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=root/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');before=(m/'校订记录/1.1/B001-修订前.md').read_text(encoding='utf-8');a=s.split('## 1. 引言',1)[1].split('## 2. SFG 极化与和频过程',1)[0]
assert a.count('$')%2==0 and '\u200b' not in a and '\t' not in a
assert len([x for x in a.strip().split('\n\n') if not x.startswith('>')])==6
assert s.split('## 2. SFG 极化与和频过程',1)[1]==before.split('## 2. SFG 极化与和频过程',1)[1]
assert hashlib.sha256((root/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('PASS: 6 paragraphs, paired math delimiters, no hidden indentation, unmodified remainder, unchanged source hash; management and navigation updated. Render pending.')

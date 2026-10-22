from pathlib import Path
import csv,re,json,hashlib
root=Path('HiroseSFGNote').resolve();m=root/'翻译管理';rec=m/'校订记录/1.1'
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8');s=s.replace('对照 PDF 原式后处理；未确定错误来源','B002 已对照 PDF p2 式(4)：多余右圆括号来自旧译，已删除；此项已解决');s=s.replace('内容及公式已对照，保留待排版状态；B002 开始先验证显示','B002 已补完 B001 的 KaTeX HTML＋本地字体参考渲染和截图检查；已解决（仅限该参考环境）');s+='\n| Q010 | 1.1 PDF p2 式(2)—(3) | N 原文称分子数，宏观 P 的归一化未在此明确 | 原文约定/P2 | 保留原式并加译者注；后续涉及单位制时回查，不擅改为数密度或补 ε₀ |\n';p.write_text(s,encoding='utf-8')
p=rec/'B001.md';s=p.read_text(encoding='utf-8');s+='\n## B002 补充更新（2026-10-16）\n\nB001 数学参考渲染现已验证通过：marked＋KaTeX HTML/配套字体，无界面 Edge 中已视觉检查完整截图。17 个数学片段解析正常，页面无水平溢出；粗体矢量与上下标可见。此前“渲染待验证”为 B001 当时状态，现由本更新取代；详见 B002.md。\n';p.write_text(s,encoding='utf-8')
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8');s+='''
## B002（1.1 PDF p1—2）

| 符号 | 本批原文含义及规则 | 核验状态 |
|---|---|---|
| p / P | 式(1) p 为分子电偶极矩；式(2) P 为宏观极化；保留大小写与矢量 | 已页面对照 |
| α / β / γ | 式(1)微观响应系数；α有两个指标，β有三个指标；不把场幂次与指标个数混淆 | 已页面对照；超极化率译名仍候选 |
| χ⁽¹⁾ / χ⁽²⁾ / χ⁽³⁾ | 式(2)宏观响应；χ⁽²⁾ 全称二阶非线性极化率 | 已页面对照；中文二阶全称用户已确定 |
| N | 式(3)原文称分子数；不擅加单位体积或 ε₀ | 本段已核对；整体归一化后续回查 Q010 |
| ⟨…⟩ | 系综平均或取向平均 | 已页面对照 |
| exp[i(ωt−k·r)] / c.c. | 时间与空间符号依式(4)，c.c. 为紧邻前项的复共轭 | 已页面对照 |

N 在引言的力矩公式与式(3)中含义不同，须按局部上下文区分。
''';p.write_text(s,encoding='utf-8')
p=m/'术语表.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'))
for r in R:
 if r['术语编号'] in ['T003','T005','T020','T024','T025','T026','T028','T049']:
  r['文本定位状态']='B002 已对照 PDF p1—2 相关定义（模型页面核验）';r['原文位置']='1.1 PDF p1—2，第二部分，式(1)—(5)及说明'
  if r['术语编号'] not in ['T005','T049']:
   r['状态']='本批用法已页面核对；译名依项目决定或暂用'
  r['依据']=r['依据']+'；B002 已对照本段语境'
 if r['术语编号']=='T024':r['定义与适用语境']='本段 P 为各分子极化矢量和；单位体积归一化未明示，保留宏观极化，不擅写极化强度'
 if r['术语编号']=='T004':r['定义与适用语境']+=' B002 原文使用高阶分極率，超分極率不是本段原词。'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'章节清单.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));r=next(x for x in R if x['编号']=='1.1');r['状态']='校订中：第1、2部分已对照及参考渲染，其余待校订';r['映射核验']='PDF p1—2第1、2部分已对照；其余待核验';r['公式图表范围']='引言5组无编号公式＋第二部分式(1)—(5)已视觉核对；本范围无图表';r['导读状态']='整节导读仍草案；第1、2部分已校订'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=m/'全书调查/分批建议.tsv';R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));R[0]['执行状态']='由B001+B002覆盖p1—2；内容对照及参考渲染完成，非整节定稿'
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8');s=s.replace('部分校订：引言已对照，排版待验证','部分校订：第1、2部分已对照及参考渲染');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B001 已对照校订 1.1 引言，数学渲染待验证，整节未完成。','B001–B002 已对照校订 1.1 第1、2部分并完成参考渲染，整节未完成。');s=s.replace('B001 已核对 1.1 引言；下一批先验证数学渲染，再从 PDF p1 第二部分开始；','B001–B002 已完成 1.1 第1、2部分；下一批从 PDF p3 第三部分开始；');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

更新时间：2026-10-16。

## 当前状态

- B001–B002：1.1 第1、2部分（PDF p1—2）已对照校订及参考渲染；第三部分以后仍为旧译，整节未完成。
- B001 的数学显示检查在 B002 补完，Q009 已关闭；式(4)旧译括号错误 Q004 已修正。
- 范围内：引言五组无编号公式、式(1)—(5)，无图表；核验为模型页面对照，未经独立专业人工审校。
- 参考渲染：marked＋KaTeX HTML/本地字体，无界面 Edge，截图与数据保存在校订记录/1.1；不是所有 Markdown 阅读器兼容保证。
- 全书39份、717页；23份旧译尚未重新校订，1.1部分校订，15节待译。P001由B001+B002覆盖，其他P窗口仍为预排。
- 已有4条模型页面对照语料。Preface整节导读仍为草案，仅更新局部进度。

## 最新断点

- 最后批次：[B002](校订记录/1.1/B002.md)。
- 底本：1.1，SHA256 55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b。
- 已起草/已对照/已参考渲染：从 p1 引言起至 p2 末“赤外・可視SFG分光という。”，即第1、2部分。
- 下一批 B003：PDF p3“３．分子のSFG分極と振動共鳴”，首句“閉じた（物理）系では、全エネルギーを一定に保ったままで…”。先检查含时相互作用与薛定谔方程的小单元，不一次处理整个第三部分，实际终点据完整推导登记。
- 延续约定：p为分子电偶极矩，P为宏观极化；α/β/γ为微观响应，χ为宏观响应；χ⁽²⁾全称二阶非线性极化率；N在式(3)称分子数，不擅改密度；式(4)相位为 exp[i(ωt−k·r)]。
- 用户决定：SFG译“和频过程”，Fresnel coefficient译“菲涅尔因子”；其他未确认译名不自动视为用户同意。
- 未决：Q008原文疑似脱字已注；Q010宏观归一化后续回查。其他见疑难与勘误。

## 开始下一批

先读本文件、B002记录及相关术语；检查用户变更，按需查看p3及邻页，不重新扫描全书。渲染工具可重复使用，无需重新下载依赖。第三部分以后的旧译保持至对应批次处理。
''',encoding='utf-8')
# 后文与引言保护检查。
p=root/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');old=(rec/'B002-修订前.md').read_text(encoding='utf-8')
assert s.split('## 3. 分子的 SFG 极化与振动共振',1)[1]==old.split('## 3. 分子的 SFG 极化与振动共振',1)[1]
assert s.split('## 1. 引言',1)[1].split('## 2.',1)[0]==old.split('## 1. 引言',1)[1].split('## 2.',1)[0]
seg=s.split('## 2. SFG 极化与和频过程',1)[1].split('## 3.',1)[0];assert re.findall(r'\\tag\{(\d+)\}',seg)==['1','2','3','4','5'];assert '\u200b' not in seg and '\t' not in seg
assert hashlib.sha256((root/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
data=json.loads((rec/'渲染检查.json').read_text(encoding='utf-8'));assert len(data['results'])==2 and all(x['width']==x['scrollWidth'] for x in data['results'])
print('PASS: equations 1–5, unchanged intro and later text, source hash, two reference renders without horizontal overflow; records updated.')

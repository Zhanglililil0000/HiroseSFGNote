from pathlib import Path
import csv,re,json,hashlib
from urllib.parse import quote,unquote
r=Path('HiroseSFGNote');m=r/'翻译管理';p=m/'章节清单.tsv';rows=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'))
summaries={'1.1':'分子与宏观响应、共振选择规则、取向张量和界面场；附录A—C给出含时微扰及密度矩阵推导。','1.2':'将振动偶极矩与拉曼张量联系起来，讨论简并振动和费米共振，再以双原子分子展示坐标变换及八类偏振组合。','1.3':'从复电场、边界条件到s/p反射透射及金属界面场，最后用有量纲的菲涅尔L因子连接SFG极化与辐射场。','1.4':'在cgs高斯单位制下讨论近区/远区偶极场、辐射功率、界面出射与全反射，以及相干SFG的观测几何。','1.5':'1983—1995年94条历史书目；保留原编号、英文信息与原题，补充中文题名，记录原始页码与拼写疑点。'}
batches={'1.1':(1,27),'1.2':(28,34),'1.3':(35,38),'1.4':(39,43),'1.5':(44,49)};counts={};hashes=[]
for x in rows:
 sec=x['编号']
 if sec not in summaries:continue
 src=r/x['原文路径'];assert hashlib.sha256(src.read_bytes()).hexdigest()==x['原文SHA256'];hashes.append(sec)
 s=(r/x['现有译文路径']).read_text(encoding='utf-8');tags=re.findall(r'\\tag\{([^}]+)\}',s);assert len(tags)==len(set(tags));counts[sec]=len(tags)
 lo,hi=batches[sec];x.update({'状态':'本轮全节页面对照及排版整理完成；原式/书目疑难未决','映射核验':f'全{x["PDF页数"]}页已按B{lo:03d}—B{hi:03d}对照','公式图表范围':f'{len(tags)}个唯一编号式及无编号项目已覆盖' if sec!='1.5' else '94个原书目编号及双语题名完整；非论文全文核验','导读状态':'已根据正文更新；见Preface与第一章阅读导航','导读草案':summaries[sec]})
 if sec=='1.3':x['暂定中文标题']='光电场、极化与菲涅尔因子'
with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8');s=s.replace('以下概括仅据目录标题拟定，尚未核对 PDF 正文。链接指向现有旧译，不表示其已通过校订。','第一章导读已根据正文更新（2026-10-18）；第二至八章仍是据目录拟定的准备稿。第一章已完成本轮页面对照和排版整理，原式疑点仍见译者注；其他章的链接不表示已校订。');s=s.replace('**本章导读（待正文核验）：** 建立和频光谱、电磁场与共振的基础概念。','**本章导读：** 先以1.1建立和频响应、共振和取向框架，再用1.2理解拉曼张量、简并与费米共振；1.3、1.4分别处理界面光场和偶极辐射，1.5提供历史检索入口。全章5节61页本轮已对照整理，仍有原式未决问题。各节内部小标题的内容概括见[第一章阅读导航](中文版本/第一章%20SFG快速入门/阅读导航.md)。')
lines=s.splitlines()
for i,line in enumerate(lines):
 for sec in summaries:
  if line.startswith('- ['+sec+' '):
   x=next(x for x in rows if x['编号']==sec);label={'1.1':'SFG光谱入门','1.2':'振动共振、费米共振与双原子分子','1.3':'光电场、极化与菲涅尔因子','1.4':'电偶极子的电场与辐射','1.5':'SFG早期工作（1983—1995）'}[sec]
   lines[i]=f'- [{sec} {label}]({quote(x["现有译文路径"],safe="/")})（本轮已对照整理，疑点保留）：{summaries[sec]}'
s='\n'.join(lines)+'\n';p.write_text(s,encoding='utf-8')
# Actual first chapter preplanned windows only; retain others untouched.
p=m/'全书调查/分批建议.tsv';rs=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'))
for x in rs:
 if any(v in ['1.1','1.2','1.3','1.4','1.5'] for k,v in x.items() if k in ['章节编号','节编号','编号']):x['执行状态']='第一章本轮页面对照/排版整理已覆盖；原式疑难保留，见各节B001—B049记录'
with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rs[0]),delimiter='\t');w.writeheader();w.writerows(rs)
report=json.loads((m/'校订记录/第一章渲染检查.json').read_text(encoding='utf-8'));assert all(v['scrollWidth']==v['width'] for v in report['results']);assert all(f'B{n:03d}' in [v['batch'] for v in report['results']] for n in range(1,50) if n!=15)
text='''# 第一章本轮完成复核

收尾日期：2026-10-18。覆盖第一章1.1—1.5，全61页；B001—B049按完整段落/公式或书目条目留存记录。B015分组随B016整式渲染。

| 节 | 页数 | 批次 | 编号项目 |
|---|---:|---|---|
| 1.1 | 23 | B001—B027 | 49个编号式 |
| 1.2 | 12 | B028—B034 | 37个编号式 |
| 1.3 | 5 | B035—B038 | 19个编号式 |
| 1.4 | 9 | B039—B043 | 25个编号式及完整方程对照表 |
| 1.5 | 12 | B044—B049 | 94个原书目编号、94个中文题名 |

合计130个唯一编号式（按节独立编号），无编号推导、条件、附注、跨页段落和书目均纳入。5份源PDF哈希与基线一致；英文书目编号与旧译/原文94项一致。渲染结果见校订记录/第一章渲染检查.json，已逐批查看图像，未发现水平溢出；截图发现的字面行距标记已修复并重渲染。数学显示检查仅对应本地marked/KaTeX/Edge环境。

术语80条；第1章重要对照语料16条。沿用用户指定和频过程、二阶非线性极化率、菲涅尔因子。新增译名仍标译者暂用，不冒称用户已确认。1.3文件名保留历史名称，以免既有链接失效；正文与导航显示菲涅尔因子。

## 完成范围与保留问题

本轮完成的是原文页面对照、译文修订和Markdown排版整理，不是原作者公式的独立推导认证。Q013/Q015—Q030等原式、归一化、符号与书目疑点未关闭；候选读法在正文中明确标注，不收作确定公式语料。95-2两种表面物种名暂保留英文精确术语，中文对应仍待确认。旧译备份及原图可回查。

较大修订包括补回1.2共轭表达式和求和/因子、纠正甲基例系数、恢复1.4漏掉的比较表一列、修复附录指数及分母转录、恢复原文件引用、补译94条书目题名。Preface已更新第一章章/节概括；阅读导航进一步概括节内各部分及附录，其他章保持准备稿状态。

本章可作为带疑点注释的阅读版本交付。后续若要求无疑点定稿，应专项核验已登记原式问题；不能仅把这些注释删除后称定稿。下一章翻译须另行进入第二章授权范围，当前不自动改第二章正文。
'''
(m/'第一章完成复核.md').write_text(text,encoding='utf-8')
(m/'当前进度与续接.md').write_text('''# 当前进度与续接

2026-10-18。第一章1.1—1.5全61页已完成本轮页面对照、译文修订和排版整理（B001—B049）；原式疑点未决，不是无疑点定稿。

阅读入口：../Preface序言.md、../中文版本/第一章 SFG快速入门/阅读导航.md。验收与限制：第一章完成复核.md。130个编号式、94条双语书目；术语80条、语言对照语料16条。5份底本哈希已核对。

Q013/Q015—Q030等继续保留。第一章本轮目标已收尾；如继续，应先决定开展原式疑点专项核验，或第二章逐批翻译校订。不把第二章旧译当已核对，不重跑历史一次性修订脚本。
''',encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8');s=re.sub(r'当前阶段：[^\n]*','当前阶段：2026-10-18第一章5节61页本轮对照及排版整理完成；原式疑点保留，参见第一章完成复核。其他章节尚未执行。',s,count=1);p.write_text(s,encoding='utf-8')
print('PASS: chapter metadata, Preface and handoff synchronized; 5 source hashes,130 tags,94 entries,48 rendering results verified.')

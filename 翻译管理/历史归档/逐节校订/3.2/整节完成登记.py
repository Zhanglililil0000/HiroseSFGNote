from pathlib import Path
import re,json,hashlib
import pypdfium2 as pdf
p=Path(__file__).resolve().parent; root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8')
tags=re.findall(r'\\tag\{([^}]+)\}',s)
expected=[f'2.{i}' for i in range(1,23)]+[f'A.{i}' for i in range(1,7)]+[f'B.{i}' for i in range(1,6)]
assert tags==expected and len(set(tags))==33
assert '旧译待核' not in s and '```' not in s
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
links=re.findall(r'!\[[^]]*\]\(([^)]+)\)',s)
assert len(links)==8 and all((f.parent/a).resolve().exists() for a in links)
digest=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest()
assert digest=='46a6bd5c96ff5066926f458052e3bc177f51f805b80227bc35617f9c465b3b76'
# p10裁图只含图组，移除上方邻式及日文叙述边缘。
d=pdf.PdfDocument(str(root/'日语原版/Chapter3/chap3-2.pdf')); im=d[9].render(scale=3).to_pil(); w,h=im.size
im.crop((int(w*.08),int(h*.25),int(w*.95),int(h*.79))).save(root/'中文版本/assets/ch03/ch03-s03-2-p10-paths.png')
newq='''\n\n## 3.2后半节原文疑点：Q118—Q121（待核验）

- Q118（p7—8）：2.14初值列后多一个右方括号，原字形已保留；2.15指定x=a₀rₘ′₁a，但第一行外部缺a，末行有a。候选为补第一行a，未采用。p7光路图部分层标及a²字形亦按原图保留。
- Q119（p8—12）：m层段落的界面反射叙述保留原层名；2.17的x′到x关联Q117。p9递推及2.18的行向量采用rₘ′ₘ、tₘ′ₘ，而初始表达及后续具体应用采用rₘₘ′、tₘₘ′，候选统一方向，未采用。图内额外撇号、层标等原样保留，不据路径对称性改写。
- Q120（p13，附录A）：元素绝对值均小于1不足以保证矩阵幂趋零。正文列0.6全元素矩阵作为反例，候选条件为谱半径小于1；仍照译原条件和A.6，不采用替换。仅检验n=0、1、2不足以证明一般有限和式，原叙述照译并注。
- Q121（p13，附录B）：原引用“第2节、第3节”与本文件编排不直接对应，保留待核；括注左端的拉丁b及无分母括号串保留，不能径改为β。相似变换A须可逆，不能与附录A一般矩阵或相位a混同。

Q118—Q121均在相应正文位置说明，未采用原文公式修正，不新增已确认勘误。旧译转录修复与这些原文问题分开登记。
'''
q=root/'翻译管理/疑难与勘误.md'; q.write_text(q.read_text(encoding='utf-8')+newq,encoding='utf-8')
card=p/'局部约定卡.md'; card.write_text(card.read_text(encoding='utf-8')+'\n## 整节补充\n\nB237—B248完成后半节。图内原因子保留原图；相似变换A、附录A一般矩阵A与传播相位a须区分。附录A已明确单位矩阵E，使前文上下文解释有本节后文依据。收敛条件疑点Q120不反向替换正文原条件。Q113—Q121仍待核，无原文修正采用。\n',encoding='utf-8')
coverage=p/'结构与复用核验表.md'; c=coverage.read_text(encoding='utf-8').replace('| E+反射光路图及式2.12起，p5—13 | 旧译待核 | 下一批B237起 |','| m′层四类场及23幅图，p5—8，式2.12—2.15 | 已对照原页；Q118未决 | B237—B240 |\n| m层路径与递推，p8—9，式2.16—2.18 | 已对照原页；Q119未决 | B241—B242 |\n| m层四类场及23幅图，p9—12，式2.19—2.22 | 已对照原页；原图疑点保留 | B243—B246 |\n| 附录A，p12—13，A.1—A.6 | 已对照原页；Q120未决 | B247 |\n| 附录B，p13，B.1—B.5 | 已对照原页；Q121未决 | B248 |')
coverage.write_text(c+'\n整节13页覆盖完毕，33个唯一编号式、8组46幅原光路子图。原图并非原文编号图，新文件名仅为资产管理标识。\n',encoding='utf-8')
index=[]
for a in sorted(p.glob('B???-覆盖.json')):
    r=json.loads(a.read_text(encoding='utf-8'))
    index.extend(dict(tag=t,batch=r['batch'],pages=r['pages']) for t in r.get('tags',[]))
(p/'全节公式编号索引.json').write_text(json.dumps(dict(count=33,tags=tags,locations=index),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'全节公式编号索引.md').write_text('# 3.2公式编号索引\n\n| 编号 | 批次 | 原文页 |\n|---|---|---|\n'+'\n'.join(f"| {r['tag']} | {r['batch']} | {r['pages']} |" for r in index)+'\n',encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'; t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：3.2全节译校完成（2026-10-20）\n\nB228—B248覆盖全13页：33个唯一编号式、8组46幅原光路子图，以及附录A/B完整保留。旧译漏行与矩阵乘法次序已修复；Q113—Q121保留原式并就地说明，未采用原文公式修正。最终排版结果见3.2整节完成复核。\n\n第三章两节均完成本轮译校，原文疑点不视为已解决。下一批B249：进入4.1，先核原页结构、标题与局部约定，不自动继承第三章符号。以下为历史记录。\n',1); progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第三章 双层膜的和频/阅读导航.md'; t=nav.read_text(encoding='utf-8'); i=t.index('## 3.2 '); t=t[:i]+'''## 3.2 双层膜和频的一般式

[进入3.2](3.2%20双层膜和频的一般式.md)。全13页本轮译校完成，33个编号式、8组46幅原光路子图及两个附录齐备。

先读系数与概述（p1—4），按膜层和初始方向选取8条场表达；再读详论（p4—12），以路径分类、反转次数递推和逆矩阵求和理解多重反射。附录A（p12—13）给出矩阵级数，收敛条件见Q120；附录B（p13）解释相似变换等价性，引用与记号疑点见Q121。Q113—Q121均保留待核，未采用原文修正。
'''; nav.write_text(t,encoding='utf-8')
preface=root/'Preface序言.md'; t=preface.read_text(encoding='utf-8'); t=re.sub(r'(^- \[3\.2[^\n]+?\)（)旧译待校订[^\n]*',r'\1全13页本轮译校完成）：以光路递推和矩阵级数组织双层膜响应，保留33个编号式与46幅光路子图；附录讨论级数与相似变换，原文疑点另注。',t,flags=re.M); preface.write_text(t,encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'; lines=listing.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    if line.startswith('3.2\t'):
        col=line.split('\t'); col[7]='全13页本轮译校完成；原文疑点Q113—Q121未决'; col[8]='B228—B248逐页对照；旧译漏行与矩阵次序已修复'; col[9]='33个唯一编号式；8组46幅原光路子图'; col[10]='已依据全文更新'; col[11]='以多重反射路径建立递推与逆矩阵场表达，附矩阵级数及相似变换说明。'; lines[i]='\t'.join(col)
listing.write_text('\n'.join(lines)+'\n',encoding='utf-8')
plan=root/'翻译管理/全书调查/分批建议.tsv'; lines=plan.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    c=line.split('\t')
    if len(c)>1 and c[1]=='3.2': c[-1]='全节完成；B228—B248按完整图组/公式组覆盖，页界按实际衔接'; lines[i]='\t'.join(c)
plan.write_text('\n'.join(lines)+'\n',encoding='utf-8')
err=root/'中文版本/附件/原文勘误表.md'; t=err.read_text(encoding='utf-8').replace('## 后续维护','## 3.2本轮状态（2026-10-20）\n\n全13页已完成本轮译校。Q113—Q121保留原式并就地说明，未采纳原文公式修正，故本轮无新增已确认勘误条目。旧译漏行、矩阵次序及原图恢复属于译文修复。\n\n## 后续维护',1); err.write_text(t,encoding='utf-8')
symbols=root/'翻译管理/符号与约定.md'; symbols.write_text(symbols.read_text(encoding='utf-8')+'\n\n## 3.2局部约定补充（2026-10-20）\n\n星号不表示复共轭；a/b为相位因子，αβγ为多重反射组合；E为单位矩阵，E±为场。附录B的A是相似变换矩阵，不自动等同附录A一般矩阵或传播相位a。原图因子和Q113—Q121未决值保留，详情见3.2局部约定卡。\n',encoding='utf-8')
print('全节覆盖、导航、疑难与管理登记完成；33编号，8组46子图')

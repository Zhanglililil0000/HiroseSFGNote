from pathlib import Path
import csv,json,re
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1'
(o/'B012.md').write_text('''# B012：式（13）第3、4主组校订记录

日期：2026-10-16。范围：1.1 PDF p8上半两主组，各4子项；本批不处理第5、6组及解释段。

## 页面核对

| 主组 | 外因子 | 四个中间分母（依次） |
|---|---|---|
| 3 | (r_k)_{ng}/(ω₁−ω_ng+iΓ_ng) | ω₁−ω₂−ω_n′g+iΓ_n′g；ω₁−ω₂−ω_nn″+iΓ_nn″；2ω₁−ω_n′g+iΓ_n′g；2ω₁−ω_nn″+iΓ_nn″ |
| 4 | (r_j)_{ng}/(ω₁−ω_ng+iΓ_ng) | 同第3组；矩阵元仍逐项按原页核验 |

已对照矩阵元的i/j/k/l、态指标和排列、频率/衰减下标、正负号及组内括号。每组四项相加，每个内括号为A−B；两组26个分式，iΓ均正。第1/3子项内A项为ω_n″g型分母，第2/4子项内A项为ω_nn′型；所有B项为ω_n′n″型，频率均为2ω₁−ω₂后减该跃迁频率再加iΓ。本批未发现旧译实质符号差异，无新增疑难。

## 交付与验证

[工作稿](B012-式13工作稿.md)、[原文裁图](B012-第3至4组原文.png)、[参考渲染](B012-参考渲染.png)、[批前备份](B012-修订前.md)。T₃/T₄仅管理标识，不写入正文。

参考渲染2个数学片段通过；窗口与文档宽均1100像素，高1454像素，无水平溢出；完整截图已查看。此检查仅对应本地marked/KaTeX/Edge。正文只更新进度提示，公式及其他正文逐字不变；PDF源哈希已验证不变。

累计4/6组、16/24子项已页面对照，其中首组Q016仍为拟读，Q017仍保留原式正号。不能据此将整式或整节标为完成。术语仍70条、语言语料仍12条，历史疑难未关闭。

下一批B013：p8下半第5、6主组，各4子项；完成后检查整式公共系数、求和、24子项顺序、括号、编号及显示，再统一替换正文。Q016/Q017未获新证据时明确加注保留，不静默修正。
''',encoding='utf-8')
p=o/'式13-核对进度.md';s=p.read_text(encoding='utf-8').replace('已页面对照2/6主组（8/24子项）','已页面对照4/6主组（16/24子项）').replace('| 第3、4主组 | 8上半 | 待B012 |','| 第3、4主组 | 8上半 | [B012记录](B012.md)、[工作稿](B012-式13工作稿.md)：已对照并参考渲染 |').replace('待后续批次','待B013');p.write_text(s,encoding='utf-8')
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');a=s.index('## 最新工作稿');b=s.index('沿用和频过程',a);s=s[:a]+'''## 最新工作稿与下一批B013

式（13）位于p7—8，六组24子项。B011核定义及第1、2组；B012核p8上半第3、4组，累计4/6组、16/24子项。Q016下标仍暂拟nn″，Q017仍照录原文ω₁＋ω₂；本批未新增疑难。B012工作稿2个数学片段参考渲染通过，无水平溢出。正文只更新进度提示，式（13）尚未整体替换，正式完成断点仍为式（12）末。

读取[式13总表](校订记录/1.1/式13-核对进度.md)、[B012记录](校订记录/1.1/B012.md)及前批工作稿。下一批B013核p8下半第5、6主组，各4子项；外因子依次为(r_j)_{gn″}/(ω₁+ω_n″g+iΓ_n″g)、(r_k)_{gn″}/(ω₁+ω_n″g+iΓ_n″g)。按需补高分辨率裁图，复用已有页图和文本缓存。核完后整体验证并替换；如有新疑点可进一步拆批，不强行标完成。

合并检查需保留输出2ω₁−ω₂、负频输入E_l(−ω₂)、−Ne⁴/ℏ³、g/n/n′/n″求和，删除旧译重复χ定义。核对所有括号和式号13；Q016拟读与Q017原式正号必须加注并保留未决状态。p9解释段另批，不把式12机械换号当作校订。

'''+s[b:];s=s.replace('P004仅覆盖p7式12结尾','P004正式正文仅覆盖p7式12结尾，式13前4组为工作稿');p.write_text(s,encoding='utf-8')
for file,key,value,updates in [('章节清单.tsv','编号','1.1',{'状态':'校订中：正文至式12末；式13前4组已对照工作稿，Q016/Q017未决','公式图表范围':'式1—12已对照（原式疑难未结）；式13工作稿4/6组，未替换正文'}),('全书调查/分批建议.tsv','预排编号','P004',{'执行状态':'B010完成式12末；B011—B012对照式13定义及前4组工作稿，Q016/Q017未决；后2组及整式未完'})]:
 p=m/file;rows=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));next(x for x in rows if x[key]==value).update(updates)
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
p=r/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('式（13）前两组已有部分核对工作稿','式（13）前四组已有部分核对工作稿');p.write_text(s,encoding='utf-8')
p=m/'执行方案.md';s=p.read_text(encoding='utf-8').replace('B011已定位式（13）p7—8并对照前两组工作稿，Q016/Q017未决；下一批B012核p8第3、4组，整式暂不替换。','B011—B012已对照式（13）定义及前四组工作稿，Q016/Q017未决；下一批B013核p8第5、6组，再整式检查及替换。');p.write_text(s,encoding='utf-8')
p=m/'符号与约定.md';s=p.read_text(encoding='utf-8')+'\n## B012：式（13）第3、4组\n\n两组外分母均为ω₁−ω_ng+iΓ_ng，中间分母依次为ω₁−ω₂−ω_n′g、ω₁−ω₂−ω_nn″、2ω₁−ω_n′g、2ω₁−ω_nn″，各加对应正iΓ。内括号A−B的矩阵元及态顺序见工作稿；不据对称性改动尚未核对的第5、6组。\n';p.write_text(s,encoding='utf-8')
p=m/'排版工具/README.md';s=p.read_text(encoding='utf-8')+'\n`--b012`检查式（13）第3、4主组的部分工作稿。\n';p.write_text(s,encoding='utf-8')
v=next(x for x in json.loads((o/'渲染检查.json').read_text(encoding='utf-8'))['results'] if x['batch']=='B012');assert v['formulas']==2 and v['width']==v['scrollWidth']
print('PASS: B012 management records synchronized; partial completion and unresolved issues retained.')

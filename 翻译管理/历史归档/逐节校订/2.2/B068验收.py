from pathlib import Path
import re,json,csv,io
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'));s=p.read_text(encoding='utf-8');marker='#### 4.1d.'
old=(out/'B068-修订前.md').read_text(encoding='utf-8');assert s[s.index(marker):]==old[old.index(marker):]
done=''.join((out/f'B{i:03}-本批译文.md').read_text(encoding='utf-8') for i in range(58,69));assert done==s[:s.index(marker)]
tags=re.findall(r'\\tag\{([^}]+)\}',done);assert len(tags)==15 and tags[-3:]==['4.7','4.8','4.9']
r=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));assert len(r['results'])==11 and all(i['width']==i['scrollWidth'] and not i['overs'] for i in r['results'])
report={'date':'2026-10-19','batch':'B068','scope':'PDF p6下部完整4.1c，式4.7—4.9','completedNumberedEquations':15,'completedMathFragments':r['math'],'part41dOnwardUnchanged':True,'batchTextsMatchReviewedPrefix':True,'sectionComplete':False}
(out/'B068验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
ep=root/'中文版本/附件/原文勘误表.md';t=ep.read_text(encoding='utf-8').replace('\n\n| E-2.2-003','\n| E-2.2-003');ep.write_text(t,encoding='utf-8')
pref=root/'Preface序言.md';lines=pref.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    if line.startswith('- [2.2 '):
        prefix=re.match(r'^(- \[2\.2[^\n]+?\]\([^)]+\))',line).group(1)
        lines[i]=prefix+'（分批校订中，已至4.1c）：讨论膜厚干涉、五类光源位置与多重反射光路，已核对反射/透射场及界面激发场至式（4.9）；原式疑点保留，4.1d起仍待校订。'
pref.write_text('\n'.join(lines)+'\n',encoding='utf-8')
nav=root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md';t=nav.read_text(encoding='utf-8').replace('2.2已分批校订至4.1b','2.2已分批校订至4.1c')
pos=t.index('## 2.2 ');a=t[:pos];b=t[pos:].replace('4.1c起仍为旧译待校订','4.1d起仍为旧译待校订')
b+='\n4.1c已核对有限膜1/m界面介质1侧的式（4.7）—（4.9）：区分源点位移的SF角度与两束激发光各自的波矢和角度。式（4.7）的visr原下标与式（4.9）的vis差异见Q043，未作统一修正。\n';nav.write_text(a+b,encoding='utf-8')
bp=mg/'全书调查/分批建议.tsv';rows=list(csv.DictReader(io.StringIO(bp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['节号']=='2.2' and int(row['PDF起页'])<=6:row['执行状态']='2026-10-19实际B058—B068，已覆盖p1—6至4.1c末；4.1d/p7起未核，跨出本范围的预排单元仅部分完成'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);bp.write_text(buf.getvalue(),encoding='utf-8-sig')
(out/'B068复核.md').write_text('''# B068复核

2026-10-19，目视核对p6下部及高分辨率B068-原式局部.png，完整覆盖4.1c式4.7—4.9。

恢复旧译数学格式与原编号，分式长乘积分行；核对0−、源点坐标、每束激发光的波矢/角度、两组往返相位、分子四因子及分母二因子的乘积关系。4.7两处visr按原文恢复，候选vis移注，Q043/E-2.2-003同步；4.9保持vis。

实际截图已查看，无横向溢出；已核部分累计15个编号式、214个数学片段严格解析通过。4.1d起与本批前备份相同；导读、符号卡、章节/分批、疑难及勘误记录已更新。全节仍在校订中。

下一批：p7完整4.1d式4.10—4.12，随后按界面侧别处理4.1e/f。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

from pathlib import Path
import re,json,csv,io
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'));s=p.read_text(encoding='utf-8')
old=(out/'B065-修订前.md').read_text(encoding='utf-8');marker='#### 4.1c.'
assert s[s.index(marker):]==old[old.index(marker):]
done=''.join((out/f'B{i:03}-本批译文.md').read_text(encoding='utf-8') for i in range(58,68));assert done==s[:s.index(marker)]
tags=re.findall(r'\\tag\{([^}]+)\}',done);assert tags==['2.1','2.2','2.3','2.4','2.5','2.6','4.1','4.2','4.3','4.4','4.5','4.6']
r=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));assert len(r['results'])==10
assert all(i['width']==i['scrollWidth'] and not i['overs'] for i in r['results'])
report={'date':'2026-10-19','batches':['B065','B066','B067'],'scope':'p5末—p6，4.1引言及4.1a/b','completedNumberedEquations':len(tags),'completedMathFragments':r['math'],'part41cOnwardUnchanged':True,'batchTextsMatchReviewedPrefix':True,'sectionComplete':False}
(out/'B065-B067验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
pref=root/'Preface序言.md';t=pref.read_text(encoding='utf-8');lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- [2.2 '):
        lines[i]=line.replace('已至第3部分末','已至4.1b').replace('第4部分起仍待校订。','并已校订波长/坐标分量约定及两介质界面两侧的式（4.1）—（4.6）；4.1c起仍待校订。')
pref.write_text('\n'.join(lines)+'\n',encoding='utf-8')
nav=root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md';t=nav.read_text(encoding='utf-8').replace('2.2已分批校订至第3部分末','2.2已分批校订至4.1b')
t=t.replace('第4部分起仍为旧译待校订','波长/坐标分量约定及两介质界面两侧激发场式（4.1）—（4.6）亦已核对；4.1c起仍为旧译待校订')
nav.write_text(t,encoding='utf-8')
bp=mg/'全书调查/分批建议.tsv';rows=list(csv.DictReader(io.StringIO(bp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['节号']=='2.2' and int(row['PDF起页'])<=6:row['执行状态']='2026-10-19部分覆盖：B058—B067，至p6的4.1b末；4.1c起待核，不按p6整页标完成'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);bp.write_text(buf.getvalue(),encoding='utf-8-sig')
(out/'B065-B067复核.md').write_text('''# B065—B067复核

2026-10-19，目视核对p5末—p6，按完整概念单元分为三批：4.1引言与无编号分量关系；4.1a式4.1—4.3；4.1b式4.4—4.6。

已逐项核对反射方向、z分量负号、四组透射坐标比值、两组tt/rr关系、vis/ir及α/β下标、0±侧别和E⁰幅值记号。仅作翻译润色、分行及数学格式修复，未改原公式；分量关系的普适正确性不作本轮独立证明。没有新增原文勘误或问题条目。

新三批截图均已查看；已完成部分累计12个编号式、194个数学片段严格解析通过，无水平溢出。4.1c起与本批备份相同。章节清单、预排进度、局部约定卡、符号、Preface及阅读导航均已更新。

下一批从4.1c有限膜1/m界面介质1侧的式4.7—4.9开始；当前未覆盖p6全页，全节仍在处理中。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

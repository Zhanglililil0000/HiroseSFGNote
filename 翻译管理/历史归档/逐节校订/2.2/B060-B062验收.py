from pathlib import Path
import csv,io,json,re
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'));s=p.read_text(encoding='utf-8')
old=(out/'B060-修订前.md').read_text(encoding='utf-8')
marker='## 3. SFG光的光路'
assert s[s.index(marker):]==old[old.index(marker):]
done=''.join((out/f'B{i:03}-本批译文.md').read_text(encoding='utf-8') for i in range(58,63))
assert done==s[:s.index(marker)]
tags=re.findall(r'\\tag\{([^}]+)\}',done);assert tags==['2.1','2.2','2.3','2.4','2.5','2.6']
assert '\u2500' not in done and 'exp(' not in done # all exponential functions use mathematical commands
r=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert len(r['results'])==5 and all(i['width']==i['scrollWidth'] and not i['overs'] for i in r['results'])
report={'date':'2026-10-19','batches':['B060','B061','B062'],'sourcePages':'p2—3，式2.1—2.6及对应解释','completedNumberedEquations':tags,'completedMathFragments':r['math'],'unrevisedPart3OnwardUnchanged':True,'batchTextsMatchCompletedPrefix':True,'sectionComplete':False}
(out/'B060-B062验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
pref=root/'Preface序言.md';t=pref.read_text(encoding='utf-8');lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- [2.2 '):
        line=line.replace('（分批校订中，仅序论及定义已对照）','（分批校订中，已至式2.6）')
        line=line.replace('编号公式与后续主体仍待校订。','并已校订反射、透射及膜内场式（2.1）—（2.6）；第3部分起仍待校订。')
        lines[i]=line
pref.write_text('\n'.join(lines)+'\n',encoding='utf-8')
nav=root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md';t=nav.read_text(encoding='utf-8')
t=t.replace('2.2已开始分批校订（序论及坐标定义）','2.2已分批校订至式（2.6）')
t=t.replace('当前仅序论及定义完成页面对照：说明干涉观测用途、五类光源位置及1/m/2坐标和上下行定义。式（2.1）起仍为旧译待校订，当前导读不替代全节内容概括。','当前序论、定义及式（2.1）—（2.6）完成页面对照：说明干涉观测用途、五类光源位置、坐标方向及多重反射场和膜内场。复数模平方转录已修复，原相位和强度关系疑点见Q040，第3部分起仍为旧译待校订。当前导读不替代全节内容概括。')
nav.write_text(t,encoding='utf-8')
bp=mg/'全书调查/分批建议.tsv';rows=list(csv.DictReader(io.StringIO(bp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['节号']=='2.2' and int(row['PDF起页'])<=3:
        row['执行状态']='2026-10-19部分覆盖：B058—B062截至式2.6；第3部分源点/光路分类起待核，不能按p3整页视为完成'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);bp.write_text(buf.getvalue(),encoding='utf-8-sig')
sp=mg/'符号与约定.md';t=sp.read_text(encoding='utf-8');sp.write_text(t+'\n## 第2.2节场表达（B060—B062，2026-10-19）\n\n式2.2的β_m为2π n_m cosθ_m/λ；式2.3及膜内场明确负时间因子。模平方已按底本恢复；r/t仍为场幅，不直接据光强名称补能流权重。Q040相位/复数强度、Q041方向名称与a下标省略问题保留，见本节局部约定卡。\n',encoding='utf-8')
(out/'B060-B062复核.md').write_text('''# B060—B062复核

2026-10-19。已目视核对底本p2—3及公式局部：B060含反射场2.1/2.2和跨页解释；B061含透射场2.3/2.4；B062含膜内场2.5/2.6及方向注释。未截断公式组。

旧译修复：2.1首行相位恢复求和指标n；2.2/2.4恢复分母模平方，2.4恢复分子各项模平方；复共轭改成正确星号上标；ASCII分数与裸数学改为可渲染公式，原编号全部恢复。

原式疑点Q040/Q041不修正；原文“上行+”照录，候选下行移注及附件E-2.2-002。第3部分起与本批备份完全相同，未改图或后续旧译。完成部分共6个编号式、64个数学片段严格解析通过；新批次截图已目视检查，无水平溢出。

目录导读、局部约定、问题表、勘误附件、章节及预排进度已同步。全节未完成；下一批完整处理跨p3—4的源点分类与图3.1，不以页末切断。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

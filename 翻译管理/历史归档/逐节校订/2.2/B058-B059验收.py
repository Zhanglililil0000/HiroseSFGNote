from pathlib import Path
import csv,io,json,hashlib
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'));s=p.read_text(encoding='utf-8')
base=(out/'B058-修订前.md').read_text(encoding='utf-8-sig')
mark='"反射光"中，除在1/m界面反射的光之外'
assert s[s.index(mark):]==base[base.index(mark):]
assert s.count('\n# ')==0
src=root/'日语原版/Chapter2/chap2-2.pdf'
assert src.read_bytes()==(mg/'基线快照/2026-10-16/日语原版/Chapter2/chap2-2.pdf').read_bytes()
r=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert [i['batch'] for i in r['results']]==['B058','B059']
assert all(i['width']==i['scrollWidth'] and not i['overs'] for i in r['results'])
report={'date':'2026-10-19','batches':['B058','B059'],'sourcePages':'p1序论及p1末—p2坐标定义；不含式2.1','mathFragments':r['math'],'sourceHash':hashlib.sha256(src.read_bytes()).hexdigest(),'unrevisedTailUnchanged':True,'horizontalOverflow':False,'sectionComplete':False}
(out/'B058-B059验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
bp=mg/'全书调查/分批建议.tsv';rows=list(csv.DictReader(io.StringIO(bp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['节号']=='2.2' and int(row['PDF起页'])<=2:
        row['执行状态']='2026-10-19部分覆盖：B058序论及B059坐标定义；式2.1起未处理，不能按整页视为已校订'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);bp.write_text(buf.getvalue(),encoding='utf-8-sig')
pp=mg/'当前进度与续接.md';t=pp.read_text(encoding='utf-8').replace('后文47页主体和附录尚未校订','其余主体与附录尚未校订')
pp.write_text(t,encoding='utf-8')
sp=mg/'符号与约定.md';t=sp.read_text(encoding='utf-8')
sp.write_text(t+'\n## 第2.2节开头（B058—B059，2026-10-19）\n\n仅依据p1—2定义部分：z由介质1向介质2，x为传播方向的界面投影；−上行到介质1、+下行到介质2。r/t为场幅系数；r₂m的原文界面名疑误见Q039。其余物理量和后文公式尚未核验，详见校订记录/2.2/局部约定卡.md。\n',encoding='utf-8')
(out/'B058-B059复核.md').write_text('''# B058—B059复核

2026-10-19。已目视对照2.2底本p1—2，仅覆盖完整序论与坐标/符号定义，不含p2的式（2.1）、（2.2）。

五类光源位置保留介质侧/薄膜侧的区分，原文件引用不编造为章节号；重复一级标题已清理。坐标、角度和r/t清单以数学格式及表格重排，未改变已定义方向。Q039原界面名1/m保留，候选2/m移入注释和附件E-2.2-001。

两批31个数学片段严格解析通过，实际截图已查看，表格无水平溢出。式（2.1）前多重反射说明开始至文末，与本轮备份相同；未对后续旧译作批量术语替换或公式清洗。PDF哈希与基线一致。章节清单、预排记录、Preface、第二章导航、符号与疑难记录、勘误附件及续接已同步。

下一批从“反射光”多重反射说明及式（2.1）开始，核对p2—3的反射、透射场和强度；按完整公式组分批。全节仍在处理中。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

from pathlib import Path
import re,json,csv,io
from PIL import Image
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'));s=p.read_text(encoding='utf-8')
old=(out/'B063-修订前.md').read_text(encoding='utf-8');marker='## 4. 光路上的SFG极化'
assert s[s.index(marker):]==old[old.index(marker):]
done=''.join((out/f'B{i:03}-本批译文.md').read_text(encoding='utf-8') for i in range(58,65))
assert done==s[:s.index(marker)]
r=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'));assert len(r['results'])==7
assert all(i['width']==i['scrollWidth'] and not i['overs'] and all(x['loaded'] for x in i['images']) for i in r['results'])
assert len(re.findall(r'^### （[a-f]）',done,re.M))==6
for n,im in enumerate([Image.open(out/'B064-参考渲染.png')]):
    for j,y in enumerate(range(0,im.height,1800),1):im.crop((0,y,im.width,min(y+1800,im.height))).save(out/f'B064-显示分段{j}.png')
report={'date':'2026-10-19','batches':['B063','B064'],'scope':'p3—5，完整第3部分六类源点、图3.1及路径汇总','sourceClasses':6,'restoredImages':3,'completedMathFragments':r['math'],'prefixMatchesBatches':True,'part4OnwardUnchanged':True,'sectionComplete':False}
(out/'B063-B064验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
pref=root/'Preface序言.md';t=pref.read_text(encoding='utf-8');lines=t.splitlines()
for i,line in enumerate(lines):
    if line.startswith('- [2.2 '):lines[i]=line.replace('已至式2.6','已至第3部分末').replace('第3部分起仍待校订。','六类源点、图3.1与光路汇总亦已校订；第4部分起仍待校订。')
pref.write_text('\n'.join(lines)+'\n',encoding='utf-8')
nav=root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md';t=nav.read_text(encoding='utf-8').replace('2.2已分批校订至式（2.6）','2.2已分批校订至第3部分末')
t=t.replace('第3部分起仍为旧译待校订','六类源点、图3.1及跨页流程已补齐，图文对应疑点见Q042；第4部分起仍为旧译待校订')
nav.write_text(t,encoding='utf-8')
bp=mg/'全书调查/分批建议.tsv';rows=list(csv.DictReader(io.StringIO(bp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['节号']=='2.2' and int(row['PDF起页'])<=5:row['执行状态']='2026-10-19部分覆盖：B058—B064，至p5第3部分光路汇总末；第4部分起未核，不按p5整页标完成'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);bp.write_text(buf.getvalue(),encoding='utf-8-sig')
card=out/'局部约定卡.md';t=card.read_text(encoding='utf-8');card.write_text(t+'\n## B063—B064补充\n\n第3部分区分膜内A/B源点及两界面四侧源点；0±与h_m±表示界面侧别。+方向仍按第2部分定义识别，原称上行+照录并注。原图及汇总的B′/B″标记未强制统一，部分流程出射名称不作推导修正版。\n',encoding='utf-8')
(out/'B063-B064复核.md').write_text('''# B063—B064复核

2026-10-19。目视核对底本第3—5页，以完整第3部分为范围，不在页末截断(a)—(f)源点分类。

B063：六类源点坐标、n范围、膜内两种源点的传播相位、界面两侧源点的次数及贡献说明全部转为可读数学和分组文字；“上行+”按底本保留，候选下行只在注释。

B064：恢复图3.1原图及旧译完全遗漏的跨第4—5页流程。中文对照共26个出射分支，分五组，与原图逐行核对；分支续行标明只对应原流程分支，不自行补前序路径。Q042保留B′/B″及出射名称的原文衔接差异，不作统一修正版。

已完成部分累计167个数学片段严格解析通过，3张图正常加载，7批宽度均无水平溢出；本批截图已检查。第4部分及以后与B063前备份相同；章节、导读、分批、疑难、勘误适用位置及续接记录已更新。全节仍未完成。

下一批：p5末—p6的第4部分及4.1开头，将波长标记和坐标分量关系作为一个完整单元，再进入4.1a、4.1b。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

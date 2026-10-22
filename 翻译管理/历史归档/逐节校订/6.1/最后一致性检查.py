from pathlib import Path
import re,json,hashlib,csv,io
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
f=o/'B574-本批译文.md';chunk=f.read_text(encoding='utf-8')
for path in [r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md',r/'翻译管理/疑难与勘误.md']:
 t=path.read_text(encoding='utf-8')
 t=t.replace(r'dt\{P^0(\omega)[e^{-2i\omega t}+1]-P^0(\omega)^*[e^{+2i\omega t}+1]\}',r'dt\{P^0(\omega)[e^{-2i\omega t}+1\}-P^0(\omega)^*[e^{+2i\omega t}+1)]')
 t=t.replace('上一无编号积分式原排印的花括号、方括号闭合混杂；这里只配平分组符号以显示既有两项，未改变项的内容。','上一无编号积分式原排印的花括号、方括号、圆括号闭合混杂，此处亦照录，未配平为修正式。')
 path.write_text(t,encoding='utf-8')
assert chunk in (r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md').read_text(encoding='utf-8')
for name in ['B574验收.json','B574最终检查.json']:
 p=o/name;a=json.loads(p.read_text(encoding='utf-8'));a['translation_sha256']=hashlib.sha256(chunk.encode()).hexdigest();p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
f=r/'Preface序言.md';t=f.read_text(encoding='utf-8');t=re.sub(r'> 本导航由译者编写，不属于作者序言。[^\n]*','> 本导航由译者编写，不属于作者序言。原网站目录于2026-10-16整理，此后随正文逐节更新；具体完成范围以各节状态、阅读导航及翻译管理记录为准。链接存在不单独代表已完成，译校完成也不代表原文疑点已解决。',t,count=1);f.write_text(t,encoding='utf-8')
for name in ['检查合稿.cjs','检查排版.cjs']:
 p=o/name;t=p.read_text(encoding='utf-8').replace("date:'2026-10-21'","date:'2026-10-22'");p.write_text(t,encoding='utf-8')
print('括号原印及说明已同步；B574哈希更新；序言总说明、验收日期已对齐。')

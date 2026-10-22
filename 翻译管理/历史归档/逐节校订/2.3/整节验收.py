from 整节续校工具 import *
from collections import Counter
from urllib.parse import unquote
import pdfplumber
s=TARGET.read_text(encoding='utf-8');tags=re.findall(r'\\tag\{([^}]+)\}',s)
assert len(tags)==21 and len(set(tags))==21,tags
assert len(re.findall(r'\$\$[\s\S]*?\$\$',s[s.index('## 附录D.'):]))==6
assert s.strip().endswith('证毕。')
assert len(re.findall(r'^# ',s,re.M))==1
assert not any(ord(c)<32 and c not in '\n\r' for c in s)
assert '旧译待校订' not in s[:s.index('## 附录A.')]
rows=[]
with pdfplumber.open(ROOT/'日语原版/Chapter2/chap2-3.pdf') as pdf:
 for i,page in enumerate(pdf.pages,1):
  for w in page.extract_words():
   a=re.fullmatch(r'\(([ABC]\.\d+[ab]?)\)',w['text'])
   if a and w['x0']/page.width>.8:rows.append({'page':i,'label':a[1],'representation':'可编辑数学' if a[1] in tags else '缺失'})
assert len(rows)==21 and {x['label'] for x in rows}==set(tags),rows
(OUT/'全节公式编号索引.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'全节公式编号索引.md').write_text('# 2.3全节公式编号索引\n\n由独立PDF右侧编号定位，不把正文引用重复计数。\n\n| PDF页 | 原编号 | 当前形式 |\n|---|---|---|\n'+''.join(f"| {x['page']} | {x['label']} | {x['representation']} |\n" for x in rows),encoding='utf-8')
plain=re.sub(r'\$\$[\s\S]*?\$\$|\$[^$\n]+\$','',s);missing=[]
for link in re.findall(r'\]\(([^\n)]+)\)',plain):
 if re.match(r'https?://|#',link):continue
 if not (TARGET.parent/unquote(link.split('#')[0])).resolve().exists():missing.append(link)
assert not missing,missing
images=re.findall(r'!\[[^\n]*\]\(([^)]+)\)',s)
assert len(images)==5 and len(set(images))==5
assert all('/s03/' in x for x in images)
render=json.loads((OUT/'渲染检查.json').read_text(encoding='utf-8'))
assert {x['batch'] for x in render['results']}=={f'B{i}' for i in range(115,123)}
assert all(not x['overs'] and x['scrollWidth']==1100 and all(y['loaded'] for y in x['images']) for x in render['results'])
sha=hashlib.sha256((ROOT/'日语原版/Chapter2/chap2-3.pdf').read_bytes()).hexdigest();assert sha==SHA
units=[('p1—3至B前','B115','引言、附录A全部；16个编号式及无编号轴分量/边界/强度关系'),('p3—4至C前','B116','附录B全部；B.1/B.2、行驻波、两种复表示及观测量约定'),('p4，C标题至页末','B117','C引言、C.1、均匀介质六个关系单元'),('p5至2c','B118','双介质全部定义与七个透射步骤'),('p5反射段及p6原图','B119','七个反射步骤与第一幅原图'),('p6夹膜标题—p9内部光前','B120','夹膜定义、四幅原图、反射与透射路径、全部C.2/C.3及干涉/条纹'),('p9内部光—p10 D前','B121','两方向路径表、六个内部场式、A/B坐标及双出口传播相位'),('p10—12证毕','B122','附录D限制条件、两侧各三条完整推导')]
(OUT/'全节单元覆盖.md').write_text('# 2.3全节单元覆盖\n\n共享页按论述单元分开核验，不把同页其他内容提前算作已核。\n\n| 独立PDF位置 | 批次 | 内容 |\n|---|---|---|\n'+''.join('| '+' | '.join(x)+' |\n' for x in units)+'\nB123仅关联修复2.2附录的同类转写，另存母本修订前快照；不计为2.3新内容单元。\n',encoding='utf-8')
report={'date':'2026-10-19','pages':12,'source_sha256':sha,'batches':['B115','B116','B117','B118','B119','B120','B121','B122'],'numbered_total':21,'numbered_unique':21,'numbered_missing':[],'D_complete_derivations':6,'figures':5,'all_equations_editable':True,'all_local_references_valid':True,'control_characters':0,'render_overflows':0,'rendered_batches':8,'issues_retained':['Q073','Q074','Q075','Q076','关联2.2 Q044/Q047/Q053—Q058/Q072'],'adopted_provisional_text':'E-2.3-001，加重反射→多重反射','author_formula_corrections_adopted':False,'related_parent_transcription_repair':'B123'}
(OUT/'整节完成复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'整节完成复核.md').write_text('''# 2.3整节完成复核

2026-10-19，独立底本chap2-3.pdf全部12页。源SHA256：`63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384`。

B115—B122已完成引言及附录A—D本轮译校与数学排版，逐段核对独立PDF原页及文字层后复用母本候选译文。不是将母本完成标记直接复制。

| 检查 | 结果 |
|---|---|
| 编号 | 独立PDF右侧21个唯一编号式全部为可编辑数学，无重号/漏号；见全节公式编号索引 |
| 无编号式 | 定义、行驻波、复表示与观测量、双介质1—4c、夹膜路径表/求和、内部场、A/B相位及D六条完整推导均覆盖；见全节单元覆盖 |
| 插图 | p6一幅，p7两幅，p8两幅；全部直接从独立PDF裁切，重复原图保留，图中文字有中文说明；已逐幅目视检查，裁切边界完整 |
| 跨页 | C.2从p7续p8、透射路径p8续p9、A点p9续p10、D中Px/Pz跨页，完整衔接 |
| 显示 | B115—B122八批参考渲染，严格数学语法通过，无公式水平溢出，五幅图片全部加载；最终全文另生成参考预览 |
| 范围 | PDF摘要不变；所有本地引用有效；无制表符/控制字符；一篇一个一级标题，至证毕 |
| 管理 | Preface、第二章导航、章节清单、分批建议、当前进度、复用表、局部/全局约定、疑难与勘误附件已同步 |

本轮新增Q074—Q076，与Q073及原有关联疑点按原式保留，候选未采用。E-2.3-001仅为暂定文字补读“加重反射→多重反射”，非作者认可。没有新采用的原文公式修正。

独立复核发现的母本同类转写遗漏由B123回查原页后修复（角下标、入射点原缺n、两处π_m、D末式n_1和斜线范围），修订前另存。未将转写修复伪装成原文勘误。

本验收确认翻译、覆盖、转写与排版层面的本轮完成；原式未作独立专家代数认证。下一独立2.4底本尚未开始本轮校订，下一新批B124。
''',encoding='utf-8')
for n in range(119,123):
 bid=f'B{n}';coverage=json.loads((OUT/(bid+'-覆盖.json')).read_text(encoding='utf-8'));rr=next(x for x in render['results'] if x['batch']==bid)
 (OUT/(bid+'验收.json')).write_text(json.dumps({'batch':bid,'pages':coverage['pages'],'labels':coverage['labels'],'images':coverage['images'],'page_compared':True,'math_syntax_passed':True,'render_overflows':rr['overs'],'all_images_loaded':all(x['loaded'] for x in rr['images']),'source_formula_correction_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

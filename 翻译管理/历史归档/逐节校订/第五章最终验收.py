from pathlib import Path
import json,re,hashlib,csv,io
from urllib.parse import unquote
import pdfplumber
r=Path(__file__).resolve().parents[2];o=r/'翻译管理/校订记录/第五章收尾';d=r/'中文版本/第五章 张量与对称性'
meta=json.loads((o/'底本及页面.json').read_text(encoding='utf-8'));assets=json.loads((o/'公式图表资源.json').read_text(encoding='utf-8'));batches=json.loads((o/'本轮批次.json').read_text(encoding='utf-8'));render=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'))
assert not render['errors'] and len(render['results'])==95
assert all(x['scrollWidth']<=x['width'] and x['mathOverflow']==0 and all(i['loaded'] for i in x['images']) for x in render['results'])
assert len(batches)==91 and [int(x['批次'][1:]) for x in batches]==list(range(474,565))
titles={s:next(d.glob(s+' *.md')).stem for s in ['5.1','5.2','5.3','5.4','5.5','5.6']}
for m in meta:
 src=r/f'日语原版/Chapter5/chap{m["节"].replace(".","-")}.pdf';assert hashlib.sha256(src.read_bytes()).hexdigest()==m['sha256']
forms=[x for x in assets if x['节']=='5.3'];assert len(forms)==81
assert all(len({x['分量'] for x in forms[i:i+27]})==27 for i in [0,27,54])
assert all(len(x['片段']) in [1,2] for x in forms)
missing=[]
with pdfplumber.open(r/'日语原版/Chapter5/chap5-3.pdf') as pp:
 for pn in range(2,17):
  p=pp.pages[pn-1];lines=p.extract_text_lines();footer=min(x['top'] for x in lines if '分子から空間' in x['text']);head=[x for x in lines if '軸に沿った' in x['text']]
  boxes=[z['框'] for f in forms for z in f['片段'] if z['页']==pn]
  for c in p.chars:
   if not c['text'].strip() or c['top']<(220 if pn==2 else 65) or c['bottom']>=footer:continue
   if any(h['top']-1<=c['top'] and c['bottom']<=h['bottom']+1 for h in head):continue
   if not any(c['x0']>=b[0]-1 and c['x1']<=b[2]+1 and c['top']>=b[1]-1 and c['bottom']<=b[3]+1 for b in boxes):missing.append({'页':pn,'字':c['text'],'top':c['top']})
assert not missing,missing[:20]
mat=[x for x in assets if x['节']=='5.6' and x['页']>=2];assert len(mat)==36
assert sum((x['行数含表头']-1)*(x['列数含行标']-1) for x in mat)==729
alllinks=[];usedimages=[]
for p in [d/(titles[s]+'.md') for s in ['5.3','5.4','5.5','5.6']]+[d/'阅读导航.md',r/'Preface序言.md']:
 t=p.read_text(encoding='utf-8');assert not re.search(r'<!-- (TABLE|GROUPS|MATRICES)',t)
 for match in re.finditer(r'(!?)\[[^\]]*\]\(([^\n]+?)\)',t):
  target=match[2].strip('<>');
  if re.match(r'\w+://',target) or target.startswith('#'):continue
  path=(p.parent/unquote(target.split('#',1)[0])).resolve();assert path.exists(),(p,target)
  alllinks.append(str(path))
  if match[1]:usedimages.append(path)
assert len(usedimages)==151 and len(set(usedimages))==151
for b in batches:
 sec=b['节'];bid=b['批次'];folder=r/f'翻译管理/校订记录/{sec}';p=folder/f'{bid}验收.json';a=json.loads(p.read_text(encoding='utf-8'))
 snapshot=(folder/f'{bid}-本批译文.md').read_text(encoding='utf-8')
 a['译文SHA256']=hashlib.sha256(snapshot.encode('utf-8')).hexdigest()
 if sec=='5.3':a['对象']=[next(x for x in forms if x['序号']==old['序号']) for old in a['对象']]
 else:a['对象']=[next((x for x in assets if x['节']==sec and x.get('页')==old.get('页') and x.get('表')==old.get('表')),old) for old in a['对象']]
 rr=next(x for x in render['results'] if x['name']==bid);assert (folder/f'{bid}-参考渲染.png').exists()
 a.update({'已排版':True,'数学片段语法':next(x['count'] for x in render['syntax'] if x['name']==bid),'图片数':len(rr['images']),'显示检查':'全量自动加载与溢出检查；全原页目视对照、代表排版截图目视核对','验收范围':'中文正文及原式/原表保真图；非全LaTeX版，非独立公式证明'})
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
 (folder/f'{bid}.md').write_text(f'# {bid}｜{sec}\n\n原PDF页：'+ '、'.join(map(str,a['原页']))+'。起止对象及公式片段坐标见本批验收JSON，原文文字定位见覆盖JSON。\n\n正文/表注已翻译并对照；公式/矩阵保留原图，源符号未擅自修正。数学语法与全量图片加载、溢出检查通过；截图见本目录。参考排版采用与合稿相同的图片资源。原页目视、全量自动显示检查及代表截图目视的覆盖范围分别记录，不冒称每个矩阵系数获独立证明。\n\n已起草、已原页对照、已排版。本轮未采用原文修正。\n',encoding='utf-8')
 b.update(a)
(o/'本轮批次.json').write_text(json.dumps(batches,ensure_ascii=False,indent=2),encoding='utf-8')
sectioninfo={'5.3':(16,'B473—B500','81条完整分量式图；含跨页拼接，三个轴组各27式','Q221—Q222'),'5.4':(15,'B501—B514','19张原表图及正文公式；p15无正文','Q223—Q224'),'5.5':(13,'B515—B527','15张原矩阵表图及说明式','Q225—Q227'),'5.6':(37,'B528—B564','36个表块、729个系数位置；首页公式为LaTeX','Q228')}
for sec,(n,br,desc,qs) in sectioninfo.items():
 folder=r/f'翻译管理/校订记录/{sec}';p=d/(titles[sec]+'.md');h=hashlib.sha256(p.read_bytes()).hexdigest()
 rec={'节':sec,'页数':n,'批次':br,'本轮状态':'中文图式版完成','对象范围':desc,'来源SHA256':next(x['sha256'] for x in meta if x['节']==sec),'合稿原始字节SHA256':h,'疑点':qs,'采用原文修正':False,'原页目视':True,'全量自动显示检查':True,'代表排版目视检查':True,'全部公式可编辑LaTeX':False,'独立理论验证':False}
 (folder/'全节验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
 (folder/'全节验收.md').write_text(f'# {sec}全节验收\n\n2026-10-21；全{n}页，{br}。本轮中文图式版完成。\n\n{desc}。{qs}依原文保留，未采用修正。中文正文、标题、表注及覆盖记录已整理；原页均已目视查看，全量检查图片加载与横向溢出，合稿首尾和代表批次截图已目视。检查通过。\n\n公式图式沿用底本内容，未全部转为可编辑LaTeX，未独立证明所有系数正确。摘要、坐标和资源对应见JSON及第五章收尾/公式图表资源.json。\n',encoding='utf-8')
 (folder/'局部约定卡.md').write_text((folder/'局部约定卡.md').read_text(encoding='utf-8')+'\n\n全节补充：本轮'+desc+'。参见共享《符号与约定》第五章后段条目及本目录全节验收。\n' if (folder/'局部约定卡.md').exists() else f'# {sec}局部约定卡\n\n见正文阅读导引、共享《符号与约定》的“第五章后段跨节约定”。{qs}待核；矩阵方向、星号、行列式因子和分量符号不得跨节直接套用。\n',encoding='utf-8')
p=r/'翻译管理/校订记录/5.3/结构与分批计划.md';p.write_text('# 5.3结构与批次完成记录\n\n底本16页，B473—B500完成本轮中文图式版。原目录、第1—3部分在p1；第4部分引言和分子分量关系在p2。c组27式位于p2—p6上端，a组27式位于p6—p10，b组27式位于p10—p16。原无b组标题，译者加检索标题并注明。\n\nB474—B500每批三条完整公式；跨页式拼成同一图。来源框、原页号、分量及资源名逐式登记于第五章收尾/公式图表资源.json。没有继续沿旧页边界将ZXX拆为半式。\n',encoding='utf-8')
for s in ['5.4','5.5','5.6']:
 m=next(x for x in meta if x['节']==s);(r/f'翻译管理/校订记录/{s}/结构与覆盖.md').write_text(f'# {s}结构与覆盖\n\n全{m["页数"]}页已按原页/完整原表分批。各页日语文字清单见第五章收尾/日语文字逐页清单.txt，原表框与行列数见公式图表资源.json；本节覆盖对象为正文全部段落及所有表块，p5.4第15页无正文另有说明。\n\n原页逐页查看，所有大型矩阵按原列组保留；不以简述替代作者段落、不把原作者未解释的表格补成新推导。章节内部导读见中文版本第五章阅读导航。\n',encoding='utf-8')
progress=r/'翻译管理/当前进度与续接.md';t=progress.read_text(encoding='utf-8');t=t.replace('## 当前有效状态：5.3首页完成','## 历史状态：5.3首页完成',1)
new='## 当前有效状态：第五章中文图式版完成（2026-10-21）\n\n全章5.1—5.6共110页完成本轮译校，批次B423—B564。本轮新增B474—B564共91批，完成5.3余下15页和5.4—5.6。5.3有81条完整分量式图；5.4有19张原表图；5.5有15张；5.6有36张、729个系数位置。新增正文资源共151张。四节合稿246个数学片段语法通过，91批及4份合稿全量检查无缺图/横向溢出；全原页已查看、合稿首尾及代表批次截图已目视。\n\n重要交付范围：完成中文正文与原公式图式，未把全部大型公式转成可编辑LaTeX。Q198—Q228保留待核，新Q223—Q228均有就地说明及附件索引，本轮无新增已采用原文修正。序言、全章阅读导航、术语、符号、问题表和章节清单已同步。详见《第五章完成复核.md》及校订记录/第五章收尾。\n\n用户本轮指定范围已完成，未开始第六章。后续继续翻译的入口为6.1《偶极间相互作用》，55页；下一批编号B565。先核原目录和局部符号，再选完整引言/推导单元，不沿5.3的角度和单位制默认套用。\n\n'
t=t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+new,1);progress.write_text(t,encoding='utf-8')
report={'日期':'2026-10-21','第五章总页数':110,'全章批次':'B423—B564','新增批次数':91,'本轮状态':'中文图式版完成','全部公式可编辑LaTeX':False,'新正文图式资源':151,'5.3分量式':81,'5.6矩阵表块':36,'5.6系数位置':729,'5.3图式文字框遗漏':missing,'四节合稿数学片段':sum(x['count'] for x in render['syntax'] if x['name'] in sectioninfo),'渲染对象':95,'缺图':0,'横向溢出':0,'正文及导航链接检查数':len(alllinks),'源PDF摘要匹配':True,'新增疑点':'Q223—Q228','未决总范围':'Q198—Q228','新增采用原文修正':False,'源页目视范围':'5.3—5.6全81页','排版目视范围':'四节首尾及B475/B502/B521等代表截图；其他批次全量自动检查','独立公式证明':False,'后续入口':'6.1 / B565'}
(o/'最终检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(r/'翻译管理/第五章完成复核.md').write_text('# 第五章完成复核\n\n2026-10-21。全章6节110页，本轮中文图式版完成（B423—B564）。本轮新增91批；5.3—5.6的正文、标题及表注完整翻译，大型原公式/矩阵按保真图式交付，未全部转为可编辑LaTeX。\n\n5.3的81条完整分量式逐条登记并拼接跨页；5.4的19张原表、5.5的15张矩阵表及5.6的36张分块表均有原页定位。5.6共有729个系数位置。底本5.4 p15只有页脚。\n\n全量检查原文摘要、分量覆盖、151张正文图、相对链接和数学显示；95份批次/合稿显示检查无缺图或横向溢出。四节合稿246个数学片段通过语法检查；全81页原页已目视，合稿首尾及代表排版已查看。5.3图片曾发现右边界过紧，已统一扩至原页右边界并重新输出，避免字宽元数据误差造成裁切。\n\nQ198—Q228仍为待核，Q223—Q228为本轮新增；本轮没有采用原文修正，勘误附件仅增待核索引，不伪造已确认E编号。术语沿用户决定，新增T099—T101标明译者暂用。跨节保留Z方向、星号、ε及β/χ差异。完成状态不表示原文所有理论断言和矩阵系数均已独立验证。\n\n完整检查数据和资源清单见校订记录/第五章收尾；续接为6.1、B565，尚未开始。\n',encoding='utf-8')
# Preserve only short, unambiguous prose examples in the checked corpus.
(r/'翻译管理/已核验对照语料/第5章.md').write_text('# 第五章已核验对照语料\n\n这里的“核验”指与日语原页的翻译对照，非独立理论审查。未决公式及候选修正不收入。\n\n## 5.4 p4末段：重复表示编号\n\n原文：この番号が同じもの同士が球対称群の既約表現の基底としての組を構成する。\n\n译文：编号相同的基底共同组成球对称群一个不可约表示的基底组。\n\n## 5.6 p1：三角函数写法\n\n原文：なお、次の関係式を使って、三角関数sin2θ、cos2θ、sin3θ、cos3θをsinθ、cosθのべき乗に書き換えることができる。\n\n译文：另外，可以利用以下关系，将sin2θ、cos2θ、sin3θ、cos3θ写成sinθ、cosθ的幂。\n\n原文数学符号按可读字符转写；倍角与幂的区别依原页，非OCR原始串。\n',encoding='utf-8')
resourcehash={str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in usedimages}
(o/'正文图式摘要.json').write_text(json.dumps(resourcehash,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

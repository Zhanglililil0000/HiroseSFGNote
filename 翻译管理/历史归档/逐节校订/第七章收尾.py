from pathlib import Path
import importlib.util,re,json,csv,hashlib,sys
from urllib.parse import quote,unquote
R=Path(__file__).resolve().parents[2]; D=R/'中文版本/第七章 Heinz论文解读'
spec=importlib.util.spec_from_file_location('chapter7',Path(__file__).with_name('第七章续译.py'))
W=importlib.util.module_from_spec(spec);spec.loader.exec_module(W)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,t):p.write_text(t,encoding='utf8')
def link(p,base):return quote(p.relative_to(base).as_posix(),safe='/')
titles={613:'路径积分与薄片跳跃条件',614:'极化薄片的辐射与等介电常数近似',615:'菲涅尔变换及折射率表示',616:'膜内双向场及式21—22',617:'式21证明框全段',618:'表面响应与膜内外场',619:'一般入射几何、辐照度及同尺寸光束',620:'任意光束和高斯重叠',621:'体相非局域展开与四极参数',622:'体相源的等效面极化与相干长度',623:'纵向体相响应与面响应的对应',624:'实验、对称性及原作省略',625:'附录A方向、基本关系与磁场',626:'附录A边界分量与跨页波矢',627:'附录A辐射场求解',628:'附录B方向与s偏振',629:'附录B的s解和p偏振解',630:'附录B膜内总场及有限厚度极限',631:'附录C路径求和',632:'附录C场、系数及零厚度对应',633:'附录D十类独立分量表'}
image_eq={616:['20′b','20′c','20′d','20″b','20″c','20″d'],619:['31','32'],620:['33a','33c'],621:['36','37a','37b','37c','37d'],622:['40'],623:['41','46','47a','47b'],626:['A4e','A4f'],627:['A8a','A8b','A8c','A8d','A8e','A8f','A9a','A9b'],629:['B4a','B4b','B4c','B5','B6'],630:['B8']}
descriptions={
'7.1':'从极化薄片的边界条件推导辐射场，经菲涅尔变换联系外场与膜内场，讨论有限光束、体相多极贡献及与表面响应的区分；末页介绍偏振与表面对称性。',
'7.2':'解除两侧与膜介电常数相同的限制，以六个边界分量方程求两侧s、p偏振辐射振幅，并回到式(17)的特殊极限。',
'7.3':'分别从s、p偏振连续条件求解透射、反射与膜内总场，说明正文式(20)和有限膜厚零厚度极限的关系。',
'7.4':'按传播路径累加多重反射，列出膜两端的双向场和s、p界面系数，再与附录B的零厚度结果对应。',
'7.5':'按1、2、3、4、5、6、7、9、13、14个独立非零分量分组，完整保留各点群的原张量表，注明指标和坐标待核项。'}
def prepare():
    W.write_all()
    f=next(D.glob('7.1 *.md'));t=f.read_text(encoding='utf8')
    t=re.sub(r'> \*\*译校状态（B609，[\s\S]*?\n>\n', '> **译校状态（2026-10-22）：** B609—B624完成底本14页全部正文、证明框和原注；原作省略处明确保留。复杂公式组采用原式图，尚非全部可编辑LaTeX。Q274—Q292待核，未新增已采用修正。\n>\n',t,count=1)
    t=t.replace('先建立极化薄片及膜内电场模型，后续将讨论边界条件、薄片辐射、表面与体相响应。','先读极化薄片模型与边界条件，再读辐射场、菲涅尔变换、表面与体相响应；四个独立附录见本章阅读导航。')
    put(f,t)
    files={s:next(D.glob(s+' *.md')) for s in descriptions}
    nav='# 第七章阅读导航\n\n本章5节、底本共23页，已完成本轮全文翻译、原页对照与排版整理。它是广濑对Heinz综述的解读笔记，不能当作Heinz原章的全文译本。复杂公式保留原式图；原稿明确略去的内容未补写。\n\n'
    for s,p in files.items():nav+=f'- [{p.stem}]({link(p,D)})：{descriptions[s]}\n'
    nav+='\n## 7.1内部阅读路线\n\n'
    parts=[('2.1 唯象模型','界面与体相分开，面源极化由膜内场激发；膜介电常数随频率改变。'),('2.2 极化薄片边界条件','从源电荷、电流与麦克斯韦方程到场的跳跃条件；一般边界条件与δ薄片极限应分开辨认。'),('2.3 极化薄片的辐射','先看等介电常数特例，再以菲涅尔变换纳入线性响应；附录A、B、C分别补一般辐射、场因子和多重反射。'),('2.4 表面非线性响应','联系三种频率的膜内偏振矢量，确定输出方向、辐照度、有限光束功率和重叠因子。'),('2.5 体相非线性响应','多极展开、四极参数、相干长度与等效面源；纵向体相项可能无法与局域表面项分离。'),('2.6 讨论','原作省略。'),('3.1 各向同性介质','镜面对称、偏振组合及四组面张量；对称性表可转查附录D。'),('3.2 各向异性介质','单晶和重构表面；(110)、(111)、(001)表面的二、三、四重旋转对称。后续原作略。')]
    for a,b in parts:nav+=f'- **{a}**：{b}\n'
    nav+='\n## 译校边界\n\nQ274—Q299共26项待核，均有正文就地说明，未转为已确认勘误；详见[勘误附件的待核索引](../附件/原文勘误表.md)。本轮新增Q278—Q299。原文的式号跳跃、附录A与B的场系数差异及张量指标疑点均保留。阅读和应用公式时应先查对应注释；排版通过不代表物理推导已经独立证实。\n\n本章累计B609—B633；本轮续译B613—B633。下一翻译入口为第八章8.1《SFG的光谱线形》，下一批B634。\n'
    put(D/'阅读导航.md',nav)
    pre=R/'Preface序言.md';t=pre.read_text(encoding='utf8')
    start=t.index('### 第 7 章 Heinz 论文解读');end=t.index('### 第 8 章',start)
    repl='### 第 7 章 Heinz 论文解读\n\n**本章导读（本轮全章完成）：** '+descriptions['7.1']+'先读7.1，再按所需推导查7.2—7.4；对称性查7.5。共23页，原作省略及待核疑点均保留，复杂公式并非全部可编辑。详见[第七章阅读导航](中文版本/第七章%20Heinz论文解读/阅读导航.md)。\n\n'
    for s,p in files.items():repl+=f'- [{p.stem}]({link(p,R)})（全节完成）：{descriptions[s]}\n'
    repl+='\n**7.1内部各部分概括：**\n\n'
    for a,b in parts:repl+=f'- {a}：{b}\n'
    put(pre,t[:start]+repl+'\n'+t[end:])
    inventory=R/'翻译管理/章节清单.tsv'
    with inventory.open(encoding='utf8',newline='') as h:
        reader=csv.DictReader(h,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
    bounds={'7.1':'B609—B624','7.2':'B625—B627','7.3':'B628—B630','7.4':'B631—B632','7.5':'B633'}
    for row in rows:
        s=row['编号']
        if s in files:
            row.update({'暂定中文标题':files[s].stem.split(' ',1)[1],'现有译文路径':files[s].relative_to(R).as_posix(),'状态':'本轮全节页面对照及排版整理完成；原式疑难未决','映射核验':f'底本全部页面已按{bounds[s]}对照','公式图表范围':'全部正文、原式、图、原注与原作省略已覆盖；含原式图，非全部可编辑LaTeX','导读状态':'已根据正文更新；见Preface与第七章阅读导航','导读草案':descriptions[s],'结构调查状态':'2026-10-22全页原图与正文对照完成；详见本节校订记录','调查备注':row['调查备注']+'；2026-10-22完成本轮译校，待核问题保留。'})
    with inventory.open('w',encoding='utf8',newline='') as h:
        w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
    # Mirror exactly the local question notes, preserving chapter order.
    questions=[]
    for n,(s,pages,t) in W.batches.items():
        for block in re.findall(r'^>[^\n]*(?:\n>[^\n]*)*',t,re.M):
            m=re.search(r'Q(\d+)',block)
            if m and int(m[1])>=278:
                q='Q'+m[1]
                if q not in [v[0] for v in questions]:questions.append((q,n,s,pages,block))
    qpath=R/'翻译管理/疑难与勘误.md';t=qpath.read_text(encoding='utf8')
    for q,n,s,pages,note in questions:
        if f'## {q}｜' not in t:t+=f'\n\n## {q}｜{s} PDF p'+ '—'.join(map(str,[min(pages),max(pages)] if len(pages)>1 else pages))+f' / B{n} {titles[n]}\n\n'+note.removeprefix('> ')+'\n\n状态：原文保留、待核；候选未采用，未分配E编号。正文有就地说明。\n'
    put(qpath,t)
    epath=R/'中文版本/附件/原文勘误表.md';t=epath.read_text(encoding='utf8')
    if '### 第七章续译B613—B633待核索引' not in t:
        t+='\n\n### 第七章续译B613—B633待核索引\n\n以下为疑点索引，尚未采用原文修正，不分配E编号。按章节及原页顺序增补；各项的原式与候选解释见正文相应Q注。\n\n| 章节及原页 | 问题号 | 待核内容 |\n|---|---|---|\n'
        for q,n,s,pages,note in questions:t+=f'| [{s}](../{link(files[s],R/"中文版本")}) p'+ '—'.join(map(str,[min(pages),max(pages)] if len(pages)>1 else pages))+f' | {q} | {titles[n]}；原印保留，候选未采用 |\n'
    put(epath,t)
    # New terminology is explicitly provisional.
    terms=[('非局在性','nonlocality','非局域性','体相响应中电场空间变化的非局域展开','7.1 p10 / B621'),('longitudinal polarization','longitudinal polarization','纵向极化','本处沿波矢的体相源极化；区别附录A相对界面的垂直分量','7.1 p13 / B623'),('コヒーレント長','coherence length','相干长度','本文反射配置有效源深度；原式因子与记号见Q290','7.1 p12 / B622'),('放射強度（irradiance）','irradiance','辐照度','I为单位面积功率；区别辐射强度和总功率P','7.1 p9 / B619'),('beam waist','beam waist','束腰','高斯光束在界面聚焦时的最小束宽位置','7.1 p10 / B620'),('見かけの面積','effective beam area','有效面积','按P/I⁰定义；不预设几何光斑面积','7.1 p10 / B620'),('多重反射','multiple reflection','多重反射','膜内往返路径及其相干叠加','7.4 p1 / B631'),('振幅反射率','amplitude reflection coefficient','振幅反射系数','场振幅比r；不直接等于功率反射率','7.3 p3 / B630'),('振幅透過率','amplitude transmission coefficient','振幅透射系数','场振幅比t；功率换算另需介质/角度因子','7.3 p3 / B630')]
    termpath=R/'翻译管理/术语表.tsv'
    with termpath.open(encoding='utf8',newline='') as h:
        reader=csv.reader(h,delimiter='\t');tr=list(reader)
    existing={row[0] for row in tr if row}
    for i,(ja,en,zh,definition,loc) in enumerate(terms,133):
        tid=f'T{i:03d}'
        if tid not in existing:tr.append([tid,ja,en,zh,'',definition,loc,'本轮原页对照；非用户新确认','原文语境已核；译名暂用','原页已对照','译者暂用；非用户新确认','底本所列英语或译者辅助释义，非独立英文语料'])
    with termpath.open('w',encoding='utf8',newline='') as h:csv.writer(h,delimiter='\t',lineterminator='\n').writerows(row for row in tr if row)
    symbols='''\n\n## 第七章续译局部约定（B613—B633）

- 波矢的正负以所在推导为准：7.1出射波为k1=pux−q1uz、k2=pux+q2uz；入射激发光的正负相反，不跨段默换。
- Ps为面源，P或Pb为体/空间源；χs²为面二阶非线性极化率。ε′为膜介电常数，撇号不是实部。
- e_i为介质侧偏振矢量，e=F e_i为膜内修正量，一般不再是单位矢量。式27的下标混用见Q284。
- I暂译辐照度，标量P为光功率，粗体P为极化；A=P/I⁰为有效面积。ν为普通频率、n为折射率，λ=c/ν。
- 7.1体相段β、γ、δ、ζ为四极响应唯象参数，不沿用分子超极化率含义。7.3、7.4的β为膜传播相位；同字母不等同。
- 7.2的transverse/longitudinal原括注为相对界面的面内/垂直，区别通常相对波矢的横/纵。原式H系数ω/c与7.3的c/ω不一致，见Q293。
- 7.3上标i/r/t为入射/反射/透射，下标i/m/j为介质；7.4的m与m′区分膜两端，β=(2π/λ0)nd cosθm。
- r、t为场振幅系数；不能直接当作功率反射率、透射率；归一化疑点见Q297。
- 7.5原张量β及各点群坐标未改为宏观χ或另一套常用坐标。指标疑点见Q299。
- 原作内部式号跳跃及明确省略照录；本轮新增Q278—Q299全部未采用修正。
'''
    sp=R/'翻译管理/符号与约定.md';put(sp,sp.read_text(encoding='utf8')+symbols)
    for s in files:
        out=R/f'翻译管理/校订记录/{s}'
        if s!='7.1':put(out/'局部约定卡.md',f'# {s}局部约定卡\n\n'+symbols.split('## 第七章续译局部约定（B613—B633）',1)[1])
        else:
            card=out/'局部约定卡.md';put(card,card.read_text(encoding='utf8')+symbols)
        selected=[n for n,v in W.batches.items() if v[0]==s]
        plan=f'# {s}结构与批次覆盖\n\n底本全部页面本轮译校完成。原作省略照录；以下为本轮新增批次，历史B609—B612见各批记录。\n\n| 批次 | 原页 | 完整单元 |\n|---|---|---|\n'
        for n in selected:plan+=f'| B{n} | '+','.join(map(str,W.batches[n][1]))+f' | {titles[n]} |\n'
        put(out/'结构与分批计划.md',plan)
    # Build whole-document renderer for each final file.
    template=(R/'翻译管理/校订记录/6.1/检查合稿.cjs').read_text(encoding='utf8')
    for s,p in files.items():
        code=template.replace('6.1',s).replace('第六章 偶极间相互作用','第七章 Heinz论文解读').replace(f"'{s} 偶极间相互作用.md'",json.dumps(p.name,ensure_ascii=False))
        code=code.replace('h2,h3','h2,h3,h4')
        code=code.replace('const positions=[0,...metrics.headings.filter(x=>/^(2\\.|3\\.|4\\.|附录|2\\.4 |3\\.2 |1\\.3 )/.test(x.text)).map(x=>Math.max(0,x.y-16)),metrics.height-1000];','const positions=[0,...metrics.headings.map(x=>Math.max(0,x.y-16)),Math.max(0,metrics.height-1000)];')
        put(R/f'翻译管理/校订记录/{s}/检查合稿.cjs',code)
    print(json.dumps({'prepared':True,'questions':len(questions),'new_terms':len(terms)},ensure_ascii=False))

def finalize():
    files={s:next(D.glob(s+' *.md')) for s in descriptions};all_records=[];broken=[]
    locations={278:('7.1 p3式(10)','面内梯度首矢量原为n_z，候选n_x'),279:('7.1 p4式(17)','P_sv与后文P_s不一致'),280:('7.1 p6首段、p10高斯段','不存在的式(29d)及高斯段式(21)引用'),281:('7.1 p6式(22b)','根号内K位置与式(21)不一致'),282:('7.1 p7证明框','重复e_2p标签、波数幂和消失的q分母'),283:('7.1 p8式(24)后及式(26)','ω/c缺平方，膜与体相下标对应不清'),284:('7.1 p8式(27)—(29)','修正前后偏振矢量下标混用及介电参数称谓'),285:('7.1 p9式(31)','频率ω³与后式ω²不一致，ω_i未定义'),286:('7.1 p11手性及偏振选择段','手性判据中的旋转操作及体相段χ_s下标'),287:('7.1 p11式(37d)','四极张量末项缺指标'),288:('7.1 p11末—p12首','沿波矢振荡却称transverse'),289:('7.1 p12式(39)','指数时间项缺t'),290:('7.1 p12式(40)后相干长度段','q_b/q_s及波长、余弦和2π因子'),291:('7.1 p13式(41)、(46)—(47)','两侧贡献符号及未定义投影系数'),292:('7.1 p14镜面对称段','无镜面时三组分量负号和指标配对'),293:('7.2 p1式(A1)—(A2)及后式','H场系数ω/c与附录B的c/ω不同'),294:('7.2 p2式(A6)—p3式(A7)','E_z2正负与图不一致，θ缺下标'),295:('7.2 p3式(A9)前无编号式','介电常数/波数恒等式疑缺k_x因子'),296:('7.3 p2式(B3b)、p3式(B7)','反射场介质下标及xt指标位置'),297:('7.4 p1级数后的关系与闭式','振幅归一化恒等式及重复反射场左端'),298:('7.4 p2的p偏振系数组','t_im分母、t_mj波数和r_jm标签'),299:('7.5 p1的C3、C2及相关点群组','四指标、重复分量及未明坐标约定')}
    qpath=R/'翻译管理/疑难与勘误.md';qt=qpath.read_text(encoding='utf8')
    for num,(loc,desc) in locations.items():qt=re.sub(rf'^## Q{num}｜[^\n]+',f'## Q{num}｜{loc}：{desc}',qt,flags=re.M)
    put(qpath,qt)
    epath=R/'中文版本/附件/原文勘误表.md';et=epath.read_text(encoding='utf8')
    for num,(loc,desc) in locations.items():
        s=loc[:3];entry=f'| [{loc}](../{link(files[s],R/"中文版本")}) | Q{num} | {desc}；原印保留，候选未采用 |'
        et=re.sub(rf'^\|[^\n]*\| Q{num} \|[^\n]*$',lambda m:entry,et,flags=re.M)
    put(epath,et)
    for s,p in files.items():
        text=p.read_text(encoding='utf8')
        for dest in re.findall(r'\]\(([^)]+)\)',text):
            if '://' not in dest and not (p.parent/unquote(dest.split('#')[0])).exists():broken.append([s,dest])
    assert not broken,broken
    for n,(s,pages,t) in W.batches.items():
        out=R/f'翻译管理/校订记录/{s}';p=out/f'B{n}-本批译文.md';t=p.read_text(encoding='utf8')
        render=json.loads((out/'渲染检查.json').read_text(encoding='utf8'));r=next(v for v in render['results'] if v['batch']==f'B{n}')
        assert not r['overs'] and r['scrollWidth']<=r['width'] and all(v['loaded'] for v in r['images'])
        parts=[x.strip() for x in re.split(r'\n\s*\n',t) if x.strip() and not x.lstrip().startswith('<!--')]
        coverage=[{'原文定位':f'{s} PDF p'+','.join(map(str,pages))+' / '+titles[n], '对象序号':i,'译文定位':f'B{n}-本批译文.md第{i}单元','对象摘录':v[:110],'已翻译':True,'已原页对照':True} for i,v in enumerate(parts,1)]
        put(out/f'B{n}-覆盖.json',json.dumps(coverage,ensure_ascii=False,indent=2))
        labels=re.findall(r'\\tag\{([^}]+)\}',t)+image_eq.get(n,[])
        record={'批次':f'B{n}','日期':'2026-10-22','章节':s,'范围':titles[n],'原页':pages,'source_sha256':sha(R/f'日语原版/Chapter7/chap7-{s[-1]}.pdf'),'translation_sha256':sha(p),'覆盖单元':len(parts),'编号式':labels,'原式图及原图数量':len(r['images']),'新增疑点':sorted(set(re.findall(r'Q\d+',t))),'采用原文修正':False,'已原页对照':True,'数学语法':'严格检查通过','已排版':True,'横向溢出':False,'图片全部加载':True,'目视范围':'原页和全部新原式裁图已目视；合稿按标题及首末屏复核','全幅截图逐批目视':False,'全节状态':'本轮全部翻译完成；原文疑点待核'}
        put(out/f'B{n}验收.json',json.dumps(record,ensure_ascii=False,indent=2))
        put(out/f'B{n}最终检查.json',json.dumps(record,ensure_ascii=False,indent=2))
        put(out/f'B{n}.md',f'# B{n} 译校记录\n\n{s} PDF p'+','.join(map(str,pages))+f'：{titles[n]}。\n\n{len(parts)}个译文段落/公式/注释覆盖单元；编号式含原式图标号见验收JSON。全部原页已对照，原注与原作省略保留。疑似错误就地加Q注，未新增已采用勘误。严格数学语法、图片加载与页面宽度通过；合稿抽查并非独立物理证明。\n')
        put(out/f'B{n}术语核对.md',f'# B{n}术语与符号核对\n\n沿用户确定的和频过程、二阶非线性极化率、菲涅尔因子。新增暂译见T133—T141，未冒记为用户确认。局部β/γ及入射/出射方向按本节约定卡；原指标和系数疑点未改写。\n')
        all_records.append(record)
    metrics=[]
    for s,p in files.items():
        out=R/f'翻译管理/校订记录/{s}'
        render=json.loads((out/'全节渲染检查.json').read_text(encoding='utf8'))
        assert not render['overs'] and render['scrollWidth']==1100 and all(v['loaded'] for v in render['images'])
        metrics.append({'section':s,'translated_file':p.relative_to(R).as_posix(),'translated_sha256':sha(p),'source_sha256':sha(R/f'日语原版/Chapter7/chap7-{s[-1]}.pdf'),'math':render['math'],'images':len(render['images']),'screenshots':render['screenshots'],'all_loaded':True,'overflow':False})
    report={'日期':'2026-10-22','范围':'第七章7.1—7.5全部23页','本轮批次':'B613—B633','累计批次':'B609—B633','原页逐页核对':True,'新原式裁图全量目视':True,'合稿标题及首末屏目视':True,'新问题':'Q278—Q299','全章问题':'Q274—Q299','新术语':'T133—T141（译者暂用）','采用原文修正':False,'公式形式':'LaTeX与原式图混排，非全部可编辑','省略':'原作者明确省略处已标明，不视为漏译','broken_links':broken,'sections':metrics,'batches':all_records}
    put(R/'翻译管理/校订记录/第七章全章验收.json',json.dumps(report,ensure_ascii=False,indent=2))
    manifest=[]
    for s in files:
        for p in sorted((R/f'中文版本/assets/{s}').glob('*.png')):manifest.append({'file':p.relative_to(R).as_posix(),'sha256':sha(p)})
    put(R/'翻译管理/校订记录/第七章资源清单.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    math=sum(v['math'] for v in metrics);images=sum(v['images'] for v in metrics)
    summary=f'''# 第七章全章译校完成记录

2026-10-22。底本7.1—7.5共23页，本轮B613—B633续完，累计B609—B633。

- 全部日文正文、括注、引文指引、证明步骤、原图和张量表已覆盖；原作明确省略处按原文保留。
- {math}个数学片段严格语法通过，{images}个图片引用全部加载，5份合稿无横向溢出；新裁图全部目视，三处裁边问题已修复。
- 公式含原式图，尚非全部可编辑LaTeX；源图哈希见资源清单。排版检查不能替代物理推导复核。
- Q278—Q299共22项新增疑点有正文就地说明，问题表与勘误附件同步；本章累计Q274—Q299，均未新增采用修正或E编号。
- T133—T141为9项暂用术语；β/γ、偏振矢量、入射/出射方向、振幅系数局部约定已记录。
- Preface、本章阅读导航、章节清单、各批覆盖/验收与当前续接均已更新。下一入口8.1，批号B634。

重点待核：式(10)单位矢量、式(22b)/(26)/(31)频率因子、式(21)证明、体相相干长度及两侧符号、附录A磁场系数和Ez符号、附录C系数归一化与指标、附录D重复/多余指标。所有候选均未静默替换原式。
'''
    put(R/'翻译管理/校订记录/第七章全章完成记录.md',summary)
    current=R/'翻译管理/当前进度与续接.md';t=current.read_text(encoding='utf8');t=t.replace('## 当前有效状态：7.1 B612完成','## 历史状态：7.1 B612完成',1)
    intro=f'''## 当前有效状态：第七章7.1—7.5全章完成（2026-10-22）

本轮B613—B633完成7.1剩余内容及7.2—7.5四个独立附录；全章23页，累计B609—B633。全部正文、证明、原注、图和张量表覆盖；原作省略处明确保留。

{math}个数学片段严格语法通过，{images}幅图片引用全部加载；各批参考排版及5份合稿检查通过，无横向溢出。全部新原式裁图目视，合稿按标题/首末屏检查；不是每批完整截图逐屏目视，也不代表物理公式已独立证实。复杂公式仍含原式图。

新增Q278—Q299共22项待核，全部保留原文及就地注释，未新增已采用修正/E编号。本章累计Q274—Q299。T133—T141为译者暂用词条；符号卡、Preface各部分导读、导航、清单、勘误附件及各批覆盖/验收/哈希同步。详见校订记录/第七章全章完成记录.md及全章验收JSON。

用户“完成第七章”的范围已完成。下一入口8.1《SFG的光谱线形》，14页，下一批B634。开始前核第八章原题、局部符号与旧译状态；不得默认套用本章高斯单位、β/γ含义或时间因子。

'''
    t=t.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+intro,1);put(current,t)
    print(json.dumps({'complete':True,'math':math,'images':images,'new_batches':len(all_records),'broken_links':broken},ensure_ascii=False))

if __name__=='__main__':
    if '--prepare' in sys.argv:prepare()
    if '--final' in sys.argv:finalize()

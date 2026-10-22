from pathlib import Path
from urllib.parse import quote,unquote
import importlib.util,re,csv,json,hashlib,sys
R=Path(__file__).resolve().parents[2];D=R/'中文版本/第八章 拟合'
spec=importlib.util.spec_from_file_location('ch8',Path(__file__).with_name('第八章续译.py'));W=importlib.util.module_from_spec(spec);spec.loader.exec_module(W)
N={'8.1':'8.1 和频光谱的线形.md','8.2':'8.2 和频光谱分析便览.md','8.3':'8.3 拟合概述.md'}
DESC={'8.1':'从共振与非共振干涉进入分子数估算，再区分均匀、非均匀展宽及激光谱宽；附录A—C给出数学公式、吸收虚部推导和有限脉冲相干性的未完成讨论。','8.2':'汇总单谱带、多谱带模拟公式及分子数估算，重点辨认峰高、线宽、积分强度与背景交叉项；保留与8.1不同的原文结论。','8.3':'由局部线性化和雅可比矩阵介绍最小二乘迭代，列出九类展宽/相干条件的强度与偏导；附录1—3说明高斯权重、宽度定义和正规方程。'}
PARTS={
'8.1':[
('要点1—6','模平方中的背景与带间干涉、相位和符号；展宽条件决定模拟方式。'),('由参数估算分子数','区分响应振幅、峰高、宽度及积分面积；本节与8.2的差异见Q302、Q316。'),('观测谱与分子响应的联系','局域场、取向平均、菲涅尔因子和L系数连接分子与宏观响应。'),('参数与线形函数','区分Γ、γ、非均匀半高半宽及实线形/复响应；归一化问题见Q303、Q304。'),('谱线展宽','以分子群和时间波动区分两类展宽，讨论运动窄化。'),('条件1：无展宽','使用δ函数表示无限窄的响应极限。'),('条件2：仅均匀宽度','复洛伦兹响应、背景色散型干涉和带间交叉项。'),('条件3：仅非均匀宽度','高斯频率分布的极限模型及其宽度、相位疑点。'),('条件4：两类宽度并存','先在电场/响应层面对分子频率分布作卷积，再取模平方。'),('条件5：激光谱宽','按不同频率的相干性，区分平方后积分与积分后平方。'),('附录A','洛伦兹、高斯、δ函数及分布公式；积分范围和根号原印保留。'),('附录B','由相位与能流引入受迫阻尼振子，推导吸收与响应虚部的关系。'),('附录C','从时域响应讨论有限脉冲和傅里叶变换极限；原作者未证明、未解决处照录。')],
'8.2':[('光谱模拟','单谱带和多谱带强度式，以及背景、相位、带间干涉解释。'),('分子数变化','由χ_v、Γ_v讨论峰强和面积，保留峰高宽度运算与积分近似的待核项。')],
'8.3':[('最小二乘与分类','按A/B1/B2分子展宽及a/b1/b2红外条件组织程序。'),('九类程序','(1)Aa；(2)Ab1；(3)Ab2；(4)B1a；(5)B1b1；(6)B1b2；(7)B2a；(8)B2b1；(9)B2b2。'),('基本响应与雅可比','分解复背景，列出对振幅、频率、均匀宽度的偏导。'),('条件2—3','对红外频率相干时先积分后平方，不相干时先平方后积分。'),('条件4—6','固定非均匀宽度，在分子场叠加外再区分单色、相干和不相干红外。'),('条件7—9','把非均匀宽度也作为参数，增加高斯核对Δ_g的导数；跨页展开完整保留。'),('附录1','红外光强与电场分别归一的高斯权重，宽度均以实测光强定义。'),('附录2','非均匀高斯权重及其宽度导数，区别线性谱与和频谱的相对宽度。'),('附录3','残差、雅可比与参数修正的正规方程；可逆性、记号和收敛条件需留意。')]}
LOC={302:('8.1 p2分子数估算','积分范围与χ_v/Γ_v分子数结论'),303:('8.1 p4式(1)、p5式(4)','洛伦兹归一化与实/复g_L混用'),304:('8.1 p4、p7—8、p10式(A3)','高斯归一化根号范围与平方系数'),305:('8.1 p5运动窄化段','NMR样品旋转例子的适用条件'),306:('8.1 p6式(5)后','峰位偏移方向和色散型判据的条件'),307:('8.1 p6式(7)','求和前因子与N、π次幂不一致'),308:('8.1 p7式(10)—(12)','重复φ、β平方、宽度比例及相位区间'),309:('8.1 p8式(13)后','复响应核不能未经说明直接取实δ极限'),310:('8.1 p9式(17)','复响应强度积分未印绝对值符号'),311:('8.1 p10式(A1)—(A5)','积分符号条件、分布意义与极限下标'),312:('8.1 p10—11附录B','拉比周期/频率、弛豫时间的概率表述'),313:('8.1 p12式(B2)、(B6)—(B9)','场/力、时间因子及吸收虚部符号'),314:('8.1 p13式(C2)—(C6)','傅里叶正负号及交叉项次序'),315:('8.2 p1单/多谱带式','ω与ω_IR自变量标签混用'),316:('8.2 p2分子数估算','峰高宽度运算、半轴积分与8.1差异'),317:('8.3 p1—2分类与引用','附录B引用、Aa宽度及B1a比较对象'),318:('8.3 p3基本雅可比','参数下标和实部求和缺写'),319:('8.3 p4条件3、p8附录1','电场与光强的独立归一化关系'),320:('8.3 p4条件4、p6条件7、p7','分子积分截断范围使用红外宽度'),321:('8.3 p8附录2','1/2、1/4宽度用语与高斯平方'),322:('8.3 p9附录3','残差与参数混称、全步迭代收敛条件')}
def put(p,t):p.write_text(t,encoding='utf8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def link(p,base):return quote(p.relative_to(base).as_posix(),safe='/')
def questions():
    result=[]
    for n,v in W.B.items():
        for block in re.findall(r'^>[^\n]*(?:\n>[^\n]*)*',v['text'],re.M):
            m=re.search(r'Q(\d+)',block)
            if m and int(m[1]) in LOC and int(m[1]) not in [q[0] for q in result]:result.append((int(m[1]),n,v['s'],block))
    assert [q[0] for q in result]==list(range(302,323))
    return result
def prepare():
    # Refresh only this turn's translated text; the checked crop files remain intact.
    for n,v in W.B.items():
        put(R/f'翻译管理/校订记录/{v["s"]}/B{n}-本批译文.md',f'<!-- B{n}：PDF p'+','.join(map(str,v['pages']))+'；'+v['title']+'。 -->\n\n'+v['text'])
    for s in N:
        chunks=sorted((R/f'翻译管理/校订记录/{s}').glob('B[0-9][0-9][0-9]-本批译文.md'))
        t='\n\n'.join(re.sub(r'<!-- B\d+结束：[\s\S]*?-->','',p.read_text(encoding='utf8')).strip() for p in chunks)+'\n'
        if s=='8.1':
            t=re.sub(r'> \*\*译校状态（B634，[\s\S]*?\n>\n','> **译校状态（2026-10-22）：** B634—B648完成底本14页全部正文、公式及附录A—C；原作者“未严格证明”和“尚待解决”的内容明确保留。复杂原式使用清晰公式图，非全部可编辑LaTeX；Q300—Q314待核，未采用修正。\n>\n',t,count=1)
            t=t.replace('下文的多谱带干涉、展宽和激光线宽等内容仍待分批译校；不能用本批的简单表达式替代后文各种条件下的计算。','再按均匀/非均匀展宽和激光相干性选择计算次序；附录补充数学、吸收与脉冲讨论。各部分阅读概括见本章导航。')
        put(D/N[s],t)
    nav='# 第八章阅读导航\n\n本章三节、底本共25页，本轮全部翻译、原页对照和排版整理完成。建议先读8.1的模型与条件，再用8.2查公式，最后按8.3条件选择拟合表达式。复杂公式含原式图；这不是对所有原公式的独立物理认证。\n\n'
    for s in N:
        p=D/N[s];nav+=f'## [{p.stem}]({link(p,D)})\n\n{DESC[s]}\n\n'
        for title,desc in PARTS[s]:nav+=f'- **{title}**：{desc}\n'
        nav+='\n'
    nav+='''## 跨节阅读约定

- 8.1前段用Γ，后段用γ；8.3的Γ为均匀宽度，Δ_g与Δ_ir分别为分子非均匀和红外光强的半峰全宽。不能只因同一字母就跨节套值。
- 比较分子数时，8.1的χ_v/Γ_v与8.2的χ_v结论不同，先读Q302、Q316；不把积分面积直接当作分子数。
- 同一红外频率下的分子场叠加，与不同红外频率之间是否相干，是两个层次；九类模型的积分和平方次序均保留。
- MathCad文件夹与程序名按原稿记载，程序没有随这三份PDF给出，本轮未运行其数值代码。
- Q300—Q322共23项仍待核，正文有就地说明，见[勘误附件](../附件/原文勘误表.md)。本轮新增Q302—Q322，未新增已采用修正或E编号。

本章累计B634—B664。本轮续完B635—B664。章节翻译范围已完成；下一阶段建议全书术语、符号、引用及合稿准备复核，尚未执行，不将原文未决问题视为已解决。
'''
    put(D/'阅读导航.md',nav)
    pf=R/'Preface序言.md';p=pf.read_text(encoding='utf8');a=p.index('### 第 8 章 拟合');b=p.index('## 导读的定稿要求',a)
    sec='### 第 8 章 拟合\n\n**本章导读（本轮全章完成）：** 从干涉谱形和展宽模型进入分析便览，再由九种实验条件组织拟合强度和雅可比。共25页，原作未证明的讨论和待核公式均保留。参见[第八章阅读导航](中文版本/第八章%20拟合/阅读导航.md)。\n\n'
    for s in N:
        f=D/N[s];sec+=f'- [{f.stem}]({link(f,R)})（全节完成）：{DESC[s]}\n'
    sec+='\n**各节内部阅读概括：**\n\n'
    for s in N:
        sec+=f'**{s}**\n\n'
        for title,desc in PARTS[s]:sec+=f'- {title}：{desc}\n'
        sec+='\n'
    put(pf,p[:a]+sec+p[b:])
    inv=R/'翻译管理/章节清单.tsv'
    with inv.open(encoding='utf8',newline='') as h:reader=csv.DictReader(h,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
    bounds={'8.1':'B634—B648','8.2':'B649—B650','8.3':'B651—B664'}
    for row in rows:
        s=row['编号']
        if s in N:
            assert row['原文SHA256']==sha(R/f'日语原版/Chapter8/chap8-{s[-1]}.pdf')
            row.update({'暂定中文标题':N[s].removesuffix('.md').split(' ',1)[1],'现有译文路径':(D/N[s]).relative_to(R).as_posix(),'状态':'本轮全节页面对照及排版整理完成；原文疑点未决','映射核验':f'全部页面按{bounds[s]}对照','公式图表范围':'正文、原式及全部附录完整覆盖；含原式图，非全部可编辑LaTeX','导读状态':'已按全文更新Preface与第八章阅读导航','导读草案':DESC[s],'结构调查状态':'2026-10-22本节全部原页对照完成；详见校订记录'})
    with inv.open('w',encoding='utf8',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
    qs=questions();qp=R/'翻译管理/疑难与勘误.md';q=qp.read_text(encoding='utf8')
    for num,n,s,note in qs:
        assert f'## Q{num}｜' not in q
        loc,desc=LOC[num];q+=f'\n\n## Q{num}｜{loc}：{desc}\n\n'+note.removeprefix('> ')+f'\n\n状态：原印保留、待核；候选未采用。来源B{n}，正文有就地说明；不分配E编号。\n'
    put(qp,q)
    ep=R/'中文版本/附件/原文勘误表.md';e=ep.read_text(encoding='utf8')
    e+='\n\n### 第八章续译B635—B664待核索引\n\n以下按章节、原页顺序列疑点；均未采用原文修正，不分配E编号。点击章节位置可查看正文相应Q注。\n\n| 原位置 | 问题号 | 待核内容 |\n|---|---|---|\n'
    for num,n,s,note in qs:
        loc,desc=LOC[num];e+=f'| [{loc}](../{link(D/N[s],R/"中文版本")}) | Q{num} | {desc}；原印保留 |\n'
    put(ep,e)
    # Preserve TSV schema and the user's confirmed terms; new entries remain provisional.
    tp=R/'翻译管理/术语表.tsv'
    with tp.open(encoding='utf8',newline='') as h:terms=list(csv.reader(h,delimiter='\t'))
    updates={'T035':'8.1 p3—8；均匀展宽','T036':'8.1 p2—8、8.3附录2；非均匀展宽','T037':'8.3 p3—8；Δ_ir与Δ_g的光强/分子半峰全宽','T044':'8.1 p8—14、8.3九类模型；区分两种相干层次','T048':'8.3 p1、p8—9；局部线性化与正规方程'}
    for row in terms[1:]:
        if row and row[0] in updates:
            row[6]+='；'+updates[row[0]];row[7]+='；B635—B664原页对照';row[8]='本章语境已核；中文暂用';row[9]='本章原页已对照；其他定位状态另查';row[10]='译者暂用；非用户新确认'
            if row[0]=='T037':row[4]='半高全宽（同义）；本章正文统一半峰全宽'
    new=[('運動による先鋭化','motional narrowing','运动窄化','快速环境变化平均导致的谱线窄化；原NMR例见Q305','8.1 p5'),('衝突による先鋭化','collisional narrowing','碰撞窄化','原文作为窄化的例子，不自行补微观模型','8.1 p5'),('ヤコビアン行列','Jacobian matrix','雅可比矩阵','测量点×参数的一阶偏导矩阵','8.3 p1、p9'),('ラビ周波数','Rabi frequency','拉比频率','原文周期/频率混称见Q312，保留其h约定','8.1 p10—11'),('フーリエ限界','Fourier transform limit','傅里叶变换极限','原作有限脉冲讨论，未严格证明处保留','8.1 p14'),('半値半幅','half width at half maximum','半高半宽','8.1的γ、Δ1/2及8.2的Γ；区别8.3的半峰全宽','8.1 p3、8.2 p1'),('ガウス関数','Gaussian function','高斯函数','归一化与电场/强度权重依原式分别核对','8.1 p4、8.3附录1—2'),('たたみこみ積分','convolution integral','卷积积分','在复响应或电场层面按条件积分，不与强度卷积互换','8.1 p8、p14')]
    for num,(ja,en,zh,definition,loc) in enumerate(new,143):terms.append([f'T{num:03d}',ja,en,zh,'',definition,loc,'B635—B664原页对照；非用户新确认','本章语境已核；译名暂用','原页已对照','译者暂用；非用户新确认','底本所列英语或译者辅助对应，以正文实际列词为准'])
    assert all(len(row)==12 for row in terms if row)
    with tp.open('w',encoding='utf8',newline='') as h:csv.writer(h,delimiter='\t',lineterminator='\n').writerows(row for row in terms if row)
    conventions='''\n\n## 第八章全章局部约定（B635—B664）

- χ^SFG为和频二阶非线性极化率，χ^NR为振动非共振背景；允许电子共振。β_v为单分子二阶响应的一阶超极化率相关矩阵元系数，不能按线性α命名。
- 8.1要点用Γ_v，参数定义及展宽模型改用γ_v；Δ1/2为非均匀半高半宽。8.3的Γ_v为均匀宽度、Δ_g为非均匀半峰全宽、Δ_ir为红外光强半峰全宽。
- T037统一本章“半峰全宽”；“半高全宽”为同义读法。原文只说“半高宽”或“1/2宽度”处不擅补定义，见Q321。
- ω在原文兼称频率、波数；保留原符号，不自行引入2πc转换。ω_IR自变量混用见Q315。
- 实洛伦兹线形和复洛伦兹响应不能因同名g_L互换；高斯根号范围、分布极限及归一化差异均按Q303—Q304、Q309保留。
- 同一频率下分子群的复场叠加，与不同红外频率成分的相干性是两个层次。sqr(Integrn)先积分后平方；Integrn(sqr)先平方后积分。
- 8.3背景E′NR、E″NR是实部与虚部，撇号非导数；星号为复共轭。上标0为中心频率，δ_g、δ_ir为积分偏移。
- F为n×m雅可比，d为m维修正量，vx为n维残差；原文末句混称参数见Q322。
- MathCad/Voight/Voightx/Integrn原拼法和程序名保留，未运行未随PDF提供的程序；原作者未证明、未解决的段落保留。
- 本轮Q302—Q322均未采用修正；章累计Q300—Q322。未跨节统一阻尼、相位或傅里叶符号。
'''
    sp=R/'翻译管理/符号与约定.md';put(sp,sp.read_text(encoding='utf8')+conventions)
    for s in N:
        out=R/f'翻译管理/校订记录/{s}';card=out/'局部约定卡.md'
        put(card,(card.read_text(encoding='utf8') if card.exists() else f'# {s}局部约定卡\n')+conventions)
        plan=f'# {s}结构与批次覆盖\n\n底本全部页面已译校；本轮按完整论述/公式组划批。8.1首批B634另见历史记录。\n\n| 批次 | 原页 | 内容 |\n|---|---|---|\n'
        for n,v in W.B.items():
            if v['s']==s:plan+=f'| B{n} | '+','.join(map(str,v['pages']))+f' | {v["title"]} |\n'
        put(out/'结构与分批计划.md',plan)
    # Whole-document renderer: identical layout machinery to the previously checked chapter.
    template=(R/'翻译管理/校订记录/7.1/检查合稿.cjs').read_text(encoding='utf8')
    for s in N:
        code=template.replace('7.1',s).replace('第七章 Heinz论文解读','第八章 拟合')
        code=re.sub(r'const source=path.join\(dir,.*?\);let md=',lambda m:'const source=path.join(dir,'+json.dumps(N[s],ensure_ascii=False)+');let md=',code,count=1)
        put(R/f'翻译管理/校订记录/{s}/检查合稿.cjs',code)
    print(json.dumps({'prepared':True,'new_questions':len(qs),'new_terms':len(new)},ensure_ascii=False))

def finalize():
    broken=[];sections=[];records=[];alllabels=[]
    for s in N:
        f=D/N[s];out=R/f'翻译管理/校订记录/{s}'
        for p in [f,D/'阅读导航.md']:
            for dest in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf8')):
                if '://' not in dest and not (p.parent/unquote(dest.split('#')[0])).exists():broken.append([p.name,dest])
        render=json.loads((out/'全节渲染检查.json').read_text(encoding='utf8'))
        assert render['scrollWidth']==1100 and not render['overs'] and all(v['loaded'] for v in render['images'])
        sections.append({'section':s,'source_sha256':sha(R/f'日语原版/Chapter8/chap8-{s[-1]}.pdf'),'translation_sha256':sha(f),'translated_file':f.relative_to(R).as_posix(),'math':render['math'],'images':len(render['images']),'all_loaded':True,'overflow':False,'screenshots':render['screenshots']})
    assert not broken,broken
    for n,v in W.B.items():
        s=v['s'];out=R/f'翻译管理/校订记录/{s}';f=out/f'B{n}-本批译文.md';t=f.read_text(encoding='utf8')
        rendered=json.loads((out/'渲染检查.json').read_text(encoding='utf8'));m=next(x for x in rendered['results'] if x['batch']==f'B{n}')
        assert m['scrollWidth']==m['width'] and not m['overs'] and all(x['loaded'] for x in m['images'])
        parts=[x.strip() for x in re.split(r'\n\s*\n',t) if x.strip() and not x.lstrip().startswith('<!--')]
        coverage=[{'原文定位':f'{s} PDF p'+','.join(map(str,v['pages']))+' / '+v['title'],'对象序号':i,'译文定位':f'B{n}-本批译文.md第{i}单元','对象摘录':p[:125],'已翻译':True,'已原页对照':True} for i,p in enumerate(parts,1)]
        put(out/f'B{n}-覆盖.json',json.dumps(coverage,ensure_ascii=False,indent=2))
        qs=sorted(set(re.findall(r'Q\d+',t)),key=lambda q:int(q[1:]))
        record={'批次':f'B{n}','日期':'2026-10-22','章节':s,'范围':v['title'],'PDF原页':v['pages'],'source_sha256':sha(R/f'日语原版/Chapter8/chap8-{s[-1]}.pdf'),'translation_sha256':sha(f),'覆盖单元':len(parts),'编号式':v['labels'],'原式图数量':len(m['images']),'涉及疑点':qs,'采用原文修正':False,'已原页对照':True,'数学语法严格检查':True,'已排版':True,'横向溢出':False,'图片全部加载':True,'目视范围':'全部原页与全部原式裁图；合稿首末屏及标题位置，非逐批全长截图逐屏目视','原作者未完成论证':'按原文保留，不补造'}
        for name in [f'B{n}验收.json',f'B{n}最终检查.json']:put(out/name,json.dumps(record,ensure_ascii=False,indent=2))
        put(out/f'B{n}.md',f'# B{n}校订记录\n\n{s} PDF p'+','.join(map(str,v['pages']))+f'：{v["title"]}。\n\n{len(parts)}个译文段落/原式/注释覆盖单元。完整原页与公式图已对照，原注、程序名、相干性假定及未完成讨论保留；原文疑点未采用修正。语法、图像加载与批次/合稿排版通过。详细覆盖、式号及哈希见本批JSON。\n')
        put(out/f'B{n}术语核对.md',f'# B{n}术语核对\n\n沿用和频过程、二阶非线性极化率、菲涅尔因子及分子一阶超极化率。均匀/非均匀展宽、相干与宽度定义按本章局部约定；T143—T150为暂用，非用户确认。\n')
        records.append(record)
        if s=='8.1':alllabels.extend(v['labels'])
    expected=[str(i) for i in range(1,19)]+[f'A{i}' for i in range(1,6)]+[f'B{i}' for i in range(1,10)]+[f'C{i}' for i in range(1,7)]
    assert len(alllabels)==len(set(alllabels))==38 and set(alllabels)==set(expected)
    put(R/'翻译管理/校订记录/8.1/编号公式覆盖.json',json.dumps({'expected':expected,'covered':alllabels,'missing':[],'duplicates':[],'形式':'原式图与少量LaTeX；无编号公式另按批次覆盖'},ensure_ascii=False,indent=2))
    assets=[]
    for s in N:
        for p in sorted((R/f'中文版本/assets/{s}').glob('*.png')):assets.append({'file':p.relative_to(R).as_posix(),'sha256':sha(p)})
    put(R/'翻译管理/校订记录/第八章资源清单.json',json.dumps(assets,ensure_ascii=False,indent=2))
    math=sum(v['math'] for v in sections);images=sum(v['images'] for v in sections)
    report={'日期':'2026-10-22','范围':'第八章8.1—8.3全部25页','本轮批次':'B635—B664','累计批次':'B634—B664','全部原页对照':True,'全部原式裁图目视':True,'合稿目视':'首末屏及各标题位置，非每批长截图逐屏复核','new_questions':'Q302—Q322，共21项','chapter_questions':'Q300—Q322，共23项','new_terms':'T143—T150，8项译者暂用','采用原文修正':False,'编号公式':38,'原程序运行':False,'物理推导独立认证':False,'broken_links':broken,'sections':sections,'batches':records}
    put(R/'翻译管理/校订记录/第八章全章验收.json',json.dumps(report,ensure_ascii=False,indent=2))
    summary=f'''# 第八章完成复核

2026-10-22。8.1（14页）、8.2（2页）、8.3（9页）共25页完成本轮翻译、原页对照与排版整理。累计B634—B664，本轮B635—B664共30批。

- 8.1正文及附录A—C完整，38个唯一编号式全部入账，无缺号、重复号；原作者未证明和未解决的讨论照录。
- 8.2单/多谱带公式、说明及分子数估算完整；与8.1不同的源结论分别保留。
- 8.3九类条件、跨页雅可比展开及附录1—3完整；MathCad程序名保留，未运行PDF未附的程序代码。
- {math}个数学片段严格语法通过，{images}个原式图引用全部加载，无横向溢出；全部新裁图已目视，截边问题已修复，合稿首末/标题屏检查完成。
- 复杂数学保留原式图，非全部可编辑LaTeX；图像与译稿哈希见资源清单和全章验收。
- 新Q302—Q322共21项待核，正文就地说明、管理问题及勘误附件同步；本章累计Q300—Q322，不新增采用修正/E编号。
- 新T143—T150为8项暂译；沿用并核对原有术语，半峰全宽与半高半宽、Δ_g与Δ_ir、分子与红外频率相干层次分别记录。
- Preface各部分概括、章节导航、清单与续接已更新。

重点待核：分子数归一化与宽度因子、实线形/复响应混用、高斯根号及宽度关系、傅里叶正负号、雅可比求和/参数下标、积分截断变量与残差/参数记号。公式排版检查不代表这些物理、数学疑点已解决。

用户“完成第八章”的范围已完成。后续建议全书一致性复核与合稿准备，本轮未执行；下一批号B665。
'''
    put(R/'翻译管理/第八章完成复核.md',summary)
    cur=R/'翻译管理/当前进度与续接.md';old=cur.read_text(encoding='utf8').replace('## 当前有效状态：8.1 B634完成','## 历史状态：8.1 B634完成',1)
    intro=f'''## 当前有效状态：第八章8.1—8.3全章完成（2026-10-22）

本轮B635—B664完成8.1剩余及8.2—8.3；全章25页，累计B634—B664。8.1的38个编号式、正文/附录A—C，8.2全部便览，以及8.3九类条件与附录1—3完整覆盖。未严格证明/未解决的原作讨论保留，未补造MathCad代码。

{math}数学片段严格语法通过，{images}原式图引用全部加载，三份合稿无横向溢出。全部原页、原式裁图已目视，合稿按首末及标题屏检查；不是逐批长截图逐屏目视，也不是独立物理认证。公式仍部分为图片。

新增Q302—Q322共21项保留原印与就地注释，无新增采用修正/E编号；章累计Q300—Q322。新增T143—T150均暂用，原有T035/T036/T037/T044/T048已核本章语境；符号、勘误索引、Preface逐部分导读、导航、清单、覆盖/验收/哈希同步。

用户“完成第八章”的范围已完成。详见翻译管理/第八章完成复核.md及校订记录/第八章全章验收.json。下一阶段可做全书术语、符号、引用与合稿准备复核，尚未执行；下一批号B665。不能把章节翻译完成等同于未决疑点已确认或全书最终定稿。

'''
    put(cur,old.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+intro,1))
    print(json.dumps({'complete':True,'math':math,'images':images,'unique_numbered_equations':38,'new_batches':len(records),'new_questions':21,'broken_links':broken},ensure_ascii=False))
if __name__=='__main__':
    if '--prepare' in sys.argv:prepare()
    if '--final' in sys.argv:finalize()

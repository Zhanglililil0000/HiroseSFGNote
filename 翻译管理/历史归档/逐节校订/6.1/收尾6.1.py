from pathlib import Path
import re,json,hashlib,csv,io
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;d=r/'中文版本/第六章 偶极间相互作用';p=d/'6.1 偶极间相互作用.md'
date='2026-10-22'
rr=json.loads((o/'渲染检查.json').read_text(encoding='utf-8'))
for metric in rr['results']:
 assert metric['scrollWidth']==1100 and not metric['overs'],metric['batch']
 assert all(x['loaded'] for x in metric['images']),metric['batch']
assert rr['math']==902
chunks=sorted(o.glob('B*-本批译文.md'));chunks=[f for f in chunks if 565<=int(f.name[1:4])<=608]
assert len(chunks)==44
t=p.read_text(encoding='utf-8')
assert all(f.read_text(encoding='utf-8') in t for f in chunks[2:])
assert '局域场因子' in t and '6.1底本PDF p55' in t
t=re.sub(r'> \*\*译校状态[^\n]*',f'> **译校状态（B565—B608，{date}）：** 底本55页的原目录、正文1—4及附录A—F已完成本轮中文译校。一般公式采用LaTeX，18个编号公式组及部分复杂无编号式采用原式图，另保留9幅原图，共31个图像资源；未全部转成可编辑公式。Q229—Q273待核，未将疑点静默改为修正式。',t,count=1)
t=t.replace('### 1.2 线性极化率（PDF p4起；分批译稿）','### 1.2 线性极化率（PDF p4—10）')
t=re.sub(r'> \*\*阅读导引（译者，分批稿）：\*\*[^\n]*','> **阅读导引（译者）：** 第1部分比较经典与量子线性响应、旋波近似，以及吸收与辐射强度；第2部分由两个振子走向晶格、覆盖度和CPA；第3部分建立三频局域场下的和频响应，3.3—3.5仍是原作提纲；第4部分汇总公式。附录A—D用于核对偶极场、镜像和多层边界，E—F供公式与术语查阅。局部符号、时间因子和单位制依原文分别保留。详见[本章阅读导航](阅读导航.md)。',t,count=1)
p.write_text(t,encoding='utf-8')
sourcehash=hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest();newchunks=chunks[5:]
for f in newchunks:
 s=f.read_text(encoding='utf-8');bid=f.name[:4];a=json.loads((o/f'{bid}验收.json').read_text(encoding='utf-8'))
 assert a['source_sha256']==sourcehash
 a.update({'translation_sha256':hashlib.sha256(s.encode()).hexdigest(),'已排版':True,'数学语法':'严格模式通过','图像加载':'全量通过','横向溢出':False,'目视范围':'所有原文页与所有原式裁切；译文代表版面抽查。非每一译文截图逐像素检查。','验收日期':date})
 for name in [f'{bid}验收.json',f'{bid}最终检查.json']:(o/name).write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
 (o/f'{bid}.md').write_text(f'# {bid}｜6.1分批记录\n\n范围：{a["范围"]}。覆盖{a["覆盖块"]}个译文块，原页逐段对照；跨页内容按完整论述接续。\n\n数学严格语法与显示宽度检查通过，资源加载通过；原式图裁切全部目视，译文代表版面抽查。原文疑点：'+('、'.join(a['疑点']) or '无新增')+'。无新增已采用修正。该记录不是独立物理推导认证。\n',encoding='utf-8')
# 所有143个原编号对象：124个LaTeX标签、18个原式图编号组、1个表。
image_ids={'B582':['2.2.6','2.2.9','2.2.10'],'B583':['2.3.4'],'B591':['3.6','3.7','3.8','3.9','3.10'],'B592':['3.14'],'B593':['3.18'],'B601':['C.2'],'B604':['D.2a','D.3a','D.4a'],'B605':['D.5a','D.6a','D.7a']}
inventory=[]
for f in chunks:
 s=f.read_text(encoding='utf-8');bid=f.name[:4]
 for tag in re.findall(r'\\tag\{([^}]+)\}',s):inventory.append({'原编号':tag,'批次':bid,'呈现':'LaTeX','路径':p.relative_to(r).as_posix(),'已原页对照':True})
 for tag in image_ids.get(bid,[]):inventory.append({'原编号':tag,'批次':bid,'呈现':'原式图','路径':p.relative_to(r).as_posix(),'已原页对照':True})
inventory.append({'原编号':'A.2','批次':'B597','呈现':'中文表格','路径':p.relative_to(r).as_posix(),'已原页对照':True})
assert len(inventory)==143 and len({x['原编号'] for x in inventory})==143
(o/'全节公式账本.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
# 待核疑点由就地注原文登记，不分配已采用修正E编号。
issues=[]
for f in newchunks:
 s=f.read_text(encoding='utf-8');loc=re.search(r'<!-- 原文定位：(.*?) -->',s).group(1)
 for line in s.splitlines():
  if not line.startswith('>'):continue
  m=re.search(r'Q(\d+)',line)
  if m and 237<=int(m.group(1))<=273:issues.append((int(m.group(1)),f.name[:4],loc,line.lstrip('> ')))
assert sorted(x[0] for x in issues)==list(range(237,274))
qfile=r/'翻译管理/疑难与勘误.md';qt=qfile.read_text(encoding='utf-8')
for q,bid,loc,note in issues:
 if f'## Q{q}｜' not in qt:qt+=f'\n\n## Q{q}｜6.1 {loc}\n\n{note}\n\n状态：原文保留、待核；候选未采用。来源{bid}，正文有就地说明。\n'
qfile.write_text(qt,encoding='utf-8')
efile=r/'中文版本/附件/原文勘误表.md';et=efile.read_text(encoding='utf-8')
if '### 6.1 B570—B608新增待核索引' not in et:
 et+='\n\n### 6.1 B570—B608新增待核索引\n\n以下均为待核项，保留原文，未采用修正，不分配E编号。原有Q229—Q236继续保留。疑点与候选详见[6.1正文](../第六章%20偶极间相互作用/6.1%20偶极间相互作用.md)及翻译管理。\n\n| 问题号 | 原范围/批次 | 疑点概要 |\n|---|---|---|\n'
 for q,bid,loc,note in issues:
  brief=note.split('：',1)[-1].replace('|','／')
  et+=f'| Q{q} | {loc} / {bid} | {brief[:150]} |\n'
efile.write_text(et,encoding='utf-8')
# 术语登记：保留12列，暂用不等于用户确认。
tf=r/'翻译管理/术语表.tsv';rd=csv.DictReader(io.StringIO(tf.read_text(encoding='utf-8-sig')),delimiter='\t');fields=rd.fieldnames;rows=list(rd)
newterms=[('自己無撞着場','self-consistent field','自洽场','SCF；不将规则晶格q分量闭合直接等同SCF','p21—23、28—32、54'),('平均場近似','mean field approximation','平均场近似','MFA；分子场近似为本词条别名','p31—32、54'),('コヒーレントポテンシャル近似','coherent potential approximation','相干势近似','CPA；原文英文另有Potenshal/field写法，见Q273','p25、31—33、54'),('被覆率','coverage','覆盖度','与物种混合浓度分开；并非自动等于数密度','p14、27—33、42'),('ホットバンド','hot band','热带','振动激发态的吸收带，区别基频带','p33、40、42'),('誘導放出','stimulated emission','受激发射','与自发辐射分开；极化率共振项可取相反号','p33、40、42'),('intensity borrowing','intensity borrowing','强度借用','描述谱带强度重新分配','p33'),('intensity suppression','intensity suppression','强度抑制','不改写为物种布居减少','p33、42'),('ホモダイン検出','homodyne detection','零差检测','本段同频相干光混合','p13—14'),('ヘテロダイン検波','heterodyne detection','外差检测','本段不同频相干光混合','p13—14'),('局部発振','local oscillator','本振','与和频场干涉的参考场EL','p14'),('反電場','depolarization field','退极化场','宏观形状场E1','p55'),('反電場係数','depolarization factor','退极化因子','Ni，非分子数N','p55'),('ブリルアンゾーン','Brillouin zone','布里渊区','q空间积分区域，不与实空间晶胞混用','p32—33'),('タイトバインディングモデル','tight-binding model','紧束缚模型','此处是最近邻耦合类比','p24—25'),('モル屈折','molar refraction','摩尔折射度','R0；与折射率n分开','p55')]
for idx,(ja,en,zh,context,loc) in enumerate(newterms,113):
 tid=f'T{idx:03}'
 if any(x['术语编号']==tid for x in rows):continue
 row={k:'' for k in fields};row.update(dict(zip(fields,[tid,ja,en,zh,'',context,'6.1 '+loc,'B570—B608原页对照；非独立术语规范认证','本节语境已核；译名暂用','原页已对照','译者暂用；非用户新确认','英文原文所列或译者辅助对应；以正文实际记载为准'])))
 rows.append(row)
for row in rows:
 if row['术语编号'] in ['T104','T105','T106']:
  row['定义与适用语境']={'T104':'中心真实偶极自身的镜像，区别其他偶极的镜像；边界条件及k定义按所在部分。','T105':'用于相应介质区域求场的等效虚拟电荷，无独立物理实体。','T106':'真实偶极的等效镜像，不赋予独立分子极化率。'}[row['术语编号']]
  row['原文位置']+='；6.1 p15、33—35、附录A—D / B576—B605';row['状态']='正文语境已核；译名暂用'
b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);tf.write_text(b.getvalue(),encoding='utf-8')
(o/'本轮术语与符号复核.md').write_text('# B570—B608术语与局部约定\n\n- T113—T128新增暂用；T104—T106由目录定位推进为正文核对。T012局域场、T039简正振动及既有用户译名沿用。\n- 2.2选exp(+iωt)，2.3及和频推导重新用exp(-iωt)。不强行改号统一。\n- γ先为阻尼率，附录F末为局域场因子；β在振子方程为阻力参数，和频β为一阶超极化率。\n- 附录D的αij、βij为界面电荷系数；ε星为膜介电常数名称，电荷上的星/撇是序列标签；附录E的星才按定义为复共轭。\n- 附录A面内ρ与密度矩阵ρ、附录F密度ρ分开；N、Ni、NA依词条定义。\n- 附录B分开保留cgs esu与MKSA；附录F的相对ε与绝对ε/ε0不自动合并。\n- 原作3.3—3.5的未完成提纲和3.6省略，不补推导；历史性“尚无实验”等不改写成当代文献判断。\n- 37个新待核Q237—Q273均未采用修正，未增加E编号。\n',encoding='utf-8')
for f in [o/'局部约定卡.md',r/'翻译管理/符号与约定.md']:
 s=f.read_text(encoding='utf-8');mark='## 6.1 B570—B608收尾约定'
 if mark not in s:s+='\n\n'+mark+'\n\n'+(o/'本轮术语与符号复核.md').read_text(encoding='utf-8').split('\n\n',1)[1]
 f.write_text(s,encoding='utf-8')
print('验收、143个公式编号账本、37个待核项、128条术语登记完成；导读与全节复核随后更新。')

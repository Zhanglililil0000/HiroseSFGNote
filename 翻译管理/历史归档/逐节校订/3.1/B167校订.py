from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B167-修订前.md').exists();(o/'B167-修订前.md').write_text(old,encoding='utf-8')
a=old.index('**m/2 界面的 2 侧：**');b=old.index('**m/2 界面的 m 侧：**',a);prior=old[a:b];eqs=re.findall(r'\$\$([\s\S]*?)\$\$',prior);assert len(eqs)==8
# The independently page-checked numerators are three transmission factors and a propagation exponential.
parts=[]
for f,axis in [('vis',r'\alpha'),('ir',r'\beta')]:
 A=f"r_{{1m',{f},{axis}}}";B=f"r_{{m'm,{f},{axis}}}";C=f"r_{{m2,{f},{axis}}}";X=f"e^{{2i\\beta_{{m',{f}}}h_{{m'}}}}";Y=f"e^{{2i\\beta_{{m,{f}}}h_m}}"
 num=f"t_{{1m',{f},{axis}}}t_{{m'm,{f},{axis}}}t_{{m2,{f},{axis}}}e^{{i(\\beta_{{m',{f}}}h_{{m'}}+\\beta_{{m,{f}}}h_m)}}"
 den=r'\begin{aligned}&1+'+A+B+X+r'\\&\quad+('+B+'+'+A+X+')'+C+Y+r'\end{aligned}'
 parts.append(r'\frac{'+num+'}{'+den+'}')
def equation(tag,phase):
 return r'''\begin{aligned}
E_{vis,\alpha}(h_{m'}+h_m^+)E_{ir,\beta}(h_{m'}+h_m^+)
 &=E^0_{vis,\alpha}E^0_{ir,\beta}\\
 &\quad\times '''+parts[0]+r'''\\[6pt]
 &\quad\times '''+parts[1]+r'''\\[6pt]
 &\quad\times\exp\!\Bigl['''+phase+r'''
 (h_m\tan\theta_{m,SF}+h_{m'}\tan\theta_{m',SF})\\
 &\hspace{7em}\times(-k_{m,ir}\sin\theta_{m,ir}
 -k_{m,vis}\sin\theta_{m,vis})\Bigr]
\end{aligned}
\tag{'''+tag+'}'
formulas=[equation('2.3','2ni'),equation('2.4','i(2n+1)')]
def norm(s):
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s);s=re.sub(r'\\\\(?:\[[^\]]*\])?','',s);s=re.sub(r'\\hspace\{[^}]*\}','',s);s=re.sub(r'\\(?:quad|qquad|times|Bigl|Bigr)','',s);s=re.sub(r'\\[,!]','',s);return re.sub(r'[\s{}&]','',s)
assert norm(''.join(eqs[:4]))==norm(formulas[0]);assert norm(''.join(eqs[4:]))==norm(formulas[1])
text='**m/2界面的2侧：**\n\n（a）：$E^+$ 源。\n\n$$\n'+formulas[0]+'\n$$\n\n（b）：$E^-$ 源（$n>0$ 时，经反射）。\n\n$$\n'+formulas[1]+'\n$$\n\n'
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B167完成原目录、引言、第1部分系数及2.1至m/2界面2侧的式(2.1)—(2.4)（PDF p1—4）；m/2界面m侧起仍为旧译待校订。Q096—Q097保留原文并就地说明。',new);p.write_text(new,encoding='utf-8');assert new[new.index('**m/2 界面的 m 侧：**'):]==old[b:]
(o/'B167-本批译文.md').write_text(text,encoding='utf-8');sha=hashlib.sha256((r/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
coverage={'batch':'B167','date':'2026-10-20','pages':[4],'units':'m/2界面2侧源分类(a)/(b)与完整式2.3—2.4','tags':['2.3','2.4'],'source_images_visually_checked':True,'formula_factors_checked_after_layout_normalization':True,'source_sha256':sha,'new_source_issues':[],'source_corrections_adopted':False,'unchanged_tail':'m/2界面m侧及以后'}
(o/'B167-覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B167.md').write_text('# B167：3.1的m/2界面2侧\n\n2026-10-20，PDF p4。原页逐项核源分类(a)E⁺、(b)E⁻（n>0，经反射）及式2.3—2.4。保留两频率各三个t因子和前向传播指数，共同分母不变；两式路径相位分别为2ni及i(2n+1)，不擅自添加反射因子或改n的范围。原位置记号h_m′+h_m⁺照录，未改写为新定义的坐标。八个旧展示块合为两个可编辑编号式，仅分行，全部因子经格式归一化比对一致。无新增原文疑点，无原文修正。m侧及以后逐字保持。\n',encoding='utf-8')
def append(f,t):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
append(o/'局部约定卡.md','## B167补充\n\nm/2界面2侧的原场位置写h_m′+h_m⁺；式2.3列E⁺源，式2.4列E⁻源（n>0，经反射）。两频率各保留t1m′·tm′m·tm2及exp[i(βm′hm′+βmhm)]，路径相位分别为2ni与i(2n+1)。不因源方向而自行补反射系数，也不将n条件改为其他范围；其明确计数定义仍待后文。')
append(o/'结构与复用核验表.md','## B167执行更新\n\np4的m/2界面2侧(a)/(b)及式2.3—2.4均已核。下一单元m侧式2.5跨p4—5，须接全红外分式和相位再结束；2侧已核不能扩展为整个m/2界面完成。')
progress=m/'当前进度与续接.md';s=progress.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);progress.write_text(h+'\n\n## 当前有效状态：B167完成3.1的式2.3—2.4（2026-10-20）\n\n已核p4的m/2界面2侧两种源分类及完整式2.3—2.4；三重透射乘积、前向传播指数及路径相位2ni/i(2n+1)逐项保留。无新增原文疑点或修正；m/2界面m侧起仍为旧译。\n\n下一批B168：核m/2界面m侧源分类及式2.5，跨p4—5接全两频率分式与相位；重点核(1+rm2)和源方向分类，止于m′/m界面m′侧之前。n明确含义仍待原文核实。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B167已核第1部分及2.1式2.1—2.4；m/2界面m侧起待校订','映射核验':'p1—4已核至m/2界面2侧式2.4末；后续据原目录定位','公式图表范围':'25组无编号展示式及完整编号式2.1—2.4已核；后续待核','导读状态':'已更新B167范围；后续仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
pref=r/'Preface序言.md';s=pref.read_text(encoding='utf-8-sig').replace('B163—B166已核第1部分及2.1引言、式2.1—2.2；后续待校订','B163—B167已核第1部分及2.1引言、式2.1—2.4；后续待校订');pref.write_text(s,encoding='utf-8')
nav=p.parent/'阅读导航.md';s=nav.read_text(encoding='utf-8-sig').replace('当前3.1开篇、第1部分及2.1前两式B163—B166','当前3.1开篇、第1部分及2.1前四式B163—B167').replace('m/2界面2侧式2.3起仍待逐项核对。','m/2界面2侧式2.3—2.4已核，分别保留正反向源分类及两种路径相位；m/2界面m侧式2.5起仍待逐项核对。');nav.write_text(s,encoding='utf-8')
print(json.dumps(coverage,ensure_ascii=False))

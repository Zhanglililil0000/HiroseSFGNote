from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B165-修订前.md').exists();(o/'B165-修订前.md').write_text(old,encoding='utf-8')
a=old.index('## 2. 二层系');b=old.index("**1/m' 界面的 m' 侧：**",a);prior=old[a:b]
q='''> **原文疑点（Q097，PDF p3，2.1引言）：** 本段位于二层系1/m′/m/2中，却同时提及三层记法中的m/m″界面。原文还引用《二层膜产生的和频光（SFG）》第4节及《叠层膜产生的和频过程（SFG）》第4节；这些文件名与本文或本地文件的对应尚未确认，不据此重定向到某个本地节号。此处保留界面名称、引用文件名和节号。m/m″的提及是否为兼顾后文三层系，留待后续核验。
'''
text='''## 2. 二层系（1/m′/m/2）产生的和频光

### 2.1 电场振幅的乘积

下面给出可见光电场与红外光电场的乘积。其中，相位部分按和频光路径在最外表面反射的情况给出；若还需要计入m′/m界面及m/m″界面处的反射，则必须另行考虑。关于公式的推导，请参阅文件《二层膜产生的和频光（SFG）》第4节或《叠层膜产生的和频过程（SFG）》第4节。

'''+q+'''
**1/m′界面的1侧：**

（a）：$E^+$ 源（经反射和透射）以及 $E^-$ 源（$n=0$ 时）。

'''
# Expand both frequency branches explicitly, without introducing physical shorthand.
parts=[]
for freq,axis in [('vis',r'\alpha'),('ir',r'\beta')]:
 A=f"r_{{1m',{freq},{axis}}}";B=f"r_{{m'm,{freq},{axis}}}";C=f"r_{{m2,{freq},{axis}}}"
 X=f"e^{{2i\\beta_{{m',{freq}}}h_{{m'}}}}";Y=f"e^{{2i\\beta_{{m,{freq}}}h_m}}"
 num=r'\begin{aligned}&(1+'+A+')[\,(1+'+B+X+r')\\&\qquad+('+B+'+'+X+')'+C+Y+r'\,]\end{aligned}'
 den=r'\begin{aligned}&1+'+A+B+X+r'\\&\quad+('+B+'+'+A+X+')'+C+Y+r'\end{aligned}'
 parts.append(r'\frac{'+num+'}{'+den+'}')
formula=r'''\begin{aligned}
E_{vis,\alpha}(0^-)E_{ir,\beta}(0^-)
 &=E^0_{vis,\alpha}E^0_{ir,\beta}\\
 &\quad\times '''+parts[0]+r'''\\[6pt]
 &\quad\times '''+parts[1]+r'''\\[6pt]
 &\quad\times\exp\!\Bigl[2ni
 (h_m\tan\theta_{m,SF}+h_{m'}\tan\theta_{m',SF})\\
 &\hspace{7em}\times(-k_{m,ir}\sin\theta_{m,ir}
 -k_{m,vis}\sin\theta_{m,vis})\Bigr]
\end{aligned}
\tag{2.1}'''
text+='$$\n'+formula+'\n$$\n\n'+'''> **译校说明：** 式(2.1)从PDF p3接至p4，合为一条可编辑公式；分子、分母及指数仅分行，所有因子与原层标保留。原文此处仅在源的分类中标出n=0，尚未单独定义n；不把它解释为折射率或自行补定其计数含义。此处保留的 $k_{m,ir}$、$k_{m,vis}$ 和相应角标未改写为其他层指标。“最外表面”原文为“最外面”，旧译“最小侧面”已据原文纠正，属于翻译错误修复。

'''
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B165完成原目录、引言、第1部分系数及2.1引言与1/m′界面1侧的式(2.1)（PDF p1—4）；1/m′界面m′侧起仍为旧译待校订。Q096—Q097保留原文并就地说明。',new);new=new.replace('后续内容目前仅完成目录定位，尚未完成公式校订。','其余后续内容目前仅完成目录定位，尚未完成公式校订。');p.write_text(new,encoding='utf-8');assert new[new.index("**1/m' 界面的 m' 侧：**"):]==old[b:]
(o/'B165-本批译文.md').write_text(text,encoding='utf-8')
sha=hashlib.sha256((r/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
coverage={'batch':'B165','date':'2026-10-20','pages':[3,4],'units':'2.1引言、源分类(a)、1/m′界面1侧完整跨页式2.1','tags':['2.1'],'source_images_visually_checked':True,'source_sha256':sha,'unresolved':['Q097'],'source_corrections_adopted':False,'unchanged_tail':'1/m′界面m′侧及以后逐字保持'}
(o/'B165-覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B165.md').write_text('# B165：3.1的2.1开篇及式(2.1)\n\n2026-10-20；PDF p3—4。原图核对可见光及红外光两分式与完整路径相位。保留乘积次序、频率/轴向指标、指数符号和m层k/θ指标；未采用原式修正。四个原分离展示块接为一条带编号公式，长分式与指数仅分行，无省略或代入简写。英文源分类译出，n只保留原条件不补定义。“最小侧面”据原文纠正为“最外表面”。Q097记录二层引言中的m/m″界面及引用对应未决。后续从m′侧式2.2开始，未改。\n',encoding='utf-8')
def append(path,t):path.write_text(path.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
append(m/'疑难与勘误.md',q[2:]);append(o/'局部约定卡.md','## B165补充\n\n式2.1处的vis/ir分别为可见光/红外光，α/β为两激发场的坐标分量指标；β带层和频率下标时为传播相位参数，不与该分量指标或分子超极化率混同。0⁻为1/m′界面1侧的原记法。路径相位按最外表面反射给出，内部界面反射须另计；保留原式m层k与θ，不补换层标。源分类中的n仅保留条件，定义待后文核实。Q097保留m/m″及文献名，不静默统一成二层记法。')
append(o/'结构与复用核验表.md','## B165执行更新\n\n2.1引言和1/m′界面1侧的式2.1（p3—4）已完整接续；尚未核m′侧式2.2。相位限制与Q097已就地注明。下一批从p4式2.2完整单元开始，不能把同页其他源点一并标为已核。')
progress=m/'当前进度与续接.md';s=progress.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);progress.write_text(h+'\n\n## 当前有效状态：B165完成3.1的2.1引言与首式（2026-10-20）\n\n已核p3—4的2.1引言、1/m′界面1侧源分类(a)及式2.1；可见光分式、红外光分式和路径相位全部接全。Q097保留m/m″界面称谓及未匹配的文件第4节引用，不采用原文修正。旧译最小侧面改为最外表面，属误译修复。\n\n下一批B166：核p4的1/m′界面m′侧源分类及式2.2，逐项核t1m′、共同分母和相位，止于m/2界面2侧之前。n的含义仍待本节原文明确，不先补定义。后续旧译原样保留。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B165完成第1部分及2.1引言/式2.1；m′侧式2.2起待校订','映射核验':'p1—4已核至1/m′界面1侧式2.1末；后续据原目录定位','公式图表范围':'25组无编号展示式及完整编号式2.1已核；后续待核','导读状态':'已更新B165范围；后续仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
pref=r/'Preface序言.md';s=pref.read_text(encoding='utf-8-sig').replace('B163—B164已核目录、引言及第1部分全部系数；第2部分起待校订','B163—B165已核第1部分及2.1引言、式2.1；后续待校订');pref.write_text(s,encoding='utf-8')
nav=p.parent/'阅读导航.md';s=nav.read_text(encoding='utf-8-sig').replace('当前3.1开篇及第1部分B163—B164已完成本轮译校','当前3.1开篇、第1部分及2.1首式B163—B165已完成本轮译校').replace('第2部分起仍待本轮逐项核对。','2.1引言及1/m′界面1侧的式2.1已核，按最外表面反射路径给出相位；Q097记录界面名与引用对应疑点。m′侧式2.2起仍待逐项核对。');nav.write_text(s,encoding='utf-8')
print(json.dumps(coverage,ensure_ascii=False))

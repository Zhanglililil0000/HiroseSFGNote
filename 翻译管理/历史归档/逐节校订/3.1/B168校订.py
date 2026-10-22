from pathlib import Path
import re,json,csv
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B168-修订前.md').exists();(o/'B168-修订前.md').write_text(old,encoding='utf-8')
a=old.index('**m/2 界面的 m 侧：**');b=old.index("**m'/m 界面的 m' 侧：**",a);prior=old[a:b]
base=(o/'B167-本批译文.md').read_text(encoding='utf-8');formula=re.findall(r'\$\$([\s\S]*?)\$\$',base)[1].replace('h_m^+','h_m^-').replace(r'\tag{2.4}',r'\tag{2.5}')
for f,axis in [('vis',r'\alpha'),('ir',r'\beta')]:
 t=f't_{{m2,{f},{axis}}}';assert formula.count(t)==1;formula=formula.replace(t,f'(1+r_{{m2,{f},{axis}}})')
def norm(s):
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s);s=re.sub(r'\\\\(?:\[[^\]]*\])?','',s);s=re.sub(r'\\hspace\{[^}]*\}','',s);s=re.sub(r'\\(?:quad|qquad|times|Bigl|Bigr)','',s);s=re.sub(r'\\[,!]','',s);return re.sub(r'[\s{}&]','',s)
assert norm(''.join(re.findall(r'\$\$([\s\S]*?)\$\$',prior)))==norm(formula)
text='**m/2界面的m侧：**\n\n（a）：$E^+$ 源（经反射）与 $E^-$ 源。\n\n$$\n'+formula.strip()+'\n$$\n\n'
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B168完成原目录、第1部分及2.1至m/2界面m侧的式(2.1)—(2.5)（PDF p1—5）；m′/m界面m′侧起仍为旧译待校订。Q096—Q097保留原文并就地说明。',new);p.write_text(new,encoding='utf-8');assert new[new.index("**m'/m 界面的 m' 侧：**"):]==old[b:]
(o/'B168-本批译文.md').write_text(text,encoding='utf-8');c={'batch':'B168','date':'2026-10-20','pages':[4,5],'units':'m/2界面m侧源分类(a)及跨页完整式2.5','tags':['2.5'],'source_images_visually_checked':True,'formula_factors_checked_after_layout_normalization':True,'source_corrections_adopted':False,'unchanged_tail':'m′/m界面m′侧及以后'};(o/'B168-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B168.md').write_text('# B168：m/2界面m侧\n\n2026-10-20，PDF p4—5，式2.5接全。核源分类E⁺（经反射）与E⁻；场位置h_m′+h_m⁻，两频率各保留两个透射因子、(1+rm2)与前向传播指数，共同分母和i(2n+1)路径相位均按原式。仅合并展示块及分行，无省略、无源式修正；全部因子格式归一化与旧转写一致，另对照原页确认。m′/m界面起未改。\n',encoding='utf-8')
def append(f,t):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
append(o/'局部约定卡.md','## B168补充\n\nm/2界面m侧场位置h_m′+h_m⁻；源分类为E⁺（经反射）与E⁻。式2.5的每频率分子为t1m′·tm′m·(1+rm2)及传播指数，与2侧的三个t区别；路径相位保留i(2n+1)，不补n范围。')
append(o/'结构与复用核验表.md','## B168执行更新\n\nm/2界面m侧式2.5跨p4—5已接全，至此该界面两侧完成。下一批p5的m′/m界面m′侧式2.6—2.7为完整组；核局部厚度hm′、两个路径相位及源分类，不将m侧2.8预先纳入已核范围。')
f=m/'当前进度与续接.md';s=f.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);f.write_text(h+'\n\n## 当前有效状态：B168完成3.1的式2.5（2026-10-20）\n\nm/2界面m侧跨p4—5式2.5及源分类已核，两个频率的(1+rm2)、传播指数和i(2n+1)相位保留。无新增原文疑点或修正。\n\n下一批B169：核p5的m′/m界面m′侧源分类(a)/(b)及式2.6—2.7；特别核场位置、局部相位及2n/2n+1差别；m侧2.8起后续仍待核。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B168已核第1部分及2.1式2.1—2.5；m′/m界面m′侧起待校订','映射核验':'p1—5已核至m/2界面m侧式2.5末；后续据原目录定位','公式图表范围':'25组无编号展示式及完整编号式2.1—2.5已核；后续待核','导读状态':'已更新B168范围；后续仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8-sig').replace('B163—B167已核第1部分及2.1引言、式2.1—2.4；后续待校订','B163—B168已核第1部分及2.1引言、式2.1—2.5；后续待校订');f.write_text(s,encoding='utf-8')
f=p.parent/'阅读导航.md';s=f.read_text(encoding='utf-8-sig').replace('当前3.1开篇、第1部分及2.1前四式B163—B167','当前3.1开篇、第1部分及2.1前五式B163—B168').replace('m/2界面m侧式2.5起仍待逐项核对。','m/2界面m侧跨页式2.5已接全；m′/m界面m′侧式2.6起仍待逐项核对。');f.write_text(s,encoding='utf-8');print('B168内容与管理范围已更新')

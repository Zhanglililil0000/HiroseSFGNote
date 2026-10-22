from pathlib import Path
import re,json,csv
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B169-修订前.md').exists();(o/'B169-修订前.md').write_text(old,encoding='utf-8')
a=old.index("**m'/m 界面的 m' 侧：**");b=old.index("**m'/m 界面的 m 侧：**",a);prior=old[a:b];eqs=re.findall(r'\$\$([\s\S]*?)\$\$',prior);assert len(eqs)==10
def norm(s):
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s);s=re.sub(r'\\\\(?:\[[^\]]*\])?','',s);s=re.sub(r'\\hspace\{[^}]*\}','',s);s=re.sub(r'\\(?:quad|qquad|times|Bigl|Bigr)','',s);s=re.sub(r'\\[,!]','',s);return re.sub(r'[\s{}&]','',s)
def make(group):
 first=group[0].strip().replace(' = ',' &=')
 rows=[first]
 for x in group[1:]:
  x=x.strip()
  if r'\exp[' in x:
   x=x.replace(r'\exp[',r'\exp\!\Bigl[').replace('] ',r'\Bigr] ')
   if x.endswith(']'):x=x[:-1]+r'\Bigr]'
   # Break before the common wave-vector sum; retain the original multiplication.
   x=x.replace('(-k_{m,ir}',r'\\ &\hspace{6em}\times(-k_{m,ir}',1)
  else:
   # Split denominator at its final summand, keeping numerator and denominator grouping.
   x=x.replace('}{1+ ',r'}{\begin{aligned}&1+ ',1)
   marker=' + (r_{m\'m,'
   assert marker in x
   x=x.replace(marker,r'\\&\quad'+marker.lstrip(),1)
   x=x[:-1]+r'\end{aligned}}'
  rows.append('&\quad '+x)
 tag=re.search(r'\\tag\{[^}]+\}',rows[-1])[0];rows[-1]=rows[-1].replace(tag,'')
 return r'\begin{aligned}'+'\n'+r'\\[6pt]'.join(rows)+'\n'+r'\end{aligned}'+'\n'+tag
formulas=[make(eqs[:5]),make(eqs[5:])]
assert norm(''.join(eqs))==norm(''.join(formulas))
text='**m′/m界面的m′侧：**\n\n（a）：$E^+$ 源与 $E^-$ 源（经反射）。\n\n$$\n'+formulas[0]+'\n$$\n\n（b）：$E^+$ 源（经反射）与 $E^-$ 源。\n\n$$\n'+formulas[1]+'\n$$\n\n'
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B169完成原目录、第1部分及2.1至m′/m界面m′侧的式(2.1)—(2.7)（PDF p1—5）；m′/m界面m侧起仍为旧译待校订。Q096—Q097保留原文并就地说明。',new);p.write_text(new,encoding='utf-8');assert new[new.index("**m'/m 界面的 m 侧：**"):]==old[b:]
(o/'B169-本批译文.md').write_text(text,encoding='utf-8');c={'batch':'B169','date':'2026-10-20','pages':[5],'units':'m′/m界面m′侧源分类(a)/(b)及完整式2.6—2.7','tags':['2.6','2.7'],'source_images_visually_checked':True,'formula_factors_checked_after_layout_normalization':True,'source_corrections_adopted':False,'unchanged_tail':'m′/m界面m侧及以后'};(o/'B169-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B169.md').write_text('# B169：m′/m界面m′侧\n\n2026-10-20，PDF p5。对照原页核两种源分类、hm′⁻位置、两频率分式与两个独立路径相位。保留t1m′、exp(iβm′hm′)、(1+rm′m)、(1+rm2 exp(2iβmhm))与共同分母；局部相位为ihm′tanθm′,SF乘原m层波矢和，两式往返相位分别i(2n+1)与2ni。源(a)反射修饰E⁻，源(b)修饰E⁺，未添加n条件。十个旧展示块合为两完整编号式，分母和指数分行，无省略或原式修正。格式归一化因子逐字比对通过，m侧及以后未改。\n',encoding='utf-8')
def append(f,t):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
append(o/'局部约定卡.md','## B169补充\n\nm′/m界面m′侧位置hm′⁻；式2.6中反射修饰E⁻源，式2.7中修饰E⁺源。两个独立相位因子完整保留：局部横向路径相位使用hm′tanθm′,SF，波矢项仍为原m层指标；往返相位分别i(2n+1)及2ni，不合并或换层标。')
append(o/'结构与复用核验表.md','## B169执行更新\n\np5的m′/m界面m′侧式2.6—2.7及源分类已完整核对。下一单元为该界面m侧2.8—2.9，2.9跨p5—6；不能按页末切断。')
f=m/'当前进度与续接.md';s=f.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);f.write_text(h+'\n\n## 当前有效状态：B169完成3.1的式2.6—2.7（2026-10-20）\n\n已核p5的m′/m界面m′侧两种源分类及完整两式；局部相位与往返相位分别保留，未补n条件或改m层波矢指标。无新增原文疑点或修正。\n\n下一批B170：核m′/m界面m侧的式2.8—2.9及源分类，跨p5—6接全；重点核两频率分子是否一致采用tm′m、原层标及路径相位，疑似不一致保留原式并注。m′体相深度z1段起继续待核。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B169已核第1部分及2.1式2.1—2.7；m′/m界面m侧起待校订','映射核验':'p1—5已核至m′/m界面m′侧式2.7末；后续据原目录定位','公式图表范围':'25组无编号展示式及完整编号式2.1—2.7已核；后续待核','导读状态':'已更新B169范围；后续仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8-sig').replace('B163—B168已核第1部分及2.1引言、式2.1—2.5；后续待校订','B163—B169已核第1部分及2.1引言、式2.1—2.7；后续待校订');f.write_text(s,encoding='utf-8')
f=p.parent/'阅读导航.md';s=f.read_text(encoding='utf-8-sig').replace('当前3.1开篇、第1部分及2.1前五式B163—B168','当前3.1开篇、第1部分及2.1前七式B163—B169').replace('m′/m界面m′侧式2.6起仍待逐项核对。','m′/m界面m′侧式2.6—2.7已核，保留各自源分类与两个独立相位因子；m侧式2.8起仍待逐项核对。');f.write_text(s,encoding='utf-8');print('B169内容与管理范围已更新')

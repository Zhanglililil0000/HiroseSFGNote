from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');backup=o/'B177-修订前.md'
if backup.exists():assert backup.read_text(encoding='utf-8')==old
else:backup.write_text(old,encoding='utf-8')
start=old.index('### 2.2 和频极化');a=old.index('**m/2 界面的 2 侧：**',start);b=old.index('**m/2 界面的 m 侧：**',a);prior=old[a:b];eqs=re.findall(r'\$\$([\s\S]*?)\$\$',prior);assert len(eqs)==6
def norm(s):
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s);s=re.sub(r'\\\\(?:\[[^\]]*\])?','',s);s=re.sub(r'\\(?:quad|qquad|times)','',s);s=re.sub(r'\\[,!]','',s);return re.sub(r'[\s{}&]','',s)
def layout(g):
 tag=re.search(r'\\tag\{[^}]+\}',g[-1])[0];rows=[]
 for i,x in enumerate(g):
  x=x.strip().replace(tag,'').rstrip();x=re.sub(r'\s+',' ',x)
  if i==0:x=x.replace(' = ',' &=',1)
  else:
   x='&'+x
   x=re.sub(r'}\{1\s*\+\s*',lambda z:r'}{\begin{aligned}&1+',x,count=1)
   assert " + (r_{m'm," in x;x=x.replace(" + (r_{m'm,",r"\\&\quad+(r_{m'm,",1)
   assert x.endswith('}');x=x[:-1]+r'\end{aligned}}'
  rows.append(x)
 result=r'\begin{aligned}'+'\n'+r'\\[6pt]'.join(rows)+'\n'+r'\end{aligned}'+'\n'+tag
 assert norm(''.join(g))==norm(result)
 return result
formulas=[layout(eqs[:3]),layout(eqs[3:])]
# Page 10 gives the same amplitude expression for both source classes; preserve both tags and classifications.
assert norm(formulas[0]).replace('2.20','2.21')==norm(formulas[1])
text='**m/2界面的2侧：**\n\n（a）：$E^+$ 源。\n\n$$\n'+formulas[0]+'\n$$\n\n（b）：$E^-$ 源（$n>0$ 时，经反射）。\n\n$$\n'+formulas[1]+'\n$$\n\n'
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B177完成原目录、第1部分、2.1全小节及2.2至m/2界面2侧的式(2.18)—(2.21)；m/2界面m侧式(2.22)起仍为旧译待校订。Q096—Q101保留原文并就地说明，未采用原文公式修正。',new);p.write_text(new,encoding='utf-8');assert new[new.index('**m/2 界面的 m 侧：**',new.index('### 2.2 和频极化')):]==old[b:]
(o/'B177-本批译文.md').write_text(text,encoding='utf-8');sha=hashlib.sha256((r/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
c={'batch':'B177','date':'2026-10-20','pages':[10],'units':'m/2界面2侧源分类(a)/(b)及完整式2.20—2.21','tags':['2.20','2.21'],'source_images_visually_checked':True,'formula_factors_checked_after_layout_normalization':True,'same_amplitude_different_source_classes_preserved':True,'source_sha256':sha,'source_formula_corrections_adopted':False,'unchanged_tail':'2.2的m/2界面m侧式2.22及以后'};(o/'B177-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B177.md').write_text('# B177：2.2的m/2界面2侧\n\n2026-10-20，PDF p10逐项核源分类(a)E⁺、(b)E⁻（n>0，经反射）。原页两条极化振幅式内容相同，分别保留原编号2.20和2.21，不合并删项；两频率各三个透射系数、前向传播指数与共同分母保留，求和包含全部α/β因子。仅合并原展示块与分行，不补原页未列的路径相位或反射因子，P星号保留。全部因子格式归一化比对一致，无新增原式疑点或修正；2.22起未改。\n',encoding='utf-8')
def append(f,t):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
append(o/'局部约定卡.md','## B177补充\n\n2.20/2.21原位置为hm′+hm⁺，两条极化振幅式相同，但分别对应E⁺源与反射产生的E⁻源（n>0）。按作者去相位限定保留分子内传播指数，未补显式路径相位；两原编号与分类均保留，不以式同而删除。')
append(o/'结构与复用核验表.md','## B177执行更新\n\np10的m/2界面2侧2.20—2.21及两类源已完成；尚不表示该界面m侧2.22完成。下一批B178处理同页m侧完整式2.22，止于m′/m界面m′侧。')
f=m/'当前进度与续接.md';s=f.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);f.write_text(h+'\n\n## 当前有效状态：B177完成3.1的式2.20—2.21（2026-10-20）\n\n已核p10的m/2界面2侧两类源及两式；两振幅式内容相同而源分类不同，保留两编号。两频率三个t与膜内传播指数、共同分母、完整求和均核对，无新增原式疑点或修正。\n\n下一批B178：核p10的m/2界面m侧源分类及式2.22，重点核0⁻侧位置的原层厚写法、两个t和(1+rm2)及分母，不补原文未列路径相位；止于m′/m界面m′侧之前。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B177完成第1部分、2.1及2.2至2.21；2.22起待校订','映射核验':'已核至p10的m/2界面2侧式2.21末；后续据原目录定位','公式图表范围':'25组无编号系数展示式及25个唯一编号式（2.1—2.21，含a/b）已核；后续待核','导读状态':'已更新B177范围；后续仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8-sig').replace('B163—B176完成第1部分、2.1及2.2引言/式2.18—2.19；2.20起待校订','B163—B177完成第1部分、2.1及2.2至式2.21；2.22起待校订');f.write_text(s,encoding='utf-8')
f=p.parent/'阅读导航.md';s=f.read_text(encoding='utf-8-sig').replace('### 2.2当前进度（B175—B176）','### 2.2当前进度（B175—B177）').replace('m/2界面2侧式2.20起尚未本轮校订。','m/2界面2侧式2.20—2.21已核：分别保留正反向源分类，振幅式相同；m侧式2.22起尚未本轮校订。');f.write_text(s,encoding='utf-8');print(json.dumps(c,ensure_ascii=False))

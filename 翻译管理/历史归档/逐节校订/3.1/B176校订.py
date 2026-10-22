from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B176-修订前.md').exists();(o/'B176-修订前.md').write_text(old,encoding='utf-8')
start=old.index('### 2.2 和频极化');a=old.index("**1/m' 界面的 m' 侧：**",start);b=old.index('**m/2 界面的 2 侧：**',a);prior=old[a:b]
base=(o/'B175-本批译文.md').read_text(encoding='utf-8');formula=re.findall(r'\$\$([\s\S]*?)\$\$',base)[0].replace('(0^-)','(0^+)').replace(r'\tag{2.18}',r'\tag{2.19}')
for f,axis in [('vis',r'\alpha'),('ir',r'\beta')]:
 z=f"(1+r_{{1m',{f},{axis}}})";assert formula.count(z)==1;formula=formula.replace(z,f"t_{{1m',{f},{axis}}}")
def norm(s):
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s);s=re.sub(r'\\\\(?:\[[^\]]*\])?','',s);s=re.sub(r'\\(?:quad|qquad|times)','',s);s=re.sub(r'\\[,!]','',s);return re.sub(r'[\s{}&]','',s)
assert norm(''.join(re.findall(r'\$\$([\s\S]*?)\$\$',prior)))==norm(formula)
text='**1/m′界面的m′侧：**\n\n（a）：$E^+$ 源与 $E^-$ 源（经反射）。\n\n$$\n'+formula.strip()+'\n$$\n\n'
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B176完成原目录、第1部分、2.1全小节及2.2引言与1/m′界面两侧式(2.18)—(2.19)；m/2界面2侧式(2.20)起仍为旧译待校订。Q096—Q101保留原文并就地说明，未采用原文公式修正。',new);p.write_text(new,encoding='utf-8');assert new[new.index('**m/2 界面的 2 侧：**',new.index('### 2.2 和频极化')):]==old[b:]
(o/'B176-本批译文.md').write_text(text,encoding='utf-8');sha=hashlib.sha256((r/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
c={'batch':'B176','date':'2026-10-20','pages':[9],'units':'1/m′界面m′侧源分类(a)及完整式2.19','tags':['2.19'],'source_images_visually_checked':True,'formula_factors_checked_after_layout_normalization':True,'source_sha256':sha,'source_formula_corrections_adopted':False,'unchanged_tail':'2.2的m/2界面2侧式2.20及以后'};(o/'B176-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B176.md').write_text('# B176：2.2的1/m′界面m′侧\n\n2026-10-20，PDF p9原页对照。完整核源分类(a)E⁺与反射产生的E⁻，式2.19场位置0⁺、χ与P星号、两频率各自t1m′前因子和共同分母。求和仍作用于含α、β的全部因子。按2.2引言仅列作者原振幅式，不补路径相位。三旧展示块合为一个可编辑编号式，全部因子格式归一化一致，无新原文疑点或修正。2.20起逐字不变。\n',encoding='utf-8')
def append(f,t):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
append(o/'局部约定卡.md','## B176补充\n\n2.19位于1/m′界面m′侧，原位置为0⁺；两频率分子前各用自身t1m′，不能与1侧的1+r互换。沿用2.2去相位振幅范围及P星号原记法，不补新的相位或共轭解释。')
append(o/'结构与复用核验表.md','## B176执行更新\n\np9的2.2中1/m′界面m′侧2.19及源分类已核，至此本界面两侧极化式均完成。下一批m/2界面2侧2.20—2.21需核p10原页，不能沿2.1光场式直接认定极化式完成。')
f=m/'当前进度与续接.md';s=f.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);f.write_text(h+'\n\n## 当前有效状态：B176完成3.1的式2.19（2026-10-20）\n\n已核p9的1/m′界面m′侧源分类及完整式2.19；两激发频率各自透射因子、共同分母与求和范围已核。P星号仍保留未定义状态，无新增原式疑点或修正。\n\n下一批B177：核p10的m/2界面2侧源分类(a)/(b)与式2.20—2.21，重点核三个t乘积、膜内传播指数及两极化式相同/不同项；止于m侧2.22之前。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B176完成第1部分、2.1及2.2引言/2.18—2.19；2.20起待校订','映射核验':'已核至p9的2.2式2.19末；后续据原目录定位','公式图表范围':'25组无编号系数展示式及23个唯一编号式（2.1—2.19，含a/b）已核；后续待核','导读状态':'已更新B176范围；后续仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8-sig').replace('B163—B175完成第1部分、2.1及2.2引言/式2.18；2.19起待校订','B163—B176完成第1部分、2.1及2.2引言/式2.18—2.19；2.20起待校订');f.write_text(s,encoding='utf-8')
f=p.parent/'阅读导航.md';s=f.read_text(encoding='utf-8-sig').replace('### 2.2首批进度（B175）','### 2.2当前进度（B175—B176）').replace('m′侧式2.19起尚未本轮校订。','m′侧式2.19也已核，保留对应两频率透射因子和完整求和范围；m/2界面2侧式2.20起尚未本轮校订。');f.write_text(s,encoding='utf-8');print(json.dumps(c,ensure_ascii=False))

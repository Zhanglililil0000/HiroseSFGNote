from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B166-修订前.md').exists();(o/'B166-修订前.md').write_text(old,encoding='utf-8')
a=old.index("**1/m' 界面的 m' 侧：**");b=old.index('**m/2 界面的 2 侧：**',a);before=old[a:b]
base=(o/'B165-本批译文.md').read_text(encoding='utf-8');formula=re.findall(r'\$\$([\s\S]*?)\$\$',base)[0]
formula=formula.replace('(0^-)','(0^+)').replace(r'\tag{2.1}',r'\tag{2.2}')
for f,axis in [('vis',r'\alpha'),('ir',r'\beta')]:
 x=f"(1+r_{{1m',{f},{axis}}})";assert formula.count(x)==1;formula=formula.replace(x,f"t_{{1m',{f},{axis}}}")
text='''**1/m′界面的m′侧：**

（a）：$E^+$ 源与 $E^-$ 源（经反射）。

$$
'''+formula.strip()+'''
$$

'''
# Confirm that the independently page-checked expression retains every old factor.
def norm(s):
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s);s=re.sub(r'\\\\(?:\[[^\]]*\])?','',s);s=re.sub(r'\\hspace\{[^}]*\}','',s);s=re.sub(r'\\(?:quad|qquad|times|Bigl|Bigr)','',s);s=re.sub(r'\\[,!]','',s);return re.sub(r'[\s{}&]','',s)
assert norm(''.join(re.findall(r'\$\$([\s\S]*?)\$\$',before)))==norm(formula)
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B166完成原目录、引言、第1部分系数及2.1中1/m′界面两侧的式(2.1)—(2.2)（PDF p1—4）；m/2界面2侧起仍为旧译待校订。Q096—Q097保留原文并就地说明。',new);p.write_text(new,encoding='utf-8');assert new[new.index('**m/2 界面的 2 侧：**'):]==old[b:]
(o/'B166-本批译文.md').write_text(text,encoding='utf-8')
sha=hashlib.sha256((r/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
coverage={'batch':'B166','date':'2026-10-20','pages':[4],'units':'1/m′界面m′侧源分类(a)与完整式2.2','tags':['2.2'],'source_images_visually_checked':True,'formula_factors_checked_after_layout_normalization':True,'source_sha256':sha,'new_source_issues':[],'source_corrections_adopted':False,'unchanged_tail':'m/2界面2侧及以后'}
(o/'B166-覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B166.md').write_text('# B166：3.1的1/m′界面m′侧\n\n2026-10-20，PDF p4。源分类(a)译出；式2.2两分式与相位均对照原页，四个旧展示块接为一个编号式。与2.1相比，两频率分子前因子为各自的t1m′，场位置为0⁺；分母及指数保持原式。长分式仅分行，全部因子通过格式归一化比对，无省略/新简写。无新增原文疑点，无原文修正。m/2界面2侧及后续逐字保持。\n',encoding='utf-8')
def append(f,t):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
append(o/'局部约定卡.md','## B166补充\n\n1/m′界面m′侧位置写0⁺，两激发频率分子前分别为t1m′,vis,α与t1m′,ir,β；与1侧的1+r前因子分别核对，不混用。源分类按原文列E⁺及反射产生的E⁻，式2.2未另列n条件，不补入。其余相位适用限定沿2.1引言保留。')
append(o/'结构与复用核验表.md','## B166执行更新\n\np4的1/m′界面m′侧源分类及式2.2已核，至此2.1中的第一个界面两侧均已处理。m/2界面2侧的式2.3—2.4尚待核；应把两种源分类及相位2n与2n+1分别核对。')
progress=m/'当前进度与续接.md';s=progress.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);progress.write_text(h+'\n\n## 当前有效状态：B166完成3.1的式2.2（2026-10-20）\n\n已核p4的1/m′界面m′侧源分类及完整式2.2；与式2.1的场位置和两频率分子前因子分别核对，分母及相位保留。无新增原文疑点或原文修正；m/2界面2侧起保持旧译。\n\n下一批B167：核p4的m/2界面2侧源分类(a)/(b)及式2.3—2.4，尤其传输乘积、前向传播指数以及路径相位2n和2n+1的差别；止于m/2界面m侧之前。n尚未获本节文字明确，维持待核。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B166已核第1部分及2.1式2.1—2.2；m/2界面2侧起待校订','映射核验':'p1—4已核至1/m′界面m′侧式2.2末；后续据原目录定位','公式图表范围':'25组无编号展示式及完整编号式2.1—2.2已核；后续待核','导读状态':'已更新B166范围；后续仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
pref=r/'Preface序言.md';s=pref.read_text(encoding='utf-8-sig').replace('B163—B165已核第1部分及2.1引言、式2.1；后续待校订','B163—B166已核第1部分及2.1引言、式2.1—2.2；后续待校订');pref.write_text(s,encoding='utf-8')
nav=p.parent/'阅读导航.md';s=nav.read_text(encoding='utf-8-sig').replace('当前3.1开篇、第1部分及2.1首式B163—B165','当前3.1开篇、第1部分及2.1前两式B163—B166').replace('m′侧式2.2起仍待逐项核对。','m′侧式2.2已完成核对，两激发频率保留各自透射因子及同一原路径相位。m/2界面2侧式2.3起仍待逐项核对。');nav.write_text(s,encoding='utf-8')
print(json.dumps(coverage,ensure_ascii=False))

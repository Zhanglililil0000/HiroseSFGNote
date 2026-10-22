from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B175-修订前.md').exists();(o/'B175-修订前.md').write_text(old,encoding='utf-8')
a=old.index('### 2.2 SFG极化');b=old.index("**1/m' 界面的 m' 侧：**",a);prior=old[a:b]
base=(o/'B165-本批译文.md').read_text(encoding='utf-8');formula=re.findall(r'\$\$([\s\S]*?)\$\$',base)[0]
formula=formula[:formula.index(r' &\quad\times\exp')].rstrip();assert formula.endswith(r'\\[6pt]');formula=formula[:-8]+ '\n'+r'\end{aligned}'+'\n'+r'\tag{2.18}'
formula=formula.replace(r'E_{vis,\alpha}(0^-)E_{ir,\beta}(0^-)',r'P_a^*(0^-)').replace(r'&=E^0_{vis,\alpha}E^0_{ir,\beta}',r'&=\sum_{\alpha,\beta}\chi_{a\alpha\beta}E^0_{vis,\alpha}E^0_{ir,\beta}')
def norm(s):
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s);s=re.sub(r'\\\\(?:\[[^\]]*\])?','',s);s=re.sub(r'\\hspace\{[^}]*\}','',s);s=re.sub(r'\\(?:quad|qquad|times|Bigl|Bigr)','',s);s=re.sub(r'\\[,!]','',s);return re.sub(r'[\s{}&]','',s)
assert norm(''.join(re.findall(r'\$\$([\s\S]*?)\$\$',prior)))==norm(formula)
text=r'''### 2.2 和频极化

各位置的和频极化，是该处可见光与红外光的电场乘积乘以极化率得到的。下面列出去除相位部分后的极化振幅。

> **译者注（记号与范围）：** 此处χ表示二阶非线性极化率，正文在阶数明确的上下文中简称“极化率”；原式未显式写出的阶数上标不另行补入。保留原文的 $P_a^*$ 记号；本段未单独解释星号，不据一般习惯将其改写成复共轭或赋予新的定义。“去除相位部分”沿用作者的限定；以下仍保留分式内的膜内传播指数，不据此把全部指数项删去。式(2.18)的求和作用于含α、β的完整场乘积，两条频率分式随同前因子在求和内读取。

**1/m′界面的1侧：**

（a）：$E^+$ 源（经反射和透射）以及 $E^-$ 源（$n=0$ 时）。

$$
'''+formula.strip()+'\n$$\n\n'
new=old[:a]+text+old[b:];new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B175完成原目录、第1部分、2.1全小节及2.2引言与式(2.18)；1/m′界面m′侧式(2.19)起仍为旧译待校订。Q096—Q101保留原文并就地说明，未采用原文公式修正。',new);p.write_text(new,encoding='utf-8');assert new[new.index("**1/m' 界面的 m' 侧：**",new.index('### 2.2 和频极化')):]==old[b:]
(o/'B175-本批译文.md').write_text(text,encoding='utf-8');sha=hashlib.sha256((r/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
c={'batch':'B175','date':'2026-10-20','pages':[9],'units':'2.2和频极化引言、1/m′界面1侧源分类及完整式2.18','tags':['2.18'],'source_images_visually_checked':True,'formula_factors_checked_after_layout_normalization':True,'source_sha256':sha,'source_formula_corrections_adopted':False,'unchanged_tail':'1/m′界面m′侧式2.19及以后'};(o/'B175-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B175.md').write_text('# B175：2.2和频极化开篇\n\n2026-10-20；PDF p9原页核对。将旧译感受率按已确认规则改为极化率，并首次在译者注说明二阶非线性极化率，不擅自给原χ添加阶数上标。保留作者去相位振幅限定及分式内传播指数；P星号定义未明确，保留而不推断共轭。求和覆盖两频率完整乘积。三旧展示块合为一个可编辑式2.18，因子格式归一化逐字一致，无原文修正或新增疑难。2.19起不变。\n',encoding='utf-8')
def append(f,t):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+t+'\n',encoding='utf-8')
append(o/'局部约定卡.md','## B175：2.2开篇约定\n\nχ为本节和频过程的二阶非线性极化率，原符号无阶数上标时不补改。a为输出极化坐标分量，α/β为可见/红外输入分量，求和覆盖两频率分式。P*原样保留，本段未解释星号，不标为已确认共轭记号。“去除相位”按作者原限定，未删除分母及分子中膜内传播指数。2.18仅未列2.1对应式末端显式路径相位，原页逐项核对，不将2.1状态自动复制到后续。')
append(o/'结构与复用核验表.md','## B175执行更新\n\np9的2.2引言、1/m′界面1侧源分类及式2.18已核。下一批B176为同页m′侧2.19，止于m/2界面2侧之前。2.2尚未全节完成。')
f=m/'当前进度与续接.md';s=f.read_text(encoding='utf-8-sig');h,t=s.split('\n',1);f.write_text(h+'\n\n## 当前有效状态：B175完成3.1的2.2引言与式2.18（2026-10-20）\n\n已核p9的引言及1/m′界面1侧源分类和完整式2.18。χ按二阶非线性极化率命名，保留原无阶数上标及P星号；去相位振幅限定与膜内指数共存，不擅自删改。无新增原文疑难或修正。\n\n下一批B176：核p9的1/m′界面m′侧源分类及式2.19，逐项核两频率t1m′、共同分母和求和范围，止于m/2界面2侧之前。P星号含义仍未明，不自动判为共轭。以下为历史记录。\n'+t,encoding='utf-8')
f=m/'章节清单.tsv'
with f.open(encoding='utf-8-sig',newline='') as h:rd=csv.DictReader(h,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for row in rows:
 if row['编号']=='3.1':row.update({'状态':'B163—B175完成第1部分、2.1及2.2引言/2.18；2.19起待校订','映射核验':'已核至p9的2.2式2.18末；后续据原目录定位','公式图表范围':'25组无编号系数展示式及22个唯一编号式（2.1—2.18，含a/b）已核；后续待核','导读状态':'已更新B175范围；后续仅目录定位'})
with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
f=r/'Preface序言.md';s=f.read_text(encoding='utf-8-sig').replace('B163—B174完成第1部分及2.1全小节；2.2起待校订','B163—B175完成第1部分、2.1及2.2引言/式2.18；2.19起待校订');f.write_text(s,encoding='utf-8')
f=p.parent/'阅读导航.md';s=f.read_text(encoding='utf-8-sig');s+='\n\n### 2.2首批进度（B175）\n\np9引言与1/m′界面1侧式2.18已核：由二阶非线性极化率连接两激发场，按作者说明列去相位的极化振幅，仍保留分式中的膜内指数。P星号按原文保留，含义待后文确认。m′侧式2.19起尚未本轮校订。\n';s=s.replace('下一步为2.2和频极化，正文该段仍是待校订旧译。','2.2首批范围见下方，其余仍为待校订旧译。');f.write_text(s,encoding='utf-8')
f=o/'检查2.1完整排版.cjs';s=f.read_text(encoding='utf-8').replace("split('### 2.2 SFG极化')","split('### 2.2 和频极化')");f.write_text(s,encoding='utf-8');print(json.dumps(c,ensure_ascii=False))

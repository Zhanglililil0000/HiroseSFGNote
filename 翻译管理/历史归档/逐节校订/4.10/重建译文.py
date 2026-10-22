from pathlib import Path
import json,re,hashlib
from PIL import Image
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.10 CH₂基团及HCCH基团的欧拉角.md'
if not (out/'重建前旧译.md').exists():(out/'重建前旧译.md').write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
events=[]
def event(p,y,s):events.append({'page':p,'y':y,'kind':'prose','text':s})
def display(s):return '\n\n$$\n'+s+'\n$$\n\n'
def vector(name,rows):return 'e_{'+name+r'}=\begin{pmatrix}'+'\\\\'.join(rows)+r'\end{pmatrix}'
def vectors(a,b,c,dot):return display(r'\begin{gathered}'+vector('a',a)+r',\quad '+vector('b',b)+r',\\'+vector('c',c)+r',\quad e_z\cdot e_b='+dot+r'.\end{gathered}')
assets=root/'中文版本/assets';images=[]
for name,p,box in [('CH2',1,(180,350,425,510)),('HCCH-C2',1,(170,580,425,750)),('HCCH-C2v',2,(170,105,425,285))]:
 im=Image.open(out/f'原文p{p}.png');im.crop(tuple(int(x*2) for x in box)).save(assets/f'4.10-{name}.png');images.append({'asset':f'4.10-{name}.png','pdf_page':p,'crop_pdf_points':box,'method':'原PDF渲染裁取，未重绘'})
(out/'图像来源.json').write_text(json.dumps(images,ensure_ascii=False,indent=2),encoding='utf-8')
event(1,0,r'''# 4.10 CH₂基团及HCCH基团的欧拉角

> 原作：广瀬千秋；中文翻译：章力。按8页原稿译校。原文件名保留以兼容链接。

## 阅读引导与目录

| 部分 | PDF页 | 内容概括 |
|---|---|---|
| 1 坐标轴 | 1—2 | 用三幅原图区分分子系、CH键系与表面系 |
| 2、2a | 2—6 | 用单位向量和二面角处理CH₂的纯扭转、纯倾斜及三类组合取向 |
| 2b | 6 | 平面HCCH交替倾斜、扭转HCCH坐标重合 |
| CH键系到分子系 | 6—8 | CH₂、平面及扭转HCCH的两键欧拉角关系 |

## 1. 坐标轴

**分子固定$(abc)$系。** CH₂的$c$轴沿HCH角外向角平分线，$a$轴在分子面内并平行于H—H连线。HCCH的$a$轴取向被氢化的碳原子方向，$c$轴沿二重轴。两个HCC面共面时有C₂ᵥ对称，$ac$面即该平面；若位阻使两个CH键相对原HCCH面同向偏移，$a,c$轴也随之偏移。两HCC面成角度时有C₂对称，$ac$面位于两平面锐角一侧的角平分面上，即假设无位阻时的HCCH面。

**CH键固定$(\xi\eta\zeta)$系。** $\zeta$轴沿CH键；CH₂的$\xi$轴在HCH面内指向C₂轴，HCCH的$\xi$轴在HCC面内指向C₂轴。

![CH₂的分子与键坐标，原PDF p1](../assets/4.10-CH2.png)

![扭转HCCH的坐标，原PDF p1](../assets/4.10-HCCH-C2.png)

![平面HCCH的坐标，原PDF p2](../assets/4.10-HCCH-C2v.png)

图中字母与箭头保留。HCCCH型单元也可采用与HCCH相同的形式。

**表面固定$(xyz)$系。** $z$轴取表面外向法线；$x$轴取无位阻时CH₂或HCCH分子面相互对齐并排列的方向。

> **局部约定：** 此稿法线向外，与4.8、4.9第2部分的向内约定不同，跨稿引用须明确转换。
''')
event(2,449,r'''## 2. 取向CH₂、HCCH相对表面系的欧拉角

经三个旋转$R_z(\chi)R_{b\prime}(\theta)R_c(\phi)$使$(abc)$与$(xyz)$重合时，旋转角$(\chi,\theta,\phi)$称为欧拉角。$\theta$为$z,c$两轴夹角，也是$xy,ab$两面二面角；$\phi$为两面交线与$b$轴夹角，也是$zc$平面与分子面夹角；$\chi$为交线与$y$轴夹角，也是$zc$平面与$xz$面夹角。

同一官能团覆盖表面时，将相邻、彼此对顶的两个CH键作为一对单元，则无论来自CH₂或HCCH，两键均相互扭转；可使固定在键对上的坐标系与表面系重合，但两类键对所需角度不同，求解较为费力。氢化部分若改变排列方向90°，需出现台阶，台阶中段存在CH基团。

### 2a. 取向CH₂基团

无位阻时，表面CH₂垂直于表面、分子面彼此平行。若位阻引起绕竖直$c$轴的扭转$\gamma$及倾斜$\theta$，可有下列旋转方式。描述平面分子时，用主轴偏离$z$轴的倾角，以及分子面或交线方向与表面的二面角更直观。以下必要时同时列出分子面$ac$与表面$xy$间二面角$\tau$与欧拉角的关系。

求解时，先分别以二面角、欧拉角表示$a,b,c$轴单位向量在表面系中的分量；再利用$b,z$轴夹角对应二面角，故内积绝对值为$\cos\tau$。二面角取锐角，$\cos\tau>0$。使两种表达式一致即可确定欧拉角。
''')
event(3,268,vectors([r'\cos\chi\cos\phi\cos\theta-\sin\chi\sin\phi',r'-\sin\chi\cos\phi\cos\theta-\cos\chi\sin\phi',r'\cos\phi\sin\theta'],[r'\cos\chi\sin\phi\cos\theta+\sin\chi\cos\phi',r'-\sin\chi\sin\phi\cos\theta+\cos\chi\cos\phi',r'\sin\phi\sin\theta'],[r'-\cos\chi\sin\theta',r'+\sin\chi\sin\theta',r'+\cos\theta'],r'\sin\phi\sin\theta'))
event(3,449,r'$R_c(\phi)$使$b$轴垂直于$z$轴，即垂直于$zc$面；$R_{b\prime}(\pm\theta)$使$c,z$轴及$xy,ab$面重合；$R_z(\chi)$使$b,y$轴及$xz$面与分子面重合。')
event(3,514,'#### 只有绕z轴的扭转\n\n相邻CH₂同向扭转以增大H—H间距。')
event(3,564,display(r'\begin{gathered}R_z(\chi=\gamma)R_{b\prime}(\theta=0)R_c(\phi=0)\quad\text{或}\\R_z(\chi=-\gamma)R_{b\prime}(\theta=0)R_c(\phi=0),\quad\tau=\pi/2.\tag{Eu-1}\end{gathered}'))
event(3,646,r'相邻CH₂同取$+\gamma$或同取$-\gamma$，不交替。'+'\n\n'+r'> **原文疑点Q195（p3）：** $\phi=0$后原列$\cos2\phi=-1$，候选$+1$未采用。')
event(3,678,'#### 只有倾斜，情形1\n\n相邻CH₂绕x轴旋转，向表面沿±y方向倒伏，以增大H—H间距。')
event(4,88,vectors(['1','0','0'],['0',r'\cos\theta',r'\sin\theta'],['0',r'-\sin\theta',r'+\cos\theta'],r'\sin\theta'))
event(4,154,display(r'\begin{gathered}R_z(\chi=-\pi/2)R_{b\prime}(-\theta)R_c(\phi=\pi/2)\quad\text{或}\\R_z(\chi=-\pi/2)R_{b\prime}(\theta)R_c(\phi=\pi/2).\tag{Eu-2a}\end{gathered}')+r'$\tau=\pi/2-\theta$，严格地说$\cos\tau=\sin\theta$。')
event(4,252,r'相邻CH₂交替取$+\theta$与$-\theta$。')
event(4,285,'#### 只有倾斜，情形2\n\n相邻CH₂绕y轴旋转，向表面沿±x方向倒伏，以增大H—H间距。')
event(4,335,vectors([r'\cos\theta','0',r'-\sin\theta'],['0','1','0'],[r'+\sin\theta','0',r'+\cos\theta'],'0'))
event(4,400,display(r'\begin{gathered}R_z(\chi=\pi)R_{b\prime}(\theta)R_c(\phi=\pi)\quad\text{或}\\R_z(\chi=-\pi)R_{b\prime}(-\theta)R_c(\phi=\pi),\quad\tau=\pi/2.\tag{Eu-2b}\end{gathered}'))
event(4,482,r'相邻CH₂“交替取$+\theta$或$-\theta$之一”，同时“异号者不相邻”。'+'\n\n'+r'> **原文疑点Q196（p4）：** 两项排列说法有歧义，保留原文，未据旧译选定取向分布。')
event(4,514,'#### 同时有扭转和倾斜\n\n实际可分为(a)—(c)三种，欧拉角各不相同。')
event(4,564,'**(a) 沿y方向倾斜。** 分子轴在yz面上，xy面投影与y轴重合，扭转与y方向倾斜同时发生。')
event(4,613,vectors([r'\cos\gamma',r'\sin\gamma\cos\theta',r'\sin\gamma\sin\theta'],[r'-\sin\gamma',r'\cos\gamma\cos\theta',r'\cos\gamma\sin\theta'],['0',r'-\sin\theta',r'+\cos\theta'],r'\cos\gamma\sin\theta'))
event(4,678,r'$\sin\chi=-1,\cos\chi=0$，即$\chi=3\pi/2,-\pi/2$。$\sin\phi=\cos\gamma,\cos\phi=\sin\gamma$，即$\phi=\pi/2-\gamma$；$\cos\gamma=\cos\tau/\sin\theta$。')
event(5,219,r'相邻CH₂同取$+\gamma$或同取$-\gamma$，$\theta$符号交替。'+'\n\n'+r'> **Q195续（p4—5）：** 原列$\sin\chi=-1$却写$\sin3\chi=-1$，负号组首项原为$-\sin2\gamma$；候选分别为$+1$、$-\sin\gamma$，未采用。')
event(5,252,'**(b) 沿x方向倾斜。** 分子轴在xz面上，xy面投影与x轴重合，扭转与x方向倾斜同时发生。')
event(5,301,vectors([r'\cos\gamma\cos\theta',r'\sin\gamma',r'-\cos\gamma\sin\theta'],[r'-\sin\gamma\cos\theta',r'\cos\gamma',r'\sin\gamma\sin\theta'],[r'\sin\theta','0',r'\cos\theta'],r'\sin\gamma\sin\theta'))
event(5,367,r'$\sin\chi=0,\cos\chi=-1$，即$\chi=\pi$；$\sin\phi=\sin\gamma,\cos\phi=-\cos\gamma$，即$\phi=\pi-\gamma$；$\sin\gamma=\cos\tau/\sin\theta$。')
event(5,580,r'相邻CH₂同取$+\gamma$或同取$-\gamma$，$\theta$也同号。')
event(5,613,r'**(c) 同时有扭转和倾斜，分子轴在xy面投影与x轴成角γ。** 可视为在(b)基础上再旋转$\chi^*$。原文先称γ、随后以χ*表示附加转角，均保留。')
event(5,678,vectors([r'\cos\chi^*\cos\gamma\cos\theta-\sin\chi^*\sin\gamma',r'+\sin\chi^*\cos\gamma\cos\theta-\cos\chi^*\sin\gamma',r'-\cos\gamma\sin\theta'],[r'-\cos\chi^*\sin\gamma\cos\theta-\sin\chi^*\cos\gamma',r'-\sin\chi^*\sin\gamma\cos\theta+\cos\chi^*\cos\gamma',r'\sin\gamma\sin\theta'],[r'\cos\chi^*\sin\theta',r'\sin\chi^*\sin\theta',r'\cos\theta'],r'\sin\gamma\sin\theta'))
event(6,104,r'$\sin\chi=\sin\chi^*,\cos\chi=-\cos\chi^*$，即$\chi=\pi-\chi^*$；$\sin\phi=\sin\gamma,\cos\phi=-\cos\gamma$，即$\phi=\pi-\gamma$；$\sin\gamma=\cos\tau/\sin\theta$。')
event(6,350,r'相邻CH₂的γ与θ分别同号，χ*符号交替。'+'\n\n'+r'> **Q195续（p6）：** 原取向组中的“in3γ”和负号组首项“−sin2γ”照录，未补字或改倍角。')
event(6,400,r'''### 2b. 取向HCCH基团

平面HCCH（C₂ᵥ）无需考虑扭转，只需给出$ac$面相对$xz$面绕$a$轴的旋转$\tau$。相邻基团如下。''')
event(6,580,r'相邻HCCH交替取$-\tau$与$+\tau$。扭转HCCH（C₂）可认为$xz$与$ac$面，进而两套坐标系本身重合。'+'\n\n'+r'> **Q196续（p6）：** 原稿并列θ=±τ与τ=π/2−θ，角度含义不直接统一；原式保留。')
event(6,646,r'''## CH键固定$(\xi\eta\zeta)$系到分子固定$(abc)$系的欧拉角

### CH₂基团

设HCH角为α，两个CH键的坐标系分别作下列旋转。''')
event(7,137,r'### 平面HCCH基团（C₂ᵥ）'+'\n\n'+r'原文称“HCH角”为α，两个CH键的坐标系分别作下列旋转。')
event(7,154,r'> **原文疑点Q197（p7）：** HCCH小节称α为“HCH角”，候选为“HCC/CCH角”；原称保留，未采用候选。')
event(7,268,r'''### 扭转HCCH基团（C₂）

采用结构化学常用的CCH角α与两个CCH面间二面角τ；后二面角由从面交线上一点向两面所作垂线的夹角定义。ξ、ζ轴均在CCH面上，该面与ac面间二面角为τ/2。将两条CH键的单位向量在abc系中并列如下：左列对应朝a轴正向、偏向b轴的键，右列对应相反方向的键。''')
v=''
for name,left,right,tag in [('xi',[r'-\sin\alpha',r'-\cos\alpha\sin(\tau/2)',r'-\cos\alpha\cos(\tau/2)'],[r'+\sin\alpha',r'+\cos\alpha\sin(\tau/2)',r'-\cos\alpha\cos(\tau/2)'],'Eu-7a'),('eta',['0',r'-\cos(\tau/2)',r'+\sin(\tau/2)'],['0',r'+\cos(\tau/2)',r'+\sin(\tau/2)'],'Eu-7b'),('zeta',[r'-\cos\alpha',r'+\sin\alpha\sin(\tau/2)',r'+\sin\alpha\cos(\tau/2)'],[r'+\cos\alpha',r'-\sin\alpha\sin(\tau/2)',r'+\sin\alpha\cos(\tau/2)'],'Eu-7c')]:
 v+=display(vector('\\'+name,left)+r',\qquad '+vector('\\'+name,right)+r'\tag{'+tag+'}')
event(7,433,v)
event(7,596,r'$e_\zeta$与$e_c$的夹角θ由原写内积$e_z\cdot e_c=\cos\theta$求出。')
event(7,678,r'垂直于$e_\zeta$与$e_c$的单位向量$e_{\eta\prime}$，原文将“向量积$e_\zeta\cdot e_c$”的方向定义为正向，得到：')
event(7,711,display(vector(r'\eta\prime',[r'+\sin\alpha\sin(\tau/2)/\sin\theta',r'+\cos\alpha/\sin\theta','+0'])+r',\qquad '+vector(r'\eta\prime',[r'-\sin\alpha\sin(\tau/2)/\sin\theta',r'-\cos\alpha/\sin\theta','+0'])+r'\tag{Eu-9}'))
event(8,104,r'''由此，$e_{\eta\prime}$与$e_\eta$间的角φ，以及$e_{\eta\prime}$与$e_b$间的角χ分别为下式。两列对应前述两条CH键。

> **Q197续（p7）：** 求θ时原下标为拉丁z而前文为ζ；“向量积”却使用点号。候选分别为ζ及叉乘号×，原写保留，未采用候选。
'''+display(r'\begin{aligned}\sin\phi&=\frac{\sin(\tau/2)}{\sin\theta},&\sin\phi&=\frac{\sin(\tau/2)}{\sin\theta},\\\cos\phi&=-\frac{\cos\alpha\cos(\tau/2)}{\sin\theta},&\cos\phi&=-\frac{\cos\alpha\cos(\tau/2)}{\sin\theta}.\end{aligned}\tag{Eu-10}')+display(r'\begin{aligned}\sin\chi&=\frac{\sin\alpha\sin(\tau/2)}{\sin\theta},&\sin\chi&=-\frac{\sin\alpha\sin(\tau/2)}{\sin\theta},\\\cos\chi&=\frac{\cos\alpha}{\sin\theta},&\cos\chi&=-\frac{\cos\alpha}{\sin\theta}.\end{aligned}\tag{Eu-11}'))
event(8,285,r'''两个CH键之间有$\phi\leftrightarrow\phi$、$\chi\leftrightarrow\chi+\pi$的关系。坐标变换时，含χ与3χ的三角函数在两键间反号。若平面HCCH也采用与此相同的abc系，则χ部分变为$\chi\leftrightarrow\pi-\chi$。

利用上述欧拉角，结合《从分子固定系到空间固定系.doc》，可用CH键和频张量表示CH₂、HCCH的分子固定系和频张量；《CH₂的取向与张量分量.doc》亦可参考。''')
data=json.loads((out/'字形行.json').read_text(encoding='utf-8'))
excluded=[(3,260,449),(4,70,154),(4,330,400),(4,610,678),(5,300,367),(5,670,765),(6,575,646),(7,430,596),(7,710,765),(8,0,765)]
for p,ls in data.items():
 p=int(p)
 if p<3:continue
 for l in ls:
  y=l['y'];s=l['tex'].replace('(cid:160)','').strip()
  if any(p==a and b<=y<c for a,b,c in excluded):continue
  if not s or re.search('[ぁ-んァ-ン一-龯ØŒºßøœ]',s):continue
  if any(e['page']==p and abs(e['y']-y)<1 for e in events):continue
  if chr(92) in s or '=' in s or re.fullmatch(r'\(Eu-[0-9a-z]+\)',s):events.append({'page':p,'y':y,'kind':'math','text':s})
# Eu-4、Eu-5、Eu-6旋转条件不含日语，自动转录；Eu-2等含“または”已手工排入。
events.sort(key=lambda e:(e['page'],e['y']))
bounds=[(416,1,0),(417,2,449),(418,3,678),(419,6,400),(420,6,646)]
src8=(out.parent/'4.8/重建译文.py').read_text(encoding='utf-8')
exec(src8[src8.index('texts={n:'):src8.index('intro=')].replace('batch=386','batch=416'))
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-10.pdf').read_bytes()).hexdigest()
for n,_,_ in bounds:
 (out/f'B{n}-本批译文.md').write_text(texts[n],encoding='utf-8')
 (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','source_sha256':sha,'source_lines_and_locations':records[n],'source_corrections_adopted':False,'manual_vector_and_prose_pages':list(range(1,9))},ensure_ascii=False,indent=2),encoding='utf-8')
target.write_text('\n\n'.join(texts.values()),encoding='utf-8')
(out/'检查排版.cjs').write_text((out.parent/'4.7/检查排版.cjs').read_text(encoding='utf-8').replace('4.7','4.10'),encoding='utf-8')
print('4.10原图、向量、欧拉角条件和原稿说明已重建。')

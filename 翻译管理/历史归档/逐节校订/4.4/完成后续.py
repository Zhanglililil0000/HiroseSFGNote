from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.4 CH基团的取向与和频张量.md'
snap=out/'B316前整节快照.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snap.read_text(encoding='utf-8')
p42=out.parent/'4.2'
def add(n,pages,s,scope):
    (out/f'B{n}-本批译文.md').write_text(s.strip()+'\n',encoding='utf-8')
    sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-4.pdf').read_bytes()).hexdigest()
    (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','date':'2026-10-21','pages':pages,'scope':scope,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
    (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n{scope}。逐项对照本节原页，恢复原θ/χ与β符号、函数幂及全部偏振分量，删除旧译自行添加的弯曲振动与错误选择规则。原文疑点保留并就地说明，无原文修正采用。复用前节排版仅在独立核对本节原式后进行。\n',encoding='utf-8')
def table(s):
    result=[]
    for m in re.finditer(r'\$\$([\s\S]*?)\$\$|\*\*\((ppp|spp|ssp|psp|sps|pps|pss|sss)\)\*\*',s):
        if m[1] is not None:result.append('\n\n$$\n'+m[1].strip()+'\n$$\n\n')
        else:
            result.append('\n**('+m[2]+')**\n')
            if '无。' in s[m.end():m.end()+20]:result.append('\n无。\n')
    return ''.join(result)
def prior(n):return (p42/f'B{n}-本批译文.md').read_text(encoding='utf-8')
angle=r'''以$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角，以$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴之间的面内取向角，则公式中的欧拉角为$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi+\chi_{\mathrm{ip}}$。
'''
s=prior(281);general=table(s[s.index('**(ppp)**'):])
add(316,[3,4],r'''## 4. 取向CH基团的$\beta_{xyz}$（表面固定系）

用欧拉角$(\chi,\theta)$表示CH基团相对于表面固定$(xyz)$系的取向时，利用《变换矩阵(xyz)》或 *Appl. Spectrosc.* 中的表，将涉及$\phi$的项置零，可求得以下表面系张量分量。关于倾斜角$\theta$，这里不用表中$\sin\theta$、$\sin2\theta$、$\sin3\theta$形式的三角函数，而采用下列关系改写成$\sin\theta$、$\cos\theta$的幂：

$$
\begin{aligned}
\sin2\theta&=2\sin\theta\cos\theta,\\
\cos2\theta&=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta,\\
\sin3\theta&=3\sin\theta-4\sin^3\theta,\\
\sin\theta+\sin3\theta&=4(\sin\theta-\sin^3\theta),\\
\cos3\theta&=4\cos^3\theta-3\cos\theta,\\
\cos\theta-\cos3\theta&=4(\cos\theta-\cos^3\theta).
\end{aligned}
$$

'''+angle+r'''
以下给出代表性取向的张量分量。

**一般式。** 先列出一般表达式，它们是按取向条件简化时的出发点，也应能适用于各种条件。

> **译者注（处理与符号）：** “将涉及$\phi$的项置零”为原文处理说明，不能改写成“令$\phi=0$”。本节假定轴对称，只需两个取向角。表面响应$\chi$处于二阶非线性极化率的语境；分子$\beta$仍称一阶超极化率（二阶场响应）。$\sin^3\theta$与$\sin3\theta$、$\cos^3\theta$与$\cos3\theta$须区分。
'''+general,'第4部分三角恒等式、一般取向全部27个张量分量，补回旧译(spp)缺项')

s=prior(289);sym=s[s.index('#### 全对称振动'):s.index('#### 简并振动')];random=table(sym)
random=random.replace(r'\chi_{zzz} = -(\beta_{aac} - \beta_{ccc})\cos^3\theta',r'\chi_{zzz} = -(\beta_{aac} - \beta_{ccc})(\cos \theta - \cos^3\theta)')
add(317,[4,5],r'''## 5. 表面取向造成的和频张量差异

（以下叙述中使用的角$\chi$，是指以$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线计量的倾斜角、以$\chi_{\mathrm{ip}}$表示$c$轴投影与$x$轴间面内取向角时的$\chi_{\mathrm{ip}}$。它与张量分量表达式所用欧拉角之间有$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi+\chi_{\mathrm{ip}}$的关系。）

CH基团的面内取向用角$\chi$定义。将入射面与表面的交线沿光传播方向取为正方向，以该交线与CH分子轴在表面上投影之间的角作为取向角，便能导出解析测量数据所需的张量，并研究信号随样品旋转的变化。若将$\chi$定义为表面固定轴——例如晶轴——与CH轴投影之间的角，则求得的是表面固有的张量分量。

不过，对于第5d部分的$C_s$对称情形，分别定义两个角更便于解释数据：一是入射面与表面的交线相对于镜面对称面与表面交线（director）的角；二是CH轴投影相对于该镜面与表面交线的角。$C_s$对称表面的和频实验中，入射面与对称面重合时，不产生(spp)、(psp)、(pps)、(sss)光。

以下考察代表性取向形式下的张量分量。

### 5a. 随机（二维）取向表面的和频张量

CH基团面内取向随机时，面内取向角$\chi$在$0$至$2\pi$之间以相同概率取任意值。由于：

$$
\int_0^{2\pi}\cos(n\chi)\,d\chi=\int_0^{2\pi}\sin(n\chi)\,d\chi=0\qquad(n=1,2,3),
$$

张量分量大幅简化如下。以$\theta_{\mathrm{tilt}}$表示$c$轴从外向法线量起的倾斜角，则下式使用的欧拉角$\theta=\pi-\theta_{\mathrm{tilt}}$。
'''+random+r'''
> **译者注（原文疑点Q163，PDF p5）：** 本表$\chi_{zzz}$原写$-(\beta_{aac}-\beta_{ccc})(\cos\theta-\cos^3\theta)+\beta_{aac}\cos\theta$，与第4部分一般式中的$-(\beta_{aac}-\beta_{ccc})\cos^3\theta+\beta_{aac}\cos\theta$不同。正文按本表保留；候选可由一般式直接作面内平均核验，尚未采用。
''','第5部分完整引入及5a随机面内平均，全部7个分量及无信号项')

s=prior(290);sym=s[s.index('#### 全对称振动'):s.index('#### 简并振动')]
add(318,[5,6],r'''### 5b. C₃ᵥ取向表面的和频张量

此时，面内角取$\chi$、$\chi+2\pi/3$、$\chi+4\pi/3\;(=\chi-2\pi/3)$三个值的CH基团以相同概率存在。利用三角函数求和关系，将三种取向的正弦、余弦用$\chi$表示后相加，得：

$$
\begin{aligned}
\sum1&=3,\\
\sum\sin\chi=\sum\cos\chi=\sum\sin2\chi=\sum\cos2\chi&=0,\\
\sum\sin3\chi&=3\sin3\chi,\qquad\sum\cos\chi=3\cos3\chi.
\end{aligned}
$$

将其代入第4部分的一般式，得到下列结果，可知：(a) 光谱随表面旋转呈六重对称；(b) 能得到(spp)、(psp)、(psp)、(pss)信号；(c) 即使倾斜角为$90^\circ$，依基板取向而定，也能得到(spp)、(psp)、(pps)、(sss)信号。

'''+angle+table(sym)+r'''
倾斜角为零时，不出现(spp)、(psp)、(pps)、(sps)、(pss)、(sss)信号。

> **译者注（原文疑点Q164，PDF p5—6）：** 求和式末项原写$\sum\cos\chi=3\cos3\chi$，候选左侧为$\sum\cos3\chi$，未采用。(b)中的(psp)重复，组合列表也与邻近句不同，均照原述保留。旧译将(b)、(c)改成“信号消失”，与原文相反，已恢复。

### 5c. C₄ᵥ、C₆ᵥ取向表面的和频张量

此时，因为：

$$
\sum\sin\chi=\sum\cos\chi=\sum\sin2\chi=\sum\cos2\chi
=\sum\sin3\chi=\sum\cos3\chi=0,
$$

所得表达式与第5a部分相同。
''','5b三重取向与全部15个分量、零倾角结论及5c完整求和式')

s=old[old.index('### 5d.'):old.index('### 5e.')]
start=s.index('**$(ppp)$')
tab=s[start:s.index('当 $b = 0$',start)]
def normalize(m):
    x=m[1].replace('b_{',r'\beta_{')
    x=re.sub(r'\\chi(?!_)',lambda z:r'\theta',x).replace(r'\phi',r'\chi')
    x=re.sub(r'(?<![A-Za-z\\])([ab])(?![A-Za-z_])',lambda z:r'\alpha' if z[1]=='a' else r'\beta',x)
    x=re.sub(r'\\(sin|cos)\s*([23])\\theta',lambda z:'\\'+z[1]+'^'+z[2]+r'\theta',x)
    if r'\chi_{yyy}' in x.split('=')[0]:x=x.replace(r'3\sin \alpha \cos \beta -',r'3\sin \alpha \cos \beta\chi -')
    return '$$\n'+x.strip()+'\n$$'
tab=re.sub(r'\$\$([\s\S]*?)\$\$',normalize,tab)
# Headings from the old version carry a suffix; table() keeps only formulas, so retain headings explicitly.
tab=re.sub(r'\*\*\$\((\w+)\)\$ 分量：\*\*',r'**(\1)**',tab)
add(319,[6,7],r'''### 5d. Cₛ取向表面的和频张量

这是关于垂直于表面的平面具有镜面对称的情况。例如，沿提拉方向取向的LB膜中，CH基团朝该平面两侧呈V形排列。设镜面对称面与表面的交线相对于CH轴表面投影的角为$+\beta$、$-\beta$，交线与$x$轴的取向角为$\alpha$，则面内取向角$\chi_{\mathrm{ip}}=\alpha+\beta$与$\alpha-\beta$的CH基团数量相同。

'''+angle+r'''
利用下列三角函数求和关系，将两种配置的正弦、余弦用$\chi$表示后相加，代入第4a部分的结果，即得所需表达式：

$$
\begin{aligned}
\sum1&=2,\\
\sum\sin\chi_{\mathrm{ip}}&=2\sin\alpha\cos\beta,&\sum\cos\chi_{\mathrm{ip}}&=2\cos\alpha\cos\beta,\\
\sum\sin2\chi_{\mathrm{ip}}&=2\sin2\alpha\cos2\beta,&\sum\cos2\chi_{\mathrm{ip}}&=2\cos2\alpha\cos2\beta,\\
\sum\sin3\chi_{\mathrm{ip}}&=2\sin3\alpha\cos3\beta,&\sum\cos3\chi_{\mathrm{ip}}&=2\cos3\alpha\cos3\beta.
\end{aligned}
$$

'''+tab+r'''
令$\beta=0$，即得表面固定系中的张量分量。和频实验中，若使入射面与对称面重合，全对称带不产生(spp)、(psp)、(pps)、(sss)光。

> **译者注（原文疑点Q165，PDF p6—7）：** 原文引用“第4a部分”，但本稿目录及正文仅有第4部分一般式；候选为指该一般式，未改原引用。原$\chi_{yyy}$括号内还在$3\sin\alpha\cos\beta$后带一个$\chi$，此处照录，候选为多余字符，未采用。其余表项的正负号均按原页保留，不据对称性猜改。这里的$\alpha,\beta$为几何角，$\beta$不是分子超极化率。
''','5d镜面几何、求和关系、全部27个分量及末尾选择规则')

s=prior(292);sym=s[s.index('#### 全对称振动'):s.index('#### 简并振动')]
add(320,[7,8],r'''### 5e. C₂ᵥ取向表面的和频张量

对应的情况是：在垂直于表面的平面内，CH基团两两呈V形排列并配对。所有CH基团的倾斜角$\theta_{\mathrm{tilt}}$相同，面内取向角为$\chi$与$\chi+\pi$的CH基团数量相同。利用三角函数求和关系，将两种配置的正弦、余弦用$\chi$表示后相加，得到下列结果。

'''+angle+r'''
$$
\begin{aligned}
\sum1&=2,\qquad\sum\sin\chi=\sum\cos\chi=0,\\
\sum\sin2\chi&=2\sin2\chi,\qquad\sum\cos2\chi=2\cos2\chi,\\
\sum\sin3\chi&=\sum\cos3\chi=0.
\end{aligned}
$$
'''+table(sym),'5e双取向定义、求和与全部13个分量及无信号项')

s=prior(293)
s='## 6. 从表面电场到和频极化\n\n和频极化矢量$\\mathbf P(\\omega_{\\mathrm{SF}})$与入射光的表面电场（$E^{(i)}(\\omega_{\\mathrm{vis}})$和$E^{(i)}(\\omega_{\\mathrm{IR}})$，即入射光与反射光电场的矢量和）通过下式联系：\n\n'+s[s.index('$$'):]
s=s.replace(r'\theta_I',r'\theta_i').replace('vis光、ir光','vis光、IR光')
s=s.replace(r'$\theta_i$与式中的$\theta_i$也按原文局部写法保留。','')
start=s.index('$$\nE_x^{(r)}');end=s.index('$$',start+2)
x=s[start:end].replace(r'E_y^{(r)}',r'E_y^{(i)}').replace(r'E_z^{(r)}',r'E_z^{(i)}')
s=s[:start]+x+s[end:]
s+=r'''
> **译者注（原文疑点Q166，PDF p8）：** 式(6.3)说明反射光，但原式$y,z$分量左侧写$E_y^{(i)}$、$E_z^{(i)}$，右侧为反射场；此处保留，候选左侧上标为$(r)$，未采用。式(6.5c)的$(n_1n_2/n')^2$也按本节原页保留。
'''
add(321,[8,9],s,'第6部分全部7个编号式，保留6.3的混用上标')
s=prior(294).replace('Q145','Q167').replace('PDF p18—19','PDF p9—10')
add(322,[9,10],s,'第7部分全部12个编号式、L因子及作者末尾符号不确定性')
print('B316—B322译文及分批记录已生成')

from 整节工具 import *
sec=part('### 4a.','### 4b.')
identities=maths(sec[:sec.index('#### ')])[:3]
# Old identities used varphi; these are theta identities, never power-normalize their left sides.
identities=[x.replace(r'\sin^2\theta =',r'\sin2\theta =').replace(r'\cos^2\theta =',r'\cos2\theta =').replace(r'\sin^3\theta =',r'\sin3\theta =').replace(r'\cos^3\theta =',r'\cos3\theta =').replace(r'\sin\theta + \sin^3\theta',r'\sin\theta + \sin3\theta').replace(r'\cos\theta - \cos^3\theta =',r'\cos\theta - \cos3\theta =') for x in identities]
identities[0]=r'\sin2\theta=2\sin\theta\cos\theta,\qquad\cos2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta'
add(299,[4,5],r'''## 4. 取向亚甲基的$\beta_{xyz}$（表面固定系）

### 4a. 一般式

用欧拉角$(\chi,\theta,\phi)$表示亚甲基相对于表面固定$(xyz)$系的取向，借助《变换矩阵(xyz)》或 *Appl. Spectrosc.* 中的表，可求得以下表面系张量分量。不过，关于倾斜角$\theta$，这里不用表中的$\sin\theta$、$\sin2\theta$、$\sin3\theta$形式，而通过下列关系写成$\sin\theta$、$\cos\theta$的幂：
'''+''.join(fmt(x) for x in identities)+r'''
为使结果也适用于CH伸缩以外的模式，以及一般具有$C_{2v}$对称性的分子，以下也列出面外($b_2$)振动的表达式。

'''+angle+r'''
须注意：即使面内取向随机，反对称振动带也只产生(ppp)、(ssp)、(sps)、(pss)信号；但与甲基不同，对称振动带在$\phi$不是$0$或$\pi/2$、且$\theta_{\mathrm{tilt}}\ne0$时，也会产生(spp)、(psp)、(pps)、(sss)信号。

**一般式。** 先由变换表求$\beta_{aac}$、$\beta_{bbc}$等对各张量分量的变换，再将对称模式的表达式整理为$\beta_{aac}+\beta_{bbc}$、$\beta_{aac}+\beta_{bbc}-2\beta_{ccc}$及$\beta_{aac}-\beta_{bbc}$的组合。

> **译者注（原文疑点Q151，PDF p5）：** 此处对分子面与$xy$面夹角的定义给出欧拉角$\phi=\pi/2+\phi$，而第2部分式(2-1)写$\phi=\phi$。同一字形被用于物理取向角与欧拉角，且偏移不同；本节各处按原文分别保留，不自行取消或补入$\pi/2$。后续套用必须核查采用哪一局部定义。

> **译者注（原文疑点Q152，PDF p5及后续近似条件）：** 以下若干表的原文条件写作$\beta_{\xi\xi\zeta}\gg\beta_{\xi\xi\zeta}\sim\beta_{\eta\eta\zeta}$，含同一量大于自身的矛盾；候选为第一个量应为$\beta_{\zeta\zeta\zeta}$，与第3部分近似一致，但尚未采用。重复出现的该条件按原式保留。
''','第4部分引入、三角恒等式、一般式条件及内部角偏移')
labels=[sym,anti,oop];names=['对称($a_1$)振动模式','反对称($b_1$)振动模式','面外($b_2$)振动模式']
for n,label,title,pages in zip([300,301,302],labels,names,[[5,6,7],[7,8],[8,9,10]]):
    g=group(sec,label)
    # Preserve all pre-table equations; remove only Chinese lead-in from TeX.
    pre=approx(g).replace(r'\text{ 的前提下，}', '')
    tab=table(g[g.index('#####'):])
    if n==301:
        # Original p8 has no grouping parentheses around 1-cos2phi in chi_xyx.
        def original_xyx(m):
            x=m[0]
            if r'\chi_{xyx}' in x.split('=')[0]:x=x.replace(r'(1 - \cos 2\phi)\sin\theta',r'1 - \cos 2\phi\sin\theta')
            return x
        tab=re.sub(r'\$\$[\s\S]*?\$\$',original_xyx,tab)
    note=''
    if n==300:note=r'''
> **译者注（原文疑点Q153，PDF p5—7）：** 表内项、符号与三条求和关系按原式保留；$\sin^2\theta$、$\sin^3\theta$及$\cos^2\theta$、$\cos^3\theta$均为幂，$2\phi$及$2\chi,3\chi$则为倍角。个别定界符的类型配对仅作排版整理，不改变分组范围。
'''
    if n==301:note=r'''
> **译者注（原文疑点Q153续，PDF p8）：** 反对称表的$\chi_{xyx}$行将“$+1-\cos2\phi$”直接接到后项，未像$\chi_{yxx}$那样给$1-\cos2\phi$加括号；正文保留此差异。$\chi_{zzy}$中的$\sin\theta-2\sin^3\theta$也与部分相邻分量不同。候选可从坐标变换重新核算，尚未采用。
'''
    if n==302:note=r'''
> **译者注（原文疑点Q153续，PDF p9—10）：** 面外表$\chi_{yxy}$的分组写法与$\chi_{xyy}$不同，未按后者重排；原三组张量求和为零的关系照录，不把该声明当作逐项代数验证。多行长式仅分行排版。
'''
    add(n,pages,'#### '+title+'\n\n'+pre+tab+note,f'4a{title}全部27个分量及原附无编号关系')

b=part('### 4b.','### 4c.')
intro=r'''### 4b. 自由旋转、随机扭转角

甲基的内部旋转（torsion）自由时，内部旋转角$\phi$在$0$至$2\pi$之间以相同概率取任意值。由于：

$$
\int_0^{2\pi}\cos(n\phi)\,d\phi=\int_0^{2\pi}\sin(n\phi)\,d\phi=0\qquad(n=1,2,3),
$$

简并振动的张量分量大幅简化如下。（注意：这与旋转冻结、$\phi$固定为$0$或$\pi$时的表达式不同。）

'''+angle+r'''
> **译者注（原文疑点Q154，PDF p10—13）：** 本段原文写“甲基”及“简并振动”，本节主题则是亚甲基；保留原述，候选为沿用前一稿时残留的表述，尚未改写。以下自由旋转表按原式保留，不据第4.2节的模式或归一化作替换。
'''
for n,ls,pp in [(303,[sym],[10,11]),(304,[anti,oop],[11,12,13])]:
    contents=intro if n==303 else ''
    for label in ls:
        g=group(b,label);title=names[labels.index(label)]
        contents+='\n\n#### '+title+'\n\n'+approx(g)+table(g[g.index('#####'):])
    add(n,pp,contents,'4b自由内部旋转'+('对称模式27分量' if n==303 else '反对称及面外模式各27分量'))

c=part('### 4c.','## 5.')
intro=r'''### 4c. 两个H原子等价时（内部旋转被冻结）

此时，内部旋转角为$\phi$的亚甲基与内部旋转角为$-\phi$的亚甲基彼此区分，张量也不同。将两种配置的张量分量相加，就得到第4a部分结果中删去乘有$\sin(n\phi)$（$n=1,2,3$）的项之后的表达式。

> **译者注（原文疑点Q155，PDF p13—16）：** 本段“彼此区分、张量不同”与两个H等价的标题及第2部分的等价配置说明如何对应，尚须核验；原述保留。原文说将两配置相加，表内系数却未明确另乘2，不能自行改成总和或平均的另一归一化。部分表间系数/符号差异和残缺项也保留，见后注。
'''
for n,ls,pp in [(305,[sym],[13,14,15]),(306,[anti,oop],[15,16])]:
    contents=intro if n==305 else ''
    for label in ls:
        g=group(c,label);title=names[labels.index(label)]
        tab=table(g[g.index('#####'):])
        if label==anti:
            def restore(m):
                x=m[0]
                if r'\chi_{yxz}' in x.split('=')[0]:x=x[:-2].rstrip()+' +\n$$'
                if r'\chi_{xyx}' in x.split('=')[0]:x=x.replace(r'(1 - \cos 2\phi)\sin\theta',r'1 - \cos 2\phi\sin\theta')
                return x
            tab=re.sub(r'\$\$[\s\S]*?\$\$',restore,tab)
        contents+='\n\n#### '+title+'\n\n'+approx(g)+tab
    if n==306:contents+=r'''
> **译者注（原文疑点Q155续，PDF p15）：** 反对称表$\chi_{yxz}$行在式末留下孤立的“$+$”，此处照录，不补缺项；其$\chi_{xyx}$行同样缺少$1-\cos2\phi$外括号。候选为删去残留加号、核对分组及与一般式的对应，但尚未采用。
'''
    add(n,pp,contents,'4c冻结旋转'+('对称模式全部27分量' if n==305 else '反对称及面外模式各27分量，保留残缺加号'))

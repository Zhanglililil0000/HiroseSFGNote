from 整节工具 import *
b='CH₃基：取C₃轴与CH(1)形成的平面为$\\xi\\zeta$平面，$\\xi$轴朝CH键外侧，即伞张开的方向。三个键的$\\eta$轴依次相差120°。沿C₃轴由C朝H₃取$c$轴，XCH(1)平面内由C₃轴朝H₁取$a$轴。从C看去，使H(1)、H(2)、H(3)依次顺时针排列。将分子轴重合到三个键系的欧拉角依次为$(0,\\pi+\\tau,0)$、$(0,\\pi+\\tau,2\\pi/3)$、$(0,\\pi+\\tau,-2\\pi/3)$；反向操作为$(0,\\pi-\\tau,0)$、$(-2\\pi/3,\\pi-\\tau,0)$、$(2\\pi/3,\\pi-\\tau,0)$。相应矩阵如下。\n\n'
for t in ['1.29a','1.30a','1.29b','1.30b','1.29c','1.30c']:
    e=eq(t)
    # 旧译1.30b/c遗留孤立end aligned，恢复完整环境。
    e=e.replace('\n\\end{aligned}\n$$','\n$$') if '\\begin{aligned}' not in e else e
    if t in ['1.30b','1.30c']:
        # 原文先列两个矩阵之积，再列乘积；补回旧译漏掉的因子矩阵。
        sign=1 if t.endswith('b') else -1
        rot=r'\begin{pmatrix}-1/2&'+(r'\sqrt3/2' if sign==1 else r'-\sqrt3/2')+r'&0\\'+(r'-\sqrt3/2' if sign==1 else r'\sqrt3/2')+r'&-1/2&0\\0&0&1\end{pmatrix}'
        base=r'\begin{pmatrix}-\cos\tau&0&-\sin\tau\\0&1&0\\\sin\tau&0&-\cos\tau\end{pmatrix}'
        idx=e.index('=\n\\begin{pmatrix}')
        e=e[:idx]+'=\n'+rot+base+'\n=\n'+e[idx+2:]
    b+=e
add(259,b,[10,11,12],'Q127：原欧拉角描述与1.29b/c各处正负号并不完全对应，矩阵乘积与已展开的元素也有差异；全部按原式保留。旧译将π写为ρ、τ写为t、两坐标箭头方向颠倒及漏掉1.30b/c的乘积矩阵已按底本修复。候选按乘法重新计算，未采用。')
b='计算$\\boldsymbol\\alpha_a=U^{-1}\\boldsymbol\\alpha_{\\xi}U$，得到各键的结果：\n\n'
for t in ['1.31a','1.31b','1.31c']:
    e=eq(t)
    if t!='1.31a':
        e=e.replace('=\n\\begin{pmatrix}','=\\frac14\n\\begin{pmatrix}').replace('\\frac{1}{4}\\alpha','\\alpha')
    b+=e
b+='像CH₂那样求和：\n\n'+eq('1.32').replace('\\mp\\sqrt{3}', '\\sqrt{3}')+'参照(1.7)，得到：\n\n'+eq('1.33')
b+='若CH键保持轴对称，则$\\alpha_{\\xi\\xi}=\\alpha_{\\eta\\eta}=r\\alpha_{\\zeta\\zeta}$。令$(d\\alpha_{\\zeta\\zeta}/dr)_0=\\alpha_0$，可简化为：\n\n'+eq('1.34')
add(260,b,[12,13],'Q127：1.31b与1.31c原印成相同矩阵；共同1/4因子及右下元素均按原字形保留，不用理论对称性修订。1.33/1.34的部分G下标原印deb，候选deg未采用；后续与1.29/1.30变换结果的符号/系数差异仍待核。')
b='### 和频张量\n\n给出振动共振的和频张量与振动偶极矩和拉曼张量有下列关系：\n\n'+eq('1.35')
b+='代入前面结果，并记$b_0=(d\\alpha_{\\zeta\\zeta}/dr)_0(d\\mu_{\\mathrm{CH}}/dr)_0$，得到：\n\n**CH基**\n\n'+eq('1.36a')
b+='**CH₂基**\n\n比较(1.11)第二、三行可知对称模式$Q_{a1}$沿$c$轴振动，因此$a_1$振动的(1-35)中第三下标$k$只取$c$。反对称$Q_{b1}$沿$a$轴振动，故$b_1$振动的$k$只取$a$。\n\n$a_1$振动：\n\n'+eq('1.37a').replace('\\sqrt{G_{a1}}','G_{a1}')+'$b_1$振动：\n\n'+eq('1.38').replace('\\sqrt{G_{b1}}','G_{b1}')
b+='**CH₃基**\n\n由(1.13)第二、三行可知，全对称模式沿$c$轴，简并模式$Q_{\\mathrm{deg},a}$、$Q_{\\mathrm{deg},b}$分别沿$a,b$轴，因此：\n\n$a_1$振动：\n\n'+eq('1.39a')+'$e$振动：\n\n'+eq('1.40a')
b=b.replace('\\beta_0','b_0')
b+='以上是假定CH键的分子极化率不变地给出甲基与亚甲基响应时的和频张量。若考虑成键导致轴对称性破缺，则须独立取$\\alpha_{\\xi\\xi}$与$\\alpha_{\\eta\\eta}$；前述推导也保留了处理这种情况的可能。\n\n'
add(261,b,[13,14],'Q128：这里的b0按原文拉丁字母保留，与要点β0定义相近但不静默改名。β为分子二阶场响应，不能将1.35的张量关系称为已平方的光强。1.37b等系数与前后归一化差异原样保留；不凭乘积推导补因子。')

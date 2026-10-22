from 整节工具 import *
bs=re.findall(r'\\\[([\s\S]*?)\\\]',old[old.index('## 附录4：'):])
def m(i):
    t=bs[i].replace('m_C','\\mu_C').replace('m_H','\\mu_H')
    if i==0: t=t.replace('1/2','\\sqrt{1/2}').replace('\\begin{pmatrix} S_1 \\\\ S_2 \\\\ S_3 \\end{pmatrix}',r'\mathbf S')
    if i==4:t=t.replace('2\\mu_C','\\sqrt2\\mu_C')
    if i==5:t=t.replace('2(s^2 F - t^2 F\')','\\sqrt2(s^2 F - t^2 F\')')
    if i==6:t=t.replace('= 2[','= \\sqrt2[')
    if i==9:t=t.replace('4\\mu_C\\cos t]','4\\mu_C\\cos]')
    if i==10:t=t.replace('2s^2 F)] -','2s^2 F)]^2 -')
    return math(t)
b='## 附录4：CH₃基团C₃ᵥ对称性破缺时的处理\n\n若一个CH与表面相互作用，使CH(1)与其余CH(2)、CH(3)的环境或键强不同，C₃ᵥ会降为以垂直表面的平面为镜面的Cₛ。简并被解除，形成两个面内模式（CH(1)与CH(2)H(3)对称振动强混合）和一个面外模式（CH(2)H(3)反对称振动）；两个面内模式的频率及形状分别接近$Q_{\\mathrm{sym}}$和$Q_{\\mathrm{deg},a}$。\n\n只要力常数差异不大，分子固定系的和频张量可视为变化很小。但甲基取向、扭转角被固定后，实验室系张量不同于自由转动时，带间相对强度可随扭转角显著改变（参见另文《CH₃的取向与张量分量》）。内部转动冻结时，$Q_{\\mathrm{deg},b}$对应的CH(2)H(3)反对称振动平行于表面，只有对应$Q_{\\mathrm{sym}}$与$Q_{\\mathrm{deg},a}$的面内模式对IRAS及和频过程活性。\n\n定义分子内对称坐标：\n\n'+m(0)
b+='按水岛、岛内及中川教材，取内坐标G与F矩阵为：\n\n'+m(1)+math(r'\mu_C=1/m_C,\qquad\mu_H=1/m_H,\qquad\tau:\ \text{HCH夹角}')+m(2)+m(3)
b+='$K$为CH伸缩力常数（4.6 md/Å），$F$为H···H排斥常数（小于0.3 md/Å）。由此得到：\n\n'+m(4)+m(5)+'因此各乘积元素为：\n\n'+m(6)
b+='其中二维块的本征值为：\n\n'+m(7)+m(8)+'令$K_1=K_2+\\Delta K$，得到：\n\n'+m(9)+'因此：\n\n'+m(10)
add(275,b,[30,31],'Q137：Gs/Fs非对角元原为√2因子，旧译2已修复；μ为倒数质量，旧译m已恢复。原乘积21项中的K₁+2s²F、D²近似式中缺τ的cos及D展开首项平方均照录，可能与直接矩阵乘法/量纲不符；候选依定义重算，未采用。')
b='进而：\n\n'+m(11)
b+='简并振动带的分裂约为$(1/3)(\\Delta K/K_2)\\nu_{\\mathrm{deg}}$，全对称带位移约为$(1/6)(\\Delta K/K_2)\\nu_{\\mathrm{sym}}$。正四面体角下，$\\cos\\tau=-1/3$、$s=\\sqrt{2/3}$、$t=\\sqrt{1/3}$，因此：\n\n'+m(12)
b+='### L矩阵\n\n联系简正坐标Q与对称坐标S的L矩阵具有如下性质（参见水岛、岛内教材）：\n\n'+m(13)+m(14)
b+='由$GFL=L\\Lambda$，令$E=GF$，得到：\n\n'+m(16)+m(17)
b+='将此代入由$LL^{\\mathrm t}=G$得到的关系：\n\n'+m(18)
b+=math(r'''L_{11}^2=-(E_{12}E_{21})^2
\frac{\dfrac{G_1}{[(E_1-E_2)/2-\sqrt{(E_1-E_2)^2/4+E_{12}E_{21}}]^2}-\dfrac{G_2}{E_{21}^2}}
{2(E_1-E_2)\sqrt{(E_1-E_2)^2/4+E_{12}E_{21}}}''')
b+=math(r'''L_{22}^2=-(E_{12}E_{21})^2
\frac{-\dfrac{G_1}{E_{12}^2}+\dfrac{G_2}{[(E_1-E_2)/2-\sqrt{(E_1-E_2)^2/4+E_{12}E_{21}}]^2}}
{2(E_1-E_2)\sqrt{(E_1-E_2)^2/4+E_{12}E_{21}}}''')
b+='若$K_1=K_2\\gg F$，有$L_{12}\\approx-\\sqrt2L_{22}$、$L_{21}\\approx\\sqrt2L_{11}$，进一步得$L_{11}^2\\approx L_{22}^2\\approx1/3$。因此$L_{11}\\approx1/\\sqrt3$、$L_{22}\\approx-1/\\sqrt3$，从而：\n\n'+math(r'Q_1\approx(1\sqrt3)[\Delta r_1+\Delta r_2+\Delta r_3]=Q_{\mathrm{sym}}')+math(r'Q_2\approx(1\sqrt6)[2\Delta r_1-\Delta r_2-\Delta r_3]=Q_{\mathrm{deg},a}')
b+='也就是说，只要力常数变化不大，振动模式几乎仍与C₃ᵥ甲基相同。但空间取向固定会使和频张量出现新的项，振动带强度也将改变（参见《CH₃基的取向与张量分量》）。\n\n'
add(276,b,[32,33],'Q137：末两坐标式原括号内为1√3、1√6，分数线/斜线不清或缺失，此处保留可见字形，候选1/√3、1/√6未采用。L平方式恢复原双层分式，旧译展平为乘积的错误已修复；L归一化及质量尺度仍按原局部结果保留。')

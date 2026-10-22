from pathlib import Path
import re
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.1 *.md'))
s=p.read_text(encoding='utf-8')
start=s.index('逆矩阵 $(E - A)^{-1}$')
end=s.index('$$\n\\begin{aligned}\n\\Delta',start)
matrix=r'''逆矩阵 $(E-A)^{-1}$ 如下。为避免原文横向拆开的三列被误读为两个矩阵，这里将九个元素分别列出；$M_{ij}$ 仅为译者的排版标识，不是新增物理量。

$$
(E-A)^{-1}=\frac{1}{\Delta}
\begin{pmatrix}M_{11}&M_{12}&M_{13}\\M_{21}&M_{22}&M_{23}\\M_{31}&M_{32}&M_{33}\end{pmatrix}.
\tag{2.7}
$$

$$
\begin{aligned}
M_{11}={}&1-\alpha_{m'}-\alpha_{m''}-\beta_{mm'}-\beta_{m'm''}-\gamma_{mm''}\\
&+\alpha_m\alpha_{m'}+\alpha_{m'}\alpha_{m''}+\alpha_m\alpha_{m''}\\
&+\alpha_m\beta_{m'm''}+\alpha_{m''}\beta_{mm'}-\alpha_m\alpha_{m'}\alpha_{m''},\\[4pt]
M_{12}={}&(1-\alpha_{m''}-\beta_{m'm''}-\gamma_{mm''})r_{m1}r_{m'm''}t_{m'm}a_{m'}a_m^2\\
&+(\alpha_{m'}+\beta_{mm'})r_{m1}r_{m''2}t_{m''m'}t_{m'm}t_{mm'}a_{m''}^2a_{m'}a_m^2,\\[4pt]
M_{13}={}&r_{mm'}r_{m''2}t_{m''m'}t_{m'm}a_{m''}a_{m'}a_m^2,\\[4pt]
M_{21}={}&(\alpha_m-\alpha_m\alpha_{m''})t_{mm'}a_{m'},\\[4pt]
M_{22}={}&1-\alpha_{m''}-\beta_{m'm''}-\gamma_{mm''}
+\alpha_m\alpha_{m''}+\alpha_m\beta_{m'm''},\\[4pt]
M_{23}={}&(1-\alpha_m)r_{m'm}r_{m''2}t_{m''m'}a_{m''}a_{m'}\\
&+r_{m1}r_{m''2}t_{m''m'}t_{mm'}t_{m'm}a_{m''}a_{m'}^2a_m^2,\\[4pt]
M_{31}={}&\alpha_m t_{mm'}t_{m'm''}a_{m''}a_{m'},\\[4pt]
M_{32}={}&(\alpha_{m'}+\beta_{mm'}-\alpha_m\alpha_{m'})t_{m'm''}a_{m''},\\[4pt]
M_{33}={}&1-\alpha_m-\alpha_{m'}-\beta_{mm'}-\alpha_m\alpha_{m'}.
\end{aligned}
$$

> **译者注（Q034）：** 式（2.7）按底本九个元素重排，未据逆矩阵性质修正原式。$M_{11}$、$M_{13}$、$M_{33}$ 等与式（2.3）的代数衔接尚待独立核验。旧译将第三列排成游离的三行，现恢复其所属行列；$M_{23}$ 首项的 $a_{m'}$ 次数亦已按底本恢复。

'''
s=s[:start]+matrix+s[end:]
# Keep the printed row result in 2.9 without supplying the missing prefactor.
start=s.index('因此：',s.index('\\tag{2.8}'))
end=s.index('确定所考虑的光的发光部位',start)
part=s[start:end]
part=part.replace(r'\begin{pmatrix}',r'\begin{pmatrix}',1)
note='\n> **译者注（Q034续）：** 底本式（2.9）右端未显式列出式（2.7）的公共因子 $1/\\Delta$，这里照录；不能据此默认该因子已隐含或可省略。本式长行仅作分行排版，分量顺序保持为行向量。\n\n'
s=s[:start]+part+note+s[end:]
# Restore outside-cosine factors in all three depth definitions.
for key in ['m',"m'","m''"]:
    s=s.replace(r'e^{i k_{'+key+r'} z_{'+key+r'} / \cos\theta_{'+key+r'}}',r'\frac{e^{i k_{'+key+r'} z_{'+key+r'}}}{\cos\theta_{'+key+r'}}')
    s=s.replace(r'e^{i k_{'+key+r'} (h_{'+key+r'} - z_{'+key+r'}) / \cos\theta_{'+key+r'}}',r'\frac{e^{i k_{'+key+r'} (h_{'+key+r'} - z_{'+key+r'})}}{\cos\theta_{'+key+r'}}')
# Source down-going m-layer z0 ends a_m' (not old a_m).
s=s.replace(r"z_0 = E^+(z_m) a_{m0}^* t_{mm'} t_{m'm''} a_{m''} a_m",r"z_0 = E^+(z_m) a_{m0}^* t_{mm'} t_{m'm''} a_{m''} a_{m'}",1)
pos=s.index('对于下行光：',s.index('\\tag{2.10}'))
s=s[:pos]+r'''> **译者注（Q033、Q035）：** 星号在这里由底本单独定义为到另一侧界面的因子，不按通常习惯解释为复共轭；底本余弦在指数外。上下行初始系数、无反射直接出射项及式（2.11）—（2.15）均依原文，部分相位因子和透射下标仍需推导核验。式（2.13）、（2.15）公共分母的若干下标在底本有异常字形；本译文沿式（2.8）、（2.11）已定义的同一分母记号转写，字形问题保留，不作为新确定公式。

'''+s[pos:]
s=s.replace('当发光为相干时：','> **译者注（Q035续）：** 下述积分先后次序及上下行积分限按作者文字保留。“取平方”未在此明确复场的模平方、归一化及不同深度场的相位权重，不能据这两句话直接完成绝对光强计算。\n\n当发光为相干时：',1)
# Formula A.6: source brackets enclose both terms under 1/2; source says not equal 0.
s=s.replace('$u_2 v_2 \\leq 0$','$u_2 v_2 \\ne 0$')
for label in ['a','b']:
    pat=r'\$\$\s*([\s\S]*?)\\tag\{A\.6'+label+r'\}\s*\$\$'
    matches=list(re.finditer(pat,s))
    m=matches[-1]
    # locate only the nearest display start
    end=m.end();begin=s.rfind('$$',m.start(),s.index(r'\tag{A.6'+label+'}',m.start()))
    tex=(r'u_2^2 = \frac12\Biggl\{\bigl[n_2^2(1-\kappa_2^2)-n_1^2\sin^2\theta_1\bigr]'
         if label=='a' else r'v_2^2 = \frac12\Biggl\{\bigl[-n_2^2(1-\kappa_2^2)-n_1^2\sin^2\theta_1\bigr]')
    tex+=r'+\sqrt{\bigl[n_2^2(1-\kappa_2^2)-n_1^2\sin^2\theta_1\bigr]^2+4n_2\kappa_2^2}\Biggr\}'
    # Above original radicand is 4 n_2 kappa_2^2 (no square on n_2).
    replacement='$$\n'+tex+'\n\\tag{A.6'+label+'}\n$$'
    s=s[:begin]+replacement+s[end:]
s=s.replace('菲涅尔系数','菲涅尔因子')
# Quoted file name stays original Japanese.
s=s.replace('另一文件"菲涅尔因子等"','作者另备文件「フレネル係数など」')
s=s.replace('如第 2 章所示','如本文第2部分所示')
pos=s.index('**反射与折射**',s.index('## 附录 A'))
s=s[:pos]+r'''> **译者注（Q036）：** 本附录的 $\chi$ 是线性极化率。式（A.3）、（A.4）的复折射率左右沿用同一 $n$ 字形；$\mu$ 的意义及符号相容性未明确。底本式（A.6a/b）的 $1/2$ 作用于整个花括号，旧译漏掉这一作用范围，现按底本恢复；根式内末项按可见原文为 $4n_2\kappa_2^2$，不同于旧译的 $4n_2^2\kappa_2^2$。这些原式的物理与代数正确性仍待核验，不据常见公式改号或改幂次。

'''+s[pos:]
# Clarify original convergence claim without replacing it.
pos=s.index('当矩阵 $A$ 的所有元素的绝对值均小于 1 时',s.index('## 附录 B'))
s=s[:pos]+r'''> **译者注（Q037）：** 下文“所有元素绝对值小于1即可使 $A^n$ 趋于零”是底本原有表述，并非本译本确认的充分条件。例如二维矩阵所有元素均为 $3/4$ 时，沿向量 $(1,1)^T$ 的放大因子为 $3/2$，其幂不趋于零。故应另行核验矩阵幂的收敛性；正文及式（B.6）保留原文条件，不把该条件用于未经检查的数值计算。第2部分应用几何级数处同受此限制。

'''+s[pos:]
# Join fragments of the same numbered formula, preventing unmatched delimiters.
for tag in ['2.11','2.13','2.15']:
    end=s.index(r'\tag{'+tag+'}')
    anchor=s.rfind('在此基础上',0,end)
    if anchor<0: anchor=s.rfind('可得',0,end)
    begin=s.index('$$',anchor)
    part=s[begin:end]
    part=part.replace('$$\n\n$$','\\\\[6pt]\n')
    # wrap the assembled expression so linebreaks are legal
    part=part.replace('$$\n','$$\n\\begin{aligned}\n',1)
    part=part.replace('\\\\[6pt]\n\\times','\\\\[6pt]\n&\\times')
    part=part.replace('\\\\[6pt]\n+ E','\\\\[6pt]\n&+ E')
    s=s[:begin]+part+'\n\\end{aligned}\n'+s[end:]
p.write_text(s,encoding='utf-8')
print('矩阵、深度因子、附录A/B已校订；待格式检查')

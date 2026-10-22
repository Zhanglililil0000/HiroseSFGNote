from pathlib import Path
import shutil
r=Path('HiroseSFGNote').resolve();p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';o=r/'翻译管理/校订记录/1.1';s=p.read_text(encoding='utf-8');a=s.index('**（差频过程（DFG））**');b=s.index('\u200b\t上述公式表示的是',a);assert not (o/'B006-修订前.md').exists();shutil.copy2(p,o/'B006-修订前.md')
t=r'''**（差频过程（DFG））**

相应的二阶非线性极化率为

$$
\begin{aligned}
\chi_{ijk}^{(2)}(\omega=\omega_1-\omega_2)
&=\frac{P_i^{(2)}(\omega=\omega_1-\omega_2)}{E_j(\omega_1)E_k(-\omega_2)}\\[4pt]
&=-\frac{Ne^3}{\hbar^2}\sum_{g,n,n'}
\left\{
\begin{aligned}
&-\frac{(r_k)_{gn'}}{\omega_2-\omega_{n'g}-i\Gamma_{n'g}}
\left[
\frac{(r_j)_{n'n}(r_i)_{ng}}{\omega_1-\omega_2+\omega_{ng}+i\Gamma_{ng}}
-\frac{(r_i)_{n'n}(r_j)_{ng}}{\omega_1-\omega_2+\omega_{n'n}+i\Gamma_{n'n}}
\right]\\[8pt]
&-\frac{(r_k)_{ng}}{\omega_2+\omega_{ng}-i\Gamma_{ng}}
\left[
\frac{(r_i)_{gn'}(r_j)_{n'n}}{\omega_1-\omega_2-\omega_{n'g}+i\Gamma_{n'g}}
-\frac{(r_j)_{gn'}(r_i)_{n'n}}{\omega_1-\omega_2-\omega_{nn'}+i\Gamma_{nn'}}
\right]\\[8pt]
&+\frac{(r_j)_{ng}}{\omega_1-\omega_{ng}+i\Gamma_{ng}}
\left[
\frac{(r_i)_{gn'}(r_k)_{n'n}}{\omega_1-\omega_2-\omega_{n'g}+i\Gamma_{n'g}}
-\frac{(r_k)_{gn'}(r_j)_{n'n}}{\omega_1-\omega_2-\omega_{nn'}+i\Gamma_{nn'}}
\right]\\[8pt]
&+\frac{(r_j)_{gn'}}{\omega_1+\omega_{n'g}+i\Gamma_{n'g}}
\left[
-\frac{(r_k)_{n'n}(r_i)_{ng}}{\omega_1-\omega_2+\omega_{ng}+i\Gamma_{ng}}
-\frac{(r_i)_{n'n}(r_k)_{ng}}{\omega_1-\omega_2-\omega_{nn'}+i\Gamma_{nn'}}
\right]
\end{aligned}
\right\}\rho_g^{(0)}.
\end{aligned}
\tag{11}
$$

> **译者注（原文疑误）：** 本式第三组方括号内第二项的分子，原文为 $(r_k)_{gn'}(r_j)_{n'n}$，这里照录。其中 $j$ 是否为 $i$ 之误，尚待核验。

（当 $\omega_1=\omega_2$ 时，产生直流电场，即整流效应；当 $\omega_1\ne\omega_2$ 时，对应差频过程（DFG）。）

'''
head=s[:a].replace('二阶响应式（10）及其 SHG/SFG 说明（B003–B005），式（11）起仍为待校订旧译。','差频式（11）及其整流/DFG说明（B003–B006），其后解释段仍为待校订旧译。').replace('第 4 页至式（10）后的说明。','第 4 页至式（11）后的说明。');p.write_text(head+t+s[b:],encoding='utf-8')
assert p.read_text(encoding='utf-8').split('\u200b\t上述公式表示的是',1)[1]==s.split('\u200b\t上述公式表示的是',1)[1]
print('B006 eq11 transcribed without silent index correction; note added; later text preserved.')

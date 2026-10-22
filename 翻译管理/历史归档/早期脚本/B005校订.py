from pathlib import Path
import shutil
r=Path('HiroseSFGNote').resolve();p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';o=r/'翻译管理/校订记录/1.1';s=p.read_text(encoding='utf-8');a=s.index('**（二阶非线性极化：三波混频）**');b=s.index('**（差频过程（DFG））**',a);assert not (o/'B005-修订前.md').exists();shutil.copy2(p,o/'B005-修订前.md')
t=r'''**（二阶非线性极化：三波混频）**

相应的二阶非线性极化率为

$$
\begin{aligned}
\chi_{ijk}^{(2)}(\omega=\omega_1+\omega_2)
&=\frac{P_i^{(2)}(\omega=\omega_1+\omega_2)}{E_j(\omega_1)E_k(\omega_2)}\\[4pt]
&=-\frac{Ne^3}{\hbar^2}\sum_{g,n,n'}
\left\{
\begin{aligned}
&\frac{(r_k)_{ng}}{\omega_2-\omega_{ng}+i\Gamma_{ng}}
\left[
\frac{(r_i)_{gn'}(r_j)_{n'n}}{\omega_1+\omega_2-\omega_{n'g}+i\Gamma_{n'g}}
-\frac{(r_j)_{gn'}(r_i)_{n'n}}{\omega_1+\omega_2+\omega_{n'n}+i\Gamma_{n'n}}
\right]\\[8pt]
&+\frac{(r_k)_{gn'}}{\omega_2+\omega_{n'g}+i\Gamma_{n'g}}
\left[
\frac{(r_j)_{n'n}(r_i)_{ng}}{\omega_1+\omega_2+\omega_{ng}+i\Gamma_{ng}}
-\frac{(r_i)_{n'n}(r_j)_{ng}}{\omega_1+\omega_2-\omega_{nn'}+i\Gamma_{nn'}}
\right]\\[8pt]
&+\frac{(r_j)_{ng}}{\omega_1-\omega_{ng}+i\Gamma_{ng}}
\left[
\frac{(r_i)_{gn'}(r_k)_{n'n}}{\omega_1+\omega_2-\omega_{n'g}+i\Gamma_{n'g}}
-\frac{(r_k)_{gn'}(r_i)_{n'n}}{\omega_1+\omega_2-\omega_{nn'}+i\Gamma_{nn'}}
\right]\\[8pt]
&+\frac{(r_j)_{gn'}}{\omega_1+\omega_{n'g}+i\Gamma_{n'g}}
\left[
\frac{(r_k)_{n'n}(r_i)_{ng}}{\omega_1+\omega_2+\omega_{ng}+i\Gamma_{ng}}
-\frac{(r_i)_{n'n}(r_k)_{ng}}{\omega_1+\omega_2-\omega_{nn'}+i\Gamma_{nn'}}
\right]
\end{aligned}
\right\}\rho_g^{(0)}.
\end{aligned}
\tag{10}
$$

（当 $\omega_1=\omega_2$ 时，对应倍频过程（SHG）；当 $\omega_1\ne\omega_2$ 时，对应和频过程（SFG）。）

'''
head=s[:a].replace('至线性响应式（9）（B003–B004），式（10）起仍为待校订旧译。','至二阶响应式（10）及其 SHG/SFG 说明（B003–B005），式（11）起仍为待校订旧译。').replace('第 4 页至式（9）。','第 4 页至式（10）后的说明。');p.write_text(head+t+s[b:],encoding='utf-8')
assert p.read_text(encoding='utf-8').split('**（差频过程（DFG））**',1)[1]==s.split('**（差频过程（DFG））**',1)[1]
print('B005 eq10 typeset; all four contributions retained; DFG eq11 onward unchanged.')

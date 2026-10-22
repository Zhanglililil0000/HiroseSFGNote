from 收尾公式工具 import *
a2=math(r'k=2\pi/\lambda=2n\pi/\lambda_0,\qquad c=\omega/k_0,\qquad\varepsilon=c^2k^2/\omega^2,\qquad n=ck/\omega.','A.2')
a3=math(al(r'\varepsilon&=1+4\pi\chi,\qquad\chi=\chi\prime+i\chi\prime\prime,',r'n&=n(1+i\kappa),\qquad n^2(1-\kappa^2)=\mu+4\pi\mu\chi\prime,',r'n^2\kappa&=2\pi\mu\chi\prime\prime.'),'A.3')+'\n$\\kappa$：衰减指数、消光指数。\n'
a45=math(r'n_2=n_2(1+i\kappa_2)=n_2+in_2\kappa_2','A.4')+math(r'n_2\cos\theta_2=u_2+iv_2','A.5')
inner=r'n_2^2(1-\kappa_2^2)-n_1^2\sin^2\theta_1';root=r'\sqrt{\left['+inner+r'\right]^2+4n_2^2\kappa_2^2}'
a6=math(r'u_2^2=\frac12\left\{\left['+inner+r'\right]+'+root+r'\right\}','A.6a')+math(r'v_2^2=\frac12\left\{-\left['+inner+r'\right]+'+root+r'\right\}','A.6b')
a7=math(al(r'r_{12}^s&=E_r^s/E_i^s=(k_{1z}-k_{2z})/(k_{1z}+k_{2z})',r'&=(n_1\cos\theta_1-n_2\cos\theta_2)/(n_1\cos\theta_1+n_2\cos\theta_2)',r'&=-\sin(\theta_1-\theta_2)/\sin(\theta_1+\theta_2),',r'r_{12}^p&=E_r^p/E_i^p=(\varepsilon_1k_{2z}-\varepsilon_2k_{1z})/(\varepsilon_2k_{1z}+\varepsilon_1k_{2z})',r'&=(n_1\cos\theta_2-n_2\cos\theta_1)/(n_2\cos\theta_1+n_1\cos\theta_2)',r'&=-\tan(\theta_1-\theta_2)/\tan(\theta_1+\theta_2).'),'A.7')
a8=math(al(r't_{12}^s&=E_t^s/E_i^s=2k_{1z}/(k_{1z}+k_{2z})',r'&=2n_1\cos\theta_1/(n_1\cos\theta_1+n_2\cos\theta_2)',r'&=2\cos\theta_1\sin\theta_2/\sin(\theta_1+\theta_2),',r't_{12}^p&=E_t^p/E_i^p=2\varepsilon_1k_{2z}\cos\theta_1/(\varepsilon_2k_{1z}+\varepsilon_1k_{2z})',r'&=2n_1\cos\theta_1/(n_2\cos\theta_1+n_1\cos\theta_2)',r'&=2\cos\theta_1\sin\theta_2/\sin(\theta_1+\theta_2)\cos(\theta_1-\theta_2).'),'A.8')
a9=math(r'r_{21}^s=-r_{12}^s,\qquad r_{21}^p=-r_{12}^p','A.9a')+math(r't_{21}^s=(n_2\cos\theta_2/n_1\cos\theta_1)t_{12}^s,\qquad t_{21}^p=(n_2\cos\theta_2/n_1\cos\theta_1)t_{12}^p','A.9b')
fields=math(al(r'E_{x,i}&=E_i^p\cos\theta_1,\quad E_{y,i}=E_{ri}^s,\quad E_{z,i}=-E_i^p\sin\theta_1,',r'E_{x,r}&=E_r^p\cos\theta_1,\quad E_{y,r}=E_r^s,\quad E_{z,r}=E_r^p\sin\theta_1,',r'E_{x,t}&=E_t^p\cos\theta_2,\quad E_{y,t}=E_t^s,\quad E_{z,t}=-E_t^p\sin\theta_2.'))
a1011=math(r'r_{12}^x=r_{12}^p,\quad r_{12}^y=r_{12}^s,\quad r_{12}^z=-r_{12}^p','A.10a')+math(r'r_{21}^x=-r_{12}^p,\quad r_{21}^y=-r_{12}^s,\quad r_{21}^z=r_{12}^p','A.10b')+math(al(r't_{12}^x&=(\cos\theta_2/\cos\theta_1)t_{12}^p,\quad t_{12}^y=t_{12}^s,',r't_{12}^z&=(\sin\theta_2/\sin\theta_1)t_{12}^p=(n_1/n_2)t_{12}^p'),'A.11a')+math(r't_{21}^x=(n_2/n_1)t_{12}^p,\quad t_{12}^y=t_{12}^s,\quad t_{12}^z=(\cos\theta_2/\cos\theta_1)(n_2/n_1)^2t_{12}^p','A.11b')
a12=math(r'1+r_{12}^x=t_{12}^x,\quad1+r_{12}^y=t_{12}^y,\quad1+r_{12}^z=(n_2/n_1)^2t_{12}^z')+math(al(r'1+r_{12}^sr_{21}^s&=1-(r_{12}^s)^2=t_{12}^st_{21}^s,',r'1+r_{12}^pr_{21}^p&=1-(r_{12}^p)^2=t_{12}^pt_{21}^p.'),'A.12')
note='\n> **译校注（Q072，保留原式）：** 式（A.3、A.4）同用 $n$ 表示复量与实量；轴向分量首行写 $E^s_{ri}$；（A.11b）首项为 $t^x_{21}$，随后两项却为 $t^y_{12},t^z_{12}$。式（A.8）末行采用原有斜线与连乘写法，括号作用范围不作补改。这些记号按原式保留，复数与边界条件约定另见Q053。\n'
job('B111','附录A全部余留公式数学转写',{'B077-p35-01.png':a2,'B077-p35-02.png':a3,'B077-p35-03.png':a45,'B077-p35-04.png':a6,'B077-p36-05.png':a7,'B077-p36-06.png':a8,'B077-p36-07.png':a9,'B077-p37-08.png':fields,'B077-p37-09.png':a1011+note,'B077-p37-10.png':a12})
b1=math(r'E_0(\omega)\cos(kz-\omega t)=\tfrac12[\exp(ikz-i\omega t)+\mathrm{c.c.}]')+'\nc.c.表示紧邻前项的复共轭。\n'
b2=math(r'E_0(\omega)\cos(kz-\omega t)=\operatorname{Re}[\exp(ikz-i\omega t)]')
job('B112','附录B两种实电场表示法',{'B078-p38-01.png':b1,'B078-p38-02.png':b2})
apply()

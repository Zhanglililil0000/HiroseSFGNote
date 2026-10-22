from 收尾公式工具 import *
phi=r'i2\pi n_m2h_m\cos\theta_m/\lambda';ep=X(phi);den='1-r_{m2}r_{m1}'+ep
c2=math(al(r'&r_{1m}+t_{1m}t_{m1}r_{m2}\sum_{n=1}^{\infty}(r_{m2}r_{m1})^{n-1}\exp(i2\pi n2n_mh_m\cos\theta_m/\lambda)',r'&=r_{1m}+'+F('t_{1m}t_{m1}r_{m2}'+ep,den),r'&='+F(r'r_{1m}+[-r_{1m}r_{m1}+t_{1m}t_{m1}]r_{m2}'+ep,den),r'&='+F('r_{1m}+r_{m2}'+ep,den)),'C.2')
c3path=math(r'\left[t_{1m}t_{m2}+t_{1m}t_{m2}\sum_{n=1}^{\infty}(r_{m2}r_{m1})^n\exp(in_m2\pi n2h_m\cos\theta_m/\lambda)\right]\exp(i2\pi n_mh_m\cos\theta_m/\lambda)')
c3=math('='+F(r't_{1m}t_{m2}\exp(i2\pi n_mh_m\cos\theta_m/\lambda)',den),'C.3')
def internal():
 d=r'1-(r_{m2}r_{m1})\exp(ik_m2h_m\cos\theta_m)'
 return '**上行（−）光的电场：**\n\n'+math(F(r't_{1m}r_{m2}\exp[-i\omega t+ik_m(x\sin\theta_m+(2h_m-z)\cos\theta_m)]',d))+'\n**下行（+）光的电场：**\n\n'+math(F(r't_{1m}\exp[-i\omega t+ik_m(x\sin\theta_m+z\cos\theta_m)]',d))
job('B113','附录C反射透射求和与A、B点内部场',{'B080-p42-03.png':c2,'B080-p43-06.png':c3path,'B080-p44-07.png':c3,'B080-p45-08.png':internal(),'B080-p45-09.png':internal()})
# Appendix D keeps all six algebra chains, including its local signs.
cm=r'\cos\theta_m';c1=r'\cos\theta_1';c2a=r'\cos\theta_2';sm=r'\sin\theta_m';s1=r'\sin\theta_1';s2=r'\sin\theta_2';nm='n_m';n1='n_1';n2='n_2'
denp=W(n1+c2a+'+'+n2+c1);dens=W(n1+c1+'+'+n2+c2a)
def proof(direction,a):
 s='s' if a=='y' else 'p';sg='-' if direction==1 else '+';idx='m1' if direction==1 else 'm2'
 d='1-'+r('m1','',s)+r('m2','',s);p='P_'+a
 lm='L^-_{m/m,'+a+'}';lp='L^+_{m/m,'+a+'}'
 term1=F('1',d) if direction==1 else F(r('m1','',s),d)
 term2=F(r('m2','',s),d) if direction==1 else F('1',d)
 left='E^{'+sg+r'}_{\mathrm{SF},'+s+'}'+(r'(\text{来自 }P_'+a+')' if a!='y' else '')
 lines=[left+r'&=\Bigl['+lm+p+term1+('-' if a=='z' and direction==1 else '+')+lp+p+term2+r'\Bigr]'+t(idx,'',s)]
 if s=='s':
  big=F(W(n1+c1+'+'+nm+cm)+W(n2+c2a+'+'+nm+cm),'2'+nm+cm+dens)
  lines += [r'&='+F(p,'2'+nm+cm)+big+F('2'+nm+cm,W(n2+c2a+'+'+nm+cm)),r'&\quad\times'+F('2'+nm+cm,W(n1+c1+'+'+nm+cm)),r'&='+F(p,dens)+'=L^{'+sg+'}_{1/2,y}'+p]
 else:
  big=F(W(n1+cm+'+'+nm+c1)+W(n2+cm+'+'+nm+c2a),'2'+nm+cm+denp)
  pref=F(('-' if a=='z' and direction==2 else '')+(cm if a=='x' else sm),'2'+nm+cm)
  f1=F('2'+nm+(c1 if a=='x' and direction==2 else cm),W(n1+cm+'+'+nm+c1))
  f2=F('2'+(n2 if a=='z' and direction==1 else nm)+(c2a if a=='x' and direction==1 else cm),W(n2+cm+'+'+nm+c2a))
  lines += [r'&='+pref+p+big+f1,r'&\quad\times'+f2]
  if a=='x':lines.append(r'&='+F(c2a if direction==1 else c1,denp)+p+'=L^{'+sg+'}_{1/2,x}'+p)
  else:
   nn=n2 if direction==1 else n1;sn=s2 if direction==1 else s1;minus='' if direction==1 else '-'
   lines.append(r'&='+F(minus+'('+nn+'/'+nm+')'+sm,denp)+p+'='+F(minus+'('+nn+'/'+nm+')^2'+sn,denp)+p+'=L^{'+sg+'}_{1/2,z}'+p)
 return math(al(*lines))
job('B114','附录D两侧三种极化分量的完整推导',{'B081-p45-01.png':proof(1,'y'),'B081-p45-02.png':proof(1,'x'),'B081-p46-03.png':'<!-- 介质1侧Px推导跨页续式已并入前式。 -->','B081-p46-04.png':proof(1,'z'),'B081-p46-05.png':proof(2,'y'),'B081-p46-06.png':proof(2,'x'),'B081-p47-07.png':proof(2,'z')})
apply()

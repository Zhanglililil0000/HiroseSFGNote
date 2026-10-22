from 收尾光场格式 import *
km=r'k_{m,\mathrm{SF}}';cm=co('m');hm='h_m';ep=X('2i'+km+hm+'/'+cm);roundp=X('i'+km+'2h_m/'+cm)
lm=L('1/1','t','a');lp=L('1/1','t','a','+')
initial=math(al(
 r'E^-_{1t}(0^-)&=E^-_{1t}(z=0^-,n=0)+r_{1m}E^+_{1t}(z=0^-,n=0)',
 r'&\quad+t_{1m}t_{m1}r_{m2}'+X('i'+km+'2h_m/'+cm),
 r'&\qquad\times\sum_{n=1}^{\infty}(r_{m2}r_{m1})^{n-1}'+X('i'+km+'2nh_m/'+cm)+r'^{n-1}E^+_1(z=0^-,n)',
 '&='+W(lm+'+r_{1m}'+lp)+r'P_a(0^-,n=0)',
 r'&\quad+t_{1m}t_{m1}r_{m2}'+ep+lp+r'P_a(0^-,n)',
 r'&\qquad\times\sum_{n=1}^{\infty}'+W('r_{m2}r_{m1}'+roundp)+'^{n-1}'))+'\n$t=s$或$p$，$a=x,y,z$；以上各幂次按底本照录。\n'
eq12=math(al(r'E^-_{1t}(0^-)&=P_a(0^-,n=0)\Bigl['+W(lm+'+r_{1m}'+lp),r'&\quad+t_{m1}r_{m2}e^{2i\beta_mh_m}t_{1m}'+lp+F('1',r'1+r_{1m}r_{m2}e^{2i\beta_mh_m}')+r'\Bigr]'),'5.12')
rels=[]
for s,a in [('p','x'),('s','y'),('p','z')]:
    rels.append(math(L('1/1',s,a)+'+'+r('1m','',s)+L('1/1',s,a,'+')+'='+L('1/m',s,a)))
    factor=F(r'\cos\theta_1',r'\cos\theta_m') if a=='x' else ('1' if a=='y' else '-'+F('n_1','n_m'))
    rels.append(math(t('1m','',s)+L('1/1',s,a,'+')+'='+('' if factor=='1' else factor)+L('1/m',s,a)))
rel4=math(al(r'r_{1m,p}+t_{m1,p}'+W(F(r'\cos\theta_1',r'\cos\theta_m'))+'&=1,',r'r_{1m,s}+t_{m1,s}&=1,',r'r_{1m,p}-t_{m1,p}(n_m/n_1)&=-1.'))
eq13=field_expr(r'E_{1p}(0^-)','sparse',sr('p'),'5.13a',True)+field_expr(r'E_{1s}(0^-)','sparse',sr('s'),'5.13b',True)
job('B096','5.2a稀疏表面源反射场全部推导',{'B071-p13-01.png':initial,'B071-p13-02.png':eq12,'B071-p14-03.png':'\n'.join(rels),'B071-p14-04.png':rel4,'B071-p14-05.png':eq13})
apply()

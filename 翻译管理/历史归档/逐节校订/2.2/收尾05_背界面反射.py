from 收尾光场格式 import *
eta=X(r'2ih_mk_m/\cos\theta_m');half=X(r'ih_mk_m/\cos\theta_m');Q=r'e^{2i\beta_mh_m}';qh=r'e^{i\beta_mh_m}'
pm=r'P(h_m^+,n=0)';pi=r'P(h_m^-,n=0)'
rels='\n'.join(math(t('2m','',s)+L('2/2',s,a)+'='+L('m/2',s,a)) for s,a in [('p','x'),('s','y'),('p','z')])
pathout=math(al(r'E^-_1(0^-)&=t_{2m,\mathrm{SF}}t_{m1,\mathrm{SF}}\sum_{n=0-\infty}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^n',r'&\quad\times\exp[ik_{m,\mathrm{SF}}(2n+1)h_m/\cos\theta_{m,\mathrm{SF}}]E^-_2(z=h_m^+)',r'&=t_{2m,\mathrm{SF}}t_{m1,\mathrm{SF}}\exp(ik_{m,\mathrm{SF}}h_m/\cos\theta_{m,\mathrm{SF}})',r'&\quad\times\sum_{n=0-\infty}[r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}}\exp(ik_{m,\mathrm{SF}}2h_m/\cos\theta_{m,\mathrm{SF}})]^nL^-_{2/2}P(h_m^+,n)'))
phaseout=rels+math(r'P_\alpha(h_m^+,n)=P_\alpha(h_m^+,n=0)'+X(r'i(2n+1)h_m\tan\theta_{m,\mathrm{SF}}(-k_{m,\mathrm{ir}}\sin\theta_{m,\mathrm{ir}}-k_{m,\mathrm{vis}}\sin\theta_{m,\mathrm{vis}})'))
outclosed=math(r'E^-_1(0^-)='+F(r't_{2m}t_{m1}'+qh,'1+r_{1m}r_{m2}2'+Q)+r'L^-_{2/2}'+pm)
def rout(a,kind):
    d= ('1+'+r('1m','',a)+r('m2','',a)+'2'+q(SF)) if kind=='backout' else (db(SF,a) if kind=='backfilm' else dd(SF,a))
    num=t('m1',SF,a)+phase(SF,'1')
    if kind=='backfilm':num+=W('1+'+r("mm''",SF,a)+r("m''2",SF,a))
    p=F(num,d)
    return p+(W(L('2/m','p','x')+chi('x')+'+'+L('2/m','p','z')+chi('z')) if a=='p' else L('2/m','s','y')+chi('y'))
eq16=field_expr(r'E^-_{1p}(0^-)','backout',rout('p','backout'),'5.16a',True)+field_expr(r'E^-_{1s}(0^-)','backout',rout('s','backout'),'5.16b',True)
# The printed 5.16b SF numerator lacks i; retain it locally rather than changing the shared phase function.
eq16=eq16.replace(t('m1',SF,'s')+phase(SF,'1'),t('m1',SF,'s')+r'e^{\beta_{m,\mathrm{SF}}h_m}')
br=r'r_{m1}r_{mm\prime\prime}+r_{m1}t_{mm\prime\prime}\sum_n(r_{m\prime\prime2}r_{m\prime\prime m})^nr_{m\prime\prime2}t_{m\prime\prime m}'
h=r'(1+r_{mm\prime\prime}r_{m\prime\prime2})'
c=r'r_{m1}(r_{mm\prime\prime}+r_{m\prime\prime2})'
pathsfilm=math(al(r'n=0:&\quad t_{m1}'+half,r'n=1:&\quad ['+br+']'+eta+r't_{m1}'+half,r'n=k:&\quad \{['+br+']'+eta+r'\}^kt_{m1}'+half,r'&=t_{m1}'+half+r'r_{m1}\left[r_{mm\prime\prime}+'+F(r't_{mm\prime\prime}t_{m\prime\prime m}r_{m\prime\prime2}',h)+r'\right]^k'+X(r'2ikh_mk_m/\cos\theta_m'),r'&=t_{m1}'+half+r'r_{m1}\left['+F(r'r_{mm\prime\prime}+r_{mm\prime\prime}^2r_{m\prime\prime2}+(1-r_{mm\prime\prime}^2)r_{m\prime\prime2}',h)+r'\right]^k'+X(r'2ikh_mk_m/\cos\theta_m'),r'&=t_{m1}'+half+r'r_{m1}\left['+F(c+eta,h)+r'\right]^k'))
filmseries=math(r'E^-_1(0^-)=L^-_{2/m}t_{m1}'+half+r'\sum_{n=0}\left['+F(c+eta,h)+r'\right]^nP(h_m^+,n)')
filmclosed=math(al(r'E^-_1(0^-)&=L^-_{2/m}t_{m1}e^{\beta_mh_m}\left['+F('1','1+'+F(r'r_{1m}(r_{mm\prime\prime}+r_{m\prime\prime2})'+Q,h))+r'\right]'+pm,r'&=L^-_{2/m}t_{m1}'+qh+r'\left['+F(h,h+r'+r_{1m}(r_{mm\prime\prime}+r_{m\prime\prime2})'+Q)+r'\right]'+pm))
eq17=field_expr(r'E^-_{1p}(0^-)','backfilm',rout('p','backfilm'),'5.17a')+field_expr(r'E^-_{1s}(0^-)','backfilm',rout('s','backfilm'),'5.17b')
# The vis exponent and ir denominator of 5.17b differ from 5.17a in the source.
at=eq17.index(r'\tag{5.17a}')+len(r'\tag{5.17a}')
eq17=eq17[:at]+eq17[at:].replace(phase(VIS,'1'),r'e^{\beta_{m,\mathrm{vis}}h_m}').replace(W(r("mm''",IR,GA)+'+'+r("m''2",IR,GA)),W(r("mm''",IR,GA)+'-'+r("m''2",IR,GA)))
pathin=math(al(r'E^-_1(0^-)&=t_{m1,\mathrm{SF}}(1+r_{m2})\sum_{n=0-\infty}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^n',r'&\quad\times\exp[ik_{m,\mathrm{SF}}(2n+1)h_m/\cos\theta_{m,\mathrm{SF}}]E^-_m(z=h_m^-,n)'))
closedin=math(al(r'E^-_1(0^-)&=t_{m1}'+qh+r'\left[\sum_{n=0}(r_{m2}r_{m1}'+Q+r')^n\right](L^-_{m/m}+r_{m2}L^+_{m/m})'+pi,r'&='+F(r't_{m1}e^{\beta_mh_m}','1+r_{1m}r_{m2}'+Q)+r'(L^-_{m/m}+r_{m2}L^-_{m/m})'+pi))
lmrels=[]
for s,a in [('p','x'),('s','y'),('p','z')]:
    left=L('m/m',s,a)+'+'+r('m2','',s)+L('m/m',s,a,'+')
    base=F((r'\cos\theta_m' if a=='x' else r'\sin\theta_m' if a=='z' else '1'),r'2n_m\cos\theta_m')
    num=(r'2n_m\cos\theta_2' if a=='x' else r'2n_2\cos\theta_m' if a=='z' else r'2n_m\cos\theta_m')
    den=(r'n_2\cos\theta_m+n_m\cos\theta_2' if s=='p' else r'n_2\cos\theta_2+n_m\cos\theta_m')
    lmrels.append(math(left+'='+base+F(num,den)+'='+L('2/m',s,a)))
eq18=field_expr(r'E^-_{1p}(0^-)','backin',rout('p','backin'),'5.18a',True)+field_expr(r'E^-_{1s}(0^-)','backin',rout('s','backin'),'5.18b',True)
note='\n> **译校注（Q067，保留原式）：** 式（5.16）前的简式及（5.16a、b）的和频分母含独立因子2；（5.16b）、背面膜闭式首行、（5.17b）的可见光相位及膜内侧闭式第二行，有未印 $i$ 的指数。（5.17b）红外分母括号内用减号；背面膜路径化简保留额外 $r_{m1}$，膜内侧闭式第二行两项均为 $L^-$。以上按图照录，候选一致化均未采用。\n'
job('B099','背界面各源点的反射场与5.16至5.18',{'B072-p18-05.png':pathout,'B072-p18-06.png':phaseout,'B072-p18-07.png':outclosed+eq16,'B072-p18-08.png':pathsfilm,'B072-p19-09.png':filmseries,'B072-p19-10.png':filmclosed,'B072-p19-11.png':eq17,'B072-p19-12.png':pathin,'B072-p19-13.png':closedin,'B072-p20-14.png':'\n'.join(lmrels)+note,'B072-p20-15.png':eq18})
apply()

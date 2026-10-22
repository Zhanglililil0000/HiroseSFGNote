from 收尾光场格式 import *
S=r'\sum_{n=0}^{\infty}(r_{m\prime1}r_{m\prime m})^n'
H=r'(1+r_{1m\prime}r_{m\prime m})'
T=r'r_{m2}t_{mm\prime}\left['+S+r'\right]t_{m\prime1}'
R=r'\left[r_{m2}r_{mm\prime}+r_{m2}t_{mm\prime}\left['+S+r'\right]r_{m\prime1}t_{m\prime m}\right]'
eta=X(r'2ih_mk_m/\cos\theta_m');Q=r'e^{2i\beta_mh_m}'
A=F(r'-r_{m2}(r_{1m\prime}+r_{m\prime m})',H)
B=F(r'r_{m2}t_{mm\prime}t_{m\prime1}',H)
ep=lambda k:r'E^+(0,n='+k+')'
paths=math(al(r'n=0:&\quad E(0),',r'n=1:&\quad '+T+ep('1'),r'n=2\text{，(a)}:&\quad r_{m2}r_{mm\prime}'+T+ep('2'),r'\text{(b)}:&\quad r_{m2}t_{mm\prime}\left['+S+r'\right]r_{m\prime1}t_{m\prime m}'+T+ep('2'),r'\text{合计}:&\quad '+R+T+ep('2'),r'n=k\text{，(a)}:&\quad (r_{m2}r_{mm\prime})^k'+T+ep('k'),r'\text{(b)}:&\quad (k-1)(r_{m2}r_{mm\prime})^{k-1}\left['+S+r'\right]r_{m\prime1}t_{m\prime m}r_{m2}t_{mm\prime}'))
cont=math(al(r'&\qquad\times\left['+S+r'\right]t_{m\prime1}'+ep('k'),r'&{}_kC_h(r_{m2}r_{mm\prime})^{k-h}\left\{\left['+S+r'\right]r_{m\prime1}t_{m\prime m}\right\}^h'+T+ep('k'),r'&{}_kC_h=\frac{k!}{h!(k-h)!}.'))
pathsum=math(al('&'+R+'^{k-1}',r'&\quad\times'+X(r'2ih_mk_m(k-1)/\cos\theta_m')+T+eta+ep('k'),r'&=\left[\left(r_{m2}r_{mm\prime}+'+F(r'r_{m2}t_{mm\prime}t_{m\prime m}r_{m\prime1}',H)+r'\right)'+eta+r'\right]^{k-1}'+B+eta,r'&=\left['+A+eta+r'\right]^{k-1}'+B+eta))
identity=math(al(r'&r_{m2}r_{mm\prime}+'+F(r'r_{m2}t_{mm\prime}t_{m\prime m}r_{m\prime1}',H),r'&=r_{m2}'+F(r'r_{mm\prime}+r_{mm\prime}r_{m\prime m}r_{1m\prime}+r_{m2}t_{mm\prime}t_{m\prime m}r_{m\prime1}',H),r'&='+F(r'r_{m2}(r_{mm\prime}+r_{m\prime1})',H),r'&='+A))
net=math(al(r'E^-_1(0^-)&=L^-_{1/m}P(0,n=0)',r'&\quad+L^+_{1/m}\sum_{k=1}P(0,n=k)\left['+A+eta+r'\right]^{k-1}'+B+eta))
phaseblock=math(al(r'P_\alpha(0,n=k)&='+X(r'-2ikh_m\tan\theta_{m,\mathrm{SF}}(k_{m,\mathrm{vis}}\sin\theta_{m,\mathrm{vis}}+k_{m,\mathrm{ir}}\sin\theta_{m,\mathrm{ir}})')+r'P_\alpha(0,n=0)',r'k_{m,\mathrm{SF}}\sin\theta_{m,\mathrm{SF}}&+k_{m,\mathrm{vis}}\sin\theta_{m,\mathrm{vis}}+k_{m,\mathrm{ir}}\sin\theta_{m,\mathrm{ir}}=0'))+math(al(r'E^-_1(0^-)&=\left\{L^-_{1/m}+L^+_{1/m}'+B+Q,r'&\quad\times\sum_{n=0}\left['+A+Q+r'\right]^n\right\}P(0,n=0)'))
den=H+r'+r_{m2}(r_{1m\prime}+r_{m\prime m})'+Q
series=math(r'\sum_{n=0}\left['+A+Q+r'\right]^n='+F(H,den))
closed=math(al(r'E^-_1(0^-)&='+F(H+r'L^-_{1/m}+\left[(r_{1m\prime}+r_{m\prime m})L^-_{1/m}+t_{mm\prime}t_{m\prime1}L^+_{1/m}\right]r_{m2}'+Q,den)+r'P(0,n=0)'))
np=r'n_{m\prime}';cp=r'\cos\theta_{m\prime}';n1='n_1';c1=r'\cos\theta_1';nm='n_m';cm=r'\cos\theta_m'
den_s=W(n1+c1+'+'+np+cp)+W(np+cp+'+'+nm+cm)
den_p=W(n1+cp+'+'+np+c1)+W(np+cm+'+'+nm+cp)
rels=[]
for a,d,v in [('s',den_s,n1+c1),('p',den_p,n1+cm)]:
    u=nm+(cm if a=='s' else c1)
    rels.append(math('1+'+r("1m'",'',a)+r("m'm",'',a)+'='+F('2'+np+cp+W(v+'+'+u),d)))
    rels.append(math(r("1m'",'',a)+'+'+r("m'm",'',a)+'='+F('2'+np+cp+W(v+'-'+u),d)))
    rels.append(math(t("1m'",'',a)+t("m'm",'',a)+'='+F('4'+np+cp+nm+cm,d)))
for s,a in [('p','x'),('s','y'),('p','z')]:
    rels.append(math(al(W(r("1m'",'',s)+'+'+r("m'm",'',s))+L('1/m',s,a)+r'&+'+t("mm'",'',s)+t("m'1",'',s)+L('1/m',s,a,'+'),r'&='+('-' if a=='z' else '')+W('1+'+r("1m'",'',s)+r("m'm",'',s))+L('1/m',s,a))))
compact=math(r'E^-_1(0^-)='+F(H+r'(1\pm r_{m2}'+Q+r')L^-_{1/m}',den)+r'P(0,n=0)')
def out(a):
    h=W('1+'+r("1m'",SF,a)+r("m'm",SF,a))
    d=df(SF,a)
    if a=='p':return F(h+W(W('1+'+r('m2',SF,a)+q(SF))+chi('x')+L('1/m','p','x')+'+'+W('1-'+r('m2',SF,a)+q(SF))+chi('z')+L('1/m','p','z')),d)
    return F(h+W('1+'+r('m2',SF,a)+q(SF)),d)+chi('y')+L('1/m','s','y')
final=field_expr(r'E^-_{1p}(0^-)','frontfilm',out('p'),'5.14a')+field_expr(r'E^-_{1s}(0^-)','frontfilm',out('s'),'5.14b')
note='\n> **译校注（Q065，保留原式）：** 上述路径总和的后两行未再写首行的 $E^+(0,n=k)$；紧随的恒等式在分子内额外出现 $r_{m2}$。此处逐项照录，尚未据推导补乘或删因子；组合数与路径幂次的问题另见Q048。\n'
job('B097','完整表面膜的路径枚举与反射场推导',{'B071-p14-06.png':paths,'B071-p15-07.png':cont,'B071-p15-08.png':pathsum,'B071-p15-09.png':identity+note,'B071-p15-10.png':net,'B071-p15-11.png':phaseblock,'B071-p15-12.png':series,'B071-p15-13.png':closed,'B071-p15-14.png':rels[0],'B071-p16-15.png':'\n'.join(rels[1:]),'B071-p16-16.png':compact,'B071-p16-17.png':final})
apply()

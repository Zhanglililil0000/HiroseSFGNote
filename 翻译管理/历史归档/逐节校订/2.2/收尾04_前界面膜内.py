from 收尾光场格式 import *
eta=r'e^{2ih_mk_m/\cos\theta_m}';Q=r'e^{2i\beta_mh_m}'
lm=r'L^-_{m/m}';lp=r'L^+_{m/m}';pm=r'P(0^+,n=0)'
paths=math(al(r'E^-_1(0^-)&=t_{m1,\mathrm{SF}}E^-_1(z=0^+,n=0)',r'&\quad+t_{m1,\mathrm{SF}}\sum_{n=1-\infty}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^{n-1}',r'&\qquad\times\exp[ik_{m,\mathrm{SF}}2nh_m/\cos\theta_{m,\mathrm{SF}}]r_{m2,\mathrm{SF}}',r'&\qquad\times[E^+_m(z=0^+,n)+r_{m1}E^-_m(z=0^+,n)]',r'&=t_{m1}\Bigl\{\sum_{n=0}(r_{m2}r_{m1}'+eta+r')^nE^-(0^+,n)',r'&\qquad+r_{m2}'+eta+r'\sum_{n=1}(r_{m2}r_{m1}'+eta+r')^{n-1}E^+(0^+,n)\Bigr\}',r'&=t_{m1}\Bigl['+lm+pm+r'+r_{m2}'+eta+'('+lp+'+r_{m1}'+lm+')',r'&\qquad\times\sum_{n=1}(r_{m2}r_{m1}'+eta+r')^{n-1}P(0^+,n)\Bigr]'))
closed=math(al(r'E^-_1(0^-)&=t_{m1}\Bigl['+lm+r'+r_{m2}'+Q+'('+lp+'+r_{m1}'+lm+')'+pm,r'&\qquad\times\sum_{n=1}(r_{m2}r_{m1}'+Q+r')^{n-1}',r'&=t_{m1}'+pm+F(lm+'+r_{m2}'+Q+lp,'1+r_{1m}r_{m2}'+Q)))
rels=[]
for s,a in [('p','x'),('s','y'),('p','z')]:
    for sg in ['-','+']:
        rels.append(math(t('m1','',s)+L('m/m',s,a,sg)+'='+('-' if a=='z' and sg=='+' else '')+L('1/m',s,a)))
compact=math(r'E^-_1(0^-)='+pm+F(r'(1+r_{m2})'+Q+r'L^-_{1/m}','1+r_{1m}r_{m2}'+Q))
note='\n> **译校注（Q066，保留原式）：** 本页首行求和下标写作 $n=1-\\infty$，前一净场式的方括号未闭合；末尾简式分子印为 $(1+r_{m2})e^{2i\\beta_mh_m}$，下方却说明上下号。转写保留原有乘法关系，未改成候选的 $1\\pm r_{m2}e^{2i\\beta_mh_m}$。为显示排版，前式开方括号采用定尺寸符号，不补原式闭括号。\n'
final=field_expr(r'E^-_{1p}(0^-)','frontin',sr('p'),'5.15a',True)+field_expr(r'E^-_{1s}(0^-)','frontin',sr('s'),'5.15b',True)
job('B098','前界面薄膜侧的反射场推导与5.15',{'B072-p17-01.png':paths,'B072-p17-02.png':closed,'B072-p17-03.png':'\n'.join(rels)+compact+note,'B072-p17-04.png':final})
apply()

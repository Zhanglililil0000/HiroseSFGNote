from 收尾公式工具 import *
VIS=r'\mathrm{vis}';IR=r'\mathrm{ir}';SF=r'\mathrm{SF}'
BE=r'\beta';GA=r'\gamma'
SUM=r'\sum_{\beta,\gamma}E^0_{\mathrm{vis},\beta}E^0_{\mathrm{ir},\gamma}'
def chi(a):return r'\chi_{'+a+r'\beta\gamma}'
def q(w):return phase(w)
def dd(w,a):return W('1+'+r('1m',w,a)+r('m2',w,a)+q(w))
def df(w,a):return '1+'+r("1m'",w,a)+r("m'm",w,a)+'+'+W(r("m'm",w,a)+'+'+r("1m'",w,a))+r('m2',w,a)+q(w)
def db(w,a):return W('1+'+r("mm''",w,a)+r("m''2",w,a))+'+'+r('1m',w,a)+W(r("mm''",w,a)+'+'+r("m''2",w,a))+q(w)
def excitation(w,a,kind):
    if kind=='sparse':return (W('1+'+r('1m',w,a))+W('1+'+r('m2',w,a)+q(w)),dd(w,a))
    if kind=='frontfilm':return (t("1m'",w,a)+W('1+'+r("m'm",w,a))+W('1+'+r('m2',w,a)+q(w)),df(w,a))
    if kind=='frontin':return (t('1m',w,a)+W('1+'+r('m2',w,a)+q(w)),dd(w,a))
    if kind=='backout':return (t('1m',w,a)+t('m2',w,a)+phase(w,'1'),dd(w,a))
    if kind=='backfilm':return (t('1m',w,a)+t("mm''",w,a)+W('1+'+r("m''2",w,a))+phase(w,'1'),db(w,a))
    if kind=='backin':return (t('1m',w,a)+W('1+'+r('m2',w,a))+phase(w,'1'),dd(w,a))
    raise ValueError(kind)
def field_expr(lhs,kind,output,tag,combined=False):
    av,dv=excitation(VIS,BE,kind);ai,di=excitation(IR,GA,kind)
    lines=[lhs+'&='+SUM]
    if combined:lines+=[r'&\quad\times'+F(av+ai,dv+di)]
    else:lines+=[r'&\quad\times'+F(av,dv),r'&\quad\times'+F(ai,di)]
    lines+=[r'&\quad\times'+output]
    return math(al(*lines),tag)
def sr(a,sg='+',ij='1/m'):
    if a=='p':return F(W('1+'+r('m2',SF,'p')+q(SF))+L(ij,'p','x','-')+chi('x')+'+'+W('1-'+r('m2',SF,'p')+q(SF))+L(ij,'p','z','-')+chi('z'),dd(SF,'p'))
    return F(W('1+'+r('m2',SF,'s')+q(SF)),dd(SF,'s'))+L(ij,'s','y','-')+chi('y')

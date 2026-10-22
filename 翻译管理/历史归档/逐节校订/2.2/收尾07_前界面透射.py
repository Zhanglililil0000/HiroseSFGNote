from 收尾光场格式 import *
Q=r'e^{2i\beta_mh_m}';qh=r'e^{i\beta_mh_m}';eta=X(r'2ih_mk_m/\cos\theta_m');half=X(r'ih_mk_m/\cos\theta_m')
pos=r'h_m^+';lhs=r'E^+_2(h_m^+)';pn=r'P(0^-,n=0)'
prop=r'\exp[ik_{m,\mathrm{SF}}(2n+1)h_m/\cos\theta_{m,\mathrm{SF}}]'
sum0=r'\sum_{n=0}^{\infty}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^n'
path=math(al(lhs+r'&=t_{1m,\mathrm{SF}}t_{m2,\mathrm{SF}}'+sum0,r'&\quad\times'+prop+r'E^+_m(z=0^-,n)'))
closed=math(al(lhs+r'&=t_{1m,\mathrm{SF}}t_{m2,\mathrm{SF}}'+sum0,r'&\quad\times'+prop+r'L^+_{1/1}P^+(0^-,n=0)',r'&='+F(t('1m',SF)+t('m2',SF)+phase(SF,'1'),dd(SF,''))+r'L^+_{1/1}'+pn))
rels='\n'.join(math(t('1m','',s)+L('1/1',s,a,'+')+'='+L('m/1',s,a,'+')) for s,a in [('p','x'),('s','y'),('p','z')])+"\n这里取 $n_{m'}=n_1$。\n"
def transout(s,kind):
 if kind=='sparse':num=t('1m',SF,s)+t('m2',SF,s)+phase(SF,'1');den=dd(SF,s);ij='m/1'
 elif kind=='frontfilm':
  num=t('m2',SF,s)+W('1+'+r("1m'",SF,s)+r("m'm",SF,s))+phase(SF,'1')
  den='1+'+r("1m'",SF,s)+r("m'm",SF,s)+'+'+r('m2',SF,s)+W(r("mm'",SF,s)+'+'+r("m'1",SF,s))+q(SF);ij='1/m'
 else:num=t('m2',SF,s)+phase(SF,'1');den=dd(SF,s);ij='1/m'
 return F(num,den)+(W(L(ij,s,'x','+')+chi('x')+'+'+L(ij,s,'z','+')+chi('z')) if s=='p' else L(ij,s,'y','+')+chi('y'))
eq20=field_expr(r'E^+_{2p}(h_m^+)','sparse',transout('p','sparse'),'5.20a',True)+field_expr(r'E^+_{2s}(h_m^+)','sparse',transout('s','sparse'),'5.20b',True)
br=r'r_{m2}r_{mm\prime}+r_{m2}t_{mm\prime}r_{m\prime1}\left[\sum_n(r_{m\prime1}r_{m\prime m})^nt_{m\prime m}\right]'
H=r'(1+r_{1m\prime}r_{m\prime m})';C=r'r_{m2}(r_{mm\prime}+r_{m\prime1})'
pathsfilm=math(al(r'n=0:&\quad t_{m2}'+half,r'n=1:&\quad t_{m2}'+half+r'\{'+br+r'\}'+eta,r'n=k:&\quad t_{m2}'+half+r'\{'+br+r'\}^k'+X(r'2ikh_mk_m/\cos\theta_m'),r'&=t_{m2}'+half+r'\left['+F(C,H)+eta+r'\right]^k'))
closedfilm=math(al(lhs+r'&=t_{m2}'+qh+r'\sum_{k=0}\left['+F(C,H)+Q+r'\right]^kL^+_{1/m}P(0,n=0)',r'&=t_{m2}'+qh+F('1','1+'+F(C,H)+Q)+r'L^+_{1/m}P(0,n=0)',r'&='+F('t_{m2}'+H+qh,H+'+'+C+Q)+r'L^+_{1/m}P(0,n=0)'))
eq21=field_expr(r'E^+_{2p}(h_m^+)','frontfilm',transout('p','frontfilm'),'5.21a')
# 5.21b prints a back-film vis factor, followed by the front-film ir factor.
av,dv=excitation(VIS,BE,'backfilm');ai,di=excitation(IR,GA,'frontfilm')
eq21+=math(al(r'E_{2s}(h_m^+)&='+SUM,r'&\quad\times'+F(av,dv),r'&\quad\times'+F(ai,di),r'&\quad\times'+transout('s','frontfilm')),'5.21b')
pathsinner=math(al(lhs+r'&=t_{m2,\mathrm{SF}}'+sum0,r'&\quad\times'+prop+r'[E^+_m(z=0^+,n)+r_{m1}E^-_m(z=0^+,n)]'))
closedinner=math(al(lhs+r'&=t_{m2,\mathrm{SF}}'+sum0+prop+r'[L^+_{m/m}+r_{m1}L^-_{m/m}]P^+(0^-,n=0)',r'&='+F(t('m2',SF)+phase(SF,'1'),dd(SF,''))+r'(L^+_{m/m}+r_{m1}L^-_{m/m})'+pn,r'&='+F(t('m2',SF)+phase(SF,'1'),dd(SF,''))+r'L^+_{1/m}'+pn))
relsin='\n'.join(math(L('m/m',s,a,'+')+'+'+r('m1','',s)+L('m/m',s,a)+'='+L('1/m',s,a,'+')) for s,a in [('p','x'),('s','y'),('p','z')])
eq22=field_expr(r'E^+_{2p}(h_m^+)','frontin',transout('p','frontin'),'5.22a',True)+field_expr(r'E^+_{2s}(h_m^+)','frontin',transout('s','frontin'),'5.22b',True)
note='\n> **译校注（Q069，保留原式）：** 式（5.20）的和频因子保留 $t_{1m}t_{m2}$ 及 $L^+_{m/1}$；式（5.21b）的可见光因子却使用背面膜 $m^{\\prime\\prime}$ 的形式，红外光因子仍用前面膜 $m^\\prime$。式（5.22）前的极化位置沿用 $0^-$。不按分支主题替换这些记号；斜体 $i$ 均结合文字层核对。\n'
job('B103','前界面外侧及完整表面膜的透射场',{'B074-p24-01.png':path,'B074-p25-02.png':closed,'B074-p25-03.png':rels,'B074-p25-04.png':eq20,'B074-p25-05.png':pathsfilm,'B074-p25-06.png':closedfilm,'B074-p26-07.png':eq21+note})
job('B104','前界面薄膜侧透射场全部推导',{'B074-p26-08.png':pathsinner,'B074-p26-09.png':closedinner,'B074-p26-10.png':relsin,'B074-p27-11.png':eq22})
apply()

from 收尾光场格式 import *
Q=r'e^{2i\beta_{m,\mathrm{SF}}h_m}';qh=r'e^{i\beta_mh_m}';eta=X(r'2ih_mk_m/\cos\theta_m')
sum0=r'\sum_{n=0}^{\infty}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^n'
prop=r'\exp[ik_{m,\mathrm{SF}}2(n+1)h_m/\cos\theta_{m,\mathrm{SF}}]'
lhs=r'E^+_2(h_m^+)';pout=r'P(h_m^+,n=-1)';pin=r'P(h_m^-,n=-1)';D='1+r_{1m}r_{m2}'+Q
pathout=math(al(lhs+r'&=E^+_2(z=h_m^+,n=-1)+r_{2m,\mathrm{SF}}E^-_2(z=h_m^+,n=-1)',r'&\quad+t_{2m,\mathrm{SF}}\sum_{n=0}^{\infty}r_{m1,\mathrm{SF}}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^n',r'&\qquad\times'+prop+r't_{m2,\mathrm{SF}}E^-_2(z=h_m^+,n)'))
lp=r'L^+_{2/2}';lm=r'L^-_{2/2}'
closedout=math(al(lhs+r'&=('+lp+r'+r_{2m,\mathrm{SF}}'+lm+r')P(z=h_m^+,n=-1)',r'&\quad+t_{2m,\mathrm{SF}}\sum_{n=0}^{\infty}r_{m1,\mathrm{SF}}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^n',r'&\qquad\times'+prop+r't_{m2,\mathrm{SF}}L^-_{2/2}P(z=h_m^+,n=0)',r'&='+pout+r'\Bigl[('+lp+'+r_{2m}'+lm+')+t_{m2}t_{2m}r_{m1}'+Q,r'&\qquad\times\sum_{n=0}(r_{m2}r_{m1}'+Q+r')^n'+lm+r'\Bigr]',r'&='+pout+r'\Bigl['+lp+'+'+lm+W('r_{2m}+'+F('t_{m2}t_{2m}r_{m1}'+Q,D))+r'\Bigr]',r'&='+pout+r'\Bigl['+lp+'+'+lm+W(F(r'r_{2m}+(r_{1m}r_{m2}r_{2m}+(1+r_{m2}r_{2m})(-r_{1m}))'+Q,D))+r'\Bigr]',r'&='+pout+F(lp+'+r_{2m}'+lm+'-r_{1m}(r_{2m}'+lp+'+'+lm+')'+Q,D)))
relsout=[]
for s,a in [('p','x'),('s','y'),('p','z')]:
 relsout.append(math(L('2/2',s,a,'+')+'+'+r('2m','',s)+L('2/2',s,a)+'='+L('2/m',s,a,'+')))
 relsout.append(math(r('2m','',s)+L('2/2',s,a,'+')+'+'+L('2/2',s,a)+'='+('-' if a=='z' else '')+L('2/m',s,a,'+')))
simpleout=math(lhs+'='+pout+F(r'(1\mp r_{1m}'+Q+r')L^+_{2/m}',D))
def backout(s,film=False):
 d=db(SF,s) if film else dd(SF,s)
 a=r('1m',SF,s)+q(SF)
 num=W('1-'+a)+L('2/m',s,'x','+')+chi('x')+'+'+W('1+'+a)+L('2/m',s,'z','+')+chi('z') if s=='p' else W('1-'+a)+L('2/m',s,'y','+')+chi('y')
 if film:num=W('1+'+r("mm''",SF,s)+r("m''2",SF,s))+W(num)
 return F(num,d)
eq23=field_expr(r'E^+_{2p}(h_m^+)','backout',backout('p'),'5.23a',True)+field_expr(r'E^+_{2s}(h_m^+)','backout',backout('s'),'5.23b',True)
pathin=math(al(lhs+r'&=t_{m2,\mathrm{SF}}E^+_2(z=h_m^-,n=-1)',r'&\quad+t_{m2,\mathrm{SF}}'+sum0+prop,r'&\qquad\times r_{m1,\mathrm{SF}}[E^-_m(z=h_m^-,n)+r_{m2,\mathrm{SF}}E^+_m(z=h_m^-,n)]'))
closedin=math(al(lhs+r'&=t_{m2,\mathrm{SF}}L^+_{m/m}P(z=h_m^-,n=-1)',r'&\quad+\sum_{n=0}^{\infty}r_{m1,\mathrm{SF}}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^n'+prop,r'&\qquad\times t_{m2,\mathrm{SF}}[L^+_{m/m}+r_{m2,\mathrm{SF}}L^-_{m/m}]P(z=h_m^-,n=0)',r'&='+pin+r't_{m2}(L^+_{m/m}+r_{m1}'+Q+r'L^-_{m/m})\sum_{n=0}(r_{m2}r_{m1}'+Q+r')^n',r'&='+pout+r'(L^+_{m/m}+r_{m1}'+Q+r'L^-_{m/m})'+F('1',D)))
relsin=[]
for s,a in [('p','x'),('s','y'),('p','z')]:
 for sg in ['+','-']:relsin.append(math(t('m2','',s)+L('m/m',s,a,sg)+'='+('-' if a=='z' and sg=='+' else '')+L('2/m',s,a,'+')))
simplein=math(lhs+'='+pout+r'L^+_{2/m}'+F(r'(\pm1+r_{m1}'+Q+')',D))
def innerout(s):
 rr=r('m1',SF,s)+q(SF)
 num=W('1+'+rr)+L('2/m',s,'x','+')+chi('x')+'+'+W('-1+'+rr)+L('2/m',s,'z','+')+chi('z') if s=='p' else W('1+'+rr)+L('2/m',s,'y','+')+chi('y')
 return F(num,dd(SF,s))
eq24=field_expr(r'E^+_{2p}(h_m^+)','backin',innerout('p'),'5.24a',True)+field_expr(r'E^+_{2s}(h_m^+)','backin',innerout('s'),'5.24b',True)
idx=eq24.index(r'\tag{5.24a}')+len(r'\tag{5.24a}')
eq24=eq24[:idx]+eq24[idx:].replace(SUM,SUM+'e',1)
note='\n> **译校注（Q070，保留原式）：** 薄膜侧透射场的末行从 $h_m^-$ 换成 $h_m^+$，且未再写前行 $t_{m2}$；式（5.24b）两束入射振幅之后有独立的 $e$。背面膜推导最后一个整理分子的结构与前行不直接一致。均按原式保留，不据上下文删补。\n'
job('B105','背界面外侧透射场全部推导与5.23',{'B075-p27-01.png':pathout,'B075-p27-02.png':closedout,'B075-p27-03.png':'\n'.join(relsout)+'\n这里取 $m^{\prime\prime}=2$。\n','B075-p27-04.png':simpleout,'B075-p28-05.png':eq23})
job('B106','背界面薄膜侧透射场与5.24',{'B075-p28-06.png':pathin,'B075-p28-07.png':closedin,'B075-p28-08.png':'\n'.join(relsin)+'\n这里取 $m^{\prime\prime}=m$。\n','B075-p28-09.png':simplein,'B075-p29-10.png':eq24+note})
H=r'(1+r_{mm\prime\prime}r_{m\prime\prime2})';C=r'(r_{mm\prime\prime}+r_{m\prime\prime2})';T=r't_{mm\prime\prime}t_{m\prime\prime2}';eta2=X(r'2ikh_mk_m/\cos\theta_m')
summ=r'\sum_{n=0}(r_{m\prime\prime2}r_{m\prime\prime m})^n'
br=r'\left\{r_{mm\prime\prime}+t_{mm\prime\prime}\left[r_{m\prime\prime2}\sum_{n=0}(r_{m\prime\prime m}r_{m\prime\prime2})^n\right]t_{m\prime\prime m}\right\}'
pathsf=math(al(r'n=-1:&\quad E^+_2(h_m,n=-1)',r'n=0:&\quad E^-(h_m,n=0)'+eta+r'r_{m1}t_{mm\prime\prime}\left['+summ+r'\right]t_{m\prime\prime2}',r'n=1:&\quad E^-(h_m,n=1)'+eta+r'r_{m1}'+br+r'r_{m1}'+eta,r'&\quad\times t_{mm\prime\prime}\left['+summ+r'\right]t_{m\prime\prime2}',r'n=k:&\quad E^-(h_m,n=k)'+eta+r'r_{m1}'+br+r'^kr_{m1}^k'+eta2,r'&\quad\times t_{mm\prime\prime}\left['+summ+r'\right]t_{m\prime\prime2}',r'&=E^-(h_m,n=k)'+eta+r'r_{m1}\left\{\left[r_{mm\prime\prime}+'+F(r't_{mm\prime\prime}t_{m\prime\prime m}r_{m\prime\prime2}',H)+r'\right]r_{m1}\right\}^k'+eta2+F(T,H),r'&=E^-(h_m,n=k)'+eta+r'r_{m1}\left['+F(C,H)+r'r_{m1}\right]^k'+eta2+F(T,H)))
dn=H+r'+r_{1m}'+C+r'e^{2i\beta_mh_m}';Qm=r'e^{2i\beta_mh_m}';po=r'P_\alpha(h_m,n=-1)'
closedf=math(al(r'E^+(h_m^+)&=P(h_m,n=-1)L^+_{2/m}',r'&\quad+'+po+r'L^-_{2/m}'+Qm+r'r_{m1}'+F(T,H)+r'\sum_{n=0}\left['+F(C,H)+r'r_{m1}'+Qm+r'\right]^n',r'&='+po+r'\Bigl\{L^+_{2/m}+L^-_{2/m}'+Qm+r'r_{m1}'+F(T,H)+F(H,dn)+r'\Bigr\}',r'&='+po+r'\Bigl\{L^+_{2/m}+L^-_{2/m}'+Qm+F('r_{m1}'+T,dn)+r'\Bigr\}',r'&='+po+F(H+r'L^+_{2/m}+r_{1m}['+C+r'L^+_{2/m}-'+T+C+r'L^-_{2/m}]'+Qm,dn)))
relsf=[]
nm='n_m';cm=r'\cos\theta_m';np=r'n_{m\prime\prime}';cp=r'\cos\theta_{m\prime\prime}';n2='n_2';c2=r'\cos\theta_2'
for s,d,v,u in [('s',W(nm+cm+'+'+np+cp)+W(np+cp+'+'+n2+c2),nm+cm,n2+c2),('p',W(nm+cp+'+'+np+cm)+W(np+c2+'+'+n2+cp),nm+c2,n2+cm)]:
 relsf.extend([math('1+'+r("mm''",'',s)+r("m''2",'',s)+'='+F('2'+np+cp+W(v+'+'+u),d)),math(r("mm''",'',s)+'+'+r("m''2",'',s)+'='+F('2'+np+cp+W(v+'-'+u),d)),math(t("mm''",'',s)+t("m''2",'',s)+'='+F('4'+np+cp+nm+cm,d))])
for s,a,c in [('p','x',F(c2,cm)),('s','y',''),('p','z','-'+F(n2,nm))]:relsf.append(math(L('2/m',s,a)+'='+c+L('2/m',s,a,'+')))
simplef=math(r'E^+(h_m^+)='+po+F(H+r'(1\mp r_{1m}'+Qm+')',dn)+r'L^+_{2/m}')
eq25=field_expr(r'E_{2p}(h_m^+)','backfilm',backout('p',True),'5.25a')+field_expr(r'E_{2s}(h_m^+)','backfilm',backout('s',True),'5.25b')
job('B107','背面极化薄膜的透射场全部推导与5.25',{'B075-p29-11.png':pathsf,'B075-p29-12.png':closedf,'B075-p30-13.png':'\n'.join(relsf),'B075-p30-14.png':simplef,'B075-p30-15.png':eq25})
apply()

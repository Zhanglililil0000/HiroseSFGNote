from 收尾光场格式 import *
bs=b('SF');bv=b('vis');bi=b('ir');rv=r('m2',VIS,BE);ri=r('m2',IR,GA);r1=r('m1',SF);Q=q(SF);qm=phase(SF,'1')
def ex(a,z='z'):return 'e^{i('+a+')'+z+'}'
def ss(s,v,i):return ('-' if s<0 else '')+bs+('+' if v>0 else '-')+bv+('+' if i>0 else '-')+bi
lm=r'L^-_{m/m}';lp=r'L^+_{m/m}';sum0=r'\sum_{n=0}^{\infty}(r_{m2}r_{m1})^n'
path=math(al(r'E^+_2(h_m^+)&=t_{m2}\Bigl\{E^+_m(B_{-1}(z))\exp[ik_m(h_m-z)/\cos\theta_m]',r'&\quad+'+sum0+r'\Bigl\{r_{m1}\exp[ik_m[(2n+1)h_m+z]/\cos\theta_m]E^-_m(A_n(z))',r'&\qquad+r_{m2}r_{m1}\exp[ik_m[(2n+3)h_m-z]/\cos\theta_m]E^+_m(B_n(z))\Bigr\}\Bigr\}',r'&=t_{m2}L^+_{2/m}\exp[ik_m(h_m-z)/\cos\theta_m]\Bigl\{P(z,B_{n=-1})',r'&\quad+r_{m2}r_{m1}\exp(2ik_mh_m/\cos\theta_m)'+sum0+r'\exp(2ink_mh_m/\cos\theta_m)P(z,B_n)\Bigr\}',r'&\quad+t_{m2}r_{m1}L^-_{2/m}\exp[ik_m(h_m+z)/\cos\theta_m]',r'&\qquad\times'+sum0+r'\exp(2ink_mh_m/\cos\theta_m)P(z,A_n)'))
ph=X(r'-i(2n+1)h_m\tan\theta_{m,\mathrm{SF}}(k_{m,\mathrm{vis}}\sin\theta_{m,\mathrm{vis}}+k_{m,\mathrm{ir}}\sin\theta_{m,\mathrm{ir}})')
phases=math(al(r'P_\alpha(z,B_n)&=P_\alpha(z,B_{n=0})'+ph,r'P_\alpha(z,A_n)&=P_\alpha(z,A_{n=0})'+ph))
reduced=math(al(r'E^+(h_m^+)&=t_{m2}L^+_{m/m}P(z,B_{n=0})e^{ik_m(h_m-z)}',r'&\quad\times\left[1+r_{m2}r_{m1}e^{2ik_mh_m/\cos\theta_m}\sum_{n=0}(r_{m2}r_{m1}e^{2i\beta_mh_m})^n\right]',r'&\quad+t_{m2}r_{m1}L^-_{m/m}P(z,A_{n=0})e^{ik_m(h_m+z)}\sum_{n=0}(r_{m2}r_{m1}e^{2i\beta_mh_m})^n'))
old=(OUT/'B100-本批译文.md').read_text(encoding='utf-8');blocks=re.findall(r'\$\$[\s\S]*?\$\$',old)
polar=[x for x in blocks if r'P_\alpha(z,A_{n=0})&=' in x or r'P_\alpha(z,B_{n=0})&=' in x]
assert len(polar)==2
star=next(x for x in blocks if r'P^*_\alpha\equiv' in x)
def terms(s):
 vals=[]
 for j,(v,i) in enumerate([(1,1),(1,-1),(-1,1),(-1,-1)]):
  c=ri+q(IR) if j==1 else rv+q(VIS) if j==2 else rv+ri+ex('2('+bv+'+'+bi+')','h_m') if j==3 else ''
  vals.append(c+ex(ss(s,v,i)))
 return vals
expanded=[r'E^+(h_m^+)&=P^*\Bigl\{'+t('m2',SF)+lp+qm+r'\left[1+'+r('m2',SF)+r1+Q+r'\sum_{n=0}('+r('m2',SF)+r1+Q+r')^n\right]']
for z in [0,1]:
 if z:expanded.append(r'&\quad+'+t('m2',SF)+r1+lm+r'P(z,A_{n=0})'+qm+r'\sum_{n=0}('+r('m2',SF)+r1+Q+r')^n')
 for j,a in enumerate(terms(-1 if z==0 else 1)):expanded.append(r'&\quad'+(r'\times\Bigl[' if j==0 else '+')+a+(r'\Bigr]' if j==3 else ''))
expanded[-1]+=r'\Bigr\}'
expanded.append(r'&=P^*'+F('1',dd(SF,''))+r'\Bigl\{'+t('m2',SF)+lp+qm)
for z in [0,1]:
 if z:expanded.append(r'&\quad+'+t('m2',SF)+r1+lm+qm)
 for j,a in enumerate(terms(-1 if z==0 else 1)):expanded.append(r'&\quad'+(r'\times\Bigl[' if j==0 else '+')+a+(r'\Bigr]' if j==3 else ''))
expanded[-1]+=r'\Bigr\}'
job('B108','体相透射场的路径、极化与展开',{'B076-p31-01.png':path,'B076-p31-02.png':phases,'B076-p31-03.png':reduced,'B076-p31-04.png':'\n\n'.join(polar),'B076-p32-05.png':'<!-- 零阶B极化跨页续式已并入上式。 -->','B076-p32-06.png':star,'B076-p32-07.png':math(al(*expanded))})
def integral(useL=True,sg=r'\pm'):
 lines=[r'E^+_2(h_m^+)&=\frac{i}{\delta}'+F(t('m2',SF) if useL else r'L^+_{2/m}',dd(SF,''))+r'P^*_\alpha']
 for z,s in enumerate([-1,1]):
  for j,(v,i) in enumerate([(1,1),(1,-1),(-1,1),(-1,-1)]):
   c=ri+q(IR) if j==1 else rv+q(VIS) if j==2 else rv+ri+ex('2('+bv+'+'+bi+')','h_m') if j==3 else ''
   den=ss(1,-v,-i) if z==0 else ss(1,v,i)
   num=ex(ss(s,v,i),'h_m')+'-1' if z==0 else '1-'+ex(ss(s,v,i),'h_m')
   lead=(r'\times\Bigl\{'+(lp if useL else '')+qm+r'\Bigl[' if z==0 else ('+' if useL else sg)+r1+(lm if useL else '')+qm+r'\Bigl[') if j==0 else '+'
   lines.append(r'&\quad'+lead+c+F(num,den)+(r'\Bigr]'+(r'\Bigr\}' if z else '') if j==3 else ''))
 return math(al(*lines))
rel='\n'.join(math(t('m2','',s)+L('m/m',s,a,sg)+'='+('-' if sg=='-' and a=='z' else '')+L('2/m',s,a,'+')) for sg in ['+','-'] for s,a in [('p','x'),('s','y'),('p','z')])
dens=[ss(1,-1,-1),ss(1,-1,1),ss(1,1,-1),ss(1,1,1)]
em=ex(ss(-1,1,1),'h_m');ep=ex(ss(1,1,1),'h_m');ev=q(VIS);ei=q(IR);evplus=ex('2('+bv+'+'+bi+')','h_m')
def numerators(sg,sfpol=''):
 rr=r('m1',SF,sfpol)
 return [(em+'-1',rr+rv+ri+W(evplus+'-'+ep)),(ri+W(em+'-'+ei),rr+rv+W(ev+'-'+ep)),(rv+W(em+'-'+ev),rr+ri+W(ei+'-'+ep)),(rv+ri+W(em+'-'+evplus),rr+W('1-'+ep))]
def grouped():
 lines=[r'E^+_2(h_m^+)&=\frac{i}{\delta}'+F(r'L^+_{2/m}'+qm,dd(SF,''))+r'P^*_\alpha']
 for j,(d,(a,c)) in enumerate(zip(dens,numerators(r'\pm'))):lines.append(r'&\quad'+(r'\times\Bigl\{' if j==0 else '+')+F(a+r'\pm'+c,d)+(r'\Bigr\}' if j==3 else ''))
 return math(al(*lines))
note='\n> **译校注（Q071，保留原式）：** 体相透射推导在 $L_{2/m}$ 与 $L_{m/m}$、$B_{-1}$ 与 $B_0$ 之间切换；代入极化后的场式在 $e^{ik_m(h_m\pm z)}$ 中未写前一式的 $1/\\cos\\theta_m$，完整展开首段还含 $P(z,A_{n=0})$。式（5.26）分组中的各相位是否与前式一致仍待确认，未据积分推导改写。\n'
job('B109','体相透射积分与两种整理形式',{'B076-p32-08.png':integral(),'B076-p33-09.png':'<!-- 积分跨页续式已合并至前式。 -->','B076-p33-10.png':rel,'B076-p33-11.png':integral(False)+grouped()+note})
def eq26(s):
 lines=[r'E^+_{2'+s+r'}(h_m^+)&=\frac{i}{\delta}'+SUM,r'&\quad\times'+F(t('1m',VIS,BE)+t('1m',IR,GA)+qm,dd(SF,s)+dd(VIS,BE)+dd(IR,GA))]
 coords=['x','z'] if s=='p' else ['y']
 for k,a in enumerate(coords):
  lines.append(r'&\quad'+(r'\times\Bigl\{' if s=='p' and k==0 else '+' if k else r'\times')+L('2/m',s,a,'+')+chi(a)+r'\Bigl[')
  for j,(d,(u,v)) in enumerate(zip(dens,numerators('',s))):
   lines.append(r'&\qquad'+('+' if j else '')+F(u+('-' if a=='z' else '+')+v,d))
  lines[-1]+=r'\Bigr]'
 lines[-1]+=(r'\Bigr\}' if s=='p' else '')
 return math(al(*lines),'5.26a' if s=='p' else '5.26b')
job('B110','完整体相p、s偏振透射场5.26',{'B076-p34-12.png':eq26('p'),'B076-p34-13.png':eq26('s')})
apply()

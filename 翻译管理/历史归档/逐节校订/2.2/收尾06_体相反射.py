from 收尾光场格式 import *
bs=b('SF');bv=b('vis');bi=b('ir');rv=r('m2',VIS,BE);ri=r('m2',IR,GA);rs=r('m2',SF)
lm=r'L^-_{m/m}';lp=r'L^+_{m/m}';hm='h_m'
def exp(s,z='z'):return 'e^{i('+s+')'+z+'}'
def sum3(s=1,v=1,i=1):return ('-' if s<0 else '')+bs+('+' if v>0 else '-')+bv+('+' if i>0 else '-')+bi
path=math(al(r'E^-_1(0^-)&=t_{m1,\mathrm{SF}}\sum_{n=0-\infty}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}})^n',r'&\quad\times\Bigl\{\exp[ik_{m,\mathrm{SF}}(2nh_m+z)/\cos\theta_{m,\mathrm{SF}}]E^-_m(A_n(z))',r'&\qquad+r_{m2,\mathrm{SF}}\exp[ik_{m,\mathrm{SF}}(2(n+1)h_m-z)/\cos\theta_{m,\mathrm{SF}}]E^+_m(B_n(z))\Bigr\}'))
phase=X(r'-2inh_m\tan\theta_{m,\mathrm{SF}}(k_{m,\mathrm{vis}}\sin\theta_{m,\mathrm{vis}}+k_{m,\mathrm{ir}}\sin\theta_{m,\mathrm{ir}})')
phases=math(al(r'P_\alpha(z,B_n)&=P_\alpha(z,B_{n=0})'+phase,r'P_\alpha(z,A_n)&=P_\alpha(z,A_{n=0})'+phase))
path2=math(al(r'E^-(0^-)&=\Bigl[t_{m1}L^-_{m/m}e^{ik_mz/\cos\theta_m}P(z,A_{n=0})',r'&\quad+t_{m1}r_{m2}e^{ik_mh_m/\cos\theta_m}L^+_{m/m}e^{-ik_mz/\cos\theta_m}P(z,B_{n=0})\Bigr]',r'&\quad\times\sum_{n=0}(r_{m2}r_{m1}e^{2i\beta_mh_m})^n'))
pref=SUM+F(t('1m',VIS,BE)+t('1m',IR,GA),dd(VIS,BE)+dd(IR,GA))
def polar(which):
    B=which=='B';d=dd(VIS,BE)+dd(IR,GA)
    if B:d=d.replace(q(VIS),'TEMP').replace(q(IR),q(VIS)).replace('TEMP',q(IR))
    lines=[r'P_\alpha(z,'+which+r'_{n=0})&='+SUM+chi(r'\alpha'),r'&\quad\times'+F(t('1m',VIS,BE)+t('1m',IR,GA),d)]
    if B:lines.append(r'&\quad\times'+X(r'-2ih_m\tan\theta_{m,\mathrm{SF}}(k_{m,\mathrm{vis}}\sin\theta_{m,\mathrm{vis}}+k_{m,\mathrm{ir}}\sin\theta_{m,\mathrm{ir}})'))
    for idx,(v,i) in enumerate([(1,1),(1,-1),(-1,1),(-1,-1)]):
        coeff=(ri+q(IR) if idx==1 else rv+q(VIS) if idx==2 else rv+ri+exp('2('+bv+'+'+bi+')',hm) if idx==3 else '')
        angle_v=('+' if B else '-') if v>0 else ('-' if B else '+')
        angle_i=('+' if B else '-') if i>0 else ('-' if B else '+')
        def term(w,sg,sa):
            tw=SF if B and idx==3 and w==VIS else w
            return ('-' if sg<0 else '')+'k_{m,'+w+r'}\cos\theta_{m,'+w+'}'+W(r'1'+sa+r'\tan\theta_{m,'+SF+r'}\tan\theta_{m,'+tw+'}')
        arg=term(VIS,v,angle_v)+('+' if i>0 else '')+term(IR,i,angle_i)
        lines.append(r'&\quad'+(r'\times\Bigl\{' if idx==0 else '+')+coeff+X('iz'+W(arg)))
    lines[-1]+=r'\Bigr\}'
    return math(al(*lines))
polarzero=polar('A')+polar('B')
star=math(r'P^*_\alpha\equiv'+SUM+chi(r'\alpha')+F(t('1m',VIS,BE)+t('1m',IR,GA),dd(VIS,BE)+dd(IR,GA)))
def four(s,includeSF=True):
    lines=[]
    for idx,(v,i) in enumerate([(1,1),(1,-1),(-1,1),(-1,-1)]):
        coeff=('r_{m2,\\mathrm{ir}}'+q(IR) if idx==1 else 'r_{m2,\\mathrm{vis}}'+q(VIS) if idx==2 else 'r_{m2,\\mathrm{vis}}'+q(VIS)+'r_{m2,\\mathrm{ir}}'+q(IR) if idx==3 else '')
        ss=sum3(s,v,i) if includeSF else (('-' if v<0 else '')+bv+('+' if i>0 else '-')+bi)
        if s==-1 and idx==1:coeff='r_{m2}e^{i\beta_{m,\mathrm{ir}}h_m}'
        lines.append((('+' if idx else '')+coeff+exp(ss)))
    return lines
expanded=[r'E^-_1(0^-)&=t_{m1,\mathrm{SF}}\left[\sum_{n=0}(r_{m2,\mathrm{SF}}r_{m1,\mathrm{SF}}'+q(SF)+r')^n\right]P^*_\alpha']
for j,s in enumerate([1,-1]):
    fs=four(s)
    expanded.append(r'&\quad\times\Bigl\{'+lm+r'\Bigl['+fs[0] if j==0 else r'&\quad+'+rs+q(SF)+lp+r'\Bigl['+fs[0])
    expanded.extend(r'&\qquad'+z for z in fs[1:]);expanded[-1]+=r'\Bigr]'+(r'\Bigr\}' if j else '')
expanded+=[r'&='+F(t('m1',SF),dd(SF,''))+r'P^*_\alpha',r'&\quad\times\Bigl[e^{i'+bs+'z}'+lm+'+'+rs+q(SF)+'e^{-i'+bs+'z}'+lp+r'\Bigr]']
for j,z in enumerate(four(1,False)):expanded.append(r'&\quad'+(r'\times\Bigl[' if j==0 else '')+z+(r'\Bigr]' if j==3 else ''))
job('B100','体相反射场的路径、零阶极化及展开',{'B073-p20-01.png':path,'B073-p20-02.png':phases,'B073-p20-03.png':path2,'B073-p21-04.png':polarzero,'B073-p21-05.png':star,'B073-p21-06.png':math(al(*expanded))})
# Integral in the first arrangement: keep its printed denominator signs.
lines=[r'E^-_1(0^-)&=\frac{i}{\delta}'+F(t('m1',SF),dd(SF,''))+r'P^*_\alpha']
for j,s in enumerate([1,-1]):
    for k,(v,i) in enumerate([(1,1),(1,-1),(-1,1),(-1,-1)]):
        cf=('r_{m2,\\mathrm{ir}}'+q(IR) if k==1 else 'r_{m2,\\mathrm{vis}}'+q(VIS) if k==2 else 'r_{m2,\\mathrm{vis}}'+q(VIS)+'r_{m2,\\mathrm{ir}}'+q(IR) if k==3 else '')
        if s<0 and k==1:cf='r_{m2,\\mathrm{ir}}e^{2\beta_{m,\mathrm{ir}}h_m}'
        den=sum3(s,v,i) if s>0 else [sum3(1,-1,-1),sum3(1,-1,1),sum3(-1,1,-1),sum3(1,1,1)][k]
        head=(r'\times\Bigl\{'+lm+r'\Bigl[' if j==0 else '+'+rs+q(SF)+lp+r'\Bigl[') if k==0 else '+'
        lines.append(r'&\quad'+head+cf+F(exp(sum3(s,v,i),hm)+'-1',den)+(r'\Bigr]'+(r'\Bigr\}' if j else '') if k==3 else ''))
# Grouped denominator version; the raw grouped phase in this source is all-plus in each block.
grouped=[]
common=exp(sum3(),hm)
dens=[sum3(1,-1,-1),sum3(1,-1,1),sum3(1,1,-1),sum3()]
coeffs=[('r_{m2,\\mathrm{vis}}r_{m2,\\mathrm{ir}}',common+'-'+exp('2('+bv+'+'+bi+')',hm),'',common+'-'+q(SF)),('r_{m2,\\mathrm{vis}}',common+'-'+q(VIS),'r_{m2,\\mathrm{ir}}',common+'-'+exp('2('+bs+'+'+bi+')',hm)),('r_{m2,\\mathrm{ir}}',common+'-'+q(IR),'r_{m2,\\mathrm{vis}}',common+'-'+exp('2('+bs+'+'+bv+')',hm)),('',common+'-1','r_{m2,\\mathrm{vis}}r_{m2,\\mathrm{ir}}',common+'-'+exp('2('+bv+'+'+bi+')',hm))]
grouped=[r'E^-_1(0^-)&=\frac{i}{\delta}'+F(t('m1',SF),dd(SF,''))+r'P^*_\alpha']
for j,(den,(c1,e1,c2,e2)) in enumerate(zip(dens,coeffs)):
    grouped.append(r'&\quad'+(r'\times\Bigl\{' if j==0 else '+')+F('1',den))
    grouped.append(r'&\qquad\times\Bigl['+lm+c1+W(e1))
    grouped.append(r'&\qquad+'+rs+lp+c2+W(e2)+r'\Bigr]'+(r'\Bigr\}' if j==3 else ''))
note='\n> **译校注（Q068，保留原式）：** 体相反射推导中，零阶B极化的两分母频率标签互换、最后可见光项的正切角写作和频角；场展开与积分中若干指数未印 $i$、相位及分母符号不完全对应。（5.19）沿用交叉频率分母，后两组仍写 $L^-_{m/m}$，前两组写 $L^-_{1/m}$。均逐项保留，未按相邻式统一。按相位失配整理时的各相位是否一致仍待确认。\n'
relations='\n'.join(math(t('m1','',s)+L('m/m',s,a,sg)+'='+('-' if a=='z' and sg=='+' else '')+L('1/m',s,a)) for s,a in [('p','x'),('s','y'),('p','z')] for sg in ['-','+'])
job('B101','体相反射积分和相位失配分组',{'B073-p22-07.png':math(al(*lines))+math(al(*grouped))+note,'B073-p23-08.png':relations})
def eq19(s):
    # Keep the source's crossed incident-frequency phase labels.
    dv=dd(VIS,BE).replace(q(VIS),q(IR));di=dd(IR,GA).replace(q(IR),q(VIS))
    lines=[r'E^-_{1'+s+r'}(0^-)&=\frac{i}{\delta}'+SUM,r'&\quad\times'+F(t('m1',SF,s)+t('1m',VIS,BE)+t('1m',IR,GA),dd(SF,s)+dv+di)]
    coords=['x','z'] if s=='p' else ['y']
    for j,(den,(c1,e1,c2,e2)) in enumerate(zip(dens,coeffs)):
        lines.append(r'&\quad'+(r'\times\Bigl\{' if j==0 else '+')+F('1',den))
        for k,a in enumerate(coords):
            ij='1/m' if j<2 else 'm/m'
            cc1=c1.replace('r_{m2,\\mathrm{vis}}',rv).replace('r_{m2,\\mathrm{ir}}',ri)
            cc2=c2.replace('r_{m2,\\mathrm{vis}}',rv).replace('r_{m2,\\mathrm{ir}}',ri)
            f1=e1;f2=e2
            if s=='p' and j==1 and a=='z':f1=f1.replace(q(VIS),'e^{2\beta_{m,\mathrm{vis}}h_m}')
            if s=='p' and j==2 and a=='z':f2=f2.replace(exp('2('+bs+'+'+bv+')',hm),'e^{2('+bs+'+'+bv+')h_m}')
            lines.append(r'&\qquad'+(r'\times\Bigl\{' if k==0 else '+')+chi(a)+L(ij,s,a)+r'\Bigl['+cc1+W(f1))
            lines.append(r'&\qquad'+('-' if a=='z' else '+')+r('m2',SF,s)+cc2+W(f2)+r'\Bigr]'+(r'\Bigr\}' if k==len(coords)-1 else ''))
    lines[-1]+=r'\Bigr\}'
    return math(al(*lines),'5.19a' if s=='p' else '5.19b')
job('B102','完整的体相p、s偏振反射场5.19',{'B073-p23-09.png':eq19('p'),'B073-p23-10.png':eq19('s'),'B073-p24-11.png':'<!-- 式（5.19b）的跨页续式已与上式合并为单一可编辑公式，未重复显示重叠区域。 -->'})
apply()

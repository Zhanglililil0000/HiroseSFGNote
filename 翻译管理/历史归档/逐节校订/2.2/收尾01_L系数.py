from 收尾公式工具 import *
dp=n('2')+co('m')+'+'+n('m')+co('2');ds=n('2')+co('2')+'+'+n('m')+co('m')
parts=[]
for num,sg,xm,zm in [('5.3','-','2','2'),('5.4','+','m','m')]:
    parts.append(math(L('2/m','p','x',sg)+'='+F(co(xm),dp),num+'a'))
    parts.append(math(L('2/m','s','y',sg)+'='+F('1',ds),num+'b'))
    sign='-' if sg=='+' else '';ratio=W(n(zm)+'/'+n("m''"))
    parts.append(math(al(L('2/m','p','z',sg)+'&='+sign+F(ratio+si("m''"),dp),'&='+sign+F(ratio+'^2'+si(zm),dp)),num+'c'))
job('B094','m/2界面两方向L系数',{'B070-p12-02.png':'\n'.join(parts)})
den='2'+n('m')+co('m')
parts=[math(L('m/m','p','x')+'='+L('m/m','p','x','+')+'='+F(co('m'),den),'5.5a'),math(L('m/m','s','y')+'='+L('m/m','s','y','+')+'='+F('1',den),'5.5b'),math(L('m/m','p','z')+'=-'+L('m/m','p','z','+')+'='+F(si('m'),den),'5.5c')]
mapping={'B070-p12-03.png':'\n'.join(parts)}
for img,ij,z,args,minusmed,plusmed,a,bnum in [('B070-p12-04.png','1/m','0','z=0','1','m','5.6','5.7'),('B070-p13-05.png','2/m','h_m','z=h_m','m','2','5.8','5.9'),('B070-p13-06.png','m/m','z','z','m','m','5.10','5.11')]:
    seq=[]
    for num,sg,med in [(a,'-',minusmed),(bnum,'+',plusmed)]:
        seq.append(math(E(med,'p',args,sg)+'='+L(ij,'p','x',sg)+P('x',z)+'+'+L(ij,'p','z',sg)+P('z',z),num+'a'))
        seq.append(math(E(med,'s',args,sg)+'='+L(ij,'s','y',sg)+P('y',z),num+'b'))
    mapping[img]='\n'.join(seq)
job('B095','膜内L系数及全部源点电场振幅',mapping)
apply()

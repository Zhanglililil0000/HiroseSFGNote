from pathlib import Path
import json,re,hashlib
O=Path(__file__).resolve().parent;R=O.parents[2];P=next((R/'中文版本/第二章 薄膜产生的SFG').glob('2.4 *.md'))
BS=chr(92)
def tex(s):return s.replace('§',BS)
def block(s):return '\n$$\n'+tex(s)+'\n$$\n\n'
def al(rows,tag=None):return block('§begin{aligned}\n'+(' §§\n'.join(rows))+'\n§end{aligned}'+('§tag{'+tag+'}' if tag else ''))
def frac(a,b):return '§frac{'+a+'}{'+b+'}'
def n(a):return 'n_{'+a+',§mathrm{SF}}'
def th(a):return '§theta_{'+a+',§mathrm{SF}}'
def L(d,j,q,c):return 'L^{'+d+'}_{'+j+','+q+','+c+'}'
def chi(c):return '§chi_{'+c+'§beta§gamma}'
def rt(k,j,f,q):return k+'_{'+j+','+('§mathrm{'+f+'}' if f in ['SF','vis','ir'] else f)+','+q+'}'
def rr(j,f,q):return rt('r',j,f,q)
def tt(j,f,q):return rt('t',j,f,q)
def b(f):return '§beta_{m,§mathrm{'+f+'}}'
def ex(f,mul='2i'):return 'e^{'+mul+b(f)+'h_m}'
def D(f,q,phase=None):return '(1+'+rr('1m',f,q)+rr('m2',f,q)+ex(phase or f)+')'
def par(s):return '(1+'+s+')'
def field(q,trans=False,missing=False):return 'E'+('' if missing else ('^+' if trans else '^-'))+'_{'+('2' if trans else '1')+q+'}('+('h_m^+' if trans else '0^-')+')'
pref='§sum_{§beta,§gamma}E^0_{§mathrm{vis},§beta}E^0_{§mathrm{ir},§gamma}'
def eq(q,t,factors,last,tag,missing=False,standalone=False):
 return al([field(q,t,missing)+'&='+pref+('e' if standalone else '')+' '+factors[0]]+['&§quad§times '+x for x in factors[1:]]+['&§quad§times '+last],tag)
def commit(batch,text,start,end=None):
 text=tex(text);old=P.read_text(encoding='utf-8');a=old.index(start);z=old.index(end,a) if end else len(old)
 assert not (O/(batch+'-修订前.md')).exists()
 (O/(batch+'-修订前.md')).write_text(old,encoding='utf-8');new=old[:a]+text+old[z:];P.write_text(new,encoding='utf-8')
 assert new[:a]==old[:a] and (not end or new[new.index(end,a):]==old[z:])
 (O/(batch+'-本批译文.md')).write_text(text,encoding='utf-8')
 print(batch,len(text))

# B126: six back-interface coefficients and three internal relations.
s='### 介质2与膜之间的极化片\n\n对于介质2与层叠膜 $m$ 之间的极化片 $m^{§prime§prime}$ 所产生的光，有：\n\n'
den=n('2')+'§cos'+th('m')+'+'+n('m')+'§cos'+th('2');ds=n('2')+'§cos'+th('2')+'+'+n('m')+'§cos'+th('m')
for direction,medium,sign in [('-','2',''),('+','m','-')]:
 s+=block(L(direction,'2/m','p','x')+'='+frac('§cos'+th(medium),den)+'.')
 s+=block(L(direction,'2/m','s','y')+'='+frac('1',ds)+'.')
 ratio='('+n(medium)+'/'+n('m^{§prime§prime}')+')'
 s+=al([L(direction,'2/m','p','z')+'&='+sign+frac(ratio+'§sin'+th('m^{§prime§prime}'),den), '&='+sign+frac(ratio+'^2§sin'+th(medium),den)+'.'])
s+='### 膜内部的极化片\n\n对于层叠膜内部的极化片所产生的光，有：\n\n'
for q,c,num,negative in [('p','x','§cos'+th('m'),False),('s','y','1',False),('p','z','§sin'+th('m'),True)]:
 s+=block(L('-','m/m',q,c)+'='+('-' if negative else '')+L('+','m/m',q,c)+'='+frac(num,'2'+n('m')+'§cos'+th('m'))+'.')
commit('B126',s,'对于媒质2与多层薄膜 m 之间的极化片','由此，各部位产生的 SFG 光电场振幅可表示为：')

# B127: all twelve emitted fields, including the source's P_y(00+) typo.
s='### 各源点的和频光电场振幅\n\n由此，各部位产生的和频光电场振幅可表示如下。\n\n**来自 $P(0)$ 的贡献**：$P(0^-)$ 为介质1侧电场产生的极化强度，$P(0^+)$ 为膜侧电场产生的极化强度。\n\n'
for j,pos,layer in [('1/m','0','1'),('2/m','h_m','m'),('m/m','z','m')]:
 if j=='2/m':s+='**来自 $P(h_m)$ 的贡献**：$P(h_m^+)$ 为介质2侧电场产生的极化强度，$P(h_m^-)$ 为膜侧电场产生的极化强度。\n\n'
 if j=='m/m':s+='**来自 $P(z)$ 的贡献**：\n\n'
 rows=[]
 for d,out in [('-',layer),('+','m' if j=='1/m' else ('2' if j=='2/m' else 'm'))]:
  arg=pos+('^'+d if pos!='z' else '')
  rows.append('E^{'+d+'}_{'+out+',p}(z='+arg+')&='+L(d,j,'p','x')+'P_x('+arg+')+'+L(d,j,'p','z')+'P_z('+arg+'),')
  py='00^+' if j=='1/m' and d=='+' else arg
  rows.append('E^{'+d+'}_{'+out+',s}(z='+arg+')&='+L(d,j,'s','y')+'P_y('+py+').')
 s+=al(rows)
 if j=='1/m':s+='> **原文疑点（Q079，PDF p3）**：最后一式原写 $P_y(00^+)$，此处照录；候选为 $P_y(0^+)$，未采用修正。\n\n'
commit('B127',s,'由此，各部位产生的 SFG 光电场振幅可表示为：','## 1/m 界面的外侧')

def excitation(kind):
 # Each factor is expanded in the emitted Markdown; these helpers introduce no shorthand there.
 if kind in ['front','inside']:
  fac=[]
  for f,q in [('vis','§beta'),('ir','§gamma')]:
   lead=par(rr('1m',f,q)) if kind=='front' else tt('1m',f,q)
   fac.append(frac(lead+par(rr('m2',f,q)+ex(f)),D(f,q)))
  return fac
 if kind in ['back','backinside']:
  lead=tt('1m','vis','§beta')+tt('1m','ir','§gamma')
  if kind=='back':lead+=tt('m2','vis','§beta')+tt('m2','ir','§gamma')
  else:lead+=par(rr('m2','vis','§beta'))+par(rr('m2','ir','§gamma'))
  return [frac(lead+'e^{i('+b('ir')+'+'+b('vis')+')h_m}',D('vis','§beta')+D('ir','§gamma'))]
def frontfilmden(f,q,reverse=False):
 a=rr("1m'",f,q);c=rr("m'm",f,q)
 tail=(rr("mm'",f,q)+'+'+rr("m'1",f,q)) if reverse else '('+a+'+'+c+')'
 if reverse:tail='('+tail+')'
 return '1+'+a+c+'+'+rr('m2',f,q)+tail+ex(f)
def filmexc(front=True):
 fac=[]
 for f,q in [('vis','§beta'),('ir','§gamma')]:
  if front:num=tt("1m'",f,q)+par(rr("m'm",f,q))+par(rr('m2',f,q)+ex(f));den=frontfilmden(f,q)
  else:
   a=rr("mm^{§prime§prime}",f,q);c=rr("m^{§prime§prime}2",f,q)
   num=tt('1m',f,q)+tt('mm^{§prime§prime}',f,q)+par(c)+ex(f,'i')
   den='(1+'+a+c+')+'+rr('1m',f,q)+'('+a+'+'+c+')'+ex(f)
  fac.append(frac(num,den))
 return fac
def polsum(d,j,q):
 if q=='s':return L(d,j,q,'y')+chi('y')
 return '('+L(d,j,q,'x')+chi('x')+'+'+L(d,j,q,'z')+chi('z')+')'
def frontreflect(q):
 a=par(rr('m2','SF',q)+ex('SF'))+L('-','1/m',q,'x' if q=='p' else 'y')+chi('x' if q=='p' else 'y')
 if q=='p':a+='+(1-'+rr('m2','SF',q)+ex('SF')+')'+L('-','1/m',q,'z')+chi('z')
 return a
def backtrans(q):
 a='(1-'+rr('1m','SF',q)+ex('SF')+')'+L('+','2/m',q,'x' if q=='p' else 'y')+chi('x' if q=='p' else 'y')
 if q=='p':a+='+'+par(rr('1m','SF',q)+ex('SF'))+L('+','2/m',q,'z')+chi('z')
 return a

# B128: front outside and complete front molecular film, eight numbered expressions.
s='## 1/m界面外侧产生的和频光\n\n源点为 $x=-2nh_m§tan§theta_{m,§mathrm{SF}}$、$z=0^-$。\n\n### 反射和频光\n\n'
for q,letter in [('p','a'),('s','b')]:s+=eq(q,False,excitation('front'),frac(frontreflect(q),D('SF',q)),'1'+letter,True)
s+='### 透射和频光\n\n'
for q,letter in [('p','a'),('s','b')]:
 s+=eq(q,True,excitation('front'),frac(tt('1m','SF',q)+tt('m2','SF',q)+ex('SF','i'),D('SF',q))+polsum('+','m/1',q),'2'+letter)
s+='> **原文疑点（Q080，PDF p4，式2a、2b）**：这里的L层标原为 $m/1$，而定义段用 $1/m$。此处保留；是否应统一为 $1/m$ 待核。式1a、1b的场振幅原未写方向上标，也不补入。\n\n'
s+='### 表面已形成完整薄膜时\n\n当表面已形成完整薄膜时，构成该薄膜（原文用 $m\'$ 标示其折射率）的分子所产生的和频光需要考虑内部反射。\n\n#### 反射和频光\n\n'
for q,letter in [('p','a'),('s','b')]:
 factor=par(rr("1m'",'SF',q)+rr("m'm",'SF',q))
 s+=eq(q,False,filmexc(),frac(factor+'['+frontreflect(q)+']',frontfilmden('SF',q)),'3'+letter)
s+='#### 透射和频光\n\n'
for q,letter in [('p','a'),('s','b')]:
 num=tt('m2','SF',q)+par(rr("1m'",'SF',q)+rr("m'm",'SF',q))+ex('SF','i')
 s+=eq(q,True,filmexc(),frac(num,frontfilmden('SF',q,True))+'§mathclose{)}'+polsum('+','1/m',q),'4'+letter)
s+='> **原文疑点（Q081，PDF p5，式4a、4b）**：和频出射分母的末项原用 $r_{mm\',§mathrm{SF},p(s)}+r_{m\'1,§mathrm{SF},p(s)}$，与式3的方向下标不同，且分式之后有一个未配对的右圆括号。两处均保留；方向改用式3及删去该括号只是候选，未采用。\n\n'
commit('B128',s,'## 1/m 界面的外侧','## 1/m 界面的内侧')

# B129: front inside, including 6b across p5/6.
s='## 1/m界面内侧产生的和频光\n\n源点为 $x=-2nh_m§tan§theta_{m,§mathrm{SF}}$、$z=0^+$。\n\n### 反射和频光\n\n'
for q,l in [('p','a'),('s','b')]:s+=eq(q,False,excitation('inside'),frac(frontreflect(q),D('SF',q)),'5'+l)
s+='### 透射和频光\n\n'
for q,l in [('p','a'),('s','b')]:s+=eq(q,True,excitation('inside'),frac(tt('m2','SF',q)+ex('SF','i'),D('SF',q))+polsum('+','1/m',q),'6'+l)
commit('B129',s,'## 1/m 界面的内侧','## m/2 界面的外侧')

# B130: back outside and complete molecular back film.
s='## m/2界面外侧产生的和频光\n\n源点为 $x=-(2n+1)h_m§tan§theta_{m,§mathrm{SF}}$、$z=h_m^+$。\n\n### 反射和频光\n\n'
for q,l in [('p','a'),('s','b')]:
 # Source has a baseline 2 followed by an exponential lacking i.
 oddden='1+r_{1m,'+q+'}r_{m2,'+q+'}§,2e^{2'+b('SF')+'h_m}'
 oddnum='t_{m1,'+q+'}'+ex('SF','i' if q=='p' else '')
 # Original printed r_m2,wvis is retained in visible numerator's denominator.
 exc=excitation('back')
 exc=[x.replace(rr('m2','vis','§beta'),rr('m2','wvis','§beta')) for x in exc]
 s+=eq(q,False,exc,frac(oddnum,oddden)+polsum('-','2/m',q),'7'+l)
s+='> **原文疑点（Q082，PDF p6，式7a、7b）**：激发光分母的可见光反射系数原写 $r_{m2,wvis,§beta}$。和频出射分母在 $r_{m2,p(s)}$ 后另有基线数字2，随后指数写 $2§beta_{m,§mathrm{SF}}h_m$，未见 $i$；7b出射分子的指数也未见 $i$。这里保留这些写法以及省略SF的系数下标；候选为常规 $1+r_{1m,§mathrm{SF},p(s)}r_{m2,§mathrm{SF},p(s)}e^{2i§beta_{m,§mathrm{SF}}h_m}$ 及相应出射相位，未采用。\n\n'
s+='### 透射和频光\n\n'
for q,l in [('p','a'),('s','b')]:
 exc=[x.replace(rr('m2','vis','§beta'),rr('m2','wvis','§beta')) for x in excitation('back')]
 s+=eq(q,True,exc,frac(backtrans(q),D('SF',q)),'8'+l)
s+='> **原文疑点（Q082续）**：式8a、8b同样使用 $wvis$，也按原文保留。\n\n'
s+='### 发出和频光的界面为薄膜时\n\n当发出和频光的界面为折射率以 $m^{§prime§prime}$ 标示的薄膜时，有：\n\n#### 反射和频光\n\n'
for trans,number in [(False,'9'),(True,'10')]:
 if trans:s+='#### 透射和频光\n\n'
 for q,l in [('p','a'),('s','b')]:
  a=rr('mm^{§prime§prime}','SF',q);c=rr('m^{§prime§prime}2','SF',q)
  den='1+'+a+c+'+'+rr('1m','SF',q)+'('+a+'+'+c+')'+ex('SF')
  num=par(a+c)
  if trans:num+='['+backtrans(q)+']'
  else:num=tt('m1','SF',q)+ex('SF','i')+num
  last=frac(num,den)+('' if trans else polsum('-','2/m',q))
  s+=eq(q,trans,filmexc(False),last,number+l,missing=trans)
s+='> **原文记号说明（Q080续，PDF p7）**：式10a、10b左端未写“+”方向上标，此处保留。此段 $m^{§prime§prime}$ 作为薄膜/折射率标记的用法亦随原文，不另引入新的折射率值。\n\n'
commit('B130',s,'## m/2 界面的外侧','## m/2 界面的内侧')

# B131: back inside.
s='## m/2界面内侧产生的反射和频光\n\n源点为 $x=-(2n+1)h_m§tan§theta_{m,§mathrm{SF}}$、$z=h_m^-$。\n\n> **标题说明（译者）**：原文总标题含“反射”，其下仍依次列反射与透射两组，此处按原顺序保留。\n\n### 反射和频光\n\n'
for q,l in [('p','a'),('s','b')]:s+=eq(q,False,excitation('backinside'),frac(tt('m1','SF',q)+ex('SF','i'),D('SF',q))+polsum('-','2/m',q),'11'+l)
s+='### 透射和频光\n\n'
for q,l in [('p','a'),('s','b')]:
 num=par(rr('m1','SF',q)+ex('SF'))+L('+','2/m',q,'x' if q=='p' else 'y')+chi('x' if q=='p' else 'y')
 if q=='p':num+='+(-1+'+rr('m1','SF',q)+ex('SF')+')'+L('+','2/m',q,'z')+chi('z')
 s+=eq(q,True,excitation('backinside'),frac(num,D('SF',q)),'12'+l,standalone=True)
s+='> **原文疑点（Q083，PDF p7—8，式12a、12b）**：求和中的两入射场之后有孤立的 $e$，未见指数。此处照录；删除它只是候选。式12a的 $z$ 项写作 $-1+r_{m1,§mathrm{SF},p}e^{2i§beta_{m,§mathrm{SF}}h_m}$，未按相邻式改号。\n\n'
commit('B131',s,'## m/2 界面的内侧','## 薄膜体相')

# Bulk expressions: fully expanded terms, original mixed L layers and phase pairings retained.
sumphase=b('SF')+'+'+b('vis')+'+'+b('ir')
ep='e^{i('+sumphase+')h_m}'
en='e^{i(-'+b('SF')+'+'+b('vis')+'+'+b('ir')+')h_m}'
def exp_sum(a,c):return 'e^{2i('+b(a)+'+'+b(c)+')h_m}'
rv=rr('m2','vis','§beta');ri=rr('m2','ir','§gamma')
dens=[b('SF')+'-'+b('vis')+'-'+b('ir'),b('SF')+'-'+b('vis')+'+'+b('ir'),b('SF')+'+'+b('vis')+'-'+b('ir'),b('SF')+'+'+b('vis')+'+'+b('ir')]
def reflpair(k,q):
 rs=rr('m2','SF',q)
 return [(rv+ri+'('+ep+'-'+exp_sum('vis','ir')+')',rs+'('+ep+'-'+ex('SF')+')'),(rv+'('+ep+'-'+ex('vis')+')',rs+ri+'('+ep+'-'+exp_sum('SF','ir')+')'),(ri+'('+ep+'-'+ex('ir')+')',rs+rv+'('+ep+'-'+exp_sum('SF','vis')+')'),('('+ep+'-1)',rs+rv+ri+'('+ep+'-'+exp_sum('vis','ir')+')')][k]
def bulkhead(q,trans):
 den=D('SF',q)+D('vis','§beta',None if trans else 'ir')+D('ir','§gamma',None if trans else 'vis')
 # Wide three-factor denominator is split as a product of three fractions, with no new named factors.
 factors=[frac(tt('1m','vis','§beta'),D('vis','§beta',None if trans else 'ir')),frac(tt('1m','ir','§gamma'),D('ir','§gamma',None if trans else 'vis')),frac(ex('SF','i') if trans else tt('m1','SF',q),D('SF',q))]
 return [field(q,trans)+'&=§frac{i}{§delta}'+pref, '&§quad§times '+factors[0]+factors[1], '&§quad§times '+factors[2]]
s='## 膜体相产生的和频光\n\n体相范围与源点位置为：\n\n'+al(['0&<z<h_m,','A_{n=0,1,2}:§quad x&=-2nh_m§tan§theta_{m,§mathrm{SF}}-z§tan§theta_{m,§mathrm{SF}},','B_{n=-1,0,1,2}:§quad x&=-(2n+1)h_m§tan§theta_{m,§mathrm{SF}}+z§tan§theta_{m,§mathrm{SF}}.'])
s+='> **记号说明（译者）**：这里的 $§beta_{m,§mathrm{SF/vis/ir}}$ 是传播量；求和下标 $§beta,§gamma$ 则枚举入射场与二阶非线性极化率的分量，两种用途按原文保留。原文前因子为 $i/§delta$，本独立文件未在此定义 $§delta$，不以旧译 $i§Delta$ 代换，也不补其含义。\n\n### 反射和频光\n\n'
for q,l in [('p','a'),('s','b')]:
 rows=bulkhead(q,False)
 for k,den in enumerate(dens):
  a,c=reflpair(k,q);j='1/m' if k<2 else 'm/m'
  if q=='p':
   expr=chi('x')+L('-',j,q,'x')+'['+a+'+'+c+']'
   rows.append('&§quad'+('§times§big§{' if k==0 else '+')+frac('1',den)+'§big§{'+expr)
   rows.append('&§qquad+'+chi('z')+L('-',j,q,'z')+'['+a+'-'+c+']§big§}')
  else:
   expr=chi('y')+L('-',j,q,'y')+'['+a+'+'+c+']'
   rows.append('&§quad'+('§times§big§{' if k==0 else '+')+frac('1',den)+'§big§{'+expr)
 s+=al(rows,'13'+l)
s+='> **原文疑点（Q084，PDF p8—9，式13a、13b）**：公共分母中vis系数配ir相位、ir系数配vis相位，按原文保留；候选为各频率与自身相位配对。四个积分项的L层标前两项用 $1/m$，后两项用 $m/m$，也未统一。原式13a外层左花括号、13b各项左花括号的闭合不齐；这里以固定大小括号照录可见符号，不补一个推定的闭合范围。\n\n'
commit('B132',s,'## 薄膜体相')

def transpair(k,q):
 rs=rr('m1','SF',q)
 return [('['+en+'-1]',rs+rv+ri+'['+exp_sum('vis','ir')+'-'+ep+']'),(ri+'['+en+'-'+ex('ir')+']',rs+rv+'['+ex('vis')+'-'+ep+']'),(rv+'['+en+'-'+ex('vis')+']',rs+ri+'['+ex('ir')+'-'+ep+']'),(rv+ri+'['+en+'-'+exp_sum('vis','ir')+']',rs+'[1-'+ep+']')][k]
s='### 透射和频光\n\n'
for q,l in [('p','a'),('s','b')]:
 rows=bulkhead(q,True)
 for c,sgn in ([('x','+'),('z','-')] if q=='p' else [('y','+')]):
  rows.append('&§quad'+('§times§big§{' if c=='x' else ('+' if c=='z' else '§times'))+L('+','2/m',q,c)+chi(c)+'§big[')
  for k,den in enumerate(dens):
   a,bb=transpair(k,q)
   # Two fractions per numerator permit a narrow multiline layout while retaining every term.
   rows.append('&§qquad'+('' if k==0 else '+')+frac(a,den))
   rows.append('&§qquad'+sgn+frac(bb,den)+('§big]' if k==3 else '')+('§big§}' if k==3 and c=='z' else ('§big§}' if k==3 and c=='y' else '')))
 if q=='s':
  # Source uses curly braces, not square brackets, for the s chain.
  rows=[x.replace('§big[','§big§{').replace('§big]','') for x in rows]
 s+=al(rows,'14'+l)
s+='> **跨页说明（译者）**：式14a的 $z$ 分量后两项从PDF p9续至p10，已在此接全。各积分项的分子为两部分；为便于阅读，将同分母分子的两部分分行写成两个分式，未引入省略因子或新记号。式13—14的 $§delta$ 含义及异常层标/相位仍属未决问题（Q084），完成转写不表示已证明原式无误。\n\n'
with P.open('a',encoding='utf-8') as f:f.write(tex(s))
(O/'B133-本批译文.md').write_text(tex(s),encoding='utf-8')
print('B133',len(s))

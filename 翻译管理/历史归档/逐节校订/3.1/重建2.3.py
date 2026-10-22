exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
old=P.read_text(encoding='utf-8');assert not (O/'2.3-修订前.md').exists();(O/'2.3-修订前.md').write_text(old,encoding='utf-8');a=old.index('### 2.3 SFG电场');b=old.index('## 3. 三层系',a);source=old[a:b];cut=source.index("**m' 层内部极化产生的SFG：**");interface=source[:cut]
# Remove the duplicated m/2 source-point pair in the old translation, verified against p17—21.
label='**m/2 界面的 2 侧极化产生的SFG：**';one=interface.index(label);two=interface.index(label,one+1);z=interface.index("**m'/m 界面的 m' 侧极化产生的SFG：**",two);interface=interface[:two]+interface[z:]
interface=interface.replace('r_{1m,,SF,',"r_{1m',SF,")
def disp(s):return '$$\n'+s.strip()+'\n$$\n\n'
def eqblocks(s):return re.findall(r'\$\$([\s\S]*?)\$\$',s)
def tagged(s):
 result={};buf=[]
 for x in eqblocks(s):
  buf.append(x)
  if r'\tag{' in x:
   t=re.search(r'\\tag\{([^}]+)\}',x)[1];result[t]=buf;buf=[]
 return result
# For 2.31, unnumbered preceding derivation blocks occur before the first field LHS.
allblocks=eqblocks(interface);groups={}
for i,x in enumerate(allblocks):
 if r'\tag{' in x:
  tag=re.search(r'\\tag\{([^}]+)\}',x)[1];j=i
  while j>0 and not ('E^' in allblocks[j] and '=' in allblocks[j]):j-=1
  groups[tag]=allblocks[j:i+1]
assert '2.31a' in groups
g33=[]
for suffix in 'ab':
 g='\n'.join(groups['2.31'+suffix]).replace('2.31'+suffix,'2.33'+suffix).replace('n_{m"} = n_1',"n_{m''} = n_{m'}")
 for f,axis in [('vis',r'\alpha'),('ir',r'\beta')]:g=g.replace('(1+ r_{1m\','+f+','+axis+'})','t_{1m\','+f+','+axis+'}')
 g=g.replace("L^{-}_{1/m',",'L^{-}_{1/m,')
 g33.append(disp(g))
den=r'1+r_{1m\prime}r_{m\prime m}a^2+(r_{m\prime m}+r_{1m\prime}a^2)r_{m2}b^2'
missing='''**1/m′界面m′侧的极化产生的和频光：**

（a）反射方向。

在文件《一般式》的(2.1)和(2.3)式中，令 $z_1=0$、$a_0^*=a$、$a_0=1$。

'''
missing+=disp(r'E_1^-(0^-)_{net}=\frac{t_{m\prime1}[(r_{m\prime m}+r_{m2}b^2)a^2L^+_{m\prime/m\prime}+(1+r_{m\prime m}r_{m2}b^2)L^-_{m\prime/m\prime}]}{'+den+r'}P^*(z_1=0)')
missing+='其中，\n\n'+disp(r'\begin{aligned}t_{1m\prime,p}L^+_{m\prime/m\prime,px}&=t_{1m\prime,p}L^-_{m\prime/m\prime,px}=L^-_{1/m\prime,px},\\t_{1m\prime,s}L^+_{m\prime/m\prime,sy}&=t_{1m\prime,s}L^-_{m\prime/m\prime,sy}=L^-_{1/m\prime,sy},\\t_{1m\prime,p}L^+_{m\prime/m\prime,pz}&=-t_{1m\prime,p}L^-_{m\prime/m\prime,pz}=L^-_{1/m\prime,pz}\quad(n_{m\prime\prime}=n_{m\prime}).\end{aligned}')
missing+='因此，\n\n'+disp(r'E_1^-(0^-)_{net}=\frac{t_{m\prime1}[(1+r_{m\prime m}r_{m2}b^2)\pm(r_{m\prime m}+r_{m2}b^2)a^2]}{'+den+r'}L^-_{1/m}P^*(z_1=0)')+'上符号用于x、y分量，下符号用于z分量。由式(2.19)，\n\n'+''.join(g33)
missing+='（b）透射方向。\n\n在文件《一般式》的(2.2)和(2.4)式中，令 $z_1=0$、$a_0^*=a$、$a_0=1$，得到\n\n'
missing+=disp(r'E_2^+(h_{m\prime}+h_m^+)_{net}=\frac{t_{m2}ab[t_{m\prime m}L^+_{m\prime/m\prime}+r_{m\prime1}t_{m\prime m}L^-_{m\prime/m\prime}]}{'+den+r'}P^*(z_1=0)')
missing+='其中，\n\n'+disp(r'\begin{aligned}t_{m\prime m,p}L^+_{m\prime/m\prime,px}&=t_{m\prime m,p}L^-_{m\prime/m\prime,px}=L^+_{m\prime/m,px},\\t_{m\prime m,s}L^+_{m\prime/m\prime,sy}&=t_{m\prime m,s}L^-_{m\prime/m\prime,sy}=L^+_{m\prime/m,sy},\\t_{m\prime m,p}L^+_{m\prime/m\prime,pz}&=-t_{m\prime m,p}L^-_{m\prime/m\prime,pz}=L^+_{m\prime/m,pz}\quad(n_{m\prime\prime}=n_{m\prime}).\end{aligned}')
missing+='因此，\n\n'+disp(r'E_2^+(h_{m\prime}+h_m^+)_{net}=\frac{t_{m2}ab(1\pm r_{m\prime1})}{'+den+r'}L^-_{m\prime/m}P^*(z_1=0)')+'上符号用于x、y分量，下符号用于z分量。由式(2.19)，\n\n'
interface=interface.replace("（2）1/m' 界面的 m' 侧（续）\n\n由 (2.19) 式，",missing)
q=note('Q105','PDF p13—25，界面出射场',r'原式中的双撇层折射率条件、L的正负号及层名、场位置和引用号均逐处保留，不跨式统一。p19—21的m/2界面m侧引用2.23而非邻近2.22，候选为2.22；2.33与2.34的L层名/正负也有差异，候选须结合源片定义核验。p24—25无编号式中m/2连接因子的m记号、2.42a/b的正反射系数因子亦按原式保留；未采用修正。旧译r的层标“1m,,SF”恢复为原页1m′,SF，属转写修复。')
interface=interface.replace('### 2.3 SFG电场','### 2.3 和频电场').replace('SFG','和频').replace('E$^{-}',r'$E^{-}').replace('E$^{+}',r'$E^{+}')
interface+=q
# Utilities for the full body-source expansions printed p25—37.
def rr(ij,f='',p=''):return 'r_{'+ij+(','+f if f else '')+(','+p if p else '')+'}'
def tt(ij,f='',p=''):return 't_{'+ij+(','+f if f else '')+(','+p if p else '')+'}'
def beta(l,f=''):return r'\beta_{'+l+(','+f if f else '')+'}'
def ex(l,f='',mult='2'):return 'e^{'+mult+'i'+beta(l,f)+'h_{'+l+'}}'
def d(f,axis):return '1+'+rr("1m'",f,axis)+rr("m'm",f,axis)+ex("m'",f)+'+('+rr("m'm",f,axis)+'+'+rr("1m'",f,axis)+ex("m'",f)+')'+rr('m2',f,axis)+ex('m',f)
def fr(n,de):return r'\frac{'+n+'}{'+de+'}'
def block(rows,tag=None):return disp(r'\begin{aligned}'+'\n'+r'\\[5pt]'.join(rows)+'\n'+r'\end{aligned}'+(r'\tag{'+tag+'}' if tag else ''))
def weights(layer):
 vals=[]
 for f,axis in [('vis',r'\alpha'),('ir',r'\beta')]:
  if layer=="m'":fw='(1+'+rr("m'm",f,axis)+rr('m2',f,axis)+ex('m',f)+')';bw='('+rr("m'm",f,axis)+'+'+rr('m2',f,axis)+ex('m',f)+')'+ex("m'",f)
  else:fw='1';bw=rr('m2',f,axis)+ex('m',f)
  vals.append((fw,bw))
 return [vals[0][0]+vals[1][0],vals[0][0]+vals[1][1],vals[0][1]+vals[1][0],vals[0][1]+vals[1][1]]
signs=[(1,1),(1,-1),(-1,1),(-1,-1)]
def bsums(layer,sv,si,sf):
 v=beta(layer,'vis');ir=beta(layer,'ir');s=beta(layer,'SF');out=('' if sf==1 else '-')+s
 out+=('+' if sv==1 else '-')+v;out+=('+' if si==1 else '-')+ir;return out
def kernel(layer,sv,si,sf):
 phase=bsums(layer,sv,si,sf);denom=phase if sf==1 else bsums(layer,-sv,-si,1)
 return fr('e^{i('+phase+')h_{'+layer+'}}-1',denom)
def sumrows(layer,mode,component):
 # component '+' for x/y, '-' for z, or '\\pm' for generic relations.
 sfaxis='p' if component!='s' else 's';op='-' if component=='-' else ('\\pm' if component=='pm' else '+');rows=[]
 for j,((sv,si),w) in enumerate(zip(signs,weights(layer))):
  sf=sfaxis;H=ex('m','SF');X=ex("m'",'SF')
  if layer=="m'" and mode=='R':A='(1+'+rr("mm'",'SF',sf)+rr('m2','SF',sf)+H+')';B='('+rr("m'm",'SF',sf)+'+'+rr('m2','SF',sf)+H+')'+X;term=A+kernel(layer,sv,si,1)+op+B+kernel(layer,sv,si,-1)
  elif layer=="m'":term=kernel(layer,sv,si,-1)+op+rr("m'1",'SF',sf)+kernel(layer,sv,si,1)
  elif mode=='R':term=kernel(layer,sv,si,1)+op+rr('m2','SF',sf)+H+kernel(layer,sv,si,-1)
  else:
   A='(1+'+rr("1m'",'SF',sf)+rr("m'm",'SF',sf)+X+')';B='('+rr("m'm",'SF',sf)+'+'+rr("1m'",'SF',sf)+X+')';term=A+kernel(layer,sv,si,-1)+op+B+kernel(layer,sv,si,1)
  # Keep each coefficient and each paired integral term on separate rows.
  rows += [('&\quad\times\{' if j==0 else '&\qquad+')+w+r'\bigl[',r'&\qquad '+term+r'\bigr]'+(r'\}' if j==3 else '')]
 return rows
def pumps(layer,phase=True):
 rows=[]
 for f,axis in [('vis',r'\alpha'),('ir',r'\beta')]:
  num=tt("1m'",f,axis)
  if layer=='m':num+=tt("m'm",f,axis)+(ex("m'",f,'') if phase else '')
  rows.append(r'&\quad\times'+fr(num,d(f,axis)))
 return rows
def efield(layer,mode,sv,si,sf):
 z='z_1' if layer=="m'" else 'z_2';return r'\exp[i'+z+'('+bsums(layer,sv,si,sf)+')]'
def sourcefield(layer,mode,source):
 sf=-1 if source=='+' else 1;L='L^{'+source+'}_{'+layer+'/'+layer+'}';phase="e^{i"+beta("m'",'SF')+"h_{m'}}";H=ex('m','SF');X=ex("m'",'SF')
 if layer=="m'" and mode=='R':pref=tt("m'1")+(X+'('+rr("m'm")+'+'+rr('m2')+ex('m')+')' if source=='+' else '(1+'+rr("mm'")+rr('m2')+ex('m')+')')
 elif layer=="m'":pref=tt('m2')+'e^{i'+beta('m')+'h_m}'+tt("m'm")+('' if source=='+' else rr("m'1"))
 elif mode=='R':pref=tt("m'1")+tt("mm'")+phase+(rr('m2')+ex('m') if source=='+' else '')
 else:pref=tt('m2')+'e^{i'+beta('m')+'h_m}'+('(1+'+rr("1m'")+rr("m'm")+ex("m'")+')' if source=='+' else '('+rr("m'm")+'+'+rr("1m'")+ex("m'")+')')
 rows=[('E_1^-(0^-)' if mode=='R' else r'E_2^+(h_{m\prime}+h_m^+)')+r'&=\sum_{\alpha,\beta}'+pref+L+r'P_a^*']
 for j,((v,i),w) in enumerate(zip(signs,weights(layer))):rows.append(('&\quad\times\{' if j==0 else '&\qquad+')+w+efield(layer,mode,v,i,sf)+(r'\}' if j==3 else ''))
 return block(rows)
def lrelations(layer,mode):
 t="m'1" if mode=='R' and layer=="m'" else ("mm'" if mode=='R' else ("m'm" if layer=="m'" else 'm2'));target="1/m'" if mode=='R' and layer=="m'" else ("m'/m" if mode=='R' or layer=="m'" else 'm/2');out='-' if mode=='R' else '+';rows=[]
 for sign in ['+','-']:
  for pol,axis in [('p','x'),('s','y'),('p','z')]:
   minus=(axis=='z' and ((mode=='R' and sign=='+') or (mode=='T' and sign=='-')))
   rows.append(tt(t,'',pol)+'L^{'+sign+'}_{'+layer+'/'+layer+','+pol+axis+'}&='+('-' if minus else '')+'L^{'+out+'}_{'+target+','+pol+axis+'}')
 return block(rows)+r'$(n_{m\prime\prime}=n_{'+layer+'})$。'+'\n\n'
body=''
for k,layer in enumerate(["m'",'m']):
 body+='**'+('m′' if k==0 else 'm')+'层内极化产生的和频光：**\n\n'
 if k==0:
  body+='在文件《一般式》的(2.1)—(2.4)式中，使用下列定义：\n\n'+disp(r'a_0=e^{ik_{m\prime}z_1/\cos\theta_{m\prime}},\qquad a_0^*=e^{i\beta_{m\prime}h_{m\prime}/\cos\theta_{m\prime}}e^{-ik_{m\prime}z_1/\cos\theta_{m\prime}}')
  body+='不过，本文由(2.10)—(2.17)式导出(2.27)—(2.30)式时所用的光路，没有考虑某一层内部的多重反射；因而相位部分的处理有欠缺。作者指出，可将指数自变量中h/cosθ及z/cosθ形式的部分分别替换为β×h和β×z来修正。下面列出这样替换后的结果。为简便，取\n\n'+disp(r'a_0=e^{i\beta_{m\prime}z_1},\qquad a_0^*=e^{i\beta_{m\prime}h_{m\prime}}e^{-i\beta_{m\prime}z_1}')+'并和上面同样定义\n\n'
 else:body+='在文件《一般式》的(2.5)—(2.8)式中，使用下列定义：\n\n'+disp(r'b_0=e^{ik_mz_2/\cos\theta_m},\qquad b_0^*=e^{i\beta_mh_m/\cos\theta_m}e^{-ik_mz_2/\cos\theta_m}')
 body+=block([r'P_a^*&=\sum_{\alpha,\beta}\chi_{a\alpha\beta}E^0_{vis,\alpha}E^0_{ir,\beta}']+pumps(layer))
 for mode in ['R','T']:
  num=43+2*k+(1 if mode=='T' else 0);body+='（'+('a' if mode=='R' else 'b')+'）'+('反射' if mode=='R' else '透射')+'方向。\n\n'
  body+='$E^+$ 源的贡献由文件《一般式》的('+('2.1' if k==0 and mode=='R' else '2.2' if k==0 else '2.5' if mode=='R' else '2.6')+')式和本文('+('2.27' if k==0 else '2.29')+')式给出：\n\n'+sourcefield(layer,mode,'+')
  body+='$E^-$ 源的贡献由文件《一般式》的('+('2.3' if k==0 and mode=='R' else '2.4' if k==0 else '2.7' if mode=='R' else '2.8')+')式和本文('+('2.28' if k==0 else '2.30')+')式给出：\n\n'+sourcefield(layer,mode,'-')
  z='z_1' if k==0 else 'z_2';body+='对于由E⁺源产生的和频光，将'+z+'从0积分至该层厚度；对于由E⁻源产生的和频光，从该层厚度积分至0。再利用下列关系整理：\n\n'+lrelations(layer,mode)
  pre='L^-_{1/m\prime}' if mode=='R' and k==0 else ('t_{m2}e^{i(\\beta_{m\prime}h_{m\prime}+\\beta_mh_m)}L^+_{m\prime/m}' if k==0 else ('t_{m\prime1}e^{i\\beta_{m\prime}h_{m\prime}}L^-_{m\prime/m}' if mode=='R' else 'e^{i\\beta_mh_m}L^+_{m/2}'))
  body+=block([('E_1^-(0^-)' if mode=='R' else r'E_2^+(h_{m\prime}+h_m^+)')+r'&=\sum_{\alpha,\beta}'+pre+r'P_a^*\frac{i}{\delta}']+sumrows(layer,mode,'pm'))+'上符号用于x、y分量，下符号用于z分量。因此，\n\n'
  for pol,suffix in [('p','a'),('s','b')]:
   sf=pol;first=('E_{1}^-(0^-)_{'+pol+'}' if mode=='R' else 'E_2^+(h_{m\prime}+h_m^+)_{'+pol+'}')+r'&=\sum_{\alpha,\beta}E^0_{vis,\alpha}E^0_{ir,\beta}'
   if k==0 and mode=='T':first+=tt('m2','SF',pol)+'e^{i('+beta("m'",'SF')+"h_{m'}+"+beta('m','SF')+'h_m)}'
   if k==1 and mode=='R':first+=tt("m'1",'SF',pol)+'e^{i('+beta("m'",'SF')+'+'+beta("m'",'vis')+'+'+beta("m'",'ir')+")h_{m'}}"
   if k==1 and mode=='T':first+='e^{i('+beta("m'",'vis')+'+'+beta("m'",'ir')+")h_{m'}}e^{i"+beta('m','SF')+'h_m}(1+'+rr("1m'",'SF',pol)+rr("m'm",'SF',pol)+ex("m'",'SF')+')'
   else:first+=r'\frac{i}{\delta}'
   rows=[first]+pumps(layer,phase=(k==0))
   target="1/m'" if k==0 and mode=='R' else ("m'/m" if k==0 or mode=='R' else 'm/2');lsign='-' if mode=='R' else '+'
   for c,ax in ([('+','x'),('-','z')] if pol=='p' else [('s','y')]):
    rrrows=sumrows(layer,mode,c)
    if pol=='p' and ax=='z':rrrows[0]=rrrows[0].replace(r'\times',r'+',1)
    rows+=rrrows;rows[-1]+='L^{'+lsign+'}_{'+target+','+pol+ax+r'}\chi_{'+ax+r'\alpha\beta}'
   body+=block(rows,str('2.')+str(num)+suffix)
 body+=note('Q106' if k==0 else 'Q107','PDF '+('25—32' if k==0 else '32—37')+'，体相积分',r'作者在此明确指出前面相位处理的欠缺，并说明替换方式；这属于原文推导说明，未反向修改2.1/2.2的式子。原定义P星号内含求和，而随后又写求和，按原样保留；δ记号、端点方向和各积分分母符号不擅自消去。m体相的最终式中全局因子、层标与通式有差异，按原页保留，未作为已确认理论修正。')
parts=interface+body;P.write_text(old[:a]+parts+old[b:],encoding='utf-8');append(M/'疑难与勘误.md',q)
# Complete, reviewable batches: interface source units, then body source direction groups.
segments=re.split(r'(?=\*\*[^\n]+极化产生的)',parts)
for j,t in enumerate([x for x in segments if x.strip()]):writebatch(183+j,t,list(range(13,38)),'二层系和频场推导与完整展开（按源点组）')
(O/'2.3-重建全文.md').write_text(parts,encoding='utf-8');print('2.3已去重复并补回2.33、2.43—2.46与中间式')

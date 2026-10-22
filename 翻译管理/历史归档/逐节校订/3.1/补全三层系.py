exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
old=P.read_text(encoding='utf-8');assert not (O/'三层系-修订前.md').exists();(O/'三层系-修订前.md').write_text(old,encoding='utf-8');cut=old.index('**3. 三层')
def al(rows):return r'\begin{aligned}&'+r'\\&'.join(rows)+r'\end{aligned}'
def frac(n,d):return r'\frac{'+n+'}{'+d+'}'
def display(rows,tag=None):return '$$\n'+r'\begin{aligned}'+'\n'+r'\\[5pt]'.join(rows)+'\n'+r'\end{aligned}'+('\n'+r'\tag{'+tag+'}' if tag else '')+'\n$$\n\n'
def sy(f,a):
 rr=lambda ij:'r_{'+ij+','+f+','+a+'}';tt=lambda ij:'t_{'+ij+','+f+','+a+'}';be=lambda l:r'\beta_{'+l+','+f+'}';h=lambda l:'h_{'+l+'}';e=lambda l:'e^{2i'+be(l)+h(l)+'}'
 A,B,C,D=[rr(x) for x in ["1m'","m'm","mm''","m''2"]];X,Y,Z=[e(l) for l in ["m'","m","m''"]]
 den=al(['(1+'+A+B+X+')(1+'+C+D+Z+')','+('+B+'+'+A+X+')('+C+'+'+D+Z+')'+Y])
 front=al(['(1+'+B+X+')(1+'+C+D+Z+')','+('+B+'+'+X+')('+C+'+'+D+Z+')'+Y])
 refl=al(['(1+'+C+D+Z+')','+('+C+'+'+D+Z+')'+Y])
 return rr,tt,be,h,e,den,front,refl
def pref(index,f,a):
 rr,tt,be,h,e,den,front,refl=sy(f,a);B=rr("m'm");C=rr("mm''");D=rr("m''2");Y=e('m');Z=e("m''");ep='e^{i'+be("m'")+h("m'")+'}';ep2='e^{i('+be("m'")+h("m'")+'+'+be('m')+h('m')+')}';ep3='e^{i('+be("m''")+h("m''")+'+'+be('m')+h('m')+'+'+be("m'")+h("m'")+')}';t1=tt("1m'");t2=tt("m'm");t3=tt("mm''");t4=tt("m''2")
 nums={1:'(1+'+rr("1m'")+e("m'")+')['+front+']',2:t1+'['+front+']',3:t1+t2+t3+t4+ep3,4:t1+t2+t3+'(1+'+D+')'+ep3,5:t1+ep+'(1+'+B+')['+refl+']',6:t1+ep+'(1+'+B+')['+refl+']',7:t1+t2+ep+'['+refl+']',8:t1+t2+ep+'['+refl+']',9:t1+t2+ep2+'(1+'+C+')(1+'+D+Z+')',10:t1+t2+ep2+'(1+'+C+')(1+'+D+Z+')',11:t1+t2+t3+ep2+'(1+'+D+Z+')',12:t1+t2+t3+ep2+'(1+'+D+Z+')',13:t1,14:t1,15:t1+t2+ep,16:t1+t2+ep,17:t1+t2+t3+ep2,18:t1+t2+t3+ep2}
 return frac(nums[index],den)
def localterm(index,f,a,sgn):
 rr,tt,be,h,e,den,front,refl=sy(f,a);B=rr("m'm");C=rr("mm''");D=rr("m''2");Y=e('m');Z=e("m''");sign='+' if sgn=='+' else '-';z='z_1' if index<=14 else ('z_2' if index<=16 else 'z_3');layer="m'" if index<=14 else ('m' if index<=16 else "m''")
 # These literal parentheses and the m-SF label in the m′/vis branch follow the printed page.
 thSF='m' if index<=14 and f=='vis' else layer
 def ex(s):return r'\exp[i'+z+'(k_{'+layer+','+f+r'}\cos\theta_{'+layer+','+f+'}('+s+sign+r'\tan\theta_{'+thSF+r',SF}\tan\theta_{'+layer+','+f+'})]'
 if index<=14:
  fw=al(['(1+'+C+D+Z+')','+'+B+'('+C+'+'+D+Z+')'+Y]);bw=al([B+'(1+'+C+D+Z+')','+('+C+'+'+D+Z+')'+Y])
 elif index<=16:fw='(1+'+C+D+Z+')';bw='('+C+'+'+D+Z+')'+Y
 else:fw='1';bw=D+'e^{2i('+be('m')+h('m')+'+'+be("m''")+h("m''")+')}'
 return [r'&\quad\times\{'+fw+ex('1'),r'&\qquad+'+bw+ex('-1')+r'\}']
positions=['0^-','0^+',"h_{m'}+h_m+h_{m''}^+","h_{m'}+h_m+h_{m''}^-","h_{m'}^-","h_{m'}^-","h_{m'}^+","h_{m'}^+","h_m+h_{m'}^-","h_m+h_{m'}^-","h_m+h_{m'}^+","h_m+h_{m'}^+",'z_1','z_1',"h_{m'}+z_2","h_{m'}+z_2","h_{m'}+h_m+z_3","h_{m'}+h_m+z_3"]
path=r'(h_m\tan\theta_{m,SF}+h_{m\prime}\tan\theta_{m\prime,SF}+h_{m\prime\prime}\tan\theta_{m\prime\prime,SF})'
wave=r'(-k_{m,ir}\sin\theta_{m,ir}-k_{m,vis}\sin\theta_{m,vis})'
def equations(index,polar=False):
 tag='3.'+str(index+18 if polar else index);pos=positions[index-1];first=('P_a^*('+pos+')' if polar else 'E_{vis,\\alpha}('+pos+')E_{ir,\\beta}('+pos+')')+r'&='+ (r'\sum_{\alpha,\beta}\chi_{a\alpha\beta}' if polar else '')+r'E^0_{vis,\alpha}E^0_{ir,\beta}'
 rows=[first]
 for f,a in [('vis',r'\alpha'),('ir',r'\beta')]:rows.append(r'&\quad\times'+pref(index,f,a))
 if index>=13:
  for f,a in [('vis',r'\alpha'),('ir',r'\beta')]:rows+=localterm(index,f,a,'+' if index%2 else '-')
 if not polar:
  if 5<=index<=12:
   # Original local path differences are not unified across source classes.
   loc={5:r'(h_m\tan\theta_{m,SF}+h_{m\prime\prime}\tan\theta_{m\prime\prime,SF})',6:r'h_{m\prime}\tan\theta_{m\prime,SF}',7:r'(h_m\tan\theta_{m,SF}+h_{m\prime\prime}\tan\theta_{m\prime\prime,SF})',8:r'h_{m\prime}\tan\theta_{m\prime,SF}',9:r'h_{m\prime}\tan\theta_{m\prime,SF}',10:r'(h_m\tan\theta_{m,SF}+h_{m\prime}\tan\theta_{m\prime,SF})',11:r'h_{m\prime}\tan\theta_{m\prime,SF}',12:r'(h_m\tan\theta_{m,SF}+h_{m\prime}\tan\theta_{m\prime,SF})'}[index]
   rows.append(r'&\quad\times\exp[i'+loc+wave+']')
  factor='i2n' if index in [1,2,6,8,10,12,14,16,18] else ('i(2n+2)' if index>=13 else 'i(2n+1)')
  rows.append(r'&\quad\times\exp['+factor+path+r'\\&\qquad\times'+wave+']')
 return display(rows,tag)
head='''## 3. 三层系（1/m′/m/m″/2）产生的和频光

如开篇所述，为求出这一体系产生的和频电场，需要求张量等比级数之和。因此，以作者当时的能力尚不能完成直至最终表达式的计算。不过，可以求出极化，下面将其列出。

若三个膜层中某一层的厚度可以忽略，则在第2部分所得结果中，(1)把极化表达式替换为下面给出的式子，(2)按下述方式替换与该层外侧界面有关的反射系数和透射系数，即可得到所需表达式。

**当两层m与m′之间夹有厚度可忽略的m″层，形成m/m″/m′系时，作如下替换：**

'''
head+=display([r'r_{mm\prime}&\Rightarrow\frac{r_{mm\prime\prime}+r_{m\prime\prime m\prime}}{1+r_{mm\prime\prime}r_{m\prime\prime m\prime}},\qquad t_{mm\prime}\Rightarrow\frac{t_{mm\prime\prime}t_{m\prime\prime m\prime}}{1+r_{mm\prime\prime}r_{m\prime\prime m\prime}}',r'r_{m\prime m}&\Rightarrow\frac{r_{m\prime m\prime\prime}+r_{m\prime\prime m}}{1+r_{m\prime m\prime\prime}r_{m\prime\prime m}},\qquad t_{m\prime m}\Rightarrow\frac{t_{m\prime m\prime\prime}t_{m\prime\prime m}}{1+r_{m\prime m\prime\prime}r_{m\prime\prime m}}'])
head+='### 3.1 电场振幅的乘积\n\n'
titles={1:'1/m′界面的1侧',2:'1/m′界面的m′侧',3:'m″/2界面的2侧',4:'m″/2界面的m″侧',5:'m′/m界面的m′侧',7:'m′/m界面的m侧',9:'m/m″界面的m侧',11:'m/m″界面的m″侧',13:'m′层中深度z1处',15:'m层中距m′/m界面深度z2处',17:'m″层中距m/m″界面深度z3处'}
field=[];pol=[]
for i in range(1,19):
 title='**'+titles[i]+'：**\n\n' if i in titles else ''
 source=('$E^+$ 源（经反射和透射）与 $E^-$ 源（$n=0$ 时）。\n\n' if i==1 else ('$E^+$ 源与 $E^-$ 源（经反射和透射）。\n\n' if i in [2,5,7,9,11,13,15,17] else '$E^+$ 源（经反射和透射）与 $E^-$ 源。\n\n'))
 field.append(title+source+equations(i));pol.append(title+source+equations(i,True))
q=note('Q110','PDF p38—51，三层系公式',r'3.1及3.19最前端的反射因子含传播指数，原式照录。内部源点正反两类的局部路径相位不同（如3.5/3.6、3.7/3.8），不统一；3.13/3.14与3.31/3.32中m′层vis支角标局部写m,SF，仍保留。体相指数内可见额外左圆括号且未闭合，按原符号保留；m″体相反射项指数还含βmhm项，不删除。以上均为原式记号/分组疑点，候选为按各层传播及配对括号统一，尚未采用。')
polintro='### 3.2 和频极化\n\n将上面求得的电场乘积乘以和频过程的二阶非线性极化率，即得到和频极化。再往后的计算极为复杂；作者认为，只有在某一层无限薄时，才可能求得表达式。\n\n'
# Batches follow complete source-point pairs, including all cross-page continuations.
allparts=[head]+field+[polintro]+pol+[q];third=''.join(allparts);P.write_text(old[:cut]+third,encoding='utf-8')
num=210
for j in range(0,18,2):
 text=(head if j==0 else '')+''.join(field[j:j+2]);writebatch(num,text,[38+j//2, min(45,39+j//2)],'三层系场乘积3.'+str(j+1)+'—3.'+str(j+2));num+=1
for j in range(0,18,2):
 text=(polintro if j==0 else '')+''.join(pol[j:j+2])+(q if j==16 else '');writebatch(num,text,[45+j//3,min(51,46+j//3)],'三层系和频极化3.'+str(j+19)+'—3.'+str(j+20));num+=1
append(M/'疑难与勘误.md',q);print('三层系36个编号式已完整展开；旧译省略和自造D简写已移除')

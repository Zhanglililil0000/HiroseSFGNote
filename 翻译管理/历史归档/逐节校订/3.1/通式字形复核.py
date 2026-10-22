exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
for f in [P,O/'B189-本批译文.md',O/'B190-本批译文.md']:
 s=f.read_text(encoding='utf-8')
 def change(z):
  t=z[1]
  if r'\tag{' in t or r'\delta' not in t:return z[0]
  if r'L^-_{1/m\prime}' in t:
   # p27 places the final backward integral after the printed right square bracket.
   i=t.rfind(r'\frac{e^');j=t.rfind(r'\bigr]')
   if 0<i<j:t=t[:j]+t[j:].replace(r'\bigr]','',1);t=t[:i]+r'\bigr]'+t[i:]
  if r'L^-_{m\prime/m}' in t:
   a=r'\beta_{m,SF}+\beta_{m,vis}-\beta_{m,ir}';b=r'\beta_{m,SF}+\beta_{m,vis}\beta_{m,ir}';pair=r'\frac{e^{i('+a+r')h_{m}}-1}{'+a+'}';t=t.replace(pair,r'\frac{e^{i('+a+r')h_{m}}-1}{'+b+'}')
  if r'L^+_{m/2}' in t:t=t.replace(r'\pm',r'\mathord{m}')
  return '$$'+t+'$$'
 s=re.sub(r'\$\$([\s\S]*?)\$\$',change,s);f.write_text(s,encoding='utf-8')
q=note('Q112','PDF p27、p33、p35—36，无编号积分通式',r'p27最后一项的右方括号印在最后一个积分分式之前，此处按原位置保留；候选为移到该分式之后。p33的局部积分分母有vis与ir相乘字形，关联Q111。p35—36无编号通式的成对项之间为可见m字形，照录为m；候选为上下符号∓，不能据末尾分量式静默改写成±。这些通式与随后的分量式仍分别保留原值，均未采用原文修正。')
s=P.read_text(encoding='utf-8').replace('## 3. 三层系',q+'## 3. 三层系',1);P.write_text(s,encoding='utf-8');append(M/'疑难与勘误.md',q)
print('unconfirmed printed bracket/sign variants retained')

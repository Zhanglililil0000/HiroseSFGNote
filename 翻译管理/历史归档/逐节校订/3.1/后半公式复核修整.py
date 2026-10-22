exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
# Repairs to generated typesetting, plus explicit restoration of locally anomalous printed terms.
files=[P]+[O/f'B{n}-本批译文.md' for n in range(183,228) if (O/f'B{n}-本批译文.md').exists()]
for f in files:
 s=f.read_text(encoding='utf-8').replace(r'\pmr',r'\pm r')
 def eq(m):
  t=m[1];z=re.search(r'\\tag\{([^}]+)\}',t)
  if not z:return m[0]
  tag=z[1]
  if tag in ['2.45a','2.45b']:
   t=t.replace(r'\beta_{m,SF}+\beta_{m,vis}-\beta_{m,ir}',r'\beta_{m,SF}+\beta_{m,vis}\beta_{m,ir}')
   if tag=='2.45a':t=t.replace(r'&\quad+\{',r'&\quad\times\{',1)
  if tag=='2.46b':
   # The last printed direct contribution has an additional m′-SF round-trip factor.
   mark=r'(1+r_{1m\prime,SF,s}r_{m\prime m,SF,s}e^{2i\beta_{m\prime,SF}h_{m\prime}})'
   alt="(1+r_{1m',SF,s}r_{m'm,SF,s}e^{2i\\beta_{m',SF}h_{m'}})"
   pos=t.rfind(alt)
   if pos>=0:t=t[:pos]+r'e^{2i\beta_{m\prime,SF}h_{m\prime}}'+t[pos:]
  if tag.startswith(('2.43','2.44','2.45','2.46')):
   layer=r'm\prime' if tag.startswith(('2.43','2.44')) else 'm'
   if r'\quad(n_' not in t:t=t.replace(r'\tag{'+tag+'}',r'\quad(n_{m\prime\prime}=n_{'+layer+r'})\tag{'+tag+'}')
  return '$$\n'+t.strip()+'\n$$'
 s=re.sub(r'\$\$([\s\S]*?)\$\$',eq,s)
 f.write_text(s,encoding='utf-8')
q=note('Q111','PDF p33—37，式2.45—2.46',r'2.45的部分积分分母印为βm,SF+βm,visβm,ir，中间未见加减号，按乘积字形保留；候选为补减号。2.45a的z支前印乘号而非加号，2.46b最后一项的直接贡献多一层m′的SF往返指数，均照录。2.46a/b原页前因子未显式列i/δ，与前一无编号通式不同；不自动补入，候选须结合归一化核验。')
s=P.read_text(encoding='utf-8');s=s.replace('## 3. 三层系',q+'## 3. 三层系',1);P.write_text(s,encoding='utf-8');append(M/'疑难与勘误.md',q)
print('typesetting and printed anomalies recorded')

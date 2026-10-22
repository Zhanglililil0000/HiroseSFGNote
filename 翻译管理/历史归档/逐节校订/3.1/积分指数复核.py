exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
files=[P]+[f for f in O.glob('B*-本批译文.md') if int(f.name[1:4])>=183]
for f in files:
 s=f.read_text(encoding='utf-8')
 def fix(z):
  t=z[1];tag=re.search(r'\\tag\{([^}]+)\}',t)
  if tag and tag[1] in ['2.45a','2.45b']:
   bad=r'\beta_{m,SF}+\beta_{m,vis}\beta_{m,ir}';good=r'\beta_{m,SF}+\beta_{m,vis}-\beta_{m,ir}';t=t.replace(bad,good)
   pair=r'\frac{e^{i('+good+r')h_{m}}-1}{'+good+'}'
   t=t.replace(pair,r'\frac{e^{i('+good+r')h_{m}}-1}{'+bad+'}')
  return '$$'+t+'$$'
 s=re.sub(r'\$\$([\s\S]*?)\$\$',fix,s);f.write_text(s,encoding='utf-8')
print('integration numerator signs preserved; only printed anomalous denominator retained')

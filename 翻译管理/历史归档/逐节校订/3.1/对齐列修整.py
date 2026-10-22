exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
files=[P]+[f for f in O.glob('B*-本批译文.md') if int(f.name[1:4])>=178]
for f in files:
 s=f.read_text(encoding='utf-8')
 def change(z):
  t=z[1];head='\\begin{aligned}';i=t.find(head)
  if i<0:return z[0]
  start=i+len(head);first=t[start:].lstrip();off=start+len(t[start:])-len(first)
  if first.startswith('&'):return z[0]
  j=t.find('&=',off)
  if j>=0:t=t[:j]+r'\\ &='+t[j+2:];t=t[:off]+'&'+t[off:]
  # Separating x and z contributions into rows preserves the printed bracket scope.
  t=t.replace(r'\chi_{x\alpha\beta}',r'\chi_{x\alpha\beta}')
  t=re.sub(r'(\\chi_\{x\\alpha\\beta\}\s*)\n?\s*\+\s*',lambda q:q[1]+r'\\&\quad+ ',t)
  return '$$'+t+'$$'
 s=re.sub(r'\$\$([\s\S]*?)\$\$',change,s);f.write_text(s,encoding='utf-8')
print('left-hand fields moved to shared alignment column')

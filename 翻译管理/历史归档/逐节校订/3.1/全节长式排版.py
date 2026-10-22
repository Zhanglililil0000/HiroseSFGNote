exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
bs=chr(92)
tree=ast.parse((M/'校订记录/2.6/长式排版.py').read_text(encoding='utf-8'))
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('topsplit','wrapsum','groups','braceend','fractions')],type_ignores=[]),'layout-functions','exec'))
def fmt(t):
 t=t.strip()
 # Fixed delimiters may span aligned rows; preserve the visible signs.
 t=t.replace(r'\left.','').replace(r'\right.','').replace(r'\left','').replace(r'\right','')
 t=fractions(t)
 if not t.startswith(r'\begin{aligned}'):
  # Put separate top-level multiplicative factors on separate rows.
  tag=re.search(r'\\tag\{[^}]+\}',t);mark=tag[0] if tag else '';t=t.replace(mark,'')
  rows=[];brace=0;i=0;start=0
  while i<len(t):
   if t[i]=='{':brace+=1
   elif t[i]=='}':brace-=1
   if brace==0 and t.startswith(r'\times',i):rows.append(t[start:i]);start=i
   i+=1
  rows.append(t[start:]);out=[]
  for j,x in enumerate(rows):
   if j==0 and '=' in x:x=x.replace('=',r'&=',1)
   else:x='&'+x
   out.append(x)
  t=r'\begin{aligned}'+'\n'+r'\\[4pt]'.join(out)+'\n'+r'\end{aligned}'+mark
 # A few integration brackets contain two long fractions; split the pair at +/-.
 t=t.replace(r'\pm r',r'\\&\qquad\pm r')
 return '$$\n'+t+'\n$$'
files=[P]+[f for f in O.glob('B*-本批译文.md') if int(f.name[1:4])>=178]
for f in files:
 s=f.read_text(encoding='utf-8');start=s.index('**m/2 界面的 m 侧：**',s.index('### 2.2 和频极化')) if f==P else 0
 head=s[:start];tail=s[start:];tail=re.sub(r'\$\$([\s\S]*?)\$\$',lambda z:fmt(z[1]),tail);f.write_text(head+tail,encoding='utf-8')
print('all remaining long equations regrouped without shortening')

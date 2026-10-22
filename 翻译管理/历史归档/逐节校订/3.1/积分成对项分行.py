exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
def rowfix(row):
 if row.count(r'\frac')<2:return row
 brace=par=0;cuts=[];first=row.find(r'\frac')
 for i,c in enumerate(row):
  if c=='{':brace+=1
  elif c=='}':brace-=1
  elif brace==0:
   if c=='(':par+=1
   elif c==')':par-=1
   elif c in '+-' and par==0 and i>first+40 and r'\frac' in row[i:] and row[i-1]!='^':cuts.append(i)
 if not cuts:return row
 for i in reversed(cuts):row=row[:i]+r'\\ &\qquad'+row[i:]
 return row
for f in [P,O/'B189-本批译文.md',O/'B190-本批译文.md']:
 s=f.read_text(encoding='utf-8')
 def change(z):
  t=z[1]
  if r'\tag{2.46' not in t:return z[0]
  t=r'\\[5pt]'.join(rowfix(x) for x in t.split(r'\\[5pt]'))
  return '$$'+t+'$$'
 s=re.sub(r'\$\$([\s\S]*?)\$\$',change,s);f.write_text(s,encoding='utf-8')
print('paired integration terms placed on separate rows')

from pathlib import Path
import re
O=Path(__file__).resolve().parent;R=O.parents[2];P=next((R/'中文版本/第二章 薄膜产生的SFG').glob('2.6 *.md'));bs=chr(92)
def topsplit(s,chars):
 brace=par=sq=0;cuts=[]
 for i,c in enumerate(s):
  if c=='{':brace+=1
  elif c=='}':brace-=1
  elif brace==0:
   if c=='(':par+=1
   elif c==')':par-=1
   elif c=='[':sq+=1
   elif c==']':sq-=1
   elif c in chars and par==sq==0 and i>0 and s[i-1]!='^':cuts.append(i)
 return cuts
def wrapsum(s):
 cuts=topsplit(s,'+-')
 if len(s)<170 or not cuts:return s
 chunks=[];start=0
 for k in cuts:chunks.append(s[start:k].strip());start=k
 chunks.append(s[start:].strip())
 return '{'+bs+'begin{aligned}&'+(bs*2+'&').join(chunks)+bs+'end{aligned}}'
def groups(s):
 # Parenthesis/square-bracket contents can contain long sums even when multiplied outside.
 result='';i=0;curly=0
 while i<len(s):
  c=s[i]
  if c=='{':curly+=1
  if c=='}':curly-=1
  if c in '([' and curly==0 and not (i>0 and s[i-1]==bs):
   end=')' if c=='(' else ']';depth=1;j=i+1;br=0
   while j<len(s):
    if s[j]=='{':br+=1
    elif s[j]=='}':br-=1
    elif br==0:
     if s[j]==c:depth+=1
     elif s[j]==end:
      depth-=1
      if depth==0:break
    j+=1
   if j<len(s):result+=c+wrapsum(groups(s[i+1:j]))+end;i=j+1;continue
  result+=c;i+=1
 return result
def braceend(s,i):
 assert s[i]=='{';d=1;j=i+1
 while j<len(s):
  if s[j]=='{':d+=1
  elif s[j]=='}':
   d-=1
   if not d:return j
  j+=1
 raise ValueError('unclosed TeX group')
def fractions(s):
 out='';i=0
 while i<len(s):
  if s.startswith(bs+'frac{',i) or s.startswith(bs+'dfrac{',i):
   a=s.index('{',i);z=braceend(s,a)
   if z+1<len(s) and s[z+1]=='{':
    end=braceend(s,z+1);num=s[a+1:z];den=s[z+2:end]
    out+=s[i:a+1]+wrapsum(groups(num))+'}{'+wrapsum(groups(den))+'}';i=end+1;continue
  out+=s[i];i+=1
 return out
def formatmath(t):
 tag=re.search(re.escape(bs)+r'tag\{([^}]+)\}',t)
 if not tag:return t
 tag=tag[1]
 # Correct only the extra third prime introduced while transcribing a distinct occurrence.
 if tag=='4.18a':
  loc=t.rfind("r_{mm'''}")
  if t.count("r_{mm'''}")==2:t=t[:loc]+t[loc:].replace("r_{mm'''}","r_{mm''}",1)
 # Fixed-size unmatched brackets reproduce the original marks without assigning a candidate scope.
 if tag=='4.20b':t=t.replace("(1 + r_{m'm})[","(1 + r_{m'm})"+bs+'mathopen{[}',1).replace("(1 - r_{m'm})][","(1 - r_{m'm})"+bs+'mathclose{]}[',1)
 if tag=='4.25b':t=t.replace("\n[(1 + r_{1m'})","\n"+bs+"mathopen{[}(1 + r_{1m'})",1).replace("\n[(1 - r_{1m'})","\n"+bs+"mathopen{[}(1 - r_{1m'})",1)
 # Transform coefficients and each matrix entry independently; no formula term is omitted.
 t=fractions(t)
 def matrix(m):
  content=m[1];rows=re.split(r'\\\\(?:\[[^]]+\])?',content);rr=[]
  for row in rows:rr.append(' & '.join(wrapsum(groups(cell.strip())) for cell in row.split('&')))
  return bs+'begin{bmatrix}'+(bs*2+'[6pt]\n').join(rr)+bs+'end{bmatrix}'
 t=re.sub(re.escape(bs)+r'begin\{bmatrix\}([\s\S]*?)'+re.escape(bs)+r'end\{bmatrix\}',matrix,t)
 # Long standalone equalities: place each equality and final matrix product on its own line.
 if bs+'begin{aligned}' not in t:
  cuts=topsplit(t,'=')
  if cuts:
   text=t[:cuts[0]]+'&'+t[cuts[0]:]
   # Subsequent equal signs share the same aligned column.
   off=cuts[0]+1
   for cut in reversed(cuts[1:]):text=text[:cut+1]+bs*2+'\n&'+text[cut+1:]
   text=re.sub(r'\n\s*'+re.escape(bs)+r'times\s*'+re.escape(bs)+r'begin\{bmatrix\}',lambda m:bs*2+'\n&'+bs+'quad'+bs+'times '+bs+'begin{bmatrix}',text)
   t=bs+'begin{aligned}\n'+text.strip()+'\n'+bs+'end{aligned}'
 # When scalar wrapping introduced a nested aligned block, a larger equation still needs an outer alignment.
 elif not t.strip().startswith(bs+'begin{aligned}'):
  mark=bs+'tag{'+tag+'}';t=t.replace(mark,'');cuts=topsplit(t,'=')
  if cuts:
   i=cuts[0];t=t[:i]+'&'+t[i:]
   t=re.sub(r'\n\s*'+re.escape(bs)+r'times\s*'+re.escape(bs)+r'begin\{bmatrix\}',lambda m:bs*2+'\n&'+bs+'quad'+bs+'times '+bs+'begin{bmatrix}',t)
   # Coefficient immediately followed by a column vector, without an explicit multiplication sign.
   t=re.sub(r'}\s*\n'+re.escape(bs)+r'begin\{bmatrix\}',lambda m:'}'+bs*2+'\n&'+bs+'quad'+bs+'times '+bs+'begin{bmatrix}',t)
   t=bs+'begin{aligned}\n'+t.strip()+'\n'+bs+'end{aligned}'+mark
 return t
for f in [P]+[O/f'B{n}-本批译文.md' for n in range(151,163)]:
 s=f.read_text(encoding='utf-8');start=s.index('在和频过程中，需要求出的是电场振幅。') if f==P else 0
 head=s[:start];tail=s[start:];tail=re.sub(r'\$\$([\s\S]*?)\$\$',lambda m:'$$\n'+formatmath(m[1])+'\n$$',tail);f.write_text(head+tail,encoding='utf-8')
print('long expressions reformatted without abbreviations')

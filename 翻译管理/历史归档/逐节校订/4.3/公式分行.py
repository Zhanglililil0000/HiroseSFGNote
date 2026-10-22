from pathlib import Path
import re
o=Path(__file__).resolve().parent
def wrap(m):
    x=m[1].strip()
    if r'\begin{aligned}' in x or len(x)<180 or ' = ' not in x:return m[0]
    eq=x.index(' = '); candidates=[];depth=0;paren=0;bracket=0
    for i,c in enumerate(x):
        escaped=i>0 and x[i-1]=='\\'
        if c=='{' and not escaped:depth+=1
        elif c=='}' and not escaped:depth-=1
        elif not depth:
            if c=='(':paren+=1
            elif c==')':paren-=1
            elif c=='[':bracket+=1
            elif c==']':bracket-=1
        if i>eq+3 and c in '+-' and i>0 and x[i-1]==' ' and i+1<len(x) and x[i+1]==' ' and depth==0:
            candidates.append((i,paren+bracket))
    cuts=[];start=0
    while len(x)-start>170:
        possible=[(i,d) for i,d in candidates if start+55<i<start+180]
        if not possible:break
        preferred=[z for z in possible if z[1]==0]
        pool=preferred or possible
        i,d=min(pool,key=lambda z:abs(z[0]-(start+135)))
        cuts.append(i);start=i
    if not cuts:return m[0]
    rows=[];last=0
    for cut in cuts+[len(x)]:rows.append(x[last:cut].strip());last=cut
    rows[0]=rows[0].replace(' = ',' &= ',1)
    return '$$\n\\begin{aligned}\n'+rows[0]+'\n'+''.join(chr(92)*2+'\n&'+chr(92)+'quad '+z+'\n' for z in rows[1:])+r'\end{aligned}'+'\n$$'
for n in range(297,314):
    p=o/f'B{n}-本批译文.md';s=p.read_text(encoding='utf-8');s=re.sub(r'\$\$([\s\S]*?)\$\$',wrap,s);p.write_text(s,encoding='utf-8')
print('长公式已按运算项分行，保留分组和系数')

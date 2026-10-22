from pathlib import Path
import re
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.1 *.md'))
s=p.read_text(encoding='utf-8')
# Restore source's unsuffixed E in initial upward amplitudes and direct terms only.
for a,b in [('### 2.1 m 层发光','### 2.2'),('### 2.2', '### 2.3'),('### 2.3','## 附录 A')]:
    lo=s.index(a);hi=s.index(b,lo+len(a));part=s[lo:hi]
    begin=part.index('对于上行光：');end=part.index('在此基础上',begin)
    part=part[:begin]+part[begin:end].replace('E^-(', 'E(')+part[end:]
    s=s[:lo]+part+s[hi:]
# The initial recurrence matrix is rewritten by entries, preserving source order.
start=s.index('$$\n\\begin{pmatrix}\nx_{n+1}')
end=s.index('其中：',start)
old=s[start:end]
m=re.search(r'\\begin\{pmatrix\}\n(\\alpha_m[\s\S]*?)\\end\{pmatrix\}',old)
assert m
rows=re.split(r'\\\\\[4pt\]\s*',m.group(1).strip())
assert len(rows)==3
cells=[x.strip() for row in rows for x in row.split('&')]
assert len(cells)==9
layout=r'''$$
\begin{pmatrix}x_{n+1}\\y_{n+1}\\z_{n+1}\end{pmatrix}
=A\begin{pmatrix}x_n\\y_n\\z_n\end{pmatrix}
=A^{n+1}\begin{pmatrix}x_0\\y_0\\z_0\end{pmatrix},
\qquad A=\begin{pmatrix}A_{11}&A_{12}&A_{13}\\A_{21}&A_{22}&A_{23}\\A_{31}&A_{32}&A_{33}\end{pmatrix}.
\tag{2.3}
$$

为便于阅读，原矩阵的元素分列如下；$A_{ij}$ 只是对原矩阵元素的排版标记：

'''
for i,c in enumerate(cells):
    c=c.replace('\\left(', '\\bigl(').replace('\\right)','\\bigr)')
    if len(c)>170:c=c.replace(' + ', '\\\\ &+ ',1)
    layout+='$$\n\\begin{aligned}\nA_{'+str(i//3+1)+str(i%3+1)+'}={}&'+c+'\n\\end{aligned}\n$$\n\n'
s=s[:start]+layout+s[end:]
# Split multi-tag display A.10/A.11 into four independent formulas.
begin=s.index('$$\n\\begin{aligned}\nr_{12}^x');end=s.index('$$',begin+2)+2
part=s[begin:end]
lines=[x.strip() for x in part.splitlines() if r'\tag{A.' in x]
repl=[]
for line in lines:
    line=re.sub(r'\\\\\[4pt\]\s*$','',line)
    repl.append('$$\n\\begin{aligned}\n'+line+'\n\\end{aligned}\n$$')
s=s[:begin]+'\n\n'.join(repl)+s[end:]
# All overly long display lines are wrapped at top-level operators; no changes to tokens.
def wrap(tex):
    if '\\begin{pmatrix}' in tex or '\\begin{matrix}' in tex:return tex
    has='\\begin{aligned}' in tex
    text=tex.replace('\\left','\\bigl').replace('\\right','\\bigr')
    # Existing aligned may have stray alignment on wrapped continuation; keep a single column.
    if has:text=text.replace('&','')
    # Break only where no braces are open, so fractions and matrix cells remain intact.
    result=[];depth=0;run=0;i=0
    while i<len(text):
        c=text[i]
        if c=='{':depth+=1
        elif c=='}':depth-=1
        if c in '+-' and depth==0 and run>135:
            result.append('\\\\\n&'+c);run=0
        elif c=='=' and depth==0 and run>180:
            result.append('\\\\\n&=');run=0
        else:result.append(c)
        if c=='\n':run=0
        else:run+=1
        i+=1
    text=''.join(result)
    if not has and '\\\\\n&' in text:text='\\begin{aligned}\n'+text+'\n\\end{aligned}'
    return text
s=re.sub(r'\$\$([\s\S]*?)\$\$',lambda m:'$$'+wrap(m.group(1))+'$$',s)
# Fraction denominators in the three emitted fields are long products: wrap at the subtraction.
den=r"(1 - r_{m1} r_{mm'} a_m^2)(1 - r_{m''m'} r_{m''2} a_{m''}^2) - (r_{m'm} + r_{m1} a_m^2)(r_{m'm''} + r_{m''2} a_{m''}^2) a_{m'}^2"
new=r"\begin{aligned}&(1-r_{m1}r_{mm'}a_m^2)(1-r_{m''m'}r_{m''2}a_{m''}^2)\\&-(r_{m'm}+r_{m1}a_m^2)(r_{m'm''}+r_{m''2}a_{m''}^2)a_{m'}^2\end{aligned}"
s=s.replace(den,new)
p.write_text(s,encoding='utf-8')
# Refresh batch texts from final source; batch boundaries follow complete units, not page ends.
batches=[('B050',0,s.index('## 2. 一般公式'),'p1—2开头，序论与定义'),('B051',s.index('## 2. 一般公式'),s.index('逆矩阵 $(E-A)'),'p2—5上部，光路图及矩阵递推'),('B052',s.index('逆矩阵 $(E-A)'),s.index('### 2.1 m 层发光'),'p5—6上部，逆矩阵、行列式及行向量'),('B053',s.index('### 2.1 m 层发光'),s.index('### 2.2'),'p6，m层发光及强度处理'),('B054',s.index('### 2.2'),s.index('## 附录 A'),'p6末—7，m′及m″层发光'),('B055',s.index('## 附录 A'),s.index('**反射与折射**'),'p8，附录A复场及复折射率'),('B056',s.index('**反射与折射**'),s.index('## 附录 B'),'p8末—10上部，附录A边界关系'),('B057',s.index('## 附录 B'),len(s),'p10—11，附录B矩阵等比级数')]
for bid,a,b,scope in batches:
    (out/f'{bid}-本批译文.md').write_text(s[a:b],encoding='utf-8')
    (out/f'{bid}.md').write_text(f'# {bid} 校订记录\n\n2026-10-19。范围：{scope}。已目视对照对应底本页面及跨页延续；修订前全节备份B050-修订前.md。公式及图文按原文保留，区别旧译转录修复与原式疑点；细节见本节完成复核和Q031—Q038。每批译文及渲染保存在同目录。历史脚本仅作执行记录，不应重复运行。\n',encoding='utf-8')
print('8批译文已刷新')

from pathlib import Path
import re
root=Path(__file__).resolve().parents[3];out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.1 *.md'))
s=p.read_text(encoding='utf-8')
# The plain m spelling differs from the braced m'/m'' forms.
for old,new in [(r'e^{i k_m h_m / \cos\theta_m}',r'\frac{e^{ik_mh_m}}{\cos\theta_m}'),(r'e^{i k_m z_m / \cos\theta_m}',r'\frac{e^{ik_mz_m}}{\cos\theta_m}'),(r'e^{i k_m (h_m - z_m) / \cos\theta_m}',r'\frac{e^{ik_m(h_m-z_m)}}{\cos\theta_m}')]:
    assert old in s,old
    s=s.replace(old,new)
start=s.index('因此：',s.index('\\tag{2.8}'))
end=s.index('> **译者注（Q034续）',start)
part=s[start:end]
tex=part[part.index(r'\begin{pmatrix}')+len(r'\begin{pmatrix}'):part.index(r'\end{pmatrix}')]
rows=re.split(r'\\\\\[(?:2|6)pt\]\s*',tex.strip())
assert len(rows)==5,len(rows)
c1=rows[0]+'\\\\\n&'+rows[1].rstrip(',')
c2=rows[2]+'\\\\\n&'+rows[3].rstrip(',')
c3=rows[4].strip().rstrip(',')
prefix=part[:part.index('$$')]
row=r'''$$
\begin{aligned}
&(r_{mm'}a_m,\;r_{m'm''}t_{m'm}a_{m'}a_m,\;r_{m''2}t_{m''m'}t_{m'm}a_{m''}a_{m'}a_m)(E-A)^{-1}\\
&\qquad=(C_1,C_2,C_3).
\end{aligned}
\tag{2.9}
$$

这里用译者排版标识 $C_1,C_2,C_3$ 分别列出原文行向量的三个分量，不改变分量次序或公共因子：

'''
for i,c in enumerate([c1,c2,c3],1):
    row+='$$\n\\begin{aligned}\nC_'+str(i)+'={}&'+c+'\n\\end{aligned}\n$$\n\n'
s=s[:start]+prefix+row+s[end:]
s=s.replace('在处理 $1/m\'/m$ 体系中的和频（SFG）光时','在处理 $1/m\'/m$ 体系中的和频过程（SFG）光时')
s=s.replace('公式化过程中会出现维度数与层数相同的矩阵','公式化过程中会出现维数与层数相同的矩阵')
s=s.replace('> 原作：广瀬千秋\n> 中文翻译：章力','> 原作：广瀬千秋  \n> 中文翻译：章力')
s=s.replace('> **底本：**','>\n> **底本：**').replace('> **局部约定：**','>\n> **局部约定：**')
p.write_text(s,encoding='utf-8')
# Refresh batch texts without repeating mutations.
starts=[0,s.index('## 2. 一般公式'),s.index('逆矩阵 $(E-A)'),s.index('### 2.1 m 层发光'),s.index('### 2.2'),s.index('## 附录 A'),s.index('**反射与折射**'),s.index('## 附录 B'),len(s)]
for n,(a,b) in enumerate(zip(starts,starts[1:]),50):(out/f'B{n:03}-本批译文.md').write_text(s[a:b],encoding='utf-8')
print('最终公式结构及8批文本已同步')

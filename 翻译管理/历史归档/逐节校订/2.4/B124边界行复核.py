from pathlib import Path
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];D=ROOT/'中文版本/第二章 薄膜产生的SFG'
row='''$$
1+r_{12}^x=t_{12}^x,§qquad 1+r_{12}^y=t_{12}^y,§qquad
1+r_{12}^z=(n_2/n_1)^2t_{12}^z.
$$

'''.replace('§',chr(92))
for p in [next(D.glob('2.4 *.md')),OUT/'B124-本批译文.md']:
 s=p.read_text(encoding='utf-8');key='上式满足以下关系；首行表示电场的边界条件：\n\n';assert key in s
 assert '1+r_{12}^x=t_{12}^x' not in s[:s.index('## L系数与电场振幅')] if '## L系数与电场振幅' in s else True
 s=s.replace(key,key+row,1);p.write_text(s,encoding='utf-8')
print('source unnumbered boundary row included explicitly')

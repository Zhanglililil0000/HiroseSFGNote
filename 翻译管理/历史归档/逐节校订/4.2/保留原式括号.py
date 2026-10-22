from pathlib import Path
import re
o=Path(__file__).resolve().parent
p=o/'B290-本批译文.md';s=p.read_text(encoding='utf-8')
s=s.replace('原表简并(spp)、(psp)、(pps)、(sss)行有孤立的花括号，排版仅整理定界符，不改变项的加乘结构。','原表简并(spp)、(psp)、(pps)、(sss)行有孤立的花括号，下文照录，不补定闭合位置；相关分组与加乘范围仍待核。')
def fix(m):
    x=m[0]
    if any(r'\chi_{'+i+'}' in x.split('=')[0] for i in ['yxx','xyx','xxy']):
        x=x.replace(r'\beta_{caa}\Bigl(-',r'\beta_{caa}\{\Bigl(-',1)
    if r'\chi_{yyy}' in x.split('=')[0]:
        x=x.replace(r'\beta_{aaa}\frac',r'\beta_{aaa}\{\frac',1)
    return x
# Restrict to degenerate table.
a,b=s.split('#### 简并振动',1)
b=re.sub(r'\$\$[\s\S]*?\$\$',fix,b)
p.write_text(a+'#### 简并振动'+b,encoding='utf-8')
root=o.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.2 CH₃基团的取向与和频张量.md'
t=target.read_text(encoding='utf-8');start=t.index('### 5b.');end=t.index('### 5c.',start)
target.write_text(t[:start]+p.read_text(encoding='utf-8')+'\n\n'+t[end:],encoding='utf-8')
q=root/'翻译管理/疑难与勘误.md';s=q.read_text(encoding='utf-8').replace('原表简并(spp)、(psp)、(pps)、(sss)行有孤立的花括号，排版仅整理定界符，不改变项的加乘结构。','原表简并(spp)、(psp)、(pps)、(sss)行有孤立的花括号，下文照录，不补定闭合位置；相关分组与加乘范围仍待核。');q.write_text(s,encoding='utf-8')
print('已保留5b原式的孤立花括号，未补定分组')

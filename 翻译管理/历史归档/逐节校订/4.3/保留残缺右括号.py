from pathlib import Path
import re
o=Path(__file__).resolve().parent
for n in [301,306]:
    p=o/f'B{n}-本批译文.md';s=p.read_text(encoding='utf-8')
    def fix(m):
        x=m[0]
        if r'\chi_{xyx}' in x.split('=')[0]:x=x.replace(r'1 - \cos 2\phi\sin\theta',r'1 - \cos 2\phi)\sin\theta')
        return x
    s=re.sub(r'\$\$[\s\S]*?\$\$',fix,s)
    s=s.replace('未像$\chi_{yxx}$那样给$1-\cos2\phi$加括号','只见$1-\cos2\phi$后的右括号，未见与之配对的左括号')
    s=s.replace('同样缺少$1-\cos2\phi$外括号','同样只见$1-\cos2\phi$后的右括号，缺少配对的左括号')
    p.write_text(s,encoding='utf-8')
root=o.parents[2];q=root/'翻译管理/疑难与勘误.md';s=q.read_text(encoding='utf-8').replace('未像$\chi_{yxx}$那样给$1-\cos2\phi$加括号','只见$1-\cos2\phi$后的右括号，未见与之配对的左括号').replace('同样缺少$1-\cos2\phi$外括号','同样只见$1-\cos2\phi$后的右括号，缺少配对的左括号');q.write_text(s,encoding='utf-8')

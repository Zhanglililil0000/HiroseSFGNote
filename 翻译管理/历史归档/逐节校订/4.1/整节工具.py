from pathlib import Path
import re,json,hashlib
p=Path(__file__).resolve().parent; root=p.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.1 CH、CH₂、CH₃基团CH伸缩振动的和频极化率.md'
snapshot=p/'B251前整节快照.md'
if not snapshot.exists(): snapshot.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snapshot.read_text(encoding='utf-8')
blocks=re.findall(r'\\\[([\s\S]*?)\\\]',old)
def norm(s):
    s=s.replace('\\(', '$').replace('\\)', '$')
    s=re.sub(r'(?m)^\\\[\s*$',lambda m:'$$',s)
    s=re.sub(r'(?m)^\\\]\s*$',lambda m:'$$',s)
    s=re.sub(r'\bb_(?=\{|0)',r'\\beta_',s)
    s=s.replace('\\cos a','\\cos\\alpha').replace('\\sin a','\\sin\\alpha').replace('(a/2)','(\\alpha/2)')
    s=s.replace('\\cos^2 a','\\cos^2\\alpha').replace('\\sin^2 a','\\sin^2\\alpha')
    s=s.replace('\\cos t','\\cos\\tau').replace('\\sin t','\\sin\\tau').replace('\\cos^2 t','\\cos^2\\tau').replace('\\sin^2 t','\\sin^2\\tau')
    s=s.replace('\\cos 2t','\\cos^2\\tau').replace('\\sin 2t','\\sin^2\\tau')
    s=s.replace('\\rho+t','\\pi+\\tau').replace('\\rho-t','\\pi-\\tau')
    # 恢复原键固定坐标希腊字母，仅用于正文α张量和场、变换矢量。
    for a,b in [('xx','\\xi\\xi'),('zz','\\zeta\\zeta')]: s=s.replace(a,b)
    s=re.sub(r'(?<=[_{, ])x(?=[}, ^])',r'\\xi',s)
    s=re.sub(r'(?<=[_{, ])z(?=[}, ^])',r'\\zeta',s)
    return s
def math(tex): return '$$\n'+norm(tex.strip())+'\n$$\n\n'
def eq(tag):
    appendix={
    'B.1':r'T(X)=\frac12\sum_i m_i[(dX_i/dt)^2+(dY_i/dt)^2+(dZ_i/dt)^2]\tag{B.1}',
    'B.2':r'T(X^{\prime})=\frac12\sum_i m_i[(dX_i^{\prime}/dt)^2+(dY_i^{\prime}/dt)^2+(dZ_i^{\prime}/dt)^2]\tag{B.2}',
    'B.3':r'\mathbf r=U(\chi,\theta,\phi)\mathbf X^{\prime}\tag{B.3}'}
    if tag in appendix:return math(appendix[tag])
    found=[b for b in blocks if '\\tag{'+tag+'}' in b]
    assert len(found)==1,(tag,len(found))
    return math(found[0])
def span(a,b): return norm(old[old.index(a):old.index(b,old.index(a)+len(a))])
def add(n,body,pages,issues=''):
    if issues: body+='\n> **译者注（原文疑点）：** '+issues+'\n'
    (p/f'B{n}-本批译文.md').write_text(body,encoding='utf-8')
    rec=dict(batch=f'B{n}',date='2026-10-20',pages=pages,tags=re.findall(r'\\tag\{([^}]+)\}',body),source_sha256=hashlib.sha256((root/'日语原版/Chapter4/chap4-1.pdf').read_bytes()).hexdigest(),source_images_visually_checked=True,source_formula_corrections_adopted=False)
    (p/f'B{n}-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (p/f'B{n}.md').write_text(f'# B{n} 校订记录\n\n对照原文页{pages}，完整保留本组段落、公式及条件。恢复旧译转录和漏译；原文疑点另就地说明，未采用原文公式修正。\n\n'+issues+'\n',encoding='utf-8')

from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent
root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.2 CH₃基团的取向与和频张量.md'
snapshot=out/'B278前整节快照.md'
if not snapshot.exists(): snapshot.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snapshot.read_text(encoding='utf-8')
def part(start,end=None):
    a=old.index(start); b=old.index(end,a) if end else len(old)
    return old[a:b]
def norm(s,powers=True):
    s=re.sub(r'\bb_\{',r'\\beta_{',s)
    s=re.sub(r'\bc_\{(?=[xyz]{3}\})',r'\\chi_{',s)
    s=re.sub(r'(?<![A-Za-z\\])([qfc])(?![A-Za-z])',lambda m:{'q':r'\theta','f':r'\phi','c':r'\chi'}[m[0]],s)
    s=s.replace(r'b_{xxz}',r'\beta_{\xi\xi\zeta}').replace(r'b_{hhz}',r'\beta_{\eta\eta\zeta}').replace(r'b_{zzz}',r'\beta_{\zeta\zeta\zeta}')
    # b was already normalized above.
    s=s.replace(r'\beta_{xxz}',r'\beta_{\xi\xi\zeta}').replace(r'\beta_{hhz}',r'\beta_{\eta\eta\zeta}').replace(r'\beta_{zzz}',r'\beta_{\zeta\zeta\zeta}')
    if powers:
        s=re.sub(r'\\(sin|cos) ([23])\\theta',lambda m:'\\'+m[1]+'^'+m[2]+r'\theta',s)
    s=s.replace(r'}{\chi}',r'}{c}')
    s=re.sub(r'\\tag\{([0-9.]+)\\chi\}',r'\\tag{\1c}',s)
    return s
def maths(s,powers=True):
    return [norm(m,powers) for m in re.findall(r'\$\$([\s\S]*?)\$\$',s)]
def fmt(m): return '\n\n$$\n'+m.strip()+'\n$$\n\n'
def allmath(s,powers=True):return ''.join(fmt(m) for m in maths(s,powers))
def add(n,pages,s,desc):
    (out/f'B{n}-本批译文.md').write_text(s.strip()+'\n',encoding='utf-8')
    sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-2.pdf').read_bytes()).hexdigest()
    (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','date':'2026-10-21','pages':pages,'scope':desc,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
    (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n{desc}。逐页对照原页，恢复希腊字母、θ函数幂与倍角的区别、系数及模式条件；旧译修复不作为原文勘误。原文疑点见就地注，未采用原文公式修正。\n',encoding='utf-8')

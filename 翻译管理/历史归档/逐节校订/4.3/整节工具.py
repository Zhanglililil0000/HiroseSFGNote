from pathlib import Path
import re,json,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.3 CH₂基团的取向与和频张量.md'
snapshot=out/'B297前整节快照.md'
if not snapshot.exists():snapshot.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snapshot.read_text(encoding='utf-8')
def part(a,b=None):
    start=old.index(a);return old[start:old.index(b,start)] if b else old[start:]
def norm(s):
    s=s.replace(r'\varphi',r'\theta')
    s=s.replace('b_{',r'\beta_{')
    s=re.sub(r'\bc_\{(?=[xyz]{3}\})',r'\\chi_{',s)
    s=re.sub(r'(?<![A-Za-z\\])c(?![A-Za-z])',lambda m:r'\chi',s)
    s=s.replace(r'}{\chi}',r'}{c}')
    s=re.sub(r'\\tag\{([0-9.\-]+)\\chi\}',r'\\tag{\1c}',s)
    for i,j in [('xxz',r'\xi\xi\zeta'),('hhz',r'\eta\eta\zeta'),('zzz',r'\zeta\zeta\zeta')]:s=s.replace(r'\beta_{'+i+'}',r'\beta_{'+j+'}')
    s=re.sub(r'\\(sin|cos)\s+([23])\\(theta|alpha)',lambda m:'\\'+m[1]+'^'+m[2]+'\\'+m[3],s)
    return s
def fmt(m):return '\n\n$$\n'+m.strip()+'\n$$\n\n'
def maths(s):return [norm(m) for m in re.findall(r'\$\$([\s\S]*?)\$\$',s)]
def table(s):
    result=[]
    for m in re.finditer(r'\$\$([\s\S]*?)\$\$|##### \\\(\((ppp|spp|ssp|psp|sps|pps|pss|sss)\)\\\)',s):
        if m[1] is not None:result.append(fmt(norm(m[1])))
        else:
            result.append('\n**('+m[2]+')**\n')
            if '无双' in s[m.end():m.end()+25]:result.append('\n无。\n')
    return ''.join(result)
def add(n,pages,s,scope):
    (out/f'B{n}-本批译文.md').write_text(s.strip()+'\n',encoding='utf-8')
    sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-3.pdf').read_bytes()).hexdigest()
    (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','date':'2026-10-21','pages':pages,'scope':scope,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
    (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n{scope}。逐页对照原页与文本，恢复β/χ、键系希腊字母、θ及α幂次和倍角的区别；旧译修复不作为原文勘误。原文疑点保留并就地说明，未采用候选修正。\n',encoding='utf-8')
def group(s,label):
    a=s.index(label); nxt=s.find('\n#### ',a+5)
    return s[a:nxt] if nxt!=-1 else s[a:]
sym=r'#### 【全对称（\(a_1\)）'
anti=r'#### 【反对称（\(b_1\)）'
oop=r'#### 【面外（\(b_2\)）'
angle=r'''分子面与$xy$面的角（内部旋转角）记为$\phi$，$c$轴从外向法线量起的倾斜角记为$\theta_{\mathrm{tilt}}$，$c$轴投影与$x$轴的角（面内取向角）记为$\chi_{\mathrm{ip}}$；以下公式使用的欧拉角为$\phi=\pi/2+\phi$、$\theta=\pi-\theta_{\mathrm{tilt}}$、$\chi=\pi/2+\chi_{\mathrm{ip}}$。
'''
def approx(s):
    pre=s[:s.index('#####')];m=''.join(fmt(x) for x in maths(pre))
    if r'\gg' in pre and r'\gg' not in m:
        m=r'在原文条件$\beta_{\xi\xi\zeta}\gg\beta_{\xi\xi\zeta}\sim\beta_{\eta\eta\zeta}$下：'+'\n'+m
    return m

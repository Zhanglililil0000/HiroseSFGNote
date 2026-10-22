from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B019-修订前.md');a=s.index('## 附录 A');b=s.index('## 附录 B',a);t=s[a:b].replace('​\t','').replace("$H\\'$","$H'$").replace("$H\\'(t)$","$H'(t)$")
t=t.replace('微扰项中的二次微扰项', '微扰中的二阶项：相互作用微扰').replace('(\\omega \\neq \\omega_{nm})','(\\omega \\neq \\omega_{mn})')
# Source A8 second-frequency denominators are 2omega2, unlike old 2omega1.
x=t.index(r'\tag{A-7}');y=t.index(r'\tag{A-8}');sub=t[x:y];sub=sub.replace(r'\frac{e^{2i\omega_2 t}}{2\omega_1 + \omega_{ln}}',r'\frac{e^{2i\omega_2 t}}{2\omega_2 + \omega_{ln}}').replace(r'\frac{e^{-2i\omega_2 t}}{2\omega_1 - \omega_{ln}}',r'\frac{e^{-2i\omega_2 t}}{2\omega_2 - \omega_{ln}}');t=t[:x]+sub+t[y:]
note='> **译者注（Q021）：** 附录 A 保留原文中的若干形式约定与疑点：式（A-2）首个系数未标时间导数；初始条件写成 $c_{nn}(t)=1$，未明确限定初始时刻；坐标矩阵元及极化式中的电荷/场幅因子未在各式显式统一。这些均不在翻译中自行补改，阅读推导时须留意。\n\n'
t=t.replace('## 附录 A：含时微扰中的近似展开\n\n','## 附录 A：含时微扰中的近似展开\n\n'+note)
# Reflow at brace-level zero while retaining exact algebraic token order.
def reflow(mat):
 tex=mat.group(1).strip();tag=re.search(r'\\tag\{[^}]+\}',tex);tagtext=tag.group(0) if tag else '';tex=re.sub(r'\\tag\{[^}]+\}','',tex)
 tex=tex.replace(r'\begin{align*}','').replace(r'\end{align*}','').replace(r'\left',r'\bigl').replace(r'\right',r'\bigr')
 tex=tex.replace('&','');tex=tex.replace(r'\\',' BREAK ');tex=re.sub(r'\s+',' ',tex)
 chunks=[]
 for row in tex.split(' BREAK '):
  depth=0;start=0;last=0
  for j,c in enumerate(row):
   if c=='{' and (j==0 or row[j-1]!='\\'):depth+=1
   elif c=='}' and (j==0 or row[j-1]!='\\'):depth-=1
   if depth==0 and c in '+-=' and j-start>210:
    chunks.append(row[start:j].strip());start=j
  if row[start:].strip():chunks.append(row[start:].strip())
 return '$$\n'+r'\begin{aligned}'+'\n'+('\\\\[6pt]\n'.join('&'+z for z in chunks))+'\n'+r'\end{aligned}'+'\n'+tagtext+'\n$$'
t=re.sub(r'\$\$([\s\S]*?)\$\$',reflow,t);s=s[:a]+t+s[b:];p.write_text(s,encoding='utf-8')
# Split deliverable at full formula boundaries.
cut1=t.index('$$',t.index(r'\tag{A-6}'))+2
cut2=t.index('**（二阶近似）**',t.index(r'\tag{A-9}'))
for id,text in [('B019',t[:cut1]),('B020',t[cut1:cut2]),('B021',t[cut2:])]:
 (o/f'{id}-本批译文.md').write_text(f'# {id}：附录A分批校订\n\n'+text,encoding='utf-8')
 ranges={'B019':'p13—14，开头说明、无编号推导及A-1至A-6','B020':'p15，A-7至A-9及跃迁/极化说明','B021':'p15—16，完整跨页A-10、A-11、A-12及末句'}
 (o/f'{id}.md').write_text(f'''# {id} 校订记录

2026-10-16。范围：{ranges[id]}。各编号式及范围内文字均按页面对照；跨页A-10未在中间切批。备份为B019-修订前.md（附录A联合修订前），分批输出与参考渲染独立留存。

A-8中omega2项两个分母旧译误写2omega1，已按原页改为2omega2。A-4条件旧译omega_nm改为底本omega_mn。A-7第二段分母仍是omega1，原文如此，未擅作对称化；A-9/A-11求和m而式内出现l及A-8外指数指标等尚需独立推导复核，列入Q021续记，不擅消指标。A-2首项无导数、初始时刻与电荷因子约定见正文注。

统一可渲染aligned结构，差项及指数符号保持；只按完整分式之间换行，不删公式项。语言保持“概率”与“单位时间跃迁概率”的区别。下一批附录B。
''',encoding='utf-8')
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8')+'\n| Q021 | 1.1附录A p13—16 | A-2首项系数无导数、初始时刻及电荷/场因子未明确；A-9/A-11的l指标与m求和及A-8指数指标需推导复核；A-7 omega2段出现omega1分母 | 原式约定/公式/P1 | B019—B021按底本保留并注明；A-8旧译2omega1对照改为2omega2，A-4条件改为原文mn；其他未独立推导，不称全部原式正确 |\n';p.write_text(s,encoding='utf-8')
print('AppendixA split into B019–B021, explicit transcription corrections and unresolved source conventions retained.')

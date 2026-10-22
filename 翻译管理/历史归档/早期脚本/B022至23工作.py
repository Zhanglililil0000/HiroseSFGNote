from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B022-修订前.md');a=s.index('## 附录 B');b=s.index('## 附录 C',a);t=s[a:b].replace('​\t','').replace('c_(t){n,n}',r'c(t)_{n,n}')
x=t.index(r'\tag{B-7}');y=t.index(r'\tag{B-8}');sub=t[x:y].replace(r'\frac{e^{-i(\omega_1 - \omega_2)t} + e^{-i(\omega_1 + \omega_2)t}}{\omega_2 + \omega_{mn}}',r'\frac{e^{-i(\omega_1 - \omega_2)t} + e^{i(\omega_1 + \omega_2)t}}{\omega_2 + \omega_{mn}}');t=t[:x]+sub+t[y:]
note='> **译者注（Q022）：** 式（B-1）、（B-2）按底本保留 $r_{nm}$ 及系数下标，部分指标与左端是否相容仍需推导核验；不据对称性静默替换。式（B-8）末项第二个指数已对照底本改为 $e^{+i(\\omega_1+\\omega_2)t}$，旧译误写负号。\n\n'
t=t.replace('## 附录 B 含时相互作用的微扰论中的展开系数\n\n','## 附录 B：含时相互作用微扰论中的展开系数\n\n'+note)
helper=(m/'B019至21工作.py').read_text(encoding='utf-8');fn=helper[helper.index('def reflow(mat):'):helper.index("t=re.sub(r'\\$\\$",helper.index('def reflow(mat):'))];exec(fn);t=re.sub(r'\$\$([\s\S]*?)\$\$',reflow,t);s=s[:a]+t+s[b:];p.write_text(s,encoding='utf-8')
cut=t.index('$$',t.index(r'\tag{B-7}'))+2
for id,txt,scope in [('B022',t[:cut],'p17，B-1至B-7及相关文字'),('B023',t[cut:],'p17末跨p18，双波长交叉项说明及B-8、B-9')]:
 (o/f'{id}-本批译文.md').write_text(f'# {id}：附录B分批校订\n\n'+txt,encoding='utf-8');(o/f'{id}.md').write_text(f'# {id} 校订记录\n\n2026-10-16。范围：{scope}。对照原页指数、分母、矩阵元和初始系数。B-1旧译损坏的c_(t){{n,n}}恢复c(t)_{{n,n}}；B-8末项指数按原页由负改正。其他疑似原式指标问题Q022加注保留，未自行推导修式。备份B022-修订前.md覆盖附录B修订前。\n\n独立分批输出及渲染记录保存；下一范围附录C。\n',encoding='utf-8')
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8')+'\n| Q022 | 1.1附录B p17式B-1/B-2 | r_nm及c系数下标与左端指标是否相容需核验 | 原式公式/P1 | B022/B023照底本保留并注；B-8旧译末项指数负号按底本正号纠正；原式其余问题未解决 |\n';p.write_text(s,encoding='utf-8')
print('AppendixB split B022/B023; one broken index and B8 exponential sign corrected, source issues retained.')

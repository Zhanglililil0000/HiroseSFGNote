from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.3';p=r/'中文版本/第一章 SFG快速入门/1.3 光电场、极化与菲涅尔因子.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B035-修订前.md');s=s.replace('菲涅尔系数','菲涅尔因子').replace('菲涅尔的 L 系数','菲涅尔 L 因子').replace('​\t','');s=s.replace('感受率张量','极化率张量');s=s.replace('极化层厚度相对于波长可忽略的情况。','极化层厚度相对于波长可忽略的情况。式（11）的 $\\chi^{\\mathrm{SF}}$ 表示二阶非线性极化率。')
s=s.replace('### [菲涅尔 L 因子]','### 菲涅尔 L 因子')
# Preserve physics-sensitive source expressions, explicitly register where not mutually consistent.
s+='\n> **译者注（Q028）：** 式（2）的真空下标与介质参数关系、式（3）的复折射率及$\\mu$记号、表面两侧$z$场表达式的符号，以及式（10）的根式系数和复折射率代入关系，均按底本保留；部分等价式的符号/分母范围需独立复核。式（12）—（14）的正负上标方向遵照作者文字，不擅按其他教材约定倒置。本节式（3）的$\\chi$为线性响应，不能称二阶非线性极化率。\n'
helper=(m/'B019至21工作.py').read_text(encoding='utf-8');fn=helper[helper.index('def reflow(mat):'):helper.index("t=re.sub(r'\\$\\$",helper.index('def reflow(mat):'))];exec(fn);s=re.sub(r'\$\$([\s\S]*?)\$\$',reflow,s)
s=s.replace('> 中文翻译：章力','> 中文翻译：章力\n\n> **校订状态（2026-10-16）：** B035—B038全5页已分批页面对照及排版整理；原式约定疑点Q028未决。文件路径保留历史名称，正文术语统一为菲涅尔因子。');p.write_text(s,encoding='utf-8')
markers=[s.index('### [反射系数与透射系数]'),s.index('金属表面的折射率通常为复数'),s.index('### 菲涅尔 L 因子')];markers=[s.rfind('\n',0,x)+1 for x in markers];bounds=[0]+markers+[len(s)]
for i,(a,b,scope) in enumerate(zip(bounds,bounds[1:],['p1—2首，绪论/式1—3/边界条件','p2—3，式4—7与表面场无编号式','p3末—4，式8—10及注1','p4末—5，SFG极化和辐射L因子式11—15']),35):
 id=f'B{i:03d}';(o/f'{id}-本批译文.md').write_text(f'# {id}：1.3分批校订\n\n'+s[a:b],encoding='utf-8');(o/f'{id}.md').write_text(f'''# {id} 校订记录

2026-10-16。范围：{scope}。按原页对照文字、式号及全部无编号式，四批覆盖5页。备份B035-修订前.md。与用户指定统一“菲涅尔因子”，r/t具体仍称振幅反射/透射系数；L不称无量纲，保留90度相位说明。chi线性与二阶分开命名。

本节公式中的真空/介质下标、z场符号、根式及方向约定有疑点，Q028集中登记并在正文注；无据修改会造成另一套约定，故照底本保留。已调整aligned断行，括号与分母结合范围仍按底本/旧译留存并注明，不将有歧义的斜线式作为已独立证明等价式。下一节1.4。
''',encoding='utf-8')
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8')+'\n| Q028 | 1.3式2/3/10及表面z场与L因子 | 真空/介质下标、复折射率记号、等价式符号与分母及方向约定需复核 | 原式约定/P1 | B035—B038按底本保留并注；菲涅尔因子译名统一，线性chi与二阶chi分开 |\n';p.write_text(s,encoding='utf-8')
print('1.3 reviewed in four units, user terminology applied without changing source conventions.')

from 整节续校工具 import *
for p in [TARGET,OUT/'B119-本批译文.md']:
 s=p.read_text(encoding='utf-8').replace('不得把母本译文中已统一的下标直接当作本独立底本的原式。','两个不同下标照录，不据相邻式统一。')
 p.write_text(s,encoding='utf-8')
needle='*两图中的“媒質-1”“媒質-2”分别为介质1、介质2；其余符号与前图相同。底本图前“加重反射”按上下文译为多重反射，文字勘误见E-2.3-001。*'
replacement='''*两图中的“媒質-1”“媒質-2”分别为介质1、介质2；其余符号与前图相同。*

> **译者注（原文修正 E-2.3-001；暂定文字补读）：** 独立PDF p8第二幅光路图前，原文写作「加重反射光」。根据图中光路及前后多重反射的讨论，中译暂按“多重反射光”处理。此项是项目暂定文字补读，未经作者认可；原文与处理状态同时记入勘误附件。'''
for p in [TARGET,OUT/'B120-本批译文.md']:
 s=p.read_text(encoding='utf-8');assert needle in s;s=s.replace(needle,replacement,1);p.write_text(s,encoding='utf-8')
print('local adopted text reading now has explicit correction note and appendix identity')

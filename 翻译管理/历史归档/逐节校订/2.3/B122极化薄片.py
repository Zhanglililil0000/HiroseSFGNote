from 整节续校工具 import *
mother=(OUT/'母本夹膜及D参考.md').read_text(encoding='utf-8');u=mother[mother.index('## 附录D.'):]
u=u.replace('正文所称','底本所称正文的').replace('Q047','关联第2.2节Q047')
u=u.replace('本附录的（4.29）—（4.36）与现底本正文编号不匹配。本节界面和片内L系数实际集中于5.1，式（5.1a）—（5.5c）；这里只提供定位线索，不建立未经验证的一一换号关系。','本独立PDF不含这些正文公式；所引用（4.29）—（4.36）与第2.2节现有正文编号也不匹配。第2.2节界面和片内L系数集中于5.1，式（5.1a）—（5.5c）；这里只提供定位线索，不建立未经验证的一一换号关系。')
u=u.replace('跨p45—46','跨独立PDF p10—11').replace('标题位于p46末，公式在p47','公式跨独立PDF p11—12')
# Match the independent p12 source: its first Fresnel numerator is 2n_1 cos(theta_m).
head=u.rfind('**p偏振：来自 $P_z$ 的贡献。**');pre=u[:head];last=u[head:]
key=tex('§frac{2n_m§cos§theta_m}{§left(n_1§cos§theta_m+n_m§cos§theta_1§right)}')
assert key in last
last=last.replace(key,tex('§frac{2n_1§cos§theta_m}{§left(n_1§cos§theta_m+n_m§cos§theta_1§right)}'),1)
u=pre+last
assert len(re.findall(r'\$\$[\s\S]*?\$\$',u))==6
put('B122','## 附录D',None,u,'极化薄片L系数的两侧六条完整推导',[10,12],['L系数的原正文引用、无限薄片及外侧介质有限厚度限制','向介质1侧：s(Py)、p(Px)、p(Pz)三条推导，保留全部中间因子及负号','向介质2侧：s(Py)、p(Px)、p(Pz)三条推导至证毕','p12末式第一透射因子分子为2n_1 cosθ_m，局部放大确认；不套用母本转写的2n_m','两处跨页推导各合成完整数学式；无新增编号式，无原文公式修正'])

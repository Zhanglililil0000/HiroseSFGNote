from pathlib import Path
import re
out=Path(__file__).resolve().parent
unit='''### 两种介质组成的体系

设界面为平面，光由介质1侧入射到与介质2的界面。坐标轴等定义如下：

| 量 | 定义 |
|---|---|
| 原点 | 光线的入射点；光束有宽度时取其中央 |
| $z$ 轴 | 从介质1指向介质2的界面法线 |
| $x$ 轴 | 光沿界面的传播方向，与波矢 $§boldsymbol{k}$ 在界面上的投影一致 |
| 入射角 $§theta_i$ | 入射光线与外向法线（$-z$ 方向）的夹角，$0<§theta_i<§pi/2$ |
| 反射角 $§theta_r$ | 反射光线与外向法线（$-z$ 方向）的夹角，$0<§theta_r<§pi/2$ |
| 折射角 $§theta_t$ | 透射光线与内向法线（$+z$ 方向）的夹角，$0<§theta_t<§pi/2$ |

设两介质的折射率为 $n_1,n_2$，波矢的长度为 $k_1,k_2$，其中 $k=n§omega/c$。

> **译校注（关联第2.2节Q056，角度约定）：** “入射光线”与外向法线的夹角沿用底本；不要未经说明就将它改解为入射传播矢量与外向法线的夹角。本节的轴向与角度定义各自保留。

由斯涅尔定律，令 $§theta_i=§theta_r=§theta_1$、$§theta_t=§theta_2$，则

$$
n_1§sin§theta_1=n_2§sin§theta_2,§qquad
k_1§sin§theta_1=k_2§sin§theta_2.
$$

对于平面波，垂直于传播方向的平面上各点的光电场同相。沿传播方向，等相位面的间距就是波长，底本写为 $§lambda=2§pi/k=2§pi c/§omega n$。（见后面的示意图。）

> **译校注（斜线排版）：** 底本末项连写为 $2§pi c/§omega n$，未给出分母括号，此处保留这种写法。结合上文 $k=n§omega/c$，候选读法为 $2§pi c/(§omega n)$，未将补括号后的形式冒充原式。底本所指示意图位于PDF p6，将随下一批反射光路核对。

设原点处的电场为 $E_0e^{-i§omega t}$。先追踪通过介质2中 $(x,z)$ 点的光：

| 步骤 | 光路、相位与时间 |
|---|---|
| （1） | 该光入射到界面的位置为 $(x-z§tan§theta_2,0)$。 |
| （1a） | 在同一时刻 $t$，相对于入射到原点的光，它沿光路超前 $(x-z§tan§theta_2)§sin§theta_1$；因此，入射点处的相位比通过原点的光超前 $k_1(x-z§tan§theta_2)§sin§theta_1$。 |
| （1b） | 反过来，与原点相同的相位在 $t$ 之后 $(x-z§tan§theta_2)§sin§theta_1/(§omega/k_1)$ 通过该点。 |
| （2） | 进入介质2后，到达 $(x,z)$ 点的传播距离为 $z/§cos§theta_2$。 |
| （2a） | 与入射界面时的相位相比，$(x,z)$ 点的相位前进 $k_2z/§cos§theta_2$。 |
| （2b） | 从入射界面到达 $(x,z)$ 点所经历的时间，底本连写为 $§omega z/k_2§cos§theta_2$。 |
| （2c） | 结合（1a）及斯涅尔定律，相对于通过原点的光的相位 $-§omega t$，总相位前进 $k_2(x§sin§theta_2+z§cos§theta_2)$。 |

> **译校注（关联第2.2节Q056，保留原式）：** （2b）的底本没有标明斜线后的分母范围。无论将其读为 $(§omega z/k_2)§cos§theta_2$ 或 $§omega z/(k_2§cos§theta_2)$，均需核对其时间量纲；按本段传播距离 $z/§cos§theta_2$ 除以相速度 $§omega/k_2$，候选为 $k_2z/(§omega§cos§theta_2)$。这里保留底本连写，不采用候选式。

'''.replace('§',chr(92))
p=out/'B118校订.py';s=p.read_text(encoding='utf-8');s=re.sub("unit=r'''[\s\S]*?'''",lambda _:"unit=r'''"+unit+"'''",s,count=1)
s=s.replace("assert not (OUT/'B118-修订前.md').exists();(OUT/'B118-修订前.md').write_text(old,encoding='utf-8')","assert (OUT/'B118-修订前.md').exists()")
p.write_text(s,encoding='utf-8')
target=next((out.parents[2]/'中文版本/第二章 薄膜产生的SFG').glob('2.3 *.md'))
target.write_text((out/'B118-修订前.md').read_text(encoding='utf-8'),encoding='utf-8')
print('restored batch input and corrected math command entry')

from pathlib import Path
import shutil,hashlib
root=Path('HiroseSFGNote').resolve();m=root/'翻译管理';p=root/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md'
old=p.read_text(encoding='utf-8');a=old.index('## 1. 引言');b=old.index('## 2. SFG 极化与和频过程');tail=old[b:]
out=m/'校订记录'/'1.1';out.mkdir(parents=True,exist_ok=True)
assert not (out/'B001-修订前.md').exists(),'B001 backup exists; inspect before re-running'
shutil.copy2(p,out/'B001-修订前.md')
intro=r'''## 1. 引言

首先简要回顾静电学。点电荷周围会产生电场：将点电荷 $q_2$ 放在距点电荷 $q_1$ 为 $r$ 的位置时，$q_2$ 受到库仑力，其表达式为 $q_1q_2/(4\pi\epsilon r^2)$。这是因为 $q_1$ 在 $q_2$ 所在位置产生了电场 $\mathbf{E}=q_1\mathbf{e}_{12}/(4\pi\epsilon r_{12}^2)$。其中，$\mathbf{e}_{12}$ 是从 $q_1$ 指向 $q_2$ 的单位矢量，$r_{12}$ 为两电荷之间的距离。

电偶极矩 $\mathbf{p}$ 在距其 $r$ 处产生的电场为 $\mathbf{E}=[3(\mathbf{p}\cdot\mathbf{e})\mathbf{e}-\mathbf{p}]/(4\pi\epsilon r^3)$。置于电场中的电偶极矩受到力 $\mathbf{F}=(\mathbf{p}\cdot\nabla)\mathbf{E}$ 和力矩 $\mathbf{N}=\mathbf{r}\times\mathbf{F}=\mathbf{p}\times\mathbf{E}$ 的作用。

当电荷或电偶极矩的大小随时间振荡时，由此产生的电场也随之振荡。振荡的电场就是电磁波，光也是电磁波的一种。电偶极矩与电场之间的关系可由麦克斯韦方程组导出。

分子置于电场中会发生极化。对于由分子组成的宏观物质，各分子的极化矢量之和就是物质的宏观极化。产生极化时，以及极化的大小发生振荡时，都会产生电磁波。

> **译者注（原文疑误）：** 此句原文为「分極がするとき」，疑有脱字；这里按“产生极化时”译出。

光照射分子时，会在特定频率下发生光吸收。用电磁学的语言表述如下：当分子的固有跃迁频率与光的频率一致时，诱导极化会共振增强。由此发生的激发使分子的内能增加，因而消耗光的能量。若分子已经处于激发态，则在返回基态时，将多余的内能转化为光能，产生受激发射。（若处于跃迁上能级的分子数多于下能级，则由分子传递给光的能量会超过分子吸收的光能，结果就会产生激光振荡或光放大。）

如上所述，分子置于电场中会发生极化；只要电场不太强，分子中诱导的电偶极矩就与电场强度成正比。反过来，每个分子的电偶极矩也会在其周围产生电场。因此，考虑分子实际感受到的电场时，不仅要考虑外加电场，也要考虑周围分子电偶极矩传来的电场。处理这一问题的一个代表性方法，是引入“局域场”概念，描述固体或液体中分子实际感受到的电场。此外，吸附分子吸收光谱的峰位和强度会随覆盖率变化（在溶液中则随浓度变化）。解释这种变化时，需要用偶极–偶极相互作用理论来修正以下效应：周围分子所产生的极化，其大小和相位随光的频率变化，导致分子实际感受到的电场，其大小和相位也与外加光场略有不同。由于极化产生的电场效应相当于分子之间反复“传球”，偶极–偶极相互作用的表达式会成为相当复杂的无穷级数。

'''
head=old[:a]+'> **校订状态（2026-10-16）：** B001 已对照校订“1. 引言”；第 2 部分及以后仍为待校订旧译。底本：日语原版 Chapter1/chap1-1Japanese.pdf，PDF 第 1 页。\n\n'
p.write_text(head+intro+tail,encoding='utf-8')
assert p.read_text(encoding='utf-8').split('## 2. SFG 极化与和频过程',1)[1]==old.split('## 2. SFG 极化与和频过程',1)[1]
(out/'B001-底本摘要.txt').write_text(hashlib.sha256((root/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()+'\n',encoding='utf-8')
print('B001 intro updated; six source paragraphs retained; remainder unchanged.')

from pathlib import Path
import re,json,csv,io,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];M=ROOT/'翻译管理';D=ROOT/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.3 *.md'))
old=P.read_text(encoding='utf-8');assert (OUT/'B118-修订前.md').exists()
unit=r'''### 两种介质组成的体系

设界面为平面，光由介质1侧入射到与介质2的界面。坐标轴等定义如下：

| 量 | 定义 |
|---|---|
| 原点 | 光线的入射点；光束有宽度时取其中央 |
| $z$ 轴 | 从介质1指向介质2的界面法线 |
| $x$ 轴 | 光沿界面的传播方向，与波矢 $\boldsymbol{k}$ 在界面上的投影一致 |
| 入射角 $\theta_i$ | 入射光线与外向法线（$-z$ 方向）的夹角，$0<\theta_i<\pi/2$ |
| 反射角 $\theta_r$ | 反射光线与外向法线（$-z$ 方向）的夹角，$0<\theta_r<\pi/2$ |
| 折射角 $\theta_t$ | 透射光线与内向法线（$+z$ 方向）的夹角，$0<\theta_t<\pi/2$ |

设两介质的折射率为 $n_1,n_2$，波矢的长度为 $k_1,k_2$，其中 $k=n\omega/c$。

> **译校注（关联第2.2节Q056，角度约定）：** “入射光线”与外向法线的夹角沿用底本；不要未经说明就将它改解为入射传播矢量与外向法线的夹角。本节的轴向与角度定义各自保留。

由斯涅尔定律，令 $\theta_i=\theta_r=\theta_1$、$\theta_t=\theta_2$，则

$$
n_1\sin\theta_1=n_2\sin\theta_2,\qquad
k_1\sin\theta_1=k_2\sin\theta_2.
$$

对于平面波，垂直于传播方向的平面上各点的光电场同相。沿传播方向，等相位面的间距就是波长，底本写为 $\lambda=2\pi/k=2\pi c/\omega n$。（见后面的示意图。）

> **译校注（斜线排版）：** 底本末项连写为 $2\pi c/\omega n$，未给出分母括号，此处保留这种写法。结合上文 $k=n\omega/c$，候选读法为 $2\pi c/(\omega n)$，未将补括号后的形式冒充原式。底本所指示意图位于PDF p6，将随下一批反射光路核对。

设原点处的电场为 $E_0e^{-i\omega t}$。先追踪通过介质2中 $(x,z)$ 点的光：

| 步骤 | 光路、相位与时间 |
|---|---|
| （1） | 该光入射到界面的位置为 $(x-z\tan\theta_2,0)$。 |
| （1a） | 在同一时刻 $t$，相对于入射到原点的光，它沿光路超前 $(x-z\tan\theta_2)\sin\theta_1$；因此，入射点处的相位比通过原点的光超前 $k_1(x-z\tan\theta_2)\sin\theta_1$。 |
| （1b） | 反过来，与原点相同的相位在 $t$ 之后 $(x-z\tan\theta_2)\sin\theta_1/(\omega/k_1)$ 通过该点。 |
| （2） | 进入介质2后，到达 $(x,z)$ 点的传播距离为 $z/\cos\theta_2$。 |
| （2a） | 与入射界面时的相位相比，$(x,z)$ 点的相位前进 $k_2z/\cos\theta_2$。 |
| （2b） | 从入射界面到达 $(x,z)$ 点所经历的时间，底本连写为 $\omega z/k_2\cos\theta_2$。 |
| （2c） | 结合（1a）及斯涅尔定律，相对于通过原点的光的相位 $-\omega t$，总相位前进 $k_2(x\sin\theta_2+z\cos\theta_2)$。 |

> **译校注（关联第2.2节Q056，保留原式）：** （2b）的底本没有标明斜线后的分母范围。无论将其读为 $(\omega z/k_2)\cos\theta_2$ 或 $\omega z/(k_2\cos\theta_2)$，均需核对其时间量纲；按本段传播距离 $z/\cos\theta_2$ 除以相速度 $\omega/k_2$，候选为 $k_2z/(\omega\cos\theta_2)$。这里保留底本连写，不采用候选式。

'''
# Raw string is used deliberately: prevent \t in theta/tan from becoming tabs.
i=old.index('### 由两种介质组成的系统');j=old.index('追踪通过介质 1 侧点',i)
new=old[:i]+unit+old[j:]
new=new.replace('至B117已完成引言、附录A/B及附录C开头“单一且均匀的介质”（PDF p1—4）的本轮校订，含相应编号公式及无编号关系。附录C自“两种介质”起及附录D仍为旧译待校订。','至B118已完成引言、附录A/B、C的单一均匀介质及双介质的定义和透射光路（PDF p1—5，至步骤2c）。C的反射光路及以后、附录D仍为旧译待校订。')
new=new.replace('双介质、夹膜体系及附录D的极化薄片L系数仍待逐段校订。','双介质的坐标定义及透射光路已核；反射光路、夹膜体系及附录D的极化薄片L系数仍待逐段校订。')
new=new.replace('本节附录B及已核的C.1采用负时间因子','本节附录B、C.1及双介质原点场采用负时间因子')
P.write_text(new,encoding='utf-8');(OUT/'B118-本批译文.md').write_text(unit,encoding='utf-8')
assert new[new.index('追踪通过介质 1 侧点'):]==old[j:]
assert not any(ord(c)<32 and c not in '\r\n' for c in new)
sha=hashlib.sha256((ROOT/'日语原版/Chapter2/chap2-3.pdf').read_bytes()).hexdigest();assert sha=='63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384'
(OUT/'B118-覆盖.json').write_text(json.dumps({'batch':'B118','page':5,'start':'两种介质组成的体系','end':'(2c)及译校注','definitions':9,'path_steps':['1','1a','1b','2','2a','2b','2c'],'new_numbered_equations':[],'source_sha256':sha,'unreviewed_remainder_unchanged':True,'issues':'关联Q056；斜线范围另加局部说明','source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'B118.md').write_text('''# B118：双介质坐标定义及透射光路

2026-10-19；独立底本PDF p5，“两种介质”标题至(2c)。逐项核对原页和文字层，不能将2.2对应表格的分母括号当成独立底本原有括号。

范围：原点、x/z轴、三个角及范围、n/k定义、斯涅尔关系、等相位面与波长、原点负时间因子、(1)—(2c)七个完整步骤。无新增编号式；本节累计已核编号式仍19个。下一批B119从反射光追踪开始。

保留原式：波长末项2πc/ωn、(2b)时间ωz/k2cosθ2均为无分母括号的连写，正文照录；补括号读法及传播时间候选仅注，不声称作者公式。入射光线与外向法线定义沿底本，关联2.2 Q056。无新增原文采用修正，不分配E编号；无新术语决定。p6示意图有明确后续去向，尚未纳入本批。

相较母本：母本将时间式和波长式按候选范围排出括号，本批独立依据原页保留线性写法并说明歧义；没有因此回写母本或将两份内容误称完全一致。后续反射与夹膜旧译逐字保持，边界断言已检查。

已同步章节清单、分批建议、进度、导读、局部约定、复用表及疑难记录。渲染和范围验收另存；全文件语法通过不意味着后续旧译已核。
''',encoding='utf-8')
def append(p,t):p.write_text(p.read_text(encoding='utf-8').rstrip()+'\n\n'+t+'\n',encoding='utf-8')
append(OUT/'2.2与2.3复用核验表.md','## B118核验更新\n\n独立p5双介质的定义及(1)—(2c)已逐项核对。没有原文编号式新增；两处斜线连写按独立图照录：2πc/ωn及ωz/k2cosθ2。母本译文为其添加了分母范围，本批不直接搬用该排版，候选括号及时间式仅注。反射光路及p6图待B119。')
append(OUT/'局部约定卡.md','## B118：双介质透射光路\n\nz由介质1指向介质2，x沿界面上的波矢投影；θi、θr按原光线与外法线定义，θt按内法线。θi=θr=θ1、θt=θ2。原点E0exp(−iωt)；位移/路径使用当地介质角度和波矢。波长及时间的斜线未标分母范围，原连写保留、候选仅注，关联Q056。')
append(M/'疑难与勘误.md','## 2.3双介质透射光路（B118）\n\n独立PDF p5，(2b)连写ωz/k2cosθ2，没有分母括号；两种读法均需核对时间量纲，传播距离除相速度的候选k2z/(ωcosθ2)只列注，关联2.2 Q056。波长末项2πc/ωn的分母范围也只说明候选，不替换原式。角度定义按本段光线记法保留。未采用原文修正，无新E编号。')
def tsv(p,key,val,changes):
 rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0]);found=0
 for row in rows:
  if row[key]==val:row.update(changes);found+=1
 assert found
 buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_text(buf.getvalue(),encoding='utf-8-sig')
tsv(M/'章节清单.tsv','编号','2.3',{'状态':'至B118，已核引言、A/B、C均匀介质及双介质定义/透射路径至2c；其余待核','映射核验':'独立p1—4及p5至2c已核；反射路径及后文待核','公式图表范围':'19个已核编号式及相应无编号式；B118新增7个透射路径步骤对照','导读状态':'Preface与第二章导航更新至B118'})
tsv(M/'全书调查/分批建议.tsv','节号','2.3',{'执行状态':'2026-10-19至B118，双介质定义及透射路径至2c完成；B119续反射路径3—4c及p6示意图；其余待核'})
p=M/'当前进度与续接.md';s=p.read_text(encoding='utf-8');entry='''## 当前有效状态：B118完成2.3双介质定义及透射光路（2026-10-19）

已核独立PDF p5双介质标题、坐标/角度/n/k定义、斯涅尔关系及透射步骤(1)—(2c)。斜线连写保留，分母范围和时间候选只注，关联Q056；无新增原文采用修正。本节已核编号式仍19个，未核反射及后文逐字保持。

下一批B119：从p5“媒質1側の点(x,−z)…反射光”开始，完整核对(3)—(4c)，并处理p6两介质示意图，止于夹膜体系标题前。特别注意(3a)距离角θ2与相位角θ1不一致、(4b)时间连写及(x,−z)/(x,z)；分别对原页确认，不能套用母本规范化结果。后续夹膜体系与附录D仍待核。下面均为历史记录。

''';p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
p=ROOT/'Preface序言.md';s=p.read_text(encoding='utf-8').replace('（至B117已核引言、A/B及C的单一均匀介质；后续待校订）','（至B118已核引言、A/B及C双介质透射光路；后续待校订）');p.write_text(s,encoding='utf-8')
p=D/'阅读导航.md';s=p.read_text(encoding='utf-8').replace('2.3已校订至附录C的单一均匀介质；C自双介质起、D及2.4以后仍为旧译待校订。','2.3已校订至附录C双介质的透射光路；反射光路及其后、D与2.4以后仍待校订。').replace('至B117完成引言、附录A/B及C的单一均匀介质。','至B118完成引言、附录A/B、C的单一均匀介质及双介质定义/透射光路。').replace('双介质与夹膜体系仍待核。','p5双介质定义及透射光路(1)—(2c)已核；反射光路、示意图与夹膜体系仍待核。');p.write_text(s,encoding='utf-8')
print('B118 applied; definitions and seven path steps; remainder unchanged')

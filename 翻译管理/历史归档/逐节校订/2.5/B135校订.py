from pathlib import Path
import json,csv,re
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.5 *.md'));old=P.read_text(encoding='utf-8');a=old.index('所谓"反射光"');z=old.index('## 4.1 激发电场',a)
assert not (O/'B135-修订前.md').exists()
(O/'B135-修订前.md').write_text(old,encoding='utf-8')
s='''### 多重反射与透射场

所谓“反射光”，是指在 $1/m$ 界面反射的光，再叠加上进入膜内经多重反射后从 $1/m$ 界面出射的上行（−）光。$1/m$ 界面的边界条件应施加于膜两侧分别叠加了这些多重反射光的总场。

$$
§begin{aligned}
&r_{1m}+t_{1m}t_{m1}r_{m2}§sum_{n=0}^{§infty}(r_{m2}r_{m1})^n
 §exp(i2§pi n_m2nh_m§cos§theta_m/§lambda) §§
&=r_{1m}+§frac{t_{1m}t_{m1}r_{m2}§exp(i2§pi n_m2h_m§cos§theta_m/§lambda)}
 {1-r_{m2}r_{m1}§exp(i2§pi n_m2h_m§cos§theta_m/§lambda)} §§
&=§frac{r_{1m}+[-r_{1m}r_{m1}+t_{1m}t_{m1}]r_{m2}§exp(i2§pi n_m2h_m§cos§theta_m/§lambda)}
 {1-r_{m2}r_{m1}§exp(i2§pi n_m2h_m§cos§theta_m/§lambda)} §§
&=§frac{r_{1m}+r_{m2}§exp(i2§pi n_m2h_m§cos§theta_m/§lambda)}
 {1-r_{m2}r_{m1}§exp(i2§pi n_m2h_m§cos§theta_m/§lambda)}.
§end{aligned}
§tag{2.1}
$$

> **原文疑点（Q040关联，2.5 PDF p2，式2.1）**：首行求和相位按 $2nh_m$ 写出，$n=0$ 项不带一次往返相位；下一行闭式的分子却含一次往返相位。这里完整保留原来的等号链。候选是在首行求和项之外再乘 $§exp(i2§pi n_m2h_m§cos§theta_m/§lambda)$，或将其相位中的 $n$ 改为 $n+1$；两者均未作为原文修正采用。求和序号 $n$ 与折射率 $n_m$ 不同。

所谓“透射光”，是直接通过薄膜的光与进入膜内经多重反射后从 $m/2$ 界面出射的光叠加而成的。$m/2$ 界面的边界条件应施加于包含这些多重反射光的总场。将入射光的振幅取为1、相位取为 $e^{-i§omega t}$ 时，“透射光”的电场振幅由下式给出：

$$
§begin{aligned}
&t_{1m}t_{m2}§sum_{n=0}^{§infty}(r_{m2}r_{m1})^n
 §exp(i2§pi n_m2h_m§cos§theta_m/§lambda)^n §§
&§qquad§times§exp(i2§pi n_mh_m§cos§theta_m/§lambda) §§
&=§frac{t_{1m}t_{m2}§exp(i2§pi n_mh_m§cos§theta_m/§lambda)}
 {1-r_{m2}r_{m1}§exp(i2§pi n_m2h_m§cos§theta_m/§lambda)}.
§end{aligned}
§tag{2.3}
$$

> **编号说明（译者）**：底本从式（2.1）直接接至（2.3），随后进入“4.1 激发电场”；此处保留原编号，不补造（2.2）或第3部分。式（2.3）求和中的 $n$ 为整个指数函数的幂，按原排版保留。

'''.replace('§',chr(92))
new=old[:a]+s+old[z:];assert new[:a]==old[:a];assert new[new.index('## 4.1 激发电场'):]==old[z:];P.write_text(new,encoding='utf-8');(O/'B135-本批译文.md').write_text(s,encoding='utf-8')
text=P.read_text(encoding='utf-8');text=text.replace('B134完成PDF p1的引言、体系设定及全部定义，止于“反射光”说明前；其后仍为旧译待校订。','B134—B135完成PDF p1—2的引言、定义及多重反射/透射说明和式（2.1）、（2.3），止于4.1标题前；其后仍为旧译待校订。');P.write_text(text,encoding='utf-8')
(O/'B135.md').write_text('''# B135：多重反射与透射场

2026-10-20，独立底本p1末段至p2的4.1标题前。完整核反射/透射两段说明、2.1四行等号链及2.3求和/闭式；保留n与n_m、负时间指数、原编号跳跃。

Q040关联：反射首行n=0项的相位与下一行闭式不一致。原式照录，补一次往返相位或n→n+1候选只注。没有采用原文修正，未增E条目。旧译后段4.1及以后逐字保持；页首状态已更新。

下一批B136：4.1开头的波长依赖、坐标分量的r/t关系与两个乘积恒等式，止于4.1a前。独立核原页，不直接认定等于2.4。
''',encoding='utf-8')
(O/'B135-覆盖.json').write_text(json.dumps({'batch':'B135','date':'2026-10-20','pages':[1,2],'equation_tags':['2.1','2.3'],'source_p2_visually_checked':True,'reflection_chain_rows':4,'transmission_chain_complete':True,'unreviewed_tail_unchanged':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
f=R/'翻译管理/当前进度与续接.md';v=f.read_text(encoding='utf-8');i=v.index('\n')+1;v=v[:i]+'''\n## 当前有效状态：B135完成2.5多重反射/透射（2026-10-20）

B134—B135已核p1—2至4.1标题前：引言、全部定义、反射/透射说明及式2.1/2.3。Q040关联首行与闭式相位差异按原值保留并加注，候选未采用。4.1及以后旧译逐字保持，数学检查仅覆盖已校订片段。

下一批B136：核4.1开头波长/复数说明、r/t坐标分量六行及两个乘积恒等式，止于4.1a前。编号跳跃保留，不补造2.2或第3部分。以下为历史记录。

'''+v[i:];f.write_text(v,encoding='utf-8')
for rel,key in [('翻译管理/章节清单.tsv','编号'),('翻译管理/全书调查/分批建议.tsv','节号')]:
 f=R/rel
 with f.open(encoding='utf-8-sig',newline='') as h:d=csv.DictReader(h,delimiter='\t');fields=d.fieldnames;rows=list(d)
 for row in rows:
  if row[key]!='2.5':continue
  if key=='编号':row['状态']='B134—B135已核引言、定义与多重反射/透射；4.1起待校订';row['映射核验']='独立20页；p1—2至4.1前已逐项核验';row['公式图表范围']='已核编号式2.1/2.3；4.1及以后待核'
  else:row['执行状态']='B134—B135已核p1—2至4.1前；B136续4.1开头系数关系；后续未核'
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(rows)
f=R/'Preface序言.md';v=f.read_text(encoding='utf-8').replace('（B134已核引言及定义，后续待校订）','（B134—B135已核引言、定义及多重反射/透射，后续待校订）');f.write_text(v,encoding='utf-8')
f=D/'阅读导航.md';v=f.read_text(encoding='utf-8').replace('2.5已核引言及定义','2.5已核引言、定义及多重反射/透射').replace('B134已核p1引言、体系设定及全部定义；反射光说明及后续尚待校订。','B134—B135已核p1—2引言、体系设定、全部定义及反射/透射说明和式2.1/2.3；4.1起尚待校订。');v+='\nB135补充：多重反射/透射总场与边界条件已核；反射求和起始相位与闭式存在原文差异，保留并注Q040关联。\n';f.write_text(v,encoding='utf-8')
for rel,extra in [('翻译管理/疑难与勘误.md','\nQ040续记（B135，2026-10-20）：2.5 PDF p2式2.1首行相位2nh_m、下一行闭式分子含一次往返相位；与母本相同疑点，原等号链保留。补公共一次往返相位或n→n+1只作候选，无采用修正。\n'),('翻译管理/校订记录/2.5/局部约定卡.md','\nB135：入射振幅1、时间相位e^(−iωt)；求和n与折射率n_m不同。2.1首项相位与闭式差异只注，2.3保留整个exp的n次幂；原编号2.1→2.3→4.1不重排。\n'),('翻译管理/校订记录/2.5/结构与复用核验表.md','\nB135更新：p1—2多重反射/透射说明及2.1/2.3已逐项核验完成。4.1及以后仍待核。\n')]:
 f=R/rel;f.write_text(f.read_text(encoding='utf-8')+extra,encoding='utf-8')
print('B135 written; later text unchanged')

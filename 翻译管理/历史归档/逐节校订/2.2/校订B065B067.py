from pathlib import Path
import csv,io
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'));s=p.read_text(encoding='utf-8')
start=s.index('## 4. 光路上的SFG极化');end=s.index('#### 4.1c.',start);tail=s[end:]
general=r'''## 4. 光路上的SFG极化

考虑薄膜两侧表面及膜内部都能产生极化，分别考察各位置的激发光电场与极化。

### 4.1. 激发电场

折射率和波矢的大小取决于波长，因此红外光与可见光对应不同的数值。对于存在吸收的红外光，这些量为复数。为区分波长，以下使用第二下标 $\mathrm{ir}$、$\mathrm{vis}$、$\mathrm{SF}$。

以表面固定坐标系的分量表示电场时，使用下列反射、透射系数关系：

$$
\begin{aligned}
r_{1m,x}&=-r_{m1,x}=r_{1m,p},\\
r_{1m,y}&=-r_{m1,y}=r_{1m,s},\\
r_{1m,z}&=-r_{m1,z}=-r_{1m,p}.
\end{aligned}
$$

$$
\begin{aligned}
r_{2m,x}&=-r_{m2,x}=r_{2m,p},\\
r_{2m,y}&=-r_{m2,y}=r_{2m,s},\\
r_{2m,z}&=-r_{m2,z}=-r_{2m,p}.
\end{aligned}
$$

$$
\begin{aligned}
t_{1m,x}&=\frac{\cos\theta_m}{\cos\theta_1}t_{1m,p},&
t_{1m,y}&=t_{1m,s},&
t_{1m,z}&=\frac{\sin\theta_m}{\sin\theta_1}t_{1m,p},\\[4pt]
t_{m1,x}&=\frac{\cos\theta_1}{\cos\theta_m}t_{m1,p},&
t_{m1,y}&=t_{m1,s},&
t_{m1,z}&=\frac{\sin\theta_1}{\sin\theta_m}t_{m1,p}.
\end{aligned}
$$

$$
\begin{aligned}
t_{2m,x}&=\frac{\cos\theta_m}{\cos\theta_2}t_{2m,p},&
t_{2m,y}&=t_{2m,s},&
t_{2m,z}&=\frac{\sin\theta_m}{\sin\theta_2}t_{2m,p},\\[4pt]
t_{m2,x}&=\frac{\cos\theta_2}{\cos\theta_m}t_{m2,p},&
t_{m2,y}&=t_{m2,s},&
t_{m2,z}&=\frac{\sin\theta_2}{\sin\theta_m}t_{m2,p}.
\end{aligned}
$$

$$
\begin{aligned}
t_{1m,\alpha}t_{m1,\alpha}
&=1+r_{1m,\alpha}r_{m1,\alpha}=1-r_{1m,\alpha}^{2},\\
t_{2m,\alpha}t_{m2,\alpha}
&=1+r_{2m,\alpha}r_{m2,\alpha}=1-r_{2m,\alpha}^{2},
\qquad \alpha=x,y,z.
\end{aligned}
$$

> **译者注（分量约定）：** 上式中的 $x,y,z$ 下标表示电场的坐标轴分量，$s,p$ 表示偏振。尤其应保留 $r_z=-r_p$ 的原文约定，不把所有坐标分量系数一律当作同一 $r_p$。这些系数关系按底本列出，本轮未以其作为所有吸收介质、角度及归一化选择下的独立证明。

'''
outside=r'''#### 4.1a. $1/2$ 体系界面外侧（介质1侧）的激发电场

这对应于玻璃表面、金属表面等表面或界面的介质1侧稀疏吸附分子所感受到的电场。只有介质1和介质2时，界面介质1侧的电场是入射光与反射光的矢量和。因此，

$$
E_{\mathrm{vis},\alpha}(0^-)
=E^0_{\mathrm{vis},\alpha}(1+r_{12,\mathrm{vis},\alpha}).
\tag{4.1}
$$

$$
E_{\mathrm{ir},\beta}(0^-)
=E^0_{\mathrm{ir},\beta}(1+r_{12,\mathrm{ir},\beta}).
\tag{4.2}
$$

$$
\begin{aligned}
E_{\mathrm{vis},\alpha}(0^-)E_{\mathrm{ir},\beta}(0^-)
={}&E^0_{\mathrm{vis},\alpha}E^0_{\mathrm{ir},\beta}\\
&\times(1+r_{12,\mathrm{vis},\alpha})(1+r_{12,\mathrm{ir},\beta}).
\end{aligned}
\tag{4.3}
$$

其中 $\alpha,\beta=x,y,z$，并且

$$
r_{12,x}=+r_{12,p},\qquad
r_{12,y}=+r_{12,s},\qquad
r_{12,z}=-r_{12,p}.
$$

> **译者注（符号辨析）：** 这里的 $\alpha,\beta$ 是坐标方向下标，不是分子极化率、超极化率，也不是式（2.2）的传播参数 $\beta_m$。$E^0$ 保留底本对激发场幅的记号；本段从只有两个介质的 $1/2$ 界面出发，不将其直接等同于后文有限厚度薄膜的激发场。

'''
inside=r'''#### 4.1b. $1/2$ 体系界面内侧（介质2侧）的激发电场

这对应于通常表面的介质2侧，或液体界面内侧稀疏吸附分子所感受到的电场。界面内侧只有透射光，因此，

$$
E_{\mathrm{vis},\alpha}(0^+)
=E^0_{\mathrm{vis},\alpha}t_{12,\mathrm{vis},\alpha}.
\tag{4.4}
$$

$$
E_{\mathrm{ir},\beta}(0^+)
=E^0_{\mathrm{ir},\beta}t_{12,\mathrm{ir},\beta}.
\tag{4.5}
$$

$$
\begin{aligned}
E_{\mathrm{vis},\alpha}(0^+)E_{\mathrm{ir},\beta}(0^+)
={}&E^0_{\mathrm{vis},\alpha}E^0_{\mathrm{ir},\beta}\\
&\times t_{12,\mathrm{vis},\alpha}t_{12,\mathrm{ir},\beta}.
\end{aligned}
\tag{4.6}
$$

其中，

$$
\begin{aligned}
t_{12,x}&=+\frac{\cos\theta_2}{\cos\theta_1}t_{12,p},\\
t_{12,y}&=+t_{12,s},\\
t_{12,z}&=+\frac{\sin\theta_2}{\sin\theta_1}t_{12,p}.
\end{aligned}
$$

'''
s=s[:start]+general+outside+inside+tail
s=s.replace('当前完成B058—B064：序论、定义、式（2.1）—（2.6），以及跨第3—5页的六类光路、图3.1和光路汇总；**第4部分“光路上的SFG极化”起仍为旧译待校订**。','当前完成B058—B067：序论、定义、式（2.1）—（2.6）、第3部分光路，以及第4部分开头至4.1b的分量约定和式（4.1）—（4.6）；**4.1c起仍为旧译待校订**。')
p.write_text(s,encoding='utf-8');assert s[s.index('#### 4.1c.'):]==tail
for bid,part,scope in [('B065',general,'p5末—p6开头，4/4.1引言及全部无编号分量关系'),('B066',outside,'p6，4.1a完整小节，式4.1—4.3及反射分量约定'),('B067',inside,'p6，4.1b完整小节，式4.4—4.6及透射分量约定')]:
    (out/f'{bid}-本批译文.md').write_text(part,encoding='utf-8')
    (out/f'{bid}.md').write_text(f'# {bid} 校订记录\n\n2026-10-19。范围：{scope}。已目视对照原文p5.png及原文p6.png；修订前备份B065-修订前.md。旧译裸数学、连续未分行公式和文字编号改为规范数学与独立编号，原式下标、正负号、角度比保持；α/β为坐标指标，与分子响应及β_m区分。无原式修正，无新增确定勘误。4.1c起未改。\n',encoding='utf-8')
(out/'B058-本批译文.md').write_text(s[:s.index('## 2. 准备')],encoding='utf-8')
rp=out/'检查排版.cjs';t=rp.read_text(encoding='utf-8').replace("'B063','B064']","'B063','B064','B065','B066','B067']").replace('6[0-4]','6[0-7]');rp.write_text(t,encoding='utf-8')
card=out/'局部约定卡.md';t=card.read_text(encoding='utf-8');t+='\n## B065—B067补充\n\nir/vis/SF区分波长；α、β在4.1中为坐标方向x/y/z，不是响应系数。坐标分量的反射关系z带负的p系数；透射分量包含相应sin/cos比。4.1a/b为仅介质1与介质2的1/2体系，0−/0+分别表示界面1侧/2侧；E⁰记号依底本，不补归一化。有限膜的4.1c起尚未核验。\n';card.write_text(t,encoding='utf-8')
sp=mg/'符号与约定.md';t=sp.read_text(encoding='utf-8');sp.write_text(t+'\n## 第2.2节4.1开头（B065—B067，2026-10-19）\n\n已核波长标记ir/vis/SF及s/p到x/y/z的分量关系。r_z=−r_p；透射分量的角度比按原文保留；α/β为坐标指标。4.1a/b仅1/2界面，E⁰为原激发场幅记号，不将其当作已核有限膜场或数密度归一化。详见该节局部约定卡。\n',encoding='utf-8')
cp=mg/'章节清单.tsv';rows=list(csv.DictReader(io.StringIO(cp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['编号']=='2.2':row['状态']='处理中：B058—B067，已至4.1b末';row['映射核验']='p1—6截至4.1b；4.1c起未校订';row['公式图表范围']='式2.1—2.6、4.1—4.6、分量关系及第3部分图文已覆盖'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);cp.write_text(buf.getvalue(),encoding='utf-8-sig')
pp=mg/'当前进度与续接.md';t=pp.read_text(encoding='utf-8')
entry='''## 最新续接：2.2的B065—B067完成（2026-10-19）

已目视核对p5末—p6，完成第4/4.1部分引言、所有无编号坐标分量关系，以及4.1a/b两个完整小节（式4.1—4.6）。明确α/β是坐标指标、β_m是相位参数，r_z与r_p的负号保留。仅格式和译文表达校订，无原式修正、无新增勘误条目。

下一批从4.1c（p6下半部，式4.7—4.9）开始，按有限膜的界面侧别逐小节推进，再进入p7的4.1d。不要把p6整页标为已核；4.1c起与本批备份保持相同。

''';pp.write_text(t.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
print('B065—B067正文及管理已同步')

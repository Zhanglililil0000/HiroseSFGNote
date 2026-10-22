from pathlib import Path
import pypdfium2 as pdfium
import csv,io
root=Path(__file__).resolve().parents[3];mg=root/'翻译管理';out=Path(__file__).resolve().parent
assets=root/'中文版本/assets/ch02';assets.mkdir(exist_ok=True)
d=pdfium.PdfDocument(str(root/'日语原版/Chapter2/chap2-2.pdf'))
for page,box,name in [(4,(.20,.53,.63,.735),'ch02-s02-fig31'),(4,(.11,.775,.88,.86),'ch02-s02-paths-a'),(5,(.11,.08,.88,.65),'ch02-s02-paths-b')]:
    im=d[page-1].render(scale=2.3).to_pil();w,h=im.size
    im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(assets/(name+'.png'))
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'));s=p.read_text(encoding='utf-8')
start=s.index('## 3. SFG光的光路');end=s.index('## 4. 光路上的SFG极化',start);tail=s[end:]
classification=r'''## 3. SFG光的光路

从原点出射至介质1的SFG光称为反射SFG，从点 $(h_m\tan\theta_{m,\mathrm{SF}},h_m)$ 出射至介质2的SFG光称为透射SFG。分别考察以下六类光源位置及路径。

### （a）膜内的 $A_n(z)$ 点

位置与范围为

$$
x=-[2nh_m+z]\tan\theta_{m,\mathrm{SF}},\qquad
n=0,1,2,\ldots,\quad 0<z<h_m.
$$

这些点生成上行（−）光。到达原点前的相位增量，以及到达 $(h_m\tan\theta_{m,\mathrm{SF}},h_m)$ 前的相位增量，分别为：

$$
\frac{k_{m,\mathrm{SF}}(2nh_m+z)}{\cos\theta_{m,\mathrm{SF}}},\qquad
\frac{k_{m,\mathrm{SF}}[(2n+1)h_m+z]}{\cos\theta_{m,\mathrm{SF}}}.
$$

### （b）膜内的 $B_n(z)$ 点

位置与范围为

$$
x=-[2nh_m+(2h_m-z)]\tan\theta_{m,\mathrm{SF}},\qquad
n=(-1),0,1,2,\ldots,\quad 0<z<h_m.
$$

底本称这些点生成“上行（＋）光”；其中 $n=-1$ 只对透射SFG有贡献。到达原点前及到达 $(h_m\tan\theta_{m,\mathrm{SF}},h_m)$ 前的相位增量，分别为：

$$
\frac{k_{m,\mathrm{SF}}[2nh_m+(2h_m-z)]}{\cos\theta_{m,\mathrm{SF}}},\qquad
\frac{k_{m,\mathrm{SF}}[2(n+1)h_m-z]}{\cos\theta_{m,\mathrm{SF}}}.
$$

来自 $B_{-1}(z)$ 的光只对透射SFG有贡献。

> **译者注（Q041续，E-2.2-002）：** 底本本部分同样反复使用「上向き（＋）」；其名称与第2部分“＋为下行”的定义不一致。本轮在下列各项保留“上行（＋）”的原称，按“下行（＋）”理解仅为候选，未确认替换；正负上标及相位式均照录。

### （c）$1/m$ 界面外侧的 $A_n'(0^-)$ 点

$$
x=-2nh_m\tan\theta_{m,\mathrm{SF}},\qquad z=0^-.
$$

- **上行（−）光：** $n=0$ 为反射SFG的零次光。
- **上行（＋）光（原文称呼）：** $n=0$ 在 $1/m$ 界面的反射光为反射SFG的零次光；$n=0$ 在该界面的透射光对透射SFG有贡献。$n=1,2,\ldots$ 在该界面的透射光对反射SFG和透射SFG均有贡献。

### （d）$1/m$ 界面内侧的 $A_n''(0^+)$ 点

$$
x=-2nh_m\tan\theta_{m,\mathrm{SF}},\qquad z=0^+.
$$

- **上行（−）光：** $n=0$ 在 $m/1$ 界面的透射光为反射SFG的一次光，在该界面的反射光为透射SFG的一次光；$n=1,2,\ldots$ 在该界面的反射光对反射SFG和透射SFG均有贡献。
- **上行（＋）光（原文称呼）：** $n=0$ 为透射SFG的零次光；$n=1,2,\ldots$ 对反射SFG和透射SFG均有贡献。

### （e）$m/2$ 界面内侧的 $B_n'(h_m^-)$ 点

$$
x=-(2n+1)h_m\tan\theta_{m,\mathrm{SF}},\qquad z=h_m^-.
$$

- **上行（−）光：** $n=0,1,2,\ldots$ 对反射SFG和透射SFG均有贡献。
- **上行（＋）光（原文称呼）：** $n=-1$ 在 $m/2$ 界面的透射光为透射SFG的零次光；$n=0,1,2,\ldots$ 在该界面的反射光对反射SFG和透射SFG均有贡献。

### （f）$m/2$ 界面外侧的 $B_n''(h_m^+)$ 点

$$
x=-(2n+1)h_m\tan\theta_{m,\mathrm{SF}},\qquad z=h_m^+.
$$

- **上行（−）光：** $n=-1$ 在 $m/2$ 界面的反射光为透射SFG的零次光；$n=0,1,2,\ldots$ 在该界面的透射光对反射SFG和透射SFG均有贡献。
- **上行（＋）光（原文称呼）：** $n=-1$ 为透射SFG的零次光。

'''
figures=r'''### 图3.1与光路汇总

上述路径示意如下。

![图3.1：薄膜内部的光传播；原图保留源点及坐标标记](../assets/ch02/ch02-s02-fig31.png)

图3.1：薄膜内部的光传播（原图）。$x$ 沿界面向右，$z$ 向下；箭头及源点撇号保留底本写法。

以下原文光路汇总跨第4—5页，旧译漏列，现补回；后附中文对照。为便于追溯，原图中的源点符号、界面次序和出射名称均不作修正。

![原文光路汇总第一部分：膜内源](../assets/ch02/ch02-s02-paths-a.png)

![原文光路汇总续：膜内源及各界面两侧源](../assets/ch02/ch02-s02-paths-b.png)

**膜内部**

| 原文源点与方向 | 经历的路径 | 原文出射名称 |
|---|---|---|
| $A_0,A_1,A_2,\ldots$，− | $n$重反射 → $1/m$透射 | 反射SFG |
| 同上 | $n$重反射 → $m/2$透射 | 透射SFG |
| $B_{-1}$，＋ | $m/2$透射 | 透射SFG |
| $B_0,B_1,B_2,\ldots$，＋ | $n$重反射 → $1/m$透射 | 反射SFG |
| 同上 | $n$重反射 → $m/2$透射 | 透射SFG |

**$1/m$ 界面的介质1侧**

| 原文源点与方向 | 经历的路径 | 原文出射名称 |
|---|---|---|
| $A_0'$，− | 直接出射 | 反射SFG |
| $A_0'$，＋ | $1/m$反射 → $m/2$透射 | 反射SFG |
| 同上 | $1/m$透射 | 反射SFG |
| $A_1',A_2',A_3',\ldots$，＋ | $1/m$透射 → 多重反射 → $1/m$透射 | 反射SFG |
| 同组另一分支 | $m/2$透射 | 透射SFG |

**$1/m$ 界面的薄膜侧**

| 原文源点与方向 | 经历的路径 | 原文出射名称 |
|---|---|---|
| $A_0''$，− | $1/m$透射 | 反射SFG |
| $A_0''$，− | $1/m$反射 → $m/2$透射 | 透射SFG |
| $A_1'',A_2'',A_3'',\ldots$，− | $1/m$反射 → 多重反射 → $1/m$透射 | 反射SFG |
| 同组另一分支 | $m/2$透射 | 透射SFG |
| $A_0''$，＋ | $m/2$透射 | 透射SFG |
| $A_1'',A_2'',A_3'',\ldots$，＋ | 多重反射 → $1/m$透射 | 反射SFG |
| 同组另一分支 | $m/2$透射 | 透射SFG |

**$m/2$ 界面的薄膜侧（下列撇号按汇总原文）**

| 原文源点与方向 | 经历的路径 | 原文出射名称 |
|---|---|---|
| $B_0'',B_1'',B_2'',\ldots$，− | 多重反射 → $1/m$透射 | 反射SFG |
| 同上 | $m/2$透射 | 透射SFG |
| $B_{-1}''$，＋ | $m/2$透射 | 透射SFG |
| $B_0'',B_1'',B_2'',\ldots$，＋ | $m/2$反射 → 多重反射 → $1/m$透射 | 反射SFG |
| 同组另一分支 | $m/2$透射 | 透射SFG |

**$m/2$ 界面的介质2侧（下列撇号按汇总原文）**

| 原文源点与方向 | 经历的路径 | 原文出射名称 |
|---|---|---|
| $B_{-1}'$，− | $m/2$反射 | 透射SFG |
| $B_0',B_1',B_2',\ldots$，− | $m/2$透射 → 多重反射 → $1/m$透射 | 反射SFG |
| 同组另一分支 | $m/2$透射 | 透射SFG |
| $B_{-1}''$，＋ | 直接出射 | 反射SFG |

> **译者注（Q042）：** 上表逐行翻译底本的流程，不是译者重新推导的路径表。底本第5页将 $m/2$ 薄膜侧标为 $B''$、介质2侧多标为 $B'$，与第3部分（e）、（f）及图3.1的撇号对应不同；最后直接出射一行又写 $B_{-1}''$。$A_0'$ 正向分支中的界面次序和“反射SFG”名称、最后一行的“反射SFG”名称也与邻近说明存在衔接疑点。原流程与正文分类分别照录，未用其中一套修正另一套。“同组另一分支”仅说明原图的分支排版，不补造前置界面过程。

'''
s=s[:start]+classification+figures+tail
s=s.replace('当前完成B058—B062：序论、坐标定义及第2—3页的式（2.1）—（2.6）；**第3部分“SFG光的光路”起仍为旧译待校订**。','当前完成B058—B064：序论、定义、式（2.1）—（2.6），以及跨第3—5页的六类光路、图3.1和光路汇总；**第4部分“光路上的SFG极化”起仍为旧译待校订**。')
p.write_text(s,encoding='utf-8');assert s[s.index('## 4. 光路上的SFG极化'):]==tail
for bid,part,scope in [('B063',classification,'p3—4，六类光源位置与相位、次数说明'),('B064',figures,'p4—5，图3.1及跨页光路汇总')]:
    (out/f'{bid}-本批译文.md').write_text(part,encoding='utf-8')
    (out/f'{bid}.md').write_text(f'# {bid} 校订记录\n\n2026-10-19。范围：{scope}。已目视对照原文p3.png、原文p4.png、原文p5.png；修订前全节备份B063-修订前.md。原文+光仍称上行，旧译擅改方向名称已恢复并关联Q041/E-2.2-002。恢复旧译遗漏的图与流程；流程撇号和出射名称疑点Q042保留。第4部分及以后未改。\n',encoding='utf-8')
# Opening metadata is part of the first batch.
(out/'B058-本批译文.md').write_text(s[:s.index('## 2. 准备')],encoding='utf-8')
rp=out/'检查排版.cjs';t=rp.read_text(encoding='utf-8').replace("'B061','B062']","'B061','B062','B063','B064']").replace('6[0-2]','6[0-4]');rp.write_text(t,encoding='utf-8')
q=mg/'疑难与勘误.md';t=q.read_text(encoding='utf-8')
t+='\nQ041续记（B063，2026-10-19）：第3部分（b）—（f）同样将+光写作上行，正文恢复原称，候选下行只在注释，E-2.2-002适用位置扩展至p3—4。\n\n| 编号 | 原文位置 | 疑点 | 类别/优先级 | 处理与状态 |\n|---|---|---|---|---|\n| Q042 | 2.2 p4—5图3.1及路径汇总 | 流程B′/B″侧别与分类(e)/(f)不同；部分界面路径及反射/透射名称衔接异常 | 原文图文关系/P1 | B064恢复全部原图和中文流程对照，原流程不修改，未以其中一套统一另一套；并列原文、就地说明，待核验。 |\n'
q.write_text(t,encoding='utf-8')
ep=root/'中文版本/附件/原文勘误表.md';t=ep.read_text(encoding='utf-8').replace('PDF第3页，式（2.5）前 | 正、负两种光均称','PDF第3—4页，式（2.5）前及第3部分（b）—（f） | 正、负两种光均称');ep.write_text(t,encoding='utf-8')
pp=mg/'当前进度与续接.md';t=pp.read_text(encoding='utf-8')
entry='''## 最新续接：2.2的B063—B064完成（2026-10-19）

已目视对照p3—5，完成第3部分(a)—(f)六类源点、相位、反射次数及贡献分类；恢复图3.1及旧译漏掉的跨p4—5全部路径汇总，附中文对照。Q041“上行+”原称在分类中照录，E-2.2-002扩展位置；Q042记录流程撇号和出射名称疑点，原流程未改，未新增确定勘误。

下一批从第4部分开始，连同p5末—p6的波长/偏振分量约定处理，再按4.1a等完整小节推进。第4部分起旧译与本批备份相同；当前覆盖至第3部分末，不将p5全页标为已核对。

''';pp.write_text(t.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
cp=mg/'章节清单.tsv';rows=list(csv.DictReader(io.StringIO(cp.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
    if row['编号']=='2.2':row['状态']='处理中：B058—B064，已至第3部分末';row['映射核验']='p1—5截至光路汇总；p5第4部分起未校订';row['公式图表范围']='式2.1—2.6、六类源点相位、图3.1及跨页路径汇总已覆盖'
buf=io.StringIO(newline='');w=csv.DictWriter(buf,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);cp.write_text(buf.getvalue(),encoding='utf-8-sig')
print('B063—B064及图像、管理记录已更新')

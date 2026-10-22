from pathlib import Path
import json,re
out=Path(__file__).resolve().parent
data=json.loads((out/'逐行提取.json').read_text(encoding='utf-8'))
rows={r['id']:r for p in data for r in p['lines']}
translation={};skip=set()
def setrange(start,end,text):
 keys=[k for k in rows if start<=k<=end]
 assert keys and keys[0]==start and keys[-1]==end,(start,end)
 translation[start]=text;skip.update(keys[1:])
def one(k,text):translation[k]=text
one('p03l14','## 5. 分子固定系中的和频张量')
one('p03l15','### 5.1 自由旋转')
one('p03l16',r'只需去掉含内部旋转角$\phi_A$、$\phi_B$的项。')
one('p03l31',r'### 5.2 $\phi_A=\phi_B=0,\pi$（两个三角形均朝下或均朝上）')
setrange('p03l32','p03l33',r'''当$\phi_A=\phi_B=0$时，$\cos\phi_A=\cos\phi_B=\cos2\phi_A=\cos2\phi_B=\cos3\phi_A=\cos3\phi_B=+1$；当$\phi_A=\phi_B=\pi$时，$\cos\phi_A=\cos\phi_B=\cos3\phi_A=\cos3\phi_B=-1$，$\cos2\phi_A=\cos2\phi_B=+1$。''')
one('p04l17',r'### 5.3 $\phi_A=\phi_B\ne0,\pi$（两个三角形如相互排斥般错开）')
one('p04l18',r'''此时，$\sin(n\phi_B)=-\sin(n\phi_A)$、$\cos(n\phi_B)=\cos(n\phi_A)$。

> **译者注（原文疑点Q171，PDF p4）：** 标题写$\phi_A=\phi_B$，随后却给出正弦互为相反数的关系；候选为两个局部旋转正方向有差别，或标题/关系式之一有误。原文未在此解释，标题与关系均保留，不改成反号角。''')
one('p05l07',r'''### 5.4 $\phi_A=0,\phi_B=\pi$或$\phi_A=\pi,\phi_B=0$

（一个三角形朝下，另一个也朝下。）

> **译者注（原文疑点Q168续，PDF p5）：** 本段标题仍重复“两者朝下”，原述保留；候选“一下、另一上”未采用。''')
one('p05l24',r'### 5.5 $\phi_A=-\phi_B\ne0,\pi$（两个三角形向同一侧倾斜）')
one('p06l13','## 6. 空间固定$(XYZ)$系中的张量分量')
setrange('p06l14','p06l16',r'''设分子固定$(xyz)$系通过欧拉角$(\chi,\theta,\phi)$与空间固定$(XYZ)$系重合。一般地求得的$(XYZ)$系张量分量如附录F所示。式中欧拉角与$(\mathrm{CH}_3)_2\mathrm X$基团取向的关系如下。''')
setrange('p06l17','p06l24',r'''**(1) 内部旋转角$\phi$：** 指CXC面相对于表面的扭转角，即绕$z$轴使分子面垂直于表面所需的旋转角；也可以说，是使$x$轴与$-Z$轴在$ab$面上的投影重合所需的旋转角。按此处$Z$轴的取向，朝$X$轴看去时$y$轴在左侧，因此CXC面向右上方倾斜时，对应正向旋转（小于$90^\circ$）。（取使沿$x$轴的矢量与沿$X$轴的矢量内积为正的重合方向。）

(a) 分子面垂直于表面时，$\phi=0$或$\pi$；CXC面与表面相对时，$\phi=\pi/2$或$3\pi/2$。(b) 两个甲基等价时，对于内部旋转角为$\phi$的基团，存在同等数量内部旋转角为$-\phi$的基团。(c) 若基团自由旋转，或其内部旋转角随机，则$\phi$以相同权重取$0$至$2\pi$内的任意值。''')
setrange('p06l25','p06l28',r'''**(2) 倾斜角（tilt角）$\theta_{\mathrm{tilt}}$：** 按通常定义，取$z$轴（CXC角平分线）与外向法线之间的角；绕$N$轴使$z$轴与外向法线重合的方向为正向旋转。由于$Z$轴为向下的法线，欧拉角$\theta=\pi-\theta_{\mathrm{tilt}}$。当基团的两个CH₃朝向真空侧时，$\theta_{\mathrm{tilt}}<\pi/2$。''')
setrange('p06l29','p06l34',r'''**(3) 面内取向角$\chi_{\mathrm{in\text{-}plane}}$（简记$\chi_{\mathrm{ip}}$）：** 指绕$Z$轴使$z$轴在$XY$面上的投影与$X$轴重合所需的旋转角。按此处$Z$轴的方向，沿$X$轴看去，投影位于左侧时为正。由于$Z$轴指向基板内部，对应欧拉角$\chi=\pi/2+\chi_{\mathrm{ip}}$。

(a) 投影后的CXC角平分线偏离$X$轴的角为$\alpha$时，$y$轴与$Y$轴的夹角也为$\alpha$。若该投影呈“八”字形，相对于$X$轴左右交替偏转，则$\chi_{\mathrm{ip}}$以$+\alpha$、$-\alpha$表示。(b) 面内取向随机时，$\chi_{\mathrm{ip}}$以相同权重取$0$至$2\pi$内的任意值。

> **译者注（原文疑点Q172，PDF p6）：** 此处原写投影到$ab$面，虽本段讨论基团$(xyz)$系，仍照录；候选为$xy$面，未采用。面内示例又用$\alpha$表示方位偏角，与前文CXC半角同符号，按本段语境辨认，不静默统一。此处$\phi$是整个基团的CXC面扭转角，与单个甲基内部角$\phi_A,\phi_B$分属不同坐标层级；偏移$\chi=\pi/2+\chi_{\mathrm{ip}}$也不改成4.4的$\pi$偏移。''')
setrange('p06l35','p07l01',r'''本文列出实际体系可能出现的几种情况：甲基自由旋转；固定在$\phi_A=\phi_B=0$或$\pi$；固定在$\phi_A=\phi_B\ne0,\pi$；以及固定在$\phi_A=0,\phi_B=\pi$或$\phi_A=\pi,\phi_B=0$时的张量分量。这四种情况具有以下共同关系。''')
one('p07l02',r'全对称振动中，$\beta_{zxx}=\beta_{xzx}$。')
one('p07l03',r'简并振动中，$\beta_{zxx}=\beta_{xzx}$、$\beta_{zyy}=\beta_{yzy}$；最后一种情况还满足$\beta_{yzx}=\beta_{zyx}$、$\beta_{zxy}=\beta_{xzy}$、$\beta_{xyz}=\beta_{yxz}$。')
setrange('p07l04','p07l06',r'''一般空间取向的表达式较长，故分别列于附录B、C、D、E，正文只列面内取向随机的表达式。（如果CXC面相对于表面的取向角$\phi$也随机，只需在下式中令$\cos(n\phi)=0$、$\sin(n\phi)=0$。）''')
setrange('p07l07','p07l08','其他取向的表达式可参考《CH₃基团的取向与和频张量》及《CH₂基团的取向与和频张量》求得。')
one('p07l09','### 6.1 自由旋转、面内随机取向\n\n一般取向的表达式见附录B。')
one('p09l28',r'### 6.2 $\phi_A=\phi_B=0,\pi$、面内随机取向'+'\n\n一般取向的表达式见附录C。')
one('p12l26',r'### 6.3 $\phi_A=\phi_B\ne0,\pi$、面内随机取向'+'\n\n一般取向的表达式见附录D。')
one('p16l25',r'### 6.4 $\phi_A=0,\phi_B=\pi$或$\phi_A=\pi,\phi_B=0$'+'\n\n一般取向的表达式见附录E。')
one('p19l18','## 附录A：(CH₃)₂X基团的和频张量')
one('p19l19','### 坐标系与甲基取向')
setrange('p19l20','p19l21',r'**1. 甲基固定坐标系——$(a,b,c)$系：** 沿$C_3$轴从C原子朝H原子的方向取$c$轴，使三个CH键之一位于$ac$面内。')
setrange('p19l22','p19l23',r'**2. 基团固定坐标系——$(x,y,z)$系：** 沿两个甲基$C_3$轴的角平分线取$z$轴，从X原子指向甲基为正方向。在两条$C_3$轴所成的平面内取$x$轴。')
setrange('p19l24','p19l27',r'**3. 甲基取向：** 令$z$轴与甲基分子轴的夹角（即CXC角的一半）为$\alpha$。用下标A、B区分两个甲基，其内部旋转角分别为$\phi_A,\phi_B$。以三个H原子构成的正三角形有一个顶点朝向表面的状态为基准，此时$\phi_A=0,\phi_B=0$；正三角形的一条边靠近表面时，内部旋转角为$180^\circ$。')
setrange('p19l28','p19l29','只有“简并振动”谱带的和频张量会随内部旋转角变化。因此，可以从简并谱带的表现了解甲基的相对取向及旋转情况。')
setrange('p19l30','p19l31',r'**4. 欧拉角——$(\chi,\theta,\phi)$：** 设CXC角为$2\alpha$，将两个甲基坐标系分别与分子固定系重合时，欧拉角为$(0,\alpha,\phi)$和$(\pi,\alpha,\phi)$（据此确定$b$轴方向）。')
one('p19l32','在张量分量变换式中：')
setrange('p20l02','p20l05',r'使用另文《变换矩阵$(xyz)$》或 *Appl. Spectrosc.* 论文表中列出的系数$U_{ijk:abc}$，可求得以下$(xyz)$系和频张量分量。（对于倾斜角$\theta$，不采用表中$\sin\theta$、$\sin2\theta$、$\sin3\theta$的形式，而采用经下列关系转换得到的$\sin\theta$、$\cos\theta$的幂表达式。）')
one('p20l10','（表达式与两个甲基的相对取向无关。）')
one('p22l04','## 附录B：自由旋转时$(XYZ)$系中的张量分量')
one('p30l06',r'## 附录C：$\phi_A=\phi_B=0,\pi$时$(XYZ)$系中的张量分量')
one('p38l30',r'## 附录D：$\phi_A=\phi_B\ne0,\pi$时$(XYZ)$系中的张量分量')
one('p49l29',r'## 附录E：$\phi_A=0,\phi_B=\pi$或$\phi_A=\pi,\phi_B=0$时$(XYZ)$系中的张量分量')
one('p58l21','## 附录F：空间固定$(XYZ)$系中的张量分量（一般式）')
setrange('p62l23','p62l24',r'''这里给出的张量$XYZ$分量表达式，是适用于分子固定系张量左侧两个下标交换后相等，即$\beta_{ijk}=\beta_{jik}$时的一般式。

> **译者注（适用条件）：** 附录F后半的一般式明示左侧两个下标的交换条件，不能将此条件扩大为任意下标全置换对称。后续保留其$a,b,c$下标，依原文说明替换为$x,y,z$后再代入双甲基表达式。''')
one('p63l27','将以上关系代入下式，即得两个甲基的表达式（先将$abc$改为$xyz$）。')

# Repeated prose is translated at every occurrence; formulas remain source-local.
def automatic(k,raw):
 raw=raw.replace('［ ','［')
 if '［全対称バンド］' in raw or (k=='p16l29'):
  title='#### 全对称谱带\n\n' if '［' in raw else ''
  if raw.strip()=='［全対称バンド］':return title.strip()
  return title+r'当$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时，$\beta_{aac}\sim(4/9)\beta_{\zeta\zeta\zeta}$、$\beta_{ccc}\sim(1/9)\beta_{\zeta\zeta\zeta}$。'
 if '［縮重バンド］' in raw:
  if raw.strip()=='［縮重バンド］':return '#### 简并谱带'
  return '#### 简并谱带\n\n'+r'当$\beta_{\zeta\zeta\zeta}\gg\beta_{\xi\xi\zeta},\beta_{\eta\eta\zeta}$时，$\beta_{caa}\sim(4/9)\beta_{\zeta\zeta\zeta}$、$\beta_{aaa}\sim(4\sqrt2/9)\beta_{\zeta\zeta\zeta}$。'
 if '原理的には振動バンド' in raw:
  num='两' if '２つ' in raw else '三'
  return '原则上，振动谱带会分裂为'+num+'个；若实际相互重叠，则应将下面'+num+'个谱带表达式相加，用于拟合测得的光谱。'
 if any(x in raw for x in ['ンドに対する表式について','に対する表式について和を取った','バンドに対する表式について']):return ''
 if '［対称' in raw:
  return '##### 对称$(a_1)$振动'+('，沿$c$轴的振动' if 'c軸' in raw else '')
 if '［逆対称' in raw:
  return '##### 反对称$(b_1)$振动'+('，沿$a$轴的振动' if 'a 軸' in raw else '')
 if '［面外' in raw:
  return '##### 面外$(b_2)$振动'+('，沿$b$轴的振动' if 'b 軸' in raw else '')
 if 'グループ' in raw:return '#### 第'+re.search(r'\d+',raw)[0]+'组'
 if ('軸方向の振動が' in raw and '寄与' in raw):return r'（$\beta_{zyy}$和$\beta_{yzy}$由$b$轴方向振动贡献，其他分量由$a$轴方向振动贡献。）'
 if '面外振動と面内振動を分ける' in raw:return '（为便于区分面外与面内振动，分别处理$a$轴与$b$轴方向的振动。）'
 if '上側が a軸' in raw:return '（$\pm$的上号对应$a$轴方向振动，下号对应$b$轴方向振动。）'
 if '上側が  φ' in raw:return r'（$\pm$的上号对应$\phi_A=\phi_B=0$，下号对应$\phi_A=\phi_B=\pi$。）'
 if '上側は' in raw:return r'（$\pm$的上号对应$\phi_A=0,\phi_B=\pi$，下号对应$\phi_A=\pi,\phi_B=0$。）'
 if 'であるから' in raw:
  t=raw.split('であるから')[0].strip()
  note=''
  if t.count('(')!=t.count(')'):
   note='\n\n> **译者注（原式分组疑点Q174，PDF p'+str(int(k[1:3]))+'）：** 上述代入关系末尾多一个右圆括号，照原保留；候选为删除多余右括号，未采用。'
  return '由于$'+tex(t)+'$，得到：'+note
 if 'とすると' in raw:
  return r'''（若$\beta_{\xi\xi\zeta}\gg\beta_{\xi\xi\zeta}\sim\beta_{\eta\eta\zeta}$，则$\beta_{caa}=\beta_{\zeta\zeta\zeta}(\cos\alpha-\cos^3\alpha)\sim(2\sqrt3/9)\beta_{\zeta\zeta\zeta}$（Td）、$(3/8)\beta_{\zeta\zeta\zeta}$（sp²）。）

> **译者注（原文疑点Q173，PDF p12、p15）：** 原近似条件首项与比较项都写$\beta_{\xi\xi\zeta}$，保留原式；首项候选为$\beta_{\zeta\zeta\zeta}$，未采用。此处$\alpha$及三角系数也按本节原述保留，不据其他章节替换。'''
 raise ValueError((k,raw))

# Load only extraction helpers, without repeating the full PDF extraction.
namespace={}
exec((out/'提取数学.py').read_text(encoding='utf-8').split('doc=pdfplumber.open')[0].replace('out=Path(__file__).resolve().parent;root=out.parents[2]','out=Path(r"'+str(out)+'");root=out.parents[2]'),namespace)
tex=namespace['tex']
for k,r in rows.items():
 if k<'p03l14' or not r['jp'] or k in skip:continue
 if k not in translation:translation[k]=automatic(k,r['raw'])
(out/'叙述译文映射.json').write_text(json.dumps({'translation':translation,'skip':sorted(skip)},ensure_ascii=False,indent=2),encoding='utf-8')
print('prose entries',len(translation),'joined continuation lines',len(skip))

from pathlib import Path
import json,re,hashlib
r=Path(__file__).resolve().parents[2];o=r/'翻译管理/校订记录/第五章收尾';d=r/'中文版本/第五章 张量与对称性'
assets=r/'中文版本/assets/ch05';manifest=json.loads((o/'公式图表资源.json').read_text(encoding='utf-8'));meta=json.loads((o/'底本及页面.json').read_text(encoding='utf-8'))
def img(x,caption):return f'![{caption}](../assets/ch05/{x["资源"]})\n\n'
def find(sec,p,t):return next(x for x in manifest if x['节']==sec and x.get('页')==p and x.get('表')==t)
def table(sec,p,t):
 x=find(sec,p,t);return f'原PDF p{p}，第{t}表；行列与系数均依底本。\n\n'+img(x,f'{sec} PDF p{p} 第{t}表')
for sec in ['5.4','5.5','5.6']:
 p=next(d.glob(sec+' *.md'));text=p.read_text(encoding='utf-8')
 text=re.sub(r'<!-- TABLE:([\d.]+):(\d+):(\d+) -->',lambda m:table(m[1],int(m[2]),int(m[3])),text)
 text=re.sub(r'<!-- TABLES:([\d.]+):(\d+) -->',lambda m:'\n'.join(table(m[1],int(m[2]),x['表']) for x in manifest if x['节']==m[1] and x.get('页')==int(m[2])),text)
 if sec=='5.4':
  blocks=[]
  for pn in range(5,13):
   group=f'{(pn-5)//2+1}-{(pn-5)%2+1}';blocks.append(f'### 5.{pn-4} 第{group}组（PDF p{pn}）\n\n'+table(sec,pn,1))
  text=text.replace('<!-- GROUPS:5.4 -->','\n'.join(blocks))
 if sec=='5.6':
  blocks=[]
  for pn in range(2,38):
   group='ABCD'[(pn-2)//9];n=(pn-2)%9+1
   note=''
   if pn==3:note='> **原文显示疑点（Q228）：** A-2表的zzx行、bab列第二行式首在底本显示为方框；保留原图，不猜填符号。A-3表（p4）的xxx行、aab列也有方框，处理相同。\n\n'
   blocks.append(f'## {pn+1}. 和频张量{group}-{n}（PDF p{pn}）\n\n'+table(sec,pn,1)+note)
  text=text.replace('<!-- MATRICES:5.6 -->','\n'.join(blocks))
 assert '<!-- TABLE' not in text and '<!-- GROUPS' not in text and '<!-- MATRICES' not in text
 p.write_text(text,encoding='utf-8')
p=next(d.glob('5.3 *.md'));text=p.read_text(encoding='utf-8');text=re.sub(r'\n<!-- B473结束：[\s\S]*?-->\s*$','\n',text)
text=text.replace('B473完成PDF p1原目录及第1—3部分的翻译和原页对照；p2起第4部分的张量展开尚未翻译。本文件为分批稿。','B473—B500覆盖全16页；正文与81条完整分量式已整理，参考排版验收另见管理记录。密集展开式采用保真图式，跨页式已接成同一条公式。')
text=text.replace('本稿在分子张量前两个指标可互换的条件下，将分子固定系分量变换为空间固定系分量。先读首页的适用范围、坐标与三个取向角定义，再读后续按c、a、b轴振动分组的展开式。后续公式仅作结构预览，尚需逐组对照；本节Z轴向内，不能套用法线向外的角度关系。','本稿在分子张量前两个指标可互换的条件下，将分子固定系分量变换为空间固定系分量。先读适用范围、坐标与三个取向角，再按c、a、b轴振动查找完整分量式。本节Z轴向内，不能套用法线向外的角度关系。')
intro=r'''
## 4. 空间固定(XYZ)系中的张量分量（PDF p2—16）

设分子固定(xyz)系经欧拉角 $(\chi,\theta,\phi)$ 所表示的旋转后与空间固定(XYZ)系重合，由此求(XYZ)系中的张量分量。

假定分子固定系的非零分量及其相互关系如下：

$$
\begin{aligned}
&\beta_{aac},\quad\beta_{bbc},\quad\beta_{ccc},\quad
\beta_{abc}=\beta_{bac},\quad\beta_{acc}=\beta_{cac},\quad\beta_{bcc}=\beta_{cbc},\\
&\beta_{aaa},\quad\beta_{bba},\quad\beta_{cca},\quad
\beta_{baa}=\beta_{aba},\quad\beta_{caa}=\beta_{aca},\quad\beta_{bca}=\beta_{cba},\\
&\beta_{bbb},\quad\beta_{aab},\quad\beta_{ccb},\quad
\beta_{cbb}=\beta_{bcb},\quad\beta_{cab}=\beta_{acb},\quad\beta_{abb}=\beta_{bab}.
\end{aligned}
$$

> **图式与记号说明（译者）：** 下列81条是原式的清晰保真图，不是由文字提取结果重算的公式。每条标明原PDF页码；跨页式已在同一图中顺序拼接。β为分子一阶超极化率，对应二阶场响应；χ依底本表示空间分量。倍角与函数幂依原字形位置区分，例如 $\sin3\chi$ 与 $\sin^3\theta$ 不可混读。xyz记号仍按Q221保留。ppp、spp等偏振标签依原式保留，不另行推定频率顺序。

'''
forms=[x for x in manifest if x['节']=='5.3'];assert len(forms)==81
parts=[]
for f in forms:
 idx=f['序号'];axis=f['轴'];local=(idx-1)%27+1;pages='、'.join(str(x['页']) for x in f['片段'])
 heading=''
 if local==1:
  heading=f'### 4.{(idx-1)//27+1} 沿{axis}轴的振动'+('（译者按分量分组）' if axis=='b' else '')+'\n\n'
  if axis=='b':heading+='> **编排说明（译者）：** 底本p10在a轴组末式之后直接开始含βcbb等分量的ppp式，没有另印“沿b轴的振动”标题。此处依首页的三轴分类和该组分量增加阅读标题；原公式及其先后次序未改。\n\n'
 block=heading+f'#### {axis}轴组第{local}式：$\\chi_{{{f["分量"]}}}$（原PDF p{pages}）\n\n'+img(f,f'{axis}轴组 χ{f["分量"]} 完整原式，PDF p{pages}')
 parts.append(block)
text+='\n'+intro+''.join(parts)
text+='\n> **全节保留说明（译者）：** 对公式中可能存在的括号不配对、重复项或相邻分量差异，均保留底本，不以对称性推测作替换。以上完成的是译文与底本内容、排版的对照，不声称已独立验证81条展开式的物理及代数正确性。\n'
p.write_text(text,encoding='utf-8')
# Readable, independently traceable batches: three whole formulas per batch in 5.3;
# subsequent sections use source-page or complete source-table units.
batches=[]
def add(sec,n,chunk,pages,objects):
 folder=r/f'翻译管理/校订记录/{sec}';folder.mkdir(exist_ok=True)
 bid=f'B{n}';snapshot=f'# {bid}｜{sec}\n\n'+chunk.strip()+'\n';(folder/f'{bid}-本批译文.md').write_text(snapshot,encoding='utf-8')
 source=next(x for x in meta if x['节']==sec)
 coverage=[]
 for pn in sorted(set(pages)):
  jp=source['页面'][pn-1]['日语行']; coverage.append({'原文定位':f'PDF p{pn}','项目':'本批原段落或公式片段','日语文字定位':jp,'译文定位':f'{bid}-本批译文.md','已翻译':True,'已原页对照':True,'备注':'页码为所含对象来源；跨页公式按完整式计，不把同页其他批次对象重复计数。'})
 record={'批次':bid,'节':sec,'原页':sorted(set(pages)),'对象':objects,'来源SHA256':source['sha256'],'译文SHA256':hashlib.sha256(snapshot.encode('utf-8')).hexdigest(),'已起草':True,'已原页对照':True,'已排版':False,'公式处理':'LaTeX说明式及原式/原表图；无推测补字','采用原文修正':False}
 (folder/f'{bid}-覆盖.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
 (folder/f'{bid}验收.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
 batches.append(record)
for j in range(27):
 chunk=('## 4. 空间固定(XYZ)系中的张量分量\n'+intro.split('## 4.',1)[1].split('\n',1)[1] if j==0 else '')+''.join(parts[j*3:j*3+3])
 fs=forms[j*3:j*3+3];add('5.3',474+j,chunk,[z['页'] for f in fs for z in f['片段']],[{'类型':'完整分量式','轴':f['轴'],'分量':f['分量'],'序号':f['序号'],'资源':f['资源'],'来源片段':f['片段']} for f in fs])
# Split at major headings; selected headings contain several source pages and are
# subdivided at their explicitly labelled lower headings.
def between(t,start,end=None):
 a=t.index(start);b=t.index(end,a+len(start)) if end else len(t);return t[a:b]
t=next(d.glob('5.4 *.md')).read_text(encoding='utf-8')
chunks=[(501,[1],between(t,'# 5.4','## 2.')),(502,[2],between(t,'## 2.','## 4.')),(503,[3],between(t,'## 4.','### 4.2')),(504,[4],between(t,'### 4.2','## 5.'))]
for pn in range(5,13):
 h=f'### 5.{pn-4} ';nxt=f'### 5.{pn-3} ' if pn<12 else '## 6.';c=between(t,h,nxt)
 if pn==5:c=between(t,'## 5.',h)+c
 chunks.append((500+pn,[pn],c))
chunks.extend([(513,[13],between(t,'## 6.','原PDF p14')),(514,[14,15],between(t,'原PDF p14'))])
for n,pages,c in chunks:add('5.4',n,c,pages,[x for x in manifest if x['节']=='5.4' and x['页'] in pages])
t=next(d.glob('5.5 *.md')).read_text(encoding='utf-8')
chunks=[(515,[1],between(t,'# 5.5','## 2.')),(516,[2],between(t,'## 2.','## 3.')),(517,[3],between(t,'## 3.','## 4.')),(518,[4],between(t,'## 4.','### 4.2')),(519,[5],between(t,'### 4.2','### 4.3')),(520,[6],between(t,'### 4.3','### 4.4')),(521,[7],between(t,'### 4.4','## 5.')),(522,[8],between(t,'## 5.','### 5.3'))]
for pn in range(9,14):
 h=f'### 5.{pn-6} ';nxt=f'### 5.{pn-5} ' if pn<13 else None;chunks.append((514+pn,[pn],between(t,h,nxt)))
for n,pages,c in chunks:add('5.5',n,c,pages,[x for x in manifest if x['节']=='5.5' and x['页'] in pages])
t=next(d.glob('5.6 *.md')).read_text(encoding='utf-8');add('5.6',528,between(t,'# 5.6','## 3.'),[1],[{'类型':'旋转矩阵与六条三角关系式；译者查表目录'}])
for pn in range(2,38):add('5.6',527+pn,between(t,f'## {pn+1}.',f'## {pn+2}.' if pn<37 else None),[pn],[find('5.6',pn,1)])
(o/'本轮批次.json').write_text(json.dumps(batches,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'新批次{len(batches)}：{batches[0]["批次"]}—{batches[-1]["批次"]}；图式与译稿已组织，等待排版。')

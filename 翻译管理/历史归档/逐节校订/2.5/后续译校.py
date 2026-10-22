from pathlib import Path
import re,json
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.5 *.md'));bs=chr(92)
old=P.read_text(encoding='utf-8');assert not (O/'B136-修订前.md').exists();(O/'B136-修订前.md').write_text(old,encoding='utf-8')
def tx(s):return s.replace('§',bs)
def note(s):return '\n\n> '+tx(s)+'\n\n'
def sub(s,a,z):return s[s.index(a):s.index(z,s.index(a))]
def mathmap(s):
 d={}
 for m in re.finditer(r'\$\$([\s\S]*?)\$\$',s):
  tags=re.findall(re.escape(bs)+r'tag\{([^}]+)\}',m[1])
  if len(tags)==1:d[tags[0]]=m.group(0)
 return d
def edit_eq(s,tag,fun):
 pattern=r'\$\$([\s\S]*?)\$\$'
 def work(m):return '$$'+fun(m[1])+'$$' if bs+'tag{'+tag+'}' in m[1] else m[0]
 return re.sub(pattern,work,s)
def clean(s):
 return s.replace('感受率张量','二阶非线性极化率张量').replace('Fresnel 系数','菲涅尔因子').replace('Snell','斯涅尔').replace('Brewster','布儒斯特').replace('Maxwell','麦克斯韦').replace('SFG 极化','和频极化').replace('向上(-)光','上行（−）光').replace('向下(+)光','下行（+）光').replace('$E^+$ sources','$E^+$ 源点').replace('$E^-$ sources','$E^-$ 源点')
parts=[]
def save(batch,s,pages,desc):
 s=clean(s);parts.append(s);(O/(batch+'-本批译文.md')).write_text(s,encoding='utf-8');tags=re.findall(re.escape(bs)+r'tag\{([^}]+)\}',s)
 (O/(batch+'-覆盖.json')).write_text(json.dumps({'batch':batch,'date':'2026-10-20','pages':pages,'units':desc,'tags':tags,'source_pages_visually_checked':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
 (O/(batch+'.md')).write_text('# '+batch+'：2.5译校\n\n独立底本PDF p'+ '、'.join(map(str,pages))+'。'+desc+'。已对独立原图与文字层逐项核验；重合数学只作录入候选，按本文件编号和局部差异输出。未采用原文公式修正，候选只注；后续排版验收见整节完成复核。\n',encoding='utf-8')

s=sub(old,'## 4.1 激发电场','### 4.1a.')
# One original line per displayed row prevents a six-column alignment from stretching the page.
s=s.replace(', &',',§qquad ').replace(' &', ' &')
save('B136',s,[2],'波长与复数说明、两组轴向反射关系、四组轴向透射关系及两个乘积恒等式')
s=sub(old,'### 4.1a.','## 4.2 SFG')
s=edit_eq(s,'4.15',lambda x:x.replace('r_{m2,vis,§beta}'.replace('§',bs),'r_{m2,ivis,§beta}'.replace('§',bs)))
s+=note('**原文疑点（Q085，PDF p3，式4.15）**：可见光分母原写 $r_{m2,ivis,§alpha}$，保留其中的 $ivis$；候选 $vis$ 未采用。该小节标题中的位置原写 $z=h^+$，未补膜下标。')
s+=note('**原文疑点（Q044／Q047关联，PDF p3—4）**：4.1g的B源点位置为 $x=-(2(n+1)h_m-z)§tan§theta_{m,§mathrm{SF}}$，而式4.21外部相位含 $2n+1$；两处原值保留。4.1d引用附录C，但本独立文件实际只附A与D，不补造C。')
save('B137',s,[2,3,4],'双介质两侧与膜两界面各侧的激发场，以及膜内A/B四项场乘积；4.21跨p3—4完整接续')
s=sub(old,'## 4.2 SFG','## 5.1 L')
s=edit_eq(s,'4.26a',lambda x:x.replace(')]',')]§big§}'.replace('§',bs)))
s=edit_eq(s,'4.28a',lambda x:x.replace('r_{m2,vis,§beta}'.replace('§',bs),'r_{m2,wvis,§beta}'.replace('§',bs)))
s=edit_eq(s,'4.29',lambda x:x.replace('E^0_{ir,§gamma}'.replace('§',bs),'E^0_{ir,§gamma}e'.replace('§',bs),1))
s+=note('**原文疑点（Q061／Q062／Q063关联，PDF p4—6）**：式4.26a的两行相位之后各有未配对右花括号，照录可见符号；4.28a写 $wvis$；4.29在两入射场后有孤立 $e$。这些均不以旧译的规范化形式代替原文。')
s+=note('**原文疑点（Q064／Q047关联，PDF p5—7）**：4.30a的vis反射系数配ir相位、ir系数配vis相位，且另有不含求和序号n的外部相位；均保留。4.2b按原文引用4.13，而本独立文件此处激发场编号为4.12；不改号。')
save('B138',s,[4,5,6,7],'二阶非线性极化率定义、五类源点极化、完整薄膜两组及额外无编号场关系；4.28b和4.30b跨页接全')

def split_tags(s):
 def one(m):
  t=m[1];tags=re.findall(re.escape(bs)+r'tag\{([^}]+)\}',t)
  if len(tags)<=1:return m[0]
  t=t.replace(bs+'begin{aligned}','').replace(bs+'end{aligned}','').strip();result=[];pos=0
  for tag in tags:
   loc=t.index(bs+'tag{'+tag+'}',pos);chunk=t[pos:loc].strip();chunk=re.sub(r'^\\\\(?:\[[^]]+\])?\s*','',chunk).strip();chunk=re.sub(r'\\\\(?:\[[^]]+\])?\s*$','',chunk).strip()
   result.append('$$\n'+bs+'begin{aligned}\n'+chunk+'\n'+bs+'end{aligned}'+bs+'tag{'+tag+'}\n$$')
   pos=loc+len(bs+'tag{'+tag+'}')
  return '\n\n'.join(result)
 return re.sub(r'\$\$([\s\S]*?)\$\$',one,s)
s=sub(old,'## 5.1 L','## 5.2a.')
s=s.replace('向下(+)光','上行（+）光（原文称谓）')
s=split_tags(s)
s+=note('**原文疑点（Q041关联，PDF p7）**：本段两次将“+”光也写作上向。这里保留原称；下行仅为候选名称，不改系数符号。式5.6—5.9的场与极化位置按原文只写0或 $h_m$，不从2.4移入其两侧上标，也不移入该文件的 $P_y(00^+)$ 字样。')
save('B139',s,[7,8],'L定义、公共因子、十五条系数关系及十二个源点出射场；保留本文件的式号与位置简写')

# Independent p8—15 checked: use the already editable parallel expressions only after comparing each source group.
candidate=next(D.glob('2.4 *.md')).read_text(encoding='utf-8');cm=mathmap(candidate)
mapping={**{'5.'+str(13+i)+l:str(1+i)+l for i in range(7) for l in 'ab'},**{'5.'+str(20+i)+l:str(2+i*2)+l for i in range(3) for l in 'ab'},**{'5.21'+l:'4'+l for l in 'ab'},**{'5.24'+l:'12'+l for l in 'ab'},**{'5.25'+l:'10'+l for l in 'ab'},**{'5.26'+l:'14'+l for l in 'ab'}}
# Reflection groups map 1,3,5,7,9,11,13 rather than a consecutive list.
for i,num in enumerate([1,3,5,7,9,11,13]):
 for l in 'ab':mapping['5.'+str(13+i)+l]=str(num)+l
def replace_math(s):
 def one(m):
  tags=re.findall(re.escape(bs)+r'tag\{([^}]+)\}',m[1])
  if len(tags)!=1 or tags[0] not in mapping:return m[0]
  tag=tags[0];return cm[mapping[tag]].replace(bs+'tag{'+mapping[tag]+'}',bs+'tag{'+tag+'}')
 return re.sub(r'\$\$([\s\S]*?)\$\$',one,s)
s=sub(old,'## 5.2a.','## 5.2e.')
s=replace_math(s)
s+=note('**原文疑点（Q082关联，PDF p10，式5.16a/b）**：保留 $wvis$、省略SF的系数下标、分母基线数字2及随后指数缺i的写法；5.16b出射分子指数亦未见i。常规分母与相位仅列为候选，不用于正文。')
save('B140',s,[8,9,10,11],'各界面源点的八组反射场5.13—5.18；含完整薄膜组、5.13a/5.15b/5.18a跨页')
s=sub(old,'## 5.2e.','## 5.3 透射')
s=replace_math(s)
s+=note('**原文疑点（Q084／Q053关联，PDF p11—12）**：5.19前因子为 $i/§delta$，旧译 $i§delta$ 已按原页恢复。vis/ir交叉相位、前两项1/m与后两项m/m层标混用及原花括号闭合不齐均照录。净场强度的“和的平方”也按原措辞保留；复振幅可观测强度通常涉及模平方，此处不擅改作者表述。')
save('B141',s,[11,12],'体相p/s反射长式各四个积分项及净反射场说明')
s=sub(old,'## 5.3 透射','### 5.3e.')
s=replace_math(s)
s+=note('**原文疑点（Q080／Q081／Q083关联，PDF p12—14）**：5.20的L层标为m/1；5.21分母末项用反向界面下标且带未配对右括号；5.24有孤立e；5.25左端缺“+”。分别保留原值，不把相邻公式代为统一。')
save('B142',s,[12,13,14],'透射范围说明、前后界面各侧与完整薄膜组5.20—5.25，跨页完整接续')
s=sub(old,'### 5.3e.','## 附录 A')
s=replace_math(s)
s+=note('**原文疑点（Q084／Q053关联，PDF p15—16）**：5.26的前因子同样为 $i/§delta$；未把旧译乘积当作原式。净透射场的“和的平方”按原措辞保留。长式同分母分子拆为分行分式，仅为排版，各项完整展开。')
save('B143',s,[15,16],'体相p/s透射全式5.26a/b及跨p15—16的净透射说明')

# Appendix A: compare the independent pages, then transfer editable formulas with the local printed peculiarities intact.
c3=next(D.glob('2.3 *.md')).read_text(encoding='utf-8');s=sub(c3,'## 附录A.','## 附录B.')
s=s.replace('第2.2节SFG正文','本节和频正文').replace('本底本','本独立底本').replace('第2.2节PDF p35亦有相同字形，已同步修复先前转写漏字；这属于转写修复，不是对原文公式作修正。','2.5 PDF p16亦有同样四处额外上标；已逐项对原页保留，属于转写恢复。')
s=s.replace('正文和本节尚待校订的附录B、C与第2.2节主要使用','本节正文以及第2.2节主要使用')
s=s.replace('PDF p1','PDF p16').replace('PDF p2','PDF p17').replace('PDF p3','PDF p18')
s+=note('**独立底本说明（译者）**：以上A.1—A.12已对2.5 PDF p16—18重核；采用正时间指数，χ为线性极化率。A.6角度额外平方、入射y场的ri下标及反向t21/t12混写等均保留；不从其他章节带入已推定的修正。')
save('B144',s,[16,17,18],'附录A全式与无编号边界、轴分量及强度关系；局部正时间约定、额外平方与下标原值')
s=(R/'翻译管理/校订记录/2.3/B122-本批译文.md').read_text(encoding='utf-8')
s=s.replace('本独立PDF不含这些正文公式；所引用（4.29）—（4.36）与第2.2节现有正文编号也不匹配。第2.2节界面和片内L系数集中于5.1','本独立PDF的4.29—4.30为极化表达式，所引用4.29—4.36并非本节L系数编号。本节界面和片内L系数集中于5.1')
s=s.replace('独立PDF p10—11','独立PDF p18—19').replace('独立PDF p12','独立PDF p20').replace('独立PDF p11','独立PDF p19')
save('B145',s,[18,19,20],'附录D六条完整多重反射证明链；原引用编号、层标及最终Pz的2n1因子按独立原页核验')
new=old[:old.index('## 4.1 激发电场')]+''.join(parts)
assert new.startswith(old[:old.index('## 4.1 激发电场')]);P.write_text(new,encoding='utf-8')
print('B136—B145 written',len(new),len(re.findall(re.escape(bs)+r'tag\{([^}]+)\}',new)))

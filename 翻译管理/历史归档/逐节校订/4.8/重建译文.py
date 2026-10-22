from pathlib import Path
import json,re,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.8 氢化金刚石表面CH的和频张量.md'
snap=out/'重建前旧译.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
data=json.loads((out/'字形行.json').read_text(encoding='utf-8'))
events=[]
def event(p,y,s):events.append({'page':p,'y':y,'kind':'prose','text':s})
event(3,303,r'''## 3. 分子固定$(abc)$系中的张量分量

由对称性可筛出非零分量。C₂ᵥ分子（CH₂及平面HCCH基团）为$\beta_{aac}$、$\beta_{bbc}$、$\beta_{ccc}$、$\beta_{caa}=\beta_{aca}$、$\beta_{cbb}=\beta_{bcb}$；C₂分子（扭转HCCH基团）还允许$\beta_{abc}=\beta_{bac}$、$\beta_{bca}=\beta_{cba}$、$\beta_{cab}=\beta_{acb}$。若假设可直接沿用CH键的张量分量，则可参照《欧拉角》及《从分子固定系到空间固定系》估算各分量。

### CH₂基团

根据《欧拉角》式(Eu-5)，两个CH键的$\chi$相差$\pi$，故含$\sin\chi$、$\sin3\chi$、$\cos\chi$、$\cos3\chi$的项相加为零。又因$\chi=0,\pi$，有$\sin2\chi=0$、$\cos2\chi=1$，含$\sin2\chi$和$1-\cos2\chi$的项也为零。$\phi=0$时，各正弦及$1-\cos2\phi$项均消失，各余弦均为1。按《从分子固定系到空间固定系》叠加两个CH键的张量，得到下式。
''')
event(3,613,'CH伸缩振动无$b$轴方向的分量，因此最右侧下标为$b$的张量分量为零。')
event(3,646,r'取HCH角为四面体角，则$\cos\alpha=-1/3$、$\sin\alpha=2\sqrt2/3$，故$\cos(\alpha/2)=\sqrt{1/3}$，可得：')
event(4,74,r'注意：与单独CH基团不同，这里$\beta_{aac}\sim\beta_{ccc}$。')
event(4,107,r'### 平面HCCH基团'+'\n\n'+r'推导与上面相同。《欧拉角》的(Eu-6)与(Eu-5)相比，以$\alpha-\pi/2$代替$\alpha/2$；这里$\alpha$指HCC角。因而得到：')
event(4,270,r'取HCC角为四面体角，$\cos\alpha=-1/3$、$\sin\alpha=2\sqrt2/3$，得到：')
event(4,385,r'这里应注意$\beta_{aac}<\beta_{ccc},\beta_{caa}$。')
event(4,417,r'### 扭转HCCH基团'+'\n\n'+r'先根据《欧拉角》的(Eu-8)、(Eu-10)、(Eu-10)得到欧拉角表达式，再将欧拉角与HCC角及二面角联系起来。这一步较为繁复。《从分子固定系到空间固定系》给出的欧拉角表达式如下。原文重复列出(Eu-10)，照录。')
event(5,139,r'将这些式子改写成$\alpha$与$\tau$的表达式，直接代换后整理，得到：')
event(5,335,r'取HCC角为四面体角，$\cos\alpha=-1/3$、$\sin\alpha=2\sqrt2/3$，得到：')
event(5,515,r'## 4. 表面固定$(xyz)$系中HCCH基团的张量分量'+'\n\n'+r'以下求典型取向的表面系张量。附录A给出一般取向的表达式，代入相应欧拉角即可得到各式。下文$\tau$指分子面（$ac$面）与表面（$xy$面）之间的二面角。')
event(5,597,r'### 4a. 倾斜的平面HCCH基团'+'\n\n'+r'设分子面$ac$相对表面倾斜$\tau$。两种倾斜方式对应的欧拉角如下，参见《欧拉角》式(Eu-4)。$\alpha$为CCH键角。')
event(5,728,r'相邻HCCH基团交替取$-\tau$和$+\tau$，据此得到下列分量。')
event(6,450,'用CH基团张量表示时，在式(3-6)中取四面体角，即使用式(3-8)，得到下式。')
event(7,172,r'### 4b. 扭转HCCH基团'+'\n\n'+r'扭转HCCH的$ac$面可视为与$xz$面重合。因此，式(3-10)—(3-18)左侧下标由$(abc)$改为$(xyz)$后便直接适用。这里$\alpha$为CCH键角，$\tau$为两个CCH面之间的二面角。')
event(7,286,'据此得到以下表达式；同时列出用CH键张量的式(3-13)整理后的结果。')
event(7,712,r'进一步取四面体角，$\cos\alpha=-1/3$、$\sin\alpha=2\sqrt2/3$，得到：')
event(8,434,r'## 5. 表面固定$(xyz)$系中CH₂基团的张量分量')
event(8,450,r'### 5a. 扭转的CH₂基团'+'\n\n'+r'为消除位阻，基团绕C₂轴扭转$\gamma$时，由《欧拉角》式(Eu-1)得到下式。$\alpha$为HCH键角。')
event(8,581,r'相邻CH₂基团同取$+\gamma$或同取$-\gamma$，不交替。由此得到：')
event(9,319,'若用CH键张量表示并取四面体角，可按式(3-4)、(3-5)进一步整理。')
event(9,728,r'### 5b. 后仰的CH₂基团'+'\n\n'+r'分子面由$xz$面沿$\pm y$方向后仰$\theta$以消除位阻时，由《欧拉角》式(Eu-2a)得到下式。$\alpha$为HCH键角。')
event(10,172,r'$\sin\theta/-\sin\theta$成对出现；相邻CH₂基团交替取$+\theta$与$-\theta$。据此得到：')
event(11,335,r'### 5c. 向侧方倾斜的CH₂基团'+'\n\n'+r'分子面在$xz$面内沿$\pm x$方向侧倾$\theta$以消除位阻时，由《欧拉角》式(Eu-2b)得到下式。$\alpha$为HCH键角。')
event(11,401,r'$$R_z(\chi=\pi)R_{b\prime}(\theta)R_c(\phi=\pi)\quad\text{或}\quad R_z(\chi=-\pi)R_{b\prime}(-\theta)R_c(\phi=\pi),\quad\tau=\pi/2.$$')
event(11,483,r'原文称相邻CH₂基团“交替取$+\theta$或$-\theta$之一”，同时又称“异号者不相邻”；这两项表述均保留，排列条件的歧义见Q191。')
event(13,156,r'### 5d. 绕$z$轴扭转后再后仰的CH₂基团'+'\n\n'+r'分子面绕$z$轴扭转$\gamma$，同时从$xz$面沿$\pm y$方向后仰$\theta$时，由《欧拉角》式(Eu-3a)得到下式。$\alpha$为HCH键角。')
event(13,352,r'相邻CH₂基团同取$+\gamma$或同取$-\gamma$，而$\theta$的符号交替。由此得到：')
event(15,466,r'### 5e. 绕$z$轴扭转后再侧倾的CH₂基团'+'\n\n'+r'分子面绕$z$轴扭转$\gamma$，同时在$xz$面内沿$\pm x$方向侧倾$\theta$时，由《欧拉角》式(Eu-3b)得到下式。$\alpha$为HCH键角。')
event(15,646,r'相邻CH₂基团同取$+\gamma$或同取$-\gamma$，且$\theta$也同号。由此得到：')
event(18,679,r'### 5f. 同时具有扭转和倾斜的CH₂基团'+'\n\n'+r'分子轴偏离$z$轴$\pm\theta$，且分子面与表面成二面角$\tau$，以此消除位阻时，由《欧拉角》式(Eu-3c)得到下式。$\alpha$为HCH键角。')
event(19,90,r'$R_c(\phi)$使$b$轴垂直于$z$轴，即垂直于$z$、$c$两轴组成的平面；$R_{b\prime}(\pm\theta)$使$c$轴与$z$轴重合，即使$xy$与$ab$面重合；$R_z(\chi)$使$b$轴与$y$轴重合，即使$xz$面与分子面重合。将相对于情形5e的旋转角记为$\chi^*$。')
event(19,254,r'相邻CH₂基团同取$+\gamma$或同取$-\gamma$，$\theta$同号，而$\chi^*$的符号交替。由此得到：')
event(22,335,r'利用$1\pm\cos2\phi$与$\theta,\tau$的关系，再在CH键张量表达式中取四面体角，也可按式(3-4)、(3-5)进一步整理。不过预期收获不大，这里不再展开。')
event(22,385,r'## 6. 实验室固定$(XYZ)$系中的张量分量'+'\n\n'+r'以下求按光路定义的实验室系张量。设$(XYZ)$系由表面系$(xyz)$绕$z$轴旋转$\chi$而得，参见《表面的旋转》。')
event(22,466,'### 6a. 倾斜的平面HCCH基团')
event(24,90,'使用式(3-8)，得到：')
event(25,450,'### 6b. 扭转HCCH基团')
event(26,172,'使用式(3-16)—(3-18)，得到：')
event(27,90,'### 6c. 后仰的CH₂基团\n\n以分子固定系张量表示时，方式与式(6a-1)、(6a-2)相同；差别出现在用CH键固定系张量作近似的阶段。')
event(28,434,'使用式(3-4)、(3-5)，得到：')
event(30,107,'### 6d. 绕z轴扭转后再后仰的CH₂基团\n\n原文：尚未着手。\n\n> **原文范围说明（Q192）：** 本小节的缺项属于作者原稿未写，不补造推导。原目录将6d与附录A的起页列为p29，实际均从PDF p30开始。')
event(30,156,r'## 附录A　C(100)面双氢化基团及单氢化基团对的和频张量'+'\n\n'+r'设分子固定$(abc)$系通过欧拉角$(\chi,\theta,\phi)$与空间固定$(XYZ)$系重合，所得$(XYZ)$系张量如下。')
event(30,221,'### CH₂及平面HCCH基团（C₂ᵥ对称）')
event(33,188,'### 扭转HCCH基团（C₂对称）')
skip=[(3,0,531),(3,613,678),(4,70,186),(4,269,303),(4,380,498),(5,138,188),(5,334,368),(5,514,662),(7,171,253),(7,285,334),(7,710,743),(8,433,515),(8,580,629),(9,318,351),(9,727,765),(10,0,106),(10,171,237),(11,334,417),(11,482,548),(13,155,221),(13,351,417),(15,465,531),(15,645,712),(18,678,765),(19,89,171),(19,253,335),(22,334,499),(24,89,107),(25,449,483),(26,171,205),(27,89,156),(28,433,466),(30,106,254),(33,187,221)]
generic='若用CH键张量表示并取四面体角，可按式(3-4)、(3-5)进一步整理。'
mathlines=[];untranslated=[]
for p,ls in data.items():
 p=int(p)
 if p<3:continue
 for l in ls:
  y=l['y'];s=l['tex'].replace('(cid:160)','').strip()
  if any(p==a and b<=y<c for a,b,c in skip):
   if '［対称伸縮振動］' in s:event(p,y,'#### 对称伸缩振动')
   elif '［逆対称伸縮振動］' in s:event(p,y,'#### 反对称伸缩振动')
   continue
  if not s:continue
  if re.search('[ぁ-んァ-ン一-龯]',s):
   if '［対称伸縮振動］' in s:event(p,y,'#### 对称伸缩振动')
   elif '［逆対称伸縮振動］' in s:event(p,y,'#### 反对称伸缩振动')
   elif 'CH基のテンソル成分による表式にTd角を仮定すると' in s:event(p,y,generic)
   elif s in ['により、','により、下記の表式を得る。']:pass
   elif not any(e['page']==p and abs(e['y']-y)<1 for e in events):untranslated.append([p,y,s])
   continue
  # 被前文范围边界排除的模式标题在边界上仍需显示。
  if chr(92) in s or '=' in s or 'none' in s or re.fullmatch(r'\([0-9a-z-]+\)',s):
   mathlines.append({'page':p,'y':y,'kind':'math','text':s})
events+=mathlines;events.sort(key=lambda x:(x['page'],x['y']))
(out/'未映射文字.json').write_text(json.dumps(untranslated,ensure_ascii=False,indent=2),encoding='utf-8')
# 完整段落和公式组为批次边界，跨页续行不断开。
bounds=[(385,1,0),(386,3,303),(387,5,515),(388,7,172),(389,8,434),(390,9,728),(391,11,335),(392,13,156),(393,15,466),(394,18,679),(395,22,385),(396,25,450),(397,27,90),(398,30,107),(399,32,90),(400,33,188),(401,35,564)]
texts={n:'' for n,_,_ in bounds};records={n:[] for n,_,_ in bounds};batch=386;current=[];currentloc=[]
def flush():
 global current,currentloc
 if not current:return
 joined='\n'.join(current)
 # 原编号留作原样标签，不生成新公式号。
 joined=re.sub(r'(?<!\\)\{',r'\\{',joined) if False else joined
 def clean(line):
  line=line.replace('’',r'\prime ').replace('、',r',\quad ').replace('　',' ').replace('±',r'\pm ').replace('）',')').replace('（','(')
  # 原页并排的正弦/余弦条件用显式间隔分开，避免TeX忽略空格后误读为连乘。
  for var in ['chi','phi','theta']:
   if line.startswith(r'\sin '+'\\'+var):
    line=line.replace(r'\cos '+'\\'+var,r'\qquad\cos '+'\\'+var,1)
  while '(cid:214)(' in line:
   pos=line.index('(cid:214)(');start=pos+len('(cid:214)(');depth=1;stop=start
   while stop<len(line) and depth:
    if line[stop]=='(':depth+=1
    elif line[stop]==')':depth-=1
    stop+=1
   assert depth==0,line
   line=line[:pos]+r'\sqrt{'+line[start:stop-1]+'}'+line[stop:]
  line=line.replace('pairs',r'\text{成对}').replace('pair',r'\text{成对}').replace('either',r'\text{取}').replace('set',r'\text{组}').replace('for ',r'\text{对于}').replace('one of the',r'\text{下列之一}').replace('/or',r'/\text{或}').replace(' or ',r'\text{或}')
  line=re.sub(r'\(cid:214\)([0-9])',lambda m:r'\sqrt{'+m[1]+'}',line)
  return line
 typeset=[];tags=[]
 for line in current:
  line=clean(line)
  m=re.search(r'\(((?:[0-9]+[a-z]?-[0-9]+[a-z]?)|(?:Eu-[0-9]+[a-z]?))\)\s*$',line)
  if m:tags.append(m[1]);line=line[:m.start()].rstrip()
  if line:typeset.append(line)
 assert len(tags)<=1,(currentloc,tags)
 tex='\\begin{aligned}\n'+typeset[0].replace('=','&=',1)
 for line in typeset[1:]:tex+='\\\\\n&\\quad '+line
 tex+='\n\\end{aligned}'+(r'\tag{'+tags[0]+'}' if tags else '')
 texts[batch]+='$$\n'+tex+'\n$$\n\n'
 raw=''.join(current)
 if any(raw.count(a)!=raw.count(b) for a,b in [('(',')'),('[',']'),(r'\{',r'\}')]):texts[batch]+='> **原式括号提示（Q193）：** 本式原页括号未配对，按原位置保留；页、行位置见本批覆盖记录，不补写因子或调整括号范围。\n\n'
 records[batch].append({'locations':currentloc,'source_lines':current})
 current=[];currentloc=[]
for e in events:
 p,y=e['page'],e['y'];new=max(n for n,pp,yy in bounds if (p,y)>=(pp,yy))
 if new!=batch:flush();batch=new
 s=e['text']
 if e['kind']=='prose':flush();texts[batch]+=s+'\n\n';continue
 # 每个新左式、旋转条件、none项独立；其余为同式续行。
 newleft=bool(re.match(r'^(?:\([ps]{3}\))?\\(?:chi|beta)_\{',s))
 pm=re.match(r'^\(([ps]{3})\)',s)
 if pm:
  flush();texts[batch]+='**('+pm[1]+')**\n\n';s=s[5:].strip()
 if 'none' in s:
  flush();texts[batch]+='无（原文none）。'+re.sub(r'.*none','',s)+'\n\n';continue
 if newleft or s.startswith(('R_',r'\sin',r'\cos')):flush()
 current.append(s);currentloc.append([p,y])
flush()
intro=(root/'翻译管理/校订记录/4.7/B365-本批译文.md').read_text(encoding='utf-8').split('## 1. 绪论')[1]
coords=(root/'翻译管理/校订记录/4.7/B366-本批译文.md').read_text(encoding='utf-8').replace('Q180','Q189')
texts[385]='# 4.8 氢化金刚石表面CH的和频张量\n\n> 原作：广瀬千秋；中文翻译：章力。本轮按38页原稿重新核对。\n> 旧译的“面内弯曲”主题及若干说明与底本不符，现按原题修复；原文件名保留以兼容链接。\n\n## 阅读引导与目录\n\n| 部分 | 原PDF实际页 | 阅读要点 |\n|---|---|---|\n| 1—2 绪论与坐标 | 1—3 | 表面位阻、三套坐标及欧拉角 |\n| 3 分子张量 | 3—5 | 由两个CH键叠加，并给四面体角近似 |\n| 4a—4b HCCH表面张量 | 5—8 | 平面倾斜与扭转两种构型 |\n| 5a—5f CH₂表面张量 | 8—22 | 绕轴扭转、后仰、侧倾及组合取向 |\n| 6a—6c 实验室系张量 | 22—30 | 用表面旋转联系光路与分量 |\n| 6d | 30 | 原稿明确“尚未着手” |\n| 附录A | 30—38 | C₂ᵥ与C₂两种对称性、两种伸缩模式的一般式 |\n\n## 1. 绪论'+intro+'\n\n'+coords+'\n'
# 同节内τ有不同定义，及原式异常，保留原值并明确标识。
notes={386:r'> **原文疑点Q190（p4—5）：** 式(3-8)、(3-9)原分母为37，后续对应的四面体角表达式多用27；原37保留，候选27未采用。式(3-10c)行末有孤立数字1，原样保留。对(Eu-10)的重复引用也未改号。',387:r'> **原文疑点Q191（p5—6）：** τ的定义、θ=±τ及τ=π/2−θ的并列写法存在局部约定差异，参见4.7的Q183。此页还印有cos2ϖ、sin3ϖ等未定义符号，按原字形保留，不默换成χ或φ。',388:r'> **Q191续（p7）：** 本处τ指两个CCH面间的二面角，与前部“ac面和xy面”的τ不同；旋转条件中原写τ=0，均保留局部原约定。',389:r'> **Q191续（p8）：** χ=±γ时原仍写cos2χ=−cos2γ；保留原负号，候选去负号未采用。',391:r'> **Q191续（p11）：** 原文同时写“交替”与“异号者不相邻”，排列条件未确定；不根据旧译选择其中一种。',392:r'> **Q191续（p13）：** sinχ=−1与sin3χ=−1、1+cosφ及负号组首项−sin2γ均按原页照录；与通常恒等式或相邻式不一致处未自行修正。',398:r'> **原文范围说明Q192：** 6d的未完成状态属于原稿内容，不计作译文漏译。附录从p30中部开始，目录p29保留为原目录页界信息。',400:r'> **原文疑点Q193（附录p33—35）：** 若干括号不配对、同类分量的因子与系数不同，均按原页位置完整转录；未由C₂ᵥ表复制来覆盖C₂表。',401:r'> **Q193续（附录p35—38）：** 保留提前或缺少的闭括号、未定义“in2χ”、显式“1sin2χ”及不一致的角度因子；这些表项需进一步推导核定，不能直接作为已验证的数值公式。'}
for n,note in notes.items():texts[n]+='\n'+note+'\n'
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-8.pdf').read_bytes()).hexdigest()
for n,_,_ in bounds:
 (out/f'B{n}-本批译文.md').write_text(texts[n],encoding='utf-8')
 (out/f'B{n}-覆盖.json').write_text(json.dumps({'batch':f'B{n}','source_sha256':sha,'source_lines_and_locations':records[n],'source_corrections_adopted':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
target.write_text('\n\n'.join(texts[n] for n,_,_ in bounds),encoding='utf-8')
print('4.8重建完成；未映射原文字行：',len(untranslated));print(untranslated)

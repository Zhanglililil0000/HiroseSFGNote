from pathlib import Path
import re,json
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.6 *.md'));bs=chr(92);old=P.read_text(encoding='utf-8')
assert not (O/'B151-修订前.md').exists();(O/'B151-修订前.md').write_text(old,encoding='utf-8')
def tx(s):return s.replace('§',bs)
def note(s):return '\n\n> '+tx(s)+'\n\n'
def sub(a,z):return old[old.index(a):old.index(z,old.index(a))]
def eqedit(s,tag,fn):
 def work(m):return '$$'+fn(m[1])+'$$' if bs+'tag{'+tag+'}' in m[1] else m[0]
 return re.sub(r'\$\$([\s\S]*?)\$\$',work,s)
def indexrestore(s):
 bases=r'(\\mathbf\{[LMN]\}|\\boldsymbol\{\\mathcal\{[MN]\}\})'
 s=re.sub(bases+r'_([axy])\^(\{[^}]+\}|[a-z0-9])',lambda m:m[1]+'_'+m[3]+'^{'+m[2]+'}',s)
 s=re.sub(bases+r'_([axy])',lambda m:m[1]+'^{'+m[2]+'}',s)
 s=re.sub(r'\b([UV])_([axy])',lambda m:m[1]+'^{'+m[2]+'}',s)
 return s
parts=[]
def save(batch,s,pages,desc):
 s=indexrestore(s).replace('SFG 极化','和频极化');parts.append(s);(O/(batch+'-本批译文.md')).write_text(s,encoding='utf-8');tags=re.findall(re.escape(bs)+r'tag\{([^}]+)\}',s)
 (O/(batch+'-覆盖.json')).write_text(json.dumps({'batch':batch,'date':'2026-10-20','pages':pages,'units':desc,'tags':tags,'source_images_visually_checked':True,'source_formula_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
 (O/(batch+'.md')).write_text('# '+batch+'：2.6译校\n\n2026-10-20；独立PDF p'+','.join(map(str,pages))+'。'+desc+'。逐项对照原图与文字层，恢复原上标偏振分组/下标层序及原式局部差异。未决原式照录并就地说明，无原文公式修正采用。数学排版验收见整节完成复核。\n',encoding='utf-8')

s=sub('在 SFG 中需要的是电场振幅。','若记\n')
s=s.replace('在 SFG 中需要的是电场振幅。因此扩展 B & W 的处理，进行如下改写。','在和频过程中，需要求出的是电场振幅。因此，这里扩展Born与Wolf的处理，作如下改写。')
s+=note('**原文疑点（Q088，PDF p3，式2.5a/b）**：本页前段定义 $V^y=-n(E_y^+-E_y^-)§cos§theta$，而这里2.5a矩阵第二行给出相反符号；2.5b与2.5a这一矩阵互逆。两处均保留原式。候选为统一前段定义或同时改变2.5a/b第二列/行相关符号，尚未采用。这里的 $L^x,L^y$ 是场量基变换矩阵，区别于前几节连接极化源与出射光的L系数。')
save('B151',s,[3],'电场幅变换说明、2.5a/b与2.6a/b四个完整变换式')
s=sub('若记\n','由式 (2.3) ~ (2.6)')
s+=note('**原文疑点（Q089，PDF p4，式2.7b）**：最后一行在 $§mathcal N_1^a$ 后另有 $§mathcal N_0^a$，而前一行展开至 $L_1^aN_1^a(L_0^a)^{-1}$。此处保留多出的0层因子；删去它只是候选。为区分底本中转换前后两套不同字形的M/N，本译文用粗体M/N与花体 $§mathcal M,§mathcal N$，层号为下标、分组a为上标，不新增物理量。')
save('B152',s,[4],'一般场幅基变换与2.7a/b全部中间乘积链；保留末行额外N0')
s=sub('由式 (2.3) ~ (2.6)','## 3. 界面数量')
s+=note('**原文疑点（Q089续，PDF p4）**：2.8b的分母为 $t_{i-1,i,y}$，对角相位依次为 $e^{-i§beta_i z},e^{+i§beta_i z}$；2.9b分母却为 $t_{i,i-1,x}$、对角相位次序相反。第3部分的一界面式又写成后一种结构。保留各处值；2.8b是否应改为后一种分母方向与相位结构待核，不直接统一。')
save('B153',s,[4],'2.8a/b、2.9a/b全部矩阵元素、t分量与β定义')
s=sub('## 3. 界面数量','### 3.3.')
save('B154',s,[4,5],'界面编号与膜厚总述，单界面3.1a/b及双界面3.2a/b')
s=sub('### 3.3.','## 4. 层数')
# Attach printed equation numbers to their four-entry groups rather than leaving an empty display.
s=re.sub(re.escape(bs)+r'end\{aligned\}\$\$\s*\$\$('+re.escape(bs)+r'tag\{3\.[34][ab]\})\$\$',lambda m:bs+'end{aligned}'+m[1]+'$$',s)
s+=note('**原文疑点（Q090，PDF p6，式3.4b的(2,2)元素）**：在p偏振表达式中出现 $r_{21,p}r_{10,s}$，这里保留混用的s下标；候选为 $r_{10,p}$，未采用。式3.4a的(2,2)元素跨p5—6，已完整接续。')
save('B155',s,[5,6],'三界面与四界面s/p乘积，四组各四个展开元素，含跨页3.4a')
s=sub('## 4. 层数','### 4.1. 单层')
save('B156',s,[6],'末介质无反向场条件、双介质无编号关系与4.1a/b、4.2a/b')
s=sub('### 4.1. 单层','### 4.2. 双层')
s+=note('**原文记号疑点（Q091，PDF p7—8）**：4.4a/b在m层记法中仍混用 $r_{10},t_{10},§beta_1h_1,§beta_1z_1$；正文又把4.4a称为透射光振幅式，尽管其列出的是膜内场。这里均按原文保留；将层号1等同m、或将该引用改为4.5a只是候选。零厚度极限4.6c及p偏振z分量说明跨至p8，已接全。')
save('B157',s,[7,8],'单层完整场、和差场及零厚度极限4.3a—4.6c和z分量说明')
s=sub('### 4.2. 双层','**表面一侧薄膜厚度为零的极限')
save('B158',s,[8],'双层膜反射、各层正反场及和差场4.7a/b—4.10a/b')
s=sub('**表面一侧薄膜厚度为零的极限','### 4.3. 三层')
save('B159',s,[9],'双层前/后薄膜分别零厚度的八个完整极限式4.11a/b—4.14a/b')
s=sub('### 4.3. 三层','在此，考虑 SFG 中较为常见')
s=eqedit(s,'4.18a',lambda x:x.replace("t_{mm''}","t_{mm'''}").replace("r_{mm''}","r_{mm'''}"))
for tag in ['4.19a','4.19b']:s=eqedit(s,tag,lambda x:x.replace('e^{i'+bs+'beta_2 z_4}',"e^{i"+bs+"beta_{2'} z_4}"))
s+=note('**原文疑点（Q092，PDF p9—11）**：4.18a局部出现 $t_{mm^{§prime§prime§prime}}$ 及分母 $r_{mm^{§prime§prime§prime}}$，4.19a/b的前行相位写 $§beta_{2\prime}$，保留额外撇号，候选为双撇号层标或无撇号2。4.19b在已经规定末介质无−波后仍有 $e^{-i§beta_2z_4}$ 项，未直接删去。')
s+=note('**原文疑点（Q093，PDF p9—10，式4.15a/b）**：右侧前因子原为1，没有像邻式那样写 $E^+(0)$；与左端场幅的归一化关系不明。此处照录，不补入场幅。候选为作者在此归一化入射场或漏写该因子。')
save('B160',s,[9,10,11],'三层膜五处正反场与五处和差场4.15a/b—4.19a/b；4.18b跨p10—11')
s=sub('在此，考虑 SFG 中较为常见','**表面一侧和背面一侧薄膜厚度均为零时')
# Restore printed extra/missing brackets, locally anomalous layer label, and repeated plus field.
def br20(x):
 a=x.index(bs+'begin{bmatrix}',x.index(bs+'frac'));z=x.index(bs+'end{bmatrix}',a);m=x[a:z];rows=re.split(r'\\\\\[8pt\]',m);assert len(rows)==2
 rows[0]=rows[0].rstrip();assert rows[0].endswith(']');rows[0]=rows[0][:-1]
 rows[1]=rows[1].replace("(1 - r_{m'm})[","(1 - r_{m'm})][",1)
 return x[:a]+(bs*2+'[8pt]').join(rows)+x[z:]
s=eqedit(s,'4.20b',br20)
s=eqedit(s,'4.22',lambda x:x.replace("r_{mm'}","r_{mm'''}"))
s=eqedit(s,'4.23',lambda x:x.replace('E^+(z_3) + E^-(z_3)','E^+(z_3) + E^+(z_3)',1))
s+=note('**原文疑点（Q094，PDF p11—12）**：4.20a/b的右侧前因子仍为1，场幅归一化问题同Q093。4.20b上行缺一个右方括号、下行在 $(1-r_{m\prime m})$ 后多一个右方括号，保留可见括号；候选为补齐/去掉相应括号。4.22下行系数写三撇层标；4.23左端上行为两个 $E^+(z_3)$ 相加，均恢复原字形。候选为对应双撇层标及 $E^++E^-$，未采用。4.23跨p11—12已接全。')
save('B161',s,[11,12],'三层表面层零厚度的4.20a/b—4.24六式及极限情形说明')
s=old[old.index('**表面一侧和背面一侧薄膜厚度均为零时'):]
def br25(x):
 a=x.index(bs+'begin{bmatrix}',x.index(bs+'frac'));z=x.index(bs+'end{bmatrix}',a);m=x[a:z].replace("\n(1 + r_{1m'})","\n[(1 + r_{1m'})",1).replace("\n(1 - r_{1m'})","\n[(1 - r_{1m'})",1);return x[:a]+m+x[z:]
s=eqedit(s,'4.25b',br25)
s=eqedit(s,'4.29',lambda x:x.replace('E^+(z_4) - E^-(z_4)','E^+(z_4) + E^-(z_4)',1))
s+=note('**原文疑点（Q095，PDF p12）**：4.25a/b右侧前因子为1，仍按Q093保留归一化疑点；4.25b两行各有多出的左方括号，照录可见符号，去掉为候选。4.29左端两行同为 $E^+(z_4)+E^-(z_4)$，未沿用旧译自动改为和/差的写法；下行为差是候选，尚未采用。')
save('B162',s,[12],'三层前后表面层同时零厚度的4.25a/b—4.29六式及结语')
new=old[:old.index('在 SFG 中需要的是电场振幅。')]+''.join(parts);P.write_text(new,encoding='utf-8')
print('B151—B162 complete transcription',len(new),'tags',len(re.findall(re.escape(bs)+r'tag\{([^}]+)\}',new)))

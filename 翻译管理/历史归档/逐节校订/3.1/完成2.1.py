from pathlib import Path
import re,json,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/3.1';p=r/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md';old=p.read_text(encoding='utf-8');assert not (o/'B170-修订前.md').exists();(o/'B170-修订前.md').write_text(old,encoding='utf-8')
a=old.index("**m'/m 界面的 m 侧：**");end=old.index('### 2.2 SFG极化',a);tail=old[end:];src=old[a:end]
def note(q,where,txt):return '\n> **原文疑点（'+q+'，'+where+'）：** '+txt+'\n\n'
q98=note('Q098','PDF p5—6，式2.8—2.9','式2.8的红外光分子沿用 $(1+r_{m\prime m,ir,\beta})$，而可见光分子及式2.9使用对应的透射系数；两式末端相位又同为2ni。这里逐处保留，不把红外因子或相位静默统一。候选为将2.8红外因子改为对应透射系数；两式源分类与路径相位是否对应仍待核验。')
q99=note('Q099','PDF p6—7，式2.10b、2.12b','这两个红外场单独表达式的末端相位仍写 $k_{m,vis}\sin\theta_{m,vis}$，但乘积式2.11、2.13的总相位含vis与ir两项之和。保留原值；候选为单独红外场末端采用ir指标，尚未采用。')
q100=note('Q100','PDF p7—9，m层体相段','原文标题将 $z_2$ 定为距m′/m界面的深度，但场位置写 $h_m+z_2$；与前文层序比较，候选为 $h_{m\prime}+z_2$，此处不改。p8的反向源标题又写 $B_n^{(m\prime)}$，旧译改成了m；现恢复原层标，候选为m，尚未采用。')
q101=note('Q101','PDF p8—9，式2.15、2.17','四项展开式在每项指数前重复出现左花括号，末尾未见与之配对的右花括号；原页指数写法的圆括号也未完整闭合。这里保留可见括号而不赋予候选分组。候选为仅保留一对包住四项和的花括号，并补齐指数内圆括号；尚未采用原文修正。')
notes={'B170':q98,'B171':q99,'B172':'','B173':q100+q101,'B174':''}
marks=[0,src.index("**m' 层的深度"),src.index('$[B_n'),src.index('**m 层中距'),src.index('$[B_n',src.index('**m 层中距')),len(src)]
units=['m′/m界面m侧式2.8—2.9','m′层正向源单场2.10a/b与四项乘积2.11','m′层反向源单场2.12a/b与四项乘积2.13','m层正向源单场2.14a/b与四项乘积2.15','m层反向源单场2.16a/b与四项乘积2.17']
pages=[[5,6],[6,7],[7],[7,8],[8,9]]
def norm(t):
 t=re.sub(r'\\(?:begin|end)\{aligned\}','',t);t=re.sub(r'\\\\(?:\[[^\]]*\])?','',t);t=re.sub(r'\\hspace\{[^}]*\}','',t);t=re.sub(r'\\(?:quad|qquad|times|Bigl|Bigr|bigl|bigr)','',t);t=re.sub(r'\\[,!]','',t);return re.sub(r'[\s{}&]','',t)
def layout(blocks):
 text='\n'.join(x.strip() for x in blocks);tag=re.search(r'\\tag\{([^}]+)\}',text)[0];text=text.replace(tag,'')
 rows=[]
 for block in blocks:
  x=block.strip().replace(tag,'');x=re.sub(r'\n\s*',' ',x)
  # Each original display fragment becomes one or more aligned rows.
  if '=' in x:
   x=x.replace(' = ',' &=',1)
   if r'\frac' in x:x=x.replace(r'\frac',r'\\ &\quad\times\frac',1)
  else:x='&\quad '+x
  if r'\frac' in x:
   x=re.sub(r'}\{1\s*\+\s*',lambda z:r'}{\begin{aligned}&1+',x,count=1)
   assert " + (r_{m'm," in x
   x=x.replace(" + (r_{m'm,",r"\\&\quad+(r_{m'm,",1)
   assert x.endswith('}');x=x[:-1]+r'\end{aligned}}'
  # Separate long coefficients from the exponential that follows them.
  pos=x.find(r'\exp[')
  if pos>130:x=x[:pos]+r'\\ &\qquad '+x[pos:]
  # Break the sum of vis/ir wave-vector terms inside the fixed-size exponential brackets.
  x=x.replace(' + k_',r'\\ &\hspace{5em}+ k_')
  # Four-term coefficients are products, not sums: a row break adds only explicit multiplication.
  if len(x)>250 and r'\frac' not in x and r'\exp' not in x:
   k=x.find(')(')
   if k>0:x=x[:k+1]+r'\\ &\qquad\times '+x[k+1:]
  rows.append(x)
 result=r'\begin{aligned}'+'\n'+r'\\[4pt]'.join(rows)+'\n'+r'\end{aligned}'+'\n'+tag
 assert norm(''.join(blocks))==norm(result),tag
 return '$$\n'+result+'\n$$'
def join_formulas(s):
 # Group adjacent old math fragments up to each original tag, ignoring only their display separators.
 ms=list(re.finditer(r'\$\$([\s\S]*?)\$\$',s));out='';cursor=0;buf=[];first=None
 for x in ms:
  if first is None:first=x.start();out+=s[cursor:first]
  else:assert not s[cursor:x.start()].strip()
  buf.append(x[1]);cursor=x.end()
  if r'\tag{' in x[1]:out+=layout(buf);buf=[];first=None
 assert not buf
 return out+s[cursor:]
parts=[];sha=hashlib.sha256((r/'日语原版/Chapter3/chap3-1.pdf').read_bytes()).hexdigest();assert sha=='3fdb1ecaa620a0b809337eacd52e356ef7c8145642b49df5c7ee476f7789387f'
for i in range(5):
 b=f'B{170+i}';s=src[marks[i]:marks[i+1]]
 s=s.replace("**m'/m 界面的 m 侧：**",'**m′/m界面的m侧：**').replace("**m' 层的深度 $z_1$ 点：**",'**m′层中深度 $z_1$ 处：**').replace("**m 层中距 m'/m 界面深度 $z_2$ 的点：**",'**m层中距m′/m界面深度 $z_2$ 处：**')
 s=s.replace('(a): $E^{+}$ and $E^{-}$ (by reflection) sources','（a）：$E^+$ 源与 $E^-$ 源（经反射）。').replace('(b): $E^{+}$ (by reflection) and $E^{-}$ sources','（b）：$E^+$ 源（经反射）与 $E^-$ 源。')
 s=s.replace(': $E^{+}$ sources','：$E^+$ 源。').replace(': $E^{-}$ sources','：$E^-$ 源。').replace('两者的乘积为：','两者的乘积为：').replace('两者乘积为：','两者的乘积为：')
 if b=='B174':s=s.replace(r'$[B_n^{(m)}]$',r"$[B_n^{(m')}]$")
 s=join_formulas(s)+notes[b];parts.append(s)
 (o/(b+'-本批译文.md')).write_text(s,encoding='utf-8')
 tags=re.findall(r'\\tag\{([^}]+)\}',s);c={'batch':b,'date':'2026-10-20','pages':pages[i],'units':units[i],'tags':tags,'source_images_visually_checked':True,'source_sha256':sha,'source_formula_corrections_adopted':False,'layout_factor_comparison_passed':True}
 (o/(b+'-覆盖.json')).write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
 (o/(b+'.md')).write_text('# '+b+'：3.1的2.1续校\n\n2026-10-20；PDF '+str(pages[i])+'。'+units[i]+'。逐项对照原图与文字层，保留层标、指标、全部项、系数和相位。展示块按原编号合并，跨页式接全；仅分行与显式乘号排版。B174的B源上标恢复原文m′，属于旧译转写修复；疑点候选均未采用。\n',encoding='utf-8')
new=old[:a]+''.join(parts)+tail;new=re.sub(r'\*\*译校状态（2026-10-20）：\*\*[^\n]+','**译校状态（2026-10-20）：** B163—B174完成原目录、第1部分及2.1“电场振幅的乘积”全小节（PDF p1—9至式2.17）；2.2起仍为旧译待校订。Q096—Q101保留原文并就地说明，未采用原文公式修正。',new);p.write_text(new,encoding='utf-8');assert new[new.index('### 2.2 SFG极化'):]==tail
(o/'2.1-疑点登记待同步.md').write_text(q98+q99+q100+q101,encoding='utf-8');print('B170—B174全部内容已转写；2.2起保持原样')

from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');assert not (o/'B011-修订前.md').exists();shutil.copy2(p,o/'B011-修订前.md')
a=s.index('$$',s.index('**译者注（Q015）'));b=s.index('$$',a+2)+2;old=s[a:b];assert r'\tag{13}' in old;(o/'式13-旧译候选.txt').write_text(old,encoding='utf-8')
groups=old.split(r'\Bigg\{',1)[1].split(r'\Bigg]');assert len(groups)==7
clean=lambda t:re.sub(r'\s+',' ',t.replace(r'\\','').replace('&','').replace(r'\quad','').replace(r'\times','')).strip()
lines=['# B011：式（13）定义及前两主组工作稿','','> **部分核对：2/6主组、8/24子项；不是整式定稿。Q016下标暂拟读，Q017原式正号待理论核验。**','','PDF p7；整式至p8末。T₁、T₂仅为管理标识，不是作者符号；下列分组不含整式公共系数和求和。','','## 定义与公共因子','', '$$',r'\chi^{(3)}_{ijkl}(\omega=2\omega_1-\omega_2)=\frac{P_i^{(3)}(\omega=2\omega_1-\omega_2)}{E_j(\omega_1)E_k(\omega_1)E_l(-\omega_2)}','$$','','公共因子：$-Ne^4/\hbar^3$；求和指标：$g,n,n\prime,n\prime\prime$。旧译定义重复写了一遍χ等式，最终合并时删除重复。','']
for ix in [0,1]:
 prefix,inner=groups[ix].split(r'\Bigg[',1);ext=clean(prefix[prefix.index(r'\frac'):]);chunks=inner.split(r'\right]');assert len(chunks)==5
 lines += [f'## 第{ix+1}主组','', '$$',r'\begin{aligned}',f'T_{ix+1}={{}}&'+ext+r'\\[6pt]']
 for j,c in enumerate(chunks[:4]):
  t=clean(c[c.index(r'\frac'):])+r'\right]'
  if ix==0 and j==2:
   # Source shows a double-prime-like suffix and a stray glyph; provisional reading, explicitly noted below.
   x,y=t.split(r'\left[',1);x=x.replace(r'\omega_{n n\prime}',r'\omega_{n n\prime\prime}') if False else x
   x=x.replace(r'\omega_{n n\'}',r'\omega_{n n\'\'}') if False else x
   x=x.replace("\\omega_{n n'}", "\\omega_{n n''}").replace("\\Gamma_{n n'}", "\\Gamma_{n n''}")
   t=x+r'\left['+y
  lead=r'\times\Biggl[' if j==0 else '+'
  lines.append(r'&\quad '+lead+t+(r'\Biggr]' if j==3 else '')+(r'\\[8pt]' if j<3 else ''))
 lines += [r'\end{aligned}','$$','']
lines+=['## 本批疑点与边界','','- Q016：首组第3子项的中间分母，底本ω、Γ下标均有双撇及额外字形迹象；旧译写nn′。此稿暂拟读nn″，并不作为确定转录，不把猜读静默写回正文。须以更清晰底本或推导复核。','','- Q017：首组第4子项的中间分母，原文确为ω₁＋ω₂−ω_nn″＋iΓ_nn″，旧译亦如此；此稿保留加号，不由式13输出频率擅改。','','- 第2组4子项已对照页面，未发现旧译实质符号差异。两组组内均为四项相加，内括号A−B；全部iΓ为正。','','- 第3—6组位于p8，尚未逐项核对；正文整式保持旧译，仅增加工作进度提示。下一批B012核p8第3、4组。','']
(o/'B011-式13工作稿.md').write_text('\n'.join(lines),encoding='utf-8')
s=s[:a]+'> **式（13）工作进度：** B011已对照定义及前2主组（8/24子项），Q016下标暂拟读、Q017保留原文正号；整式尚未完成，正文旧式暂未替换。\n\n'+s[a:];p.write_text(s,encoding='utf-8')
p=m/'排版工具/检查译文.cjs';t=p.read_text(encoding='utf-8');t=t.replace(" const exe=["," if(process.argv.includes('--b011')) {sections.length=0;sections.push(['B011',fs.readFileSync(path.join(out,'B011-式13工作稿.md'),'utf8')]);}\n const exe=[");p.write_text(t,encoding='utf-8')
print('B011 draft: definition and 2 groups, 26 group fractions. Formal eq13 unchanged.')

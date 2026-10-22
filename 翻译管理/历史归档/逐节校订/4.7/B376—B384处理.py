from pathlib import Path
import json,re,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.7 CH₂、平面HCCH及扭转HCCH的和频张量.md'
snap=out/'B376前旧译.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
old=snap.read_text(encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-7.pdf').read_bytes()).hexdigest()
notes={
376:r'''> **译者注（原文疑点Q183，PDF p11—12）：** 本部分先将$\tau$定义为$ac$面与$xy$面之间的二面角，但4a同时列旋转角$\theta=\mp\tau$与$\tau=\pi/2-\theta$；4b又在$ac=xz$时写$\tau=0$。这些记法不能直接按同一个二面角定义互换。各处原约定与原式保留，不替换角名；候选解释是4a/4b局部以相对竖直面的倾斜量记$\tau$，尚未采用。''',
377:r'''> **译者注（Q183续，PDF p12）：** 本处$\tau=0$为原文；若按本部分开头$ac$与$xy$面之间的二面角定义，$ac=xz$对应$\pi/2$。原式保留，勿与5a中的$\tau=\pi/2$混用。''',
378:r'''> **译者注（原文疑点Q184，PDF p13）：** 原文在$\chi=\pm\gamma$之后仍列$\cos2\chi=-\cos2\gamma$，与通常恒等式不相容；候选为去掉右侧负号，未采用。相邻CH₂基同取$+\gamma$或同取$-\gamma$、不交替，是原文明确限定的排列。此处$\sin2\chi$、$\cos2\chi$确为倍角，区别于前表中的函数平方。''',
379:r'''> **译者注（角度与函数幂，PDF p14）：** 本处$\tau=\pi/2-\theta$以及式(5b-1)均按原文保留；上下倾斜的正负号须结合所选取向辨认。各式的$\sin^3\theta$、$\cos^3\theta$为函数立方，旧译的三倍角写法已按原页恢复。''',
380:r'''> **译者注（原文疑点Q185，PDF p15—16）：** 原编号从5b跳到5d，予以保留。式(5d-1)原列$\sin\chi=-1$而$\sin3\chi=-1$，后者候选为$+1$；末组原写$1+\cos\phi$（非$1-\cos2\phi$）；负号取向组的首项原为$-\sin2\gamma$而非$-\sin\gamma$。这些原写均保留，候选未采用。表(5d-2)的$\chi_{xxy}$首项无$\sin\theta$因子、表(5d-3)的$\chi_{yzz}$原缺闭方括号，也不自行补项或改括号作用范围。'''
}
starts=['### 4. 分子固定','#### 4b.','### 5. 表面固定','#### 5b.','#### 5d.','## 附录A']
for i,batch in enumerate(range(376,381)):
 s=old[old.index(starts[i]):old.index(starts[i+1])].strip()
 s=s.replace('C2v','C₂ᵥ').replace('C2','C₂').replace('CH2','CH₂').replace('极化组合','偏振组合').replace('均无贡献','：无（原文none）')
 s=re.sub(r'\\(sin|cos) 3\\theta',lambda m:'\\'+m[1]+'^3\\theta',s)
 if batch==380:
  s=s.replace(r'\cos 2\theta\sin 2\phi',r'\cos^2\theta\sin 2\phi')
  s=s.replace(r'1 - \cos 2\phi = 1 + \cos 2\gamma',r'1 + \cos\phi = 1 + \cos 2\gamma')
  s=s.replace(r'$(-\sin\gamma,-\sin 2\gamma,-\sin 3\gamma)$',r'$(-\sin 2\gamma,-\sin 2\gamma,-\sin 3\gamma)$')
  s=s.replace(r'[(\sin\theta - 2\sin^3\theta)(1 + \cos 2\phi)]',r'[(\sin\theta - 2\sin^3\theta)(1 + \cos 2\phi)')
 # 保持原公式组，仅按印刷行拆开超长旋转组，避免页面横向溢出。
 s=re.sub(r'\$\$(R_z.*?)\$\$',lambda m:'$$\n\\begin{gathered}\n'+m[1].replace(',\\quad ',r',\\'+'\n')+'\n\\end{gathered}\n$$',s,flags=re.S)
 s+='\n\n'+notes[batch]+'\n'
 (out/f'B{batch}-本批译文.md').write_text(s,encoding='utf-8')
 rec={'batch':f'B{batch}','pages':{376:[11,12],377:[12,13],378:[13,14],379:[14,15],380:[15,16]}[batch],'scope':['第4部分引言及4a','4b','第5部分及5a','5b','5d'][i],'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False}
 (out/f'B{batch}-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# 附录从PDF字形位置提取：保留下标、函数幂、跨页续行与原有括号。
data=json.loads((out/'附录字形提取.json').read_text(encoding='utf-8'))
groups=[('CH₂基团及平面HCCH基团（C₂ᵥ对称）','对称伸缩振动',381,[]),('CH₂基团及平面HCCH基团（C₂ᵥ对称）','反对称伸缩振动',382,[]),('扭转HCCH基团（C₂对称）','对称伸缩振动',383,[]),('扭转HCCH基团（C₂对称）','反对称伸缩振动',384,[])]
current=None
for p,ls in data.items():
 p=int(p)
 for line in ls:
  y=line['y'];s=line['tex']
  if p==16 and y<375:continue
  if p==19 and 309<y<409:continue
  group=0 if p<18 or (p==18 and y<241) else 1 if p<19 or (p==19 and y<359) else 2 if p<22 else 3
  if not (r'\chi_' in s or r'\beta_' in s or s.startswith(('+','-','3\\cos'))):continue
  pm=re.match(r'^\(([ps]{3})\)',s)
  pol=pm[1] if pm else None
  s=re.sub(r'^\([ps]{3}\)','',s).strip()
  # Symbol编码v是ϖ；保留原未定义符号，不替换为φ。
  s=s.replace(r'\sin 2v',r'\sin 2\varpi')
  m=re.match(r'\\chi_\{([XYZ]{3})\}\s*=\s*(.*)',s)
  if m:
   current={'indices':m[1],'polarization':pol,'lines':[m[2]],'locations':[[p,y]]};groups[group][3].append(current)
  else:
   assert current is not None,(p,y,s)
   current['lines'].append(s);current['locations'].append([p,y])
assert [len(g[3]) for g in groups]==[27]*4
appendix_notes={381:{'XXY':r'**原文疑点Q186（p17）：** 此式末尾花括号未闭合，且与p21的C₂式相应部分相比少一续项。原页所见范围照录，不从后页补入。'},382:{'ZZX':r'**Q186续（p18）：** 原式末项为$\sin2\varpi$，$\varpi$在此未定义；候选$\sin2\phi$未采用。','YXY':r'**Q186续（p18）：** 原系数开头为$-((1/4)$，多出的左圆括号照录。'},383:{'XXZ':r'**原文疑点Q187（p20）：** 原式的$(\beta_{aac}-\beta_{bbc}$缺右圆括号，末组又有额外右方括号；符号作用范围未擅改。','YYX':r'**Q187续（p20）：** $\beta_{abc}$组原写$[4\sin\theta\cos\chi-(2\sin\theta-\sin^3\theta)]\sin2\phi$；未参照相邻表项补角度因子。','XYX':r'**Q187续（p20）：** 末组原缺闭方括号，照录。','YXY':r'**Q187续（p21）：** 末尾原有连续两个右方括号，照录；其中$\sin\chi+\sin3\chi$也未按相邻分量改号。'},384:{'XXX':r'**原文疑点Q188（p22）：** 原式在第二行提前出现闭花括号，最后又有闭花括号；不移动括号来改变系数作用范围。','XZZ':r'**Q188续（p22）：** 中途及末尾均有闭花括号，照录。','ZXZ':r'**Q188续（p22）：** 中途及末尾均有闭花括号，照录。','ZXX':r'**Q188续（p22）：** $\beta_{bca}+\beta_{cab}$组的方括号位置不配对，按原位置保留。','XZX':r'**Q188续（p22）：** 方括号位置与上式同样不配对，保留。','YZZ':r'**Q188续（p22—23）：** 第二组中原无$\sin\chi$，第三组原为$\sin2\chi$，与p23的$\chi_{ZYZ}$形式不同；均未自行统一。','YZX':r'**Q188续（p23）：** 原写$\cos2\phi\,\mathrm{in}2\chi\cos2\phi$，其中“in”不是本节定义的函数；候选涉及$\sin2\chi$，但完整因子组合尚待推导，不采用。','YXZ':r'**Q188续（p23）：** 第二组中的$\cos2\chi\sin2\phi$原写如此，与同页$\chi_{XYZ}$不同；保留。','ZYX':r'**Q188续（p23）：** 原式在第三组后结束，未闭花括号；不按$\chi_{YZX}$补入第四组。','YXY':r'**Q188续（p23）：** 第三组原缺闭方括号，保留。','ZXY':r'**Q188续（p24）：** 首组原有$1\sin2\chi$，保留显式1；各组因子均照录，未按其他表项改写。','XZY':r'**Q188续（p24）：** 首组原有$1\sin2\chi$，同上照录。','XYY':r'**Q188续（p24）：** 第二组首两项的括号范围与p23的$\chi_{YXY}$不同，按原页保留。','YYY':r'**Q188续（p24）：** 最后两行方括号不配对，未重新指定末项的系数范围。'}}
for title,mode,batch,eqs in groups:
 s=''
 if batch==381:s+='## 附录A　C(100)面双氢化基团及单氢化基团对的和频张量\n\n设分子固定$(abc)$系通过欧拉角$(\\chi,\\theta,\\phi)$与空间固定$(XYZ)$系重合，以下求$(XYZ)$系中的张量分量。\n\n'
 s+='### '+title+'：'+mode+'\n\n'
 s+='以下逐项保留原一般式，包括跨页续项。函数幂与倍角按原字形区分；未配对括号及未定义符号在相应位置注明，不能将本表直接视为已验证的计算公式。\n\n'
 pol=''
 for eq in eqs:
  if eq['polarization']:pol=eq['polarization']
  s+='#### ('+pol+') $\\chi_{'+eq['indices']+'}$\n\n'
  s+='$$\n\\begin{aligned}\n\\chi_{'+eq['indices']+'}&='+eq['lines'][0]
  for l in eq['lines'][1:]:s+='\\\\\n&\\quad '+l
  s+='\n\\end{aligned}\n$$\n\n'
  if eq['indices'] in appendix_notes.get(batch,{}):s+='> '+appendix_notes[batch][eq['indices']]+'\n\n'
 (out/f'B{batch}-本批译文.md').write_text(s,encoding='utf-8')
 rec={'batch':f'B{batch}','scope':title+'，'+mode,'pages':sorted(set(loc[0] for eq in eqs for loc in eq['locations'])),'source_sha256':sha,'source_images_visually_checked':True,'equations':eqs,'single_component_equalities':27,'source_corrections_adopted':False,'extraction_method':'PDF字形横纵坐标识别上/下标，逐原页视觉核对；跨页续行按同一左式归组'}
 (out/f'B{batch}-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
prefix=old.split('<!-- B375止；')[0].rstrip()
target.write_text(prefix+'\n\n'+'\n\n'.join((out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(376,385))+'\n',encoding='utf-8')
print('B376—B384：正文具体取向完整覆盖，附录四组各27分量，共108等式，补齐原省略C₂两组。')

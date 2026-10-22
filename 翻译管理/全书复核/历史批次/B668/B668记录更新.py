from pathlib import Path
import re,json,shutil,math
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B668修改前'
new='**译者注释更正（Q304，B668已撤回误报）：** 已放大核对p4式(2)、p7式(8)—(12)、p8式(13)—(15)及p10式(A3)，根号均只覆盖2π，σ在根号外；高斯因子为1/(√(2π)σ)，平方项的2πσ²及式(A3)的√(2π)σ与之相容。此前“根号覆盖σ、归一化不一致”的注释属于译者误读，现撤回。未改原式内容；式(12)裁图底部截断另已修复。Q308的宽度文字、Q309的分布极限等独立疑点仍保留。'
changed=[]
def edit(rel,fn):
 p=R/rel;s=p.read_text(encoding='utf-8-sig');t=fn(s)
 if t!=s:
  b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
  p.write_text(t,encoding='utf-8');changed.append(rel)
body='中文版本/第八章 拟合/8.1 和频光谱的线形.md'
def update(s):
 s=re.sub(r'(?m)^> \*\*原文疑点（Q304[^\n]+',lambda m:'> '+new,s)
 s=s.replace('Q300—Q314待核，未采用修正。','Q300—Q314中除Q304已撤回误报外，其余疑点待核；未采用原文修正。')
 return s.replace('式(A3)根号范围另见Q304；','式(A3)根号范围已由B668核清，Q304误报已撤回；')
edit(body,update)
edit('翻译管理/疑难与勘误.md',lambda s:re.sub(r'(?m)^\*\*原文疑点（Q304[^\n]+',lambda m:new,s).replace('式(A3)根号范围另见Q304；','式(A3)根号范围已由B668核清，Q304误报已撤回；'))
edit('翻译管理/符号与约定.md',lambda s:s.replace('高斯根号范围、分布极限及归一化差异均按Q303—Q304、Q309保留。','Q304高斯根号范围误报已由B668撤回；洛伦兹归一化及分布极限仍按Q303、Q309保留。'))
for rel in ['Preface序言.md','中文版本/第八章 拟合/阅读导航.md']:
 edit(rel,lambda s:s.replace('归一化问题见Q303、Q304。','洛伦兹归一化问题见Q303；Q304高斯根号范围误报已撤回。'))
edit('中文版本/附件/原文勘误表.md',lambda s:s.replace('Q304 | 高斯归一化根号范围与平方系数；原印保留','Q304 | B668已撤回译者误报：σ在根号外，原式未改；不属原文勘误'))
def append(rel,text):
 edit(rel,lambda s:s if text.splitlines()[0] in s else s.rstrip()+'\n\n'+text+'\n')
append('翻译管理/疑难与勘误.md','''## B668：Q304误报撤回（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q304 | 8.1 p4/p7/p8/p10；式(2)、(8)—(15)、(A3) | 放大原页与裁图确认σ在根号外；平方系数相容，旧译者注释误判 | 译者误报/P2 | 已撤回并关闭此项，保留编号及更正说明；原式内容未改；裁图修复另记，无新E。详见全书复核/B668高斯复核.md。Q303/Q308/Q309/Q311其它问题独立保留 |''')
append('翻译管理/符号与约定.md','''## B668：高斯归一化与σ（2026-10-22）

8.1式(2)、(8)—(15)、(A3)根号仅覆盖2π，σ在外。p10明确σ为标准差，p4的Δ1/2=√(2ln2)σ与之相容。Q304作为译者根号范围误读已撤回；高斯平方的半高半宽缩为1/√2是条件性代数结果，p7相反文字仍留在Q308。卷积、相干积分与激光谱宽不能据此一并归一。详见[本批复核](全书复核/B668高斯复核.md)。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B668补充

Q304已撤回：8.1高斯因子为1/(√(2π)σ)，σ在根号外；标准差与半高半宽分别表述。不得继续把该项写成原文归一化错误。平方导致的宽度变化与卷积展宽、激光谱宽是不同操作，Q308/Q309等独立保留。详见[B668复核](B668高斯复核.md)。''')
append('中文版本/附件/原文勘误表.md','''## B668译者误报撤回（2026-10-22）

Q304经原页及裁图放大确认，σ位于根号外，原高斯归一化及所核平方常系数相容。原先归为原文疑点的是译者误读，现撤回；保留Q编号和就地更正说明供追溯，不作为原文勘误，不新增E。Q308宽度文字、Q309分布极限等仍按各自记录保留。''')
heading='## 当前有效状态：B668高斯归一化误报撤回（2026-10-22）'
def progress(s):
 if heading in s:return s
 s=s.replace('## 当前有效状态：B667','## 历史状态：B667',1)
 return s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+heading+'''\n\n完成8.1 p4/p7/p8/p10四页及10个编号式高斯因子的放大复核。确认σ在根号外，Q304系旧译者注释误判，现撤回并关闭；原式、公式图未改，无新增Q/E。σ为标准差，半高半宽关系及所核平方常系数相容；Q303/Q308/Q309/Q311其它问题保留。

正文、Q311关联说明、问题表、符号表、Preface、导航、勘误索引同步，合稿更新为B668。细节见全书复核/B668高斯复核.md。下一批B669优先核查Q303/Q309的实洛伦兹线形、复响应及零阻尼极限，不把不同核静默合并。\n\n''',1)
edit('翻译管理/当前进度与续接.md',progress)
(O/'B668新增阅读提示.json').write_text(json.dumps({body:'> '+new},ensure_ascii=False,indent=2),encoding='utf-8')
(O/'B668修改文件.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2),encoding='utf-8')
# The original displayed formula blocks and source images must remain identical.
old=(B/body).read_text(encoding='utf-8-sig');cur=(R/body).read_text(encoding='utf-8-sig')
blocks=lambda s:re.findall(r'\$\$[\s\S]*?\$\$',s)
images=lambda s:re.findall(r'!\[[^\n]*?\]\([^\n]*?\)',s)
assert blocks(old)==blocks(cur) and images(old)==images(cur)
out=[]
for sigma in [.3,1,2,4]:
 n=4000;lo=-12*sigma;h=24*sigma/n
 def integ(f):return h/3*sum((1 if i in [0,n] else 4 if i%2 else 2)*f(lo+i*h) for i in range(n+1))
 raw=integ(lambda x:math.exp(-x*x/(2*sigma*sigma)))
 area=raw/(math.sqrt(2*math.pi)*sigma)
 square=integ(lambda x:math.exp(-x*x/(sigma*sigma))/(2*math.pi*sigma*sigma))
 assert abs(area-1)<1e-10 and abs(square-1/(2*math.sqrt(math.pi)*sigma))<1e-10
 delta=math.sqrt(2*math.log(2))*sigma;deltasq=math.sqrt(math.log(2))*sigma
 assert abs(math.exp(-delta*delta/(2*sigma*sigma))-.5)<1e-12
 assert abs(math.exp(-deltasq*deltasq/(sigma*sigma))-.5)<1e-12
 coefficient=(1/(math.pi*math.sqrt(2*math.pi)*sigma))**2
 assert abs(coefficient-1/(2*math.pi**3*sigma**2))<1e-12
 out.append({'sigma':sigma,'gaussian_area':area,'square_area':square,'squared_HWHM_ratio':deltasq/delta,'convolution_prefactor_square':coefficient})
(O/'B668代数检查.json').write_text(json.dumps({'cases':out,'original_display_formulas_unchanged':True,'original_image_links_unchanged':True,'Q304':'已撤回译者误报','source_corrections':0,'scope':'σ>0条件下的高斯归一化、半高宽及常系数检查'},ensure_ascii=False,indent=2),encoding='utf-8')
print('B668 updated: Q304 withdrawn; four sigma cases checked; displayed formulas/images unchanged.')

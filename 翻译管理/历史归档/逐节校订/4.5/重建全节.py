from pathlib import Path
import json,re,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2]
data=json.loads((out/'逐行提取.json').read_text(encoding='utf-8'))
prose=json.loads((out/'叙述译文映射.json').read_text(encoding='utf-8'))
tr=prose['translation'];skip=set(prose['skip'])
rows=[r for p in data for r in p['lines'] if r['id']>='p03l14']
spec=[
(326,'p03l14','分子张量：自由旋转'),(327,'p03l31','分子张量：两个零角或π角'),
(328,'p04l17','分子张量：等角非零'),(329,'p05l07','分子张量：混合零角与π角'),
(330,'p05l24','分子张量：反号角'),(331,'p06l13','空间取向定义与平均条件'),
(332,'p07l09','正文自由旋转：全对称模式'),(333,'p08l14','正文自由旋转：简并模式'),
(334,'p09l28','正文等角零/π：全对称模式'),(335,'p11l03','正文等角零/π：简并模式'),
(336,'p12l26','正文等角非零：全对称模式'),(337,'p14l01','正文等角非零：简并模式'),
(338,'p16l25','正文混合角：全对称模式'),(339,'p18l01','正文混合角：简并模式'),
(340,'p19l18','附录A：分子张量一般式'),(341,'p22l04','附录B：全对称模式'),
(342,'p26l01','附录B：简并对称模式'),(343,'p27l16','附录B：简并反对称模式'),
(344,'p28l29','附录B：简并面外模式'),(345,'p30l06','附录C：全对称模式'),
(346,'p34l04','附录C：简并对称模式'),(347,'p36l14','附录C：简并反对称模式'),
(348,'p37l22','附录C：简并面外模式'),(349,'p38l30','附录D：全对称模式'),
(350,'p42l28','附录D：简并对称模式'),(351,'p45l31','附录D：简并反对称模式'),
(352,'p47l29','附录D：简并面外模式'),(353,'p49l29','附录E：全对称模式'),
(354,'p53l26','附录E：简并对称模式'),(355,'p56l05','附录E：简并反对称模式'),
(356,'p57l13','附录E：简并面外模式'),(357,'p58l21','附录F：全对称模式'),
(358,'p62l20','附录F：简并模式代入条件'),(359,'p63l28','附录F：简并对称模式'),
(360,'p67l25','附录F：简并反对称模式'),(361,'p72l24','附录F：简并面外模式')]
assert all(any(r['id']==start for r in rows) for n,start,scope in spec)
def splitline(t,limit=180):
 parts=[]
 while len(t)>limit:
  depth=0;positions=[]
  for i,c in enumerate(t[:limit+1]):
   if c=='{' and (i==0 or t[i-1]!='\\'):depth+=1
   if c=='}' and (i==0 or t[i-1]!='\\'):depth-=1
   if depth==0 and i>65 and c in '+-':positions.append(i)
  if not positions:break
  pos=positions[-1];parts.append(t[:pos].strip());t=t[pos:].strip()
 parts.append(t);return parts
def mathmd(lines):
 chunks=[]
 for line in lines:
  chunks+=splitline(line)
 if len(chunks)==1:return '$$\n'+chunks[0]+'\n$$'
 return '$$\n\\begin{aligned}\n'+'\\\\\n'.join('&'+s for s in chunks)+'\n\\end{aligned}\n$$'

index=[];allused=[]
anomalies=[]
for si,(n,start,scope) in enumerate(spec):
 end=spec[si+1][1] if si+1<len(spec) else 'p99'
 batch=[r for r in rows if start<=r['id']<end];parts=[];pending=[];ids=[];forms=[]
 def flush():
  if pending:
   parts.append('<!-- source '+','.join(ids)+' -->\n\n'+mathmd(pending));forms.append({'source_lines':ids.copy(),'latex_lines':pending.copy()})
   t=' '.join(pending)
   unpaired=[(a,b,t.count(a),t.count(b)) for a,b in [('(',')'),('[',']'),(r'\{',r'\}')] if t.count(a)!=t.count(b)]
   if unpaired:
    anomalies.append({'batch':f'B{n}','source':ids[0],'pairs':unpaired})
    parts.append('> **译者注（原式分组疑点Q174，PDF p'+str(int(ids[0][1:3]))+'）：** 上式的括号数目不配对，按原有字符保留；候选为补足缺少的括号或删去多余括号，具体分组待核，本轮未采用。')
   if 'p62l19' in ids:
    parts.append(r'> **译者注（原文疑点Q175，PDF p62）：** 此处求和关系末项原字形为$\varpi_{ZZZ}$（Symbol字体的omega1字形），按原字符保留；候选为$\chi_{ZZZ}$，未采用。')
   pending.clear();ids.clear()
 for r in batch:
  k=r['id'];allused.append(k)
  if k in skip:flush();continue
  if r['jp']:
   flush();text=tr[k]
   if 'Q174' in text:anomalies.append({'batch':f'B{n}','source':k,'pairs':[['(',')',r['raw'].count('('),r['raw'].count(')')]],'inline':True})
   if text:parts.append('<!-- source '+k+' -->\n\n'+text)
  else:
   t=r['tex']
   # Space before scripts does not change TeX attachment; preserve original symbol choice.
   t=re.sub(r'\\Sigma\b',r'\\sum',t)
   assert not any(x in t for x in ['cid:','SCRIPTPLACE']), (k,t)
   # A mode or polarization marker begins a new component group.
   m=re.match(r'^\(([ps]{3})\)\s*',t)
   if m:flush();parts.append('**('+m[1]+')**');t=t[m.end():]
   if t.strip()=='(none)':flush();parts.append('无。');continue
   m=re.match(r'^\(([ab]_\{[12]\})\)\s*',t)
   if m:flush();parts.append('**$'+m[1]+'$**');t=t[m.end():]
   # Component equalities start a formula; following physical lines continue it.
   if re.match(r'^\\(?:beta|chi)\s*_\{',t) and '=' in t:flush()
   pending.append(t);ids.append(k)
 flush()
 content='\n\n'.join(parts)+'\n'
 (out/f'B{n}-本批译文.md').write_text(content,encoding='utf-8')
 pages=sorted(set(int(r['id'][1:3]) for r in batch))
 components=[]
 for f in forms:
  m=re.match(r'^\\(beta|chi)\s*_\{([xyzXYZ]{3})\}\s*=',f['latex_lines'][0])
  if m:components.append({'symbol':m[1],'indices':m[2],'source':f['source_lines'][0]})
 rec={'batch':f'B{n}','date':'2026-10-21','pages':pages,'scope':scope,'source_lines':[r['id'] for r in batch],'formulas':forms,'tensor_components':components,'source_corrections_adopted':False,'verification_method':'数字PDF字形/字体/基线提取与逐行覆盖核验，重点页图复核；非独立物理推导验证'}
 (out/f'B{n}-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8');index.append(rec)
 (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n范围：{scope}；PDF页'+','.join(map(str,pages))+'。\n\n每个段落与公式行均有来源定位；按原式保留函数幂、倍角、键系希腊下标、分子β及空间χ；长式按原行及运算项分行。原式重复项、缺损括号与不一致符号不据推导猜改。疑点见相应就地注释；未采用原文修正。\n',encoding='utf-8')
assert allused==[r['id'] for r in rows]
(out/'全节公式与覆盖索引.json').write_text(json.dumps({'batches':index,'line_count':len(rows),'component_count':sum(len(r['tensor_components']) for r in index)},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'原式分组疑点位置.json').write_text(json.dumps(anomalies,ensure_ascii=False,indent=2),encoding='utf-8')
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.5 两个CH₃基团的张量分量.md'
snap=out/'B326前旧译.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
prefix='\n\n'.join((out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(323,326))
prefix=prefix.replace('B323—B325已核原目录及第1—4部分（PDF p1—3）；第5部分及附录仍为旧译待核。','B323—B361已完成原PDF全78页正文及附录A—F的本轮译校；原文疑点保留并就地说明，未采用原文修正。')
prefix=prefix.replace('- 第5、6部分及附录A—F：尚待本轮核验；当前目录保留原文组织，不能将旧译表项视为已确认结果。','''- 第5部分（p3—6）：按自由旋转、等角零/π、等角非零、混合零/π和反号角五类条件列分子β。先辨认每类±号的含义，再查全对称及简并分量。
- 第6部分（p6—19）：定义基团相对于表面的扭转、倾斜和面内角；随后列四类内部旋转条件下面内随机取向的空间χ。全对称带分两支，简并带分三支，重叠时按原文对表达式求和。
- 附录A（p19—22）：保留坐标定义、变换关系及一般内部角下的分子β，简并部分分四组。
- 附录B（p22—30）、C（p30—38）、D（p38—49）、E（p49—58）：依次给自由旋转、等角零/π、等角非零、混合零/π条件的一般空间取向分量。每附录分全对称与简并模式；一般取向不能以正文随机取向表替代。
- 附录F（p58—78）：先列一般内部角下的全对称响应，再列简并分量及代入关系；后半以abc分子分量给出对称、反对称、面外三类一般空间张量。须保留左侧两个下标交换对称的适用条件。

> **译者注（核验边界）：** 全文完成原文覆盖、翻译转录与参考排版核验；原文公式中的未决疑点仍待专业核实，不因转录完成而视为推导已验证。''')
joined=prefix+'\n\n'+'\n\n'.join((out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(326,362))
target.write_text(joined,encoding='utf-8')
renderer=(out/'检查排版.cjs').read_text(encoding='utf-8')
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
whole=(out.parent/'4.4/检查全节排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.4','校订记录/4.5').replace("startsWith('4.4 ')","startsWith('4.5 ')")
if not (out/'检查全节排版.cjs').exists():(out/'检查全节排版.cjs').write_text(whole,encoding='utf-8')
print(json.dumps({'batches':len(spec),'source_lines':len(rows),'components':sum(len(r['tensor_components']) for r in index)},ensure_ascii=False))

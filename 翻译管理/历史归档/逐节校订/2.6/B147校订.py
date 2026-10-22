from pathlib import Path
import re,json,csv,hashlib
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.6 *.md'));bs=chr(92);old=P.read_text(encoding='utf-8');a=old.index('### 1.2.');z=old.index('## 2. 传播',a)
assert not (O/'B147-修订前.md').exists();(O/'B147-修订前.md').write_text(old,encoding='utf-8');s=old[a:z]
def split(m):
 t=m[1];tags=re.findall(re.escape(bs)+r'tag\{([^}]+)\}',t)
 if len(tags)<=1:return m[0]
 t=t.replace(bs+'begin{aligned}','').replace(bs+'end{aligned}','').strip();out=[];pos=0
 for tag in tags:
  i=t.index(bs+'tag{'+tag+'}',pos);chunk=t[pos:i].strip();chunk=re.sub(r'^\\\\(?:\[[^]]+\])?\s*','',chunk).strip();chunk=re.sub(r'\\\\(?:\[[^]]+\])?\s*$','',chunk).strip()
  if tag=='1.5a':chunk=chunk.replace('E_x^-',bs+'theta_x^-')
  out.append('$$\n'+bs+'begin{aligned}\n'+chunk+'\n'+bs+'end{aligned}'+bs+'tag{'+tag+'}\n$$');pos=i+len(bs+'tag{'+tag+'}')
 return '\n\n'.join(out)
s=re.sub(r'\$\$([\s\S]*?)\$\$',split,s)
s=s.replace('### 1.2. Born & Wolf 的思路','### 1.2. Born与Wolf的思路')
nt='''

> **原文疑点（Q087，PDF p2，式1.5a）**：右端原印为 $§theta_x^-$，此处按原字形保留，未沿用旧译的 $E_x^-$。由式1.3a、1.3c消去 $H_y^-$ 得到的候选为 $E_z^-=(§sin§theta/§cos§theta)E_x^-$，亦与式1.5b相应；该候选尚未作为原文修正采用。

'''.replace('§',bs)
for m in re.finditer(r'\$\$([\s\S]*?)\$\$',s):
 if bs+'tag{1.5a}' in m[1]:i=m.end();s=s[:i]+nt+s[i:];break
new=old[:a]+s+old[z:];assert new[new.index('## 2. 传播'):]==old[z:];P.write_text(new,encoding='utf-8');(O/'B147-本批译文.md').write_text(s,encoding='utf-8')
new=new.replace('B146完成PDF p1的1.1引言，止于1.2标题前；后续为旧译待校订。','B146—B147完成PDF p1—2的1.1引言与1.2，含式（1.1）—（1.5b），止于第2部分前；后续为旧译待校订。').replace('本批已核引言；后续按标题包含传播关系、不同界面数的矩阵及单层至三层膜内电场，尚未逐项校订。','已核引言及1.2的方向与电磁场关系；后续按标题包含传播关系、不同界面数的矩阵及单层至三层膜内电场，尚未逐项校订。');P.write_text(new,encoding='utf-8')
tags=re.findall(re.escape(bs)+r'tag\{([^}]+)\}',s);assert tags==['1.1','1.2','1.3a','1.3b','1.3c','1.4a','1.4b','1.4c','1.5a','1.5b']
sha=hashlib.sha256((R/'日语原版/Chapter2/chap2-6.pdf').read_bytes()).hexdigest();assert sha=='329e6cc656b6e143555bac82f6320e9dd051ee782f93151a1c743159f76f2f35'
(O/'B147-覆盖.json').write_text(json.dumps({'batch':'B147','date':'2026-10-20','pages':[1,2],'tags':tags,'source_sha256':sha,'source_corrections_adopted':False,'unreviewed_tail_unchanged':True},ensure_ascii=False,indent=2),encoding='utf-8')
(O/'B147.md').write_text('''# B147：1.2方向及电磁场分量

2026-10-20，独立PDF p1—2至第2部分前。完整核坐标、s_z正负与上下标、方向单位矢量、两条矢量积、n与μ/ε关系、六组电磁场分量、偏振分量说明及1.5a/b。十个原编号独立显示，避免一个数学环境多个编号。

Q087：1.5a原字形θ_x^-，恢复旧译无注改为E_x^-的做法；候选由1.3a/c给出，仅放就地注。无采用原文修正；第2部分及以后逐字保持。下一批B148先核第2部分总述、单介质正逆传播与多介质矩阵次序2.1/2.2a/b，再按完整偏振组推进。
''',encoding='utf-8')
f=R/'翻译管理/当前进度与续接.md';v=f.read_text(encoding='utf-8');i=v.index('\n')+1;v=v[:i]+'''\n## 当前有效状态：B147完成2.6的1.2（2026-10-20）

B146—B147已核p1—2至第2部分前：引言、方向与单位矢量、电磁矢量积、六组分量关系及1.5a/b，共十个编号式。1.5a恢复θ_x^-原字形，候选E_x^-只注Q087；没有采用原文修正。第2部分及以后逐字保持。

下一批B148：从第2部分传播总述开始，核四项特点、单介质2.1及无编号MN/行列式关系、分层区间与多介质2.2a/b，止于p3“以下考虑平面波”前；特别核正逆矩阵相反乘积顺序，不把源项适用限制扩成一般结论。以下为历史记录。

'''+v[i:];f.write_text(v,encoding='utf-8')
for rel,col in [('翻译管理/章节清单.tsv','编号'),('翻译管理/全书调查/分批建议.tsv','节号')]:
 f=R/rel
 with f.open(encoding='utf-8-sig',newline='') as h:d=csv.DictReader(h,delimiter='\t');fields=d.fieldnames;rows=list(d)
 for row in rows:
  if row[col]!='2.6':continue
  if col=='编号':row['状态']='B146—B147完成引言及1.2；第2部分起待校订';row['映射核验']='独立12页；p1—2至第2部分前已逐项核验';row['公式图表范围']='已核1.1—1.5b共十编号式及无编号折射率关系';row['导读状态']='已更新B147范围'
  else:row['执行状态']='B146—B147已核第1部分；B148续第2部分总述及2.1/2.2a/b；后续未核'
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(rows)
f=R/'Preface序言.md';v=f.read_text(encoding='utf-8').replace('（B146已核1.1引言，后续待校订）','（B146—B147已核第1部分，后续待校订）');f.write_text(v,encoding='utf-8')
f=D/'阅读导航.md';v=f.read_text(encoding='utf-8').replace('2.6已核1.1引言','2.6已核第1部分').replace('B146已核1.1引言：','B146—B147已核第1部分：').replace('后续按标题含1.2方向/场关系、第2部分传播矩阵','1.2已核方向定义、矢量积与十个编号式，Q087保留并注。后续按标题含第2部分传播矩阵');f.write_text(v,encoding='utf-8')
for rel,extra in [('翻译管理/疑难与勘误.md','\n| Q087 | 2.6 PDF p2，式1.5a | 右端θ_x^-，旧译无注写E_x^- | 恢复原字形；由1.3a/c可得E_x^-候选，只放就地注，未采用修正，B147。 |\n'),('翻译管理/校订记录/2.6/局部约定卡.md','\nB147：xz为入射面，入射方向x/z均正；s_z>0标+，s_z<0标−，反射波s_x仍为正。s是传播单位矢量，不是s偏振标签；E/H矢量积次序照原文。μ=1时n=√ε；s偏振E仅y、p偏振H仅y。1.5a的θ_x^-疑点只注不改。\n'),('翻译管理/校订记录/2.6/结构与复用核验表.md','\nB147更新：1.2跨p1—2至1.5b已全部逐项核验；十个编号式完整，1.5a疑点Q087保留。第2部分及以后仍待核。\n')]:
 f=R/rel;f.write_text(f.read_text(encoding='utf-8')+extra,encoding='utf-8')
print('B147 ten equations written; source and later scope preserved')

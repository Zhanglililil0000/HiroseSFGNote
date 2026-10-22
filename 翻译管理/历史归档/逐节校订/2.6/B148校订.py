from pathlib import Path
import json,csv,re
O=Path(__file__).resolve().parent;R=O.parents[2];D=R/'中文版本/第二章 薄膜产生的SFG';P=next(D.glob('2.6 *.md'));old=P.read_text(encoding='utf-8');a=old.index('## 2. 传播');z=old.index('以下考虑平面波。',a)
assert not (O/'B148-修订前.md').exists();(O/'B148-修订前.md').write_text(old,encoding='utf-8');s=old[a:z]
s=s.replace('将伴随光波动的物理量的振幅记为','将与光波相伴的物理量的振幅记为').replace('对于像 SFG 这样内部有光源产生新增光（而非倍增光）的体系并不适用。','对于内部存在和频过程这类光源、以相加而非相乘方式引入新场的体系，这里所用的方法并不适用。')
s=s.replace('介质 n：','介质 $n$：').replace('，...，','，……，')
key='光在某介质中从'
i=s.index(key);s=s[:i]+'> **适用范围说明（译者）**：上述第4项保留原文对本方法的限制，所指为这里按振幅系数构造的传播关系；不将其扩述为所有含源项矩阵方法均不能处理和频过程。\n\n'+s[i:]
key='当光通过多种介质时';i=s.index(key);s=s[:i]+'> **记号说明（译者）**：上式的 $§mathbf{E}$ 表示单位矩阵，区别于前文电场矢量；$|§mathbf{M}|$、$|§mathbf{N}|$ 表示行列式。按式（2.1），$§mathbf{M}$ 将 $z$ 处的列向量联系到0处，$§mathbf{N}$ 则将0处的列向量联系到 $z$ 处。\n\n'.replace('§',chr(92))+s[i:]
s+='> **矩阵次序说明（译者）**：式（2.2a）从左到右依次列 $§mathbf{M}_1,§mathbf{M}_2,§ldots,§mathbf{M}_n$，式（2.2b）则为 $§mathbf{N}_n,§ldots,§mathbf{N}_2,§mathbf{N}_1$。这里按底本保留相反的乘积顺序，不将矩阵当作可交换的标量重新排列。\n\n'.replace('§',chr(92))
new=old[:a]+s+old[z:];assert new[new.index('以下考虑平面波。',a):]==old[z:];P.write_text(new,encoding='utf-8');(O/'B148-本批译文.md').write_text(s,encoding='utf-8')
new=new.replace('B146—B147完成PDF p1—2的1.1引言与1.2，含式（1.1）—（1.5b），止于第2部分前；后续为旧译待校订。','B146—B148完成PDF p1—2的第1部分及第2部分总述、式（2.1）—（2.2b），止于p3平面波说明前；后续为旧译待校订。');P.write_text(new,encoding='utf-8')
tags=re.findall(re.escape(chr(92))+r'tag\{([^}]+)\}',s);assert tags==['2.1','2.2a','2.2b']
(O/'B148-覆盖.json').write_text(json.dumps({'batch':'B148','date':'2026-10-20','pages':[2],'tags':tags,'source_page_visually_checked':True,'unnumbered_relations':['MN=E','detM=detN=1'],'unreviewed_tail_unchanged':True,'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
(O/'B148.md').write_text('''# B148：传播总述与多介质矩阵顺序

2026-10-20，独立PDF p2第2部分标题至页末，止于p3平面波说明前。完整核连续量U/V、四项特点、透镜/镜面类比、单介质双向关系2.1、无编号MN与行列式关系、各层区间及2.2a/b相反乘积顺序。

E为单位矩阵、竖线为行列式另作译者记号说明；作者对含新增光源体系的适用限制按局部方法理解，不扩为所有矩阵法的结论。未修改原公式或新增疑难/勘误条目；其后旧译逐字保持。

下一批B149：p3平面波说明起，完整核s偏振的U/V、β定义及2.3a/b，再按原文后续完整偏振组推进。
''',encoding='utf-8')
f=R/'翻译管理/当前进度与续接.md';v=f.read_text(encoding='utf-8');i=v.index('\n')+1;v=v[:i]+'''\n## 当前有效状态：B148完成2.6传播总述与矩阵顺序（2026-10-20）

已核p1—2至p3平面波说明前：第1部分十编号式，加本批2.1/2.2a/b及MN、行列式关系。四项特点、分层区间、M1…Mn及Nn…N1的相反顺序完整；E单位矩阵与前文电场区分。含源项限制按作者此处方法保留，不扩述。无新增原文修正，平面波说明及以后逐字保持。

下一批B149：p3“以下考虑平面波”起，核s偏振U/V、β及2.3a/b，按完整偏振组推进。此前Q086/Q087仍保留，后续不能按旧译直接认定正负号或矩阵元素。以下为历史记录。

'''+v[i:];f.write_text(v,encoding='utf-8')
for rel,col in [('翻译管理/章节清单.tsv','编号'),('翻译管理/全书调查/分批建议.tsv','节号')]:
 f=R/rel
 with f.open(encoding='utf-8-sig',newline='') as h:d=csv.DictReader(h,delimiter='\t');fields=d.fieldnames;rows=list(d)
 for row in rows:
  if row[col]!='2.6':continue
  if col=='编号':row['状态']='B146—B148已核第1部分及传播总述/矩阵乘积；平面波段起待校订';row['映射核验']='独立12页；p1—2至平面波说明前逐项核验';row['公式图表范围']='已核13编号式及折射率/MN/行列式关系';row['导读状态']='已更新B148范围'
  else:row['执行状态']='B146—B148已核p1—2；B149续p3平面波与s偏振矩阵；其后未核'
 with f.open('w',encoding='utf-8-sig',newline='') as h:w=csv.DictWriter(h,fields,delimiter='\t');w.writeheader();w.writerows(rows)
f=R/'Preface序言.md';v=f.read_text(encoding='utf-8').replace('（B146—B147已核第1部分，后续待校订）','（B146—B148已核第1部分及传播总述，后续待校订）');f.write_text(v,encoding='utf-8')
f=D/'阅读导航.md';v=f.read_text(encoding='utf-8').replace('2.6已核第1部分','2.6已核第1部分及传播总述');v+='\nB148补充：第2部分总述、2.1与2.2a/b已核；M连接末端到起点，N连接起点到末端，层矩阵乘积顺序相反，E为单位矩阵。p3平面波及后续仍待校订。\n';f.write_text(v,encoding='utf-8')
for rel,extra in [('翻译管理/校订记录/2.6/局部约定卡.md','\nB148：U/V选界面连续量；M把z处列向量映射到0处，N反向。MN=E中E为单位矩阵，竖线表示行列式。多介质M1…Mn与Nn…N1顺序相反，保留原次序。这里不含新增源项的振幅系数关系，不据此否定其他含源项矩阵扩展。\n'),('翻译管理/校订记录/2.6/结构与复用核验表.md','\nB148更新：第2部分p2总述、单介质及多介质关系2.1/2.2a/b已核。p3平面波和具体偏振矩阵尚待核，不能视为第2部分完成。\n')]:
 f=R/rel;f.write_text(f.read_text(encoding='utf-8')+extra,encoding='utf-8')
print('B148 written: 3 numbered relations, tail unchanged')

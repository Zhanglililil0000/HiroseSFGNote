from pathlib import Path
import json,csv,io,hashlib,re,math
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
target=r/'中文版本/第五章 张量与对称性/5.1 和频张量与对称性.md'
batch=(o/'B424-本批译文.md').read_text(encoding='utf-8')
t=target.read_text(encoding='utf-8')
if '## 线性极化与不可约基底' not in t:
 (o/'B424前分批稿.md').write_text(t,encoding='utf-8')
 t=re.sub(r'<!-- B423结束：[\s\S]*?-->\s*$', '',t).rstrip()+'\n\n'+batch
 t=t.replace('B423已完成PDF p1的翻译及原页对照。p2—7尚未翻译；','B423—B424已完成PDF p1及p2上半至式(2)的翻译及原页对照。p2表1起尚未翻译；')
 target.write_text(t,encoding='utf-8')
cov=[('p2首段','电场为极矢量及Vb/Va/V0对应','首段'),('p2首段后半','α不可约分量1+3+5个，含下标变体','首段及记号说明'),('p2式(1a)','Px的3个电场系数','式(1a)及Q200'),('p2式(1b)','Py的3个电场系数','式(1b)'),('p2式(1c)','Pz的3个电场系数','式(1c)'),('p2式(2)前引言','基底张量与笛卡尔分量关系','上述表达式段'),('p2式(2)第1行','0阶1个分量','式(2)第1行'),('p2式(2)第2—4行','1阶3个分量','式(2)第2—4行'),('p2式(2)第5—9行','2阶5个分量','式(2)第5—9行')]
(o/'B424-覆盖.json').write_text(json.dumps([{'原文定位':a,'对象':b,'译文定位':c,'已翻译':True,'已对照':True} for a,b,c in cov],ensure_ascii=False,indent=2),encoding='utf-8')
# Check the nine field coefficients against all nine independent Cartesian unit tensors.
# This is an internal consistency check of the printed equations, not a physics proof.
s2=math.sqrt(2);s3=math.sqrt(3);s6=math.sqrt(6);actual=[[[] for j in range(3)] for i in range(3)]
candidate=[]
for u in range(9):
 a=[float(i==u) for i in range(9)];xx,xy,xz,yx,yy,yz,zx,zy,zz=a
 b0=(xx+yy+zz)/s3;b1b=(yz-zy)/s2;b1a=(zx-xz)/s2;b10=(xy-yx)/s2
 b2b=(xx-yy)/s2;b2a=(xy+yx)/s2;b21b=(zx+xz)/s2;b21a=(yz+zy)/s2;b20=(-xx-yy+2*zz)/s6
 vals=[[b0/s3-b20/s6+b2b/s2,(b10+b2a)/s2,(b1a+b21b)/s2],[(-b10+b2a)/s2,b0/s3-b20/s6-b2b/s2,(b1b+b21a)/s2],[(b1a+b21b)/s2,(-b1b+b21a)/s2,b0/s3+2*b20/s6]]
 for i in range(3):
  for j in range(3):actual[i][j].append(round(vals[i][j],12))
 candidate.append(round((-b1a+b21b)/s2,12))
names=['xx','xy','xz','yx','yy','yz','zx','zy','zz'];checks=[]
for i in range(3):
 for j in range(3):
  expected=[float(k==3*i+j) for k in range(9)]
  checks.append({'P分量':'xyz'[i],'E分量':'xyz'[j],'按式2所得系数':{names[k]:v for k,v in enumerate(actual[i][j]) if v},'与前页一致':actual[i][j]==expected})
assert sum(not x['与前页一致'] for x in checks)==1 and candidate==[float(k==2) for k in range(9)]
(o/'B424-定义一致性检查.json').write_text(json.dumps({'方法':'对九个独立笛卡尔单位张量分别代入，浮点计算取12位小数','原式检查':checks,'候选负号得到alpha_xz':True,'用途':'只定位原式内部符号差异；不作为物理认证，候选未采用'},ensure_ascii=False,indent=2),encoding='utf-8')
rec={'批次':'B424','小节':'5.1','底本':'日语原版/Chapter5/chap5-1.pdf','source_sha256':hashlib.sha256((r/'日语原版/Chapter5/chap5-1.pdf').read_bytes()).hexdigest(),'范围':'PDF p2首電場成分Ej至式(2)末行；不含C3v引言及表1/表2','translation_sha256':hashlib.sha256(batch.encode('utf-8')).hexdigest(),'批次译文':'B424-本批译文.md','合稿SHA256':hashlib.sha256(target.read_bytes()).hexdigest(),'已起草':True,'已原页对照':True,'已排版':False,'覆盖单元':9,'编号式':['1a','1b','1c','2'],'式2分量数':9,'新疑点':['Q200'],'采用原文修正':False,'下一批':'B425：p2的C3v例子引言、表1、表下注释及表2，按完整表格控制范围'}
(o/'B424验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B424.md').write_text('# B424｜5.1 PDF p2上半\n\n2026-10-21。范围从页首“電場成分Ej”至式(2)末行，不含下一段C₃ᵥ例子引言和两张表。9个覆盖单元，式(1a)—(1c)的9个场系数，式(2)的9个基底分量均已原页对照。\n\n保留引言α的一阶下标b/a与公式1b/1a的原记号差异。逐项核对正负号、根号、2系数及zx/xz、yz/zy、xy/yx次序。Q200：式(1a)的Ez项按式(2)代入不一致；原式保留，候选只列注释。9个笛卡尔单位张量代入只定位到这一处差异，不冒称独立物理证明。\n\n排版状态另见验收JSON。下一批B425从C₃ᵥ例子引言开始，先处理表1及说明，再核表2；不得直接跳至p3。\n',encoding='utf-8')
def append(p,key,body):
 t=p.read_text(encoding='utf-8')
 if key not in t:p.write_text(t.rstrip()+'\n\n'+body+'\n',encoding='utf-8')
append(r/'翻译管理/疑难与勘误.md','## Q200｜','## Q200｜5.1 p2式(1a)的Ez项符号\n\nB424原页确认原式为(α₁ₐ⁽¹⁾+α₁ᵦ⁽²⁾)/√2。按式(2)代入得到αzx，与p1线性极化公式所需αxz不同。候选为(−α₁ₐ⁽¹⁾+α₁ᵦ⁽²⁾)/√2。原文未明确限制αxz=αzx。正文保留原式，注释列候选；状态：待核验、未采用原文修正。定义一致性检查见5.1/B424-定义一致性检查.json。')
append(o/'局部约定卡.md','B424（PDF p2上半）','B424（PDF p2上半）：\n\n- E为极矢量，原文Vb(Vx)、Va(Vy)、V0(Vz)对应保留。\n- 本页引言一阶α下标b/a，式(1)/(2)用1b/1a，分别保留。\n- α⁽⁰⁾为标量基底，α⁽¹⁾三项反对称组合，α⁽²⁾五项对称无迹组合，具体正负和归一化按式(2)。\n- 不预设αij=αji；Q200候选未采用。')
# Register the new lexical item as provisional, not as a user-confirmed term.
p=r/'翻译管理/术语表.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
if not any(x['日语候选']=='極性ベクトル' for x in rows):
 n=max(int(re.search(r'\d+',x['术语编号']).group()) for x in rows)+1;row={x:'' for x in fields};row.update({'术语编号':f'T{n:03d}','日语候选':'極性ベクトル','英语辅助释义':'polar vector','推荐中文候选':'极矢量','定义与适用语境':'5.1 p2：电场与位置矢量具有同样的变换性质；后文与轴矢量区别。','原文位置':'5.1 PDF p2首段 / B424','依据':'原页日语与语境已核对；中文暂用','状态':'原词及语境已页面对照；中文暂用','文本定位状态':'B424原页核对','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'译者辅助对应，本句未列英文'});rows.append(row)
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
print('B424已登记并合入正文，等待排版验收。')

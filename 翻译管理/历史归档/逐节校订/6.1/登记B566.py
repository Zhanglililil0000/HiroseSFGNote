from pathlib import Path
import hashlib,json,re
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent;p=r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md'
t=p.read_text(encoding='utf-8');assert '\\tag{1.3}' not in t
t=re.sub(r'\n<!-- B565结束：[\s\S]*?-->\s*$','\n',t)
t=t.replace('本批完成PDF p1—3：原目录、引言、1.1经典力学模型及其脚注。p4起1.2“线性极化率”尚未翻译。','B565完成PDF p1—3的原目录、引言、1.1及脚注；B566完成p4的1.2前两个论述单元，至式(1.4)后与经典式的对应关系说明。p4“量子论与经典论结果的差异”起尚未翻译。').replace('译校状态（B565，2026-10-21）','译校状态（B565—B566，2026-10-21）')
chunk=(o/'B566-本批译文.md').read_text(encoding='utf-8')
t+='\n'+chunk+'\n<!-- B566结束：PDF p4“exp(-iωt)的系数有很好的对应关系”段末。下一批B567从同页“量子论与经典论结果的差异”开始，式(1.5)与引出p5式(1.6)的句子需按完整跨页论述处理；本批未计p4全页完成。 -->\n';p.write_text(t,encoding='utf-8')
units=[('1.2标题及第1段','经典式(1.2)、同频响应、幅度比与线性极化率'),('式(1.3)第1行','χij^(1)=Pi^(1)/Ej'),('式(1.3)第2行','Ne²/h、求和gn、两项矩阵元次序、±ωng、+iΓng、ρg^(0)'),('参考文献行','Shen书名、Wiley1984、第2.2节'),('Shen约定段','exp(-iωt)时间部分、最终取实部及hωng能量差'),('经典对应标题及首句','对应式(1.2a)方括号第二项'),('所关注的方括号式','两个矩阵元乘积及分母照录'),('矩阵元比较段','复共轭、q²和原r/q比较；Q233'),('式(1.4)左端','两个分式之差'),('式(1.4)中间项','-2ωng/[(ω+iΓng)²−ωng²]'),('式(1.4)末项','ω²−(ωng²+Γng²)+2iωΓng括号与符号'),('本批末段及重引方括号式','经典两时间因子、ωo及第二项系数对应')]
cov=[{'原文定位':'PDF p4 / '+a,'对象':b,'译文定位':'B566-本批译文.md / 对应标题、段落及原式号','已翻译':True,'已原页对照':True} for a,b in units]
(o/'B566-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
rec={'批次':'B566','节':'6.1','范围':'PDF p4的1.2前两个小标题，至式(1.4)后的经典对应段末','source_sha256':hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest(),'translation_sha256':hashlib.sha256(chunk.encode('utf-8')).hexdigest(),'覆盖单元':len(cov),'编号式':['1.3','1.4'],'文献条目':1,'原图':0,'原脚注':0,'已起草':True,'已原页对照':True,'已排版':False,'疑点':['Q232','Q233'],'承接疑点':['Q230','Q231'],'采用原文修正':False,'下一批':'B567，自p4量子论与经典论结果的差异起，连同式(1.5)和p5运动方程引句按完整跨页单元处理'}
(o/'B566验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B566.md').write_text('# B566｜6.1 PDF p4前两个论述单元\n\n完成量子论的线性极化率、Shen原文引书和exp(-iωt)约定，以及经典/量子形式对应式(1.4)。12个覆盖单元，2个编号式、1条文献；无原图和脚注。\n\n逐项核对求和gn、ρg^(0)、矩阵元ng/gn及i/j次序、两个+iΓng、分母−(ωng²+Γng²)。普通h字形有局部放大图，按原文保留；r/q只作原文形式比较。Q232—Q233待核，未采用修正。原p4末第三小标题及式(1.5)未纳入本批完成范围。\n',encoding='utf-8')
print('B566登记完成，等待排版。')

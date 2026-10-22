from pathlib import Path
import json,hashlib,re
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
target=r/'中文版本/第五章 张量与对称性/5.1 和频张量与对称性.md'
source=r/'日语原版/Chapter5/chap5-1.pdf';sha=hashlib.sha256(source.read_bytes()).hexdigest()
spec={
425:('p2式(2)后C3v引言至表2末','表格',[('例子引言及表1标题','正文'),('表1的A1行','1/1/1及三个基底条目'),('表1的A2行','1/1/-1及Jz'),('表1的E行','2/-1/0及四对基底'),('表下注释','T/J/拉曼张量及逗号前后对应'),('表2标题及A1行','x镜面约定及全部12个标量/基底条目'),('表2的A2行','全部8个条目'),('表2的E行','17对条目：V1、α3、β5、γ8；缺左括号保留')]),
426:('p3首C3v乘积至式(5)引言','正文及公式',[('不可约表示乘积','全部六组乘积关系'),('乘积解释','同一/不同对象及A2×E变换'),('附录C引用','保留'),('式(3)','xx=yy及zz，非零分量'),('拉曼基频/二倍频/组合带','保留不完全推敲声明'),('广濑式方法','张量乘积及式3用途'),('式(4a)','四项关系及符号'),('式(4b)','三对关系及zzz'),('镜面与式5引言','x/y约定及球对称群基底')]),
427:('p3式(5a)首行至p4式(5a)末行','公式',[]),
428:('p4式(5b)九行','公式',[]),
429:('p4式(5c)九行','公式',[]),
430:('p4附录A至p5末欧拉角定义','附录A及B',[('附录A标题及书目','Bunker 1979完整书目信息'),('附录A正文','等价配置、Hamilton算符不变与不可观测区分'),('附录B引言','适用坐标系、归属声明与一般性'),('矢量与坐标变换','共原点及列矢量'),('式B1','x=DX'),('式B2','全部9个矩阵元素'),('Z轴旋转','观察方向及9个矩阵元素'),('Y轴旋转','9个矩阵元素'),('RK记法','下标旋转轴及角度'),('欧拉角定义','两右手系、三次旋转及角度组')]),
431:('p6欧拉角乘积至二指标基底前记号说明','附录B',[('欧拉角乘积','z/y撇/Z轴次序及χθφ'),('展开矩阵','逐行9个元素；dij为排版索引'),('欧拉角定义差异','第二次绕x/y及转引提醒'),('等长矢量及不正操作','镜映、旋转反射与置换反演群'),('XY镜映及反演矩阵','D=IRz(pi)，两个3×3矩阵'),('旋转—反演群','任意旋转及旋转乘反演'),('epsilon','行列式、极/轴矢量及星号'),('记号说明','上标阶数、下标便宜记号及右端仅列指标')]),
432:('p6二指标张量基底至p7附录C之前','附录B基底',[('0阶','1式及标量括注'),('1阶','3式、3星号及3组轨道括注'),('2阶','5式及5个nd轨道括注；缺括号原样保留'),('末段文件引用','基底张量；仅题名对应5.4，未称已核正文')]),
433:('p7附录C标题至全稿末','附录C',[('引言及小标题1','绕z旋转与T变换'),('式C1','3式及m/n指标差异'),('n重对称性说明','m=n、n偶且m=n/2、m>1三种条件'),('小标题2及式C2a','2式及各自两种m条件'),('式C2b','2式与原正负号'),('式C2c','3式、竖线及重复项'),('末段','yz镜面、x奇偶、极/轴矢量')])}
manifest=json.loads((o/'式5逐项清单.json').read_text(encoding='utf-8'))
for n in [427,428,429]:spec[n][2].extend((x['component'],str(x['terms'])+'项；原页逐项对照') for x in manifest if x['batch']==f'B{n}')
questions={425:['Q201'],426:['Q202'],427:['Q203'],428:['Q203（同组后续）'],429:['Q203（同组后续）'],430:[],431:['Q204'],432:['Q205','Q206'],433:['Q207','Q208']}
for n,(loc,kind,objs) in spec.items():
 b=f'B{n}';p=o/(b+'-本批译文.md');t=p.read_text(encoding='utf-8')
 cov=[{'原文定位':loc+' / '+a,'对象':c,'译文定位':a,'已翻译':True,'已原页对照':True} for a,c in objs]
 (o/(b+'-覆盖.json')).write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
 d={'批次':b,'范围':loc,'对象类型':kind,'source_sha256':sha,'translation_sha256':hashlib.sha256(t.encode('utf-8')).hexdigest(),'已起草':True,'已原页对照':True,'已排版':False,'覆盖单元':len(cov),'疑点':questions[n],'采用原文修正':False,'复核性质':'模型原页二次对照；不代表独立物理审校'}
 (o/(b+'验收.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
 (o/(b+'.md')).write_text('# '+b+'｜5.1 '+loc+'\n\n日期：2026-10-21。已按原页逐项翻译并对照，覆盖清单及摘要见同批JSON。\n\n本批包含'+str(len(cov))+'个覆盖单元；检查段落条件、未完成语气、上下标、正负号及所有括注。疑点：'+('、'.join(questions[n]) if questions[n] else '无新增')+'。原文未修改；所有候选只作注释。排版状态由渲染结果及验收JSON登记。\n',encoding='utf-8')
old=target.read_text(encoding='utf-8')
snapshot=o/'B425前分批稿.md'
if not snapshot.exists():snapshot.write_text(old,encoding='utf-8')
base=snapshot.read_text(encoding='utf-8')
base=re.sub(r'<!-- B424结束：[\s\S]*?-->\s*$','',base).rstrip()
alltext=base+'\n\n'+'\n\n'.join((o/f'B{n}-本批译文.md').read_text(encoding='utf-8').strip() for n in spec)+'\n'
alltext=alltext.replace('B423—B424已完成PDF p1及p2上半至式(2)的翻译及原页对照。p2表1起尚未翻译；本文件为分批稿，不代表全节完成。','B423—B433已完成全7页正文、两张表、27个三指标张量分量及附录A—C的翻译和原页对照；整节排版验收结果另见管理记录。Q198—Q208均为保留原文的未决疑点，候选未采用。')
start='> **阅读导引（译者编写，暂定）：**'
lines=alltext.splitlines()
for i,line in enumerate(lines):
 if line.startswith(start):lines[i]='> **阅读导引（译者编写）：** 先区分张量指标数与不可约角动量阶数，再由线性极化的九个基底进入C₃ᵥ特征标表及非零分量关系；式(5a)—(5c)完整列出三指标张量的27个分量。附录A概述置换反演群的出发点，附录B说明坐标变换、极／轴矢量和基底记号，附录C讨论绕z轴旋转及基底乘积。实际使用欧拉矩阵或乘积规则前须并读Q204、Q207、Q208；本轮原页对照不代表原式已获独立物理证明。'
alltext='\n'.join(lines)+'\n';target.write_text(alltext,encoding='utf-8')
qs={
'Q201':'p2表2：β二阶一对基底缺左括号；副本编号未细分；表题含x镜面与p3式4后含y镜面的叙述对应待核。',
'Q202':'p3式3后：简并基频所列非零分量与表1完整E基底的适用范围不明；作者组合带结论“尚未完全推敲清楚”保留。',
'Q203':'p3—4式5：四行Y二阶基底下标为02b,1，前导0保留。各式系数按原文，不按预想对称性改写。',
'Q204':'p6欧拉角展开矩阵：第一行第一列在零角时为0，非单位矩阵；旋转乘积与展开矩阵关系待核。保持全部原式。',
'Q205':'p6一阶基底：Jz括注为2py、4pz，2py候选2pz未采用；括注轨道与星号反演性的对应亦待核。',
'Q206':'p7二阶D2b：底本缺右括号且根号分母作用范围不明。保留(xx−yy/√2；候选(xx−yy)/√2未采用。',
'Q207':'p7式C1：左端mb/ma，右端nb/na，角度因子mχ，保留n/m差异。',
'Q208':'p7式C2a/C2b：交叉乘积的正负号与和/差频下标对应待核；C2c下标孤立竖线及重复S0T0原样保留。'}
p=r/'翻译管理/疑难与勘误.md';t=p.read_text(encoding='utf-8')
for q,desc in qs.items():
 if '## '+q+'｜' not in t:t+='\n\n## '+q+'｜5.1原文疑点\n\n'+desc+'\n\n状态：待核验，原文保留，未采用修正。详见5.1对应正文注释及B425—B433覆盖记录。\n'
p.write_text(t,encoding='utf-8')
(o/'余部登记.json').write_text(json.dumps({'batches':list(spec),'疑点':qs,'source_sha256':sha,'合稿SHA256':hashlib.sha256(target.read_bytes()).hexdigest(),'状态':'原页对照完成，等待数学渲染及整节复核'},ensure_ascii=False,indent=2),encoding='utf-8')
print('B425—B433已登记，正文已合入；进入排版及全节检查。')

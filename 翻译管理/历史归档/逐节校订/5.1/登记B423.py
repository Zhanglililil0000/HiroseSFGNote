from pathlib import Path
import csv, io, json, hashlib
r = Path(__file__).resolve().parents[3]; out = Path(__file__).resolve().parent
source = r/'日语原版/Chapter5/chap5-1.pdf'
target = r/'中文版本/第五章 张量与对称性/5.1 和频张量与对称性.md'
t = target.read_text(encoding='utf-8')
(out/'B423-本批译文.md').write_text(t,encoding='utf-8')
coverage = [
 ('p1第1段','三指标张量、点群与柔性分子、置换反演群','对称性与张量分量第1段'),
 ('p1第2段','共原点坐标系与附录B','第2段'),
 ('p1第3段前半','order/rank、2n+1、约化及表示维数','首先简要介绍张量段及术语说明'),
 ('p1第3段后半','标量、矢量、原子轨道、阶数范围及V group','将标量视为张量段；Q198、Q199'),
 ('p1第4段','点群/置换反演群基底及原文引用文件','这些基底也是段及引用说明'),
 ('p1第5段前半','线性响应与实验室/分子系，未编号式2个','分子极化率及P_i、α(X)两式'),
 ('p1第5段中段','P(X)及对称等价构型变换，未编号式2个','P(X)连等式及α(a)变换式'),
 ('p1第5段后半','全对称条件、瑞利/拉曼及振动表示乘积','这一讨论适用于段'),
 ('p1末段','C3v的两个A1基底、非全对称零值与混频','综上段'),
]
cov = [{'原文定位':a,'对象':b,'译文定位':c,'已翻译':True,'已对照':True} for a,b,c in coverage]
(out/'B423-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
record = {'批次':'B423','小节':'5.1','底本':source.relative_to(r).as_posix(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'范围':'PDF p1全页，原题至非線形分極テンソルにも当てはまる','译文':target.relative_to(r).as_posix(),'translation_sha256':hashlib.sha256(t.encode('utf-8')).hexdigest(),'已起草':True,'已原页对照':True,'已排版':False,'新疑点':['Q198','Q199'],'采用原文修正':False,'下一批':'B424，p2首電場成分Ej起，先完成式(1a)—(1c)及式(2)完整组'}
(out/'B423验收.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'B423.md').write_text('# B423｜5.1 PDF p1\n\n2026-10-21。新译；无旧中文正文。底本SHA256及译文摘要见验收JSON。\n\n范围：原题至本页末非线性极化张量适用性结论；9个覆盖单元、4个无编号独立公式，末段2个不可约基底符号。无图、表、脚注及独立书目。逐句核对条件、括注、全对称/非全对称、弹性/非弹性及坐标变换方向。\n\norder/rank按本节定义解释，原日语及英语并列保留；Q198、Q199仅加疑点说明，原文未改。附录和后续页未计完成。排版状态以验收JSON及渲染检查为准。\n\n下一批B424：p2首电场分量及基底定义，至式(2)完整组结束；表1另批处理。\n',encoding='utf-8')
def append_once(p,marker,body):
 old = p.read_text(encoding='utf-8')
 if marker not in old: p.write_text(old.rstrip()+'\n\n'+body+'\n',encoding='utf-8')
append_once(r/'翻译管理/疑难与勘误.md','## Q198｜','## Q198｜5.1 p1原子轨道的指标数\n\nB423原页确认写“主量子数减去1”。原文未限定轨道集合或进一步定义此处指标数。保留原文，不自行替换为其他量子数；待结合后续基底表核验。状态：待核验，未采用原文修正。\n\n## Q199｜5.1 p1不可约分量阶数范围\n\n原文称除单指标张量外，n指标张量存在0至n阶分量。适用范围及是否取决于张量对称性和具体分解待核验；保留原文。状态：待核验，未采用原文修正。')
append_once(r/'翻译管理/符号与约定.md','## 5.1初始约定','## 5.1初始约定（B423，p1）\n\norder（次元数）按定义解释为指标数；rank（階数）解释为不可约角动量阶数，不是矩阵秩或响应阶数。α为分子线性极化率，α上括号数字为不可约角动量阶数。a/b/c分子系，X/Y/Z实验室系；T(X:a)由a系变至X系。V group及冒号记法保留原文。详见5.1局部约定卡。')
p = r/'翻译管理/章节清单.tsv'; reader = csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
for row in rows:
 if row['编号']=='5.1':
  row.update({'暂定中文标题':'和频张量与对称性','现有译文路径':target.relative_to(r).as_posix(),'状态':'翻译中：B423已译并原页对照p1/7；排版待验收','映射核验':'PDF p1标题与正文已原页核对；p2—7尚未译校','公式图表范围':'p1四个无编号独立公式及末段两个基底符号已对照；p2起待核','导读状态':'临时导读；全节未完成','导读草案':'p1说明张量指标数、不可约角动量阶数及对称性对极化率的约束；后续C3v实例和附录A—C待逐页译校。'})
s=io.StringIO(newline=''); w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n'); w.writeheader(); w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8');t=t.replace('- 5.1 SFG 张量与对称性（待翻译）：联系张量分量与对称性。','- [5.1 和频张量与对称性](中文版本/第五章%20张量与对称性/5.1%20和频张量与对称性.md)（翻译中，p1/7已对照）：从指标数及不可约角动量阶数入手，说明对称性对极化率张量的约束；后续C₃ᵥ实例及附录A—C尚待译校。');p.write_text(t,encoding='utf-8')
renderer=(r/'翻译管理/校订记录/4.11/检查排版.cjs').read_text(encoding='utf-8').replace("校订记录/4.11","校订记录/5.1").replace("中文版本/第四章 单层膜与多层膜的和频","中文版本/第五章 张量与对称性").replace("startsWith('4.11 ')","startsWith('5.1 ')")
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
print('B423登记完成；下一步排版验收。')

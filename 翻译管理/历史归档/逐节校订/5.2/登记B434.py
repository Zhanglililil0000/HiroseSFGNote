from pathlib import Path
import hashlib,json,csv,io
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
target=r/'中文版本/第五章 张量与对称性/5.2 主要点群的特征标表与基底.md';text=target.read_text(encoding='utf-8')
(o/'B434-本批译文.md').write_text(text,encoding='utf-8')
coverage=[('原题与第1段','V/D/Y/W、abc及各散射过程'),('第2段','按对称种给出表格的组织方式'),('第3段','无分子激发的过程、全对称条件及逆变换'),('第4段','拉曼对称条件及W的abba分量方法'),('目录引言','星号定义及两栏转一栏说明')]
groups={2:'Cs/Ci/C2',3:'C2v/C2h',4:'D2/D2h',5:'C3v/D3',6:'C5v/C4v',7:'D4/D2d',8:'C6v/D6',9:'D3d/D4d',10:'D5d/D6d',11:'D3h/D5h',12:'D4h',13:'D6h',14:'C3/C4',15:'C6/S4',16:'S6/C3h',17:'C4h/C6h',18:'Td/Th',19:'T/O',20:'Oh',21:'C∞v',22:'D∞h'}
coverage.extend((f'目录页码{k}',v+'及原星号') for k,v in groups.items())
cov=[{'原文定位':'PDF p1 / '+a,'对象':b,'译文定位':a,'已翻译':True,'已原页对照':True} for a,b in coverage]
(o/'B434-覆盖.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
src=r/'日语原版/Chapter5/chap5-2.pdf';sha=hashlib.sha256(src.read_bytes()).hexdigest()
rec={'批次':'B434','小节':'5.2','日期':'2026-10-21','底本':src.relative_to(r).as_posix(),'source_sha256':sha,'范围':'PDF p1全页，原题至目录22——D∞h','translation_sha256':hashlib.sha256(text.encode('utf-8')).hexdigest(),'已起草':True,'已原页对照':True,'已排版':False,'覆盖单元':len(cov),'目录页组数':21,'疑点':['Q209'],'采用原文修正':False,'下一批':'B435，p2 Cs特征标/基底/非零分量完整块，Ci及C2另按密度分批'}
(o/'B434验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'B434.md').write_text('# B434｜5.2 PDF p1\n\n2026-10-21。全页新译，26个覆盖单元：原题及四段说明、目录星号定义、21个页组。原页下半双栏目录按页码转单栏，保留全部点群、先后顺序及星号。无独立编号公式、无图、无脚注或独立书目。\n\n核对V/D/Y/W对应、分子系、是否伴随分子激发、拉曼规则、abba指标次序。D与5.1变换矩阵不同；目录星号与5.1左上星号不同。Q209保留原标记，未采用修正。p2—22的基底与分量尚未核对，不能按本批目录直接判定其关系。\n\n数学与排版状态见验收JSON及渲染检查。下一批B435从p2 Cs完整块开始。\n',encoding='utf-8')
p=r/'翻译管理/疑难与勘误.md';old=p.read_text(encoding='utf-8')
if '## Q209｜' not in old:p.write_text(old.rstrip()+'\n\n## Q209｜5.2 p1目录的和频活性星号\n\nB434原页核对：p3项写作C2v，* C2h*，前一星号归属不清；p9 D3d带星号。原“带星号具有和频活性”的概括及含反演点群的星号适用条件待结合后续表格核验。不补星、不删星，不将未标星判为不活性。状态：原文保留，待核验，未采用修正。\n',encoding='utf-8')
renderer=(r/'翻译管理/校订记录/5.1/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/5.1','校订记录/5.2').replace("startsWith('5.1 ')","startsWith('5.2 ')")
(o/'检查排版.cjs').write_text(renderer,encoding='utf-8')
p=r/'翻译管理/章节清单.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['编号']=='5.2':
  assert sha==row['原文SHA256']
  row.update({'暂定中文标题':'主要点群的特征标表与基底','现有译文路径':target.relative_to(r).as_posix(),'状态':'翻译中：B434完成p1原页对照，排版待验收；p2—22待译','映射核验':'PDF p1原题、四段说明及完整目录已对照；p2起密集表待核','公式图表范围':'p1目录21个页组已登记；无独立编号式；实际特征标/基底/分量表待核','导读状态':'临时导读，正文部分完成','导读草案':'p1说明V/D/Y/W记号、非零规则、拉曼张量方法及查表目录；目录星号见Q209。p2起按完整点群块逐项核验。'})
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
print('B434登记完成；22页底本摘要匹配章节清单，等待排版。')

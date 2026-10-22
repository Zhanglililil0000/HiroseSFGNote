from pathlib import Path
import json,re,hashlib,copy
o=Path(__file__).resolve().parent;r=o.parents[2]
if (o/'全节验收.json').exists():
 raise SystemExit('本节已有验收记录；停止整节重建，避免覆盖完成后的译校修改。')
raw=json.loads((o/'表格字形.json').read_text(encoding='utf-8'))
names={2:['Cₛ','Cᵢ','C₂'],3:['C₂ᵥ','C₂ₕ'],4:['D₂','D₂ₕ'],5:['C₃ᵥ','D₃'],6:['C₅ᵥ','C₄ᵥ'],7:['D₄','D₂d'],8:['C₆ᵥ','D₆'],9:['D₃d','D₄d'],10:['D₅d','D₆d'],11:['D₃ₕ','D₅ₕ'],12:['D₄ₕ'],13:['D₆ₕ'],14:['C₃','C₄'],15:['C₆','S₄'],16:['S₆','C₃ₕ'],17:['C₄ₕ','C₆ₕ'],18:['T_d','Tₕ'],19:['T','O'],20:['Oₕ'],21:['C∞ᵥ'],22:['D∞ₕ']}
notes={
(2,0):('Q210','本页Cs非零分量列有重复的βaaa及γbbba，并出现五字母下标γcbcac；p7等页也有五字母γ下标。重复项及异常下标均保留，不删字、不按期望个数补齐。'),
(4,0):('Q211','D₂的β分量列重复cab，未据常见六排列将其中一项改成bac。原有逗号是否省略亦按可见符号转写。'),
(9,0):('Q212','D₃d块的基底表按g/u分行，但其下仍列出非零β及奇数取向的γ关系，与目录星号Q209及反演条件之间的适用范围待核；不删除原列β，也不把其视为已获物理认证。'),
(15,1):('Q213','S₄特征标表B行二次基底原印x−y²，x未带平方；正文保留，不自行改为x²−y²。'),
(16,0):('Q214','S₆特征标表第二个一维表示仍印为Ag，而下方基底分类表相应位置写Au；两个原表各自保留，未静默统一。'),
(18,0):('Q215','T_d块的β关系原印aac/caa/aca及bbc/cbb/bcb等分量；与表中Y基底分类及同章其他点群的对应仍待核，不替成通行的xyz排列关系。'),
(18,1):('Q216','p18—20的高阶基底有“分配于”多个表示的条目，作者接着明确排除这些分配项再列分量关系。原书并未在这些位置给出全部分配系数；译文保留此限制，不用零值或其他点群表填补。原括注的引号未闭合，中文说明其状况。'),
(20,0):('Q217','Oₕ的A₂g特征标行在S₂≡I列为−1，而该表示以g标记。原数值及g标签均保留，需核验该列/行的对应；不由通行表覆盖原表。'),
(21,0):('Q218','p21—22的特征标表中，对称种、数值、基底各列的行距不一致，存在明显垂直错位。以下分列按各自原序记录，避免未经确认重新配对。p21基底表另印拉丁P及较小的D，不改成Π/Δ；原行续行仍保持空白对称种单元格。'),
(22,0):('Q220','D∞h基底表Γg行为原有空白，Γu行列W⁽⁴⁾的4b/4a一对。空白及u标签原样保留，不将空白解释为严格零值，也不自行调换g/u。特征标列末段保留原省略号与空白。'),
}
def clean(s):
 # Only resolve extraction artefacts visible unambiguously on the original page.
 s=s.replace(r'Y^{(0}_{)0}',r'Y^{(0)}_{0}').replace(r'W^{(2}_{2a}',r'W^{(2)}_{2a}')
 s=re.sub(r'√(?:\s|\\quad)*([23])',r'\\sqrt{\1}',s)
 s=s.replace('distributed over',r'\text{分配于}')
 s=s.replace('原引号未闭合。', '〔译者注：底本引号未闭合。〕')
 s=s.replace('˚',r'{}^\circ ')
 s=s.replace('ｇ',r'\text{ｇ}')
 s=s.replace('…',r'\ldots ')
 s=re.sub(r' {2,}',r'\\quad ',s)
 return s.strip().strip(r' ').rstrip()
def splitmath(s):
 # Split long cells at commas outside TeX braces; each fragment remains editable.
 s=clean(s);items=[];buf='';depth=0;parens=0
 for c in s:
  if c=='{':depth+=1
  if c=='}':depth-=1
  if depth==0 and c=='(':parens+=1
  if depth==0 and c==')':parens-=1
  if c==',' and depth==0 and parens<=0:
   items.append(buf);buf=''
  else:buf+=c
 if buf:items.append(buf)
 def trim(x):return re.sub(r'^(?:\\quad\s*)+|(?:\\quad\s*)+$','',x.strip()).strip()
 return '， '.join('$'+trim(x)+'$' for x in items if trim(x))
def table(ev):
 rows=copy.deepcopy(ev['rows']);cols=len(rows[0]['cells'])
 if cols==5:heads=['原表左栏','操作／特征标（按表头顺序）','原表平移基底栏','原表转动基底栏','原表二次基底栏']
 else:heads=['原表左栏','分子示例／基底（依原序，空白左栏为续行）']
 lines=['| '+' | '.join(heads)+' |','|'+'---|'*cols]
 for row in rows:lines.append('| '+' | '.join(splitmath(c) if c else '' for c in row['cells'])+' |')
 return '\n'.join(lines)
def continuous_char(ev,p):
 rows=copy.deepcopy(ev['rows'])
 # Preserve the independent source columns rather than impose a conjectural row association.
 columns=[]
 for col in range(5):
  vals=[]
  for row in rows:
   c=row['cells'][col]
   if c:vals.append(c)
  columns.append(vals)
 # Repair font-baseline attachment only, without changing any source symbol or value.
 for col in range(5):
  vals=columns[col];joined=[];i=0
  while i<len(vals):
   c=vals[i]
   if c=='_{22}' and i+1<len(vals) and vals[i+1]=='(x-y, xy)':
    joined.append('(x^{2}-y^{2}, xy)');i+=2;continue
   joined.append(c);i+=1
  columns[col]=joined
 lines=['**原特征标表：分列记录。** 各列独立按自上而下的顺序列示，下列序号不表示跨列自动对应；原稿行距错位见Q218。','']
 for title,vals in zip(['对称种列','操作表头及特征标数值列','平移基底列','转动基底列','二次基底列'],columns):
  lines+=['**'+title+'**','']
  for i,s in enumerate(vals,1):lines+=['- '+str(i)+'. '+splitmath(s)]
  lines.append('')
 return '\n'.join(lines)
sha=hashlib.sha256((r/'日语原版/Chapter5/chap5-2.pdf').read_bytes()).hexdigest()
batchindex=[];n=435
for pp,events in raw.items():
 p=int(pp);starts=[i for i,e in enumerate(events) if e['kind']=='table' and e['原表序']%2==1]
 assert len(starts)==len(names[p]),(p,len(starts),names[p])
 for gi,start in enumerate(starts):
  end=starts[gi+1] if gi+1<len(starts) else len(events);group=events[start:end];b=f'B{n}';name=names[p][gi]
  lines=['## '+('$'+name+'$' if '_' in name else name)+'（PDF p'+str(p)+'）','','> 本点群块按底本保留特征标、分子示例、基底归属及其后分量关系。原空白不等同于零。','']
  if (p,gi) in notes:
   q,desc=notes[p,gi];lines+=['> **原文疑点（'+q+'）：** '+desc,'']
  if (p,gi)==(7,1):lines+=['> **原文疑点（Q210续，PDF p7，D₂d）：** 本块γ关系中也有五字母下标；按底本逐字保留，不缩成四指标。','']
  if (p,gi)==(14,0):lines+=['> **原文疑点（Q210续，PDF p14，C₃）：** 表后有重复出现的γ等式链；原序保留，不合并重复链。','']
  if (p,gi)==(18,1):lines+=['> **原文疑点（Q218续，PDF p18，Tₕ特征标表）：** 平移及转动三元基底在原表中均排在Eᵤ行的高度，下方基底分类另列F_g/F_u。这里保留可见位置，不自行将两组三元基底移行；不能单凭该垂直位置断定其表示归属。','']
  cov=[]
  for e in group:
   if e['kind']=='table':
    ischar=e['原表序']%2==1;lines+=['### '+('特征标表' if ischar else '基底分类表及分子示例'),'']
    lines+=[continuous_char(e,p) if ischar and p>=21 else table(e),'']
    for ri,row in enumerate(e['rows']):cov.append({'原文定位':f'p{p} 原表{e["原表序"]} 行{ri+1} y={row["y"]}','对象':'表格行及所有原列','原字符数':row['字符数'],'译文定位':name+' / '+('特征标表' if ischar else '基底分类表')+f' 原行{ri+1}','已翻译':True,'已原页对照':True})
   else:
    lines.append(splitmath(e['tex']));lines.append('')
    cov.append({'原文定位':f'p{p} y={e["y"]}','对象':'分量关系／表注','原字符数':e['字符数'],'译文定位':name+' / 表后原序','已翻译':True,'已原页对照':True})
  if p==21:
   lines+=['> **原文疑点（Q219，PDF p21，基底分类表D行）：** 原行重复列出$Y_{2b}^{(3)},Y_{2a}^{(3)}$，并列出$W_{2b}^{(1)},W_{2a}^{(1)}$；后者的不可约阶数与下标范围存在疑点。重复条目及原阶数均保留，未改成二阶分量。','']
  text='\n'.join(lines)+'\n';(o/(b+'-本批译文.md')).write_text(text,encoding='utf-8')
  (o/(b+'-覆盖.json')).write_text(json.dumps(cov,ensure_ascii=False,indent=2),encoding='utf-8')
  rec={'批次':b,'PDF页':p,'点群':name,'范围':'完整特征标表、基底分类表、原示例与表后全部分量/注释','source_sha256':sha,'translation_sha256':hashlib.sha256(text.encode('utf-8')).hexdigest(),'已起草':True,'已原页对照':True,'已排版':False,'覆盖单元':len(cov),'表格数':2,'字符数':sum(x['原字符数'] for x in cov),'采用原文修正':False,'排版变换':'空白左栏为原续行；操作列共用单元格按原序保存；p21—22错位表分列记录'}
  (o/(b+'验收.json')).write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
  batchindex.append(rec);n+=1
assert len(batchindex)==38 and n==473
(o/'余部分批索引.json').write_text(json.dumps(batchindex,ensure_ascii=False,indent=2),encoding='utf-8')
qs={q:{'page':p,'group':names[p][g],'description':s} for (p,g),(q,s) in notes.items()}
qs['Q219']={'page':21,'group':'C∞ᵥ','description':'基底表D行重复Y三阶2b/2a对，并列出W一阶2b/2a对；不可约阶数与下标范围待核，原样保留。'}
(o/'新增疑点.json').write_text(json.dumps(qs,ensure_ascii=False,indent=2),encoding='utf-8')
target=r/'中文版本/第五章 张量与对称性/5.2 主要点群的特征标表与基底.md';snap=o/'B435前分批稿.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
head=re.sub(r'<!-- B434结束：[\s\S]*?-->\s*$','',snap.read_text(encoding='utf-8')).rstrip()
head=head.replace('B434已翻译并对照PDF p1的说明及完整目录。p2—22的特征标表、基底及非零分量表尚未译校；本文件为分批稿。','B434—B472已完成全22页说明、目录及38个点群块的本轮翻译和原页对照。数学显示及整节排版验收另见管理记录；原式疑点保留。')
head=re.sub(r'> \*\*阅读导引（译者编写，暂定）：\*\*[^\n]+','> **阅读导引（译者编写）：** 先按首页V/D/Y/W定义及适用过程区分表格用途，再依原目录查点群。每个点群块依次保留特征标、基底分类和原有分量关系。p18—20的高阶基底“分配项”并未被作者全部纳入分量关系；p21—22的错位特征标表按列独立记录，不擅自确定跨列对应。Q209—Q220为未决疑点，不据译校完成状态将所有表项视为已获独立物理认证。',head)
intro='\n\n## 查表格式说明（译者）\n\n以下按原页及点群次序列示。表头中的“原表左栏”“操作／特征标”等为阅读辅助；操作共用原表单元格时，其数值依原表头顺序列出。基底长行按逗号拆成可换行的数学片段，原续行的左栏仍留空；空白、显式零及未列出分别保留。原分量等式及重复项不合并。D、Y、W右上括号数字为不可约角动量阶数。原表基底列的可见垂直位置也予以保留，不能仅据排版位置认证其表示归属；p18 Tₕ及p21—22的错位另见Q218，后两页按分列记录处理。所有表格与公式均为可编辑文字。\n\n'
target.write_text(head+intro+'\n\n'.join((o/(b['批次']+'-本批译文.md')).read_text(encoding='utf-8').strip() for b in batchindex)+'\n',encoding='utf-8')
print('B435—B472，38点群块、76原表已转写；等待排版复核。')

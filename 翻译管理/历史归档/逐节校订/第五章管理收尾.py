from pathlib import Path
import re,csv,io,json,hashlib
from urllib.parse import quote,unquote
import pdfplumber
r=Path(__file__).resolve().parents[2];o=r/'翻译管理/校订记录/第五章收尾';d=r/'中文版本/第五章 张量与对称性'
titles={s:next(d.glob(s+' *.md')).stem for s in ['5.1','5.2','5.3','5.4','5.5','5.6']}
def link(s,prefix=''):return f'[{titles[s]}]({prefix}{quote(titles[s]+".md",safe="/（）")})'
guides={
'5.3':'先确认前两指标互换条件及三个取向角，再按c/a/b轴组查81条完整分量式。Z指向基板内部；跨页式已拼接，Q221—Q222保留。',
'5.4':'先辨指标数、不可约角动量阶数与星号，再查1—4指标基底，最后读奇偶性附录。含19张原表图；p15无正文；Q223—Q224保留。',
'5.5':'先读行列式因子及轴矢量，再查以D元素和欧拉角表示的0—4阶矩阵。15张原表图按列分块保留；Q225—Q227保留。',
'5.6':'先核欧拉角矩阵，再按A—D及1—9列组查36个和频张量变换表块。两边都用χ；不自行代入5.3的表面角偏移。Q228保留。'}
pages={'5.3':16,'5.4':15,'5.5':13,'5.6':37}
batchranges={'5.3':'B473—B500','5.4':'B501—B514','5.5':'B515—B527','5.6':'B528—B564'}
for s in guides:
 p=d/(titles[s]+'.md');t=p.read_text(encoding='utf-8')
 if s=='5.3':
  t=t.replace('阅读导引（译者编写，暂定）','阅读导引（译者编写）').replace('参考排版验收另见管理记录。','本轮中文图式版完成；参考排版验收见管理记录。')
  t=t.replace('每条标明原PDF页码；跨页式已在同一图中顺序拼接。','每条标明原PDF页码；跨页式已在同一图中顺序拼接。分组检索序号由译者添加，不是底本式号。')
 else:
  t=t.replace('\n\n> **阅读导引',f'\n\n本轮状态（2026-10-21）：全{pages[s]}页中文图式版完成，批次{batchranges[s]}。\n\n> **阅读导引',1)
 p.write_text(t,encoding='utf-8')
# Add the same numbering clarification to the first new batch snapshot.
p=r/'翻译管理/校订记录/5.3/B474-本批译文.md';t=p.read_text(encoding='utf-8').replace('每条标明原PDF页码；跨页式已在同一图中顺序拼接。','每条标明原PDF页码；跨页式已在同一图中顺序拼接。分组检索序号由译者添加，不是底本式号。');p.write_text(t,encoding='utf-8')
questions={
'Q223':('5.4 p1，星号与变换矩阵说明','余因子矩阵/伴随矩阵及转置的措辞需区分；“酉矩阵故行列式±1”不能脱离实正交变换语境。译文保留原句并限明语境。'),
'Q224':('5.4 p2，双指标基底及第一张系数表','原D零分量重复yz−zy组合；候选xy−yx仅在译者注给出。表中D^(2)_2b行Dyy列为正1/√2，与正文差组合不一致；两处均保留原值。'),
'Q225':('5.5 p1，镜映与旋转的对应','前段xy面镜映对应绕x轴180°加反演，后文又对应绕z轴180°。依通常三维坐标前者候选应为yz面；保留原xy及角度式，候选未采用。'),
'Q226':('5.5 p2，余因子推导第2点','原文对余因子、逆矩阵转置和ε因子的叙述不完全一致，末句未写ε。保留原句和后续结论，不自行修推导。'),
'Q227':('5.5 p4，3阶第1部分表等','底本有方框及括号/排字异常，例如T′^(3)_2b行T^(3)_2a列式首。保真图保留方框，未凭相邻元补号；此项不是可辨读系数的证明。'),
'Q228':('5.6 p3 A-2表及p4 A-3表','A-2的zzx行bab列第二行式首、A-3的xxx行aab列含方框。原图保留，未猜填字符。')}
p=r/'翻译管理/疑难与勘误.md';t=p.read_text(encoding='utf-8')
for q,(loc,desc) in questions.items():
 assert not re.search(r'^## '+q+r'\b',t,re.M),q
 t+=f'\n\n## {q}｜{loc}\n\n{desc}\n\n状态：保留原文、待核验；未采用原文修正。正文有就地说明。来源：第五章B501—B564。\n'
p.write_text(t,encoding='utf-8')
p=r/'中文版本/附件/原文勘误表.md';t=p.read_text(encoding='utf-8');t+='\n\n## 第五章完成时的待核索引（2026-10-21）\n\n以下为未采用修正的疑点索引，不分配已采用勘误E编号。所有原式及缺字方框依底本保留；既有已确认勘误继续保留在附件前部。\n\n| 小节 | 问题号 | 范围 |\n|---|---|---|\n| 5.1 | Q198—Q208 | 张量基底、角度及符号约定 |\n| 5.2 | Q209—Q220 | 特征标、基底及分列关系 |\n| 5.3 | Q221—Q222 | abc/xyz及内部角几何 |\n| 5.4 | Q223—Q224 | 星号矩阵说明、双指标组合及系数符号 |\n| 5.5 | Q225—Q227 | 镜映轴、余因子推导和缺字符号 |\n| 5.6 | Q228 | 原表缺字符号 |\n\n详见[第五章阅读导航](../第五章%20张量与对称性/阅读导航.md)及[疑难与勘误](../../翻译管理/疑难与勘误.md)。本轮无新增已采用原文修正。\n';p.write_text(t,encoding='utf-8')
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8');t=t.replace('**本章导读（5.1—5.2已核，其余暂定）：** 5.1建立张量基底、对称性约束与坐标变换的基础；5.2按点群查阅特征标、基底归属及非零分量，5.3—5.6仍待译校。','**本章导读：** 全章6节110页已完成本轮中文译校。5.1建立张量与不可约基底框架，5.2供点群查阅；5.3给出取向依赖的和频分量，5.4构造基底，5.5、5.6分别给出基底和笛卡尔分量的变换矩阵。5.3后段及5.4—5.6的大型公式表保留为清晰图式，未全部转为可编辑LaTeX；Q198—Q228仍待核。各部分概括见[第五章阅读导航](中文版本/第五章%20张量与对称性/阅读导航.md)。')
lines=t.splitlines()
for i,line in enumerate(lines):
 for s in guides:
  if line.startswith('- '+s+' ') or line.startswith('- ['+s+' '):lines[i]='- '+link(s,'中文版本/第五章%20张量与对称性/')+f'（全{pages[s]}页，本轮完成）：'+guides[s]
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
p=d/'阅读导航.md';t=p.read_text(encoding='utf-8');a=t.index('## 5.2及后续小节');t=t[:a]
t=t.replace('本章5.1—5.2已完成本轮译校及排版；5.3已完成p1/16，5.4—5.6尚未开始，全章尚未完成。','全章6节110页已完成本轮中文译校与显示检查（B423—B564）。5.3后段及5.4—5.6的大型公式表采用保真图式；未全部转成可编辑LaTeX。Q198—Q228保留待核，完成状态不代表所有原公式已独立验证。')
t+='## 5.2 主要点群的特征标表与基底\n\n'+link('5.2')+'。全22页，B434—B472。先确认V/D/Y/W，再按38个点群块查特征标、基底和β/γ关系；p18—20保留高阶分配项限制，p21—22的错位表按列记录。Q209—Q220待核。\n\n'
detail={
'5.3':['p1第1—3部分：适用条件、坐标与三个取向角；保留xyz与ab面疑点。','p2第4部分引言：分子非零分量及前两指标相等关系。','p2—6：沿c轴的27条空间分量式；p6上端接续上一页末式。','p6—10：沿a轴的27条空间分量式。','p10—16：第三组27条分量式，译者按b轴振动补设检索标题；原页没有此标题。'],
'5.4':['p1要点：不可约基底、n/m/a/b记号与星号。','p2：单、双指标张量的基底公式和三张系数表。','p3—4：三指标张量的四个混合子组；末段解释重复表示编号。','p5—12：四指标张量第1-1至4-2组的八张表。','p13—14附录：极/轴矢量、镜面选择及奇偶性；p15无正文。'],
'5.5':['p1—2：旋转、反演、行列式因子及轴矢量矩阵。','p3：0、1、2阶基底的变换及ε条件。','p4—7：3、4阶矩阵及压缩系数记号；跨页按列分块。','p8：欧拉角形式的1、2阶矩阵。','p9—10：3阶欧拉角矩阵；p11—13：4阶欧拉角矩阵。'],
'5.6':['p1：D矩阵和三角倍角与幂的转换关系；图外附中文查表目录。','p2—10：和频张量A-1—A-9，每块7行3列。','p11—19：B-1—B-9，每块7行3列。','p20—28：C-1—C-9，每块7行3列。','p29—37：D-1—D-9，每块6行3列；三个下标互异。']}
for s in guides:
 t+=f'## {titles[s]}\n\n'+link(s)+f'。全{pages[s]}页，{batchranges[s]}。'+guides[s]+'\n\n'+'\n'.join(f'{i+1}. {x}' for i,x in enumerate(detail[s]))+'\n\n'
t+='## 跨节查阅\n\n次元数、階数沿5.1定义区分为指标数和不可约角动量阶数；不据汉语“阶”推断电场响应阶数。5.3的β/χ约定与5.6两边都用χ的约定分别保留。5.4—5.5的星号及ε还涉及反演、镜映和旋转反射；5.6限定为所列欧拉角的坐标旋转。先核矩阵方向和法线，再连接不同小节的结果。\n';p.write_text(t,encoding='utf-8')
# These remain UTF-8 text registries, preserving the established 12/17-column
# schemas rather than redesigning them as an Excel workbook.
p=r/'翻译管理/章节清单.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;rows=list(reader);oldother=[dict(x) for x in rows if x['编号'] not in guides]
meta=json.loads((o/'底本及页面.json').read_text(encoding='utf-8'))
for row in rows:
 s=row['编号']
 if s in guides:
  m=next(x for x in meta if x['节']==s);assert m['sha256']==row['原文SHA256']
  row.update({'暂定中文标题':titles[s].split(' ',1)[1],'现有译文路径':(d/(titles[s]+'.md')).relative_to(r).as_posix(),'状态':f'本轮完成：全{pages[s]}页；中文正文及保真图式，{batchranges[s]}','映射核验':'原页全覆盖；全量资源/显示检查，原图式不等于独立数学验证','导读状态':'本轮导读已按正文更新','导读草案':guides[s],'公式图表范围':{'5.3':'81条完整分量式图，跨页拼接；首页及分子关系为LaTeX','5.4':'19张原表图及正文基底公式；p15无正文','5.5':'15张原矩阵表图及说明式','5.6':'36张原表图，729个系数位置；p1矩阵与恒等式为LaTeX'}[s]})
assert oldother==[x for x in rows if x['编号'] not in guides]
def write_tsv(p,fields,rows):
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_bytes(s.getvalue().encode('utf-8'))
write_tsv(p,fields,rows)
p=r/'翻译管理/术语表.tsv';reader=csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t');fields=reader.fieldnames;terms=list(reader);original=[dict(x) for x in terms]
for id,jp,en,zh,loc,definition in [('T099','パリティー','parity','奇偶性','5.4 p13—14 / B513—B514','基底在反演、镜映和旋转反射下的符号性质；星号按本节镜面选择解释。'),('T100','pseudo rotation（底本英文）','improper rotation（辅助对应）','非正常旋转','5.5 p1 / B515','原文列镜映、旋转反射等，行列式为−1；保留原英文，不与绕轴正旋转混同。'),('T101','擬スカラー','pseudoscalar','赝标量','5.5 p2 / B516','按原文奇指标数的0阶基底在特定操作下变号，不据此泛指所有张量。')]:
 assert not any(x['术语编号']==id for x in terms)
 row={f:'' for f in fields};row.update({'术语编号':id,'日语候选':jp,'英语辅助释义':en,'推荐中文候选':zh,'定义与适用语境':definition,'原文位置':loc,'依据':'本轮原页语境对照；中文暂用，非新增用户确认','状态':'原词与语境已核；中文暂用','文本定位状态':'原页已对照','译名决定状态':'译者暂用；非用户新确认','英语来源说明':'T100的pseudo rotation为底本英文；其他英语为译者辅助对应'});terms.append(row)
assert terms[:len(original)]==original;write_tsv(p,fields,terms)
p=r/'翻译管理/符号与约定.md';t=p.read_text(encoding='utf-8');t+='\n\n## 第五章后段跨节约定（B474—B564）\n\n- 5.3：β分子、χ空间分量；首两指标互换是适用条件。原XYZ大写，xyz混称依Q221保留；Z向内。c/a/b三组各27条展开式；b组检索标题为译者所加。\n- 5.4：次元数译指标数，階数译不可约角动量阶数；上标(n)与下标m不混同。星号不是复共轭；在含反演/镜映/旋转反射时区分极性与轴性。xz纳入σv为本稿选择。末表o为指标数。\n- 5.5：D为坐标矢量矩阵，另一字形D对应角动量矩阵；正文用数学斜体D加以区分并有就地说明。ε=det(D)。压缩记号(AB/cd)等不是分量相除。跨页矩阵按列分块，而非依次相乘。\n- 5.6：D=R_Z(χ)R_y(θ)R_z(φ)，行xyz、列abc；χ同时用于分子及空间张量，不自动替换为β、不额外加数密度。sin3θ与sin³θ严格区分。旋转矩阵本身不授权代入5.3的表面角偏移。\n\n图式保留原字符、星号、方框、上下标及行列顺序，不能把图像清晰或语法通过视为原式正确。Q221—Q228未采用修正。\n';p.write_text(t,encoding='utf-8')
(o/'图式版执行说明.md').write_text('# 第五章图式版执行说明\n\n2026-10-21。用户本轮授权完成第五章；保留原有小批次验收，新增B474—B564。\n\n本轮排版选择：中文正文完整翻译，5.3后段逐条保留完整公式图，5.4—5.6的大型矩阵按原表保留清晰图式。共151张正文资源；p1矢量矩阵及说明公式等仍用LaTeX。图内日语行标有中文对照。该选择利用既有“图表优先使用清晰原图”的规范，避免有损文本提取把函数幂、三倍角和表格行列混淆。它是本轮执行选择，不是用户逐项确认了所有数学读法。\n\n已完成的是中文图式版，未完成“所有公式均可编辑/可搜索的LaTeX版”；后者若需要，应另做逐式转录及对照，不能宣称本轮已经做到。\n\n全量检查资源、原页范围、分量数和显示；原页81页均已查看，代表排版截图已目视核对。原表正确性、缺字符号的读法及Q198—Q228仍需专业核验。\n',encoding='utf-8')
print('正文说明、导航、术语及问题索引更新完成；等待最终渲染与验收签结。')

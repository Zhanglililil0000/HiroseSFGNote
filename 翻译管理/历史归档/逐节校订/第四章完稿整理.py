from pathlib import Path
import json,re,hashlib,csv,io
from urllib.parse import quote
root=Path(__file__).resolve().parents[2];base=root/'翻译管理/校订记录';chapter=root/'中文版本/第四章 单层膜与多层膜的和频'
spec={
'4.7':(24,365,384,'CH₂、平面HCCH及扭转HCCH的和频张量','比较位阻与三套坐标，按构型、模式及方位角读12张取向表，再查具体取向和附录四组108分量。','Q180—Q188'),
'4.8':(38,385,401,'氢化金刚石表面CH的和频张量','从CH键张量叠加进入分子系，分别处理HCCH两构型、CH₂六类取向，再转至实验室系；附录108分量齐全，6d原稿未着手已说明。','Q189—Q193'),
'4.9':(26,402,415,'氢化金刚石表面CH的和频张量（要点）','保留先第6部分、再第3—5部分的原顺序；先查实验室响应，再回查分子及表面张量，最后查附录108分量。','Q194'),
'4.10':(8,416,420,'CH₂基团及HCCH基团的欧拉角','以三幅原图定义坐标，用单位向量、二面角处理纯扭转、纯倾斜及组合取向，给出CH键系到分子系的Eu-1—Eu-11关系。','Q195—Q197'),
'4.11':(2,421,422,'表面的旋转','从向外法线约定出发，按八类偏振列出表面系到实验室系的全部27个分量。','无新增原文疑点')}
def append(p,h,t):
 s=p.read_text(encoding='utf-8') if p.exists() else ''
 if h not in s:p.write_text(s+'\n\n'+h+'\n\n'+t+'\n',encoding='utf-8')
# 精确说明保留字形；此处属于注释措辞校准，不是改原公式。
for sec,n in [('4.8',387)]:
 p=base/sec/f'B{n}-本批译文.md';s=p.read_text(encoding='utf-8').replace('cos2ϖ、sin3ϖ','cos2v、sin3v');p.write_text(s,encoding='utf-8')
for sec,n,text in [('4.8',393,'> **Q191续：** 本组条件中原写“cosτ inθ”等缺少明确运算关系的文字，按原字形保留，不直接补作除以sinθ。'),('4.8',394,'> **Q191续：** 原角度条件中的拉丁c以及其他未定义原写保留；不因本节主角记χ而自动改字母。'),('4.10',418,'> **Q195续：** 式(Eu-3b)中“cos t”的拉丁t原写保留；不直接视为τ的正常转写。')]:
 p=base/sec/f'B{n}-本批译文.md';s=p.read_text(encoding='utf-8')
 if text not in s:p.write_text(s+'\n'+text+'\n',encoding='utf-8')
for sec,(pages,start,end,title,guide,issues) in spec.items():
 if sec=='4.7':continue
 files=[base/sec/f'B{n}-本批译文.md' for n in range(start,end+1)]
 first=files[0].read_text(encoding='utf-8')
 status=f'> 本轮状态：全{pages}页原页对照、译校及参考排版完成；{issues}保留待核。'
 if status not in first:
  at=first.index('\n\n');first=first[:at]+'\n\n'+status+first[at:];files[0].write_text(first,encoding='utf-8')
 target=next(chapter.glob(sec+' *.md'));target.write_text('\n\n'.join(p.read_text(encoding='utf-8') for p in files),encoding='utf-8')
# 疑难条目与正文逐项互链，候选尚未采纳，不混入已确认勘误。
for q in range(189,198):
 notes=[]
 for sec,(pages,start,end,title,guide,issues) in spec.items():
  if sec=='4.7':continue
  for n in range(start,end+1):
   for line in (base/sec/f'B{n}-本批译文.md').read_text(encoding='utf-8').splitlines():
    if line.startswith('>') and f'Q{q}' in line:notes.append(f'来源：{sec} / B{n}。\n\n'+line)
 append(root/'翻译管理/疑难与勘误.md',f'## Q{q}｜第四章后段原稿疑点或范围说明','状态：原文保留，未采用候选修正。\n\n'+'\n\n'.join(notes))
# 本轮未更改术语规范；局部角度、坐标与字形例外分别记录。
append(root/'翻译管理/符号与约定.md','## 第四章后段跨稿约定（B370—B422）','4.8、4.9第2部分z轴向内；4.10、4.11明定向外，保留各稿原约定。χ既用作三阶张量分量记号，也表示旋转角，按指标区分。CH键系使用希腊ξ、η、ζ，不能替成拉丁x、h、z。τ在HCCH构型、分子面与表面及两CCH面二面角等处有局部定义；引用时必须附所属部分。函数平方/立方和倍角/三倍角按原字形区分。none与显式0分列，不用缺项推断零值。')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
 sec=row['编号']
 if sec not in spec:continue
 pages,start,end,title,guide,issues=spec[sec]
 if sec=='4.7':continue
 row.update({'中文拟题':title} if '中文拟题' in row else {})
 row['状态']=f'本轮全{pages}页原页对照、译校及参考排版完成；'+issues
 row['映射核验']=f'B{start}—B{end}，正文及原有附录完整覆盖'
 row['公式图表范围']={'4.8':'675个χ单分量左式（含附录108式）；951数学片段；原结构图齐备','4.9':'386个χ单分量左式（含附录108式）；605数学片段；原结构图齐备','4.10':'三幅原坐标图、全部单位向量及Eu-1—Eu-11（含子号）；161数学片段','4.11':'八类偏振全部27分量；34数学片段'}[sec]
 row['导读状态']='已按全节更新节首、序言和第四章导航';row['导读草案']=guide
with p.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8')
for sec,(pages,start,end,title,guide,issues) in spec.items():
 pat=r'(?m)^- \['+re.escape(sec)+r' [^\n]*$'
 def replace(m):
  link=re.search(r'\]\(([^)]+)\)',m[0]);assert link,m[0]
  return f'- [{sec} {title}]({link[1]})（全{pages}页已译校）：{guide}'
 s=re.sub(pat,replace,s)
p.write_text(s,encoding='utf-8')
p=chapter/'阅读导航.md';s=p.read_text(encoding='utf-8');s=s[:s.index('## 4.7 ')]
s=s.replace('# 第四章阅读导航','# 第四章阅读导航\n\n本章4.1—4.11共267页已完成本轮翻译、原页对照和分批排版检查。原文理论疑点仍在各处及管理记录中保留，译校完成不表示已全部推导证实。',1)
for sec,(pages,start,end,title,guide,issues) in spec.items():
 target=next(chapter.glob(sec+' *.md'));s+=f'## {sec} {title}\n\n[进入{sec}]({quote(target.name)})。全{pages}页按B{start}—B{end}完成本轮译校。\n\n{guide}\n\n{issues}。各部分实际页界及详细概括见节首。\n\n'
s+='## 接下来\n\n可进入第五章；第四章若开展专题复核，优先核定法线/角度约定及未决公式疑点，采用修正时按既定规则就地说明并收入勘误附件。\n';p.write_text(s,encoding='utf-8')
append(root/'中文版本/附件/原文勘误表.md','## 第四章后段完成时的疑点索引（B370—B422）','以下为待核索引，不是已采用修正。本轮无新增已采用的原文勘误。旧译主题、函数幂、希腊下标、根号及省略项的修复属于译文校订。\n\n| 原稿 | 状态 | 定位与范围 |\n|---|---|---|\n| 4.7 | Q180—Q188待核 | 局部坐标、角度与±号、表3a-3差异、附录括号和未定义字母 |\n| 4.8 | Q189—Q193待核 | 坐标重复疑点、分母37、取向条件、未定义字母、附录括号；6d原稿“未着手”保留 |\n| 4.9 | Q194待核 | 独立要点版的同类原写及版本差异，保留先6后3的顺序 |\n| 4.10 | Q195—Q197待核 | 三角恒等式、排列条件、HCH角命名和点/叉积记号 |\n| 4.11 | 无新增 | 八类偏振27分量按原式保留 |\n\n具体候选和页码见各译文就地注及《疑难与勘误》。已确认的既有勘误继续保留在本附件前部。')
desc='第四章4.1—4.11共267个PDF页均已完成本轮译校。本轮从4.7 p6继续，完成余下93页，分B370—B422共53批；4.8、4.9分别保留自身数学行和版本组织，附录各108分量齐全；4.10恢复三幅原图，4.11完整27分量。原稿未完成的4.8 §6d已如实说明。新疑点保留、候选未采纳；格式与覆盖检查不代替独立物理证明。'
append(root/'翻译管理/分批执行与质量控制.md','## 第四章本轮完成（2026-10-21）',desc+'\n\n新增字形级提取检查：主字号字符很少的短等式也必须入索引，避免χZZZ=βccc或零值被密度筛选漏掉；矢量绘制的根号单独识别并视觉复核。原编号排在式旁，不与右侧数学表达式连写；跨页续项不拆断。')
append(root/'翻译管理/执行方案.md','## 第四章阶段成果（2026-10-21）',desc)
for sec,(pages,start,end,title,guide,issues) in spec.items():
 if sec=='4.7':continue
 out=base/sec
 (out/'局部约定卡.md').write_text(f'# {sec}局部约定\n\n{guide}\n\n'+issues+'保留原写。CH键系ξ、η、ζ与表面系xyz分别辨认；角度与函数幂按本稿原字形保留；none不等于漏列分量的零值。\n',encoding='utf-8')
 (out/'术语卡.md').write_text('# 术语卡\n\n沿用已确认术语：和频过程；χ⁽²⁾二阶非线性极化率；β一阶超极化率。CH₂后仰指沿±y方向倒伏；侧倾指在xz面内沿±x方向倾斜；扭转HCCH（C₂）与平面HCCH（C₂ᵥ）不是对称/反对称振动模式的同义词。\n',encoding='utf-8')
 (out/'结构与分批计划.md').write_text(f'# {sec}完成记录\n\n全{pages}页按B{start}—B{end}完成。{guide}\n\n各批保留源页行坐标或人工向量对照记录、源文件校验值、译文和参考预览。'+issues+'。\n',encoding='utf-8')
p=root/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text('# 当前进度与续接\n\n## 当前有效状态：第四章完成（2026-10-21）\n\n'+desc+'\n\n序言、第四章阅读导航、章节清单、各批覆盖与验收、符号约定及勘误附件已更新。下一阶段为第五章；本轮未启动第五章。\n\n以下为历史记录，以本条状态为准。\n\n'+s.split('\n',1)[1],encoding='utf-8')
(root/'翻译管理/第四章完成复核.md').write_text('# 第四章完成复核\n\n2026-10-21。\n\n'+desc+'\n\n| 节 | PDF页数 | 本轮批次 | 完成范围 |\n|---|---:|---|---|\n'+'\n'.join(f'| {r["编号"]} | {r["PDF页数"] if "PDF页数" in r else ""} | '+(f'B{spec[r["编号"]][1]}—B{spec[r["编号"]][2]}' if r['编号'] in spec else '见既有验收')+' | '+r['状态']+' |' for r in rows if r['编号'].startswith('4.'))+'\n\n验收含：源页覆盖、正文与附录左式数量、函数幂与根号、原图、数学语法、参考渲染、相对链接及管理状态。未将原文疑点登记为已解决。\n',encoding='utf-8')
print(desc)

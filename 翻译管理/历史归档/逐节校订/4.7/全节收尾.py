from pathlib import Path
import json,re,hashlib,csv,io
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.7 CH₂、平面HCCH及扭转HCCH的和频张量.md'
s=target.read_text(encoding='utf-8')
s=re.sub(r'B365—B369完成原题.*?旧文件路径', 'B365—B384已完成全24页正文及附录A的原页对照与译校；原文疑点Q180—Q188保留待核，未采用候选修正。旧文件路径',s,count=1)
start=s.index('## 阅读引导');end=s.index('## 1. 绪论')
s=s[:start]+'''## 阅读引导

- 第1部分（p1—2）：比较金刚石C(100)表面的单氢化、双氢化模型，说明位阻引起的倾斜与扭转。
- 第2部分（p2）：定义分子、表面及实验室坐标；区分欧拉角与面内取向角。
- 第3部分（p3—11）：按C₂ᵥ/C₂、对称/反对称伸缩以及特殊/一般方位角查阅12张完整张量表。原共享角度列的正负号保留。
- 第4部分（p11—13）：讨论平面与扭转HCCH在具体取向下的表面系张量。τ的局部定义差异见Q183。
- 第5部分（p13—16）：依次处理CH₂绕轴扭转、后仰以及先扭转再后仰；原编号5a、5b、5d保留，函数幂与倍角分开辨认。
- 附录A（p16—24）：完整列出C₂ᵥ和C₂、两种伸缩模式的四组一般式，各27分量，共108个单分量等式；原未配对括号及未定义符号均就地注明。

'''+s[end:]
assert '旧译待核。 -->' not in s and '详细公式请参阅' not in s
target.write_text(s,encoding='utf-8')
renders=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert renders['math']==1212 and len(renders['results'])==20
assert all(not r['overs'] and r['width']==r['scrollWidth'] for r in renders['results'])
notes=[]
for n in range(370,385):
 p=out/f'B{n}-本批译文.md';t=p.read_text(encoding='utf-8');r=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'))
 r.update(status='本批原页对照、译校与参考排版完成',render=next(x for x in renders['results'] if x['batch']==f'B{n}'),translation_sha256=hashlib.sha256(t.encode()).hexdigest(),validation_limit='保留原式疑点；未声称已完成独立物理验证。')
 (out/f'B{n}验收.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\n2026-10-21。原页'+','.join(map(str,r['pages']))+'。本批完整译文、公式及覆盖记录见同目录同批文件。已对照原页图像并完成参考排版检查。原文疑点保留，未采用候选修正。\n',encoding='utf-8')
 notes.extend(l for l in t.splitlines() if l.startswith('>') and re.search(r'Q18[2-8]',l))
def append(p,h,t):
 old=p.read_text(encoding='utf-8')
 if h not in old:p.write_text(old+'\n\n'+h+'\n\n'+t+'\n',encoding='utf-8')
for q in range(182,189):
 selected=[l for l in notes if 'Q'+str(q) in l]
 append(root/'翻译管理/疑难与勘误.md',f'## Q{q}｜4.7原式保留项','状态：原文疑点未决；未采用候选修正。\n\n'+'\n\n'.join(selected))
desc='4.7全24页按B365—B384完成原页对照。正文第1—5部分及附录A完整覆盖，12张取向表、附录四组各27分量（108等式）齐全；补回原图及旧译省略的C₂附录54式。累计1212数学片段语法与参考排版检查通过。原文Q180—Q188待核，候选修正未采用；函数幂等旧译错误已按原页恢复。下一节4.8，共38页。'
for filename in ['局部约定卡.md','结构与分批计划.md']:append(out/filename,'## 全节完成（B365—B384）',desc)
append(root/'翻译管理/分批执行与质量控制.md','## 4.7全节完成（B365—B384）',desc)
append(root/'中文版本/附件/原文勘误表.md','## 4.7全节状态（B365—B384）','全24页译校完成。Q180—Q188为保留原式的未决疑点，详见正文对应位置和疑难记录；无新增已采用的原文修正。恢复旧译函数幂及补回附录公式属于译文校订，不计作原文勘误。')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for r in rows:
 if r['编号']=='4.7':r.update({'状态':'本轮全24页原页对照、译校与参考排版完成；Q180—Q188待核','映射核验':'B365—B384，正文1—5及附录A全覆盖','公式图表范围':'原图1幅、12张取向表、附录108个单分量等式；1212数学片段','导读状态':'已按全节更新','导读草案':'从金刚石表面位阻进入平面/扭转HCCH及CH₂，定义坐标，按模式与方位角查表，再查具体取向与附录一般式。'})
with p.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8');s=re.sub(r'(?m)^- \[4\.7 .*$',lambda m:m[0].split('（已译校至')[0]+'（全24页已译校）：从位阻与坐标进入平面/扭转HCCH和CH₂的取向张量，12张正文表及附录四组108分量完整覆盖；原文疑点就地标注。',s);p.write_text(s,encoding='utf-8')
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';s=p.read_text(encoding='utf-8');s+='\n\n## 4.7当前有效完成状态\n\n'+desc+'旧状态说明仅作为历史进度；以此全节状态为准。\n';p.write_text(s,encoding='utf-8')
p=root/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text('# 当前进度与续接\n\n## 当前有效状态：4.7全节完成（2026-10-21）\n\n'+desc+'\n\n用户本轮目标为完成第四章：4.8—4.11仍待继续，不能据4.7完成登记整章完成。\n\n以下为历史记录。\n\n'+s.split('\n',1)[1],encoding='utf-8')
(out/'全节验收.json').write_text(json.dumps({'date':'2026-10-21','pages':24,'batches':'B365—B384','appendix_components':108,'math_fragments':1212,'source_issues':'Q180—Q188','source_corrections_adopted':False,'translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf-8')
print(desc)

from 整节工具 import *
from collections import Counter
s=target.read_text(encoding='utf-8')
# 将导读置于原目录之后；仍保留原目录页码与勘核说明。
at=s.index('## 要点')
guide='''## 阅读导引

1. 要点（p1—4前部）：列CH、CH₂、CH₃的伸缩响应、质量因子、跃迁矩阵元、强度比，以及各基团的相对张量分量；先注意所采用的两项近似。
2. 第1部分（p4—14前部）：建立质量调整简正坐标，推导振动偶极矩，再分别以投影和矩阵变换求拉曼张量，最后连接和频张量。各处原符号、正负号及归一化差异须连同译者注阅读。
3. 第2部分（p14—16前部）：区分非简并与二重简并模式，说明l态加权及吸收/拉曼与单个和频张量分量的不同计数，列同位素质量及G数值。
4. 第3部分（p16—18前部）：以力常数、频率和红外相对强度检验相同局部键近似，说明模式混合的局限。
5. 第4部分（p18—22前部）：由拉曼不变量求强度与退偏比，再用参数表和实验数据讨论r的估计；原表数值和公式未必完全一致，疑点保留。
6. 附录1（p22—24前部）：谐振子、无量纲坐标、跃迁矩阵元与非谐耦合。
7. 附录2（p24—28前部）：依次区分实验室系、质心系、分子固定直角系、内坐标、对称坐标及简正坐标，并说明Eckart约束。
8. 附录3（p28—30前部）：G/F矩阵的动能、势能与特征值关系，以及内坐标元素和经验力场。
9. 附录4（p30—33）：表面作用使CH₃对称性降低时的模式混合、矩阵展开和L变换。

建议先确认局部坐标、模式、质量归一化及张量分量，再比较强度。全节译校完成不表示原文的定义冲突、公式和数据疑点已解决；Q122—Q137均有就地说明。

'''
s=s[:at]+guide+s[at:]; target.write_text(s,encoding='utf-8')
tags=re.findall(r'\\tag\{([^}]+)\}',s); counts=Counter(tags)
assert len(tags)==108 and len(counts)==107 and counts['1.9']==2
assert not any(ord(c)<32 and c not in '\n\r\t' for c in s)
assert '旧译待核' not in s and '\\begin{array}' not in s
rows=[]
for n in range(249,277):
    rec=json.loads((p/f'B{n}-覆盖.json').read_text(encoding='utf-8'))
    rows.extend(dict(tag=t,batch=f'B{n}',pages=rec['pages']) for t in rec['tags'])
(p/'全节公式编号索引.json').write_text(json.dumps(dict(occurrences=108,unique_labels=107,source_duplicate={'1.9':'PDF p6势能与p8极化投影，保留原号'},locations=rows),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(p/'全节公式编号索引.md').write_text('# 4.1公式编号索引\n\n共108处编号、107个不同标签。原文1.9在p6和p8重号，保留原号并以页码区分；引用1.19的差异见Q126。\n\n| 编号 | 批次 | 原文页 |\n|---|---|---|\n'+'\n'.join(f"| {r['tag']} | {r['batch']} | {r['pages']} |" for r in rows)+'\n',encoding='utf-8')
# 新问题按章节位置收录，正文候选均未采用。
q=root/'翻译管理/疑难与勘误.md'
issues=[]
for n in range(251,277):
    t=(p/f'B{n}-本批译文.md').read_text(encoding='utf-8')
    issues.extend(re.findall(r'^> \*\*译者注（原文疑点）：\*\* (.+)$',t,re.M))
q.write_text(q.read_text(encoding='utf-8')+'\n\n## 4.1全节后续疑点：Q123—Q137（待核验）\n\n'+ '\n\n'.join('- '+x for x in issues)+'\n\n以上候选均未采用。Q122—Q137正文各处原值保留；旧译漏译、误译和转录修复不列入原文修正条目。\n',encoding='utf-8')
card=p/'局部约定卡.md'; card.write_text(card.read_text(encoding='utf-8')+'''\n## 整节约定复核

- 键固定坐标为ξ、η、ζ，分子固定坐标为a、b、c；欧拉角按本节χ、θ、φ及规定转轴顺序，不能跨章默认。
- α作为夹角时与分子极化率张量区分；τ在要点称HCX角、后文称HCH角，原定义分别保留。r分量比与rCH坐标区分；附录3、4的μ是倒数质量，不能与偶极矩μ混读。
- 要点β₀和第1部分Latin b₀按局部原定义保留；β为一阶超极化率，对应二阶场响应，不能把张量乘积称作已平方的光强。
- η的星/加标记是相对基准；附录的矩阵Λ、E、L、G、F和第三章辐射L不同。附录4的t为几何系数，τ为角度。
- Q122—Q137保留待核。附录2和正文各归一化/根号/质量因子不强行统一；所有已采用的变更均为旧译修复、排版或目录定位说明，无原文公式修正采用。
''',encoding='utf-8')
coverage='''# 4.1 全节单元覆盖

| 单元 | 原文页 | 批次 |
|---|---|---|
| 目录、CH与CH₂对称要点 | 1—2 | B249—B250 |
| CH₂反对称、CH₃及相对分量表 | 2—4 | B251—B253 |
| 简正坐标与质量因子 | 4—6 | B254 |
| 振动偶极矩 | 6—7 | B255 |
| 拉曼张量与坐标图、投影法 | 7—9 | B256—B257 |
| CH₂矩阵法及CH₃完整变换 | 9—13 | B258—B260 |
| 和频张量 | 13—14 | B261 |
| 矩阵元、简并权重、质量数值 | 14—16 | B262—B263 |
| 力常数与红外近似检验 | 16—18 | B264—B265 |
| 拉曼检验、参数及实验表 | 18—22 | B266—B269 |
| 附录1 | 22—24 | B270 |
| 附录2 A—F | 24—28 | B271—B273 |
| 附录3 | 28—30 | B274 |
| 附录4及L矩阵 | 30—33 | B275—B276 |

页码交叠表示同页衔接，并非重复翻译。原文108处编号全部覆盖，1.9重号按源保留。33页均已视觉对照；原目录附录4列p31，实际p30开始，正文保留原目录值并注明定位。
'''
(p/'全节单元覆盖.md').write_text(coverage,encoding='utf-8')
st=p/'结构与复用核验表.md'; st.write_text(st.read_text(encoding='utf-8')+'\n## 完成状态\n\nB251—B276已完成原先待核部分，包含全部正文与四附录。上表早期待核为历史状态，当前以全节单元覆盖及整节完成复核为准。\n',encoding='utf-8')
progress=root/'翻译管理/当前进度与续接.md'; t=progress.read_text(encoding='utf-8').replace('# 当前进度与续接\n','# 当前进度与续接\n\n## 当前有效状态：4.1全节译校完成（2026-10-20）\n\nB249—B276覆盖全33页、四正文部分及四附录，108处编号（107个不同标签，原1.9在p6/p8重号保留）。旧译近似误译、漏项、表格串列、希腊字母和矩阵/分式转录已修复；Q122—Q137保留原式并就地说明，无原文公式修正采用。最终检查见4.1整节完成复核。\n\n下一批B277：进入4.2，先核原文结构、原题与局部符号，不自动继承4.1的模式、坐标和归一化。以下为历史记录。\n',1); progress.write_text(t,encoding='utf-8')
nav=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md'; nav.write_text('''# 第四章阅读导航

## 4.1 CH、CH₂、CH₃基团CH伸缩振动的和频极化率

[进入4.1](4.1%20CH、CH₂、CH₃基团CH伸缩振动的和频极化率.md)。全部33页本轮译校完成，四正文部分与四附录齐备。

先读要点（p1—4），区分局部坐标和响应系数；第1部分（p4—14）由振动偶极矩及拉曼张量连接和频张量；第2部分（p14—16）处理简并权重与矩阵元；第3、4部分（p16—22）用频率、红外和拉曼强度检验近似。四附录（p22—33）补充谐振子、各类坐标、GF方法及CH₃对称性破缺。详细导读见节首。

原文108处编号，1.9重号以页码区分；Q122—Q137均保留原式待核，译校完成不表示其理论疑点已解决。

## 后续

4.2及其后各节仍待本轮逐页校订；下一批B277从4.2原题、结构和局部约定开始。
''',encoding='utf-8')
pre=root/'Preface序言.md'; lines=pre.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    if line.startswith('- [4.1 '):lines[i]=re.sub(r'（本轮校订中）.*', '（全33页本轮译校完成）：从局部键近似推导偶极矩、拉曼与和频张量，以频率和强度检验近似，并附谐振子、坐标、GF及对称性破缺分析；原文疑点就地说明。',line)
pre.write_text('\n'.join(lines)+'\n',encoding='utf-8')
listing=root/'翻译管理/章节清单.tsv'; lines=listing.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    if line.startswith('4.1\t'):
        c=line.split('\t'); c[7]='全33页本轮译校完成；Q122—Q137未决'; c[8]='B249—B276原页对照，四附录全覆盖'; c[9]='108处编号、107标签；原1.9重号保留；坐标图与数据表齐备'; c[10]='已根据全文更新'; c[11]='由CH局部近似推导振动偶极矩、拉曼及和频张量，检验频率与强度，附矩阵元、坐标及GF分析。'; lines[i]='\t'.join(c)
listing.write_text('\n'.join(lines)+'\n',encoding='utf-8')
plan=root/'翻译管理/全书调查/分批建议.tsv'; lines=plan.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    c=line.split('\t')
    if len(c)>1 and c[1]=='4.1':c[-1]='已全节完成；B249—B276按完整论述/公式/表组衔接'; lines[i]='\t'.join(c)
plan.write_text('\n'.join(lines)+'\n',encoding='utf-8')
err=root/'中文版本/附件/原文勘误表.md'; t=err.read_text(encoding='utf-8').replace('## 后续维护','## 4.1本轮状态（2026-10-20）\n\n全33页及四附录完成本轮译校。Q122—Q137均保留原式并就地列疑点，未采用候选修正，无新增已确认勘误。原1.9重号及目录页界差异有定位说明；旧译修复与原文勘误分开记录。\n\n## 后续维护',1); err.write_text(t,encoding='utf-8')
symbols=root/'翻译管理/符号与约定.md'; symbols.write_text(symbols.read_text(encoding='utf-8')+'\n\n## 4.1约定补充（2026-10-20）\n\n键系ξ/η/ζ与分子系a/b/c区分；α的张量/夹角语境、τ的局部角度、r与rCH、β₀与Latin b₀、偶极矩μ与倒数质量μ、Λ/E/L及几何系数t均按原段定义，不跨章统一。详情及Q122—Q137见4.1局部约定卡。\n',encoding='utf-8')
print('4.1覆盖与管理登记完成：108编号、107标签，原重号保留')

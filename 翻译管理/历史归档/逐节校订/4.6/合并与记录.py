from pathlib import Path
import re,json,hashlib,csv,io
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.6 CH₃基团的C₃ᵥ对称性破缺时的处理.md'
snap=out/'B362前旧译.md'
if not snap.exists():snap.write_text(target.read_text(encoding='utf-8'),encoding='utf-8')
texts=[(out/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(362,365)]
s='\n\n'.join(texts);target.write_text(s,encoding='utf-8')
sha=hashlib.sha256((root/'日语原版/Chapter4/chap4-6.pdf').read_bytes()).hexdigest()
for n,page,scope in [(362,1,'原题、全文导读、对称性降低与模式、S/GR/FR/GS矩阵及定义'),(363,2,'FS矩阵、GF五分量、本征值与D展开、谱带分裂及Td近似'),(364,3,'L矩阵、嵌套分式、归一化与模式极限及结论')]:
 text=texts[n-362]
 c={'batch':f'B{n}','date':'2026-10-21','pages':[page],'scope':scope,'source_sha256':sha,'source_images_visually_checked':True,'source_corrections_adopted':False,'display_blocks':len(re.findall(r'\$\$([\s\S]*?)\$\$',text))}
 (out/f'B{n}-覆盖.json').write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8')
 (out/f'B{n}.md').write_text(f'# B{n}校订记录\n\nPDF p{page}：{scope}。整页图与文本对照；恢复原√2系数、Td根号范围及L矩阵双层分母，分别保留c/C、S/s及转置记号。Q176—Q179按所在位置保留疑点，不采用原文修正。\n',encoding='utf-8')
(out/'局部约定卡.md').write_text('''# 4.6局部约定卡

- 本节为CH₃基团C₃ᵥ对称性破缺，讨论CH伸缩、简并解除和模式混合，不是CH₂弯曲振动。
- CH(1)为与表面相互作用的键；另两键为CH(2)、CH(3)。Qsym及Qdeg,a是面内模式，Qdeg,b为面外模式；原活性结论范围留疑。
- S为分子内对称坐标，R为内坐标，Q为简正坐标；Ls是从键伸缩坐标到S的变换，L是S=LQ中的矩阵，两者不同。
- 原GR/GS中μc和质量定义、p2公式的μC分别保留。μC=1/mC、μH=1/mH，τ为HCH角。矩阵下标S与本征值段小写s分别保留。
- K1/K2为CH伸缩力常数，K1=K2+ΔK；F/F′为原排斥参数，F′=−0.1F。s、t是几何系数，与转置上标t区别；md/Å单位按原保留。
- GS与FS用原tilde Ls记法；末页LL^t中的t明确表示转置。不跨章改乘法次序。
- Td角下s=√(2/3)、t=√(1/3)，原根号覆盖整个分数；矩阵非对角为√2而非2。
- D及λ修正项中斜线分母范围未确定，保留原斜线。L11²/L22²保留嵌套分式与原前因子；末尾Q1/Q2原缺斜线，候选倒数根式未采用。
- Q176—Q179均待核；翻译覆盖、转录与排版核验不等于原推导验证。
''',encoding='utf-8')
(out/'术语卡.md').write_text('''# 4.6局部术语卡

| 原文 | 中文 | 辨析 |
|---|---|---|
| C₃ᵥ対称が崩れた | C₃ᵥ对称性破缺 | 主题为甲基对称性降低 |
| 縮重が解ける | 简并解除 | 不译作弯曲振动 |
| モードパターン | 模式形态 | 与频率变化分开 |
| 分子内対称座標 | 分子内对称坐标 | S |
| 内部座標 | 内坐标 | R |
| 基準座標 | 简正坐标 | Q；旧译“正则坐标”改为振动分析常用表述 |
| 力の定数 | 力常数 | K1/K2与排斥参数F/F′分开 |
| バンドの分裂幅／シフト | 谱带分裂宽度／位移 | 频率ν而非本征值λ的量 |

分子和空间响应语境沿用既定术语；本节矩阵L、Ls不是菲涅尔因子。
''',encoding='utf-8')
(out/'全节单元覆盖.md').write_text('''# 4.6全节单元覆盖

原PDF共3页，实际页脚也为1、2、3；旧全书调查“页码非连续”的备注由本轮页图核验纠正，不当作原文勘误。

| 批次 | PDF页 | 内容 |
|---|---|---|
| B362 | 1 | 标题、三段物理说明；S定义、GR、质量倒数、FR、几何系数/参数/单位、GS |
| B363 | 2 | FS；GF五个非零分量；二维本征值与D²；ΔK定义；D²展开、D近似、三个λ；分裂与位移；Td几何与三个λ近似 |
| B364 | 3 | S=LQ、GFL=LΛ及LLᵗ=G；E定义；L12/L21；三条归一化关系；L11²/L22²双层分式；力常数极限；Q1/Q2及结论、交叉引用 |

五个矩阵组（S/Ls定义、GR、FR、GS、FS）全部保留，无独立插图。原公式无编号，不补造原号。原近似号、等号和未决斜线范围分别保留。
''',encoding='utf-8')
p=root/'翻译管理/疑难与勘误.md';issues=p.read_text(encoding='utf-8')
for q in range(176,180):
 if re.search(rf'^## Q{q}\b',issues,re.M):continue
 notes=[line for line in s.splitlines() if line.startswith('>') and f'Q{q}' in line]
 assert notes,q
 issues+=f'\n\n## Q{q}｜4.6原文疑点\n\n状态：待核验，原式或原述保留，候选未采用。\n\n'+'\n\n'.join(notes)+'\n'
p.write_text(issues,encoding='utf-8')
renderer=(out.parent/'4.5/检查排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.5','校订记录/4.6').replace("startsWith('4.5 ')","startsWith('4.6 ')")
(out/'检查排版.cjs').write_text(renderer,encoding='utf-8')
whole=(out.parent/'4.5/检查全节排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.5','校订记录/4.6').replace("startsWith('4.5 ')","startsWith('4.6 ')")
(out/'检查全节排版.cjs').write_text(whole,encoding='utf-8')
print('B362—B364已合并并生成覆盖、约定与疑难记录')

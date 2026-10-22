from 整节工具 import *
files=[out/f'B{n}-本批译文.md' for n in range(295,314)]
texts=[p.read_text(encoding='utf-8') for p in files]
head=texts[0].replace('B295—B296已对照PDF p1—3，完成原目录、引言及第1、2部分；第3部分起仍为旧译待核。','B295—B313已完成全26页本轮译校。原文疑点Q146—Q159保留并就地说明，未采用原文公式修正。')
guide='''## 阅读引导

- 第1、2部分（p1—3）：先明确欧拉角，再定义亚甲基内部旋转、外向法线倾斜角与面内取向角。第2部分式(2-1)与后文内部角的写法有差异，须结合就地说明阅读。
- 第3部分（p3—4）：由两个CH键的坐标变换建立分子张量，区分对称、反对称及面外振动，并给出四面体与sp²角的局部参数。
- 第4a部分（p4—10）：列出一般取向下三种振动模式的完整表面张量分量，以及原文附列的求和关系。
- 第4b部分（p10—13）：处理自由内部旋转或随机扭转角，不能等同于冻结在特定角度。
- 第4c部分（p13—16）：处理内部旋转冻结且两个H等价的情形，保留偶数角函数项；表内归一化与残缺项见原文疑点。
- 第5部分（p16—25）：在冻结旋转、两个CH等价的条件下，分别讨论面内随机、C₃ᵥ、C₄ᵥ/C₆ᵥ、Cₛ与C₂ᵥ取向表面。表面对称与分子振动对称应分别辨认。
- 第6、7部分（p25—26）：先由入射及反射场得到表面场与和频极化，再求反射、透射方向的和频电场；L因子的原文不一致处保留待核。

> **译者注（阅读边界）：** 本轮完成原文覆盖与译文转录核验；原文公式的未决疑点不代表已获物理验证。应用各表时须保留其角度、模式与平均条件。

'''
head=head.replace('## 引言',guide+'## 引言')
joined='\n\n'.join([head]+texts[1:])
target.write_text(joined,encoding='utf-8')
index=[]
for f,s in zip(files,texts):
    c=json.loads((out/(f.name[:4]+'-覆盖.json')).read_text(encoding='utf-8'))
    displays='\n'.join(re.findall(r'\$\$([\s\S]*?)\$\$',s))
    lhs=re.findall(r'(?:^|\n)((?:\\chi|c)_\{[xyz]{3}\})\s*&?=',displays)
    index.append({'batch':f.name[:4],'pages':c['pages'],'scope':c['scope'],'surface_tensor_left_sides':lhs,'numbered_labels':re.findall(r'\\tag\{([^}]+)\}',s)})
count=sum(len(x['surface_tensor_left_sides']) for x in index)
tags=re.findall(r'\\tag\{([^}]+)\}',joined)
assert count==356,(count,[(x['batch'],len(x['surface_tensor_left_sides']))for x in index])
assert len(tags)==30 and len(set(tags))==30,tags
assert '旧译待核' not in joined
(out/'全节公式与覆盖索引.json').write_text(json.dumps({'numbered':tags,'table_component_occurrences':count,'batches':index},ensure_ascii=False,indent=2),encoding='utf-8')
(out/'全节单元覆盖.md').write_text('# 4.3全节单元覆盖\n\n日期：2026-10-21。PDF全26页对照页图与文本。\n\n| 批次 | PDF页 | 内容 | 表内左式数 |\n|---|---|---|---|\n'+'\n'.join(f"| {x['batch']} | {','.join(map(str,x['pages']))} | {x['scope']} | {len(x['surface_tensor_left_sides'])} |" for x in index)+'\n\n共356个表内左式：4a、4b、4c各含三个27分量表（共243项）；5a共25项，5b共49项，5e共39项。5b中两处原Latin c计入表项，未擅自改χ。30个编号式：'+', '.join(tags)+'。\n',encoding='utf-8')
renderer=(out.parent/'4.2/检查全节排版.cjs').read_text(encoding='utf-8').replace('校订记录/4.2','校订记录/4.3').replace("startsWith('4.2 ')","startsWith('4.3 ')")
(out/'检查全节排版.cjs').write_text(renderer,encoding='utf-8')
print(json.dumps({'numbered':len(tags),'table_left_sides':count,'by_batch':[(x['batch'],len(x['surface_tensor_left_sides']))for x in index]},ensure_ascii=False))

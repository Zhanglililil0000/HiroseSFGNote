from pathlib import Path
import re,json,hashlib,csv,io
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.7 CH₂、平面HCCH及扭转HCCH的和频张量.md'
s=target.read_text(encoding='utf-8');prefix=s.split('<!-- B368止；')[0]
renders=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert renders['math']==435 and len(renders['results'])==4
assert all(not x['overs'] and x['width']==x['scrollWidth'] for x in renders['results'])
index=json.loads((out/'B367—B368公式与覆盖索引.json').read_text(encoding='utf-8'))
assert index['table_cells']==162 and index['zero_cells']==126 and index['nonzero_cells']==36
assert 'Q181' in prefix and '表(3b-1)及后续仍为旧译待核' in prefix
assert r'\sin 2\tau' not in (out/'B367-本批译文.md').read_text(encoding='utf-8')
assert r'\cos 2\tau' not in (out/'B367-本批译文.md').read_text(encoding='utf-8')
for c in index['batches']:
 n=int(c['batch'][1:]);t=(out/f'B{n}-本批译文.md').read_text(encoding='utf-8')
 assert len(re.findall(r'^\| \([ps]{3}\) \|',t,re.M))==81
 assert len(re.findall(r'^##### ',t,re.M))==3
 if n==368:
  expected={'XZX':[r'\beta_{caa}\cos\tau','0','0'],'ZXX':[r'\beta_{caa}\cos\tau','0','0'],'YZY':['0',r'\beta_{caa}\cos\tau',r'\beta_{caa}\cos\tau'],'ZYY':['0',r'\beta_{caa}\cos\tau',r'\beta_{caa}\cos\tau']}
  assert all(r['values']==expected.get(r['indices'],['0']*3) for r in c['components'])
 c.update({'status':'本批逐格译校与参考排版验收完成','render':next(x for x in renders['results'] if x['batch']==f'B{n}'),'translation_sha256':hashlib.sha256(t.encode()).hexdigest(),'scope_limit':'原表覆盖、转录及排版核验，不等于验证原文公式；共享列±对应关系未确认。'})
 (out/f'B{n}验收.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=root/'翻译管理/疑难与勘误.md';old=p.read_text(encoding='utf-8')
if not re.search(r'^## Q181\b',old,re.M):
 note=next(x for x in prefix.splitlines() if x.startswith('>') and 'Q181' in x)
 p.write_text(old+'\n\n## Q181｜4.7表(3a-1)的共享角度列与符号\n\n状态：原列、±及同号表项保留，未采用原文修正。\n\n'+note+'\n',encoding='utf-8')
for name,text in [('局部约定卡.md','## B367—B368补充\n\n第3部分χ表示表面系到实验室系绕z的旋转。表(3a-1)/(3a-2)分别对称/反对称伸缩，原三个列为0°/180°共享、90°、−90°。τ的sin²/cos²是函数幂，非倍角；原±映射未明，原ZZX在±90°两列同正号保留见Q181。每表27行、81单元，表(3a-2)仅六个非零。'),('结构与分批计划.md','## B367—B368阶段完成\n\np3引言及表(3a-1)、p4表(3a-2)已逐格核对，共54分量行、162角度单元；按原角度列拆窄表，保留全部126个零值及36个非零值。Q181待核。下一批B369：p5扭转C₂对称/反对称表(3b-1)/(3b-2)，先核分子分量、角度交换与原none项。')]:
 p=out/name;old=p.read_text(encoding='utf-8')
 if text.split('\n')[0] not in old:p.write_text(old+'\n\n'+text+'\n',encoding='utf-8')
p=root/'翻译管理/当前进度与续接.md';old=p.read_text(encoding='utf-8');mark='## 当前有效状态：B367—B368完成4.7表(3a-1)/(3a-2)（2026-10-21）'
if mark not in old:p.write_text('# 当前进度与续接\n\n'+mark+'\n\n累计已核p1—4：原题、原图、第1/2部分、第3部分引言及倾斜C₂ᵥ对称/反对称伸缩两张完整表。新增54分量行×3列=162单元，126零、36非零；sin²τ/cos²τ按原页恢复。Q181保留原共享列±与ZZX同号，未采用原文修正。当前四批435数学片段排版通过；表3b-1起仍为旧译待核。\n\n下一批B369：PDF p5扭转C₂分子的表(3b-1)/(3b-2)，核β分量、角度列及none项。以下为历史记录。\n\n'+old.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for r in rows:
 if r['编号']=='4.7':r.update({'状态':'本轮校订中：B365—B368完成p1—4；表3b-1起旧译待核','映射核验':'第1/2部分及p3—4表3a-1/3a-2逐格核对','公式图表范围':'原图1幅及54分量行×3角度列=162单元已核，126零/36非零','导读状态':'已更新至第3部分前两表；后续随进度补充','导读草案':'先比较表面模型、定义坐标，再按对称/反对称模式与角度列查看倾斜C₂ᵥ完整表；扭转C₂及后续取向表待核。'})
with p.open('w',encoding='utf-8',newline='') as h:
 w=csv.DictWriter(h,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';old=p.read_text(encoding='utf-8');old=old.replace('B365—B366完成第1、2部分（PDF p1—2）并补回原生表面结构图。','B365—B368完成p1—4：第1、2部分、原结构图、第3部分引言及表(3a-1)/(3a-2)。两表共162单元，按角度列分别排版。').replace('Q180保留原称待核；第3部分起的取向张量表及附录仍为旧译待核。','Q180—Q181保留待核；扭转C₂表(3b-1)及后续取向表、附录仍为旧译待核。').replace('下一批B367进入p3第3部分，引言及完整表(3a-1)按角度列逐格核验。','下一批B369进入p5扭转C₂的表(3b-1)/(3b-2)。');p.write_text(old,encoding='utf-8')
p=root/'Preface序言.md';old=p.read_text(encoding='utf-8');old=re.sub(r'(?m)^- \[4\.7 .*$',lambda m:m[0].split('（第1、2部分已译校）')[0]+'（已译校至p4表3a-2）：比较表面模型、建立坐标，按对称/反对称模式与三个角度列读取倾斜C₂ᵥ张量；原图及两表162单元已核，扭转C₂与后续表待核。',old);p.write_text(old,encoding='utf-8')
for filename,text in [('翻译管理/分批执行与质量控制.md','## 4.7前两表完成（B367—B368）\n\np3—4表3a-1/3a-2按27分量和三个角度列逐格核对，完整162单元，含126个零。为避免横向长表，按原角度列拆成三个窄表。未据物理直觉修正原±及同号项，Q181保留。下一批B369进入扭转C₂表。'),('中文版本/附件/原文勘误表.md','## 4.7表3a-1/3a-2阶段状态（B367—B368）\n\n两表已逐格核对。Q181原共享列±及ZZX两列同号保留，候选未采用，无新增已采用的原文修正。sin²τ/cos²τ恢复属于旧译转录修复。')]:
 p=root/filename;old=p.read_text(encoding='utf-8')
 if text.split('\n')[0] not in old:p.write_text(old+'\n\n'+text+'\n',encoding='utf-8')
report={'date':'2026-10-21','section':'4.7','batches':'B367—B368','verified_pages':[3,4],'tables':['3a-1','3a-2'],'tensor_rows':54,'angle_cells':162,'zero_cells':126,'nonzero_cells':36,'cumulative_math_fragments_B365_B368':435,'math_syntax_errors':0,'formula_overflows':0,'open_source_issue':'Q181','source_corrections_adopted':False,'next_batch':'B369，p5表(3b-1)/(3b-2)','translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
(out/'B367—B368阶段复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'B367—B368阶段复核.md').write_text('''# 4.7表(3a-1)/(3a-2)阶段复核

2026-10-21，B367—B368，PDF p3—4。累计已核p1—4，未登记整节完成。

- 第3部分实验室系引言及两张倾斜C₂ᵥ对称/反对称伸缩表完整覆盖；每表27分量×三个原角度列，共162单元。
- 表(3a-1)51零/30非零，表(3a-2)75零/6非零；未因大量零项而省略分量。
- 逐格对照原页恢复sin²τ/cos²τ，旧译倍角错误已修复。按角度列拆窄表，仅改变排版。
- Q181保留共享0°/180°列的±、−(±)及原ZZX在±90°两列同号。未确认上下号映射，不自行分列指定符号。
- 累计四批435个数学片段通过严格语法检查，预览无横向页面溢出；新两表的显示检查见参考预览。排版通过不等于原文公式已获物理验证。
- 导读、序言、章节清单、当前进度、分批计划、局部约定、疑难及勘误状态已更新。

下一批B369：PDF p5扭转C₂的表(3b-1)/(3b-2)，表3b-1及其后旧译仍待核。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

from pathlib import Path
import json,hashlib,csv,io,re
out=Path(__file__).resolve().parent;root=out.parents[2]
rec=json.loads((out/'B369-覆盖.json').read_text(encoding='utf-8'))
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert render['math']==504
r=next(x for x in render['results'] if x['batch']=='B369')
assert not r['overs'] and r['width']==r['scrollWidth']
vals=[v for t in rec['tables'] for c in t['components'] for v in c['values']]
assert len(vals)==42 and vals.count('0')==3
assert sum(len(t['none_polarizations']) for t in rec['tables'])==5
rec.update(status='逐格译校及参考排版验收完成',render=r,cumulative_math_fragments=504,translation_sha256=hashlib.sha256((out/'B369-本批译文.md').read_bytes()).hexdigest(),scope_limit='原表覆盖、转录及排版核验，不等于原文公式的独立物理证明。')
(out/'B369验收.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
description='PDF p5，扭转HCCH（C₂）的对称/反对称伸缩表(3b-1)/(3b-2)已逐格译校。两表14分量行×3角度列=42单元，39非零、3零，另有5个none偏振项；none与显式零值分别保留。βbca与−βcab按原列保留指标与符号。累计B365—B369的504个数学片段语法检查通过，新表预览无页面横向溢出。无新增已采用的原文修正，Q180—Q181仍待核。下一批B370：p6表(3a-3)，逐列核对±45°/±135°条件。'
(out/'B369.md').write_text('# B369校订与验收记录\n\n2026-10-21。'+description+'\n\n已对照原文p5图像及中文参考渲染。排版检查不代替物理推导。\n',encoding='utf-8')
def append(path,heading,body):
 s=path.read_text(encoding='utf-8')
 if heading not in s:path.write_text(s+'\n\n'+heading+'\n\n'+body+'\n',encoding='utf-8')
for name in ['局部约定卡.md','结构与分批计划.md','术语卡.md']:
 append(out/name,'## B369补充',description if name!='术语卡.md' else 'none译作“无”，保留原表项的语义范围；不将未列分量自行补成零。显式0照录。βbca和βcab保持原指标，不能直接合并。')
p=root/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8');heading='## 当前有效状态：B369完成4.7表(3b-1)/(3b-2)（2026-10-21）'
if heading not in s:p.write_text('# 当前进度与续接\n\n'+heading+'\n\n累计已核4.7的p1—5；表(3a-3)及后续旧译待核。'+description+'\n\n以下为历史记录。\n\n'+s.split('\n',1)[1],encoding='utf-8')
p=root/'翻译管理/章节清单.tsv';rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0])
for row in rows:
 if row['编号']=='4.7':row.update({'状态':'本轮校订中：B365—B369完成p1—5；表3a-3起旧译待核','映射核验':'p1—5及表3a-1/3a-2/3b-1/3b-2逐格核对','公式图表范围':'原图1幅；四表204角度单元（129零/75非零），另5个none项','导读状态':'已更新至p5扭转C₂两表','导读草案':'比较表面模型、定义坐标，再读取倾斜C₂ᵥ与扭转C₂的对称/反对称伸缩表；其他角度表及附录待核。'})
with p.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p=root/'中文版本/第四章 单层膜与多层膜的和频/阅读导航.md';s=p.read_text(encoding='utf-8')
s=s.replace('B365—B368完成p1—4：第1、2部分、原结构图、第3部分引言及表(3a-1)/(3a-2)。两表共162单元，按角度列分别排版。','B365—B369完成p1—5：第1、2部分、原结构图、第3部分引言及表(3a-1)/(3a-2)、(3b-1)/(3b-2)。四表共204角度单元，另保留5个none项。')
s=s.replace('扭转C₂表(3b-1)及后续取向表、附录仍为旧译待核。','表(3a-3)及后续取向表、附录仍为旧译待核。').replace('下一批B369进入p5扭转C₂的表(3b-1)/(3b-2)。','下一批B370进入p6表(3a-3)。');p.write_text(s,encoding='utf-8')
p=root/'Preface序言.md';s=p.read_text(encoding='utf-8')
s=re.sub(r'(?m)^- \[4\.7 .*$',lambda m:m[0].split('（已译校至')[0]+'（已译校至p5表3b-2）：比较表面模型、建立坐标，读取倾斜C₂ᵥ与扭转C₂的对称/反对称伸缩张量；原图及四表204角度单元、5个none项已核，后续角度表待核。',s);p.write_text(s,encoding='utf-8')
append(root/'翻译管理/分批执行与质量控制.md','## 4.7扭转C₂前两表完成（B369）',description)
append(root/'中文版本/附件/原文勘误表.md','## 4.7表3b-1/3b-2阶段状态（B369）','p5两表已按原页核对，无新增已采用的原文修正。原none、显式零值及β指标差异均保留；Q180—Q181维持待核。')
print(description)

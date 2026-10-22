from 收尾公式工具 import *
from collections import Counter
from urllib.parse import unquote
s=TARGET.read_text(encoding='utf-8');old=(OUT/'B094-修订前.md').read_text(encoding='utf-8')
# Preserve the already reviewed portion exactly; do not apply later glyph decisions
# to an earlier source anomaly (notably Q059 / 4.17).
for label in ['4.17']:
 pattern=r'\$\$[\s\S]*?\$\$'
 before=next(x.group() for x in re.finditer(pattern,old) if r'\tag{'+label+'}' in x.group())
 s=re.sub(pattern,lambda x:before if r'\tag{'+label+'}' in x.group() else x.group(),s)
line=next(x for x in old.splitlines() if '**译校注（Q059' in x)
s=re.sub(r'> \*\*译校注（Q059[^\n]*',lambda _:line,s)
s=re.sub(r'> \*\*公式与插图说明：\*\*[^\n]*','> **公式与插图说明：** 全部公式采用可编辑数学格式，跨页长式合并衔接；实际光路示意图仍保留并配中文说明。原公式图按页码与编号归档，供逐项对照。原式疑点及候选修正见就地译校注与[勘误附件](../附件/原文勘误表.md)。',s,count=1)
s=s.replace('公式保留底本影像，未对原式各项作独立代数认证。','公式已转为可编辑数学，底本影像另存对照；未对原式各项作独立代数认证。').replace('公式影像保留底本符号；并不表示所有原式已经独立推导验证。','数学转写保留底本符号，原式图另存；并不表示所有原式已经独立推导验证。').replace('这里保留原式影像，不静默补因子。','这里按底本转写，不静默补因子；原式图另存对照。')
TARGET.write_text(s,encoding='utf-8')
# Exact coverage audit: all 132 historic images are either actual diagrams or
# explicitly retired to editable transcription by B082–B114 coverage manifests.
manifest=json.loads((OUT/'公式图索引.json').read_text(encoding='utf-8'))
live=set(re.findall(r'\.\./assets/ch02/s02/([^\s)]+)',s))
retired={}
for f in OUT.glob('B???-覆盖.json'):
 o=json.loads(f.read_text(encoding='utf-8'))
 if int(f.name[1:4])>=94:
  for name in o.get('source_images',[]):retired[name]=o['batch']
# Earlier B082–B093 records use other schemas; their 16 replacements are
# enumerated from the retained before/after image inventory.
original_live=set(re.findall(r'\.\./assets/ch02/s02/([^\s)]+)',old))
for x in manifest:
 if x['file'] not in original_live:retired[x['file']]='B082—B093'
uncovered=[x['file'] for x in manifest if x['file'] not in live and x['file'] not in retired]
allowed={'B079-p40-01.png','B080-p41-01.png','B080-p42-02.png','B080-p43-04.png','B080-p43-05.png'}
assert live==allowed,(live,allowed)
assert not uncovered,uncovered
labels=re.findall(r'\\tag\{([^}]+)\}',s);dups=[x for x,v in Counter(labels).items() if v>1]
assert len(labels)==116 and not dups,(len(labels),dups)
index=json.loads((OUT/'全节公式编号索引.json').read_text(encoding='utf-8'))
assert all(x['representation']=='数学转写' for x in index)
assert set(labels)=={x['equation'] for x in index}
control=[(i,ord(c)) for i,c in enumerate(s) if ord(c)<32 and c not in '\n\r']
assert not control,control
missing=[]
plain=re.sub(r'\$\$[\s\S]*?\$\$|\$[^$\n]+\$','',s)
for link in re.findall(r'\]\(([^\n)]+)\)',plain):
 if re.match(r'https?://|#',link):continue
 p=(TARGET.parent/unquote(link.split('#')[0])).resolve()
 if not p.exists():missing.append(str(p))
assert not missing,missing
sha=hashlib.sha256((ROOT/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest()
assert sha=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
render=json.loads((OUT/'渲染检查.json').read_text(encoding='utf-8'))
rr=[x for x in render['results'] if 94<=int(x['batch'][1:])<=114]
assert len(rr)==21 and all(not x.get('overs') and x['scrollWidth']==1100 for x in rr)
beforemath=re.findall(r'\$\$[\s\S]*?\$\$',old.split('## 5.')[0])
aftermath=re.findall(r'\$\$[\s\S]*?\$\$',s.split('## 5.')[0])
assert beforemath==aftermath,'Earlier reviewed mathematics changed'
rows=[]
for x in manifest:rows.append({'source_image':x['file'],'page':x['page'],'caption':x['caption'],'current':'示意图' if x['file'] in live else '可编辑数学','batch':retired.get(x['file'],'原图保留')})
(OUT/'全节图式去向索引.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'全节图式去向索引.md').write_text('# 全节图式去向索引\n\n132幅历史切片逐项去向；原图未删除。\n\n| PDF页 | 原图 | 内容 | 当前形式 | 批次 |\n|---|---|---|---|---|\n'+''.join(f"| {x['page']} | {x['source_image']} | {x['caption']} | {x['current']} | {x['batch']} |\n" for x in rows),encoding='utf-8')
report={'date':'2026-10-19','batch_end':'B114','source_pages':47,'source_sha256':sha,'numbered_equations':len(labels),'unique':len(set(labels)),'all_numbered_editable':True,'historical_crops':len(manifest),'retired_equation_crops':len(retired),'remaining_real_diagrams':sorted(live),'uncovered_crops':uncovered,'control_characters':control,'missing_local_references':missing,'new_rendered_batches':len(rr),'new_formula_overflows':0,'previous_section_1_to_4_math_unchanged':True}
(OUT/'全节数学收尾验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'全节数学收尾验收.md').write_text('''# 2.2全节数学收尾验收

2026-10-19，至B114。本记录取代B081交付快照中“可编辑转写待完成”的当前状态；历史快照保留。

本节47页正文与附录A—D已完成本轮译校和可编辑数学转写。B094—B114共21批覆盖剩余L系数、所有源点振幅、反射与透射的完整路径求和、体相极化展开和积分、附录A/B/C及附录D六条推导。没有用摘要替代长公式。

| 检查 | 结果 |
|---|---|
| 编号 | 116个唯一编号式，全部数学转写，无重号或漏号；见全节公式编号索引 |
| 无编号式去向 | 132幅历史切片全部有去向：127幅已替换为数学转写，5幅实际示意图继续保留；见全节图式去向索引 |
| 跨页与重叠 | 5.19b、体相透射极化/积分、附录D等并为完整公式；不重复显示重叠裁切内容 |
| 数学语法 | 全节KaTeX严格检查通过；最终片段计数见渲染检查.json |
| 显示 | B094—B114全部21批本地渲染；970px正文宽度下无公式横向溢出，页面宽1100px；重点目视检查B097/B100/B102/B110/B114 |
| 文件 | 正文全部本地引用有效，无制表符/其他控制字符；原PDF SHA256与登记一致 |
| 已核前文 | 第1—4部分数学内容与B094前快照逐块一致，既有Q059等未被后续转写规则改动 |
| 管理 | Preface、第二章导航、章节清单、分批建议、当前进度、符号卡、疑难与勘误附件状态已同步 |

Q065—Q072为新登记的未决原式问题；与既有问题一起保留原文并注明。易重叠字形经图像与文字层复核后修复的是转写误读，不增加原文勘误编号。本轮没有新增采用的公式修正，E-2.2-001—005维持既有状态。

以上为翻译、转写、覆盖和排版层面的本轮验收，不代表原式经独立专家代数/物理认证。下一独立底本2.3未开始本轮校订；后续新批号B115。
''',encoding='utf-8')
p=OUT/'整节完成复核.md';t=p.read_text(encoding='utf-8')
if '> **当前状态更新（B114）' not in t:t=t.replace('# 2.2整节完成复核\n','# 2.2整节完成复核\n\n> **当前状态更新（B114）：** 本文以下保留B081及B093历史快照。2026-10-19已完成全节正文和附录A—D的可编辑数学转写，116个唯一编号式全部覆盖；当前验收以[全节数学收尾验收](全节数学收尾验收.md)为准。\n',1)
p.write_text(t,encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

from pathlib import Path
import csv,json,hashlib,re
from urllib.parse import unquote
root=Path('HiroseSFGNote').resolve();m=root/'翻译管理';base=m/'全书调查'
def read(name):return list(csv.DictReader((base/name).open(encoding='utf-8-sig'),delimiter='\t'))
sections=read('逐节工作量.tsv');pages=read('逐页工作量.tsv');blocks=read('内部结构与页组.tsv');plans=read('分批建议.tsv');chapters=read('分章工作量.tsv')
assert len(sections)==39 and len(pages)==717 and len(blocks)==200 and len(plans)==488
for s in sections:
 sid=s['节号'];n=int(s['PDF页数'])
 assert hashlib.sha256((root/s['原文路径']).read_bytes()).hexdigest()==s['原文SHA256']
 ps=[p for p in pages if p['节号']==sid];assert sorted(int(p['PDF页']) for p in ps)==list(range(1,n+1))
 bs=[b for b in blocks if b['节号']==sid];cov=[v for b in bs for v in range(int(b['PDF起页']),int(b['PDF止页'])+1)];assert cov==list(range(1,n+1)),sid
 assert sum(int(b['清洗可提取字符数']) for b in bs)==int(s['清洗可提取字符数'])
 windows=[p for p in plans if p['节号']==sid];cov=[v for p in windows for v in range(int(p['PDF起页']),int(p['PDF止页'])+1)]
 assert cov==[v for v in range(1,n+1) if not(sid=='5.4' and v==15)],sid
 for p in s['原文视觉抽查页'].split(','):assert (base/'页面抽查'/f'{sid}-p{p}.png').exists()
assert sum(len(s['原文视觉抽查页'].split(',')) for s in sections)==88
for field in ['PDF页数','清洗可提取字符数','汉字假名字符数','结构页组数','当前保守预排批数']:
 assert sum(int(c[field]) for c in chapters)==sum(int(s[field]) for s in sections),field
for doc in [base/'全书结构与工作量调查报告.md',base/'全书结构记录.md',m/'当前进度与续接.md',m/'执行方案.md']:
 for link in re.findall(r'\]\(([^)]+)\)',doc.read_text(encoding='utf-8')):
  if not link.startswith(('http:','https:')):assert (doc.parent/unquote(link)).exists(),(doc,link)
manifest=json.loads((m/'基线快照清单.json').read_text(encoding='utf-8'))
for item in manifest:
 if item['path'].startswith(('日语原版/','中文版本/')):
  assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256'],item['path']
summary=json.loads((base/'调查摘要数据.json').read_text(encoding='utf-8'))
assert sum(int(p['清洗可提取字符数']) for p in pages)==summary['clean_chars']==967943
(base/'调查验收记录.md').write_text('''# 调查验收记录\n\n日期：2026-10-16。\n\n- 39 份 PDF 的摘要与原文一致；717 条逐页记录编号完整且唯一。\n- 200 个结构页组覆盖全部 717 页，各节内部无页码空档或重复计入。\n- 488 个待执行页级窗口覆盖全部非空白尾页；仅排除视觉确认的 5.4 p15。\n- 分章、逐节、页组和逐页字符总量一致：967,943 个清洗可提取字符。\n- 88 个不同视觉抽查页面均有图像文件，抽查位置见逐节表。\n- 报告、结构记录及续接入口中的本地链接均存在。\n- 原文及旧译与既有基线摘要一致，本轮没有改动译文正文。\n\n检查范围：数据一致性、路径、摘要与计划覆盖。结构已结合全量提取文本及首尾/关键页抽查整理；不是717页逐页视觉审校、公式验收或旧译完整性证明。\n''',encoding='utf-8')
print('PASS: 39 PDFs / 717 pages / 200 units / 488 provisional windows / 88 visual samples; counts, links, hashes and unchanged translations verified.')

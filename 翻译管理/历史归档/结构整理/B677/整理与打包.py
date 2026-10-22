from pathlib import Path
from collections import Counter,defaultdict,deque
import csv,json,re,hashlib,shutil,urllib.parse,os,zipfile
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/文件结构审查';O.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(rel,text):
 p=R/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
def link(p,base):return urllib.parse.quote(os.path.relpath(p,base).replace('\\','/'),safe='/.-_')
rows=list(csv.DictReader((R/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
protected=[R/x[k] for x in rows for k in ['现有译文路径','原文路径']]+[R/'Preface序言.md',R/'中文版本/附件/原文勘误表.md']
before={p.relative_to(R).as_posix():sha(p) for p in protected}
inventory=[];groups=defaultdict(list)
baseline=O/'整理前文件清单.json'
if baseline.exists():
 inventory=json.loads(baseline.read_text(encoding='utf-8'))['files']
 for x in inventory:groups[(x['bytes'],x['sha256'])].append(x['path'])
for p in ([] if baseline.exists() else sorted(R.rglob('*'))):
 if not p.is_file() or any(x in p.relative_to(R).parts for x in ['.git','交付版本']):continue
 rel=p.relative_to(R).as_posix();size=p.stat().st_size;digest=sha(p)
 if rel.startswith('日语原版/'):kind='日语底本（保留）'
 elif rel.startswith('中文版本/'):kind='译文稿源与资源（保留）'
 elif rel.startswith('合稿准备/'):kind='合稿生成物' if not re.match(r'B\d+.*\.html',p.name) else '历批提示验收页面（保留）'
 elif any(x in rel for x in ['/校订记录/','/基线快照/','修改前/','原页/','/术语修订记录/']):kind='历史证据（保留原址）'
 elif p.suffix in ['.py','.cjs','.pyc']:kind='维护脚本或缓存（保留）'
 elif p.name=='.DS_Store':kind='系统元数据（未删除）'
 else:kind='说明、管理或复核产物（保留）'
 inventory.append({'path':rel,'bytes':size,'sha256':digest,'category':kind});groups[(size,digest)].append(rel)
duplicates=[{'bytes_each':key[0],'sha256':key[1],'paths':paths,'decision':'保留；同内容可能是有意快照或独立底本，未按摘要删除'} for key,paths in groups.items() if len(paths)>1]
(O/'整理前文件清单.json').write_text(json.dumps({'scope':'排除.git及交付生成副本；只读摘要盘点','files':inventory},ensure_ascii=False,indent=2),encoding='utf-8')
(O/'重复内容候选.json').write_text(json.dumps(duplicates,ensure_ascii=False,indent=2),encoding='utf-8')
guide='''# 项目导航

## 阅读译本

- [打开全书阅读目录](合稿准备/index.html)：序言、八章及勘误附件。
- [序言与逐节内容概括](Preface序言.md)。
- [单文件Markdown合稿](合稿准备/全书审阅稿.md)。
- [独立阅读包说明](交付版本/README.md)：下载或转移时整体保留。

## 修订与审校

39节独立Markdown及其图片在“中文版本”中，是唯一日常修订稿源。合稿和交付包由它们生成，请勿分别修改副本。节号与原式号继续保留。

- [翻译管理入口](翻译管理/README.md)
- [当前进度](翻译管理/当前进度与续接.md)
- [章节清单](翻译管理/章节清单.tsv)
- [完整问题现状](翻译管理/全书复核/问题状态汇总.md)
- [本轮核查报告](翻译管理/全书复核/B676全书收尾复核.md)

## 底本与历史

日语原版为只读翻译底本；“校订记录”“基线快照”和历批修改前副本属于追溯证据，保留现有路径。历史文件中的旧状态仅代表当时进度。

- [历史资料索引](翻译管理/历史资料索引.md)
- [文件结构审查报告](翻译管理/文件结构审查/文件结构审查与整理报告.md)

第四章现有文件夹“单层膜与多层膜的和频”是历史路径，其正文主题为CH伸缩振动及取向张量；以节标题和本导航为准。现有文件夹名暂保留，以维持历史引用和维护脚本的定位。EnglishVersion仅保留原有占位资料，尚无英文译本。
'''
write('项目导航.md',guide)
write('翻译管理/README.md','''# 翻译管理入口

## 当前有效文件

- [当前进度与续接](当前进度与续接.md)
- [章节清单](章节清单.tsv)：39节稿源位置、底本摘要、覆盖和状态。
- [翻译规范](翻译规范.md)、[分批质量控制](分批执行与质量控制.md)
- [术语表](术语表.tsv)、[符号与约定](符号与约定.md)
- [320项问题现状](全书复核/问题状态汇总.md)：先查现状，再追溯[历史登记](疑难与勘误.md)。
- [B676核查收尾](全书复核/B676全书收尾复核.md)、[验收总表](全书复核/B676验收总表.json)
- [文件结构整理报告](文件结构审查/文件结构审查与整理报告.md)

## 维护与生成

“全书复核”内的全书复核.py、数学与合稿.cjs用于从稿源重建合稿；旧批号、绝对运行时路径及工作目录约定在运行前须检查。历批脚本是当时修订的过程记录，不作为一键重放全部翻译的入口。新建阅读包使用“文件结构审查/整理与打包.py”，当前交付是B676内容快照。

日常修订顺序：修改独立节稿与局部说明 → 更新问题/术语决定 → 重建合稿 → 验收 → 重新生成有版本标识的交付快照。已有交付包不作为稿源。

历史材料位置见[历史索引](历史资料索引.md)；完整项目入口见[项目导航](../项目导航.md)。
''')
history=['# 历史资料索引','','以下为原位分类归档，文件未搬迁或删除。原路径是已有说明和脚本的依赖；旧报告须结合当前问题状态阅读。','','| 目录 | 用途 |','|---|---|','| [校订记录](校订记录/) | 按节保存批次、原页、对照和验收 |','| [基线快照](基线快照/) | 重访前译稿及管理基线 |','| [全书调查](全书调查/) | 初始结构、工作量、提取风险和页组 |','| [已核验对照语料](已核验对照语料/) | 已登记的语料，非全书自动翻译记忆 |','| [术语修订记录](术语修订记录/) | 历次术语决定及依据 |','| [来源记录](来源记录/) | 来源与获取信息 |','','## 全书复核阶段的证据目录','']
for p in sorted((R/'翻译管理/全书复核').iterdir()):
 if p.is_dir() and re.match('B\\d+',p.name):history.append('- ['+p.name+']('+link(p,R/'翻译管理')+'/)：'+('修改前副本' if '修改前' in p.name else '专项原页或放大图'))
history+=['','“合稿准备”中的B批号阅读提示页面为历史验收生成物；主阅读入口始终是index.html。根目录历史脚本和缓存仅登记保留，不列入阅读包。']
write('翻译管理/历史资料索引.md','\n'.join(history)+'\n')
readme=R/'README.md';s=readme.read_text(encoding='utf-8-sig');banner='> 阅读与维护入口：[项目导航](项目导航.md) · [全书阅读目录](合稿准备/index.html) · [翻译管理](翻译管理/README.md) · [独立阅读包](交付版本/README.md)'
if banner not in s:readme.write_text(banner+'\n\n'+s,encoding='utf-8')
write('开始阅读.html','<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>Hirose SFG 中文译本</title><style>body{max-width:850px;margin:60px auto;padding:20px;font:20px/1.9 sans-serif}a{color:#245f8c}</style><h1>Hirose SFG 中文译本</h1><p><a href="合稿准备/index.html">打开全书阅读目录</a></p><p><a href="项目导航.md">项目导航</a> · <a href="翻译管理/README.md">翻译管理</a> · <a href="交付版本/README.md">独立阅读包</a></p><p>审阅稿B676；原文疑点和暂译保留。39节独立Markdown为修订稿源。</p></html>')
# Freeze only a new, named output; never move or delete workspace files.
D=R/'交付版本/中文审阅版-B676';D.mkdir(parents=True,exist_ok=True)
package_readme='''# Hirose SFG 中文审阅版 B676

打开[开始阅读.html](开始阅读.html)或[全书目录](合稿准备/index.html)。本包含39节独立Markdown、八章排版稿、序言、勘误和当前阅读链所需资料。文件为生成快照，请返回工作项目修改稿源后重新打包。

请整体解压并保留目录结构，图片和字体可离线读取。外部文献链接仍需联网。JSON中的原始路径与摘要是追溯字段，不表示包中附有全部历史或原始底本。未包含的历史材料请回原工作项目查阅。

320项问题已有处置记录，310项原文/约定疑点仍保留。保留原作者版权信息及LICENSE；此包为本地阅读交付，未发布。
'''
overrides={'README.md':package_readme,'开始阅读.html':'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>Hirose SFG 中文审阅版 B676</title><style>body{max-width:800px;margin:60px auto;font:20px/1.9 sans-serif}</style><h1>Hirose SFG 中文审阅版 B676</h1><p><a href="合稿准备/index.html">进入全书目录</a></p><p><a href="Preface序言.md">序言与逐节导读</a> · <a href="README.md">使用说明</a></p><p>原文疑点及暂译保留。</p></html>'}
class H(HTMLParser):
 def __init__(self):super().__init__();self.refs=[]
 def handle_starttag(self,tag,attrs):
  self.refs.extend(v for k,v in attrs if k in ['href','src'] and v)
# Bundled source CSS offers legacy fallbacks which were never installed.
# A portable copy keeps the existing WOFF2 face for each family; source CSS
# stays untouched. This removes dangling optional resources without fetching.
css_rel='翻译管理/排版工具/katex.min.css'
css=(R/css_rel).read_text(encoding='utf-8')
portable_css,nfallback=re.subn(r',url\(fonts/[^)]+\.(?:woff|ttf)\) format\("(?:woff|truetype)"\)','',css)
assert nfallback==40
overrides[css_rel]=portable_css
math=re.compile(r'\$\$[\s\S]*?\$\$|(?<![\\$])\$(?!\$)(?:\\.|[^$\n])+\$')
def references(p,s):
 if p.suffix=='.md':return re.findall(r'!?\[[^\]\n]*\]\(([^\n]*?)\)',math.sub('',re.sub(r'```[\s\S]*?```','',s)))
 if p.suffix=='.html':h=H();h.feed(s);return h.refs
 if p.suffix=='.css':return re.findall(r'url\([\'"]?([^\)\'"\s]+)',s)
 return []
roots=['开始阅读.html','README.md','LICENSE','Preface序言.md','合稿准备/index.html','合稿准备/序言.html','合稿准备/附件.html','合稿准备/使用说明.md','合稿准备/全书审阅稿.md','合稿准备/合稿清单.json',*[f'合稿准备/第{i}章.html' for i in range(1,9)],*[x['现有译文路径'] for x in rows]]
queue=deque(roots);seen=set();edges=[];missing=[]
while queue:
 rel=queue.popleft()
 if rel in seen:continue
 seen.add(rel);p=R/rel
 if rel in overrides:data=overrides[rel].encode('utf-8')
 elif p.is_file():data=p.read_bytes()
 elif p.is_dir():queue.extend(x.relative_to(R).as_posix() for x in p.rglob('*') if x.is_file());continue
 else:missing.append(rel);continue
 target=D/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
 if p.suffix not in ['.md','.html','.css']:continue
 s=data.decode('utf-8-sig')
 for href in references(p,s):
  href=href.strip().strip('<>');u=urllib.parse.urlsplit(href)
  if u.scheme or not u.path:continue
  dest=(p.parent/urllib.parse.unquote(u.path)).resolve()
  if not dest.is_relative_to(R):raise ValueError('Reference escapes project: '+href)
  dep=dest.relative_to(R).as_posix()
  if dep.startswith(('交付版本/','.git/')):raise ValueError('Unexpected generated or Git dependency: '+dep)
  edges.append({'from':rel,'to':dep});queue.append(dep)
assert not missing,missing
assert len(seen)<3000,'Unexpectedly broad dependency closure'
packfiles=[p for p in D.rglob('*') if p.is_file()]
manifest=[{'path':p.relative_to(D).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(packfiles)]
for e in edges:assert (D/e['to']).exists(),e
assert all(sha(D/x['现有译文路径'])==before[x['现有译文路径']] for x in rows)
assert all(sha(R/rel)==h for rel,h in before.items()),'Protected source modified'
(D/'阅读包清单.json').write_text(json.dumps({'content_batch':'B676','packaging_batch':'B677','files':manifest,'local_dependencies':edges,'all_local_dependencies_present':True,'source_sections':39,'policy':'生成快照；不单独编辑；保留全目录'},ensure_ascii=False,indent=2),encoding='utf-8')
zip_path=R/'交付版本/Hirose-SFG-中文审阅版-B676.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(D.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(D.parent).as_posix())
with zipfile.ZipFile(zip_path) as z:assert z.testzip() is None
write('交付版本/README.md','''# 交付版本

- [打开独立阅读包](中文审阅版-B676/开始阅读.html)
- [ZIP压缩包](Hirose-SFG-中文审阅版-B676.zip)：整体解压后打开“开始阅读.html”。
- [包内使用说明](中文审阅版-B676/README.md)
- [文件清单与摘要](中文审阅版-B676/阅读包清单.json)

内容版本B676，整理打包批次B677（2026-10-22）。此目录存放生成快照；原39节稿源仍位于项目“中文版本”。不把本目录再作为合稿输入，不从中开展平行修订。新版本采用新目录/批号，不覆盖已有交付决定。

原作者版权信息与LICENSE保留，未发布到外部网站。图片与字体随包提供，外部文献需联网；全部历史证据仍在工作项目中。
''')
counts=Counter(x['category'] for x in inventory)
result={'batch':'B677','source_content_batch':'B676','inventory_files':len(inventory),'inventory_bytes':sum(x['bytes'] for x in inventory),'categories':dict(counts),'exact_duplicate_groups':len(duplicates),'deleted_files':0,'moved_files':0,'protected_source_hashes_unchanged':True,'protected_files':before,'package_files':len(manifest)+1,'package_bytes':sum(x['bytes'] for x in manifest),'package_local_dependencies':len(edges),'missing_package_local_dependencies':missing,'package_only_removed_uninstalled_legacy_font_fallbacks':nfallback,'source_CSS_unchanged':sha(R/css_rel)==hashlib.sha256(css.encode('utf-8')).hexdigest(),'zip_bytes':zip_path.stat().st_size,'zip_sha256':sha(zip_path),'zip_integrity_passed':True}
(O/'整理与交付验收.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
report=f'''# 文件结构审查与整理报告（B677）

2026-10-22。内容基线为B676审阅稿；本批负责目录、入口、版本辨识及交付，不改变翻译决定。

## 盘点结果

初始盘点{len(inventory):,}个文件，约{result['inventory_bytes']/1048576:.1f}MiB（排除.git及交付副本）。历史主体已按节存于校订记录，现有分类具有追溯价值。摘要相同的候选组共{len(duplicates)}组，含快照和复用资源，未因重复摘要删除。清单见[整理前文件清单](整理前文件清单.json)、[重复内容候选](重复内容候选.json)。

主要问题是缺少统一入口、B批次验收页面与当前合稿并列、根目录历史脚本用途不直观，以及第四章文件夹名称为历史主题。维护脚本大量按自身相对位置定位，正文/历史证据又包含原路径，目录整体搬迁需另作兼容迁移。

## 已完成的整理

1. 新增根目录“开始阅读.html”和[项目导航](../../项目导航.md)，README顶部增加入口，保留既有作者、版权和译者说明。
2. 新增[翻译管理入口](../README.md)，明确现行清单、问题状态、规范和维护顺序。
3. 新增[历史索引](../历史资料索引.md)，对校订记录、快照、专项原页、修改前副本及历史脚本作原位归档说明；旧报告仍保留时间语境。
4. 建立“交付版本”，将稿源、工作区合稿及阅读快照的角色分开。39节稿源仍是唯一日常修订位置；未移动或删除历史资料、未重命名章节文件夹。
5. 生成[可携带阅读包](../../交付版本/README.md)，含11个阅读页面、39节Markdown、序言、勘误、图片、字体及阅读链接所需资料；通过本地依赖递归收集而非复制全部管理目录。包中不含.git或历史脚本运行环境。

## 验收

阅读包内CSS保留现有20个WOFF2字体，移除40处未安装的WOFF/TTF备用引用；工作项目原CSS不变。此项为交付副本的资源处理，使用支持WOFF2的现代浏览器，不改变数学内容。

39份正文、39份日语底本、序言与勘误附件的摘要均未改变。交付包共{len(manifest)+1}个文件，收集{len(edges)}处本地依赖且无缺失；ZIP完整性检查通过，大小{result['zip_bytes']/1048576:.1f}MiB。未移动、未删除工作区文件。详见[验收记录](整理与交付验收.json)。

本轮原位分类与入口整理已完成。第四章目录仍以兼容路径保留，在导航注明实际主题；若未来要统一实体目录名，须同时迁移稿源、清单、脚本和历史引用。JSON内的追溯路径不全部视为阅读依赖。外部链接未进行可用性保证，B676中310项未决疑点仍按原处置保留。
'''
write('翻译管理/文件结构审查/文件结构审查与整理报告.md',report)
progress=R/'翻译管理/当前进度与续接.md';s=progress.read_text(encoding='utf-8-sig')
if '## 当前有效状态：B677' not in s:
 s=s.replace('## 当前有效状态：B676','## 历史状态：B676',1)
 s=s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n## 当前有效状态：B677文件结构整理与阅读交付（2026-10-22）\n\nB676内容未变。本批完成文件盘点、统一阅读/管理入口、历史资料原位索引和独立阅读包；39节稿源、39份底本、序言及勘误附件摘要一致。历史路径保留，无删除或搬迁。使用[项目导航](../项目导航.md)或[交付包](../交付版本/README.md)阅读；详见[结构整理报告](文件结构审查/文件结构审查与整理报告.md)。\n\n',1);progress.write_text(s,encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='protected_files'},ensure_ascii=False))

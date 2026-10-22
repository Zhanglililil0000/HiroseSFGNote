"""Complete disposition index; history is evidence, never blanket proof of physics."""
from pathlib import Path
import re,json,csv,collections,urllib.parse,os
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核'
BATCH=json.loads((R/'合稿准备/合稿清单.json').read_text(encoding='utf-8')).get('batch','B676')
q=(R/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8-sig');qlines=q.splitlines()
rows=list(csv.DictReader((R/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
docs={r['现有译文路径']:(R/r['现有译文路径']).read_text(encoding='utf-8-sig') for r in rows}
# These two numbers were explicitly never allocated; mentions of that fact
# in final management prose are not new issue definitions.
ids=sorted(set(re.findall(r'Q\d{3}',q))-{'Q108','Q109'})
process={
'Q001':('主题映射已落实','第四章正文主题已明确为CH伸缩振动及取向张量；导航与各节标题据正文更正，旧章节文件夹名保留作兼容标识。'),
'Q002':('小节命名已修复','4.2—4.11按正文主题更名并同步引用；不据旧标题判整篇错译。'),
'Q003':('小节命名已修复','3.2现为双层膜和频的一般式，附录仍在本节末尾。'),
'Q004':('译者问题已修复','B002删除旧译多余括号；无原文修正。'),
'Q005':('实际页界已落实','4.1、4.5、4.8按实际PDF页续接；原目录差异保留，不改原页码。'),
'Q006':('提取风险处理策略已落实','正文以页面/原图为准；CID/私用区的源文件提取风险未被修复，不能依抽取字符串补猜符号。'),
'Q007':('重叠稿处理策略已落实','2.2/2.3及4.1/4.6独立留存、分别对照；不声称重叠段数学等价。'),
'Q009':('译者排版问题已处理','参考环境已补渲染核验，本轮再验全书；不保证所有第三方Markdown软件效果。')}
special={'Q013':('用户确认修正','E-1.1-003：按用户确认将第二个矩阵元下标j改为i；非作者已发布勘误。'),'Q304':('译者误报已撤回','B668确认σ在根号外，原归一化误报撤回；裁图修复另记。')}
current=[]
def plain(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s);s=s.replace('$','').replace('**','').replace('|','／').strip('> #')
 return re.sub(r'\s+',' ',s)
for id in ids:
 reg=[{'line':n,'text':line} for n,line in enumerate(qlines,1) if re.search(id+r'(?!\d)',line)]
 # Titles must come from this issue's heading/row, not another issue mentioning it.
 heads=[z['text'] for z in reg if re.match(r'^#{2,3} '+id+r'(?!\d)',z['text'])]
 tables=[z['text'] for z in reg if re.match(r'^\| '+id+r'\s*\|',z['text'])]
 if heads:topic=re.sub(r'^#{2,3} '+id+r'[｜：: ]*','',heads[0])
 elif tables:topic=tables[0].split('|')[3].strip()
 else:topic=reg[0]['text']
 loc=[];notes=[]
 for r in rows:
  rel=r['现有译文路径']
  for n,line in enumerate(docs[rel].splitlines(),1):
   if re.search(id+r'(?!\d)',line):
    loc.append({'section':r['编号'],'path':rel,'line':n,'text':line})
    if line.startswith('>') and not any(w in line for w in ['译校状态','校订状态','本轮状态','阅读导引','底本：']):notes.append(line)
 status,disposition=(process.get(id) or special.get(id) or ('原文/约定疑点保留','保留原文及局部说明；现有证据未确定作者修法，候选未据此自动采用。'))
 if id=='Q311':disposition='B675撤回(A4)的x→0误读，原印为α→0；a符号、主值及正侧分布极限条件仍保留。'
 if id=='Q319':disposition='B675把条件3文字恢复为√(2g)；两种面积归一权重与原文字仍有不一致，未确认作者修法。'
 method='现行呈现/登记/处置一致性核查，承接历批页面证据；未本轮逐式重推'
 if 311<=int(id[1:])<=322:method='B675原页与条件性数学专项复核；Q316承接B667'
 if id=='Q304':method='B668放大原页、根号范围及条件性系数复核'
 if id in ['Q010','Q028','Q302','Q303','Q305','Q306','Q307','Q308','Q309','Q310','Q316']:method+='；另有B666—B674专项证据'
 assert reg and (loc or id in process),(id,'untraced')
 assert notes or id in process,(id,'missing specific body note')
 current.append({'id':id,'topic':plain(topic),'status':status,'disposition':disposition,'check_method':method,'registry_mentions':reg,'body_locations':loc,'current_notes':list(dict.fromkeys(notes))})
assert len(current)==320 and len({x['id'] for x in current})==320
(O/'问题当前处置.json').write_text(json.dumps({'batch':BATCH,'theory_review_baseline':'B676','scope':'320个已登记编号的呈现、登记、处置及追溯核查；不是320项物理问题全部解决','items':current},ensure_ascii=False,indent=2),encoding='utf-8')
counts=collections.Counter(x['status'] for x in current)
lines=['# 全书问题当前状态（B676）','','本表覆盖320个已登记编号，每号一行，取代旧版仅抽取表格行的不完整汇总。Q108/Q109未分配。历史登记与当前正文注释均保存在[配套明细](问题当前处置.json)。','','**核查完成不等于原文疑点解决。** 现状保留310项原文/约定疑点（其中可含已修复的译者子问题）；8项命名、定位、流程或排版处理已落实，1项用户确认修正，1项误报撤回。未新增作者确认或独立专业人工复核。','','Q311和Q319的译者子问题本轮已修复，其余边界仍保留。专项证据见[B675](B675附录与拟合复核.md)及[B676收尾报告](B676全书收尾复核.md)。下表“现行说明”链接到稿源；原式/页号与完整注释见明细，不根据简单关键词自动关闭问题。','','| 编号 | 主题 | 当前处置 | 现行说明 |','|---|---|---|---|']
details=['# 全量问题复核明细（B676）','','本文件收集现行说明及登记入口，便利逐项阅读；收集和追溯核验不等于全部独立重推。历史初始判断若被后续修复，以当前处置为准。','']
for x in current:
 id=x['id'];paths=list(dict.fromkeys(z['path'] for z in x['body_locations']))
 refs='、'.join('['+Path(p).name.split(' ')[0]+']('+urllib.parse.quote('../../'+p,safe='/.-_')+')' for p in paths) or '[管理原登记](../疑难与勘误.md)'
 lines.append('| '+id+' | '+x['topic'][:100]+' | '+x['status']+' | '+refs+' |')
 details+=['## '+id+'：'+x['topic'],'',x['status']+'。'+x['disposition'],'',x['check_method']+'。','',refs,'']
 for note in x['current_notes']:
  loc=next(z for z in x['body_locations'] if z['text']==note)
  parent=(R/loc['path']).parent
  def relocate(m):
   u=urllib.parse.urlsplit(m[2])
   if u.scheme or m[2].startswith('#'):return m[0]
   dest=(parent/urllib.parse.unquote(u.path)).resolve()
   href=urllib.parse.quote(os.path.relpath(dest,O).replace('\\','/'),safe='/.-_')
   if u.fragment:href+='#'+u.fragment
   return '['+m[1]+']('+href+')'
  details.append(re.sub(r'\[([^\]\n]+)\]\(([^\n]*?)\)',relocate,note))
 if not x['current_notes']:details.append(x['registry_mentions'][0]['text'])
 details+=['']
(O/'问题状态汇总.md').write_text(('\n'.join(lines)+'\n').replace('（B676）',f'（{BATCH}）').replace('](B675附录与拟合复核.md)','](历史批次/B675/B675附录与拟合复核.md)'),encoding='utf-8')
(O/'全量问题复核明细.md').write_text(('\n'.join(details)+'\n').replace('（B676）',f'（{BATCH}）'),encoding='utf-8')
print(json.dumps({'ids':len(current),'statuses':counts,'missing_body_notes':[]},ensure_ascii=False))

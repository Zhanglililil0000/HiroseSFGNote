from pathlib import Path
import json,re,csv,hashlib,collections,urllib.parse
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';M=R/'合稿准备'
def read(p):return json.loads((O/p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=read('全书验收.json');m=read('数学验收.json');f=read('收尾核验.json');issues=read('问题当前处置.json')
assert a['batch']=='B676' and a['sections']==39 and a['pages']==717
assert not a['broken_links'] and not a['source_hash_mismatches'] and not a['body_questions_not_registered']
assert not m['errors'] and not f['missing_explicit_anchors'] and not f['manifest_hash_mismatch']
assert not f['body_E_not_in_attachment'] and f['body_E_ids']==f['attachment_E_ids']
assert f['question_ids_missing_in_numeric_range']==['Q108','Q109']
assert len(issues['items'])==len({x['id'] for x in issues['items']})==320
links=read('链接与图像清单.json');assets={}
for x in links:
 if not x['image']:continue
 p=((R/x['file']).parent/urllib.parse.unquote(urllib.parse.urlsplit(x['href']).path)).resolve();rel=p.relative_to(R).as_posix()
 if rel not in assets:
  with Image.open(p) as im:im.load();dim=im.size
  assets[rel]={'path':rel,'sha256':sha(p),'dimensions':dim,'bytes':p.stat().st_size,'references':[]}
 assets[rel]['references'].append({'path':x['file'],'line':x['line']})
fix=read('B668资源修订.json');assert assets[fix['asset']]['sha256']==fix['after_sha256']
(O/'B676资源清单.json').write_text(json.dumps({'batch':'B676','image_references':a['image_references'],'unique_assets':len(assets),'assets':list(assets.values()),'scope':'当前引用图像可解码、尺寸与摘要；不是每个公式裁图语义认证'},ensure_ascii=False,indent=2),encoding='utf-8')
# Check local links in the current management surface as well as reader files.
management=['问题状态汇总.md','全量问题复核明细.md','B675附录与拟合复核.md','B676全书收尾复核.md','跨章约定与合稿规则.md']
files=[O/n for n in management]+[R/'翻译管理/当前进度与续接.md',R/'翻译管理/执行方案.md',R/'合稿准备/使用说明.md']
bad=[];nlinks=0
for p in files:
 s=re.sub(r'\$\$[\s\S]*?\$\$|(?<![\\$])\$(?!\$)(?:\\.|[^$\n])+\$','',p.read_text(encoding='utf-8-sig'))
 for mt in re.finditer(r'!?\[[^\]\n]*\]\(([^\n]*?)\)',s):
  href=mt[1].strip('<>');u=urllib.parse.urlsplit(href)
  if u.scheme or href.startswith('#'):continue
  nlinks+=1
  target=(p.parent/urllib.parse.unquote(u.path)).resolve()
  # The acceptance table is written only after all checks below pass.
  if target==O/'B676验收总表.json':continue
  if not target.exists():bad.append({'file':str(p.relative_to(R)),'href':href})
assert not bad,bad
terms=list(csv.DictReader((R/'翻译管理/术语表.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
assert len(terms)==150 and len(terms[0])==12 and all(None not in t for t in terms)
rows=list(csv.DictReader((R/'翻译管理/章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
assert len(rows)==39 and len(rows[0])==17 and all(None not in t for t in rows)
names=[]
for x in rows:
 p=R/x['现有译文路径'];assert p.stem.startswith(x['编号']+' ')
 first=next(l for l in p.read_text(encoding='utf-8-sig').splitlines() if l.startswith('# '))
 title=re.sub(r'^'+re.escape(x['编号'])+r'\s+','',first.removeprefix('# '))
 if title!=p.stem.split(' ',1)[1]:names.append({'section':x['编号'],'heading':first,'filename':p.stem})
# Some source title variants are intentional; retain the comparison, not auto-rename.
assert {x['section'] for x in names}=={'4.5','4.7','7.2','7.3','7.4'},names
variants=read('术语用法候选.json');forbidden=[v for v in variants if v['term'] in ['菲涅耳','菲涅尔系数','和频发生','和频产生','二阶极化率']]
assert not forbidden,forbidden
browser=read('浏览验收.json');assert len(browser)==11 and sum(x['images'] for x in browser)==327
assert (O/'浏览验收.json').stat().st_mtime>(M/'index.html').stat().st_mtime,'browser evidence predates final build'
assert all(not x['missingImages'] and not x['mathErrors'] and not x['pageOverflow'] for x in browser)
(O/'B676浏览验收.json').write_text(json.dumps({'batch':'B676','pages':browser,'scope':'11个页面全量加载+首屏截图；非全文逐屏视觉重读'},ensure_ascii=False,indent=2),encoding='utf-8')
contact=Image.new('RGB',(4*320,3*285),'#e8e8e8');draw=ImageDraw.Draw(contact)
for i,x in enumerate(browser):
 p=O/x['file'].replace('.html','-首屏.png')
 with Image.open(p) as im:
  im.thumbnail((310,250));left=(i%4)*320+5;top=(i//4)*285+25;contact.paste(im,(left,top))
 draw.text(((i%4)*320+5,(i//4)*285+5),x['file'],fill='black')
contact.save(O/'B676全书首屏总览.png')
sources={'access_date':'2026-10-22','read_sources':[{'url':'https://dlmf.nist.gov/1.17','scope':'δ序列及测试函数意义；未用于证明原稿全部附录'},{'url':'https://wright.chem.wisc.edu/content/optical-nutation','scope':'研究组对拉比循环、周期和频率的区分；其幅度常数不直接移入底本'}],'not_used_as_full_text':[{'url':'https://www.rp-photonics.com/rabi_oscillations.html','reason':'检索命中但正文抓取超时；未以该页全文作证据'}]}
(O/'B675来源记录.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2),encoding='utf-8')
out={'batch':'B676','date':'2026-10-22','scope':'本轮翻译一致性与审阅合稿核查完成；原文未决问题仍保留','sections':39,'source_pages':717,'source_PDF_hash_mismatches':a['source_hash_mismatches'],'math_fragments':m['count'],'math_errors':len(m['errors']),'reader_local_references':a['local_links'],'management_local_references_checked':nlinks,'missing_local_references':bad+a['broken_links'],'image_references':327,'unique_image_assets':len(assets),'all_images_decoded':True,'browser_pages':len(browser),'browser_missing_images':sum(len(x['missingImages']) for x in browser),'browser_page_overflows':sum(x['pageOverflow'] for x in browser),'explicit_unique_anchors':f['unique_anchors'],'missing_anchors':f['missing_explicit_anchors'],'manifest_hash_mismatches':f['manifest_hash_mismatch'],'Q_current_rows':320,'Q_omitted_or_duplicate':0,'retained_source_convention_questions':310,'implemented_process_or_translation_items':8,'user_confirmed_source_correction_items':1,'withdrawn_translator_false_positive_items':1,'unallocated_ids':['Q108','Q109'],'body_and_attachment_E_ids':len(f['body_E_ids']),'new_adopted_source_corrections':0,'term_entries':150,'term_decision_status_counts':dict(collections.Counter(t['译名决定状态'] for t in terms)),'term_candidate_hits_reviewed':len(variants),'forbidden_term_hits':forbidden,'section_filename_heading_differences':names,'independent_fitting_model_derivative_examples':48,'not_claimed':['717页本轮重新逐页目读','全部原式的独立物理证明','原MathCad程序运行验证','全部术语获用户确认','全部图片公式转为可编辑LaTeX','出版印刷版或独立专家审校']}
(O/'B676验收总表.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))

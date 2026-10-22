from pathlib import Path
import json,hashlib,re
from PIL import Image
from pypdf import PdfReader
root=Path(__file__).resolve().parents[2];base=root/'翻译管理/校订记录';chapter=root/'中文版本/第四章 单层膜与多层膜的和频'
asset=root/'中文版本/assets/4.7-p1-diamond-models.png';pixels=Image.open(asset).convert('RGB')
for sec,num in [('4.8',8),('4.9',9)]:
 pdf=root/f'日语原版/Chapter4/chap4-{num}.pdf';matches=[]
 for item in PdfReader(pdf).pages[0].images:
  im=item.image.convert('RGB')
  if im.size==pixels.size and im.tobytes()==pixels.tobytes():matches.append(item.name)
 assert matches,(sec,'shared source image differs')
 (base/sec/'图像来源.json').write_text(json.dumps({'pdf':str(pdf.relative_to(root)),'page':1,'pdf_image_objects':matches,'asset':str(asset.relative_to(root)),'pixel_identical_to_own_pdf_image':True,'width':pixels.width,'height':pixels.height,'asset_sha256':hashlib.sha256(asset.read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf-8')
# 核对当前整节译文与已登记批次拼接完全一致，避免验收后漏合稿。
for sec,a,b in [('4.8',385,401),('4.9',402,415),('4.10',416,420),('4.11',421,422)]:
 text='\n\n'.join((base/sec/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(a,b+1))
 target=next(chapter.glob(sec+' *.md'))
 assert text==target.read_text(encoding='utf-8')
 for n in range(a,b+1):
  r=json.loads((base/sec/f'B{n}验收.json').read_text(encoding='utf-8'))
  assert r['translation_sha256']==hashlib.sha256((base/sec/f'B{n}-本批译文.md').read_text(encoding='utf-8').encode('utf-8')).hexdigest()
syntax=json.loads((base/'第四章当前译文语法.json').read_text(encoding='utf-8'))
assert all(not r['errors'] for r in syntax)
p=base/'第四章最终验收.json';r=json.loads(p.read_text(encoding='utf-8'))
r.update(current_canonical_math=syntax,shared_source_images_verified=True,batch_assembly_identical=True,final_source_issue_status='Q180—Q197保留未决，未采用候选修正')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
doc=root/'翻译管理/第四章完成复核.md';s=doc.read_text(encoding='utf-8')
extra='\n最终一致性复核：4.8—4.11整节文件与已验收批次拼接一致；各批校验值一致；4.8、4.9共享结构图与各自PDF嵌入图逐像素一致。当前4.7—4.11整节共2960个数学片段通过严格语法检查（4.7导读调整后为1209，与其历史分批1212计数口径不同）。\n'
if '最终一致性复核：' not in s:doc.write_text(s+extra,encoding='utf-8')
print('最终一致性通过：批次合稿与验收值匹配；结构图逐像素匹配；当前整节2960数学片段语法通过。')

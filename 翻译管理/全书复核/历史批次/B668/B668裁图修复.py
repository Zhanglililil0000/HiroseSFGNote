from pathlib import Path
import shutil,json,hashlib
import pypdfium2 as pdfium
from PIL import Image
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核'
rel='中文版本/assets/8.1/p7-式12.png';p=R/rel;old=O/'B668修改前'/rel
old.parent.mkdir(parents=True,exist_ok=True)
if not old.exists():shutil.copy2(p,old)
doc=pdfium.PdfDocument(str(R/'日语原版/Chapter8/chap8-1.pdf'))
im=doc[6].render(scale=3.2).to_pil()
im.crop(tuple(round(x*3.2/1.8) for x in [180,1050,950,1245])).save(p)
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
data={'batch':'B668','asset':rel,'source':'日语原版/Chapter8/chap8-1.pdf','PDF_page':7,'scale':3.2,'bbox_at_scale_1_8':[180,1050,950,1245],'before_sha256':sha(old),'after_sha256':sha(p),'dimensions':Image.open(p).size,'reason':'恢复原裁图截断的末行；不改原式内容','historical_manifests':'第八章旧资源清单为当时快照，本修订记录给出现行资源摘要'}
(O/'B668资源修订.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
q=O/'B668新增阅读提示.json';notes=json.loads(q.read_text(encoding='utf-8'));key=next(iter(notes));image='\n\n![式12重新裁取，末行完整](../中文版本/assets/8.1/p7-式12.png)'
if image not in notes[key]:notes[key]+=image
q.write_text(json.dumps(notes,ensure_ascii=False,indent=2),encoding='utf-8')
print('crop repaired; revision hash recorded')

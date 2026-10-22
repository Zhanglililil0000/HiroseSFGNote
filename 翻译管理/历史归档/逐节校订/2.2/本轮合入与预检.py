from pathlib import Path
import re,json,hashlib
from PIL import Image,ImageDraw,ImageOps
out=Path(__file__).resolve().parent;root=out.parents[2]
target=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
base=(out/'B069-持续执行前.md').read_text(encoding='utf-8')
prefix=base.split('#### 4.1d.',1)[0]
parts=[(out/f'B{n:03d}-本批译文.md').read_text(encoding='utf-8').strip() for n in range(69,82)]
body=prefix+'\n\n'.join(parts)+'\n'
body=re.sub(r'> \*\*校订进度（2026-10-19）：\*\*[^\n]+', '> **译校状态（2026-10-19）：** 底本47页的正文及附录A—D已补齐中文译文，B058—B081完成本轮页面对照；原式疑点仍有未决项。4.1d以后复杂公式采用底本高清影像，保留全部推导和原编号；可编辑数学转写尚待后续专项处理。',body,count=1)
anchor='## 1. 序论'
policy='''> **公式与插图说明：** 本节混合使用可编辑数学公式与底本公式影像。影像附中文说明、原页码和原编号；跨页长式按顺序续接，不以“略”替代。公式图中附带的日文路径说明已在相邻正文翻译，图内“媒質”译为“介质”。影像是原式的保真保留，不表示原式已获独立代数认证。勘误与候选修正见就地译校注及[勘误附件](../附件/原文勘误表.md)。

'''
body=body.replace(anchor,policy+anchor,1)
target.write_text(body,encoding='utf-8')
manifest=json.loads((out/'公式图索引.json').read_text(encoding='utf-8'))
assets=root/'中文版本/assets/ch02/s02'
# Crop overview: preserve actual crops, no modification of source illustrations.
for start in range(0,len(manifest),15):
    subset=manifest[start:start+15];sheet=Image.new('RGB',(1350,5*360),'#e9e9e9');draw=ImageDraw.Draw(sheet)
    for j,item in enumerate(subset):
        im=Image.open(assets/item['file']).convert('RGB');im.thumbnail((440,325))
        x=(j%3)*450;y=(j//3)*360
        sheet.paste(im,(x,y+25));draw.text((x+3,y+4),item['file'],fill='black')
    sheet.save(out/f'公式图总览{start//15+1}.png')
links=[]
for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)',body):
    if not (target.parent/m[1]).resolve().exists():links.append(m[1])
assert not links,links
assert not re.search(r'@@\d|旧译待校订|4\.1d起仍',body)
assert body.count('$$')%2==0
assert all(body.count(f'#### 5.3{x}.')==1 for x in 'abcde')
assert all(body.count(f'## 附录{x}.')==1 for x in 'ABCD')
assert body.split('#### 4.1d.')[0].split('## 1. 序论')[1]==base.split('#### 4.1d.')[0].split('## 1. 序论')[1]
report={'date':'2026-10-19','source_pages':47,'new_batches':13,'formula_or_figure_crops':len(manifest),'new_pages':list(range(7,48)),'missing_image_links':links,'source_sha256':hashlib.sha256((root/'日语原版/Chapter2/chap2-2.pdf').read_bytes()).hexdigest(),'editable_formula_transcription':'deferred for image formulas','scientific_validation':'unresolved source issues retained'}
(out/'本轮预检.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

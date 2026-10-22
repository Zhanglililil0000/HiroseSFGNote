from pathlib import Path
import re,json,hashlib,sys
from PIL import Image
r=Path(__file__).resolve().parents[3];o=Path(__file__).resolve().parent
dest=r/'中文版本/第六章 偶极间相互作用/6.1 偶极间相互作用.md'
assets=r/'中文版本/assets/6.1';assets.mkdir(parents=True,exist_ok=True)
cuts={
'p23-多重散射展开':(23,(175,634,910,760)),
'p25-偶极链吸收示意':(25,(673,225,894,377)),
'p26-式2.2.6':(26,(182,940,902,1010)),
'p26-辐射场':(26,(182,1100,902,1148)),
'p27-式2.2.9-10':(27,(177,435,905,647)),
'p29-式2.3.4展开':(29,(176,593,907,848)),
'p37-式3.6':(37,(183,185,899,305)),
'p37-式3.7':(37,(183,464,899,555)),
'p37-式3.8':(37,(183,648,899,776)),
'p37-式3.9':(37,(183,848,899,982)),
'p37-式3.10':(37,(183,1082,899,1163)),
'p38-式3.14':(38,(183,614,899,982)),
'p39-式3.18':(39,(183,648,899,915)),
'p41-屏蔽和频式':(41,(183,137,899,332)),
'p41-取向图':(41,(542,580,869,767)),
'p41-相互作用汇总式':(41,(183,960,899,1289)),
'p44-双偶极几何':(44,(606,409,852,569)),
'p45-镜像电荷图1':(45,(191,786,908,1139)),
'p46-极化面电荷图':(46,(614,671,904,1014)),
'p48-镜像方向图':(48,(559,362,878,595)),
'p48-式C.2':(48,(183,670,899,884)),
'p50-膜外电荷':(50,(339,530,698,834)),
'p51-式D.2a':(51,(183,311,899,514)),
'p51-式D.3a':(51,(183,723,899,870)),
'p51-式D.4a上':(51,(183,1055,899,1283)),
'p52-式D.4a下':(52,(183,119,899,173)),
'p52-膜内电荷':(52,(339,417,698,722)),
'p52-式D.5a':(52,(183,866,899,948)),
'p52-式D.6a':(52,(183,1196,899,1281)),
'p53-式D.7a':(53,(183,340,899,478)),
'p54-CPA示意':(54,(201,899,696,1028)),
}
for name,(pn,box) in cuts.items():
 import pypdfium2 as pdf
 doc=pdf.PdfDocument(str(r/'日语原版/Chapter6/chap6-1.pdf'))
 im=doc[pn-1].render(scale=3.4).to_pil();im.crop(tuple(v*2 for v in box)).save(assets/f'{name}.png');doc.close()
for name,pn,boxes in [('p27-式2.2.9-10',27,[(177,448,905,484),(177,562,905,647)]),('p29-式2.3.4展开',29,[(176,605,907,655),(176,734,907,845)])]:
 import pypdfium2 as pdf
 doc=pdf.PdfDocument(str(r/'日语原版/Chapter6/chap6-1.pdf'));im=doc[pn-1].render(scale=3.4).to_pil()
 pieces=[im.crop(tuple(v*2 for v in box)) for box in boxes];canvas=Image.new('RGB',(max(z.width for z in pieces),sum(z.height for z in pieces)+24),'white');y=0
 for z in pieces:canvas.paste(z,(0,y));y+=z.height+24
 canvas.save(assets/f'{name}.png');doc.close()
chunks=sorted(o.glob('B*-本批译文.md'));chunks=[f for f in chunks if int(f.name[1:4])>=570]
sourcehash=hashlib.sha256((r/'日语原版/Chapter6/chap6-1.pdf').read_bytes()).hexdigest()
t=dest.read_text(encoding='utf-8');base=t.split('<!-- 本轮连续译校起点 -->')[0]
base=re.sub(r'\n<!-- B569结束：[\s\S]*?-->\s*$','\n',base)
t=base+'\n<!-- 本轮连续译校起点 -->\n'+ '\n\n'.join(f.read_text(encoding='utf-8') for f in chunks)
dest.write_text(t,encoding='utf-8')
for f in chunks:
 s=f.read_text(encoding='utf-8');bid=f.name[:4];loc=re.search(r'<!-- 原文定位：(.*?) -->',s).group(1)
 blocks=re.split(r'\n\s*\n',s);units=[]
 for b in blocks:
  if not b.strip() or b.startswith('<!--'):continue
  units.append({'原文定位':loc,'译文块序号':len(units)+1,'内容开头':b[:110],'已起草':True,'已原页对照':True})
 a={'批次':bid,'范围':loc,'source_sha256':sourcehash,'translation_sha256':hashlib.sha256(s.encode()).hexdigest(),'覆盖块':len(units),'公式编号':re.findall(r'\\tag\{([^}]+)\}',s),'原式图数':len(re.findall(r'!\[',s)),'疑点':sorted(set(re.findall(r'Q\d+',s))),'已原页对照':True,'已排版':False,'采用原文修正':False}
 (o/f'{bid}-覆盖.json').write_text(json.dumps(units,ensure_ascii=False,indent=2),encoding='utf-8')
 ap=o/f'{bid}验收.json'
 if not ap.exists():ap.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
print('已合入',len(chunks),'批；排版验收另行进行。')

from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[3]
out=root/'中文版本/assets/ch02'
out.mkdir(parents=True,exist_ok=True)
d=pdfium.PdfDocument(str(root/'日语原版/Chapter2/chap2-1.pdf'))
for page,box,name in [(2,(.13,.575,.87,.756),'ch02-s01-fig21'),(3,(.10,.075,.90,.925),'ch02-s01-fig22a'),(4,(.11,.085,.90,.305),'ch02-s01-fig22b')]:
    im=d[page-1].render(scale=2.3).to_pil();w,h=im.size
    im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(out/(name+'.png'))
for page,box,name in [(5,(.13,.38,.91,.77),'式2.7底本'),(2,(.17,.76,.86,.80),'传播因子底本')]:
    im=d[page-1].render(scale=3).to_pil();w,h=im.size
    im.crop(tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(Path(__file__).parent/(name+'.png'))

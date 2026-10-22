from pathlib import Path
import re,json
import pypdfium2 as pdfium
out=Path(__file__).resolve().parent
root=out.parents[2]
assets=root/'中文版本/assets/ch02/s02';assets.mkdir(parents=True,exist_ok=True)
doc=pdfium.PdfDocument(str(root/'日语原版/Chapter2/chap2-2.pdf'))
manifest=[]
for draft in sorted(out.glob('B0[6-9][0-9]-本批译文.草稿.md')):
    count=[0]
    def crop(m):
        count[0]+=1;p=int(m[1]);a=float(m[2]);b=float(m[3]);label=m[4]
        name=f'{draft.name[:4]}-p{p:02d}-{count[0]:02d}.png'
        im=doc[p-1].render(scale=3).to_pil();w,h=im.size
        # Add room for tall fractions/superscripts, then move cut edges to white rows.
        left,right=int(w*.10),int(w*.925)
        top=max(0,int(h*(a-.008)));bottom=min(h,int(h*(b+.008)))
        gray=im.convert('L')
        def blank(y):return gray.crop((left,y,right,y+1)).getextrema()[0]>240
        for _ in range(int(h*.025)):
            if top<2 or all(blank(top-j) for j in range(3)):break
            top-=1
        for _ in range(int(h*.025)):
            if bottom>h-3 or all(blank(bottom+j) for j in range(3)):break
            bottom+=1
        im.crop((left,top,right,bottom)).save(assets/name)
        manifest.append({'batch':draft.name[:4],'page':p,'y':[a,b],'actual_y':[top/h,bottom/h],'file':name,'caption':label})
        return f'![{label}](../assets/ch02/s02/{name})\n\n*{label}（底本p{p}，公式影像）。*'
    s=re.sub(r'@@(\d+),([.\d]+),([.\d]+),([^@]+)@@',crop,draft.read_text(encoding='utf-8'))
    (out/draft.name.replace('.草稿','')).write_text(s,encoding='utf-8')
(out/'公式图索引.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(manifest),'formula blocks')

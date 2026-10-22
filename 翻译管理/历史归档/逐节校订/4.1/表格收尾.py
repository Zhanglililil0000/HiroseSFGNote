from 整节工具 import *
for n in [267,268,269]:
    fp=p/f'B{n}-本批译文.md'; s=fp.read_text(encoding='utf-8')
    lines=s.splitlines(); out=[]; i=0
    while i<len(lines):
        if lines[i].startswith('| $r$') and i+1<len(lines) and lines[i+1].startswith('|---'):
            hdr=[x.strip() for x in lines[i].strip('|').split('|')]; step={4:2,6:3,10:5}[len(hdr)]
            rows=[]; i+=2
            while i<len(lines) and lines[i].startswith('|'):
                rows.append([x.strip() for x in lines[i].strip('|').split('|')]); i+=1
            flat=[]
            for k in range(0,len(hdr),step):
                for row in rows:
                    vals=row[k:k+step]
                    if any(vals):flat.append(vals)
            out.extend(['| '+' | '.join(hdr[:step])+' |','|'+'---|'*step]+['| '+' | '.join(r)+' |' for r in flat])
        else:out.append(lines[i]); i+=1
    fp.write_text('\n'.join(out)+'\n',encoding='utf-8')
base=target.read_text(encoding='utf-8'); head=base[:base.index('#### 反对称伸缩振动：$b_1$模式')]
target.write_text(head+'\n\n'.join((p/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(251,277)),encoding='utf-8')
print('四组参数数表表头和窄列重排已核')

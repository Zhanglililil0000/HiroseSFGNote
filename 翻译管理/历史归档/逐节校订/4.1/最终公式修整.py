from 整节工具 import *
def change(n,fn):
    f=p/f'B{n}-本批译文.md'; f.write_text(fn(f.read_text(encoding='utf-8')),encoding='utf-8')
change(255,lambda s:s.replace(r'Q_{\mathrm{deg},b}]] \tag{1.13}',r'Q_{\mathrm{deg},b}]\bigr\} \tag{1.13}'))
change(256,lambda s:s.replace(r'\partial\alpha',r'd\alpha').replace(r'/\partial r',r'/dr'))
def p18(s):
    s=s.replace(r'\partial\alpha',r'd\alpha').replace(r'/\partial r',r'/dr')
    return s.replace(',\\quad\nP_',',\\\\\nP_')
change(257,p18)
def mat(s):
    s=s.replace('(x, \\eta, z)','(\\xi, \\eta, \\zeta)')
    def fit(m):
        t=m.group(1)
        if '\\tag{1.30b}' not in t and '\\tag{1.30c}' not in t:return m.group(0)
        # 将记号、矩阵之积与展开矩阵分别成行，不改变因子。
        t=t.replace('=\n','\\\\\n&=\n').replace(':\\quad',':\\quad\\\\\n&')
        return '$$\n\\begin{aligned}\n&'+t.strip()+'\n\\end{aligned}\n$$'
    return re.sub(r'\$\$([\s\S]*?)\$\$',fit,s)
change(259,mat)
# 将原分栏数表改为较窄连续表，仅改变列的排列顺序。
for n in [267,268,269]:
    def flatten(s):
        def convert(m):
            lines=m.group(0).strip().splitlines(); header=[x.strip() for x in lines[0].strip('|').split('|')]
            width={4:2,6:3,10:5}.get(len(header))
            if not width:return m.group(0)
            rows=[[x.strip() for x in l.strip('|').split('|')] for l in lines[2:]]
            flat=[]
            for k in range(0,len(header),width):
                flat.extend(row[k:k+width] for row in rows if any(row[k:k+width]))
            return '| '+' | '.join(header[:width])+' |\n|'+'---|'*width+'\n'+'\n'.join('| '+' | '.join(row)+' |' for row in flat)+'\n'
        return re.sub(r'(?m)^\|[^\n]*\n\|(?:\s*:?[-]+:?\s*\|)+\n(?:\|[^\n]*\n)+',convert,s)
    change(n,flatten)
# 汇合最终片段；已有原目录头与已验收B249/250不重写。
base=target.read_text(encoding='utf-8'); head=base[:base.index('#### 反对称伸缩振动：$b_1$模式')]
target.write_text(head+'\n\n'.join((p/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(251,277)),encoding='utf-8')
print('三处长式分行、希腊坐标与数表列宽整理完成')

from pathlib import Path
import re,json,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2]
TARGET=next((ROOT/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
def F(a,b):return r'\frac{'+a+'}{'+b+'}'
def X(a):return r'\exp\!\left['+a+r'\right]'
def W(a):return r'\left('+a+r'\right)'
def math(a,tag=None):return '$$\n'+a+(r'\tag{'+tag+'}' if tag else '')+'\n$$\n'
def al(*lines):return r'\begin{aligned}'+'\n'+('\\\\\n'.join(lines))+'\n'+r'\end{aligned}'
def r(ij,w='',a=''):return 'r_{'+ij+(','+w if w else '')+(','+a if a else '')+'}'
def t(ij,w='',a=''):return 't_{'+ij+(','+w if w else '')+(','+a if a else '')+'}'
def L(ij,s,a,sg='-'):return 'L^{'+sg+'}_{'+ij+','+s+','+a+'}'
def P(a,z):return 'P_{'+a+'}('+z+')'
def E(m,s,z,sg='-'):return 'E^{'+sg+'}_{'+m+','+s+'}('+z+')'
def n(m):return 'n_{'+m+r',\mathrm{SF}}'
def th(m):return r'\theta_{'+m+r',\mathrm{SF}}'
def co(m):return r'\cos'+th(m)
def si(m):return r'\sin'+th(m)
def b(w):return r'\beta_{m,\mathrm{'+w+'}}'
def phase(w,c='2'):return 'e^{'+c+'i'+b(w)+'h_m}'
def D(w,a):return W('1+'+r('1m',w,a)+r('m2',w,a)+phase(w))
JOBS=[]
def job(bid,title,mapping):JOBS.append((bid,title,mapping))
def apply():
    text=TARGET.read_text(encoding='utf-8');original=text;done=[]
    manifest={x['file']:x for x in json.loads((OUT/'公式图索引.json').read_text(encoding='utf-8'))}
    for bid,title,mapping in JOBS:
        changes=[]
        for img,new in mapping.items():
            pattern=r'!\[[^\n]*\]\(\.\./assets/ch02/s02/'+re.escape(img)+r'\)\s*\n\*[^\n]*\*\n*'
            hit=re.search(pattern,text)
            if hit:
                changes.append((img,hit.group(),new));text=text[:hit.start()]+new.strip()+'\n\n'+text[hit.end():]
            else:assert new.strip() in text,(bid,img,'not found / changed since generation')
        if not changes:continue
        before=OUT/f'{bid}-修订前.md';assert not before.exists(),bid
        before.write_text(original,encoding='utf-8')
        fragment='\n\n'.join(v.strip() for v in mapping.values())+'\n';(OUT/f'{bid}-本批译文.md').write_text(fragment,encoding='utf-8')
        (OUT/f'{bid}-原式图对照.md').write_text('# '+bid+'原式对照\n\n'+''.join(o for _,o,_ in changes),encoding='utf-8')
        labels=re.findall(r'\\tag\{([^}]+)\}',fragment)
        rows=''.join(f"| p{manifest[img]['page']} | {manifest[img]['caption']} | 数学转写，逐项原图对照 |\n" for img,_,_ in changes)
        (OUT/f'{bid}.md').write_text(f'# {bid}：{title}\n\n2026-10-19；底本2.2，源SHA256沿原登记。\n\n| 原文位置 | 对象 | 处理 |\n|---|---|---|\n'+rows+'\n仅排版断行；代码格式辅助函数在输出中完全展开，不新增物理简记。原有疑点/异常符号按底本保留，另作就地说明；无未记录的原式纠正。原图、原编号及修订前记录保留。显示与范围验收见收尾验收记录。\n',encoding='utf-8')
        (OUT/f'{bid}-覆盖.json').write_text(json.dumps({'batch':bid,'title':title,'source_images':[i for i,_,_ in changes],'labels':labels,'pages':sorted({manifest[i]['page'] for i,_,_ in changes})},ensure_ascii=False,indent=2),encoding='utf-8')
        done.append(bid)
    if done:
        TARGET.write_text(text,encoding='utf-8')
        p=ROOT/'翻译管理/当前进度与续接.md';s=p.read_text(encoding='utf-8')
        s=re.sub(r'## 2\.2持续收尾执行中\n[\s\S]*?(?=\n## |\Z)','',s,count=1)
        entry='## 2.2持续收尾执行中\n\n用户要求完成本节全部处理，当前连续执行至'+done[-1]+'。本轮批次见校订记录/2.2对应记录；尚未宣告整节收尾完成，待全部公式、附录及整节验收。原图保留作对照，不运行旧全节重建脚本。\n\n'
        p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
    print('Applied',done)

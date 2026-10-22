from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B015-修订前.md');a=s.index('$$',s.index('**（三阶极化－2'));b=s.index('$$',a+2)+2;old=s[a:b];(o/'式14-旧译候选.txt').write_text(old,encoding='utf-8');groups=old.split(r'\Bigg\{',1)[1].split(r'\Bigg]');assert len(groups)==7
clean=lambda t:re.sub(r'\s+',' ',t.replace(r'\\','').replace('&','').replace(r'\quad','').replace(r'\times','')).strip()
L=[r'\begin{aligned}',r'\chi^{(3)}_{ijkl}(\omega_0=\omega_1+\omega_2+\omega_3)',r'&=\frac{P_i^{(3)}(\omega_0=\omega_1+\omega_2+\omega_3)}{E_j(\omega_1)E_k(\omega_2)E_l(\omega_3)}\\[8pt]',r'&=-N\frac{e^4}{\hbar^3}\sum_{g,n,n\prime,n\prime\prime}\Biggl\{\\[8pt]'];drafts={}
for ix,g in enumerate(groups[:6]):
 x,y=g.split(r'\Bigg[',1);ext=clean(x[x.index(r'\frac'):]);parts=y.split(r'\right]');assert len(parts)==5
 rows=[r'&\quad '+('+' if ix else '')+ext+r'\\[6pt]']
 for j,c in enumerate(parts[:4]):
  t=clean(c[c.index(r'\frac'):])+r'\right]';lead=r'\times\Biggl[' if j==0 else '+'
  rows.append(r'&\qquad '+lead+t+(r'\Biggr]' if j==3 else '')+r'\\[8pt]')
 drafts[ix]=rows;L+=rows
L += [r'&\Biggr\}',r'\end{aligned}',r'\tag{14}'];formula='$$\n'+'\n'.join(L)+'\n$$';assert formula.count(r'\frac')==80
# Formula group4 source has an extra additive bracket; normalized explicitly without changing sums.
note='> **排版说明：** 原文部分加项另加方括号，本式统一按“六主组、每组四子项”的层次排写；各子项内的差项括号保留，加项次序及符号不变。\n\n'
s=s[:a]+formula+'\n\n'+note+s[b:].lstrip('\n');s=s.replace('**（三阶极化－2：三波长光引起的四波混合）**','**（三阶极化－2：三波长光引起的四波混频）**');p.write_text(s,encoding='utf-8')
for id,indices in [('B015',[0,1,2]),('B016',[3,4,5])]:
 text=f'# {id}：式（14）'+('前三' if id=='B015' else '后三')+'主组\n\n每组4子项，本稿仅为分组排版检查；不包含整式公共因子。\n\n'
 for ix in indices:text+=f'## 第{ix+1}组\n\n$$\n'+r'\begin{aligned}'+'\n'+('\n'.join(drafts[ix]).replace('&\\quad +','&\\quad ',1))+'\n'+r'\end{aligned}'+'\n$$\n\n'
 (o/f'{id}-本批译文.md').write_text(text,encoding='utf-8')
(o/'B016-式14整式.md').write_text('# 式（14）整式\n\n'+formula+'\n\n'+note,encoding='utf-8')
for id,page,scope in [('B015',9,'定义及第1—3主组'),('B016',10,'第4—6主组及整式合并')]:
 (o/f'{id}.md').write_text(f'''# {id} 校订记录

2026-10-16。范围：PDF p{page}，式14{scope}。本批3组12子项、39个分式，逐项对照矩阵元次序、态指标、频率、iΓ符号及括号；未发现旧译实质符号差异。p9指标特写确认第二组第三子项B分子为r_i，与旧译一致，不登记猜测的r_l。

整式输出ω₀=ω₁+ω₂+ω₃，输入E_j(ω₁)E_k(ω₂)E_l(ω₃)，公共−Ne⁴/ℏ³及g/n/n′/n″求和，24子项、80分式（含定义和公共因子）。原文附加的加法方括号统一层次排写，已在正文说明；差项括号和正负号未改，无另补ρ。前三组与后三组分批对照后才合并；分组稿留存供渲染。

证据：B015-式14前三组原文.png、B016-式14后三组原文.png及B015-指标特写.png。下一批B017处理p10末式14后说明及p11分子取向段，按完整段落划界。
''',encoding='utf-8')
print('B015 and B016: separately checked 3 groups each, 24 children assembled, equation14 replaced.')

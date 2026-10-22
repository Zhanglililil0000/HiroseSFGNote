from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');assert not (o/'B013-修订前.md').exists();shutil.copy2(p,o/'B013-修订前.md')
old=(o/'式13-旧译候选.txt').read_text(encoding='utf-8');groups=old.split(r'\Bigg\{',1)[1].split(r'\Bigg]');assert len(groups)==7
clean=lambda t:re.sub(r'\s+',' ',t.replace(r'\\','').replace('&','').replace(r'\quad','').replace(r'\times','')).strip()
lines=[r'\begin{aligned}',r'\chi^{(3)}_{ijkl}(\omega=2\omega_1-\omega_2)',r'&=\frac{P_i^{(3)}(\omega=2\omega_1-\omega_2)}{E_j(\omega_1)E_k(\omega_1)E_l(-\omega_2)}\\[8pt]',r'&=-N\frac{e^4}{\hbar^3}\sum_{g,n,n\prime,n\prime\prime}\Biggl\{\\[8pt]']
for ix,g in enumerate(groups[:6]):
 a,b=g.split(r'\Bigg[',1);ext=clean(a[a.index(r'\frac'):]);parts=b.split(r'\right]');assert len(parts)==5
 lines.append(r'&\quad '+('+' if ix else '')+ext+r'\\[6pt]')
 for j,c in enumerate(parts[:4]):
  t=clean(c[c.index(r'\frac'):])+r'\right]';lead=r'\times\Biggl[' if j==0 else '+'
  if ix in [4,5] and j==2:lead+=r'\Bigl['
  end=(r'\Bigr]' if ix in [4,5] and j==3 else '')+(r'\Biggr]' if j==3 else '')
  lines.append(r'&\qquad '+lead+t+end+r'\\[8pt]')
lines += [r'&\Biggr\}',r'\end{aligned}',r'\tag{13}'];formula='$$\n'+'\n'.join(lines)+'\n$$';assert formula.count(r'\frac')==80
notes=r'''> **译者注（Q016）：** 第1主组第3子项中间分母的ω、Γ下标字形异常。正文暂保留旧译的 $n n\prime$；B011工作稿曾拟读为 $n n\prime\prime$，该拟读尚未确定，未据此修改正文。

> **译者注（Q017）：** 第1主组第4子项中间分母的 $\omega_1+\omega_2$ 为原文写法，此处照录，未改成差频组合。

> **译者注（Q018）：** 第5主组有两处底本排印疑点：第3子项内B项分母可见 $2\omega_1-\omega+i\Gamma_{ng}$，频率项的下标及后续项不完整；第4子项内A项分母的 $\omega_2$ 与 $\omega_{n n\prime}$ 之间未见运算符。正文这两处暂保留旧译候选 $2\omega_1-\omega_2+\omega_{ng}+i\Gamma_{ng}$ 和 $2\omega_1-\omega_2-\omega_{n n\prime}+i\Gamma_{n n\prime}$，仅为待核验读法，不视为已确认的原式修正。'''
assert old in s;s=s.replace(old,formula+'\n\n'+notes,1);s=re.sub(r'> \*\*式（13）工作进度：\*\*[^\n]*\n\n','',s)
s=re.sub(r'> \*\*校订状态（2026-10-16）：\*\*[^\n]*','> **校订状态（2026-10-16）：** B001–B013 已完成至第 3 部分式（13）末的页面对照及排版整理（PDF 第 1–8 页相应内容）；Q016、Q018等仍含待核验读法，见译者注。第9页式（13）后的解释段起仍为待校订旧译，整节尚未完成。',s,count=1);p.write_text(s,encoding='utf-8')
(o/'B013-式13整理稿.md').write_text('# B013：式（13）整式整理稿\n\n> 六组均已页面对照；Q016/Q017/Q018未决，含明确注明的旧译候选，非无疑点定稿。\n\n'+formula+'\n\n'+notes+'\n',encoding='utf-8')
p=m/'排版工具/检查译文.cjs';s=p.read_text(encoding='utf-8').replace(" const exe=["," if(process.argv.includes('--b013')) {sections.length=0;sections.push(['B013',fs.readFileSync(path.join(out,'B013-式13整理稿.md'),'utf8')]);}\n const exe=[");p.write_text(s,encoding='utf-8')
print('Eq13 assembled: 6 groups/24 children; original extra brackets restored in groups5/6; unresolved readings explicitly annotated.')

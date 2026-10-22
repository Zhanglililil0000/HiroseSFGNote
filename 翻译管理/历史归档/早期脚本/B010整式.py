from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md'
s=p.read_text(encoding='utf-8');backup=o/'B010-修订前.md';assert not backup.exists();shutil.copy2(p,backup)
old=(o/'式12-旧译候选.txt').read_text(encoding='utf-8');groups=old.split(r'\Bigg\{',1)[1].split(r'\Bigg]');assert len(groups)==7
clean=lambda t:re.sub(r'\s+',' ',t.replace(r'\\','').replace('&','').replace(r'\quad','').replace(r'\times','')).strip()
lines=[r'\begin{aligned}',r'\chi^{(3)}_{ijkl}(\omega=2\omega_1+\omega_2)',r'&=\frac{P_i^{(3)}(\omega=2\omega_1+\omega_2)}{E_j(\omega_1)E_k(\omega_1)E_l(\omega_2)}\\[8pt]',r'&=-N\frac{e^4}{\hbar^3}\sum_{g,n,n\prime,n\prime\prime}\Biggl\{\\[8pt]']
for ix,g in enumerate(groups[:6]):
 a,b=g.split(r'\Bigg[',1);ext=clean(a[a.index(r'\frac'):]);parts=b.split(r'\right]');assert len(parts)==5
 lines.append(r'&\quad '+('+' if ix else '')+ext+r'\\[6pt]')
 for j,c in enumerate(parts[:4]):
  t=clean(c[c.index(r'\frac'):])+r'\right]'
  lead=r'\times\Biggl[' if j==0 else '+'
  if ix==5 and j==2:lead+=r'\Bigl['
  end=(r'\Bigr]' if ix==5 and j==3 else '')+(r'\Biggr]' if j==3 else '')
  lines.append(r'&\qquad '+lead+t+end+r'\\[8pt]')
lines += [r'&\Biggr\}',r'\end{aligned}',r'\tag{12}']
formula='**（三阶极化－1：双波长光引起的四波混频）**\n\n$$\n'+'\n'.join(lines)+'\n$$\n\n'
assert formula.count(r'\frac')==80 # 78 group fractions + field ratio + common e4/hbar3
assert old.strip() in s
s=s.replace(old.strip(),formula.strip(),1)
s=re.sub(r'> \*\*式（12）工作进度：\*\*[^\n]*\n\n','',s)
s=re.sub(r'> \*\*校订状态（2026-10-16）：\*\*[^\n]*','> **校订状态（2026-10-16）：** B001–B010 已对照校订至第 3 部分式（12）末（PDF 第 1–7 页相应内容）。式（13）起仍为待校订旧译；既有原式疑难见翻译管理记录，整节尚未完成。',s,count=1)
p.write_text(s,encoding='utf-8')
(o/'B010-式12定稿.md').write_text('# B010：式（12）完整转录\n\n'+formula,encoding='utf-8')
p=m/'排版工具/检查译文.cjs';t=p.read_text(encoding='utf-8');needle=" const exe=[";t=t.replace(needle," if(process.argv.includes('--b010')) {sections.length=0;sections.push(['B010',fs.readFileSync(path.join(out,'B010-式12定稿.md'),'utf8')]);}\n"+needle);p.write_text(t,encoding='utf-8')
print('Replaced eq12: 6 groups, 24 children, 80 fractions including global coefficient and definition; source extra bracket restored.')

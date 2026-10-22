from pathlib import Path
import re,shutil,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');assert not (o/'B012-修订前.md').exists();shutil.copy2(p,o/'B012-修订前.md')
old=(o/'式13-旧译候选.txt').read_text(encoding='utf-8');groups=old.split(r'\Bigg\{',1)[1].split(r'\Bigg]');assert len(groups)==7
clean=lambda t:re.sub(r'\s+',' ',t.replace(r'\\','').replace('&','').replace(r'\quad','').replace(r'\times','')).strip()
lines=['# B012：式（13）第3、4主组工作稿','','> **本批两组8子项已页面对照；累计4/6组、16/24子项。Q016/Q017仍未决，第5、6组及整式未完成，不能视为正式定稿。**','','来源：PDF p8上半。T₃、T₄仅为管理标识，不是作者符号；两式不含整式公共系数−Ne⁴/ℏ³及四重求和。','']
for ix in [2,3]:
 prefix,inner=groups[ix].split(r'\Bigg[',1);ext=clean(prefix[prefix.index(r'\frac'):]);chunks=inner.split(r'\right]');assert len(chunks)==5
 lines += [f'## 第{ix+1}主组','', '$$',r'\begin{aligned}',f'T_{ix+1}={{}}&'+ext+r'\\[6pt]']
 for j,c in enumerate(chunks[:4]):
  term=clean(c[c.index(r'\frac'):])+r'\right]'
  lines.append(r'&\quad '+(r'\times\Biggl[' if j==0 else '+')+term+(r'\Biggr]' if j==3 else '')+(r'\\[8pt]' if j<3 else ''))
 lines += [r'\end{aligned}','$$','']
lines+=['## 核对结论与续接','','两组各4子项相加，内括号为A−B；26个组内分式的iΓ均为正。矩阵元指标、频率下标及次序与底本一致，本批未发现旧译实质符号差异，未新增疑难。','','第3、4组第1/3子项内A项分母为2ω₁−ω₂−ω_n″g+iΓ_n″g，B项为2ω₁−ω₂−ω_n′n″+iΓ_n′n″；第2/4子项内A项为2ω₁−ω₂−ω_nn′+iΓ_nn′，B项为2ω₁−ω₂−ω_n′n″+iΓ_n′n″。不可将这两类顺序混淆。','','下一批B013核p8下半第5、6组，再合并整式检查；Q016拟读和Q017原文正号必须显式保留处理状态。','']
draft='\n'.join(lines);assert draft.count(r'\frac')==26;(o/'B012-式13工作稿.md').write_text(draft,encoding='utf-8')
s=re.sub(r'> \*\*式（13）工作进度：\*\*[^\n]*','> **式（13）工作进度：** B011–B012已对照定义及前4主组（16/24子项），Q016下标暂拟读、Q017保留原文正号；第5、6组及整式检查未完，正文旧式暂未替换。',s,count=1);p.write_text(s,encoding='utf-8')
p=m/'排版工具/检查译文.cjs';t=p.read_text(encoding='utf-8').replace(" const exe=["," if(process.argv.includes('--b012')) {sections.length=0;sections.push(['B012',fs.readFileSync(path.join(out,'B012-式13工作稿.md'),'utf8')]);}\n const exe=[");p.write_text(t,encoding='utf-8')
# Scope guard: only the progress notice may differ in the formal translation.
strip=lambda x:re.sub(r'> \*\*式（13）工作进度：\*\*[^\n]*','',x)
assert strip(s)==strip((o/'B012-修订前.md').read_text(encoding='utf-8'))
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
print('B012: 2 groups/8 children/26 fractions; formal equation unchanged, source hash unchanged.')

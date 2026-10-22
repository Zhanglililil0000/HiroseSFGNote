from pathlib import Path
import re,shutil
r=Path('HiroseSFGNote').resolve();o=r/'翻译管理/校订记录/1.1';old=(o/'式12-旧译候选.txt').read_text(encoding='utf-8');body=old.split(r'\Bigg\{',1)[1].split(r'\Bigg]');assert len(body)==7
out=['# B009：式（12）第2—4主组核对工作稿','','> **状态：第2—4主组已对照。加上B008的第1组，当前共4/6主组；第5、6组及整式检查尚未完成，不能作为正式译文。**','','T₂、T₃、T₄仅为工作标识，原文没有这些符号；各式均不包含整式公共系数−Ne⁴/ℏ³与求和。来源：1.1 PDF p6前3个主组。','']
def clean(s):
 s=s.replace(r'\\','').replace('&','').replace(r'\quad','').replace(r'\times','')
 return re.sub(r'\s+',' ',s).strip()
for ix in [1,2,3]:
 prefix,inner=body[ix].split(r'\Bigg[',1);external=clean(prefix[prefix.index(r'\frac'):])
 chunks=inner.split(r'\right]');assert len(chunks)==5,(ix,len(chunks));terms=[]
 for c in chunks[:4]:
  assert r'\left[' in c
  terms.append(clean(c[c.index(r'\frac'):])+r'\right]')
 label=ix+1
 out += [f'## 第{label}主组','', '$$',r'\begin{aligned}',f'T_{label}={{}}&'+external,r'\left[',r'\begin{aligned}']
 for k,t in enumerate(terms):out += ['&'+('+' if k else '')+t+(r'\\[8pt]' if k<3 else '')]
 out += [r'\end{aligned}',r'\right].',r'\end{aligned}','$$','']
out+=['## 核对与续接','','每组4个子项相加，每个内括号为A−B；三组共12子项、39个分母，iΓ均为正。矩阵元次序及频率下标按页面保留，本批未发现旧译这些主组的实质符号差异。','','第5主组从p6末的 $(r_j)_{gn\prime\prime}/(\omega_1+\omega_{n\prime\prime g}+i\Gamma_{n\prime\prime g})$ 开始，第6组位于p7首，均留待B010。正式正文式（12）尚未替换。','']
p=o/'B009-式12工作稿.md';assert not p.exists();p.write_text('\n'.join(out),encoding='utf-8')
p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B009-修订前.md');s=s.replace('B008已核对定义及第1主组','B008–B009已核对定义及第1–4主组，第5、6组和整式检查未完');p.write_text(s,encoding='utf-8')
print('B009: groups 2–4 working draft added; source candidate indices preserved; formal formula unchanged.')

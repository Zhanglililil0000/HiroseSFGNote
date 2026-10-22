from pathlib import Path
import csv, hashlib, shutil, re, json, subprocess
from urllib.parse import quote
root=Path('HiroseSFGNote').resolve(); m=root/'翻译管理'; baseline=m/'基线快照'/'2026-10-16'
for name in ['中文版本','日语原版']:
    target=baseline/name
    if not target.exists(): shutil.copytree(root/name,target)
if not (baseline/'Preface序言.md').exists():
    baseline.mkdir(parents=True,exist_ok=True); shutil.copy2(root/'Preface序言.md',baseline/'Preface序言.md')
chapters=[('SFG早わかり','SFG 快速入门','建立和频光谱、电磁场与共振的基础概念。'),('膜からのSFG','薄膜产生的 SFG','围绕薄膜内外的电场及和频响应展开。'),('二層膜からの和周波','双层膜产生的和频','转向双层膜体系及其一般表达式。'),('CH伸縮振動','CH 伸缩振动','按基团取向与对称性组织张量分量的讨论。'),('テンソル・対称性','张量与对称性','集中阅读张量、对称性、基底和坐标变换。'),('双極子‐双極子相互作用','偶极–偶极相互作用','讨论偶极之间的相互作用。'),('Heinz解読','Heinz 论文解读','结合正文与附录阅读 Heinz 论文的相关推导。'),('フィッティング','拟合','从光谱线形进入光谱分析和拟合。')]
data=[
('SFG 分光入門','SFG 光谱入门','建立 SFG 光谱的基本概念。'),('振動共鳴・フェルミ共鳴','振动共振与费米共振','了解两类共振及其关系。'),('フレネル係数など','菲涅耳系数等','阅读界面光场所需的系数。'),('電気双極子の電場と放射','电偶极子的电场与辐射','回顾偶极电场和辐射。'),('SFGの歴史-95','SFG 的历史（至 1995 年）','了解早期 SFG 研究脉络。'),
('埋込発光層からの電場','埋入发光层产生的电场','从埋入层的电场问题入手。'),('膜からの和周波','薄膜产生的和频','阅读薄膜和频响应。'),('膜からの和周波(付録）','薄膜产生的和频（附录）','配合上一节阅读补充内容。'),('膜からの和周波（表式）','薄膜产生的和频（表达式）','查阅相关表达式。'),('膜からの和周波（要点）','薄膜产生的和频（要点）','回顾本组内容的要点。'),('膜内の電場','膜内的电场','关注薄膜内部电场。'),
('２層膜からの和周波','双层膜产生的和频','阅读双层膜体系。'),('２層膜和周波一般式','双层膜和频的一般式','查阅双层膜响应的一般表达。'),
('CH, CH2, CH3伸縮感受率','CH、CH₂、CH₃ 伸缩振动的电极化率','按基团比较伸缩响应。'),('CH3の配向とテンソル成分','CH₃ 的取向与张量分量','关注 CH₃ 取向和张量。'),('CH2の配向とテンソル成分','CH₂ 的取向与张量分量','关注 CH₂ 取向和张量。'),('CHの配向とテンソル成分','CH 的取向与张量分量','关注 CH 取向和张量。'),('２個のCH3 基のテンソル成分','两个 CH₃ 基团的张量分量','转向含两个 CH₃ 基团的情形。'),('３回対称が崩れたCH3','三重对称性破缺的 CH₃','关注对称性降低的情形。'),('HCCH,C2v,C2対称テンソル','HCCH、C₂ᵥ、C₂ 对称性张量','阅读相关对称性下的张量。'),('HCCHSFGテンソル','HCCH 的 SFG 张量','查阅 HCCH 和频张量。'),('HCCHSFGテンソル要点','HCCH 的 SFG 张量要点','回顾相关张量要点。'),('HCCHのオイラー角','HCCH 的欧拉角','关注欧拉角约定。'),('HCCH表面の回転','HCCH 在表面的旋转','关注表面旋转问题。'),
('SFGテンソルと対称性','SFG 张量与对称性','联系张量分量与对称性。'),('基底とキャラクターテーブル','基底与特征标表','阅读基底和特征标表。'),('分子固定から空間固定へ','从分子固定坐标系到空间固定坐标系','阅读坐标系间的变换。'),('基底テンソル','基底张量','了解基底张量。'),('変換行列(基底)','变换矩阵（基底）','查阅基底变换矩阵。'),('変換行列(xyz)','变换矩阵（xyz）','查阅 xyz 表示下的变换矩阵。'),
('双極子間相互作用','偶极间相互作用','阅读偶极相互作用问题。'),
('Heinz論文の解読','Heinz 论文解读','进入论文解读正文。'),('付録A','附录 A','配合正文查阅；具体主题待正文核验。'),('付録B','附录 B','配合正文查阅；具体主题待正文核验。'),('付録C','附录 C','配合正文查阅；具体主题待正文核验。'),('付録D','附录 D','配合正文查阅；具体主题待正文核验。'),
('SFGのスペクトル形','SFG 的光谱线形','关注 SFG 光谱的线形。'),('SFGスペクトル解析便覧','SFG 光谱分析便览','作为光谱分析的查阅入口。'),('フィッティング概説','拟合概述','了解拟合的总体思路。')]
counts=[5,6,2,11,6,1,5,3]; rows=[]; idx=0
for c,n in enumerate(counts,1):
 for s in range(1,n+1):
  ja,zh,summary=data[idx]; idx+=1; sid=f'{c}.{s}'
  pdfs=list((root/'日语原版'/f'Chapter{c}').glob(f'chap{c}-{s}Japanese.pdf' if c==1 else f'chap{c}-{s}.pdf')); assert len(pdfs)==1
  pdf=pdfs[0]; translations=[p for p in (root/'中文版本').rglob('*.md') if p.name.startswith(sid+' ')]
  assert len(translations)<=1
  result=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,encoding='utf-8',errors='replace')
  match=re.search(r'^Pages:\s+(\d+)',result.stdout,re.M); pages=match.group(1) if match else '待核验'
  rows.append(dict(编号=sid,网页日文标题=ja,暂定中文标题=zh,原文路径=pdf.relative_to(root).as_posix(),PDF页数=pages,原文SHA256=hashlib.sha256(pdf.read_bytes()).hexdigest(),现有译文路径=translations[0].relative_to(root).as_posix() if translations else '',状态='旧译待校订' if translations else '待翻译',映射核验='仅文件编号对应；PDF正文待核验',公式图表范围='待逐页登记',导读状态='据网页标题拟定；未核对正文',导读草案=summary))
with (m/'章节清单.tsv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t'); w.writeheader(); w.writerows(rows)
manifest=[]
for p in baseline.rglob('*'):
 if p.is_file(): manifest.append({'path':p.relative_to(baseline).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(m/'基线快照清单.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
preface=root/'Preface序言.md'; original=preface.read_text(encoding='utf-8')
nav=['','---','','# 中文译本阅读导航（准备稿）','','> 本导航由译者编写，不属于作者序言。依据[原网站目录](https://comp.chem.tohoku.ac.jp/study/hirose.html)于 2026-10-16 整理。章名、节名为暂定译名；以下概括仅据目录标题拟定，尚未核对 PDF 正文。链接指向现有旧译，不表示其已通过校订。','','## 阅读方式','','初读可依章顺序阅读；查阅取向与张量问题可从第 4、5 章进入，研究光谱分析可从第 8 章进入并回查相关理论。具体先修关系待正文校订后补充。','','## 全书目录与逐节导读','']
for c,(_,title,summary) in enumerate(chapters,1):
 nav += [f'### 第 {c} 章 {title}', '',f'**本章导读（待正文核验）：** {summary}','']
 for r in rows:
  if r['编号'].split('.')[0]!=str(c): continue
  label=r['编号']+' '+r['暂定中文标题']; path=r['现有译文路径']
  link=f'[{label}]({quote(path,safe="/")})' if path else label
  nav += [f'- {link}（{r["状态"]}）：{r["导读草案"]}']
 nav += ['']
nav += ['## 导读的定稿要求','','每节正文核验后，将标题级概括替换为 1—3 句内容概括，说明研究对象、核心问题和主要结果或用途；列明必要先修节及重要约定。每章概括同时说明各节关系。不得仅凭旧译推断原文内容，附录不得臆造主题。状态和来源位置记录于[章节清单](翻译管理/章节清单.tsv)。','']
assert '# 中文译本阅读导航' not in original
preface.write_text(original.rstrip()+'\n'+'\n'.join(nav),encoding='utf-8')
print(f'已建立 {len(rows)} 节清单；{sum(bool(r["现有译文路径"]) for r in rows)} 节旧译；总计 {sum(int(r["PDF页数"]) for r in rows if r["PDF页数"].isdigit())} 页；快照 {len(manifest)} 个文件。')


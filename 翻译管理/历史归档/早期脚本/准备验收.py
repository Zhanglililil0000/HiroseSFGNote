from pathlib import Path
import csv, re, hashlib, json
from urllib.parse import unquote
root=Path('HiroseSFGNote').resolve(); m=root/'翻译管理'
terms=[
('和周波発生','sum-frequency generation','和频产生（SFG）','和频发生','过程；与光谱测量方法区分'),
('振動和周波分光','vibrational sum-frequency spectroscopy','振动和频光谱','和频振动光谱','方法名称；核对作者实际用词'),
('分極率','polarizability','极化率','','分子量；与宏观 χ 区分'),
('超分極率','hyperpolarizability','超极化率','','核对阶数及 β、γ 的定义'),
('感受率','electric susceptibility','电极化率','极化率；电极化系数','宏观响应；中文名称待全文语境统一'),
('伸縮振動','stretching vibration','伸缩振动','','不能与弯曲振动混用'),
('変角振動','bending vibration','弯曲振动','变角振动','核对原文具体振动模式'),
('配向','orientation','取向','配向','与方位角的含义区分'),
('テンソル','tensor','张量','','阶数不等于矩阵维数'),
('フレネル係数','Fresnel coefficient','菲涅耳系数','菲涅尔系数','中文音译形式需最终统一'),
('フェルミ共鳴','Fermi resonance','费米共振','',''),
('局所場','local field','局域场','局部场','日语具体写法待 PDF 核对'),
('オイラー角','Euler angles','欧拉角','','须另登记旋转顺序和符号约定'),
('キャラクターテーブル','character table','特征标表','','群论语境'),
('基底','basis','基底','','与基态区分'),
('双極子間相互作用','dipole–dipole interaction','偶极–偶极相互作用','',''),
('フィッティング','fitting','拟合','',''),
('スペクトル形','spectral line shape','光谱线形','谱形','英文对应及具体语境待核验')]
with (m/'术语表.tsv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['术语编号','日语候选','英语辅助释义','推荐中文候选','别名或需辨析译法','定义与适用语境','原文位置','依据','状态'])
 for i,(ja,en,zh,alt,note) in enumerate(terms,1):w.writerow([f'T{i:03}',ja,en,zh,alt,note,'待 PDF 核验','准备阶段拟定；英文为译者辅助释义，未确认作者原用词','候选'])
rows=list(csv.DictReader((m/'章节清单.tsv').open(encoding='utf-8-sig'),delimiter='\t'))
assert len(rows)==39 and len({r['编号'] for r in rows})==39
assert sum(bool(r['现有译文路径']) for r in rows)==24
assert sum(int(r['PDF页数']) for r in rows)==717
for r in rows:
 assert (root/r['原文路径']).is_file()
 if r['现有译文路径']:assert (root/r['现有译文路径']).is_file()
preface=(root/'Preface序言.md').read_text(encoding='utf-8')
links=re.findall(r'\]\(([^)]+)\)',preface)
for link in links:
 if not link.startswith(('https:','http:')):assert (root/unquote(link)).exists(),link
snapshot=m/'基线快照'/'2026-10-16'
manifest=json.loads((m/'基线快照清单.json').read_text(encoding='utf-8'))
for item in manifest:
 p=snapshot/item['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256']
 if item['path']!='Preface序言.md':assert (root/item['path']).read_bytes()==p.read_bytes()
original=(snapshot/'Preface序言.md').read_text(encoding='utf-8')
assert preface.startswith(original.rstrip())
(m/'准备验收记录.md').write_text('''# 准备阶段验收记录\n\n日期：2026-10-16。\n\n- 章节清单共 39 条、编号唯一，39 个原文路径均存在。\n- 24 个旧译路径均存在；其余 15 节未建立空译文占位。\n- PDF 元数据累计 717 页；尚未逐页核验内容、图表与公式。\n- Preface 本地导航目标均存在，旧序言内容保留。\n- 基线快照共 67 个文件，摘要全部校验通过；原文及旧译与快照逐字节一致。\n- 候选术语 18 条；已核验语料为空，未将候选标为定稿。\n- 本轮未修改旧译正文，未重命名章节，未提交 Git。\n\n限制：本轮检查为文件清单、哈希和链接目标检查；未做 PDF 正文视觉核验，也未验证完整数学渲染。Preface 概括仍为据网页目录标题拟定的导读草案。\n''',encoding='utf-8')
print('PASS: 39 sections, 717 pages, 24 translations, navigation targets, 67 snapshot hashes and unchanged original/translation content.')

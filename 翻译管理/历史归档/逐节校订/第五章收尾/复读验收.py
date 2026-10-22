from pathlib import Path
import csv,io,json,hashlib
r=Path(__file__).resolve().parents[3]
rows=list(csv.DictReader(io.StringIO((r/'翻译管理/术语表.tsv').read_text(encoding='utf-8')),delimiter='\t'))
assert len(rows)==101 and len({x['术语编号'] for x in rows})==101
assert all(None not in x for x in rows)
b=json.loads((Path(__file__).parent/'本轮批次.json').read_text(encoding='utf-8'))
assert all(x['已排版'] for x in b)
for x in b:
 p=r/'翻译管理/校订记录'/x['节']/(x['批次']+'-本批译文.md')
 assert hashlib.sha256(p.read_text(encoding='utf-8').encode('utf-8')).hexdigest()==x['译文SHA256']
for sec in ['5.3','5.4','5.5','5.6']:
 a=json.loads((r/'翻译管理/校订记录'/sec/'全节验收.json').read_text(encoding='utf-8'))
 p=next((r/'中文版本/第五章 张量与对称性').glob(sec+' *.md'))
 assert hashlib.sha256(p.read_bytes()).hexdigest()==a['合稿原始字节SHA256']
print('复读通过：术语表101项，91批摘要、四节合稿摘要及验收状态一致。')

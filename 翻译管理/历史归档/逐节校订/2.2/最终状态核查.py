from pathlib import Path
import json,re,csv,io,hashlib
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
body=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md')).read_text(encoding='utf-8')
render=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert len(render['results'])==13
assert all(r['scrollWidth']==r['width'] and not r['overs'] and all(i['loaded'] for i in r['images']) for r in render['results'])
assert len(json.loads((out/'全节公式编号索引.json').read_text(encoding='utf-8')))==116
assert len(json.loads((out/'公式图索引.json').read_text(encoding='utf-8')))==132
assert body.count('\n# ')==0
assert not re.search(r'@@\d|旧译待校订|4\.1d起仍',body)
for n in range(69,82):assert (out/f'B{n:03d}-本批译文.md').read_text(encoding='utf-8').strip() in body
terms=list(csv.DictReader(io.StringIO((m/'术语表.tsv').read_text(encoding='utf-8-sig')),delimiter='\t'))
assert len(terms)==90 and len({x['术语编号'] for x in terms})==90
assert all(None not in r and len(r)==12 for r in terms)
chap=list(csv.DictReader(io.StringIO((m/'章节清单.tsv').read_text(encoding='utf-8-sig')),delimiter='\t'))
assert '47页' in next(x for x in chap if x['编号']=='2.2')['状态']
q=(m/'疑难与勘误.md').read_text(encoding='utf-8')
assert all(f'| Q{n:03d} |' in q and f'Q{n:03d}' in body for n in range(44,59))
err=(root/'中文版本/附件/原文勘误表.md').read_text(encoding='utf-8')
assert all(f'E-2.2-00{n}' in err and f'E-2.2-00{n}' in body for n in [4,5])
pdf=root/'日语原版/Chapter2/chap2-2.pdf'
digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert digest=='24c9c3fcfe8b0aad0d5f5fc0a570391b7bed5336320f2800e8be0a2997ed4aad'
baseline=m/'基线快照/2026-10-16/日语原版/Chapter2/chap2-2.pdf'
assert pdf.read_bytes()==baseline.read_bytes()
report={'date':'2026-10-19','translation_pages':47,'batches':'B058—B081','new_batches':13,'numbered_equations':116,'new_image_blocks':132,'math_fragments_syntax_pass':render['math'],'rendered_new_batches':13,'terms':90,'new_questions':'Q044—Q058','new_errata':['E-2.2-004','E-2.2-005'],'source_unchanged':True,'limits':['复杂公式保留影像，可编辑转写尚待专项','原式科学/代数疑点未决','非独立专家审校']}
(out/'最终状态核查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))

from pathlib import Path
import json,re,csv,hashlib
R=Path(__file__).resolve().parents[2]; O=R/'翻译管理/全书复核'; M=R/'合稿准备'
s=(M/'全书审阅稿.md').read_text(encoding='utf-8')
anchors=re.findall(r'<a id="([^"]+)"',s)
fragments=re.findall(r'\]\(#([^)]*)\)',s)
q=(R/'翻译管理/疑难与勘误.md').read_text(encoding='utf-8-sig')
err=(R/'中文版本/附件/原文勘误表.md').read_text(encoding='utf-8-sig')
manifest=json.loads((M/'合稿清单.json').read_text(encoding='utf-8'))
body='\n'.join((R/x['path']).read_text(encoding='utf-8-sig') for x in manifest['sections'])
eref=set(re.findall(r'E-\d+\.\d+-\d{3}',body)); ereg=set(re.findall(r'E-\d+\.\d+-\d{3}',err))
checks={'explicit_anchors':len(anchors),'unique_anchors':len(set(anchors)),'fragment_links':len(fragments),'missing_explicit_anchors':sorted(set(fragments)-set(anchors)),'body_E_ids':sorted(eref),'attachment_E_ids':sorted(ereg),'body_E_not_in_attachment':sorted(eref-ereg),'manifest_hash_mismatch':[],'unchanged_math_in_edited_sections':{}}
for x in manifest['sections']:
 p=R/x['path']; h=hashlib.sha256(p.read_bytes()).hexdigest()
 if h!=x['sha256']:checks['manifest_hash_mismatch'].append(x['section'])
 old=O/'历史批次/B665/B665修改前'/x['path'].replace('第四章 CH伸缩振动与取向张量','第四章 单层膜与多层膜的和频')
 if old.exists():
  pat=r'\$\$[\s\S]*?\$\$|(?<![\\$])\$(?!\$)(?:\\.|[^$\n])+\$'
  checks['unchanged_math_in_edited_sections'][x['section']]=re.findall(pat,old.read_text(encoding='utf-8-sig'))==re.findall(pat,p.read_text(encoding='utf-8-sig'))
checks['question_ids_missing_in_numeric_range']=sorted(set(f'Q{i:03}' for i in range(1,323))-(set(re.findall(r'Q\d{3}',q))-{'Q108','Q109'}))
(O/'收尾核验.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(checks,ensure_ascii=False))

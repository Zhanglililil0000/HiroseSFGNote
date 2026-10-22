from pathlib import Path
import json,re,shutil,csv
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.5';p=r/'中文版本/第一章 SFG快速入门/1.5 SFG光谱的早期工作整理（1983—1995）.md';shutil.copy2(p,o/'B044-修订前.md');old=p.read_text(encoding='utf-8');rows=json.loads((o/'书目提取.json').read_text(encoding='utf-8'));zh=dict(line.split('\t',1) for line in (o/'中文题名对照.tsv').read_text(encoding='utf-8-sig').strip().splitlines());assert set(zh)==set(x['id'] for x in rows) and len(zh)==94
zh['95-2']='利用和频过程监测Pt(111)上双σ键吸附乙烯向 ethylidyne 物种的转化：ethylidene（或乙基）中间体的证据'
# Recover chemical superscripts/subscripts and cross-page title fragments against the viewed source pages.
fix={'85-1':('c (2)','χ⁽²⁾'),'92-2':('1· 1','1×1'),'93-1':('2· 1','2×1'),'95-7':('2· 1','2×1'),'95-2':('Di-s','Di-σ'),'90-8':('C0/Cu','CO/Cu')}
blocks=[]
for x in rows:
 id=x['id'];title=x['title'];review='(review)' in title;title=re.sub(r'"\.?(?:\s*\(review\))?\.?\s*\d*$', '',title).strip('". ')
 if id in fix:title=title.replace(*fix[id])
 if id in ['92-5','93-3']:title=title.replace('ZrO','ZrO₂');title=re.sub(r'"\.\s*2$','',title)
 if id=='93-10':title=title.replace('HCO on','HCO₂ on');title=re.sub(r'"\.\s*2$','',title)
 if id=='94-1':title=title.replace('CH OH','CH₃OH');title=re.sub(r'"\.\s*3$','',title)
 citation=re.sub(r'\s+\.\s*$','',x['citation']).strip()
 if id=='87-2':citation=citation.replace('1444 -1 446','1444 - 1446')
 block=f'### {id}　{zh[id]}'+('〔综述〕' if review else '')+'\n\n'+citation+'\n\n**英文原题：** '+title+'.\n'
 blocks.append((x,block));x['中文题名']=zh[id];x['整理英文题名']=title
intro='''# SFG光谱的早期工作整理（1983—1995）

> **校订状态（2026-10-16）：** B044—B049已按原编号核对12页、94条文献，并补充中文题名；英文题名与书目信息保留，非逐篇论文全文核查。

本节原文是一份英文历史书目。中文题名用于阅读导航，不替代正式引用；正式引用请以作者、期刊及原题为检索依据。保留原编号，不将可能重复项合并。对源书目的拼写、年份或页码疑点，不凭印象改成外部版本。

- pre-VSFG：83-1至87-2，早期共振和频/差频及表面非线性光谱。
- VSFG：87-3至95-15，覆盖单层振动光谱、界面取向、弛豫动力学、电化学、液体界面和金刚石表面。

> **译者注（Q030）：** 原书目含疑似错误或缺项，例如89-1页码“3878—3379”、89-2的“Propertied”、90-4页码“2156—159”、92-4尾页后的短横线、95-2未列终页；本稿保留并记录。95-4与95-15似为同篇但保留两个原编号。95-2的ethylidyne/ethylidene先保留英文精确术语，中文对应待术语专项确认。跨页条目已接回，化学下标和χ⁽²⁾按原页恢复；未作在线书目校勘。

'''
text=intro+'## pre-VSFG：振动和频光谱出现之前\n\n';flag=False
for x,b in blocks:
 if x['id']=='87-3':text+='\n## VSFG：振动和频光谱\n\n'
 text+=b+'\n'
p.write_text(text,encoding='utf-8');(o/'书目提取.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
for k in range(6):
 id=f'B{44+k:03d}';selected=[(x,b) for x,b in blocks if (x['page']-1)//2==k];assert selected
 draft=f'# {id}：1.5书目分批\n\n'+(intro if k==0 else '')+'\n'.join(b for x,b in selected)
 (o/f'{id}-本批译文.md').write_text(draft,encoding='utf-8');ids=[x['id'] for x,b in selected]
 (o/f'{id}.md').write_text(f'''# {id} 校订记录

2026-10-16。原始起页p{2*k+1}—{2*k+2}的条目，跨页条目完整接续至下一页；范围{ids[0]}至{ids[-1]}，共{len(ids)}条。覆盖账本见本目录书目提取.json（原编号、起页、完整英文信息、中文题名）。每条作者/刊物/原题按原页对照，题名中文逐条翻译；六批总94条，不按页末截断作者与题名。

底本拼写与页码疑点Q030保留；85-1的χ⁽²⁾、化学下标及表面2×1等按可见原页恢复；不更正作者姓名或期刊卷页为未核实的外部版本。95-4与95-15均保留。中文题名是译者导读，不冒称论文官方中文名或全文研究结论。

旧表拆成“原编号＋中文题名＋英文书目信息＋原题”的独立条目，避免作者/期刊分行被错归；备份B044-修订前.md。下一步全章一致性与Preface定稿。
''',encoding='utf-8')
oldids=re.findall(r'^\|\s*(\d{2}-\d+)',old,re.M);assert len(oldids)==94 and set(oldids)==set(zh);assert len(re.findall(r'^### \d{2}-\d+',text,re.M))==94
p=m/'疑难与勘误.md';s=p.read_text(encoding='utf-8')+'\n| Q030 | 1.5历史书目 | 89-1/90-4页码、89-2拼写、95-2终页缺失、95-4/95-15疑重复等；95-2术语中文待确认 | 原始书目/P2 | B044—B049保留原始信息并明确记录，94编号完整；跨页已接回，未在线逐篇校勘，不合并疑重复 |\n';p.write_text(s,encoding='utf-8')
print('1.5: 94 original identifiers preserved, 94 Chinese titles added, six batches and page ledger saved.')

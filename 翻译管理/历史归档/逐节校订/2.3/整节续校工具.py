from pathlib import Path
import re,json,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];D=ROOT/'中文版本/第二章 薄膜产生的SFG';TARGET=next(D.glob('2.3 *.md'));M=ROOT/'翻译管理'
SHA='63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384'
def tex(s):return s.replace('§',chr(92))
def put(bid,start,end,new,title,pages,items):
 old=TARGET.read_text(encoding='utf-8');a=old.index(start);b=old.index(end,a) if end else len(old)
 assert not (OUT/(bid+'-修订前.md')).exists()
 assert not any(ord(c)<32 and c not in '\n\r' for c in new)
 assert hashlib.sha256((ROOT/'日语原版/Chapter2/chap2-3.pdf').read_bytes()).hexdigest()==SHA
 (OUT/(bid+'-修订前.md')).write_text(old,encoding='utf-8')
 TARGET.write_text(old[:a]+new.strip()+'\n\n'+old[b:],encoding='utf-8')
 (OUT/(bid+'-本批译文.md')).write_text(new,encoding='utf-8')
 (OUT/(bid+'-覆盖.json')).write_text(json.dumps({'batch':bid,'title':title,'pages':pages,'source_sha256':SHA,'units':items,'labels':re.findall(r'\\tag\{([^}]+)\}',new),'images':re.findall(r'!\[[^\n]*\]\(([^)]+)\)',new)},ensure_ascii=False,indent=2),encoding='utf-8')
 (OUT/(bid+'.md')).write_text('# '+bid+'：'+title+'\n\n2026-10-19。独立底本chap2-3.pdf，SHA256 `'+SHA+'`，PDF p'+str(pages)+'。\n\n'+'\n'.join('- '+x for x in items)+'\n\n先对独立原页及文字层核验，再按已核单元复用母本；细小下标另作局部放大。全部公式可编辑，跨页推导完整合并；不静默改原式。批前快照、范围清单、本批译文、参考渲染分别留存。疑点只注；若采用文字补读，正文与勘误附件同步登记。整节验收另存。\n',encoding='utf-8')
 print('Applied',bid)

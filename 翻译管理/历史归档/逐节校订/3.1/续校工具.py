from pathlib import Path
import re,json,hashlib,ast
R=Path('HiroseSFGNote');M=R/'翻译管理';O=M/'校订记录/3.1';P=R/'中文版本/第三章 双层膜的和频/3.1 二层膜及三层膜产生的和频光.md'
# Reuse only the pure formatting functions, not the earlier mutation script.
tree=ast.parse((O/'完成2.1.py').read_text(encoding='utf-8').replace("x=x[:-1]+r'\\end{aligned}}'", "x=x.rstrip();x=x[:-1]+r'\\end{aligned}}'").replace("assert x.endswith('}')", "assert x.rstrip().endswith('}')"))
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('norm','layout','join_formulas')],type_ignores=[]),'formatters','exec'))
def writebatch(n,text,pages,unit):
 b=f'B{n}';(O/(b+'-本批译文.md')).write_text(text,encoding='utf-8')
 c={'batch':b,'date':'2026-10-20','pages':pages,'units':unit,'tags':re.findall(r'\\tag\{([^}]+)\}',text),'source_formula_corrections_adopted':False,'source_images_visually_checked':True}
 (O/(b+'-覆盖.json')).write_text(json.dumps(c,ensure_ascii=False,indent=2),encoding='utf-8');(O/(b+'.md')).write_text('# '+b+'：3.1续校\n\n2026-10-20；PDF '+str(pages)+'。'+unit+'。原式逐项核对；编号式跨页接全。所有展开项保留，可编辑数学分行，不用截图或省略代替。原文疑点见就地说明，候选未采用。\n',encoding='utf-8')
def note(q,loc,s):return '\n\n> **原文疑点（'+q+'，'+loc+'）：** '+s+'\n\n'
def append(f,s):f.write_text(f.read_text(encoding='utf-8-sig')+'\n\n'+s+'\n',encoding='utf-8')

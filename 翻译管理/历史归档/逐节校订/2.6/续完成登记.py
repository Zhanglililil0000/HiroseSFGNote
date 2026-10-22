from pathlib import Path
p=Path('HiroseSFGNote/翻译管理/校订记录/2.6/完成登记.py')
s=p.read_text(encoding='utf-8')
helper="\ndef append(path,text):\n path.write_text(path.read_text(encoding='utf-8-sig')+'\\n\\n'+text+'\\n',encoding='utf-8')\n"
exec(compile(s[:s.index('s=re.sub')]+helper+s[s.index("convention='"):],str(p),'exec'))

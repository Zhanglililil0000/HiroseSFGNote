exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
s=P.read_text(encoding='utf-8');s=s[s.index('### 2.3 SFG电场'):s.index('**3. 三层')]
print(re.sub(r'\$\$[\s\S]*?\$\$','\n[公式]\n',s))

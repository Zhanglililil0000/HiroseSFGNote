from 收尾公式工具 import *
for p in [TARGET,OUT/'B096-本批译文.md']:
    s=p.read_text(encoding='utf-8');s=s.replace('&\\quad\times',r'&\quad\times');p.write_text(s,encoding='utf-8')

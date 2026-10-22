from pathlib import Path
import shutil
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');shutil.copy2(p,o/'B018-修订前.md');a=s.index('## 5.');b=s.index('## 附录 A',a);t=s[a:b].replace('​\t','').replace('这方面的尝试将在第6章中加以讨论','作者已将这方面的尝试整理在另一个文件夹“dipole-dipole”中')
t=t.replace('## 7. 厚度薄膜中的 SFG 过程','## 7. 有限厚度薄膜中的和频过程').replace('请参考第1章第4节的内容。','请参考作者的文件“電気双極子の電場と放射.doc”（对应本章1.4）。').replace('请参考第2章内容。','请参考作者文件夹“膜からのSFG”中的系列文件（对应本书第二章）。')
s=s[:a]+t+s[b:];p.write_text(s,encoding='utf-8');(o/'B018-本批译文.md').write_text('# B018：入射场、辐射及有限厚度膜\n\n'+t,encoding='utf-8')
(o/'B018.md').write_text('''# B018 校订记录

2026-10-16。范围：PDF p12第5部分起至p13第7部分末，附录A之前。三段跨页电场说明、两个文件/文件夹引用均已对照，无新编号公式。

保留p偏振x/z分量反射符号、布儒斯特角、薄基板背面反射、零膜厚极限多重反射、偶极相互作用及洛伦兹修正的层次，不把作者当时的研究状态改写成今日结论。旧译“第6章将讨论局域场”无原文依据，已恢复作者dipole-dipole文件夹。第6/7部分保留原文件引用并加对应本地章节说明；第7标题修正为有限厚度薄膜。

源图续校-原文p12/p13.png。术语沿既定局域场/菲涅尔因子；原文反射系数r仍按振幅反射系数具体命名，不机械替换。下一批附录A。
''',encoding='utf-8')
print('B018 source citations restored, main sections 1–7 reviewed; appendices remain.')

from 整节续校工具 import *
parent=next(D.glob('2.2 *.md'));old=parent.read_text(encoding='utf-8');current=TARGET.read_text(encoding='utf-8');before=OUT/'B123-2.2修订前.md';assert not before.exists();before.write_text(old,encoding='utf-8');s=old
row=next(x for x in current.splitlines() if x.startswith('| （3a）'))
s=re.sub(r'^\| （3a）[^\n]*',lambda _:row,s,count=1,flags=re.M)
note74=next(x for x in current.splitlines() if '**译校注（Q074' in x).replace('PDF p5','PDF p40').replace('本独立底本','底本').replace('不得把母本译文中已统一的下标直接当作底本的原式。','先前转写统一了下标，本轮恢复底本原字形。')
idx=s.index('> **译校注（Q056');s=s[:idx]+note74+'\n\n'+s[idx:]
i=s.index('#### 反射光');a=s[:i];rest=s[i:].replace(tex('$(-2nh_m§tan§theta_m,0)$'),tex('$(-2h_m§tan§theta_m,0)$'),1);s=a+rest
note75=next(x for x in current.splitlines() if '**译校注（Q075' in x).replace('独立PDF p7','PDF p42')
idx=s.index(tex('这里使用 $k_1§sin§theta_1=k_m§sin§theta_m$'));s=s[:idx]+note75+'\n\n'+s[idx:]
blocks=lambda text:re.findall(r'\$\$[\s\S]*?\$\$',text)
c2=next(x for x in blocks(current) if tex('§tag{C.2}') in x)
s=re.sub(r'\$\$[\s\S]*?\$\$',lambda m:c2 if tex('§tag{C.2}') in m[0] else m[0],s)
note76=next(x for x in current.splitlines() if '**译校注（Q076' in x).replace('独立PDF p8','PDF p42')
s=s.replace(c2,c2+'\n\n'+note76,1)
last=blocks(current)[-1];oldlast=blocks(s)[-1];assert tex('§frac{2n_1§cos§theta_m}') in last
s=s.replace(oldlast,last,1)
# Preserve source slash form in appendix C only; explanatory candidates stay in notes.
i=s.index('## 附录C.');a=s[:i];tail=s[i:]
tail=tail.replace(tex('§lambda=2§pi/k=2§pi c/(§omega n)'),tex('§lambda=2§pi/k=2§pi c/§omega n'))
for k in ['1','2']:
 for line in tail.splitlines():
  if line.startswith('| （'+('2b' if k=='2' else '4b')+'）'):
   tail=tail.replace(line,line.replace(tex('§omega z/(k_'+k+tex('§cos§theta_')+k+')'),tex('§omega z/k_')+k+tex('§cos§theta_')+k))
tail=tail.replace(tex('§Delta§nu=1/(2n_mh_m§cos§theta_m)'),tex('§Delta§nu=1/2n_mh_m§cos§theta_m'))
tail+=tex('''
> **后续转写复核（B123）：** 独立2.3校订时回查本底本p39—40、42、47，恢复了（3a）的距离角下标 $§theta_2$、反射入射点中原未写的序号 $n$、C.2两处 $§pi_m$ 的字形以及附录D末式的 $2n_1§cos§theta_m$。波长、时间与条纹间隔恢复原有无分母括号的斜线写法。均为译文转写/排版修复，不是采用原文候选修正；Q074—Q076按原值保留，疑点及候选只入注。
''')
s=a+tail
assert re.findall(r'\\tag\{([^}]+)\}',s)==re.findall(r'\\tag\{([^}]+)\}',old)
assert s.split('## 附录C.')[0]==old.split('## 附录C.')[0]
parent.write_text(s,encoding='utf-8')
out2=OUT.parent/'2.2';fragment='\n\n'.join([row,note74,note75,c2,note76,last])
(out2/'B123-本批译文.md').write_text(fragment,encoding='utf-8')
(out2/'B123.md').write_text('# B123：2.2附录的关联转写修复\n\n2026-10-19，回查本底本p39/40/42/47及原式图B080-p42-03、B081-p47-07。两PDF原式同样含相关字形，非独立PDF特有差异。恢复3a角标、入射点原缺n、C.2两处π_m和D末式2n_1；斜线排版回到原连写。没有改作者公式、没有新E编号。Q074—Q076原值与候选分别保留。正文/编号/原PDF摘要不变，修改范围限附录C/D。修订前另存2.3/B123-2.2修订前.md。\n',encoding='utf-8')
p=out2/'全节数学收尾验收.md';t=p.read_text(encoding='utf-8');t+='\n后续复核（B123）：2.3续译触发2.2附录C/D的定点回查。修复小下标与斜线转写，不改原文、编号或完成范围；详见B123.md及跨节修订前快照。\n';p.write_text(t,encoding='utf-8')
print('B123: associated parent transcription repaired; original formulas retained')

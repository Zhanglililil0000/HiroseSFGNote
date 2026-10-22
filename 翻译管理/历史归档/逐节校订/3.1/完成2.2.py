exec(open('HiroseSFGNote/翻译管理/校订记录/3.1/续校工具.py',encoding='utf-8').read())
old=P.read_text(encoding='utf-8');assert (O/'B178-修订前.md').read_text(encoding='utf-8')==old;a=old.index('**m/2 界面的 m 侧：**',old.index('### 2.2 和频极化'));b=old.index('### 2.3 SFG电场',a);src=old[a:b]
marks=[0,src.index("**m'/m 界面的 m' 侧：**"),src.index("**m'/m 界面的 m 侧：**"),src.index("**m' 层的深度"),src.index('**m 层中距'),len(src)]
qs=[note('Q102','PDF p10—11，式2.23—2.26',r'内部界面极化的位置写 $h_m^-$、$h_m^+$，但2.1对应场写 $h_{m\prime}^{\mp}$。各处按原文保留，候选为极化式厚度下标补撇号，未采用。'),note('Q103','PDF p11，式2.25',r'红外光分子仍采用 $(1+r_{m\prime m,ir,\beta})$，与同式可见光分子及2.26的对应透射系数不同，沿原式保留。候选为改用对应透射系数，关联Q098，未采用。'),note('Q104','PDF p12—13，式2.29—2.30','四项和中重复出现左花括号、未配右花括号，保留可见符号，关联Q101。候选为只用一对花括号包住四项和，未采用。此处原极化位置只写z2，不静默补成2.1的hm+z2。')]
parts=[]
for i in range(5):
 s=src[marks[i]:marks[i+1]];s=s.replace('(a): $E^{+}$ (by reflection) and $E^{-}$ sources','（a）：$E^+$ 源（经反射）与 $E^-$ 源。').replace('(a): $E^{+}$ and $E^{-}$ (by reflection) sources','（a）：$E^+$ 源与 $E^-$ 源（经反射）。').replace('(b): $E^{+}$ (by reflection) and $E^{-}$ sources','（b）：$E^+$ 源（经反射）与 $E^-$ 源。').replace(': $E^{+}$ sources','：$E^+$ 源。').replace(': $E^{-}$ sources','：$E^-$ 源。')
 s=join_formulas(s)
 if i==1:s+=qs[0]
 if i==2:s+=qs[1]
 if i==4:s+=qs[2]
 parts.append(s);writebatch(178+i,s,[[10],[10,11],[11],[11,12],[12,13]][i],['m/2界面m侧2.22','内部界面m′侧2.23—2.24','内部界面m侧2.25—2.26','m′体相正反向极化2.27—2.28','m体相正反向极化2.29—2.30'][i])
P.write_text(old[:a]+''.join(parts)+old[b:],encoding='utf-8');append(M/'疑难与勘误.md',''.join(qs));append(O/'结构与复用核验表.md','B178—B182完成2.2余下9式；2.2合计13式2.18—2.30，跨p11—12及p12—13已接全。Q102—Q104保留原值，2.3起仍待校订。');print('2.2余下全部内容已核至2.30')

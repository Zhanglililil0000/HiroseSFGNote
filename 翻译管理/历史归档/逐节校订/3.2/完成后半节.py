from pathlib import Path
import re,json,hashlib
import pypdfium2 as pdf
p=Path(__file__).resolve().parent; root=p.parents[2]
f=root/'中文版本/第三章 双层膜的和频/3.2 双层膜和频的一般式.md'
s=f.read_text(encoding='utf-8'); cut=s.index('<!-- B236止；'); tail=s[s.index('**$E^+$ sources**',cut):]
(p/'B237前后半节快照.md').write_text(tail,encoding='utf-8')
chunks=[]
def take(marker):
    global tail
    i=tail.index(marker); v=tail[:i]; tail=tail[i:]; return v
chunks.append(take('- **透射 SFG**'))
chunks.append(take('**$E^-$ sources**'))
chunks.append(take('- **透射 SFG**'))
chunks.append(take('\n---\n'))
tail=tail.replace('\n---\n','',1).lstrip()
chunks.append(take('因此，若将经过'))
chunks.append(take('**$E^+$ sources**'))
chunks.append(take('- **透射 SFG**'))
chunks.append(take('**$E^-$ sources**'))
chunks.append(take('- **透射 SFG**'))
chunks.append(take('\n---\n'))
tail=tail.replace('\n---\n','',1).lstrip()
chunks.append(take('### 附录 B'))
chunks.append(tail)
assert len(chunks)==12
# 仅裁出底本光路图区域，保留图内原标记与原表达式，不据旧译重绘。
assets=root/'中文版本/assets/ch03'; assets.mkdir(exist_ok=True)
doc=pdf.PdfDocument(str(root/'日语原版/Chapter3/chap3-2.pdf'))
figs={0:(5,.475,.855,7),1:(6,.300,.540,4),2:(7,.105,.605,8),3:(8,.105,.350,4),6:(9,.585,.820,4),7:(10,.195,.790,8),8:(11,.315,.575,4),9:(12,.105,.485,7)}
for i,(page,top,bottom,n) in figs.items():
    im=doc[page-1].render(scale=3).to_pil(); w,h=im.size
    name=f'ch03-s03-2-p{page:02d}-paths.png'
    im.crop((int(w*.08),int(h*top),int(w*.95),int(h*bottom))).save(assets/name)
    figure=f'![原文p{page}光路图组（{n}幅子图，保留原图内标记）](../assets/ch03/{name})\n\n图内标记与各路径因子按原图保留；$m\'$与$m$分别标示两膜层。'
    assert len(re.findall(r'```[\s\S]*?```',chunks[i]))==1
    chunks[i]=re.sub(r'```[\s\S]*?```',lambda _:figure,chunks[i])
# 统一叙述与标题；公式因子保留原页，排版只作分行。
for i,c in enumerate(chunks):
    c=c.replace('**$E^+$ sources**','##### $E^+$源（初始向下传播）').replace('**$E^-$ sources**','##### $E^-$源（初始向上传播）')
    c=c.replace('- **反射 SFG** $E^{-}_{(0-)}$','**反射和频光 $E^-(0^-)$**').replace('- **透射 SFG** $E^{+}_{(h_m+)}$','**透射和频光 $E^+(h_m^+)$**')
    c=c.replace('**$m$ 层中，从 $m\'/m$ 界面算起深度 $z_2$ 点处的 SFG**','#### $m$层中距$m\'/m$界面深度$z_2$处产生的和频光')
    c=c.replace('光的选取出现在','光路的分支选择出现在').replace('净电场','合成电场')
    c=c.replace('\\begin{pmatrix}','\\begin{bmatrix}').replace('\\end{pmatrix}','\\end{bmatrix}').replace('E_{\\text{net}}','E_{\\mathrm{net}}')
    c=c.replace("+ t_{mm'} (r_{m'1}","\\\\\n&\\qquad + t_{mm'} (r_{m'1}")
    chunks[i]=c
# 原文疑点就地保留，不用后文或代数候选修订前文。
notes={
2:r'''**译者注（原文疑点Q118，PDF p7）：** 式(2.14)第一行在初值列向量后多印一个右方括号，以下保留该原字形。原图部分路径因子的层标及$a^2$字形亦有不一致，保留原图，不据相似路径改写。''',
3:r'''**译者注（原文疑点Q118，PDF p8）：** 本段指定$x=a_0r_{m'1}a$，式(2.15)第一行外部因子却只写$a_0r_{m'1}$，末行又含$a$；候选为第一行补$a$，尚未采用。''',
4:r'''**译者注（原文疑点Q119，PDF p8）：** 原文此处仍称“透过$m'/m$界面、在$m/2$界面反射”，而本段$m$层的逆向路径描述涉及另一侧的反射；不按对称性替换原层名。式(2.17)同样由$x'$转写为$x$，关系仍待核，关联Q117。''',
5:r'''**译者注（原文疑点Q119，PDF p9）：** 初始电场的行向量为$(r_{mm'},t_{mm'})$，随后递推的两行及式(2.18)却写$(r_{m'm},t_{m'm})$。原式照录，候选为统一至本段$m$层路径的反向系数，但未采用。后面的具体应用式又使用$(r_{mm'},t_{mm'})$，不能据此静默修订本通式。''',
6:r'''**译者注（原图记号，Q119）：** p9图内部分系数带额外撇号或层标差异，保留原图；式(2.19)的行向量按原页采用$(r_{mm'},t_{mm'})$，与通式(2.18)的写法差异仍待核。''',
9:r'''**译者注（原图记号，Q119，PDF p12）：** 原图部分路径的反射层标与相邻路径不一致（如b-2b中的层标），原图和式(2.22)各自按原页保留，不以路径对称性统一。''',
10:r'''**译者注（原文疑点Q120，PDF p13）：** “所有元素的绝对值均小于1”一般不足以保证$A^n\to0$。例如$A=\begin{bmatrix}0.6&0.6\\0.6&0.6\end{bmatrix}$的元素均小于1，但其特征值为$1.2$和$0$，矩阵幂不趋于零。候选条件是谱半径$\rho(A)<1$，但此处仍保留原文条件及式(A.6)，未替换。原文从$n=0,1,2$的验证推及一般$n$的句子也照译；一般有限级数恒等式可由式(A.4)的展开获得，不能仅靠三个特例证明。''',
11:r'''**译者注（原文疑点Q121，PDF p13）：** 原文所称“第2节与第3节”在本文件中没有直接对应的第3节，保留原引用，可能涉及另一编排版本，未确认。括注左端按底本保留拉丁字母$b$及未加括号的除法串；若候选读作$\beta/(r_{m2}t_{mm'}b^2)$，与前文$\beta$定义结合仍需核额外反射/透射因子，故不采用补读。这里的$A$为相似变换矩阵，须可逆，不能自动等同于附录A中的一般矩阵或前文传播因子$a$。'''
}
# p7额外右括号按原位置转写；不解释为新物理分组。
chunks[2]=chunks[2].replace("\\begin{bmatrix} a^2 \\\\ r_{m2} t_{mm'} a^2 b^2 \\end{bmatrix}","\\begin{bmatrix} a^2 \\\\ r_{m2} t_{mm'} a^2 b^2 \\end{bmatrix}\\bigr]")
# 附录B的长链分行，原因子和次序不变。
chunks[11]=chunks[11].replace("r' X^n u = rA (A^{-1} Y A) (A^{-1} Y A) (A^{-1} Y A) \\cdots (A^{-1} Y A) u = r Y^n A u = r Y^n u'",r"\begin{aligned}r'X^nu&=rA(A^{-1}YA)(A^{-1}YA)(A^{-1}YA)\cdots(A^{-1}YA)u\\&=rY^nAu=rY^nu'\end{aligned}")
pages=[[5,6],[6],[6,7],[7,8],[8],[8,9],[9,10],[10,11],[11],[11,12],[12,13],[13]]
for i,c in enumerate(chunks):
    if i in notes: c+='\n> '+notes[i]+'\n\n'
    c=c.replace('SFG 光','和频光').replace('中的 SFG','中的和频过程')
    chunks[i]=c
    n=237+i; tags=re.findall(r'\\tag\{([^}]+)\}',c)
    (p/f'B{n}-本批译文.md').write_text(c,encoding='utf-8')
    rec=dict(batch=f'B{n}',date='2026-10-20',pages=pages[i],tags=tags,source_images_visually_checked=True,source_formula_corrections_adopted=False,figure_panels=figs[i][3] if i in figs else 0,source_sha256=hashlib.sha256((root/'日语原版/Chapter3/chap3-2.pdf').read_bytes()).hexdigest())
    (p/f'B{n}-覆盖.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (p/f'B{n}.md').write_text(f'# B{n} 校订记录\n\n原文页：{pages[i]}；编号：{tags}。已对照原页，完整保留文字、等式各行、局部符号与条件。'+('已恢复原光路图组及原图下因子，替换旧译代码块。' if i in figs else '')+'\n\n'+notes.get(i,'无新增原文疑点；原式未作修正。')+'\n',encoding='utf-8')
s=s[:cut]+'\n\n'.join(chunks)
s=s.replace('B228—B236已核第1部分、2.1全部及2.2递推和式(2.11)；其后光路图与式(2.12)起仍为旧译待核。','B228—B248完成全13页本轮译校：33个唯一编号式，8组共46幅光路子图及附录A、B完整保留；原文疑点Q113—Q121保留待核，未采用原文公式修正。')
head=s.index('## 阅读导引与校订范围'); stop=s.index('## 引言',head)
s=s[:head]+'''## 阅读导引

1. 系数等（p1—2）：反射与透射系数、坐标分量转换，以及极化与辐射场之间的L系数。
2. 二层系概述2.1（p2—4）：相位和多重反射单元、四矩阵、共同分母Z，以及两膜层内正反向源的8条场表达式。
3. 详论2.2前部（p4—8）：从路径分支建立递推和逆矩阵求和，分别处理m′层两种源的反射、透射光，附23幅光路子图。
4. 详论2.2后部（p8—12）：反向组织m层路径与递推，求两种源的反射、透射光，附23幅光路子图。
5. 附录A（p12—13）：有限矩阵等比级数、逆矩阵求和及原文的收敛条件。条件存在疑点，参看Q120。
6. 附录B（p13）：以两端向量变化及相似变换说明矩阵表达的等价性；引用号与括注疑点见Q121。

建议先核源所在膜层、初始方向和观测出口，再选取场表达式。原文中若干矩阵化简、层标和相位不一致均保留并注；完成译校不等于这些原式已获理论确认。

'''+s[stop:]
f.write_text(s,encoding='utf-8')
for name in ['检查全节排版.cjs']:
    t=(root/'翻译管理/校订记录/3.1'/name).read_text(encoding='utf-8').replace('校订记录/3.1','校订记录/3.2').replace("startsWith('3.1 ')","startsWith('3.2 ')")
    (p/name).write_text(t,encoding='utf-8')
print('B237—B248正文与图组写入；尚须整节验收和管理同步')

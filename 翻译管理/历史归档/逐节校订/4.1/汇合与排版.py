from 整节工具 import *
import pypdfium2 as pdf
for n in range(251,277):
    fp=p/f'B{n}-本批译文.md'; s=fp.read_text(encoding='utf-8')
    # 将一块中多个独立编号拆成独立公式，保留每行原编号。
    def tagsplit(m):
        t=m.group(1)
        if len(re.findall(r'\\tag\{',t))<2:return m.group(0)
        t=t.replace('\\begin{aligned}','').replace('\\end{aligned}','')
        rows=re.split(r'\\\\(?:\[[^]]*\])?',t)
        return '\n\n'.join('$$\n'+row.strip().replace('&','')+'\n$$' for row in rows if row.strip())
    s=re.sub(r'\$\$([\s\S]*?)\$\$',tagsplit,s)
    if n==257:
        s=s.replace(r'r(1 - \cos\alpha)]\sqrt{2G_{a1}}',r'r(1 - \cos\alpha)\sqrt{2G_{a1}}')
    if n==259:s=s.replace('\\leftarrow','\\rightarrow')
    # CH3原1.31的共同1/4在整矩阵外；源右下因子不另补4。
    # 处理模式下标的源字形差异（p13）。
    if n==260:
        pos=s.index('参照(1.7)')
        s=s[:pos]+s[pos:].replace('G_{\\mathrm{deg}}','G_{\\mathrm{deb}}')
    # 源原式中以Latin b0定义的正文保持独立。
    if n==261:s=s.replace('\\beta_0','b_0')
    # 公式里加入的句读只用于中文行文，不进入因子。
    assert not any(ord(c)<32 and c not in '\n\r\t' for c in s),(n,'control')
    fp.write_text(s,encoding='utf-8')
# 原图仅保留p7的坐标示意，不以截图替代主公式。
assets=root/'中文版本/assets/ch04'; assets.mkdir(exist_ok=True)
d=pdf.PdfDocument(str(root/'日语原版/Chapter4/chap4-1.pdf')); im=d[6].render(scale=3).to_pil(); w,h=im.size
im.crop((int(w*.60),int(h*.735),int(w*.91),int(h*.955))).save(assets/'ch04-s04-1-p07-coordinates.png')
fp=p/'B256-本批译文.md'; s=fp.read_text(encoding='utf-8'); s+='\n![原文p7的CH键固定坐标示意](../assets/ch04/ch04-s04-1-p07-coordinates.png)\n\n原图保留键轴和分子轴标记。\n'; fp.write_text(s,encoding='utf-8')
# 连续合稿，仅去除已完成批次之间的旧译边界。
head=old[:old.index('<!-- B250止；')]
s=head+'\n\n'.join((p/f'B{n}-本批译文.md').read_text(encoding='utf-8') for n in range(251,277))
s=s.replace('B249—B250已核原目录、CH基要点及CH₂对称伸缩式(0.3)与相关关系；式(0.4)起仍为旧译待核。','B249—B276完成全部33页的本轮译校与公式、表格转写；原文疑点Q122—Q137保留原式并就地说明，未采用原文公式修正。')
target.write_text(s,encoding='utf-8')
renderer=(root/'翻译管理/校订记录/3.2/检查全节排版.cjs').read_text(encoding='utf-8').replace('校订记录/3.2','校订记录/4.1').replace('第三章 双层膜的和频','第四章 单层膜与多层膜的和频').replace("startsWith('3.2 ')","startsWith('4.1 ')")
(p/'检查全节排版.cjs').write_text(renderer,encoding='utf-8')
print('正文合稿完成，开始全节语法与排版核验')

from 收尾公式工具 import *
# Cropped italic i and + can visually merge with beta or a superscript. Cross-check
# the PDF glyph extraction as well as the crop, then fix transcription (not source).
files=[TARGET]+[OUT/f'B{i:03}-本批译文.md' for i in range(97,103)]
for p in files:
 s=p.read_text(encoding='utf-8')
 s=s.replace(r'\sum_{n=0-\infty}',r'\sum_{n=0}^{\infty}').replace(r'\sum_{n=1-\infty}',r'\sum_{n=1}^{\infty}')
 s=s.replace(r'(1+r_{m2})e^{2i\beta_mh_m}',r'(1\mp r_{m2})e^{2i\beta_mh_m}')
 s=s.replace(r"(L^-_{m/m}+r_{m2}L^-_{m/m})",r"(L^-_{m/m}+r_{m2}L^+_{m/m})")
 s=s.replace(r'e^{\beta_mh_m}',r'e^{i\beta_mh_m}')
 for w in [r'\mathrm{SF}',r'\mathrm{vis}',r'\mathrm{ir}']:
  s=s.replace(r'e^{\beta_{m,'+w+r'}h_m}',r'e^{i\beta_{m,'+w+r'}h_m}')
  s=s.replace(r'e^{2\beta_{m,'+w+r'}h_m}',r'e^{2i\beta_{m,'+w+r'}h_m}')
 s=s.replace(r'\left(r_{mm\prime\prime,\mathrm{ir},\gamma}-r_{m\prime\prime2,\mathrm{ir},\gamma}\right)',r'\left(r_{mm\prime\prime,\mathrm{ir},\gamma}+r_{m\prime\prime2,\mathrm{ir},\gamma}\right)')
 s=s.replace(r'\left(r_{mm\prime\prime,\mathrm{ir},\gamma}',r'\left(r_{mm\prime\prime,\mathrm{ir},\gamma}') # no-op; apostrophe spelling handled below
 s=s.replace(r"\left(r_{mm'',\mathrm{ir},\gamma}-r_{m''2,\mathrm{ir},\gamma}\right)",r"\left(r_{mm'',\mathrm{ir},\gamma}+r_{m''2,\mathrm{ir},\gamma}\right)")
 s=s.replace(r'r_{m2}e^{i\beta_{m,\mathrm{ir}}h_m}',r'r_{m2,\mathrm{ir}}e^{2i\beta_{m,\mathrm{ir}}h_m}')
 s=s.replace(r'\tan\theta_{m,\mathrm{SF}}\tan\theta_{m,\mathrm{SF}}',r'\tan\theta_{m,\mathrm{SF}}\tan\theta_{m,\mathrm{vis}}')
 s=s.replace(r'e^{2(\beta_{m,\mathrm{SF}}+\beta_{m,\mathrm{vis}})h_m}',r'e^{i(2(\beta_{m,\mathrm{SF}}+\beta_{m,\mathrm{vis}}))h_m}')
 # Only the first path expression is missing its closing bracket in the printed source.
 s=s.replace(r'(L^+_{m/m}+r_{m1}L^-_{m/m})P(0^+,n=0)',r'(L^+_{m/m}+r_{m1}L^-_{m/m})\Bigr]P(0^+,n=0)')
 s=re.sub(r'> \*\*译校注（Q066，[\s\S]*?(?=\n\n|\Z)',lambda m:'> **译校注（Q066，保留原式）：** 路径求和最后一行的方括号未闭合；末尾简式分子印为 $(1\\mp r_{m2})e^{2i\\beta_mh_m}$，与式（5.15）中相位所乘项的位置不同。照录原有乘法关系，未改成候选的 $1\\pm r_{m2}e^{2i\\beta_mh_m}$。求和范围的横排写法转成通常的上下限排版。',s)
 s=re.sub(r'> \*\*译校注（Q067，[\s\S]*?(?=\n\n|\Z)',lambda m:'> **译校注（Q067，保留原式）：** 式（5.16）前的简式及（5.16a、b）的和频分母含独立因子2；背面膜路径化简的前两行另有幂外的 $r_{m1}$。按原式保留。指数中的斜体 $i$ 和上标 $+$ 已结合PDF文字层复核，未当作原式缺字。',s)
 s=re.sub(r'> \*\*译校注（Q068，[\s\S]*?(?=\n\n|\Z)',lambda m:'> **译校注（Q068，保留原式）：** 体相反射推导中，零阶B极化及式（5.19）的两入射频率分母标签交叉；积分式和按失配量分组式的若干相位、分母符号不完全对应。（5.19）前两组写 $L^-_{1/m}$，后两组仍写 $L^-_{m/m}$。以上均照录，未按相邻式统一。易重叠的斜体 $i$、上下标已结合PDF文字层复核。',s)
 p.write_text(s,encoding='utf-8')
print('B097–B102 crop/text double-check applied')

from pathlib import Path
import re
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
# Reuse layout only; signs, coefficients and phase differences are checked against p8.
tex=(out/'B083-本批译文.md').read_text(encoding='utf-8').split('> **译校注')[0].strip()
for a,b in [('4.19','4.22'),('4.20','4.23'),('4.21','4.24')]:tex=tex.replace(r'\tag{'+a+'}',r'\tag{'+b+'}')
tex=tex.replace(r'-i\,2(n+1)',r'-i\,2n').replace(r'-i(2n+1)',r'-i\,2n')
tex=tex.replace(r'1+\tan','SWAPMINUS').replace(r'1-\tan',r'1+\tan').replace('SWAPMINUS',r'1-\tan')
phase=r'k_{m,\mathrm{vis}}\sin\theta_{m,\mathrm{vis}}+k_{m,\mathrm{ir}}\sin\theta_{m,\mathrm{ir}}'
assert tex.count(phase)==1
tex=tex.replace(phase,phase.replace('+',r'\;'))
new=tex+'''

> **译校注（Q060，保留原式）：** 式（4.24）的公式主体在底本p8，编号在p9页首。其整体相位括号中，可见光与红外光的两个切向波矢项之间未见加号，底本将两项并置；这里同样不补运算符。按式（4.22）、（4.23）的场乘积推测，候选为两项相加，但未经确认不用于原式。
'''
(out/'B084-本批译文.md').write_text(new,encoding='utf-8')
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
body=p.read_text(encoding='utf-8');backup=out/'B084-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=body.index('![式（4.22）—（4.24）');b=body.index('> **译校注（Q044，',a)
old=body[a:b];(out/'B084-原式图对照.md').write_text('# B084原式图对照\n\n底本2.2 PDF p8下半部；4.24编号在p9页首。\n\n'+old,encoding='utf-8')
body=body[:a]+new.strip()+'\n\n'+body[b:]
body=body.replace('式（4.10）—（4.21）已在B082—B083转为可编辑数学；','式（4.10）—（4.24）已在B082—B084转为可编辑数学；',1)
p.write_text(body,encoding='utf-8')
p=m/'疑难与勘误.md';p.write_text(p.read_text(encoding='utf-8')+'''
## 第2.2节A类源点公式转写续记（B084，2026-10-19）

| 编号 | 原文位置 | 疑点 | 类别/优先级 | 处理与状态 |
|---|---|---|---|---|
| Q060 | 2.2 PDF p8，式4.24整体相位；编号在p9页首 | 两个激发光切向波矢项之间未见加号，原式并置 | 原式运算符/P1 | 照录并置，不补符号；候选为相加，依据4.22/4.23场乘积，仅放就地注。未采用原式修正，无新增勘误附件条目。 |
''',encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B084：A类源点公式\n\n4.22—4.24整体相位的n因子均为2n；z相位中1±tanθ_SF tanθ相对于B类互换，四项反射权重仍分别为1、r_ir、r_vis、r_vis r_ir（并含往返相位）。4.24整体相位中原式未见加号，照录并置，Q060。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.21）','数学转写已推进至式（4.24）').replace('Q039—Q059尚有未决项','Q039—Q060尚有未决项');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B084完成2.2式（4.22）—（4.24）可编辑转写（2026-10-19）

已完成4.1g的A类源点三式，替换正文一幅影像，保留四个展开项与原编号（4.24编号原在p9）。新增Q060：4.24整体相位两个切向波矢项间未见加号，按底本并置；候选相加仅注。未采用原文修正，勘误附件无新增。

下一批B085：4.2a的式4.26a，再处理4.26b之前的无编号场乘积与4.26b；4.25已有可编辑数学。2.2文字已补齐，复杂公式转写仍在推进；不进入2.3。勿运行历史合入/生成脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B084.md').write_text('''# B084：4.1g的A类源点公式

日期：2026-10-19。底本2.2 PDF p8下部—p9页首（仅4.24编号）。本批边界为4.22—4.24完整三式，不进入4.2极化。

| 定位 | 对象 | 已转写 | 已对照 | 核对要点 |
|---|---|---|---|---|
| p8，4.22 | 可见光场 | 是 | 原页/高清图 | 2n整体相位，1−tan与1+tan |
| p8，4.23 | 红外光场 | 是 | 原页/高清图 | 两个z相位项及往返相位 |
| p8—9，4.24 | 场乘积 | 是 | 原页/高清图 | 四项展开、两个分母、原编号；整体相位原式并置，Q060 |

核对全部r/t方向、α/β与传播参数β、E0、z指数及正负号；仅断行，没有引入辅助记号或代数改写。Q060候选补加号不用于正文。原式图及修订前备份均保留。渲染与范围验收见B084验收.json。下一批从4.26a开始，4.25已为数学格式。
''',encoding='utf-8')
print('B084 merged; 3 equations; Q060 retained')

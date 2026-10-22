from pathlib import Path
import re

root = Path(__file__).resolve().parents[3]
chapter = root/'中文版本/第一章 SFG快速入门'
p = next(chapter.glob('1.1 *.md'))
s = p.read_text(encoding='utf-8')
lines = s.splitlines()
for i, line in enumerate(lines):
    if line.startswith(r'&\qquad +\Bigl[\frac{(r_k)_{n\prime\prime n\prime}}'):
        raise RuntimeError('Unexpected formula spelling')
    if line.startswith(r"&\qquad +\Bigl[\frac{(r_k)_{n'' n'}}") and i < 320:
        old = r'2\omega_1 - \omega_2 + \omega_{ng} + i\Gamma_{ng}'
        assert old in line
        lines[i] = line.replace(old, r'2\omega_1 - \omega + i\Gamma_{ng}', 1)
    if line.startswith(r"&\qquad +\frac{(r_k)_{n g}}{2\omega_1 - \omega_{n n''}") and 290 < i < 320:
        old = r'2\omega_1 - \omega_2 - \omega_{n n\prime} + i\Gamma_{n n\prime}'
        old = old.replace(r'\prime', "'")
        assert old in line
        lines[i] = line.replace(old, r"2\omega_1 - \omega_2\,\omega_{n n'} + i\Gamma_{n n'}", 1)
    if line.startswith('> **译者注（暂定处理 E-1.1-004'):
        lines[i] = r'> **译者注（原式待核验 E-1.1-004、E-1.1-005；Q018）：** 第5主组有两处底本排印疑点：第3子项内B项分母可见 $2\omega_1-\omega+i\Gamma_{ng}$，频率项不完整；第4子项内A项分母可见 $2\omega_1-\omega_2\,\omega_{nn\prime}+i\Gamma_{nn\prime}$，其中 $\omega_2$ 与 $\omega_{nn\prime}$ 之间未见运算符。正文已于2026-10-18按用户约定恢复底本可见写法；此处并列排印不表示已确认两者相乘。旧译候选分别为 $2\omega_1-\omega_2+\omega_{ng}+i\Gamma_{ng}$ 和 $2\omega_1-\omega_2-\omega_{nn\prime}+i\Gamma_{nn\prime}$，仅在本注中保留，未确认、未用于正文。见[原文勘误表](../附件/原文勘误表.md)。'
p.write_text('\n'.join(lines)+'\n', encoding='utf-8')
p = next(chapter.glob('1.2 *.md'))
s = p.read_text(encoding='utf-8')
# Restrict the change to the product matrix immediately preceding tag 3-2.
end = s.index(r'\tag{3-2}')
begin = s.rfind('$$', 0, end)
part = s[begin:end]
old = r'-\sin \chi & \cos \chi & 0'
assert part.count(old) == 2
pos = part.rfind(old)
part = part[:pos] + part[pos:].replace(old, r'-\sin \chi & \cos \chi & \sin \chi \sin \theta', 1)
s = s[:begin]+part+s[end:]
note = r'> **译者注（原式待核验 E-1.2-001；Q027）：** 日语底本PDF第10页式（3-2）乘积矩阵第二行第三列为 $\sin\chi\sin\theta$，正文已于2026-10-18恢复原值。按前列两矩阵相乘，该元素应为 $0$；此值作为候选修正列于本注，尚未经项目审校确认，不替换原式。见[原文勘误表](../附件/原文勘误表.md)。'
target = '\\tag{3-2}\n$$\n'
assert target in s
s=s.replace(target, target+'\n'+note+'\n',1)
s=re.sub(r'> \*\*译者注（暂定处理 E-1\.2-001；Q027）：\*\*[^\n]+', r'> **译者注（Q027，其他保留问题）：** 式（3-4）的$\\E$' if False else lambda m: '> **译者注（Q027，其他保留问题）：** 式（3-2）的矩阵疑点见该式后的就地注释。式（3-4）的 $E_{2,b}$ 正号按底本保留，与式（3-2）的符号衔接待核。末尾随机取向非零分量清单亦按原文保留，未作为完整张量表的独立证明。',s)
p.write_text(s,encoding='utf-8')
p=root/'中文版本/附件/原文勘误表.md'
s=p.read_text(encoding='utf-8')
rows=s.splitlines()
for i,line in enumerate(rows):
    if line.startswith('| E-1.1-004'):
        rows[i]=r'| E-1.1-004／Q018 | 第 8 页，式（13）第 5 主组第 3 子项 B 分母 | $2\omega_1-\omega+i\Gamma_{ng}$，频率项不完整 | 正文恢复原式；候选 $2\omega_1-\omega_2+\omega_{ng}+i\Gamma_{ng}$ 移至注释 | 2026-10-18对照底本并落实用户约定；候选待核验，未采用，不作确定勘误。 |'
    elif line.startswith('| E-1.1-005'):
        rows[i]=r'| E-1.1-005／Q018 | 第 8 页，式（13）第 5 主组第 4 子项 A 分母 | $2\omega_1-\omega_2\,\omega_{nn\prime}+i\Gamma_{nn\prime}$，两频率项间未见运算符 | 正文恢复可见原式；候选 $2\omega_1-\omega_2-\omega_{nn\prime}+i\Gamma_{nn\prime}$ 移至注释 | 2026-10-18对照底本；并列排印不表示已确认相乘。候选待核验，未采用。 |'
    elif line.startswith('| E-1.2-001'):
        rows[i]=r'| E-1.2-001／Q027 | PDF第10页，式（3-2）乘积矩阵第二行第三列 | $\sin\chi\sin\theta$ | 正文恢复原值；候选 $0$ 移至该式后注释 | 2026-10-18对照底本并落实用户约定；矩阵乘积给出候选0，待审校确认，未用于正文。Q027其他问题未关闭。 |'
s='\n'.join(rows)+'\n'
s=s.replace('以下同时收录已采用的暂定补读和候选读法', '以下同时收录暂定补读及候选读法的处理历史；已恢复原式的条目明确标注当前状态。候选仍待核验')
p.write_text(s,encoding='utf-8')
p=root/'翻译管理/疑难与勘误.md'
lines=p.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    if line.startswith('| Q018 |'):
        lines[i]=r'| Q018 | 1.1 PDF p8 式(13)第5组第3子项B分母及第4子项A分母 | 前者为2ω₁−ω+iΓ_ng，后者ω₂与ω_nn′间未见运算符 | 原式排印疑点/P1，未决 | 2026-10-18对照底本恢复正文可见原式；旧译补全候选移入就地注释。附件E-1.1-004、005同步；仅完成呈现规则调整，未确认修正式。历史B013保留 |'
    elif line.startswith('| Q027 |'):
        lines[i]+=' 2026-10-18续记：正文式（3-2）已恢复底本第二行第三列sinχsinθ；候选0移入该式后注释，见附件E-1.2-001；其余疑点仍未决。'
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
for name in ['翻译管理/当前进度与续接.md','翻译管理/翻译规范.md']:
    p=root/name
    s=p.read_text(encoding='utf-8')
    if name.endswith('翻译规范.md'):
        s=s.replace('须优先对照底本恢复原式、将候选移入注释，并同步附件状态；完成前不得标为符合本次新约定。','已于2026-10-18对照底本恢复原式，将候选移入注释，并同步附件及问题状态；候选正确性仍待核验。')
    else:
        s=s.replace('本次仅记录约定，尚未完成这项正文回查。','该衔接回查已完成，见下方续记。')
        s+='\n## 2026-10-18 原式呈现衔接已完成\n\n已目视对照1.1 PDF第8页及1.2 PDF第10页，恢复Q018两处分母及Q027矩阵元素的底本写法；候选式只保留在就地注释，问题仍未决。附件及问题表同步。Q013维持用户确认修正。核查记录：校订记录/约定衔接/原式呈现回查.md。下一步可检查跨节符号、单位与坐标约定；此次未开展该全面检查，也未进入第二章。\n'
    p.write_text(s,encoding='utf-8')
print('Q018、Q027正文、注释、附件及管理状态已同步。')

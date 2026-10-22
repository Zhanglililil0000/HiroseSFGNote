from 整节工具 import *
p=out.parent/'4.2'
s=(p/'B293-本批译文.md').read_text(encoding='utf-8')
s=s.replace(r'\omega_{\text{IR}}',r'\omega_{\text{ir}}')
add(312,[25],s,'第6部分全部7个编号式6.1—6.5c，独立对照本节p25')
s=(p/'B294-本批译文.md').read_text(encoding='utf-8')
s=s[:s.index('> **译者注（原文疑点Q145')]
def orig(m):
    x=m[0]
    if r'\tag{7.4c}' in x:x=x.replace(r'\sin \theta_t',r'\cos \theta_t')
    if r'\tag{7.5c}' in x:x=x.replace(r'\sin \theta_i',r'\cos \theta_i')
    return x
s=re.sub(r'\$\$[\s\S]*?\$\$',orig,s)
needle='$$\nL_{s,y}^{(r)}'
s=s.replace(needle,'$L$因子的表达式如下：\n\n'+needle)
s+=r'''
> **译者注（原文疑点Q159，PDF p25—26）：** 式(7.1a)、(7.2a)的系数为正，而式(7.4a)、(7.5a)的相应$L$因子带负号；式(7.4c)、(7.5c)的$L$定义还包含$P_z$，并使用$\cos\theta_t$、$\cos\theta_i$，与式(7.1b)、(7.2b)对应的正弦因子不同。上述原式全部保留。候选为核对$s$分量符号、去掉$L_{p,z}$中重复的极化因子，并核对余弦是否应为正弦，尚未采用。这里也不直接套用第4.2节的正弦写法。作者最后保留的符号不确定性照译，不能写成已有定论的惯例差异。
'''
add(313,[25,26],s,'第7部分全部12个编号式7.1a—7.5c、余弦因子及作者末尾疑问')

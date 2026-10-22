from pathlib import Path
import json,shutil,re,hashlib
R=Path(__file__).resolve().parents[2];O=R/'翻译管理/全书复核';B=O/'B673修改前'
rel='中文版本/第八章 拟合/8.1 和频光谱的线形.md'
note='> **外部核查补充（B673，Q305）：** 已核对原句并查技术资料。常规样品管旋转可平均部分空间磁场不均匀性，固体魔角旋转则另有特定角度与相互作用条件；二者不能与分子随机运动视为同一过程。原例可作为时间平均的宽泛类比，但不足以唯一指定实验机制，也不宜改成“所有NMR都须高速旋转”。原句保留，作者具体场景仍待核。（技术资料：[Nanalysis](https://www.nanalysis.com/nmready-blog/2015/5/27/to-spin-or-not-to-spin)、[Bruker](https://www.bruker.com/en/resources/library/application-notes-mr/nmr-spectroscopy-for-solids.html)。）'
changes=[]
def edit(rel,fn):
 p=R/rel;s=p.read_text(encoding='utf-8-sig');t=fn(s)
 if t!=s:
  b=B/rel;b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists():shutil.copy2(p,b)
  p.write_text(t,encoding='utf-8');changes.append(rel)
edit(rel,lambda s:re.sub(r'(?m)^> \*\*原文说明待核（Q305[^\n]+',lambda m:note,s))
old=(B/rel).read_text(encoding='utf-8-sig');cur=(R/rel).read_text(encoding='utf-8-sig')
oldnote=re.search(r'(?m)^> \*\*原文说明待核（Q305[^\n]+',old)[0]
assert cur.replace(note,oldnote,1)==old
(O/'B673新增阅读提示.json').write_text(json.dumps({rel:note},ensure_ascii=False,indent=2),encoding='utf-8')
def question(s):
 start=s.index('## Q305｜');end=s.index('\n## ',start+1);block=s[start:end]
 block=re.sub(r'(?m)^\*\*原文说明待核（Q305[^\n]+',lambda m:note[2:],block)
 block=block.replace('状态：原印保留、待核；候选未采用。来源B639，正文有就地说明；不分配E编号。','状态：B673已补原始论文摘要与厂商技术资料外查；原作者特定实验场景仍未决。原句保留、无已采用修正；最初来源B639，外查更新B673，不分配E编号。')
 return s[:start]+block+s[end:]
edit('翻译管理/疑难与勘误.md',question)
def append(rel,text):edit(rel,lambda s:s if text.splitlines()[0] in s else s.rstrip()+'\n\n'+text+'\n')
append('翻译管理/疑难与勘误.md','''## B673：Q305运动窄化与NMR旋转外查（2026-10-22）

| 编号 | 位置 | 观察或问题 | 类型/优先级 | 状态与下一步 |
|---|---|---|---|---|
| Q305 | 8.1 p5运动窄化段 | 常规旋转可平均部分空间场不均匀性；MAS有特定条件；与分子随机运动不可等同 | 原文说明/P2 | B673核对原句并读取原始论文公开摘要和厂商技术资料，已更正“未外查”旧状态。宽泛平均类比有依据，作者具体相态/轴/相互作用仍不明，保留未决与原句，无新增Q/E。见全书复核/B673运动窄化复核.md |''')
append('翻译管理/符号与约定.md','''## B673：运动类比与NMR术语边界（2026-10-22）

运动窄化的分子随机调制、常规样品管旋转的空间场平均、固体魔角旋转的各向异性平均分别说明。不能由“高速旋转毛细管”静默补成MAS，也不否定所有机械旋转的平均作用。“魔角旋转”在本次说明中仅用于译者辨析，不视作本段原文词汇，不自动新增用户确认术语。Q305已外查，作者具体场景仍未决，见[本批复核](全书复核/B673运动窄化复核.md)。''')
edit('中文版本/附件/原文勘误表.md',lambda s:s.replace('Q305 | NMR样品旋转例子的适用条件；原印保留','Q305 | B673已外查NMR旋转的不同平均作用；具体场景仍待核，原句保留'))
append('中文版本/附件/原文勘误表.md','''## B673运动窄化例子外查（2026-10-22）

Q305：外部技术资料支持部分NMR机械旋转可改善相应展宽，但应区分随机分子运动、常规样品管旋转与固体魔角旋转。原作者未说明特定条件，既不擅改成MAS，也不将原例直接认定为错误。原句保留，不新增E；正文和总表旧“未外查”状态已更新。''')
append('翻译管理/全书复核/跨章约定与合稿规则.md','''## B673补充

原文实验类比需同时核查成立的共同点与适用边界；不同时间平均过程不能直接等同。外部资料不作为替作者补实验参数、相态或机制的授权。Q305已补外查，具体场景仍待核，见[B673复核](B673运动窄化复核.md)。''')
head='## 当前有效状态：B673运动窄化与NMR旋转外查（2026-10-22）'
def progress(s):
 if head in s:return s
 s=s.replace('## 当前有效状态：B672','## 历史状态：B672',1)
 return s.replace('# 当前进度与续接\n\n','# 当前进度与续接\n\n'+head+'''\n\n核对8.1 p5原句，读取Anderson原始论文公开摘要、Nanalysis说明及Bruker技术资料，区分分子随机运动、常规样品管旋转与固体MAS。已更新Q305旧“未外查”状态；宽泛平均类比有依据，作者具体相态/旋转条件仍未决。原句不改，无新增Q/E，不把辨析用语升级为底本术语。

正文注释、问题状态、符号/术语边界、勘误维护与跨章规则同步，合稿按B673更新。详见全书复核/B673运动窄化复核.md及来源记录。下一批B674核查Q310：8.1 p8—9式(17)/(18)的积分次序、复数模平方及相干性条件，按完整段落处理。\n\n''',1)
edit('翻译管理/当前进度与续接.md',progress)
sources=[
 {'title':'A Mathematical Model for the Narrowing of Spectral Lines by Exchange or Motion','author':'P. W. Anderson','date':'1954','doi':'10.1143/JPSJ.9.316','url':'https://www.jstage.jst.go.jp/article/jpsj1946/9/3/9_3_316/_article','read_scope':'公开摘要；未通读受限全文','supports':'随机频率调制的运动/交换窄化框架'},
 {'title':'To Spin or not to Spin','author':'Susie Riegel / Nanalysis','date':'2015-05-27','url':'https://www.nanalysis.com/nmready-blog/2015/5/27/to-spin-or-not-to-spin','read_scope':'厂商原创技术说明正文','supports':'常规样品管旋转的空间场平均及实验适用范围'},
 {'title':'Avance Beginners Guide — Sample Tube','author':'Bruker','url':'https://2210pc.chem.uic.edu/nmr/downloads/bruker/en-US/html/Avance%20Beginners%20Guide/en-US/18014398881662987.html','read_scope':'原厂手册小节，UIC托管镜像','supports':'X/Y场不均匀平均与旋转边带'},
 {'title':'NMR Spectroscopy for Solids','author':'Bruker','url':'https://www.bruker.com/en/resources/library/application-notes-mr/nmr-spectroscopy-for-solids.html','read_scope':'液体运动、Magic Angle Spinning相关段落','supports':'固体MAS的特定角度与各向异性平均；不可替作者指定MAS'}
]
(O/'B673来源记录.json').write_text(json.dumps({'access_date':'2026-10-22','sources':sources,'reliance':'仅依据已打开原始来源；不使用检索摘要替代正文；不推定作者具体实验'},ensure_ascii=False,indent=2),encoding='utf-8')
(O/'B673修改文件.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
(O/'B673正文保真.json').write_text(json.dumps({'original_author_text_preserved':True,'change':'仅替换旧Q305译者注释','formula_and_image_changes':0,'new_Q_or_E':0,'question_status':'外查已补；具体作者场景未决','source_files':4,'scope':'资料辨析而非仪器操作或作者意图认证'},ensure_ascii=False,indent=2),encoding='utf-8')
print('B673 updated: old unchecked status replaced; four source records saved; original author text preserved.')

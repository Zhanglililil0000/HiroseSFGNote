from pathlib import Path
out=Path(__file__).resolve().parent;root=out.parents[2];m=root/'翻译管理'
p=next((root/'中文版本/第二章 薄膜产生的SFG').glob('2.2 *.md'))
s=p.read_text(encoding='utf-8');backup=out/'B092-修订前.md';assert not backup.exists(),'One-time mutation'
backup.write_bytes(p.read_bytes());a=s.index('![式（4.30b）：');b=s.index('## 5. L系数与SFG电场',a)
old=s[a:b];new=(out/'B092-本批译文.md').read_text(encoding='utf-8').strip()+'\n\n'
(out/'B092-原式图对照.md').write_text('# B092原式图对照\n\n底本2.2 PDF p11下半部，4.30b。图下Heinz引言已在后续正文翻译。\n\n'+old,encoding='utf-8')
s=s[:a]+new+s[b:]
old_status='式（4.10）—（4.30a）及4.26b前、4.28b后的无编号式已在B082—B091推进可编辑数学转写'
new_status='第4部分至式（4.30b）的全部公式已完成本轮可编辑数学转写（含两处无编号式，B082—B092续写）'
assert old_status in s;s=s.replace(old_status,new_status,1);p.write_text(s,encoding='utf-8')
p=out/'局部约定卡.md';p.write_text(p.read_text(encoding='utf-8')+'\n## B092：A类体相极化\n\n4.30b分母可见光配β_m,vis、红外光配β_m,ir；原式没有4.30a首部无n相位。四个z相位按A类原式的1∓tan角项逐一保留，四项之后乘−i·2n位移相位，末行P(z,n=0)。没有套用B类频率或相位写法。Q044/Q060/Q064不据本式自动结案。\n',encoding='utf-8')
for p in [root/'Preface序言.md',root/'中文版本/第二章 薄膜产生的SFG/阅读导航.md']:
    s=p.read_text(encoding='utf-8').replace('数学转写已推进至式（4.30a）','数学转写已完成第4部分至式（4.30b）');p.write_text(s,encoding='utf-8')
header='''## 最新续接：B092完成2.2第4部分公式转写（2026-10-19）

已独立核对并转写A类体相极化4.30b，替换正文一幅影像。保留两分母各自的vis/ir传播参数、四项z相位、位移相位和n=0关系；没有套用4.30a首部的无n相位或交叉频率。无新增疑难、原文采用修正或勘误附件条目。至此第4部分至4.30b及其中无编号式全部为可编辑数学，既有疑点未自动结案。

下一批B093：5.1中1/m界面极化薄片的L系数5.1a—5.2c，按三个坐标分量与两出射方向完整成组处理。2.2第5部分及附录的复杂公式转写尚未全部完成；未进入2.3，勿用历史脚本覆盖现正文。

'''
p=m/'当前进度与续接.md';s=p.read_text(encoding='utf-8');p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+header,1),encoding='utf-8')
(out/'B092.md').write_text('''# B092：4.2e的A类体相极化

日期：2026-10-19。底本2.2 PDF p11下半部，完整4.30b；止于第5部分前。

| 定位 | 对象 | 已转写 | 已对照 | 核对要点 |
|---|---|---|---|---|
| p11，4.30b首部 | χ求和与公共因子 | 是 | 高清原式及原页 | E0、两个t、分母各自vis/ir相位 |
| p11，4.30b中部 | A类四项z相位 | 是 | 高清原式 | 各反射权重、β相位、正负号及1±tan项 |
| p11，4.30b末部 | 位移相位与零阶关系 | 是 | 高清原式 | −i·2n、P(z,n=0)和原编号 |

独立按A类原式核对，未套用B类的交叉频率或无n首相位；仅断行，无辅助记号及代数化简。无新增疑难、原式修正及勘误附件条目。第4部分全部公式现可编辑，既有Q044等未决问题保留。原图及备份仍存，验收见B092验收.json。下一批5.1a—5.2c。
''',encoding='utf-8')
print('B092 merged; 4.30b; section 4 editable formulas complete')

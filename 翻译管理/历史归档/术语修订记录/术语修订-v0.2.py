from pathlib import Path
import csv,shutil,re
m=Path('HiroseSFGNote/翻译管理');p=m/'术语表.tsv';backup=m/'术语修订记录'/'术语表-v0.1.tsv'
if not backup.exists():shutil.copy2(p,backup)
R=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'))
R[0].update({'推荐中文候选':'和频过程','别名或需辨析译法':'和频产生；和频发生（检索别名，正文不作首选）','定义与适用语境':'指 sum-frequency generation 过程；SFG 作信号、光强、电场或光谱定语时按对象翻译，不机械替换','依据':'2026-10-16 用户明确指定：sum-frequency generation → 和频过程','状态':'项目译名已确定（用户指定）'})
R[2]['定义与适用语境']='分子或微观粒子的极化响应；与宏观 χ 区分。旧表“分子量”为误写。'
R[3]['定义与适用语境']='微观非线性响应；β/γ 阶数分别登记。原文可能统称高阶分極率，不假定作者一定使用超分極率。'
R[4]['定义与适用语境']='宏观 χ；中文的电极化率/极化率选择待讨论，不能与微观 α 混淆。'
R[8]['定义与适用语境']='分开记录张量指标数、不可约分解的角动量阶数和矩阵维数；作者次元/階数按上下文解释。'
extra='''和周波|sum frequency|和频|频率或输出光，与和频过程区分
差周波発生|difference-frequency generation|差频过程|候选，与和频过程平行；尚未经用户确定
分極|polarization|极化|过程或电响应；作宏观量时核实定义，不译作光的偏振
偏光|polarization|偏振|光的偏振，与电极化区分
電気双極子モーメント|electric dipole moment|电偶极矩|微观量，不与极化强度混用
巨視的な分極|macroscopic polarization|宏观极化|是否写极化强度须核对单位和定义
分極率テンソル|polarizability tensor|极化率张量|作者可能统称高阶响应，应结合符号
非線形感受率|nonlinear susceptibility|非线性电极化率|译名随 T005 决定，注明宏观及阶数
ラマンテンソル|Raman tensor|拉曼张量|按作者定义，不默认等同静态极化率
配向平均|orientational average|取向平均|记录分布与归一化
分子固定座標系|molecule-fixed coordinate system|分子固定坐标系|与表面固定及实验室固定分开
空間固定座標系|space-fixed coordinate system|空间固定坐标系|不自动等同实验室固定系
表面固定|surface-fixed|表面固定|坐标系修饰语
実験室固定|laboratory-fixed|实验室固定|坐标系修饰语
共鳴|resonance|共振|不直译为共鸣
非共鳴|nonresonant|非共振|明确是响应项还是背景
均一広がり|homogeneous broadening|均匀展宽|机制与线宽这一量区分
不均一広がり|inhomogeneous broadening|非均匀展宽|与均匀展宽配套
半値全幅|full width at half maximum|半峰全宽|候选，与半高半宽区分
偏光解消度|depolarization ratio|退偏比|拉曼语境，核对比值定义
基準振動|normal vibration|简正振动|与基频区分，不直译基准振动
基準座標|normal coordinate|简正坐标|与内部坐标、对称坐标区分
対称座標|symmetry coordinate|对称坐标|GF 矩阵法语境
既約表現|irreducible representation|不可约表示|群论语境
対称性|symmetry|对称性|与具体对称操作区分
コヒーレント|coherent|相干的|振幅相干叠加与强度相加区分
複素共役|complex conjugate|复共轭|保留共轭作用范围
位相|phase|相位|配套作者时间因子约定
線幅|linewidth|线宽|区分频率、角频率、波数以及全宽半宽
最小２乗法|least-squares method|最小二乘法|日语可能使用汉字或全角数字变体'''
for i,l in enumerate(extra.splitlines(),19):
 ja,en,zh,note=l.split('|');R.append(dict(zip(R[0].keys(),[f'T{i:03}',ja,en,zh,'',note,'待核验','新增项目候选；未作规范认证','候选'])))
files=sorted((m/'全书调查'/'文本缓存').glob('*.txt'),key=lambda f:tuple(map(int,f.stem.split('.'))))
for r in R:
 hits=[]
 for f in files:
  page=0
  for line in f.read_text(encoding='utf-8').splitlines():
   mark=re.match(r'===== PDF p\.(\d+) =====',line)
   if mark:page=int(mark.group(1))
   if r['日语候选'] in line:
    loc=f'{f.stem} PDF p{page}'
    if loc not in hits:hits.append(loc)
  if len(hits)>=3:break
 r['原文位置']='；'.join(hits[:3]) if hits else '待正文核验'
 r['文本定位状态']='缓存精确字符串命中；页面语义待核验' if hits else '尚无精确字符串命中；可能有写法变体'
 r['译名决定状态']='用户已确定' if r['术语编号']=='T001' else '待讨论/逐节核验'
 r['英语来源说明']='译者辅助对应；未逐项确认作者是否使用该英文'
assert len(R)==48 and len({r['术语编号'] for r in R})==48
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(R[0]),delimiter='\t');w.writeheader();w.writerows(R)
print('48 terms; T001 confirmed by user; original saved as v0.1; remaining terms provisional.')

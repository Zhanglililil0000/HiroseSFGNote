from pathlib import Path
import re,json,csv,io,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];M=ROOT/'翻译管理';D=ROOT/'中文版本/第二章 薄膜产生的SFG'
P=next(D.glob('2.3 *.md'));old=P.read_text(encoding='utf-8');assert not (OUT/'B117-修订前.md').exists()
(OUT/'B117-修订前.md').write_text(old,encoding='utf-8')
mother=next(D.glob('2.2 *.md')).read_text(encoding='utf-8');a=mother.index('## 附录C.');b=mother.index('### 两种介质组成的体系',a);unit=mother[a:b]
i=old.index('## 附录C');j=old.index('### 由两种介质组成的系统',i);new=old[:i]+unit+'\n'+old[j:]
new=new.replace('B115—B116已完成引言、附录A及附录B（PDF p1—4，至附录C标题前）的本轮校订，含全部编号公式及无编号关系。附录C—D仍为旧译待校订；其公式不因语法可显示而视为已核验。','至B117已完成引言、附录A/B及附录C开头“单一且均匀的介质”（PDF p1—4）的本轮校订，含相应编号公式及无编号关系。附录C自“两种介质”起及附录D仍为旧译待校订。')
new=new.replace('A.1—A.12、B.1—B.2编号','A.1—A.12、B.1—B.2、C.1编号')
new=new.replace('附录C追踪传播光路及相位，附录D讨论极化薄片的L系数（C、D目前依据结构定位，待逐段校订）。','附录C追踪传播光路及相位（已核单一均匀介质中的传播与相位衔接）；双介质、夹膜体系及附录D的极化薄片L系数仍待逐段校订。')
new=new.replace('本节附录B使用负时间因子；附录C待核。第2.2节SFG正文也主要使用','本节附录B及已核的C.1采用负时间因子；第2.2节SFG正文也主要使用')
P.write_text(new,encoding='utf-8');(OUT/'B117-本批译文.md').write_text(unit,encoding='utf-8')
assert new[new.index('### 由两种介质组成的系统'):]==old[j:]
assert re.findall(r'\\tag\{([^}]+)\}',unit)==['C.1']
assert not any(ord(c)<32 and c not in '\n\r' for c in new)
sha=hashlib.sha256((ROOT/'日语原版/Chapter2/chap2-3.pdf').read_bytes()).hexdigest();assert sha=='63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384'
units=['平面波/单位入射振幅前提、z轴方向及C.1','参考时空点零相位定义','同一时刻上游点相位−kΔz','稍后波前位置z0+(ω/k)Δt','上游波源发射时刻及到达后的同相关系','一般位移时空点相位−kΔz+ωΔt']
(OUT/'B117-覆盖.json').write_text(json.dumps({'batch':'B117','page':4,'end':'p5两种介质标题前','labels':['C.1'],'units':units,'source_sha256':sha,'remaining_text_unchanged':True,'new_issues':[],'source_corrections_adopted':False},ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'B117.md').write_text('''# B117：附录C开头及单一且均匀的介质

2026-10-19。独立底本chap2-3.pdf，PDF p4附录C标题至页末；下一页p5“两种介质”标题之前。SHA256沿本节登记：63c635f8fde9e43fd6e7e9b1be2504119bf4354fb7a1f3deba48f3024eb28384。

对照p4原页及文字层，复核C.1、参考点相位为零、上游点的负空间相位、波前位移、上游源的提前发射时刻和一般时空位移的相位，共六个单元。保留Δz/(ω/k)原有形式，不改为其他等价写法；“同相”不扩大成任意分布源均相干的额外结论。

第2.2节附录C相应译文仅在对本独立PDF核验后复用。旧译长段拆成两段，保持论述次序与全部关系。C.1为可编辑数学；本批没有示意图、没有新增术语决定、疑难或原文修正，勘误附件无需新增条目。后续“两种介质”及以后正文与批前逐字一致。

已同步进度、清单、分批建议、导读、复用核验表与局部约定。显示及范围检查见B117验收.json和渲染检查.json；全文件语法通过不表示后续旧译已核。
''',encoding='utf-8')
def append(p,t):p.write_text(p.read_text(encoding='utf-8').rstrip()+'\n\n'+t+'\n',encoding='utf-8')
append(OUT/'2.2与2.3复用核验表.md','## B117核验更新\n\n独立底本p4附录C引言、C.1与单一且均匀介质段，已对原页及文字层核验后复用（母本p38—39对应部分）。六个关系/论述单元齐备，未发现需新增登记的差异。C部双介质及夹膜部分、D部仍待核验，不以整页或整附录标为已核。')
append(OUT/'局部约定卡.md','## B117：附录C单一均匀介质\n\n沿传播方向取正z，C.1为cos(kz−ωt)。参考点(z0,t0)相位定义为零；Δz、Δt依原式保留。同一时刻上游相位−kΔz，回溯时空点相位−kΔz+ωΔt；上游源的发射时刻为t0−Δz/(ω/k)。未推广到下一单元的折射坐标。')
def tsv(p,key,val,changes):
 rows=list(csv.DictReader(io.StringIO(p.read_text(encoding='utf-8-sig')),delimiter='\t'));fields=list(rows[0]);found=0
 for row in rows:
  if row[key]==val:row.update(changes);found+=1
 assert found
 buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows);p.write_text(buf.getvalue(),encoding='utf-8-sig')
tsv(M/'章节清单.tsv','编号','2.3',{'状态':'至B117完成引言、附录A/B及C的单一均匀介质；C自双介质起及D待校订','映射核验':'独立p1—4已核；C后续/D仅结构映射','公式图表范围':'A部16个、B部2个、C.1共19个编号式及已核部分无编号关系','导读状态':'Preface与第二章导航已更新至B117'})
tsv(M/'全书调查/分批建议.tsv','节号','2.3',{'执行状态':'2026-10-19至B117，已核p1—4至单一均匀介质末；下一批B118从p5两种介质起，按完整光路组推进'})
p=M/'当前进度与续接.md';s=p.read_text(encoding='utf-8');entry='''## 当前有效状态：B117完成2.3附录C单一均匀介质（2026-10-19）

已核独立PDF p4附录C开头、C.1与单一且均匀介质全部关系；累计引言及A/B、C开头完成，19个编号式及相应无编号关系已核。本批无新增疑难或原文修正，“两种介质”以后旧译保持不变。记录与参考渲染见校订记录/2.3/B117相关文件。

下一批B118：从独立PDF p5“两种介质组成的体系”开始，先核坐标/角度定义和完整透射光路(1)—(2c)，再按完整光路组处理反射(3)—(4c)及图；注意p5文字的角下标、经历时间与(x,−z)/(x,z)差异，分别对原页核对，不直接沿用母本校订结果。后续夹膜体系及D待核。以下是历史状态。

''';p.write_text(s.replace('# 当前进度与续接\n','# 当前进度与续接\n\n'+entry,1),encoding='utf-8')
p=ROOT/'Preface序言.md';s=p.read_text(encoding='utf-8');s=s.replace('（至B116已核引言与附录A/B，C—D待校订）','（至B117已核引言、A/B及C的单一均匀介质；后续待校订）').replace('已核部分涵盖线性响应、菲涅尔因子、行波与驻波及实场复表示，原式疑点保留。','已核部分涵盖线性响应、菲涅尔因子、波动复表示及均匀介质的时空相位关系，原式疑点保留。');p.write_text(s,encoding='utf-8')
p=D/'阅读导航.md';s=p.read_text(encoding='utf-8');s=s.replace('2.3已校订引言与附录A/B，C—D及2.4以后仍为旧译待校订。','2.3已校订至附录C的单一均匀介质；C自双介质起、D及2.4以后仍为旧译待校订。').replace('B115—B116完成引言及附录A/B。','至B117完成引言、附录A/B及C的单一均匀介质。').replace('附录C（p4—10，待核）：单一介质、双介质与夹膜体系的传播光路及相位。','附录C（p4—10，部分已核）：p4单一均匀介质已核，解释零相位参考点、波前位移及上游源的提前发射；双介质与夹膜体系仍待核。').replace('C—D的概括目前仅依据标题及结构定位','C的未核部分及D的概括目前仅依据标题及结构定位');p.write_text(s,encoding='utf-8')
print('B117 applied; C.1; six units; remaining text unchanged')

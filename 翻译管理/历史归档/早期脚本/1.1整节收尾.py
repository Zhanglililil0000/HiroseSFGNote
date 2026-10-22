from pathlib import Path
import re,json,csv,hashlib
r=Path('HiroseSFGNote');m=r/'翻译管理';o=m/'校订记录/1.1';p=r/'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md';s=p.read_text(encoding='utf-8');s=re.sub(r'> \*\*校订状态（2026-10-16）：\*\*[^\n]*','> **校订状态（2026-10-16）：** B001–B027 已完成全节23页的页面对照及排版整理，正文七部分和附录A–C均已覆盖；多处原式疑点及候选读法仍未决，见各译者注与翻译管理，不能视为无疑点定稿。',s,count=1);s=s.replace('​\t','');p.write_text(s,encoding='utf-8')
(o/'整节复核.md').write_text('''# 1.1整节复核

2026-10-16。23页；B001—B027覆盖正文1—7、附录A/B/C。正式编号1—16、A-1—A-12、B-1—B-9、C-1—C-12共49个，均各出现一次；无编号推导、式后条件及跨页段落也包含。旧译备份按各批保留。B014—B027为用户授权持续推进第一章后的各小批，不需每批交还确认。

本轮已对照整理全节，不代表理论推导独立验证。Q013/Q015—Q024等疑点保留，具体候选和底本差异在正文及疑难表；不存在以候选式作为标准语料的处理。

原文图页与参考渲染按批留存。B015前三组的排版随B016整式一起验证；其余批有独立渲染。无图表遗漏（本节原文主要为文字公式）。外部原doc引用保留原名并就可确认对应章节给出说明，不伪造链接。章级术语最终回查和其余四节仍待完成。

导读：先读1—3理解局域场、宏观/分子响应和振动共振；第4部分说明取向平均与张量变换，第5—7部分连接界面场和辐射。附录A/B给出含时微扰展开，附录C给出密度矩阵及混频分量；阅读长式时同时查看译者疑点注。
''',encoding='utf-8')
tags=re.findall(r'\\tag\{([^}]+)\}',s);expected=[str(i) for i in range(1,17)]+[f'{ch}-{i}' for ch,n in [('A',12),('B',9),('C',12)] for i in range(1,n+1)];assert sorted(tags)==sorted(expected),(len(tags),len(expected))
assert hashlib.sha256((r/'日语原版/Chapter1/chap1-1Japanese.pdf').read_bytes()).hexdigest()=='55e78cbf698abc1d53b424010b3abc52299da10a7b7fee236f44a73a0ce6ac8b'
for id in ['B014','B015','B016','B017','B018','B019','B020','B021','B022','B023','B024','B025','B026','B027']:
 p=o/f'{id}.md';t=p.read_text(encoding='utf-8');t+='\n收尾：对应参考渲染无语法报错及水平溢出（B015随B016整式验证）；图像检查见整节复核，未决问题未关闭。\n';p.write_text(t,encoding='utf-8')
p=m/'章节清单.tsv';rows=list(csv.DictReader(p.open(encoding='utf-8-sig'),delimiter='\t'));x=next(x for x in rows if x['编号']=='1.1');x.update({'状态':'全节已页面对照及排版整理；原式疑难未决，非无疑点定稿','映射核验':'23页正文1—7及附录A—C均已对照（B001—B027）','公式图表范围':'49个编号式及无编号推导已页面对照；原式疑难见Q013等','导读状态':'已按整节内容更新，保留疑点提示','导读草案':'从分子/宏观响应与共振选择规则，进入取向张量、界面场与辐射；附录A—C给出微扰及密度矩阵推导。'})
with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
p=r/'Preface序言.md';t=p.read_text(encoding='utf-8');t=re.sub(r'（部分校订：正文至第8页式（13）末，整式已整理；Q016/Q018等含未确定读法，已注；后续待校订，第三部分未完）：建立 SFG 光谱的基本概念。','（全节已对照整理；原式疑难未决）：从分子与宏观响应、振动共振选择规则，进入取向张量和界面场；附录A—C提供微扰与密度矩阵推导。阅读长公式时请同时查看译者注。',t);p.write_text(t,encoding='utf-8')
p=m/'当前进度与续接.md';p.write_text('''# 当前进度与续接

2026-10-16。用户已明确授权按小批持续推进直到第一章完成，见第一章持续执行.md；不再默认每批结束。

1.1已完成B001—B027全23页页面对照及排版整理，49个编号式覆盖，附录也已处理。原式疑难Q013/Q015—Q024等未决并在正文加注，不能宣称无疑点定稿。见校订记录/1.1/整节复核.md。新增语料C013，现13条；术语70条。

下一步1.2，12页，先1—2页公式1-1至1-14，再逐段推进费米共振与双原子分子。其余1.3/1.4/1.5未开始校订。章总量5节61页；第一章尚未完成。继续保留每批备份、原图、渲染和记录。
''',encoding='utf-8')
p=m/'执行方案.md';t=p.read_text(encoding='utf-8');t=re.sub(r'当前阶段：[^\n]*','当前阶段：用户授权持续推进第一章；1.1全23页已对照整理（原式疑难未决），下一节1.2，章末统一导读及术语。',t,count=1);p.write_text(t,encoding='utf-8')
print('1.1 coverage verified: 49 unique equation tags, 23 pages, issues retained; section1.2 is next.')

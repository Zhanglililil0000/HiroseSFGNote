from pathlib import Path
import re,json,hashlib
from urllib.parse import unquote
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.7 CH₂、平面HCCH及扭转HCCH的和频张量.md'
s=target.read_text(encoding='utf-8');prefix=s.split('<!-- B366止；')[0]
r=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert r['math']==85 and len(r['results'])==2
assert all(not x['overs'] and x['width']==x['scrollWidth'] for x in r['results'])
assert sum(len(x['images']) for x in r['results'])==1
assert all(i['loaded'] for x in r['results'] for i in x['images'])
assert 'Q180' in prefix and len(re.findall(r'^## [12]\. ',prefix,re.M))==2
assert '第3部分及后续仍为旧译待核' in prefix
assert not re.search(r'[\u3040-\u30ff]',prefix)
assert not any(ord(c)<32 and c not in '\n\r\t' for c in prefix)
for n in [365,366]:
 c=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'))
 c.update({'status':'本批覆盖、译校与参考排版验收完成','render':next(x for x in r['results'] if x['batch']==f'B{n}'),'translation_sha256':hashlib.sha256((out/f'B{n}-本批译文.md').read_bytes()).hexdigest(),'scope_limit':'第1、2部分及原图；第3部分起未核，不作整节验收。'})
 (out/f'B{n}验收.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for line in prefix.splitlines():
 if line.startswith('!['):assert (target.parent/re.search(r'\]\(([^)]+)\)',line)[1]).resolve().exists()
preface=(root/'Preface序言.md').read_text(encoding='utf-8')
link=re.search(r'^- \[4\.7[^\n]+?\]\(([^\n]+?)\)（',preface,re.M)[1]
assert (root/unquote(link)).resolve()==target.resolve()
report={'date':'2026-10-21','section':'4.7','batches':'B365—B366','source_total_pages':24,'verified_scope':'PDF p1—2，第1、2部分、原图及局部导读','independent_figures':1,'math_fragments':85,'math_syntax_errors':0,'formula_overflows':0,'source_issue':'Q180，原称保留','source_corrections_adopted':False,'next_batch':'B367，PDF p3第3部分引言及完整表(3a-1)','translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
(out/'B365—B366阶段复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'B365—B366阶段复核.md').write_text('''# 4.7第1、2部分阶段复核

2026-10-21，B365—B366。底本24页，本阶段完成PDF p1—2第1、2部分，未登记整节完成。

- 原题包含CH₂及平面/扭转HCCH的和频张量，绪论讨论CH伸缩，已修复旧题“CH₂弯曲振动”。
- 第1部分全部段落、跨页避让机制与对称性讨论均已核对；修复“疑似存在位阻”被译成“存在值得怀疑”的语气，以及CH₂旋转/倾斜机制的合并。
- 补回原p1表面结构图，直接提取原嵌入RGB图像，保留(a)/(b)和2×1/1×1标签；未重绘。来源与像素/哈希见图像来源。
- 第2部分abc、xyz、XYZ三级坐标、平面/扭转形a/c轴及φ、θtilt、χip定义完整覆盖；π/2偏移依原文保留。Q180原CCC面与分子面用语待核，候选未采用。
- 85个数学片段通过严格语法检查，两批预览无公式横向溢出，唯一图片正常加载；图像及坐标定义预览已检查。
- 导读、序言、章节导航、章节清单、当前进度、局部约定/术语、疑难及勘误状态已更新。第3部分起保留旧译并设明确边界。

下一批B367从PDF p3第3部分引言及表(3a-1)开始，完整27行×3个角度列逐格核验，重点辨认τ函数幂、±号及实验室方位角。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

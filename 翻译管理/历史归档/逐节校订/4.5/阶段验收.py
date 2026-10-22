from pathlib import Path
import re,json,hashlib
from urllib.parse import unquote
out=Path(__file__).resolve().parent;root=out.parents[2]
target=root/'中文版本/第四章 单层膜与多层膜的和频/4.5 两个CH₃基团的张量分量.md'
s=target.read_text(encoding='utf-8');prefix=s.split('<!-- B325止；')[0]
r=json.loads((out/'渲染检查.json').read_text(encoding='utf-8'))
assert r['math']==128 and len(r['results'])==3
assert all(not x['overs'] and x['width']==x['scrollWidth'] for x in r['results'])
assert len(re.findall(r'^## [1-4]\. ',prefix,re.M))==4
assert all(f'Q{q}' in prefix for q in range(168,171))
assert not any(ord(c)<32 and c not in '\n\r\t' for c in prefix)
assert all((out/f'原文p{i}.png').exists() for i in range(1,4))
preface=(root/'Preface序言.md').read_text(encoding='utf-8')
link=re.search(r'^- \[4\.5[^\n]+?\]\(([^\n]+?)\)（',preface,re.M)[1]
assert (root/unquote(link)).resolve()==target.resolve()
assert '第5部分及附录仍为旧译待核' in prefix
for n in range(323,326):
 c=json.loads((out/f'B{n}-覆盖.json').read_text(encoding='utf-8'))
 c.update({'status':'本批译校及参考排版验收完成','render':next(x for x in r['results'] if x['batch']==f'B{n}'),'translation_sha256':hashlib.sha256((out/f'B{n}-本批译文.md').read_bytes()).hexdigest(),'scope_limit':'本批覆盖与译文排版核验，非原文理论验证；第5部分以后未核。'})
 (out/f'B{n}验收.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report={'date':'2026-10-21','section':'4.5','batches':'B323—B325','source_total_pages':78,'verified_scope':'PDF p1—3，原目录及第1—4部分','math_fragments':128,'math_syntax_errors':0,'formula_overflows':0,'source_issues':'Q168—Q170，原述保留','source_corrections_adopted':False,'next_batch':'B326，PDF p3第5部分自由旋转完整分子β表','translation_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
(out/'B323—B325阶段复核.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'B323—B325阶段复核.md').write_text('''# 4.5第1—4部分阶段复核

2026-10-21，B323—B325。底本共78页，本阶段核原目录及PDF p1—3第1—4部分，未登记整节完成。

- 原题恢复为“(CH₃)₂X基团的处理”；原目录完整保留正文、旋转条件及附录A—F，页码差异加注。
- 两级分子坐标、两内部旋转角与欧拉角、六条三角关系逐项核对。区分甲基abc、基团xyz与空间XYZ，未继承4.4表面角度。
- 恢复全对称/简并以及同相/反相的原述；删除旧译擅加的应用例子、弯曲模式与混合耦合论述，修复对称性分类错列。
- Q168目录朝向及页码，Q169重复a轴/极限几何，Q170角条件与群分类措辞，均原述保留并就地说明，未采用原文修正。
- 128个数学片段通过严格语法检查，三个批次在1100像素视口无公式横向溢出；目录、坐标定义、恒等式和对称性表预览已看。
- 已更新节首引导、Preface、章节导航、章节清单、当前进度、局部约定/术语、疑难及勘误状态。完整分批队列见结构与分批计划。

第5部分起保留旧译并设明确边界；下一批B326从PDF p3第5部分“自由旋转”的全对称/简并分子β表开始。排版与覆盖验收不等于原文物理推导已验证。
''',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))

from pathlib import Path
from urllib.request import urlopen,Request
from html.parser import HTMLParser
from urllib.parse import urljoin
import csv,hashlib,json
root=Path('HiroseSFGNote').resolve();out=root/'翻译管理'/'来源记录';out.mkdir(exist_ok=True)
url='https://comp.chem.tohoku.ac.jp/study/hirose.html'
snapshot=out/'hirose-2026-10-16.html'
if snapshot.exists():
 raw=snapshot.read_bytes();mime='text/html（本地快照，未保存响应头）';encoding=None
else:
 with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as resp:
  raw=resp.read();mime=resp.headers.get('Content-Type','');encoding=resp.headers.get_content_charset()
(out/'hirose-2026-10-16.html').write_bytes(raw)
class Links(HTMLParser):
 def __init__(self):super().__init__();self.items=[];self.href=None;self.label=[]
 def handle_starttag(self,tag,attrs):
  if tag=='a':self.href=dict(attrs).get('href');self.label=[]
 def handle_data(self,data):
  if self.href is not None:self.label.append(data)
 def handle_endtag(self,tag):
  if tag=='a' and self.href is not None:self.items.append((self.href,''.join(self.label).strip()));self.href=None
for enc in [encoding,'utf-8','cp932','euc_jp']:
 if not enc:continue
 try:html=raw.decode(enc);break
 except UnicodeDecodeError:continue
p=Links();p.feed(html)
links=[{'目录标签':title,'原始链接':href,'绝对地址':urljoin(url,href),'文件类型':Path(href).suffix.lower()} for href,title in p.items]
with (out/'网页链接清单.tsv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(links[0]),delimiter='\t');w.writeheader();w.writerows(links)
meta={'url':url,'saved_date':'2026-10-16','content_type':mime,'decoded_as':enc,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'links':len(links),'pdf_links':sum(x['文件类型']=='.pdf' for x in links),'note':'仅保存目录页 HTML；未重新下载各节 PDF；在线与本地 PDF 的逐字节一致性未验证'}
(out/'网页快照信息.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(meta,ensure_ascii=False))

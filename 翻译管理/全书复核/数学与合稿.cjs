const fs=require('fs'),path=require('path');
const R=path.resolve(__dirname,'../..'), O=__dirname, M=path.join(R,'合稿准备');
const katex=require(path.join(R,'翻译管理/排版工具/katex-0.16.22.min.js'));
const marked=require(path.join(R,'翻译管理/排版工具/marked-15.0.12.umd.js'));
const fragments=JSON.parse(fs.readFileSync(path.join(O,'数学片段.json'),'utf8'));
let errors=[];
for(const f of fragments){try{katex.renderToString(f.tex,{displayMode:f.display,throwOnError:true,strict:'error'});}catch(e){errors.push({...f,error:e.message});}}
fs.writeFileSync(path.join(O,'数学验收.json'),JSON.stringify({count:fragments.length,errors,scope:'KaTeX严格语法检查；不证明公式物理正确'},null,2));
const source=fs.readFileSync(path.join(M,'全书审阅稿.md'),'utf8');
const manifest=JSON.parse(fs.readFileSync(path.join(M,'合稿清单.json'),'utf8'));
const math=/\$\$([\s\S]*?)\$\$|(?<![\\$])\$(?!\$)((?:\\.|[^$\n])+)\$/g;
function render(md){let items=[];let safe=md.replace(math,(all,a,b)=>{let key='BOOKMATH'+items.length+'END';let html;try{html=katex.renderToString(a??b,{displayMode:a!==undefined,throwOnError:true,strict:'error'});}catch(e){html='<pre>'+all.replace(/&/g,'&amp;').replace(/</g,'&lt;')+'</pre>';}
items.push(html);return a!==undefined?'\n\n'+key+'\n\n':key;});let html=marked.parse(safe);return html.replace(/<p>BOOKMATH(\d+)END<\/p>|BOOKMATH(\d+)END/g,(_,a,b)=>items[Number(a??b)]);}
function wrap(title,body){return '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>'+title+'</title><link rel="stylesheet" href="../翻译管理/排版工具/katex.min.css"><style>body{max-width:1050px;margin:30px auto;padding:0 22px;font:17px/1.85 "Microsoft YaHei",sans-serif;color:#222}img{max-width:100%;height:auto}table{display:block;max-width:100%;overflow:auto;border-collapse:collapse}td,th{padding:6px;border:1px solid #ccc}.katex-display{overflow:auto;padding:10px 0}blockquote{border-left:4px solid #8b9;padding:3px 18px;background:#f3f6f7}nav{position:sticky;top:0;background:white;border-bottom:1px solid #ccc;padding:5px}a{color:#245f8c}pre{overflow:auto}</style><nav><a href="index.html">全书目录</a> · 审阅稿 B665 · 原式疑点保留</nav>'+body+'</html>';}
let index='<h1>Hirose SFG 中文译本·审阅合稿</h1><p>39节，717页底本。非最终定稿；公式编号按原节保留，跨节引用须带节号。图片公式仍为原图。</p><p><a href="全书审阅稿.md">单文件Markdown</a> · <a href="序言.html">序言与逐节导读</a> · <a href="附件.html">原文勘误附件</a></p>';
let start=source.indexOf('<a id="preface">');let first=source.indexOf('<a id="sec-');
fs.writeFileSync(path.join(M,'序言.html'),wrap('序言与阅读导航',render(source.slice(start,first))));
for(let c=1;c<=8;c++){
 const sections=manifest.sections.filter(x=>x.section.split('.')[0]===String(c));
 let body='<h1>第'+c+'章</h1><ul>'+sections.map(x=>'<li><a href="#'+x.anchor+'">'+x.title+'</a></li>').join('')+'</ul>';
 for(const x of sections){let a=source.indexOf('<a id="'+x.anchor+'">'),b=source.indexOf('<a id="',a+10);body+=render(source.slice(a,b<0?undefined:b));}
 fs.writeFileSync(path.join(M,'第'+c+'章.html'),wrap('第'+c+'章·审阅稿',body));
 index+='<h2><a href="第'+c+'章.html">第'+c+'章</a></h2><ul>'+sections.map(x=>'<li><a href="第'+c+'章.html#'+x.anchor+'">'+x.title+'</a></li>').join('')+'</ul>';
}
fs.writeFileSync(path.join(M,'附件.html'),wrap('原文勘误附件',render(source.slice(source.indexOf('<a id="errata">')))));
fs.writeFileSync(path.join(M,'index.html'),wrap('全书审阅目录',index));
const noteFile=path.join(O,manifest.batch+'新增阅读提示.json');if(fs.existsSync(noteFile)){const notes=JSON.parse(fs.readFileSync(noteFile,'utf8'));fs.writeFileSync(path.join(M,manifest.batch+'阅读提示.html'),wrap(manifest.batch+'新增提示检查',Object.entries(notes).map(([p,s])=>'<h2>'+path.basename(p)+'</h2>'+render(s)).join('')));}
const reportName=fs.readdirSync(O).find(f=>f.startsWith(manifest.batch)&&f.endsWith('复核.md'));if(reportName){const report=fs.readFileSync(path.join(O,reportName),'utf8');let count=0;for(const m of report.matchAll(math)){katex.renderToString(m[1]??m[2],{displayMode:m[1]!==undefined,throwOnError:true,strict:'error'});count++;}fs.writeFileSync(path.join(O,manifest.batch+'报告数学验收.json'),JSON.stringify({count,errors:[]},null,2));}
for(const file of fs.readdirSync(M).filter(f=>f.endsWith('.html'))){const p=path.join(M,file);fs.writeFileSync(p,fs.readFileSync(p,'utf8').replaceAll('审阅稿 B665','审阅稿 '+manifest.batch));}
console.log(JSON.stringify({fragments:fragments.length,errors:errors.length,html_chapters:8,batch:manifest.batch}));

const fs=require('fs'),path=require('path'),url=require('url');
const root=path.resolve('HiroseSFGNote'),out=path.join(root,'翻译管理/校订记录/5.2');
const source=path.join(root,'中文版本/第五章 张量与对称性/5.2 主要点群的特征标表与基底.md');
const k=require(path.join(root,'翻译管理/排版工具/katex-0.16.22.min.js'));
const marked=require(path.join(root,'翻译管理/排版工具/marked-15.0.12.umd.js'));
const sourceHash=require('crypto').createHash('sha256').update(fs.readFileSync(source)).digest('hex');
let s=fs.readFileSync(source,'utf8'),formulas=[];
s=s.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(_,b,i)=>{const key='SECMATH'+formulas.length+'END';formulas.push([key,k.renderToString(b||i,{displayMode:b!==undefined,throwOnError:true,strict:'error'})]);return b!==undefined?'\n\n'+key+'\n\n':key;});
let body=marked.parse(s);for(const [key,html] of formulas)body=body.replace(new RegExp('<p>'+key+'</p>|'+key),html);
const html='<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="'+url.pathToFileURL(path.join(root,'翻译管理/排版工具/katex.min.css')).href+'"><style>body{max-width:970px;margin:24px auto;font:18px/1.8 "Microsoft YaHei",sans-serif;padding:0 24px}blockquote{margin:16px 0;padding:10px 18px;background:#f3f6f8;border-left:4px solid #9ab}.katex{font-size:1em}.katex-display{padding:10px 0;overflow:auto}td,th{border:1px solid #ccc;padding:5px}table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%}</style>'+body;
const dest=path.join(out,'全节参考渲染.html');fs.writeFileSync(dest,html);
(async()=>{const{chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});
try{const page=await browser.newPage({viewport:{width:1100,height:1100}});await page.goto(url.pathToFileURL(dest).href);await page.evaluate(()=>document.fonts.ready);
const metrics=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,tables:[...document.querySelectorAll('table')].map(t=>({rows:t.rows.length,width:t.clientWidth,scrollWidth:t.scrollWidth})),heads:[...document.querySelectorAll('h2')].map(h=>({text:h.innerText,y:h.getBoundingClientRect().top+scrollY})),errors:document.querySelectorAll('.katex-error').length}));
for(const [file,fragment] of [['首页','记号与适用范围'],['Cs','Cₛ（'],['D3d','D₃d（'],['Td','（PDF p18）'],['连续群','C∞ᵥ（'],['末页','D∞ₕ（']]){const h=metrics.heads.find(x=>x.text.includes(fragment));if(h){await page.evaluate(y=>scrollTo(0,y),Math.max(0,h.y-15));await page.screenshot({path:path.join(out,'全节抽查-'+file+'.png')});}}
const result={date:'2026-10-21',canonical_sha256:sourceHash,math:formulas.length,...metrics};fs.writeFileSync(path.join(out,'全节排版检查.json'),JSON.stringify(result,null,2));console.log(JSON.stringify({math:formulas.length,width:metrics.width,scrollWidth:metrics.scrollWidth,tables:metrics.tables.length,scrollingTables:metrics.tables.filter(t=>t.scrollWidth>t.width+2).length,headings:metrics.heads.length,errors:metrics.errors}));if(metrics.width!==metrics.scrollWidth||metrics.errors)process.exitCode=1;
}finally{await browser.close();}})();

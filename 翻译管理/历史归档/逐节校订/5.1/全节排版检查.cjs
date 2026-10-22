const fs=require('fs'),path=require('path'),url=require('url');
const root=path.resolve('HiroseSFGNote'),out=path.join(root,'翻译管理/校订记录/5.1');
const dir=path.join(root,'中文版本/第五章 张量与对称性');
const source=path.join(dir,'5.1 和频张量与对称性.md');
const katex=require(path.join(root,'翻译管理/排版工具/katex-0.16.22.min.js'));
const marked=require(path.join(root,'翻译管理/排版工具/marked-15.0.12.umd.js'));
let md=fs.readFileSync(source,'utf8'),formulas=[],errors=[];
md=md.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(_,b,i)=>{
 const key='WHOLEMATH'+formulas.length+'END';let html='';
 try{html=katex.renderToString(b||i,{displayMode:b!==undefined,throwOnError:true,strict:'error'});}catch(e){errors.push(e.message);}
 formulas.push([key,html]);return b!==undefined?'\n\n'+key+'\n\n':key;
});
if(errors.length)throw Error(JSON.stringify(errors));
let body=marked.parse(md);for(const [key,html] of formulas)body=body.replace(new RegExp('<p>'+key+'</p>|'+key),html);
const html='<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="'+url.pathToFileURL(path.join(root,'翻译管理/排版工具/katex.min.css')).href+'"><style>body{max-width:970px;margin:24px auto;font:18px/1.8 "Microsoft YaHei",sans-serif;padding:0 24px}blockquote{margin:16px 0;padding:10px 18px;background:#f3f6f8;border-left:4px solid #9ab}.katex{font-size:1em}.katex-display{padding:10px 0;overflow-x:auto}td,th{border:1px solid #ccc;padding:5px}table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%}</style>'+body;
const dest=path.join(out,'全节参考渲染.html');fs.writeFileSync(dest,html);
(async()=>{
 const {chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});
 const page=await browser.newPage({viewport:{width:1100,height:1100}});await page.goto(url.pathToFileURL(dest).href);await page.evaluate(()=>document.fonts.ready);
 const metrics=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,tables:[...document.querySelectorAll('table')].map(t=>({rows:t.rows.length,scrollWidth:t.scrollWidth,width:t.clientWidth})),overs:[...document.querySelectorAll('.katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.innerText),headings:[...document.querySelectorAll('h2,h3')].map(e=>({text:e.innerText,y:e.getBoundingClientRect().top+scrollY})),tags:[...document.querySelectorAll('.tag')].map(e=>e.innerText)}));
 await page.screenshot({path:path.join(out,'全节参考渲染.png'),fullPage:true});
 for(const [name,title] of [['节首','对称性与张量分量'],['表格','C₃ᵥ对称性与不可约基底'],['跨页式5','式(5a)'],['附录B','附录B'],['附录C','附录C']]){
  const h=metrics.headings.find(x=>x.text.includes(title));if(!h)continue;
  await page.evaluate(y=>scrollTo(0,y),Math.max(0,Math.round(h.y)-15));
  await page.screenshot({path:path.join(out,'全节抽查-'+name+'.png')});
 }
 await browser.close();
 const report={date:'2026-10-21',math:formulas.length,errors,...metrics};fs.writeFileSync(path.join(out,'全节排版检查.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({math:formulas.length,errors,width:metrics.width,scrollWidth:metrics.scrollWidth,tables:metrics.tables,overs:metrics.overs,tags:metrics.tags}));
 if(metrics.scrollWidth>metrics.width||metrics.overs.length)process.exitCode=1;
})();

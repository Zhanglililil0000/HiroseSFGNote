const fs=require('fs'),path=require('path'),url=require('url');
const root=path.resolve('HiroseSFGNote'),out=path.join(root,'翻译管理/校订记录/2.4');
const k=require(path.join(root,'翻译管理/排版工具/katex-0.16.22.min.js'));
const marked=require(path.join(root,'翻译管理/排版工具/marked-15.0.12.umd.js'));
const dir=path.join(root,'中文版本/第二章 薄膜产生的SFG');
const source=path.join(dir,fs.readdirSync(dir).find(x=>x.startsWith('2.4 ')));
const s=fs.readFileSync(source,'utf8');let errors=[],count=0;
s.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(all,b,i,offset)=>{count++;try{k.renderToString(b||i,{displayMode:b!==undefined,throwOnError:true,strict:'error'});}catch(e){errors.push({line:s.slice(0,offset).split('\n').length,error:e.message,tex:(b||i).slice(0,160)});}return all;});
console.log(JSON.stringify({count,errors},null,2));if(errors.length)process.exit(1);
if(process.argv.includes('--syntax'))process.exit(0);
(async()=>{const {chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});let results=[];
const selection=process.argv.find(x=>x.startsWith('--batch='));const selected=selection?selection.slice(8).split(','):null;
for(const file of ['整节-本批译文.md']){
let md=s;const formulas=[];
md=md.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(_,b,i)=>{const key='MATHPLACEHOLDER'+formulas.length+'END';formulas.push([key,k.renderToString(b||i,{displayMode:b!==undefined,throwOnError:true,strict:'error'})]);return b!==undefined?'\n\n'+key+'\n\n':key;});
let body=marked.parse(md);for(const [key,html]of formulas)body=body.replace(new RegExp('<p>'+key+'</p>|'+key),html);
body=body.replace(/src="(\.\.\/assets\/[^"\n]+)"/g,(_,p)=>'src="'+url.pathToFileURL(path.resolve(dir,p)).href+'"');
const html='<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="'+url.pathToFileURL(path.join(root,'翻译管理/排版工具/katex.min.css')).href+'"><style>body{max-width:970px;margin:24px auto;font:18px/1.8 "Microsoft YaHei",sans-serif;padding:0 24px}img{max-width:100%;height:auto}blockquote{margin:16px 0;padding:10px 18px;background:#f3f6f8;border-left:4px solid #9ab} .katex{font-size:1em}.katex-display{padding:10px 0;overflow-x:auto}td,th{border:1px solid #ccc;padding:5px}table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%}</style>'+body;
const id='整节';fs.writeFileSync(path.join(out,id+'-参考渲染.html'),html);
const page=await browser.newPage({viewport:{width:1100,height:950}});await page.goto(url.pathToFileURL(path.join(out,id+'-参考渲染.html')).href);await page.evaluate(()=>document.fonts.ready);
const metrics=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,overs:[...document.querySelectorAll('.katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>({width:e.scrollWidth,available:e.clientWidth,text:e.innerText.slice(0,60)})),images:[...document.images].map(i=>({loaded:i.complete&&i.naturalWidth>0}))}));
const height=await page.evaluate(()=>document.documentElement.scrollHeight);let tiles=[];for(let top=0,n=1;top<height;top+=900,n++){await page.evaluate(y=>scrollTo(0,y),top);const actual=await page.evaluate(()=>scrollY);const name='全文分屏-'+String(n).padStart(2,'0')+'.png';await page.screenshot({path:path.join(out,name),fullPage:false});tiles.push({file:name,y:actual});}fs.writeFileSync(path.join(out,'全文分屏.json'),JSON.stringify({height,tiles}));results.push({batch:id,...metrics});await page.close();}
await browser.close();if(selected){const prev=JSON.parse(fs.readFileSync(path.join(out,'整节渲染检查.json'),'utf8'));results=[...prev.results.filter(x=>!selected.includes(x.batch)),...results].sort((a,b)=>a.batch.localeCompare(b.batch));}fs.writeFileSync(path.join(out,'整节渲染检查.json'),JSON.stringify({date:'2026-10-20',math:count,results},null,2));console.log(JSON.stringify(results.map(x=>({batch:x.batch,scrollWidth:x.scrollWidth,images:x.images.length,allLoaded:x.images.every(i=>i.loaded)}))));})();

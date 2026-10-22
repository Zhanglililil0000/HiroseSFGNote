const fs=require('fs'),path=require('path'),url=require('url');
const root=path.resolve('HiroseSFGNote'),out=path.join(root,'翻译管理/校订记录/2.1');
const k=require(path.join(root,'翻译管理/排版工具/katex-0.16.22.min.js'));
const marked=require(path.join(root,'翻译管理/排版工具/marked-15.0.12.umd.js'));
const dir=path.join(root,'中文版本/第二章 薄膜产生的SFG');
const source=path.join(dir,fs.readdirSync(dir).find(x=>x.startsWith('2.1 ')));
const s=fs.readFileSync(source,'utf8');let errors=[],count=0;
s.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(all,b,i,offset)=>{count++;try{k.renderToString(b||i,{displayMode:b!==undefined,throwOnError:true,strict:'error'});}catch(e){errors.push({line:s.slice(0,offset).split('\n').length,error:e.message,tex:(b||i).slice(0,160)});}return all;});
console.log(JSON.stringify({count,errors},null,2));if(errors.length)process.exit(1);
if(process.argv.includes('--syntax'))process.exit(0);
(async()=>{const {chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});let results=[];
for(const file of fs.readdirSync(out).filter(f=>/^B05\d-本批译文.md$/.test(f)).sort()){
let md=fs.readFileSync(path.join(out,file),'utf8');const formulas=[];
md=md.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(_,b,i)=>{const key='MATHPLACEHOLDER'+formulas.length+'END';formulas.push([key,k.renderToString(b||i,{displayMode:b!==undefined,throwOnError:true,strict:'error'})]);return b!==undefined?'\n\n'+key+'\n\n':key;});
let body=marked.parse(md);for(const [key,html]of formulas)body=body.replace(new RegExp('<p>'+key+'</p>|'+key),html);
body=body.replace(/src="(\.\.\/assets\/[^"\n]+)"/g,(_,p)=>'src="'+url.pathToFileURL(path.resolve(dir,p)).href+'"');
const html='<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="'+url.pathToFileURL(path.join(root,'翻译管理/排版工具/katex.min.css')).href+'"><style>body{max-width:970px;margin:24px auto;font:18px/1.8 "Microsoft YaHei",sans-serif;padding:0 24px}img{max-width:100%;height:auto}blockquote{margin:16px 0;padding:10px 18px;background:#f3f6f8;border-left:4px solid #9ab} .katex{font-size:1em}.katex-display{padding:10px 0}td,th{border:1px solid #ccc;padding:5px}table{border-collapse:collapse}</style>'+body;
const id=file.slice(0,4);fs.writeFileSync(path.join(out,id+'-参考渲染.html'),html);
const page=await browser.newPage({viewport:{width:1100,height:950}});await page.goto(url.pathToFileURL(path.join(out,id+'-参考渲染.html')).href);await page.evaluate(()=>document.fonts.ready);
const metrics=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,overs:[...document.querySelectorAll('.katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>({width:e.scrollWidth,available:e.clientWidth,text:e.innerText.slice(0,60)})),images:[...document.images].map(i=>({loaded:i.complete&&i.naturalWidth>0}))}));
await page.screenshot({path:path.join(out,id+'-参考渲染.png'),fullPage:true});results.push({batch:id,...metrics});await page.close();}
await browser.close();fs.writeFileSync(path.join(out,'渲染检查.json'),JSON.stringify({date:'2026-10-19',math:count,results},null,2));console.log(JSON.stringify(results));})();

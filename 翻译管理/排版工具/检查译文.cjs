const fs=require('fs'),path=require('path');
const base=path.resolve('HiroseSFGNote/翻译管理'),root=path.resolve('HiroseSFGNote');
const katex=require(path.join(base,'排版工具/katex-0.16.22.min.js'));
const marked=require(path.join(base,'排版工具/marked-15.0.12.umd.js'));
const {chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const source=path.join(root,'中文版本/第一章 SFG快速入门/1.1 红外-可见光和频振动光谱（SFG）入门.md');
 const s=fs.readFileSync(source,'utf8'); const out=path.join(base,'校订记录/1.1');
 const sections=[['B001',s.slice(s.indexOf('## 1. 引言'),s.indexOf('## 2. SFG 极化与和频过程'))]];
 if(process.argv.includes('--b002')) sections.push(['B002',s.slice(s.indexOf('## 2. SFG 极化与和频过程'),s.indexOf('## 3. 分子的 SFG 极化与振动共振'))]);
 if(process.argv.includes('--b003')) {sections.length=0;sections.push(['B003',s.slice(s.indexOf('## 3. 分子的 SFG 极化与振动共振'),s.indexOf('相互作用哈密顿量写为'))]);}
 if(process.argv.includes('--b004')) {sections.length=0;sections.push(['B004',s.slice(s.indexOf('相互作用哈密顿量写为'),s.indexOf('**（二阶非线性极化：三波混频）**'))]);}
 if(process.argv.includes('--b005')) {sections.length=0;sections.push(['B005',s.slice(s.indexOf('**（二阶非线性极化：三波混频）**'),s.indexOf('**（差频过程（DFG））**'))]);}
 if(process.argv.includes('--b006')) {sections.length=0;sections.push(['B006',s.slice(s.indexOf('**（差频过程（DFG））**'),s.indexOf('上述各式给出的是相应的极化系数'))]);}
 if(process.argv.includes('--b007')) {sections.length=0;sections.push(['B007',s.slice(s.indexOf('上述各式给出的是相应的极化系数'),s.indexOf('**（三阶极化－1：双波长光引起的四波混合）**'))]);}
 if(process.argv.includes('--b008')) {sections.length=0;sections.push(['B008',fs.readFileSync(path.join(out,'B008-式12工作稿.md'),'utf8')]);}
 if(process.argv.includes('--b009')) {sections.length=0;sections.push(['B009',fs.readFileSync(path.join(out,'B009-式12工作稿.md'),'utf8')]);}
 if(process.argv.includes('--b010')) {sections.length=0;sections.push(['B010',fs.readFileSync(path.join(out,'B010-式12定稿.md'),'utf8')]);}
 if(process.argv.includes('--b011')) {sections.length=0;sections.push(['B011',fs.readFileSync(path.join(out,'B011-式13工作稿.md'),'utf8')]);}
 if(process.argv.includes('--b012')) {sections.length=0;sections.push(['B012',fs.readFileSync(path.join(out,'B012-式13工作稿.md'),'utf8')]);}
 if(process.argv.includes('--b013')) {sections.length=0;sections.push(['B013',fs.readFileSync(path.join(out,'B013-式13整理稿.md'),'utf8')]);}
 const custom=process.argv.find(x=>x.startsWith('--draft='));if(custom){const [id,...parts]=custom.slice(8).split(':');sections.length=0;sections.push([id,fs.readFileSync(path.join(base,parts.join(':')),'utf8')]);}
 const exe=['C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe','C:/Program Files/Microsoft/Edge/Application/msedge.exe','C:/Program Files/Google/Chrome/Application/chrome.exe'].find(x=>fs.existsSync(x));
 const browser=await chromium.launch({headless:true,...(exe?{executablePath:exe}:{})});
 const page=await browser.newPage({viewport:{width:1100,height:1000},deviceScaleFactor:1}); const results=[];
 for(const [id,md] of sections){
  const formulas=[];
  const protect=(tex,display)=>{let html=katex.renderToString(tex,{displayMode:display,throwOnError:true,output:'htmlAndMathml',strict:'error'});const key='MATHPLACEHOLDER'+formulas.length+'END';formulas.push([key,display?'<div class="displaymath">'+html+'</div>':html]);return display?'\n\n'+key+'\n\n':key;};
  let safe=md.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(all,block,inline)=>protect(block||inline,block!==undefined));
  let body=marked.parse(safe);for(const [key,html] of formulas)body=body.replace(new RegExp('<p>'+key+'</p>|'+key),html);
  const cssUrl=require('url').pathToFileURL(path.join(base,'排版工具/katex.min.css')).href;
  const html='<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="'+cssUrl+'"><title>'+id+' reference render</title><style>body{max-width:960px;margin:28px auto;padding:0 24px;font:18px/1.85 "Microsoft YaHei",sans-serif;color:#222}h2{font-size:25px}blockquote{margin:18px 0;padding:6px 18px;border-left:4px solid #9aa;background:#f4f6f8}p{margin:16px 0}.displaymath{padding:10px 0;max-width:100%}.katex{font-size:1.05em}</style>'+body;
  fs.writeFileSync(path.join(out,id+'-参考渲染.html'),html);
  await page.goto(require('url').pathToFileURL(path.join(out,id+'-参考渲染.html')).href);await page.evaluate(()=>document.fonts.ready);
  const metrics=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,math:document.querySelectorAll('math').length,height:document.documentElement.scrollHeight}));
  await page.screenshot({path:path.join(out,id+'-参考渲染.png'),fullPage:true});results.push({batch:id,formulas:formulas.length,...metrics});
 }
 await browser.close();const reportPath=path.join(out,'渲染检查.json');const old=fs.existsSync(reportPath)?JSON.parse(fs.readFileSync(reportPath,'utf8')).results:[];const merged=[...old.filter(x=>!results.some(y=>y.batch===x.batch)),...results].sort((a,b)=>a.batch.localeCompare(b.batch));fs.writeFileSync(reportPath,JSON.stringify({renderer:'marked 15.0.12 + KaTeX 0.16.22 HTML with local fonts; Edge/Chromium headless',date:'2026-10-16',results:merged},null,2));console.log(JSON.stringify(results));
})().catch(e=>{console.error(e);process.exit(1)});

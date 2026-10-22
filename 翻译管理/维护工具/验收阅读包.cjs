const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const R=path.resolve(__dirname,'../..'),D=path.join(R,'交付版本/当前阅读版');const batch=JSON.parse(fs.readFileSync(path.join(D,'阅读包清单.json'),'utf8')).batch;const O=path.join(R,'翻译管理/文件结构审查',batch+'阅读包显示');fs.mkdirSync(O,{recursive:true});
(async()=>{const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});const page=await browser.newPage({viewport:{width:1280,height:1000}});const failed=[];page.on('requestfailed',r=>failed.push({url:r.url(),reason:r.failure()?.errorText}));let results=[];
for(const rel of ['开始阅读.html','合稿准备/index.html','合稿准备/序言.html',...Array.from({length:8},(_,i)=>'合稿准备/第'+(i+1)+'章.html'),'合稿准备/附件.html']){
 await page.goto(pathToFileURL(path.join(D,rel)).href,{waitUntil:'load',timeout:120000});await page.evaluate(()=>document.fonts.ready);
 results.push({path:rel,...await page.evaluate(()=>({images:document.images.length,missingImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),mathErrors:document.querySelectorAll('.katex-error').length,pageOverflow:document.documentElement.scrollWidth>innerWidth+2,math:document.querySelectorAll('.katex').length}))});
 if(rel==='合稿准备/序言.html')await page.screenshot({path:path.join(O,'序言全页.png'),fullPage:true});
 if(rel==='开始阅读.html'||rel.endsWith('第8章.html'))await page.screenshot({path:path.join(O,rel==='开始阅读.html'?'阅读包入口.png':'阅读包第八章.png')});
}
await browser.close();const passed=failed.length===0&&results.every(x=>!x.missingImages.length&&!x.mathErrors&&!x.pageOverflow)&&results.reduce((s,x)=>s+x.images,0)===327;
fs.writeFileSync(path.join(O,'阅读包浏览验收.json'),JSON.stringify({content_batch:'B676',packaging_batch:batch,passed,failedRequests:failed,pages:results,scope:'独立交付目录内12个页面加载、327处图片及字体请求；正文未重译'},null,2));if(!passed)throw Error('Portable reader validation failed');console.log(JSON.stringify({passed,pages:results.length,image_references:327,failed_requests:failed.length}));})();

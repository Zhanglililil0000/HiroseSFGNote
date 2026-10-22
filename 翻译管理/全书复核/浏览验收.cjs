const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const snapshots=path.join(__dirname,'验收快照');fs.mkdirSync(snapshots,{recursive:true});
(async()=>{const R=path.resolve(__dirname,'../..'),M=path.join(R,'合稿准备');const b=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});let results=[];const p=await b.newPage({viewport:{width:1280,height:1000}});
const notesOnly=process.argv.includes('--notes');
const batch=process.argv.find(x=>/^B\d{3}$/.test(x))||'B666';
for(const file of (notesOnly?['index.html',batch+'阅读提示.html']:['index.html','序言.html',...Array.from({length:8},(_,i)=>'第'+(i+1)+'章.html'),'附件.html'])){
 await p.goto(pathToFileURL(path.join(M,file)).href,{waitUntil:'load',timeout:120000});await p.evaluate(()=>document.fonts.ready);
 const result=await p.evaluate(()=>({title:document.title,images:document.images.length,missingImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src),mathErrors:document.querySelectorAll('.katex-error').length,anchors:[...document.querySelectorAll('[id]')].map(x=>x.id),pageOverflow:document.documentElement.scrollWidth>innerWidth+2,mathCount:document.querySelectorAll('.katex').length}));
 results.push({file,...result});await p.screenshot({path:path.join(snapshots,(notesOnly?batch+'-':'')+file.replace('.html','-首屏.png'))});
}
fs.writeFileSync(path.join(snapshots,notesOnly?batch+'浏览验收.json':'浏览验收.json'),JSON.stringify(results,null,2));await b.close();console.log(JSON.stringify(results.map(({anchors,...x})=>x)));})();

const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const R=path.resolve(__dirname,'../..'),M=path.join(R,'合稿准备');
const katex=require(path.join(R,'翻译管理/排版工具/katex-0.16.22.min.js'));
const marked=require(path.join(R,'翻译管理/排版工具/marked-15.0.12.umd.js'));
const {chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const rx=/\$\$([\s\S]*?)\$\$|(?<![\\$])\$(?!\$)((?:\\.|[^$\n])+)\$/g;
let count=0;
function render(s){let items=[];const safe=s.replace(rx,(_,a,b)=>{count++;items.push(katex.renderToString(a??b,{displayMode:a!==undefined,strict:'error',throwOnError:true}));return 'NOTEITEM'+(items.length-1)+'END';});return marked.parse(safe).replace(/NOTEITEM(\d+)END/g,(_,n)=>items[n]);}
for(const name of ['B675附录与拟合复核.md','B676全书收尾复核.md'])render(fs.readFileSync(path.join(__dirname,name),'utf8'));
const notes={...JSON.parse(fs.readFileSync(path.join(__dirname,'B675新增阅读提示.json'),'utf8')),...JSON.parse(fs.readFileSync(path.join(__dirname,'B676新增阅读提示.json'),'utf8'))};
for(const rel of Object.keys(notes)){
 const current=fs.readFileSync(path.join(R,rel),'utf8');
 for(const prefix of ['> **原文条件待核（Q311','> **原文归一化疑点（Q319']){const line=current.split('\n').find(l=>l.startsWith(prefix));if(line)notes[rel]+='\n\n'+line;}
}
let body=Object.entries(notes).map(([p,s])=>'<h2>'+path.basename(p)+'</h2>'+render(s)).join('');
const html='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><link rel="stylesheet" href="../翻译管理/排版工具/katex.min.css"><style>body{max-width:1000px;margin:25px auto;font:17px/1.85 "Microsoft YaHei";padding:0 22px}.katex-display{overflow:auto}blockquote{border-left:4px solid #899;padding:2px 16px;background:#f4f7f7}</style><h1>B675—B676新增与修订提示</h1>'+body+'</html>';
const file=path.join(M,'B675阅读提示.html');fs.writeFileSync(file,html);
(async()=>{const b=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});const p=await b.newPage({viewport:{width:1280,height:1000}});await p.goto(pathToFileURL(file).href);await p.evaluate(()=>document.fonts.ready);const checks=await p.evaluate(()=>({mathErrors:document.querySelectorAll('.katex-error').length,pageOverflow:document.documentElement.scrollWidth>innerWidth+2,notes:document.querySelectorAll('blockquote').length}));await p.screenshot({path:path.join(__dirname,'B675-B676提示全页.png'),fullPage:true});await b.close();if(checks.mathErrors||checks.pageOverflow)throw Error(JSON.stringify(checks));fs.writeFileSync(path.join(__dirname,'B675-B676提示验收.json'),JSON.stringify({report_and_note_math:count,...checks},null,2));console.log(JSON.stringify({report_and_note_math:count,...checks}));})();

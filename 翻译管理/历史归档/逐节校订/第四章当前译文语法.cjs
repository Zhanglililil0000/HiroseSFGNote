const fs=require('fs'),path=require('path');
const root=path.resolve('HiroseSFGNote'),dir=path.join(root,'中文版本/第四章 单层膜与多层膜的和频');
const katex=require(path.join(root,'翻译管理/排版工具/katex-0.16.22.min.js'));
let results=[];
for(const sec of ['4.7','4.8','4.9','4.10','4.11']){
 const file=fs.readdirSync(dir).find(f=>f.startsWith(sec+' ')&&f.endsWith('.md'));
 const s=fs.readFileSync(path.join(dir,file),'utf8');let count=0,errors=[];
 s.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(all,b,i,offset)=>{
  count++;try{katex.renderToString(b||i,{displayMode:b!==undefined,throwOnError:true,strict:'error'});}
  catch(e){errors.push({line:s.slice(0,offset).split('\n').length,error:e.message});}return all;
 });
 results.push({section:sec,math_fragments:count,errors});
}
fs.writeFileSync(path.join(root,'翻译管理/校订记录/第四章当前译文语法.json'),JSON.stringify(results,null,2));
console.log(JSON.stringify(results));if(results.some(r=>r.errors.length))process.exit(1);

const fs=require('fs'),path=require('path');
const root=path.resolve('HiroseSFGNote'),out=path.join(root,'翻译管理/校订记录/约定衔接');
const k=require(path.join(root,'翻译管理/排版工具/katex-0.16.22.min.js'));
const dir=path.join(root,'中文版本/第一章 SFG快速入门');
const read=prefix=>fs.readFileSync(path.join(dir,fs.readdirSync(dir).find(f=>f.startsWith(prefix+' '))),'utf8');
const a=read('1.1'),b=read('1.2');
let count=0;
for(const s of [a,b,fs.readFileSync(path.join(root,'中文版本/附件/原文勘误表.md'),'utf8')])for(const m of s.matchAll(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g)){k.renderToString(m[1]||m[2],{displayMode:!!m[1],throwOnError:true,strict:'error'});count++;}
if(!a.includes("-\\frac{(r_k)_{gn'}(r_i)_{n'n}}{\\omega_1-\\omega_2-\\omega_{nn'}+i\\Gamma_{nn'}}"))throw Error('Q013 regression');
const eq=b.slice(b.lastIndexOf('$$',b.indexOf('\\tag{3-2}')) , b.indexOf('\\tag{3-2}'));
if(!eq.includes('-\\sin \\chi & \\cos \\chi & \\sin \\chi \\sin \\theta'))throw Error('Q027 absent');
const formulas=[String.raw`2\omega_1-\omega+i\Gamma_{ng}`,String.raw`2\omega_1-\omega_2\,\omega_{nn'}+i\Gamma_{nn'}`,eq.replace(/^\$\$/, '')];
const css=path.join(root,'翻译管理/排版工具/katex.min.css').replace(/\\/g,'/');
const html='<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="file:///'+css+'"><style>body{font:18px sans-serif;padding:30px;width:1000px}section{padding:15px;border-bottom:1px solid #ccc}</style><h1>原式呈现检查</h1>'+formulas.map((f,i)=>'<section><p>'+['Q018 第3子项B分母（照原式）','Q018 第4子项A分母（并列处缺运算符）','Q027 式（3-2）（照原式）'][i]+'</p>'+k.renderToString(f,{displayMode:true,throwOnError:true})+'</section>').join('');
fs.writeFileSync(path.join(out,'呈现检查.html'),html);
fs.writeFileSync(path.join(out,'检查结果.json'),JSON.stringify({date:'2026-10-18',mathFragmentsPassed:count,Q013:'preserved',Q018:'source form restored',Q027:'source form restored'},null,2));
(async()=>{const {chromium}=require('C:/Users/admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});const p=await browser.newPage({viewport:{width:1100,height:900}});await p.goto('file:///'+path.join(out,'呈现检查.html').replace(/\\/g,'/'));await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:path.join(out,'呈现检查.png'),fullPage:true});await browser.close();console.log('Math parsing and visual render passed: '+count);})();

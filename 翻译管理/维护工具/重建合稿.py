"""Current build entry. Historic scripts are evidence, not replay commands."""
from pathlib import Path
import argparse,json,shutil,subprocess,sys
R=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser();p.add_argument('--batch');p.add_argument('--browse',action='store_true');a=p.parse_args()
batch=a.batch or json.loads((R/'合稿准备/合稿清单.json').read_text(encoding='utf-8'))['batch']
node=shutil.which('node')
if not node:
 bundled=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
 if bundled.exists():node=str(bundled)
if not node:raise SystemExit('未找到Node，请配置Node后重建合稿。')
F=R/'翻译管理/全书复核'
for command in [[sys.executable,str(F/'全书复核.py'),batch],[node,str(F/'数学与合稿.cjs')],[sys.executable,str(F/'收尾核验.py')]]:
 subprocess.run(command,cwd=R,check=True)
if a.browse:subprocess.run([node,str(F/'浏览验收.cjs')],cwd=R,check=True)

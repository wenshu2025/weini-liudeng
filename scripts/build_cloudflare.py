"""Build runtime-only Cloudflare static assets without secrets, tests or local backups."""
from pathlib import Path
import ast,json,re,shutil
ROOT=Path(__file__).resolve().parents[1];game=ROOT/'game';dist=ROOT/'deploy/cloudflare/dist';dist.mkdir(parents=True,exist_ok=True)
modules=['index.html','style.css','main.js','story.js','npc-story.js','activities.js','gestures.js','gesture-math.js','gesture-worker.js','audio.js','journey.js','journey-state.js','world-depth.js']
for name in modules:shutil.copy2(game/name,dist/name)
names=ast.literal_eval('['+re.search(r'const paths=\[(.*?)\];',(game/'main.js').read_text()).group(1)+']')
for name in names:
    src=game/'assets/models'/f'{name}-game.glb';dst=dist/'assets/models'/src.name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
for name in ['audio','images','gestures']:
    source=game/'assets'/name
    if not source.exists():raise SystemExit('Missing assets. Run python3 scripts/fetch_assets.py first.')
    shutil.copytree(source,dist/'assets'/name,dirs_exist_ok=True)
shutil.copytree(game/'vendor',dist/'vendor',dirs_exist_ok=True)
(dist/'_headers').write_text('/*\n  Cache-Control: public, max-age=0, must-revalidate\n  X-Content-Type-Options: nosniff\n')
(dist/'release.json').write_text(json.dumps({'gameVersion':'v3.4-ornate-altar-dog','models':len(names)},indent=2))
print(f'Cloudflare runtime build ready: {dist}')

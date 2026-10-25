"""Build the standalone making-of site with local model previews for Netlify."""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1];dist=ROOT/'deploy/netlify/dist'
shutil.copytree(ROOT/'making-of',dist,dirs_exist_ok=True,ignore=shutil.ignore_patterns('dev'))
for name in ['shoe-v2','book-closed','book-open','paper-flower','frame-empty','lantern','npc-baker','npc-musician','npc-lamplighter']:
    target=dist/'assets/models'/f'{name}-game.glb';target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/'game/assets/models'/target.name,target)
shutil.copytree(ROOT/'game/vendor/build',dist/'vendor/build',dirs_exist_ok=True)
for name in ['addons/loaders/GLTFLoader.js','addons/utils/BufferGeometryUtils.js','THREE-LICENSE.txt']:
    target=dist/'vendor'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/'game/vendor'/name,target)
(dist/'_redirects').write_text('/making-of / 301\n/making-of/* /:splat 301\n')
(dist/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Cache-Control: public, max-age=0, must-revalidate\n')
print(dist)

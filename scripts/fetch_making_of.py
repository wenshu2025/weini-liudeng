"""Restore the public making-of media with SHA-256 verification."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
for entry in json.loads((ROOT/'making-of/media-manifest.json').read_text())['files']:
    target=ROOT/entry['path'];target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest()==entry['sha256']:continue
    tmp=target.with_name(target.name+'.download')
    subprocess.run(['curl','--fail','--location','--retry','2','--silent','--show-error',entry['url'],'--output',str(tmp)],check=True)
    assert hashlib.sha256(tmp.read_bytes()).hexdigest()==entry['sha256'], 'Media checksum mismatch'
    tmp.replace(target)
print('Making-of media ready; run npm run build and serve deploy/cloudflare/dist.')

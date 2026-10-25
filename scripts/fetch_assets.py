"""Restore verified game assets from the published site or a downloaded release archive."""
from pathlib import Path
import argparse,concurrent.futures,hashlib,json,subprocess,zipfile
ROOT=Path(__file__).resolve().parents[1]
def digest(data):return hashlib.sha256(data).hexdigest()
def main():
    args=argparse.ArgumentParser(description=__doc__);args.add_argument('--archive',type=Path);args.add_argument('--verify-only',action='store_true');opt=args.parse_args()
    manifest=json.loads((ROOT/'assets-manifest.json').read_text());entries=manifest['files']
    if opt.archive:
        if manifest.get('archive_sha256') and digest(opt.archive.read_bytes())!=manifest['archive_sha256']:raise SystemExit('Release archive checksum mismatch')
        with zipfile.ZipFile(opt.archive) as z:
            expected={e['path']:e for e in entries};assert set(z.namelist())==set(expected),'Unexpected archive members'
            for name,e in expected.items():
                data=z.read(name);assert digest(data)==e['sha256'],f'Checksum mismatch: {name}'
                target=(ROOT/name).resolve();assert target.is_relative_to(ROOT),'Invalid archive path'
                if not opt.verify_only:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        print(f"Verified {len(entries)} archive assets"+(' (no files changed)' if opt.verify_only else ' and restored them'));return
    required=[e for e in entries if e['required']]
    def fetch(e):
        target=ROOT/e['path']
        if target.exists() and digest(target.read_bytes())==e['sha256']:return e['path']+' cached'
        if opt.verify_only:raise RuntimeError('Missing or changed: '+e['path'])
        target.parent.mkdir(parents=True,exist_ok=True);tmp=target.with_name(target.name+'.download')
        subprocess.run(['curl','--fail','--location','--retry','2','--silent','--show-error',e['url'],'--output',str(tmp)],check=True)
        if digest(tmp.read_bytes())!=e['sha256']:tmp.unlink(missing_ok=True);raise RuntimeError('Checksum mismatch: '+e['path'])
        tmp.replace(target);return e['path']+' ready'
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(fetch,required):print(result)
    print('All runtime assets verified. Start the server with: python3 -m http.server 8769 --directory game')
if __name__=='__main__':main()

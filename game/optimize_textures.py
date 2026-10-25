import pathlib,json,struct,io
from PIL import Image
folder=pathlib.Path(__file__).parent/'assets/models'
for p in list(folder.glob('*.glb')):
 if p.stem in ['bridge-straight','bridge-curved','kitchen','altar','chapel','arch'] or p.stem.endswith('-game'):continue
 data=p.read_bytes();n=struct.unpack_from('<I',data,12)[0];d=json.loads(data[20:20+n]);binary=data[28+n:];replacements={}
 for im in d.get('images',[]):
  if 'bufferView' not in im:continue
  v=d['bufferViews'][im['bufferView']];raw=binary[v.get('byteOffset',0):v.get('byteOffset',0)+v['byteLength']];img=Image.open(io.BytesIO(raw));img.thumbnail((1024,1024));buf=io.BytesIO()
  if 'A' in img.getbands() and img.getextrema()[-1][0]<255:img.save(buf,format='PNG');im['mimeType']='image/png'
  else:img.convert('RGB').save(buf,format='JPEG',quality=88);im['mimeType']='image/jpeg'
  replacements[im['bufferView']]=buf.getvalue()
 output=bytearray()
 for i,v in enumerate(d['bufferViews']):
  chunk=replacements.get(i,binary[v.get('byteOffset',0):v.get('byteOffset',0)+v['byteLength']]);output.extend(b'\0'*((-len(output))%4));v['byteOffset']=len(output);v['byteLength']=len(chunk);output.extend(chunk)
 output.extend(b'\0'*((-len(output))%4));d['buffers'][0]['byteLength']=len(output);j=json.dumps(d,separators=(',',':'),ensure_ascii=False).encode();j+=b' '*((-len(j))%4)
 target=p.with_stem(p.stem+'-game');target.write_bytes(struct.pack('<4sII',b'glTF',2,28+len(j)+len(output))+struct.pack('<I4s',len(j),b'JSON')+j+struct.pack('<I4s',len(output),b'BIN\0')+output);print(target.name,len(data),target.stat().st_size)

import struct,json,shutil
from pathlib import Path
src=Path('game/assets/models/altar-game.glb');b=src.read_bytes();n=struct.unpack_from('<I',b,12)[0];d=json.loads(b[20:20+n]);removed=[]
for node in d['nodes']:
 if node.get('children'):
  keep=[]
  for i in node['children']:
   if d['nodes'][i].get('name') in ['tripo_part_1','tripo_part_2','tripo_part_7','tripo_part_21','tripo_part_30','tripo_part_33','tripo_part_34']:removed.append(d['nodes'][i]['name'])
   else:keep.append(i)
  node['children']=keep
for node in d['nodes']:
 if node.get('name')=='tripo_part_6':node['translation']=[-.13,0,0]
 if node.get('name')=='tripo_part_8':node['translation']=[.12,0,0]
payload=json.dumps(d,separators=(',',':')).encode();payload+=b' '*((-len(payload))%4);rest=b[20+n:];out=struct.pack('<4sII',b'glTF',2,20+len(payload)+len(rest))+struct.pack('<II',len(payload),0x4e4f534a)+payload+rest
Path('game/assets/models/altar-remembrance-game.glb').write_bytes(out)
dog_source=Path('output/dante-walk-tripo.glb')
if dog_source.exists():shutil.copy2(dog_source,'game/assets/models/dante-walk-game.glb')
Path('output').mkdir(exist_ok=True)
print('Removed portrait assemblies:',removed)
Path('output/altar-remembrance-edit.json').write_text(json.dumps({'source':str(src),'output':'game/assets/models/altar-remembrance-game.glb','removedPortraitAssemblies':['tripo_part_1','tripo_part_2','tripo_part_7','tripo_part_21'],'removedFrameSupports':['tripo_part_30','tripo_part_33','tripo_part_34'],'retained':'Original table, purple cut-paper cloth, marigolds, candles, ceramic vases, keepsakes','propEdits':'Moved book and shoe slightly toward flanks to clear front frame'},indent=2))

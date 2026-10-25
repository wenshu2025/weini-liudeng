import bpy,pathlib,json,time
folder=pathlib.Path(__file__).parent/'assets/models'
report=[]
for name in ['bridge-straight','bridge-curved','kitchen','altar','chapel','arch']:
 p=folder/(name+'.glb'); target=folder/(name+'-game.glb')
 if target.exists():continue
 bpy.ops.wm.read_factory_settings(use_empty=True)
 bpy.ops.import_scene.gltf(filepath=str(p))
 before=after=0
 for obj in list(bpy.context.scene.objects):
  if obj.type=='MESH':
   before+=len(obj.data.polygons);bpy.context.view_layer.objects.active=obj
   mod=obj.modifiers.new('Game mesh','DECIMATE');mod.ratio=.16;bpy.ops.object.modifier_apply(modifier=mod.name);after+=len(obj.data.polygons)
 for im in bpy.data.images:
  if im.size[0]>1024 or im.size[1]>1024:
   r=1024/max(im.size);im.scale(max(1,int(im.size[0]*r)),max(1,int(im.size[1]*r)))
 bpy.ops.export_scene.gltf(filepath=str(target),export_format='GLB',export_image_format='JPEG',export_jpeg_quality=85,export_animations=False)
 report.append({'name':name,'before':before,'after':after,'bytes':target.stat().st_size});print(json.dumps(report[-1]),flush=True)
(folder.parent/'optimization.json').write_text(json.dumps(report,indent=2))

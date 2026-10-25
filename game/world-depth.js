import * as T from 'three';
const rnd=i=>{const n=Math.sin(i*71.157+3.31)*43758.54;return n-Math.floor(n);};
// Painted city backdrops frame the user-supplied 3D scenes; no box-house placeholders.
export function buildWorldDepth(world){
 const d=new T.Object3D();
 // Box-house placeholders, their piers and unsupported arches are withdrawn.
 document.querySelector('#world').dataset.midground='placeholders-removed';
 // Three angled scenery cards wrap the back of the plaza without occupying the living-world exit.
 const tex=new T.TextureLoader().load('assets/images/afterlife-city-v1.png',()=>document.querySelector('#world').dataset.city='ready');tex.colorSpace=T.SRGBColorSpace;
 const townTex=new T.TextureLoader().load('assets/images/living-town-v1.png',()=>document.querySelector('#world').dataset.town='ready');townTex.colorSpace=T.SRGBColorSpace;
 for(const [x,z,ry,plate]of [[0,-48,0,tex],[-64,4,Math.PI/2,tex],[64,4,-Math.PI/2,tex],[0,86,Math.PI,townTex]]){const m=new T.Mesh(new T.PlaneGeometry(155,51.7),new T.ShaderMaterial({uniforms:{map:{value:plate}},transparent:true,side:T.DoubleSide,depthWrite:false,vertexShader:'varying vec2 vUv;void main(){vUv=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}',fragmentShader:'uniform sampler2D map;varying vec2 vUv;void main(){vec4 c=texture2D(map,vUv);float a=smoothstep(0.,.24,vUv.y)*(1.-smoothstep(.86,1.,vUv.y))*smoothstep(0.,.1,vUv.x)*(1.-smoothstep(.9,1.,vUv.x));gl_FragColor=vec4(c.rgb*.75,a*.9);}',toneMapped:false}));m.position.set(x,plate===townTex?2:16,z);m.rotation.y=ry;m.renderOrder=-2;world.add(m);}
 // Street foundations extend the courtyard to the houses instead of leaving them in the void.
 const ground=new T.Mesh(new T.BoxGeometry(27,.6,21),new T.MeshStandardMaterial({color:0x4a394d,roughness:1}));ground.position.set(0,-.42,39.5);world.add(ground);
 // Warm home windows and handmade bunting over the courtyard.
 const flags=new T.InstancedMesh(new T.PlaneGeometry(.32,.45),new T.MeshStandardMaterial({side:T.DoubleSide,roughness:1}),36);for(let i=0;i<36;i++){const line=Math.floor(i/12),x=(i%12-5.5)*.65;d.position.set(x,3.6-Math.sin((i%12)/11*Math.PI)*.48,34+line*3);d.scale.set(1,1,1);d.rotation.set(0,0,(rnd(i)-.5)*.12);d.updateMatrix();flags.setMatrixAt(i,d.matrix);flags.setColorAt(i,new T.Color([0xe69c47,0x9d588f,0xcf715a][i%3]));}world.add(flags);
 const light=new T.PointLight(0xffbc79,9,13,2);light.position.set(0,3.5,37);world.add(light);
}

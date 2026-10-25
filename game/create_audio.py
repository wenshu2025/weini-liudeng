from pathlib import Path
import numpy as np,wave,json
SR=22050;out=Path(__file__).parent/'assets/audio';rng=np.random.default_rng(417)
def write(name,a):
 a=np.asarray(a);a=np.column_stack((a,a)) if a.ndim==1 else a
 peak=np.max(np.abs(a));a=a*min(1,.87/max(peak,.001));p=out/(name+'.wav')
 with wave.open(str(p),'wb') as f:f.setnchannels(2);f.setsampwidth(2);f.setframerate(SR);f.writeframes((np.clip(a,-1,1)*32767).astype('<i2').tobytes())
 return {'file':p.name,'duration':round(len(a)/SR,3),'peak':round(float(np.max(np.abs(a))),4),'rms':round(float(np.sqrt(np.mean(a*a))),4)}
def bell(freq,d=2):
 t=np.arange(int(d*SR))/SR;env=(1-np.exp(-t*160))*np.exp(-t*3);return (.7*np.sin(2*np.pi*freq*t)+.2*np.sin(2*np.pi*freq*2.01*t)+.1*np.sin(2*np.pi*freq*3*t))*env
def hz(m):return 440*2**((m-69)/12)
# Original 16-bar D-major / B-minor miniature, with a repeating 4-note motif.
length=48;n=int(length*SR);music=np.zeros((n,2));beat=.75
chords=[[50,57,62,66],[47,54,59,62],[43,50,55,59],[45,52,57,61]]
melodies=[[74,78,81,78,76,74,69,0],[71,74,78,76,74,71,69,0],[67,71,74,78,76,74,71,0],[69,73,76,81,78,76,74,0]]
def add(samples,start,amp=.2,pan=0):
 idx=(np.arange(len(samples))+int(start*SR))%n;music[idx,0]+=samples*amp*(.75-pan*.25);music[idx,1]+=samples*amp*(.75+pan*.25)
for bar in range(16):
 chord=chords[bar%4]
 for j,m in enumerate(chord):
  t=np.arange(int(3.8*SR))/SR;en=np.minimum(t/.65,1)*np.exp(-t/2.5)*(np.minimum((3.8-t)/.7,1));pad=(np.sin(2*np.pi*hz(m)*t)+.18*np.sin(2*np.pi*hz(m)*2*t))/1.18
  add(pad*en,bar*3,.045,(-1 if j%2 else 1)*.3)
 for j in range(8):
  add(bell(hz(chord[j%4]+12),1.9),bar*3+j*.375,.065,(-1 if j%2 else 1)*.5)
  m=melodies[bar%4][j]
  if m and (bar<12 or j%2==0):add(bell(hz(m+(12 if bar>=8 and bar<12 else 0)),2.6),bar*3+j*.375,.12,0)
 # Quiet low string pluck on beats one and three.
 for b in [0,1.5]:add(bell(hz(chord[0]-12),2.2),bar*3+b,.07,0)
# Wrapped stereo echoes make the exported file loop without a hard tail cut.
music+=np.roll(music,int(.225*SR),axis=0)*.18+np.roll(music[:,::-1],int(.47*SR),axis=0)*.12
report=[write('homeward-lights',music*2.4)]
for name,d,kind in [('footstep-stone',.22,0),('footstep-bridge',.24,1),('page-turn',.48,2),('pickup',.35,3)]:
 t=np.arange(int(d*SR))/SR;noise=rng.normal(0,1,len(t));low=np.convolve(noise,np.ones(14)/14,mode='same');high=noise-np.convolve(noise,np.ones(8)/8,mode='same')
 if kind<2:a=(low*.4+high*.035)*np.exp(-t*27)+np.sin(2*np.pi*(135 if kind else 88)*t)*np.exp(-t*40)*.2
 elif kind==2:a=high*.12*np.sin(np.pi*t/d)**2*(.7+.3*np.sin(2*np.pi*19*t))
 else:a=low*.25*np.exp(-t*16)+np.sin(2*np.pi*380*t)*np.exp(-t*32)*.05
 report.append(write(name,a))
for i,f in enumerate([392,440,523.251]):report.append(write('lamp-'+str(i+1),bell(f,2.2)*.45+bell(f*1.5,2.2)*.2))
for name,notes in [('bridge-open',[62,66,69,74]),('farewell',[74,69,66,62])]:
 a=np.zeros(int(4*SR))
 for i,m in enumerate(notes):b=bell(hz(m),2.2)*.32;k=int(i*.4*SR);a[k:k+len(b)]+=b
 report.append(write(name,a))
(out/'credits.json').write_text(json.dumps({'composition':'Homeward Lights / 归家的灯','authoring':'Original local synthesized score and Foley, created for 为你留灯. No third-party recordings.','loopSeconds':48,'sampleRate':SR,'files':report},ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))

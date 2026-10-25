import assert from 'node:assert/strict';
import {StepDistance,crossing,recipeEcho,flowerColor} from './journey-state.js';
import {initialState,restore,transition} from './story.js';
function walk(hz){const s=new StepDistance();let out=[];for(let i=0;i<=hz*10;i++){const v=s.update(0,i/hz*2.2,true);if(v)out.push(v);}return out;}
const a=walk(30),b=walk(120);assert.equal(a.length,b.length);assert.ok(a.every((x,i)=>!i||x.side!==a[i-1].side));
const s=new StepDistance();s.update(0,0,true);assert.equal(s.update(0,30,true),null);for(let i=0;i<80;i++)assert.equal(s.update(0,30,true),null);assert.equal(s.update(0,30,false),null);assert.equal(s.update(0,30.1,true),null);
assert.equal(crossing(14,14.1,true,false),true);assert.equal(crossing(14,14.1,false,false),false);assert.equal(crossing(14,14.1,true,true),false);assert.equal(crossing(15,14,true,false),false);
const state={...initialState(),phase:'TO_GATE',found:['shoe','recipe','flower'],bridgeCrossed:true,creations:{recipe:{sugar:3},flower:{color:'rose'}}};assert.equal(restore(state).bridgeCrossed,true);assert.equal(transition(state,'AT_GATE').bridgeCrossed,true);assert.equal(restore({...state,found:[]}).bridgeCrossed,false);assert.ok(recipeEcho(state.creations).includes('多放'));assert.equal(flowerColor(state.creations),0xf4a3bb);
console.log('PASS: frame-rate independent alternating footsteps; no blocked/teleport/paused bursts; one-way once-only crossing; restore and transitions preserve crossing; keepsake choices.');

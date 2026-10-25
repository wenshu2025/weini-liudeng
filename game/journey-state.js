// Distance-based footsteps: no particles while blocked, paused or teleported.
export class StepDistance {
 constructor(stride=.62){this.stride=stride;this.last=null;this.distance=0;this.side=1;this.count=0;}
 reset(){this.last=null;this.distance=0;this.side=1;this.count=0;}
 update(x,z,active){const last=this.last;this.last={x,z};if(!active||!last){this.distance=0;return null;}const d=Math.hypot(x-last.x,z-last.z);if(d>1){this.distance=0;return null;}this.distance+=d;if(this.distance<this.stride)return null;this.distance%=this.stride;this.side*=-1;this.count++;return {x,z,side:this.side};}
}
export function crossing(previousZ,z,unlocked,already){return unlocked&&!already&&previousZ!==null&&previousZ<=14.05&&z>14.05;}
export function recipeEcho(creations={}){return creations.recipe?.sugar===1?'少放一勺糖，清甜一点':creations.recipe?.sugar===3?'多放一勺糖，甜甜的':'两勺糖，刚刚好';}
export function flowerColor(creations={}){return {orange:0xffab35,gold:0xffd770,rose:0xf4a3bb}[creations.flower?.color]||0xffab35;}

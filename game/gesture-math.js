export function wrapAngle(n){return Math.atan2(Math.sin(n),Math.cos(n));}
const distance=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y);
export function describeHand(points,wasPinching=false){
 if(!points||points.length!==21)return null;
 const palm=Math.max(distance(points[5],points[17]),.025),pinchRatio=distance(points[4],points[8])/palm;
 const pinch=pinchRatio<(wasPinching?.48:.33);
 const fingers=[[8,6],[12,10],[16,14],[20,18]].filter(([tip,joint])=>distance(points[tip],points[0])>distance(points[joint],points[0])*1.18).length;
 return {pinch,open:!pinch&&fingers>=3,roll:Math.atan2(points[5].y-points[17].y,points[5].x-points[17].x),x:1-(points[4].x+points[8].x)/2,y:(points[4].y+points[8].y)/2,pinchRatio};
}

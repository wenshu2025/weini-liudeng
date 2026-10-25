export const NPCS={
 baker:{name:'罗莎',role:'点心摊主',model:'npc-baker',pos:[4.7,0,5.1],stand:[3.55,0,4.65],height:1.6,related:'recipe',object:'book-closed'},
 musician:{name:'马特奥',role:'广场乐师',model:'npc-musician',pos:[-4.65,-.06,6.8],stand:[-3.35,0,6.35],height:1.7,related:'shoe',object:'npc-musician'},
 keeper:{name:'阿玛',role:'守灯人',model:'npc-lamplighter',pos:[-2.2,0,12],stand:[-1.2,0,11.4],height:1.72,related:'flower',object:'lantern'}
};
export function npcConversation(key,state){const count=state.found.length,finished=count===3,c=state.creations||{};
 if(key==='baker'){if(finished)return [['罗莎','你把那份点心做出来了。她教过的做法，今天又照顾了一个人。'],['罗莎',c.recipe?.sugar===1?'少放一勺糖也好。她要是知道你有自己的主意，一定会笑。':'食谱会留下，做点心的人还会继续写下新的那一页。']];if(state.found.includes('recipe'))return [['罗莎',c.recipe?.sugar===1?'我尝到了，今天是清甜的。你给老配方添了自己的心思。':'这股甜味，我认得。广场以前总在这个时候热闹起来。'],['罗莎','鞋子和纸花也在等人。去吧，点心我替你看着。']];return [['罗莎','食谱上的面粉印，我认得。她做点心，总比别人多停一会儿。'],['罗莎','不必猜一个标准答案。照着记忆做一遍，再选选你今天想留下的味道。']];}
 if(key==='musician'){if(finished)return [['马特奥','听，最后那个音也回来了。原来她被记住的，不只是一个名字。'],['马特奥','我桌上还有一封未送出的信。你明晚还来吗？有个人，一直没等到回信。']];return [['马特奥',count?'每亮一盏灯，我就能多接上一小段。你愿意停下来听听吗？':'我只记得这支曲子的开头。她以前总一边补鞋，一边轻轻跟着哼。'],['马特奥',count?'你找到的小事，让这首曲子有了往下走的地方。':'看看那只红鞋吧。鞋带松了，系好它，也许有人会想起一段路。']];}
 if(finished)return [['阿玛','路已经亮了。你不必替她走完，只要让她知道有人同行。'],['阿玛','等她走进门，你还可以回广场坐坐。留灯的人，也值得歇一会儿。']];return [['阿玛','我在这里看灯。桥上的雾太深，她暂时辨不清回家的方向。'],['阿玛','把旧物里的小事亲手做一遍，再摊开手掌，把记忆交给桥灯。'],['阿玛',count?'你已经点亮了'+count+'盏。剩下的旧物不分先后，慢慢来。':'不用赶时间。鞋带可以重新系，纸也可以重新折。']];
}

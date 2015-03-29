/*javascript*/

var main = function(){

var moveLeft = 0;
var moveDown = 0;
$('div.box').hover(function(e) {
	
	var after_12 = (($(this).attr('style')).split(';'))[1].split(':');
	after_12 = after_12[1].replace('vh', '')
	var boxSize = (($(this).attr('style')).split(';'))[2].split(':');
	boxSize = boxSize[1].replace('vh', '');
	var height = window.innerHeight;
	//window.alert(after_12);
	
	var num = parseInt($(this).attr('data-popbox'));
	var target = '#' + ($(this).attr('data-popbox'));
 	
	moveLeft = $(this).outerWidth();
	moveDown = ($(target).outerHeight()-((height*parseInt(boxSize)/100)));
	//window.alert(moveDown);
	

	if (num >= 300) {
	  if (after_12 >= 34.09){
		$(target).css('top', -moveDown).css('left', -700);
	  } else {
 		$(target).css('top', 0).css('left', -700);
	  }
	} else if (after_12 >= 34.09 ) {
		$(target).css('top', -moveDown).css('left', moveLeft);
	} else {
		$(target).css('top', 0).css('left', moveLeft);
	};

	$(target).show();
	
	$(target).hover(function(){
		$(this).show();
	}, function(){
		$(this).hide();
	});
	
}, function() {
	var target = '#' + ($(this).attr('data-popbox'));
	
	$(target).hide();
}); 


function isOnScreen(element){
	var curPos = element.offset();
	var curLef = curPos.left;
	var divWidth = ($('div#wrapper').width())-50;
	return (curLef >= divWidth && curLef <= 0) ? false : true;
}


function shadow(){
	//getting window width and find center
	var mainWidth = $('div#wrapper').width();
	var VCenter = mainWidth/2;
	//window.alert(mainWidth);

	
	var box = $('div.box');
	
	var count = 0;
	for (var i=0, max=box.length; i<max; i++){
		
	  if (isOnScreen($(box[i]))) {
		count += 1;
		var boxP = $(box[i]).offset().left;
		var shadow = (VCenter - boxP)/50;

		//window.alert(shadow);
		if (boxP < VCenter){
			$(box[i]).css('box-shadow', -shadow+"px 0px 5px");
		} else {
			$(box[i]).css('box-shadow', -shadow+'px 0px 5px');
		};
	  };
	};
//window.alert(count);	
}


//shadow();

//$('div#wrapper').scroll(shadow);



function findHeight(){
	//window.alert('hello');
	var box = document.getElementsByClassName('box');
	var list = document.getElementsByClassName('TOuter');
	var TitleBar = document.getElementById('wrapper');
	var box0;
	//window.alert('hello');
	for (var i=0, max=box.length; i<max; i++){
		var start = (($(box[i]).attr('style')).split(';'))[1].split(':');
		start = start[1].replace('vh', '');
		if (start == 0){
			box0= box[i];
			break;
		} else {
			continue;
		};
	};
	var WH = window.innerHeight;
	var BY= $(box0).offset().top;
	var TY= $(TitleBar).offset().top;
	bY = ((BY - TY)/WH)*100;
	BY = (BY - TY)/WH;
	$(list).css('margin-top', bY+'vh');
	
}

findHeight();
$(window).resize(findHeight);

}

$(document).ready(main)



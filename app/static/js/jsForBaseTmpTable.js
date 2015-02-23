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
	

	if (num >= 400) {
		$(target).css('top', 0).css('left', 0);
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


function shadow(){
	//getting window width and find center
	var mainWidth = window.innerWidth;
	var VCenter = mainWidth/2;
	//window.alert(VCenter);

	
	var box = document.getElementsByClassName('box');
	//window.alert(box);
	for (var i=0, max=box.length; i<max; i++){
		var boxP = $(box[i]).offset().left;
		var shadow = (VCenter - boxP)/75;
		//window.alert((VCenter-boxP)/100);
		if (boxP < VCenter){
			$(box[i]).css('box-shadow', -shadow+"px 0px 5px");
		} else {
			$(box[i]).css('box-shadow', -shadow+'px 0px 5px');
		};
	};

	
}


shadow();

setInterval($('div#wrapper').scroll(shadow), 10);


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
	
	var LY= $(list).offset().top;
	
	LY = (LY - TY)/WH;
	
	//window.alert('y '+BY+' ly '+LY);
	//window.alert('Title '+TY);
	
}

findHeight();

/*
$("body").on("mouseover",function(){
$("#wrapper").on("mousewheel", function(e, delta) {	
	this.scrollLeft -= (delta);
	e.preventDefault();
}); 
});
*/		

}

$(document).ready(main)



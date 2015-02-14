/*javascript*/

var main = function(){

var moveLeft = 0;
var moveDown = 0;
$('div.box').hover(function(e) {
	
	
	var num = parseInt($(this).attr('data-popbox'));
	var target = '#' + ($(this).attr('data-popbox'));
 	var name = document.getElementById(num).innerHTML;
	//name = name.slice(0,15)
	//alert('innerhtml : ' + name.slice(0,16));

	moveLeft = $(this).outerWidth();
	moveDown = ($(target).outerHeight()-50);
	

	if (num >= 400) {
		$(target).css('top', 0).css('left', 0);
	} else if (name.slice(0,16) === "M3AAWG Night Out") {
		$(target).css('top', -moveDown).css('left', moveLeft);
	} else if (num%10 === 0) {
		$(target).css('top', 0).css('left', moveLeft);
	} else {
		$(target).css('top', -moveDown).css('left', moveLeft);
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


}

$(document).ready(main)



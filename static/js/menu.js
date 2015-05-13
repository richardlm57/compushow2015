$(document).ready(main);

var cont = 1;

function main(){
	$('.menu_bar').click(function(){
		
		if(cont == 1){
			$('nav').animate({
				left: '0'
			});
			cont = 0;
		}else{
			$('nav').animate({
				left:'-100%'
			});
			cont = 1;
		}
	});

	$('.submenu').click(function(){
		$(this).children('.hijos').slideToggle();

	});

}

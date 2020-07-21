// JavaScript Document
$(document).ready(function() {
	//Product listing -> show/hide bag and wishlist buttons on hover
	$(".prodImg").hover(function() {
		$(this).children(".prodActions").css({"display" : "flex"});
	}, function() {
		$(this).children(".prodActions").css({"display" : "none"});
		$(this).find(".prodSize").css({"display" : "none"});
	});
	
	//Product listing -> show/hide product sizing on hover of wish button
	$("a.btnBag").hover(function() {
		$(this).prev(".prodSize").css({"display" : "inline-block"});
		$(this).parent(".prodActions").css({"display" : "flex"});
	}, function() {
		//****
	});
	
	$(".homeNewArriCarousel").slick({
		nextArrow : $(".carouselNext"),
		infinite : true,
		slidesToShow : 4,
		prevArrow : "",
		responsive : [
			{
				breakpoint : 1024,
				settings : {
					slidesToShow : 3,
				},
			},
			{
				breakpoint : 600,
				settings : {
					slidesToShow : 2,
				},
			},
			{
				breakpoint : 480,
				settings : {
					slidesToShow: 1,
				}
			},
		],
	});
	
	$(".homeStyleGalleryCarousel").slick({
		nextArrow : $(".carouselNextSG"),
		infinite : true,
		slidesToShow : 4,
		prevArrow : "",
		responsive : [
			{
				breakpoint : 1024,
				settings : {
					slidesToShow : 3,
				},
			},
			{
				breakpoint : 600,
				settings : {
					slidesToShow : 2,
				},
			},
			{
				breakpoint : 480,
				settings : {
					slidesToShow: 1,
				}
			},
		],
	});
	
	$(".brandsCarousel").slick({
		nextArrow : $(".carouselNextBrands"),
		infinite : true,
		slidesToShow : 5,
		prevArrow : $(".carouselPrevBrands"),
		responsive : [
			{
				breakpoint : 1024,
				settings : {
					slidesToShow : 3,
				},
			},
			{
				breakpoint : 600,
				settings : {
					slidesToShow : 2,
				},
			},
			{
				breakpoint : 480,
				settings : {
					slidesToShow: 1,
				}
			},
		],
	});
	
	$(function() {
		var header = $(".headerHome");
		$(window).scroll(function() {
			var scroll = $(window).scrollTop();
			
			if(scroll >=50) {
				header.addClass('headerHomeScroll', 'fast');
			} else {
				header.removeClass('headerHomeScroll', 'fast');
			}
		});
	})
});


/*................................category....................................*/
 $(document).ready(function () {
        $(".sub > a").click(function() {
            var ul = $(this).next(),
                    clone = ul.clone().css({"height":"auto"}).appendTo(".mini-menu"),
                    height = ul.css("height") === "0px" ? ul[0].scrollHeight + "px" : "0px";
            clone.remove();
            ul.animate({"height":height});
            return false;
        });
           $('.mini-menu > ul > li > a').click(function(){
           $('.sub a').removeClass('active');
           $(this).addClass('active');
        }),
           $('.sub ul li a').click(function(){
           $('.sub ul li a').removeClass('active');
           $(this).addClass('active');
        });
    });

//   $( "#slider-range" ).on( "slidechange", function( event, ui ) {
//     console.log(ui.value);
// } );
$("#slider-range").slider({
  range: true, 
  min: 0,
  max: 9999,
  step: 4,
  slide: function( event, ui ) {
    $( "#min-price").html(ui.values[ 0 ]);
    
    suffix = '';
    if (ui.values[ 1 ] == $( "#max-price").data('max') ){
       suffix = ' +';
    }
    $( "#max-price").html(ui.values[ 1 ] + suffix);         
  }
})

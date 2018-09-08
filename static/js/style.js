$(function() {
    var images = ['1','2','3','4','5','6','7','8','9','10','11'];
    var num = Math.floor(Math.random() * images.length);

    $('.jumbotron').css({'background': 'url(/static/images/jumbotron/small_' + images[num] + '.jpg) no-repeat center'});
    $('.jumbotron').css({'background-size': 'cover'});
    $('.jumbotron').css({'border-radius': '0px'})
    setTimeout(function() {
		$('.arrow').css({'visibility':'visible'});
    },1000)
});

$(document).on('scroll', function (e) {
    if ($(document).scrollTop() > $('.jumbotron').height()) {
	  $(".navbar-logo").attr("src","/static/images/irsl_h_w.png")
      $(".navbar").removeClass("navbar-light");
      $(".navbar").removeClass("bg-faded");
      $(".navbar").addClass("navbar-inverse");
      $(".navbar").addClass("bg-inverse");      
      $(".hamburger").removeClass("hamburger-light");
    } else {
	  $(".navbar-logo").attr("src","/static/images/irsl_h_b.png")
      $(".navbar").removeClass("navbar-inverse");
      $(".navbar").removeClass("bg-inverse");
      $(".navbar").addClass("navbar-light");
      $(".navbar").addClass("bg-faded");      
      $(".hamburger").addClass("hamburger-light");
    }
});

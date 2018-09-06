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

//$(document).on('scroll', function (e) {
//    $('.navbar').css('opacity', ( (1-$(document).scrollTop()/500)>0.8 ? (1-$(document).scrollTop()/500) : 0.8));
//});

// $(document).on('scroll', function (e) {
//     if ($(window).width() > 991) {
//         $('.navbar-brand img').css('height', ((40-$(document).scrollTop()/40)>30 ? (40-$(document).scrollTop()/40) : 30));
//     }
// });
//
// $(document).on('scroll', function (e) {
//     if ($(window).width() > 991) {
//         $('#navbarNav').css('font-size', ((17-$(document).scrollTop()/200)>15 ? (17-$(document).scrollTop()/200) : 15));
//     }
// });

$(document).on('scroll', function (e) {
    if ($(document).scrollTop() > $('.jumbotron').height()) {
      console.log('1,black')
      $(".navbar").removeClass("navbar-faded");
      $(".navbar").removeClass("bg-faded");
      $(".navbar").addClass("navbar-inverse");
      $(".navbar").addClass("bg-inverse");
      $(".navbar-logo").attr("src","/static/images/irsl_h_w.png")
      $(".hamburger").addClass("hamburger-light");
    } else {
      console.log('white')
      $(".navbar").removeClass("navbar-inverse");
      $(".navbar").removeClass("bg-inverse");
      $(".navbar").addClass("navbar-faded");
      $(".navbar").addClass("bg-faded");
      $(".navbar-logo").attr("src","/static/images/irsl_h_b.png")
      $(".hamburger").removeClass("hamburger-light");
    }
});

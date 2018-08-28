$(function() {    
    var images = ['1','2','3','4','5','6','7','8','9','10','11'];
    var num = Math.floor(Math.random() * images.length);
    
    $('.jumbotron').css({'background': 'url(/static/images/jumbotron/k_' + images[num] + '.jpg) no-repeat center'});   
    $('.jumbotron').css({'background-size': 'cover'});
    $('.jumbotron').css({'border-radius': '0px'})    
    setTimeout(function() {
        $('.arrow').css({'visibility':'visible'});
    },1000)
});

//$(document).on('scroll', function (e) {
//    $('.navbar').css('opacity', ( (1-$(document).scrollTop()/500)>0.8 ? (1-$(document).scrollTop()/500) : 0.8));
//});

$(document).on('scroll', function (e) {
    if ($(window).width() > 991) {
        $('.navbar-brand img').css('height', ((40-$(document).scrollTop()/40)>30 ? (40-$(document).scrollTop()/40) : 30)); 
    }
    
});

$(document).on('scroll', function (e) {
    if ($(window).width() > 991) {
        $('#navbarNav').css('font-size', ((17-$(document).scrollTop()/200)>15 ? (17-$(document).scrollTop()/200) : 15));
    }
});

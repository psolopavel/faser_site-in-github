

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}
function currentSlide(n) {
    showSlides(slideIndex = n);
}
function showSlides(n){
    var i;
    var slides = document.getElementsByClassName("my-slader");
    var dots = document.getElementsByClassName("dot");

    if (n > slides.length){
        slideIndex = 1
    }
    if (n < 1){
        slideIndex=slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display='none';
    }
    for (i = 0; i < dots.length; i++){
        dots[i].className= dots[i].className.replace("active","");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}


$(document).ready(function(){
    $('.todo_active').click(function(){
        $('.sitebar,.image_pink').toggleClass('active');
    });
});
$(document).ready(function(){
    $('.tod_active').click(function(){
        $('.footer_conteiner').toggleClass('active');
    });
});
$(document).ready(function(){
    $('.change-theme').click(function(){
        $('body').toggleClass('active');
    });
});
$(document).ready(function(){
    $('.change-theme').click(function(){
        $('.sitebar,.header,#ponter,#ponter2,.text,.numbertext,.items_sitebar_MORE,#descriptin').toggleClass('darc');
    });
});
$(document).ready(function(){
    $('.btn').click(function(){
        alert('ви ТАКЖЕ можете посвонить продовцу')
    });
});









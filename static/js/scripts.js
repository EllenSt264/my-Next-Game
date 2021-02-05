$(document).ready(function () {
    $(window).on("load", function() {
        $('.sidenav').sidenav({ edge: "right" });
        $('.carousel.carousel-slider').carousel({
            fullWidth: true, 
            indicators: true,
            duration: 600
        });
        // https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay
        setInterval(function() {
            $('.carousel').carousel('next');
        }, 8000)
        $('.dropdown-trigger').dropdown();
    })
});
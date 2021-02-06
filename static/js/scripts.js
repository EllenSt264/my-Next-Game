$(document).ready(function () {
    $(window).on("load", function() {

        $('#hamburger').click(function(){
            $(this).toggleClass('open');
            $("#mobile-nav").css("width", "90%")

            $(".sidenav-overlay").click(function() {
                $("#hamburger").removeClass("open")
                $("#mobile-nav").css("width", '0')
            })

            $('#closeSideNav').click(function() {
                $("#hamburger").removeClass("open")
                $("#mobile-nav").css("width", '0')
            })

            if (!$(this).hasClass('open')) {
                $("#mobile-nav").css("width", '0')
            }
        });

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
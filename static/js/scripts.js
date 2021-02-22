$(document).ready(function () {
    $(window).on("load", function() {

        /* --------------------------------------- Materialize Initialization */


        /* --------------------------------------- Navbar */

        // Hamburger
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

        /* Side nav */
        $('.sidenav').sidenav({ edge: "right" });
        
        /* Dropdown */
        $('.dropdown-trigger').dropdown({constrainWidth: false, coverTrigger: false});

        /* Dropdown - Navbar */
        $('.nav-dropdown-trigger').dropdown({constrainWidth: false, coverTrigger: false, hover: true})


        
        /* --------------------------------------- Other */

        /* Parallax */
        $('.parallax').parallax();


        /* Carousel */
        $('.carousel.carousel-slider').carousel({
            fullWidth: true, 
            indicators: true,
            duration: 600
        });

            /* To initiate autoplay on the carousel, I looked to this source:
            "https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay" */

        setInterval(function() {
            $('.carousel').carousel('next');
        }, 8000)

        
        /* Collapsible */
        $('.collapsible').collapsible();
    })
});
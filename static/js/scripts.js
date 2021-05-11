$(document).ready(function () {

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
    $('.sidenav').sidenav({ edge: "left" });
    
    /* Dropdown */
    $('.dropdown-trigger').dropdown({constrainWidth: false, coverTrigger: false});

    /* Dropdown - Navbar */
    $('.nav-dropdown-trigger').dropdown({constrainWidth: false, coverTrigger: false, hover: true})


    
    /* --------------------------------------- Other */

    /* Parallax */
    $('.parallax').parallax();


    /* Carousel */
    $('.carousel').carousel({
        fullWidth: true, 
        indicators: true,
        duration: 600
    });

        /* To initiate autoplay on the carousel, I looked to this source:
        "https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay" */

    setInterval(function() {
        $('.carousel').carousel('next');
    }, 8000);

    /*  Carousel next arrow */
    $('#carousel-next a').on('click', function() {
        $('.carousel').carousel('next')
    });

    /*  Carousel prev arrow */
    $('#carousel-prev a').on('click', function() {
        $('.carousel').carousel('prev')
    });

    /* Modal */
    $('.modal').modal({
        endingTop: "25%"
    });

    $('#requestGame-confirmation').modal('open');

    $('#userRequests .modal').modal({
        endingTop: "10%"
    });

    /* To trigger Materialize tooltip on mouse click, rather than hover,
        I used the following source:
        "https://stackoverflow.com/questions/42524435/materialize-css-tooltip-shows-only-when-onclick" */

    /* Tooltip */
    $('#like-btn.tooltipped').on('click', function() {
        $(this).tooltip();
        $(this).tooltip('open');
    })

    $('#like-btn.tooltipped').on('mouseleave', function() {
        if ($(this).tooltip()) {
            $(this).tooltip('destroy');
        }
    })

    /* Navbar floating button */
    $('.fixed-action-btn').floatingActionButton({
        direction: 'right',
        hoverEnabled: false
    });

    $('#PlatformLink').on('click', function() {
        $('#GenreLink .fixed-action-btn').css('left', '225px')
    })

    $('#searchbar').on('click', function() {
        $('#searchbar .input-field').css('background-color', '#442c4c');
        $('#searchbar .input-field').css('z-index', '200');
    })


    /* --------------------------------------- Materialize forms */
    
    /* Collapsible */
    $('.collapsible').collapsible();


    /* Form select */
    $('select').formSelect();


    /* Form character count */
    $('textarea#summary, textarea#gameplay, textarea#visuals, textarea#sound').characterCounter();


    /* --------------------------------------- Enable input form button */

        /* Based upon the following source:
        "https://stackoverflow.com/questions/40404375/materialize-css-remove-disabled-input-field-not-working" */

    /* Display name input field */
    $('#allow-edit--displayName').on('click', function() {
        event.preventDefault();
        $('#edit-displayName').prop('disabled', false);
        $('.input-field--displayName').css({'background-color': 'rgb(170 170 170 / 0%)', 'border': 'none', 'color': 'rgb(210 210 210)'});
        $('.input-field--displayName > input::placeholder').css('color', 'rgb(175 175 175)');
        $('.input-field--displayName > label').css('color', 'rgb(175 175 175)');
        $('.input-field--displayName input').css('color', 'white');
    });

    /* Email input field */
    $('#allow-edit--email').on('click', function() {
        event.preventDefault();
        $('#edit-email').prop('disabled', false);
        $('.input-field--email').css({'background-color': 'rgb(170 170 170 / 0%)', 'border': 'none', 'color': 'rgb(210 210 210)'});
        $('.input-field--email > input::placeholder').css('color', 'rgb(175 175 175)');
        $('.input-field--email > label').css('color', 'rgb(175 175 175)');
        $('.input-field--email input').css('color', 'white');
    });

    /* First name input field */
    $('#allow-edit--fname').on('click', function() {
        event.preventDefault();
        $('#edit-fname').prop('disabled', false);
        $('.input-field--fname').css({'background-color': 'rgb(170 170 170 / 0%)', 'border': 'none', 'color': 'rgb(210 210 210)'});
        $('.input-field--fname > input::placeholder').css('color', 'rgb(175 175 175)');
        $('.input-field--fname > label').css('color', 'rgb(175 175 175)');
        $('.input-field--fname input').css('color', 'white');
    });
    
    /* Last name input field */
    $('#allow-edit--lname').on('click', function() {
        event.preventDefault();
        $('#edit-lname').prop('disabled', false);
        $('.input-field--lname').css({'background-color': 'rgb(170 170 170 / 0%)', 'border': 'none', 'color': 'rgb(210 210 210)'});
        $('.input-field--lname > input::placeholder').css('color', 'rgb(175 175 175)');
        $('.input-field--lname > label').css('color', 'rgb(175 175 175)');
        $('.input-field--lname input').css('color', 'white');
    });

    /*  Reset button */
    $('#reset-edits').on('click', function() {
        window.location.reload()
    });

    /* Remove disable attribute from inputs before submission */
    $('#saveChanges').on('click', function() {
        $('#edit-displayName').prop('disabled', false);
        $('#edit-email').prop('disabled', false);
        $('#edit-fname').prop('disabled', false);
        $('#edit-lname').prop('disabled', false);
    });

});
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

        /* Modal */
        $('.modal').modal({
            endingTop: "25%"
        });

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
        })
        
        /* --------------------------------------- JQuery UI Initialization */

        /*
            This code is based of the following sources:
            * "https://stackoverflow.com/questions/2909077/autocomplete-disallow-free-text-entry"
            * "https://www.encodedna.com/jquery/how-to-highlight-input-words-using-jqueryui-autocomplete-widget.htm"
            *  "https://www.encodedna.com/2013/08/jquery-autocomplete-dropdown-list-on-focus.htm"
        */

        /* Autocomplete */

        $('#query').autocomplete({
            source: gameData,   // Grabs game titles from data.js file
            scroll: true,
            // Disallow user input to only allow input that exists within the source data
            change: function (event, ui) {
                let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
                let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
                if (ui.item == null) {
                    $('#query').css(classInvalid);
                    event.currentTarget.value = '';
                    event.currentTarget.focus();
                }
                else {
                    $('#query').css(classValid);
                }
            }
        // Highlight results on hover/focus
        }).focus(function() {
            $(this).autocomplete("search", "");
        // Highlight input characters
        }).data("ui-autocomplete")._renderItem = function( ul, item ) {
            let txt = String(item.value).replace(new RegExp(this.term, "gi"),"<span class='highlight'>$&</span>");
            return $("<li></li>")
                .data("ui-autocomplete-item", item)
                .append("<a>" + txt + "</a>")
                .appendTo(ul);
        };

    })
});
$(document).ready(function() {
    /* --------------------------------------- JQuery UI Initialization */

    /*
        This code is based of the following sources:
        * "https://stackoverflow.com/questions/2909077/autocomplete-disallow-free-text-entry"
        * "https://www.encodedna.com/jquery/how-to-highlight-input-words-using-jqueryui-autocomplete-widget.htm"
        * "https://www.encodedna.com/2013/08/jquery-autocomplete-dropdown-list-on-focus.htm"
    */

    /* Autocomplete */

    $('#review-query').autocomplete({
        source: reviewData,   // Grabs game titles from data.js file
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
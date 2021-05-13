$(document).ready(function() {
    /* Autocomplete */
    $('#game-search, #nav-search, #review-search').autocomplete({
        source: gameData, // Grabs game titles from data.js file
        scroll: true,
        // Highlight results on hover/focus
    }).focus(function() {
        $(this).autocomplete("search", "");
        // Highlight input characters
    }).data("ui-autocomplete")._renderItem = function(ul, item) {
        let txt = String(item.value).replace(new RegExp(this.term, "gi"), "<span class='highlight'>$&</span>");
        return $("<li></li>")
            .data("ui-autocomplete-item", item)
            .append("<a>" + txt + "</a>")
            .appendTo(ul);
    };
});
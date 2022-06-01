const items = ['hola'];
function checkSegmentsIsEmty() {
    $(".emptySegment").remove();
    if ($(".segments .segment").length == 0) {
        var segment = $("<div class='emptySegment'>The List is empty now...</div>");
        $('.segments').append(segment);
        $('#clear').addClass('hidden');
    } else {
        $('#clear').removeClass('hidden');
    };
};

checkSegmentsIsEmty()
var elm = {};
checkSegmentsIsEmty();
$("#taskButton").on("click", function () {
    var inptVal = $("#taskArea").val().trim();
    segment = $("<div class='segment' id='seg" + countOfItems + "'><p>" + inptVal + "</p></div>"),
        panelWrap = $("<div class='panelWrap'><button class='left floated ui red button'>Delete</button><div class='right floated'><i class='star icon'></i><i class='check circle icon'></i></div></div>"),
        element = segment.append(panelWrap);
    appendTaskToList(element, inptVal.length, inptVal, countOfItems);
    $("#taskArea").val(""); // clearing teaxtarea value after creating task
    checkSegmentsIsEmty();
    if (inptVal.length != 0) {
        countOfItems++;
    };
});

function appendTaskToList(el, lengthStr, inptVal, segmentID) {
    if (lengthStr != 0) {
        elm.value = inptVal;
        elm.id = segmentID.toString();
        items.push(JSON.stringify(elm));
        $('.segments').prepend(el);
        localStorage.setItem("items", JSON.stringify(items));
    } else {
        $('.todoWrap .infoLabel').html("Sorry, tasks can`t be empty...");
        window.setTimeout(function () {
            $('.todoWrap .infoLabel').html("Short Task");
        }, 2500);
    };
};

$(document).on("click", ".segment .star", function () {
    toggleState($(this).parents(".segment"));
});

$(document).on("click", ".segment .check", function () {
    toggleDone($(this).parents(".segment"));
});
function toggleDone(domEl) {
    for (var i = 0; i < items.length; i++) {
        if (JSON.parse(items[i]).id == parseInt((domEl[0].id).match(/\d+$/)[0])) {
            var parseEl = JSON.parse(items[i]);
            parseEl.done = !parseEl.done;
            items[i] = JSON.stringify(parseEl);
            domEl.toggleClass('done');
            break;
        };
    };
    window.localStorage.clear();
    localStorage.setItem("items", JSON.stringify(items));
};
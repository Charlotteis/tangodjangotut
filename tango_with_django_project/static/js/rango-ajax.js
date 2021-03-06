$("#likes").click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get("/rango/like_category/", {category_id: catid}, function(data){
        $("#like_count").html(data);
        $("#likes").hide();
    });
});

$("#suggestion").keyup(function(){
    var query;
    query = $(this).val();
    $.get("/rango/suggest_category", {suggestion: query}, function(data){
        $("#cats").html(data);
    });
});

$('.rango-add').click(function(){
    var catid = $(this).attr("data-catid");
    var title = $(this).atrr("data-title");
    var url = $(this).attr("data-url");
    $.get('/rango/auto_add_page/', {category_id: catid, url: url, title: title}, function(data){
        $('#pages').html(data);
        $(this).hide();
    });
});

// Prevents anything from happening on form enter
$("#cat-search-form").submit(function(event) {
    event.preventDefault();
});

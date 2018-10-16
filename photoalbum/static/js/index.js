
$(function () {
    var like_button = $('.like_button');
    like_button.on('click', function (event) {
        var $photo_id = $(this).attr('data-photo');
        $(this).next('span').text(" Polubiłeś to zdjęcie!");
        $.ajax({
            url: "/like_photo",
            method: "GET",
            data: {photo_id: $photo_id}
        }).done(function(response){
            $(event.target).siblings('p').children('span').text(response)
        })
    })


});
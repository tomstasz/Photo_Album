
$(function () {
    var like_button = $('.like_button');
    like_button.on('click', function (event) {
        var $photo_id = $(this).attr('data-photo');
        var $like_message = $(this).next('span');
        var $is_liked = $like_message.hasClass('liked');


        $.ajax({
            url: "/like_photo",
            method: "GET",
            data: {photo_id: $photo_id, is_liked: $is_liked},
        }).done(function(response){
            response = JSON.parse(response);
            $(event.target).siblings('p').children('span').text(response.count_likes);
        });
        if($is_liked === false) {
            $like_message.text(" Polubiłeś to zdjęcie!");
        } else {
            $like_message.text("");

        }
        $like_message.toggleClass('liked');

    })


});
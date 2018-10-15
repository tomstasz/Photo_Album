
// document.addEventListener("DOMContentLoaded", function() {
//     var elements = document.querySelectorAll('.like');
//     for (var i= 0; i < elements.length; i++) {
//         elements[i].addEventListener('click', function() {
//             var counter_span = this.nextElementSibling.querySelector('.counter');
//             var counter = counter_span.innerText;
//             counter++;
//             counter_span.innerText = counter;
//             counter_span.parentElement.innerText += counter_span.dataset['text'];
//
//
//         }, {once: true});
//     }
// });

$(function () {
    var like_button = $('.like_button');
    like_button.on('click', function (event) {
        var $photo_id = $(this).attr('data-photo');
        $.ajax({
            url: "/like_photo",
            method: "GET",
            data: {photo_id: $photo_id}
        }).done(function(response){
            $(event.target).siblings('p').children('span').text(response)
        })
    })


});
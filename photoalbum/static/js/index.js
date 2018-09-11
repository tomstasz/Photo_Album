
document.addEventListener("DOMContentLoaded", function() {
    var elements = document.querySelectorAll('.like');
    for (var i= 0; i < elements.length; i++) {
        elements[i].addEventListener('click', function() {
            var counter_span = this.nextElementSibling.querySelector('.counter');
            var counter = counter_span.innerText;
            counter++;
            counter_span.innerText = counter;
            counter_span.parentElement.innerText += counter_span.dataset['text'];


        }, {once: true});
    }
});


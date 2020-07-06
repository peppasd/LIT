var cHeight = 0;

$('#myCarousel').on('slide.bs.carousel', function (e) {
    var $nextImage = null;

    $activeItem = $('.active.item', this);

    if (e.direction == 'left'){
        $nextImage = $activeItem.next('.item').find('img');
    } else {
        if ($activeItem.index() == 0){
            $nextImage = $('img:last', $activeItem.parent());
        } else {
            $nextImage = $activeItem.prev('.item').find('img');
        }
    }

    // prevents the slide decrease in height
    if (cHeight == 0) {
       cHeight = $(this).height();
       $activeItem.next('.item').height(cHeight);
    }

    // prevents the loaded image if it is already loaded
    var src = $nextImage.data('lazy-load-src');

    if (typeof src !== "undefined" && src != "") {
       $nextImage.attr('src', src)
       $nextImage.data('lazy-load-src', '');
    }
});
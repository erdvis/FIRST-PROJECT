$(window).on('scroll', function() {
    var scrollTop = $(this).scrollTop();
    if (scrollTop > 200) { // adjust the number to the scroll position where you want the text to appear
      $('.spinner-border.g-item').addClass('show');
    } else {
      $('.spinner-border.g-item').removeClass('show');
    }
  });
  
$(function() {
  profilePages = ['.history-block', '.news-block'];

  actionButton.addEventListener('click', function openActions() {
    // for (var i=0; i < profilePages.length; i++) {
    //   if (i == '.history-block') {
    //     continue;
    //   }
    //
    //   else {
    //     $(i).addClass('d-none');
    //   }
    // }
    $(".news-block").removeClass('d-block');
    $(".news-block").addClass('d-none');
    $(".history-block").removeClass('d-none');
    $(".history-block").addClass('d-block');
    return 0;
  });

  newsButton.addEventListener('click', function openNews() {
    $(".history-block").removeClass('d-block');
    $(".history-block").addClass('d-none');
    $(".news-block").removeClass('d-none');
    $(".news-block").addClass('d-block');
    return 0;
  });

});

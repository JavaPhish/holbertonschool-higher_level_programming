const $ = window.$;
$('HEADER').removeClass('green').addClass('red');
$('DIV#toggle_header').click(function () {
  if ($('HEADER').attr('class') === 'green') {
    $('HEADER').removeClass('green').addClass('red');
  } else {
    $('HEADER').removeClass('red').addClass('green');
  }
});

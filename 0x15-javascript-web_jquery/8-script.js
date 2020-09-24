const $ = window.$;
// This one was poorly worded but i believe this is the correct output :)
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (films) {
    $.each(films.results, function (i, film) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  }
});

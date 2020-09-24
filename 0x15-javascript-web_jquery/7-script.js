const $ = window.$;
// This one was poorly worded but i believe this is the correct output :)
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (people) {
    $('#character').text(people.name);
  }
});

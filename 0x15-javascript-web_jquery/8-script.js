/*  a Javascript script that fetches and lists all movies title by using this
    URL: https://swapi-api.hbtn.io/api/films/?format=json
*/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  data.results.forEach(element => {
    $('#list_movies').append(`<li>${element.title}</li>`);
  });
});

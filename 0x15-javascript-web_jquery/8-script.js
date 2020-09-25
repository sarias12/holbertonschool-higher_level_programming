#!/usr/bin/node
/*
script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
*/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let index = 0; index < data.results.length; index++) {
    $('UL#list_movies').append('<li>' + data.results[index].title + '</li>');
  }
});

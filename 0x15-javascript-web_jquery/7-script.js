#!/usr/bin/node
/*
script that fetches the name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
*/
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});

#!/usr/bin/node
/*
Script that prints the number of movies where the character “Wedge Antilles” is present.
*/
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = JSON.parse(body);
    let number = 0;
    for (let index = 0; index < dict.results.length; index++) {
      for (let index2 = 0; index2 < dict.results[index].characters.length; index2++) {
        if (dict.results[index].characters[index2].includes('/18/')) {
          number += 1;
        }
      }
    }
    console.log(number);
  }
});

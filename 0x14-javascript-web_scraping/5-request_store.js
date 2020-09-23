#!/usr/bin/node
/*
Script that gets the contents of a webpage and stores it in a file.
*/
const request = require('request');
const url = process.argv[2];
let text = '';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    text = body.toString();
    const fs = require('fs');
    fs.writeFile(process.argv[3], text, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});

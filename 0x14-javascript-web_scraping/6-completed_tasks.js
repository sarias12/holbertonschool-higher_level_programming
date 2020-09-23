#!/usr/bin/node
/*
Script that computes the number of tasks completed by user id.
*/
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    const dict = {};
    for (let index = 0; index < list.length; index++) {
      if (list[index].completed === true) {
        if (dict[list[index].userId]) {
          dict[list[index].userId] += 1;
        } else {
          dict[list[index].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});

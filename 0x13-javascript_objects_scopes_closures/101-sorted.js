#!/usr/bin/node
/*
Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
*/
const data = require('./101-data');
const dict = data.dict;
const dict2 = {};
for (const key in dict) {
  const value = dict[key];
  dict2[value] = [];
}
for (const key in dict) {
  const value = dict[key];
  dict2[value].push(key);
}
console.log(dict2);

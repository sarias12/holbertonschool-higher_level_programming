#!/usr/bin/node
/*
Script  that imports an array and computes a new array.
*/
const data = require('./100-data');
const map1 = data.list.map(x => x * data.list.indexOf(x));
console.log(data.list);
console.log(map1);

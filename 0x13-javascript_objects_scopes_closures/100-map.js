#!/usr/bin/node
/*
Script  that imports an array and computes a new array.
*/
const data = require('./100-data');
let num1 = 0;
const map1 = data.list.map(function (num) {
  const num2 = num * num1;
  num1 += 1;
  return (num2);
});
console.log(data.list);
console.log(map1);

#!/usr/bin/node
/*
script that prints the addition of 2 integers
*/
function add (a, b) {
  console.log(a + b);
}
if (process.argv.length < 4) {
  console.log('NaN');
} else {
  const a = parseInt(process.argv[2], 10);
  const b = parseInt(process.argv[3], 10);
  add(a, b);
}

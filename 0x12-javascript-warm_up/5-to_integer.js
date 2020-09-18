#!/usr/bin/node
/*
script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer.
*/
let argv1 = process.argv[2];
argv1 = parseInt(argv1, 10);
if (Number.isNaN(argv1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv1);
}

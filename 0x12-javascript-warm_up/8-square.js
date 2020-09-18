#!/usr/bin/node
/*
script that prints a square
*/
let argv1 = process.argv[2];
argv1 = parseInt(argv1, 10);
if (Number.isNaN(argv1) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv1; i++) {
    let str = '';
    for (let j = 0; j < argv1; j++) {
      str += 'X';
    }
    console.log(str);
  }
}

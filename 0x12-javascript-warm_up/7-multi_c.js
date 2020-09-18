#!/usr/bin/node
/*
script that prints x times “C is fun”.
*/
let argv1 = process.argv[2];
argv1 = parseInt(argv1, 10);
if (Number.isNaN(argv1) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv1; i++) {
    console.log('C is fun');
  }
}

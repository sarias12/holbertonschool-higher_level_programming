#!/usr/bin/node
/*
Script that prints the first argument passed to it.
*/
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  const argvs = process.argv.slice(2);
  console.log(argvs[0]);
}

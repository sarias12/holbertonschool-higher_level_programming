#!/usr/bin/node
/*
Script that prints the first argument passed to it.
*/
if (process.argv.length === 2) {
  console.log('No argument');
} else {
  const argvs = process.argv.slice(2);
  console.log(argvs[0]);
}

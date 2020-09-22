#!/usr/bin/node
/*
Script that returns the number of occurrences in a list.
*/
exports.nbOccurences = function (list, searchElement) {
  let macthes = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      macthes += 1;
    }
  }
  return (macthes);
};

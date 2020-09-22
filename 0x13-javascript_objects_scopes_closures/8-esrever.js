#!/usr/bin/node
/*
Script that returns the reversed version of a list.
*/
exports.esrever = function (list) {
  const reversedlist = [];
  for (let index = list.length - 1; index >= 0; index--) {
    reversedlist.push(list[index]);
  }
  return (reversedlist);
};

#!/usr/bin/node
/*
Script that defines a square and inherits from Rectangle.
*/
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    let char = c;
    if (!char) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += char;
      }
      console.log(str);
    }
  }
}
module.exports = Square;

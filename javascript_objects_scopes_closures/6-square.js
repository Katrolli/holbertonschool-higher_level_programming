#!/usr/bin/node
const Sq1 = require('./5-square');

class Square extends Sq1 {
  charPrint (c = 'x') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;

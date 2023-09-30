#!/usr/bin/node

const SquareM = require('./5-square.js');

class Square extends SquareM {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let v = c;
    if (!c) {
      v = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(v.repeat(this.width));
    }
  }
}

module.exports = Square;

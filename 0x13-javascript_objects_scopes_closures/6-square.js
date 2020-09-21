#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.name = 'Square';
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;

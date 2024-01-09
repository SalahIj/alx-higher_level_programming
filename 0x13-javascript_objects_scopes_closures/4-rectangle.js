#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const str = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(str.repeat(this.width));
    }
  }

  rotate () {
    let exchange = 0;
    exchange = this.width;
    this.width = this.height;
    this.height = exchange;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;

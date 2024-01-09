#!/usr/bin/node
let argn = 0;
exports.logMe = function (item) {
  console.log(`${argn}: ${item}`);
  argn = argn + 1;
};

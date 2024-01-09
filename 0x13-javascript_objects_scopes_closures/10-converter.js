#!/usr/bin/node
exports.converter = function (base) {
  function conver (num) {
    return num.toString(base);
  }
  return conver;
};

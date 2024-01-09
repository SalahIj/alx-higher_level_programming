#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((cou, current) => current === searchElement ? cou + 1 : cou, 0);
};

#!/usr/bin/node
const Dict = require('./101-data').dict;
const newD = {};

for (const i in Dict) {
  if (newD[Dict[i]] === undefined) {
    newD[Dict[i]] = [];
  }
  newD[Dict[i]].push(i);
}
console.log(newD);

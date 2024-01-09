#!/usr/bin/node
const { list } = require('./100-data');
console.log(list);
console.log(list.map((ele, indx) => ele * indx));

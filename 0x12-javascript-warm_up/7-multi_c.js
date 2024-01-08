#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let j = 0;
  while (j < x) {
    console.log('C is fun');
    j++;
  }
}

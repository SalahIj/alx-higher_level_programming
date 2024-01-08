#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  const size = arr.length;
  const list = arr.sort();
  console.log(list[size - 2]);
}

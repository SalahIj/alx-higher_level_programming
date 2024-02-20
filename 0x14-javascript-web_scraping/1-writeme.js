#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  process.exit(1);
}

const Path = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(Path, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});

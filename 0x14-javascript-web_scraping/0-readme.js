#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 3) {
  process.exit(1);
}

const Path = process.argv[2];

fs.readFile(Path, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

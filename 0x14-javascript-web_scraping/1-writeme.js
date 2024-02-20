#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  process.exit(1);
}

const Path = process.argv[2];

fs.writeFile(Path, process.argv[3], 'utf-8', function (err) {
  if (err) {
    console.error(err);
  }
});

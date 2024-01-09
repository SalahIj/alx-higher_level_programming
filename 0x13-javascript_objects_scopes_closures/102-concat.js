#!/usr/bin/node
const fs = require('fs');
const filea = process.argv[2];
const fileb = process.argv[3];
const filec = process.argv[4];

const dataa = fs.readFileSync(filea, { encoding: 'utf8' });
const datab = fs.readFileSync(fileb, { encoding: 'utf8' });
fs.writeFileSync(filec, dataa + datab, { encoding: 'utf8' });

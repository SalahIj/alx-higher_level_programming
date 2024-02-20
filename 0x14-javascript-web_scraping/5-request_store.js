#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`${process.argv[3]}`);
      }
    });
  }
});

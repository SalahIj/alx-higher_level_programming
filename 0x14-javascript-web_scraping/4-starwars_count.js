#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const puss = JSON.parse(body).results;
    console.log(puss.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});

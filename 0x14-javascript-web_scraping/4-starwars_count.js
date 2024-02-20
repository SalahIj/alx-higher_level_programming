#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const Urlapi = process.argv[2];

request.get(Urlapi, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});

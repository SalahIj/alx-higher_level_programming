#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});

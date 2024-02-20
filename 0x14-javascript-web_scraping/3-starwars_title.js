#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const Idofmovie = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${Idofmovie}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});

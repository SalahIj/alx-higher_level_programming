#!/usr/bin/node

const request = require('request');

const lien = `https://swapi.dev/api/films/${process.argv[2]}/`;

request(lien, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
    movie.characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else {
          const Cah = JSON.parse(body);
          console.log(Cah.name);
        }
      });
    });
  }
});

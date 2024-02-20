#!/usr/bin/node

const request = require('request');

const lien = `https://swapi.dev/api/films/${process.argv[2]}/`;

request(lien, function (error, response, body) {
  if (!error) {
    const movie = JSON.parse(body);
    const Cah = movie.characters;

    const Charactersfetched = function (liens, pos = 0) {
      if (pos >= liens.length) return;
      request(liens[pos], (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else {
          const charr = JSON.parse(body);
          console.log(charr.name);
          Charactersfetched(liens, pos + 1);
        }
      });
    };
    Charactersfetched(Cah);
  } else {
    console.error('Error:', error);
  }
});

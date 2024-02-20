#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const Urlapi = process.argv[2];
const Idofcharacter = '18';

request.get(Urlapi, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    const URL = `https://swapi-api.alx-tools.com/api/people/${Idofcharacter}/`;
    const films = JSON.parse(body).results;
    const WedgeAntillesfilm = films.filter(film =>
      film.characters.includes(URL)
    );
    console.log(WedgeAntillesfilm.length);
  }
});

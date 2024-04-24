#!/usr/bin/node

const request = require('request');
const Fid = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${Fid}`;

function fetchMovie(url) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const film = JSON.parse(body);
      const characters = film.characters;
      characters.forEach(url => fetchCharacter((url)));
    }
  });
}

function fetchCharacter(url) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
    }
  });
}

fetchMovie(url);
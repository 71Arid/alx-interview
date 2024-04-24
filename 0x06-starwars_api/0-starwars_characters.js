#!/usr/bin/node

const request = require('request');
f_id = process.argv[2];

let url = `https://swapi-api.alx-tools.com/api/films/${f_id}`;

function fetchMovie(url) {
    request(url, (error, response, body) => {
        if (!error && response.statusCode == 200) {
            const film = JSON.parse(body);
            const characters = film.characters;
            characters.forEach(url => fetchCharacter((url)));
        }
    });
}

function fetchCharacter(url) {
    request(url, (error, response, body) => {
        if (!error && response.statusCode == 200) {
            const character = JSON.parse(body);
            console.log(character.name);
        }
    });
}

fetchMovie(url);
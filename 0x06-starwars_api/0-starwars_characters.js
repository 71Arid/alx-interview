#!/usr/bin/node

const request = require('request');
const Fid = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${Fid}`;

function fetchMovie (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const film = JSON.parse(body);
    const characters = film.characters;
    const charactersNames = characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, _, body) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      })
    );
    Promise.all(charactersNames)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  });
}

fetchMovie(url);

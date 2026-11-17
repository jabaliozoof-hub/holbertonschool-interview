#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacter(characters, 0);
  }
});

function printCharacter (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      printCharacter(characters, index + 1);
    }
  });
}

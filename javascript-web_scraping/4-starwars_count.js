#!/usr/bin/node

const request = require('request');

const apiCall = process.argv[2];

function getMovies(call) {
  request.get(call, function (error, response, body) {
    if (error) {
      console.log('error', error);
    } else {
      const search = JSON.parse(body).results[0].characters;
      const char = String(search[15]);
      request.get(char, function (error, response, body) {
        if (error) {
          console.log('error', error);
        } else {
          const films = JSON.parse(body).films;
          console.log(`${films.length}`);
        }
      });
    }
  });
}

getMovies(apiCall);

// request.get(call, function (error, response, body) {
//   if (error) {
//     console.log('error', err);
//   } else {
//     const movies = JSON.parse(body).results;
//   }
// });

#!/usr/bin/node

const request = require('request');

const apiCall = process.argv[2];

function getMovies (call) {
  request.get(call, function (error, response, body) {
    const search = JSON.parse(body).results[0].characters;
    const char = String(search[15]);
    request.get(char, function (error, response, body) {
      const films = JSON.parse(body).films;
      console.log(`${films.length}`);
    });
  });
  clear;
}

getMovies(apiCall);

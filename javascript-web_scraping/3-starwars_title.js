#!/usr/bin/node

const request = require('request');
const id = Number(process.argv[2]);

const apiCall = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(apiCall, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});

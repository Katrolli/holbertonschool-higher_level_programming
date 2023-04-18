#!/usr/bin/node

const url = String(process.argv[2]);

const request = require('request');

request.get(url, function (error, response, status) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});

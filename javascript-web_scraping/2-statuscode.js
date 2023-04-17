#!/usr/bin/node

const url = String(process.argv[2]);

const request = require('request');

request.get(url, function (error, response, status) {
  console.log('code:', response.statusCode);
});

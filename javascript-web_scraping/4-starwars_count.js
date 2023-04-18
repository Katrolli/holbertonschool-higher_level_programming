#!/usr/bin/node

const request = require('request');

const apiCall = process.argv[2];

request.get(apiCall, function (error, response, body) {
  if (error) {
    console.log('error', error);
  } else {
    const data = JSON.parse(body).results;

    let count = 0;

    for (const info of data) {
      for (const chars of info.characters) {
        if (chars.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

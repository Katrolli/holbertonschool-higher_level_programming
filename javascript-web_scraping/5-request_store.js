#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const apiCall = process.argv[2];
const fileToWrite = process.argv[3];

request.get(apiCall, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileToWrite, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});

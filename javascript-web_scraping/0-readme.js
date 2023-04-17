#!/usr/bin/node

const fileToRead = String(process.argv[2]);

const fs = require('fs');

fs.readFile(fileToRead, 'utf-8', (data, error) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});

#!/usr/bin/node

const fileToWrite = process.argv[2];
const stringToWrite = String(process.argv[3]);

const fs = require('fs');

fs.writeFile(fileToWrite, stringToWrite, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});

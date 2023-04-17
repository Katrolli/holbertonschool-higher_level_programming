#!/usr/bin/node

const fileToRead = process.argv[2];

const fs = require('fs').promises;

async function readFile (filepath) {
  try {
    const data = await fs.readFile(filepath);
    console.log(data.toString());
  } catch (error) {
    console.log(error);
  }
}

readFile(fileToRead);

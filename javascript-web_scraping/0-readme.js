#!/usr/bin/node

const fileToRead = process.argv[2];

const fs = require('fs').promises;

async function readFile(filepath) {
  try {
    const data = await fs.readFile(filepath, 'utf-8');
    console.log(data.toString());
  } catch (error) {
    console.log(error);
  }
}

readFile(fileToRead);

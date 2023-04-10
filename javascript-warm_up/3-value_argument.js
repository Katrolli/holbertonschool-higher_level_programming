#!/usr/bin/node
import { argv } from 'node:process';

let count = 0;

for (let i = 0; argv[i] != null; i++) {
  count++;
}

let i = 0;
while (i < count) {
  if (i === 0) {
    i += 2;
  }
  if (i + 1 > count) {
    console.log('No argument');
    break;
  } else {
    console.log(argv[i]);
    i += 1;
  }
}

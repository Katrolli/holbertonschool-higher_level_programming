#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
}
function find_big (array) {
  let nr = 0;
  let i = 2;
  while (array[i] != null) {
    if (array[i] < array[i + 1]) {
      nr = array[i + 1];
      i++;
    }
    i++;
  }
  return nr;
}

for (let i = 2; argv[i] != null; i++) {
  if (argv[i] == find_big(argv) - 1) {
    console.log(argv[i]);
    break;
  }
}

#!/usr/bin/node

let arg = process.argv[2];

arg = Number(arg);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number(arg)}`);
}

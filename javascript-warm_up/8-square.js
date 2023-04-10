#!/usr/bin/node

const n = Number(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
}

for (let i = 0; i < n; i++) {
  let row = '';
  for (let j = 0; j < n; j++) {
    row += 'X';
  }
  console.log(row);
}

#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let nums = argv.slice(2);
  const max = Math.max(...nums);
  nums = nums.filter((nr) => nr < max);
  const secondMax = Math.max(...nums);
  console.log(secondMax);
}

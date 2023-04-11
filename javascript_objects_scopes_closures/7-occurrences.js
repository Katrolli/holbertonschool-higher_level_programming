#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const elements of list) {
    if (searchElement === elements) {
      count += 1;
    }
  }
  return count;
};

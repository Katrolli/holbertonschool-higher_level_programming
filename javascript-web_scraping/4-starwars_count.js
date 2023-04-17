#!/usr/bin/node

const request = require('request');

const apiCall = process.argv[2];

// function getMovies(call) {
//   request.get(call, function (error, response, body) {
//     if (error) {
//       console.log('error', error);
//     } else {
//       const search = JSON.parse(body).results[0].characters;
//       const char = String(search[15]);
//       request.get(char, function (error, response, body) {
//         if (error) {
//           console.log('error', error);
//         } else {
//           const films = JSON.parse(body).films;
//           console.log(`${films.length}`);
//         }
//       });
//     }
//   });
// }

// getMovies(apiCall);

request.get(apiCall, function (error, response, body) {
  if (error) {
    console.log('error', err);
  } else {
    const data = JSON.parse(body).results;

    let count = 0;

    for (const info of data) {
      for (const chars of info.characters) {
        if (chars.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

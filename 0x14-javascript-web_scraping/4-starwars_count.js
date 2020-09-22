#!/usr/bin/node

const request = require('request');
let count = 0;
const IdToCheck = 'https://swapi-api.hbtn.io/api/people/18/';
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) throw err;

  JSON.parse(body).results.forEach(function (item, index) {
    item.characters.forEach(function (item, index) {
      if (item === IdToCheck) {
        count++;
      }
    });
  });
  console.log(count);
});

#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (err) throw err;
  const dataIds = JSON.parse(body).characters;
  dataIds.forEach(function (item, index) {
    request(item, function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  });
});

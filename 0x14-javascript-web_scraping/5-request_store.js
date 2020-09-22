#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, function (err) {
    if (err) console.log(err);
  });
});

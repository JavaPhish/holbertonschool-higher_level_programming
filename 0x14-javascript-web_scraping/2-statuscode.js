#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) throw err;
  console.log('code: ' + res.statusCode);
});

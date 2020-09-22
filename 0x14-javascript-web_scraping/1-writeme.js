#!/usr/bin/node

const fs = require('fs');

// file1
fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) console.log(err);
});

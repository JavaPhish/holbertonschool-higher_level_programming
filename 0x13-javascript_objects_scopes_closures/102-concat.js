#!/usr/bin/node

const fs = require('fs');

// file1
const file1 = (fs.readFileSync(process.argv[2])).toString();

// file2
const file2 = (fs.readFileSync(process.argv[3])).toString();

// New file
const content = file1 + file2;
fs.writeFile(process.argv[4], content, function (err) {
  if (err) throw err;
});

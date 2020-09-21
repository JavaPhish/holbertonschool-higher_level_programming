#!/usr/bin/node

const ids = require('./101-data').dict;

const ndic = {};
for (const key in ids) {
  if (ndic[ids[key]] === undefined) {
    ndic[ids[key]] = [];
    ndic[ids[key]].push(key);
  } else {
    ndic[ids[key]].push(key);
  }
}
console.log(ndic);

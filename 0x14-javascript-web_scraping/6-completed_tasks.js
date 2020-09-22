#!/usr/bin/node

const request = require('request');
const taskDict = {};

request(process.argv[2], function (err, res, body) {
  if (err) throw err;
  const data = JSON.parse(body);
  data.forEach(function (item, index) {
    if (item.completed === true) {
      if (taskDict[item.userId] === undefined) {
        taskDict[item.userId] = 1;
      } else {
        taskDict[item.userId]++;
      }
    }
  });
  console.log(taskDict);
});

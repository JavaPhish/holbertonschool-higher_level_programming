#!/usr/bin/node

exports.esrever = function (list) {
  for (let x = 0; x < list.length / 2; x++) {
    [list[x], list[list.length - x - 1]] = [list[list.length - x - 1], list[x]];
  }

  return list;
};

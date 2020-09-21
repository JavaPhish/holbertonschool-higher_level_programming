#!/usr/bin/node

exports.converter = function (base) {
  return function myConverter (num) {
    return num.toString(base);
  };
};

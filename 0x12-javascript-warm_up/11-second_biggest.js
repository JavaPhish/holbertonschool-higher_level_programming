#!/usr/bin/node

if (process.argv.length > 3) {
  let argN = process.argv.splice(2).map(Number);
  argN = [...new Set(argN)];
  argN.sort();
  console.log(argN[argN.length - 2]);
} else {
  console.log(0);
}

#!/usr/bin/node

if (process.argv.length > 3) {
  const argN = process.argv.splice(2).map(Number);
  argN.sort();
  console.log(argN[argN.length - 2]);
} else {
  console.log(0);
}

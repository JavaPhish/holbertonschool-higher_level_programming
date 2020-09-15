#!/usr/bin/node

if (Number(process.argv[2])) {
  console.log(factor(process.argv[2]));
} else {
  console.log(1);
}

function factor (num) {
  if (num !== 1 && num !== 0) {
    return (num * factor(num - 1));
  }
  return 1;
}

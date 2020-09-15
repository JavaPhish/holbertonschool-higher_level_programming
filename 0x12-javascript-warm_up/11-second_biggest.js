#!/usr/bin/node

if (Number(process.argv[2]) && Number(process.argv[2]) !== 1) {
  let max = process.argv[2];
  let sec = process.argv[3];

  for (let x = 2; x < process.argv.length; x++) {
    if (Number(process.argv[x]) > max) {
      max = process.argv[x];
    }
  }

  for (let x = 2; x < process.argv.length; x++) {
    if (Number(process.argv[x]) > sec && process.argv[x] !== max) {
      sec = process.argv[x];
    }
  }

  console.log(sec);
} else {
  console.log(0);
}

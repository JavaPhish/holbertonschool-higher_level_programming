#!/usr/bin/node

if (Number(process.argv[2])) {
  for (let x = 0; x < process.argv[2]; x++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node
const char = 'X';
const num = process.argv[2];
if (parseInt(num)) {
  for (let i = 0; i < num; i++) {
    console.log(char.repeat(num));
  }
} else {
  console.log('Missing size');
}

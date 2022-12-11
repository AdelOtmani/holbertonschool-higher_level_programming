#!/usr/bin/node
let str;
if (process.argv.length< 3) {
  str = 'No argument';
} else if (process.argv.length === 3) {
  str = 'Argument found';
} else {
  str = 'Argu found';
}
console.log(str);

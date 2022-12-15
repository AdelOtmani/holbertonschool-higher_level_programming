#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, rep, num) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(num);
  let count = 0;
  for (const elem of data.results) {
    for (const people of elem.characters) {
      if (people.includes(18)) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});

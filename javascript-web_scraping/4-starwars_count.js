#!/usr/bin/node
const request = require('request');
let count = 0;
request.get(process.argv[2], function (error, rep, num) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(num);
  for (let i = 0; data.results[i] !== undefined; i++) {
    if (data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count = count + 1;
    }
  }
  console.log(count);
});

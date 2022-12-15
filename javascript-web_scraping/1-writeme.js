#!/usr/bin/node
const fs = require('fs');
fs.appendFile(process.argv[2], process.argv[3], function (error, content) {
  if (error) {
    console.log(error);
  }
  console.log(content);
});

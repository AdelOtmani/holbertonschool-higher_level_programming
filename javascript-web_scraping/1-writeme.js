#!/usr/bin/node
const fs = require('fs');
fs.appendFile(process.argv[2], process.argv[3], function (content) {
  console.log(content);
});

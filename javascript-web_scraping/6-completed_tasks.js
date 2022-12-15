#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tab = JSON.parse(body);
    const list = {};
    for (const i of tab) {
      if (i.completed === true) {
        if (i.userId in list) {
          list[i.userId]++;
        } else {
          list[i.userId] = 1;
        }
      }
    }
    console.log(list);
  }
});

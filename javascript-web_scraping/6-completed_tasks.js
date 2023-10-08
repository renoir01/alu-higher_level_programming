#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const result = {};

request.get(url, (err, resp, body) => {
  if (err) {
    throw err;
  }
  body = JSON.parse(body);
  body.forEach((item, index) => {
    if (item.completed) {
      if (result[item.userId]) {
        result[item.userId]++;
      } else {
        result[item.userId] = 1;
      }
    }
  });
  console.log(result);
});

#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (err, resp, body) => {
  if (err) {
    throw err;
  }

  fs.writeFile(fileName, body, (err) => {
    if (err) {
      throw err;
    }
  });
});

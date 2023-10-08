#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], (err, resp) => {
  if (err) {
    throw err;
  }
  console.log(resp.toString());
});

#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], (errA, dataA) => {
  if (errA) throw errA;
  fs.readFile(process.argv[3], (errB, dataB) => {
    if (errB) throw errB;
    fs.writeFile(process.argv[4], dataA + dataB, (errC) => {
      if (errC) throw errC;
    });
  });
});

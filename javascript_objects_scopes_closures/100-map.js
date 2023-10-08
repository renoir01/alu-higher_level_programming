#!/usr/bin/node
const list = require('./100-data.js').list;
const moddedList = list.map((x, index) => x * index);
console.log(list);
console.log(moddedList);
exports.list = [1, 2, 3, 4, 5];

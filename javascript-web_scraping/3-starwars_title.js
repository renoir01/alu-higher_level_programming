#!/usr/bin/node
const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api/films/:id';
request.get(endpoint.replace(':id', process.argv[2]), (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});

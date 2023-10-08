#!/usr/bin/node

const x = parseInt(process.argv[2]);

console.log(factorial(x));

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }

  return num * factorial(num - 1);
}

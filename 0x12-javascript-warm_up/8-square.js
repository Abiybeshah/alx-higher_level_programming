#!/usr/bin/node
/* print a square */
const size = process.argv[2];

if (size === undefined || isNaN(parseint(size))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(size); i++) {
    for (let j = 0; j < parseInt(size); j++) {
      row += x;
    }
    console.log(row);
  }

}

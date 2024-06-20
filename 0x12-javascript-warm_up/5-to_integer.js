#!/usr/bin/node
/* write a script that prints an int */
const args = process.argv[2];

if (args === undefined || isNaN(parseInt(args))) {
  console.log('Not a number');

} else {
  console.log('My number: ' + parseInt(args));
}

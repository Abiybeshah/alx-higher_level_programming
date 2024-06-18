#!/usr/bin/node
/* value of my argument */
const argc = process.argv;
if (argc.length <= 2) {
  console.log('No argument');
}
console.log(argc[3]);

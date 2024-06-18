#!/usr/bin/node
/* value of my argument */
const argc = process.argv;
if (argc.length <= 2) {
  console.log('No argument');
} else {
  console.log(argc[3]);
}

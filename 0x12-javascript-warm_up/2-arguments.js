#!/usr/bin/node
/* arguments on javascript */
const args = process.argv;
if (args.length <= undefined) {
	console.log('No argument');
} else if (args.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

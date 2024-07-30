#!/usr/bin/node
#task 2
const request = require('request');

request(process.argv[2], function (_err, res) {
    console.log('code:', res.statusCode); // Print the response status code if a response was received
});

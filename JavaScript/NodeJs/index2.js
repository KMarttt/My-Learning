// console.log("global.luckyNumber: ", global.luckyNumber);

// global.luckyNumber = 7;

// console.log("global.luckyNumber: ", global.luckyNumber);

// console.log(process.platform);
// will tell you what platform you are on

// console.log(process.env.USER);
// // will tell you the user that is logged in


// process.on("exit", function() {
//     console.log("About to exit");
//     });
//     // this will run when the program is about to exit


// const { EventEmitter } = require("events");
// // import EventEmitter from "events" module that is built into node;
// const eventEmitter = new EventEmitter();
// // create a custom event emitter object by calling the EventEmitter constructor

// eventEmitter.on("lunch", () => {
//     // when the lunch event is emitted, run this function
//     console.log("yum");
// });

// eventEmitter.emit("lunch");
// // this will run the lunch event and print "yum" to the console 

// const { ReadFile, readFileSync } = require("fs");
// const txt = readFileSync("./hello.txt", "utf8");
// // read the path of hello.txt file and the encoding type of utf8
// console.log(txt);
// console.log("Do this ASAP");
// // readFileSync will be executed first before the console.log("Do this ASAP") because it is synchronous



// readFile("./hello.txt", "utf8", (err, txt) => {
//     console.log(txt);
// });

// console.log("Do this ASAP");
// readFile will be executed last because it is asynchronous
// readFile is a function that takes in 3 arguments: the path of the file, 
//  the encoding type, and a callback function that takes in an error and the text of the file
// the readFile function register the callback function, execute the rest of the code, 
//  and then execute the callback function when the file is read



// const { readFile } = require("fs").promises;

// async function hello() {
//     const file = await readFile("./hello.txt", "utf8");
// }





// const myModule = require("./my-module");

// console.log(myModule);



const express = require("express");
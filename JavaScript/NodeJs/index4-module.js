// // Path Module Lecture
// 
// const path = require("path");
// // JavaScript read this as a path module

// var pathOb = path.parse(__filename);

// console.log(pathOb);
// // will print out the path object of the file name (this file) that is being executed




// // OS Module Lecture

// const os = require("os");

// var totalMemory = os.totalmem();
// var freeMemory = os.freemem();

// console.log("Total Memory: " + totalMemory);
// console.log(`Free Memory: ${freeMemory}`);



// // File System Module Lecture

// const fs = require("fs");

// // const files = fs.readdirSync("./");
// // will read the current directory and return the files in the directory

// // console.log(files);

// fs.readdir("./", function (err, files) {
//     // the first argument is the path, the second argument is a callback function that takes in an error and files
//     if (err) console.log("Error", err);
//     else console.log("Result", files);
// });



// // Event Module Lecture

// const EventEmitter = require('events');
// // this naming convention is used to indicate that this is a class (not a function)
// // class is container for data and functions

// const emitter = new EventEmitter();
// // create an instance of the EventEmitter class
// // this is an actual object (emmiter) that we can use to raise events


// // Register a listener
// emitter.on("messageLogged", (arg) => {
//     console.log("Listener called", arg);
// });

// emitter.on("logging", (arg) => {
//     console.log("Logging", arg);
// });

// emitter.emit("logging", {data: "message"});

// // Raise an event
// emitter.emit("messageLogged",{id: 1, url: "http://"});




// // Extending Event Emitter Lecture


// const EventEmitter = require('events');

// const Logger = require('./loggerModule');

// const logger = new Logger();

// logger.on("messageLogged", (arg) => {
//     console.log("Listener called", arg);
// });
// // you now use the logger object to listen for the messageLogged event

// logger.log("message");



// HTTP Module Lecture

// const http = require('http');

// const server = http.createServer();
// // this server has all of the capabilities of an event emitter

// server.on("connection", (socket) => {
//     // the name of the event is connection which is raised by the http module (can be find in the documentation)
//     // this listener has a functionn with one argument of soccket of socket class
//     // socket will be the object that will be used to communicate with the client
//     // socket will return the information about the client that is connecting to the server
//     console.log("New connection...");
// });

// server.listen(3000);

// console.log("Listening on port 3000...");

const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.write("Hello World");
        res.end();
    }

    if (req.url === '/api/courses') {
        res.write(JSON.stringify([1, 2, 3]));
        res.end();
    }
});

server.listen(3000);

console.log("Listening on port 3000...");
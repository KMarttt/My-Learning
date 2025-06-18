const express = require('express');
// const { readFile } = require('fs');

// const app = express();

// app.get('/', (request, response) => {
//     // first argument is the path, second argument is a callback function that takes in a request and a response
//     // Request = user's incoming data
//     // Response = what the server sends back

    
//     readFile('./home.html', 'utf8', (err, html) => {
//         // read the home.html file and the encoding type of utf8
//         if (err) {
//             response.status(500).send('sorry, out of order');
//             // if there is an error, send a status of 500 and a message of 'sorry, out of order'
//         }
        
//         response.send(html);
//         // if there is no error, send the html file

//     })
// });


// // To start listening to incomming request
// // we do that by defining a port -- which normally comes from a node environment variable

// app.listen(process.env.PORT || 3000, () => console.log('App available on http://localhost:3000'));
// // app.listen - tells the application to start listening for incoming HTTP requests.

// // process.env.PORT -   checks if there is an environment variable named PORT. This is 
// //          often used in cloud hosting environments (like Heroku) where the hosting 
// //          service assigns a port number dynamically.
// // || 3000 - if there is no PORT environment variable, the app will default to port 3000.
//         //  if run locally without setting a port, then it will listen to port 3000

// // The second argument is a callback function that will run when the server starts.



// To make things cleaner

const {readFile} = require('fs').promises;

app.get('/', async (request, response) => {
    
    response.send(await readFile('./home.html', 'utf8'));
    // response send then await for the operation to read the file; then send the file
    // much better when you have many asychronous operations to handle a single request
});


app.listen(process.env.PORT || 3000, () => console.log('App available on http://localhost:3000'));


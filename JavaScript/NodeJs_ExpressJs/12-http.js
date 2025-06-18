const http = require("http");

const server = http.createServer((req, res) => {


    if (req.url === "/") {
        res.write("Welcome to our home page");
        res.end();
    };
    if (req.url == "/about"){
        res.write("Welcome to our about page");
        res.end();
    }
    res.end(`
        <h1>Ooops!</h1>
        <p>We can't seem to find the page yoy are looking for </p>
        <a href="/">Back home</a>
        `)
        
});

server.listen(5000);
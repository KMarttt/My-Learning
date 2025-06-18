// Modules

const names = require("./4-names.js")
// always use ./ if the path is in the same folder
// always use ../ if the path is in the parent folder
// console.log(names);

const sayHi = require("./5-utils.js");
const data = require("./6-alternative-flavor.js");
require("./7-mind-grenade.js")
// ok I actually know the thought behind this
// the whole file is enclosed into a function?
// so when you require it, it's like calling that function (file)


console.log(data);
sayHi("susan");
sayHi(names.john);
sayHi(names.peter);
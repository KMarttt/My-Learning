const path = require("path");

// will return my platform specific separator ( / )
console.log(path.sep);

// joins path segments together into one path
const filePath = path.join("/content", "subfolder", "test.txt");
console.log(filePath);

// return the filename path of the file path
const base = path.basename(filePath);
console.log(base);

// return the abosule path of the file
const abosolute = path.resolve(__dirname, "content", "subfolder", "test.txt");
console.log(abosolute);
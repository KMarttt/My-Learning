const os = require("os");
// were not doing "./" since this is a built in module and not in your files

// infor about the current user
const user = os.userInfo();
console.log(user);

// method return the system uptine in seconds
console.log(`The System Uptime is ${os.uptime()} seconds`)

// useful info about os
const currentOS = {
    name: os.type(),
    release: os.release(),
    totalMem: os.totalmem(),
    freeMem: os.freemem(),
};
console.log(currentOS);
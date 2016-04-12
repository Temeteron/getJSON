var fs = require("fs");
console.log("\n *START* \n");
var content = fs.readFileSync("test.json");
var jsonContent = JSON.parse(content);
console.log("Output Content : \n"+ content);

console.log("############ DISTANCE #############");
var dist = jsonContent.rows[0].elements[0].distance;
console.log("distance text is: " + dist.text);
console.log("distance value is: " + dist.value);

console.log("\n *EXIT* \n");
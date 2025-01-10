const express = require("express");
const http = require("http");
const proxy = require("express-http-proxy");
const app = express();


// Configure proxy endpoints
app.use("/jaeger", proxy("http://jaeger:16686")); 
app.use("/", proxy("http://collekt-frontend:80"));

// Create and start both http and https server to handle all incoming traffic
const httpServer = http.createServer(app);

httpServer.listen(80, () => {
  console.log("HTTP Server started");
});

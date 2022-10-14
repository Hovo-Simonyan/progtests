require("dotenv").config();
const express = require("express");
const mongosee = require("mongoose");
const User = require("./models/User");
const connectDb = require("./config/dbConn");


// create App and connection
const app = express();
connectDb();




// routes
app.get("/", (req, res) => {
  User.create({ name: "Hovo", password: "1234" });
  res.send("Hello world!");
});

app.get("/users", async (req, res) => {
  const users = await User.find();
  res.send(users);
});




// connected and listening port
mongosee.connection.once("open", () => {
  console.log("Connected to MongoDb");
  app.listen(process.env.PORT || 4000, () => {
    console.log("Server is listening port 4000");
  });
});

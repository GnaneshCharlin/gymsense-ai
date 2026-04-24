const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("GymSense AI Backend Running 🚀");
});

app.listen(5000);

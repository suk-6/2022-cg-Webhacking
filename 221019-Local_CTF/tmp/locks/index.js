const express = require("express")
const bodyParser = require("body-parser")

const app = express()
const FLAG = process.env.FLAG || require("./flag")

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))

locks = {}

app.get("/", (req, res) => {
  res.status(200).send("hello world!")
})

app.get("/:id", (req, res) => {
  if (locks[req.body.id] != undefined) {
    res.status(200).send(`lock '${req.params.id}' is ${locks[req.params.id] ? "unlocked" : "locked"}`)
  } else res.status(200).send(`You don't have a lock yet :(`)
})

app.post("/buy", (req, res) => {
  if (req.body.id != undefined) {
    res.status(200).send(`Thank you for purchasing the lock '${req.body.id}'!`)
    locks[req.body.id] = false
  } else res.status(500).send(`Something wrong :(`)
})

app.unlock("/:id", (req, res) => {
  if (locks[req.params.id] == undefined) {
    res.status(500).send(`You don't have a lock yet :(`)
  } else {
    locks[req.params.id] = true
    res.status(200).send(`${req.params.id} is unlocked!`)
  }
})

app.move("/:id", (req, res) => {
  if (locks[req.params.id]) {
    res.status(200).send(FLAG)
    locks[req.params.id] = false // lock is closed after getting a flag
  } else res.status(403).send("YOU DON'T HAVE PERMISSION! :(")
})

app.listen(1337, () => {
  console.log("Express app is listening on port 1337")
})

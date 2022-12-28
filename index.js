const express = require("express")
const cors = require("cors")
require('dotenv').config()
const port = process.env.PORT
const app = express()

app.use(cors())
app.use('/Login', (request, result) => {
    result.send(
        {
            token: 'test123'
        }
    )
})

app.listen(port, () => console.log(`API is running on localhost:${port}/Login`))
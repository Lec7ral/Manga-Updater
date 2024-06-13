from pyrogram import Client
from config import Config



xbot = Client(
	"MangaLoader",
	api_id=Config.APP_ID,
	api_hash=Config.API_HASH,
	bot_token=Config.BOT_TOKEN,
	plugins=dict(root="plugins"),
)
const express = require('express')
const app = express()
const port = process.env.PORT || 4000;

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
xbot.run()

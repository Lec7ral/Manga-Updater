from pyrogram import Client
from flask import Flask, request
from config import Config

url = 'https://Lectral.pythonanywhere.com/' + Config.SECRET


xbot = Client(
	"MangaLoader",
	api_id=Config.APP_ID,
	api_hash=Config.API_HASH,
	bot_token=Config.BOT_TOKEN,
	plugins=dict(root="plugins"),
)

xbot.run()

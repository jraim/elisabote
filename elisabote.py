import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client =commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
	print("Bot is online and connected to Discord")
	
@client.event
async def on_message(message):
	if message.content.startswith('!ping'):
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Pong!" % (userID))


client.run("NDE5ODk0MTY5MTM4NDk1NDk4.DX2xDQ.gn8L0o4gFGPtaujiHVxpID-UgaU")

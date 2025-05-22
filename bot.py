
import discord
from discord.ext import commands
import requests
import os

TOKEN = os.getenv("DISCORD_TOKEN")
MISTRAL_URL = os.getenv("MISTRAL_URL", "http://localhost:11434/api/generate")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ask(ctx, *, prompt):
    try:
        response = requests.post(MISTRAL_URL, json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })
        reply = response.json().get("response", "No response.")
        await ctx.send(reply)
    except Exception as e:
        await ctx.send("Error: " + str(e))

bot.run(TOKEN)

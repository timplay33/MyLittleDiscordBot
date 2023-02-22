from dotenv import load_dotenv
import os

import discord
from discord import app_commands
from discord.ext import commands

#Load .env data
load_dotenv()
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD_ID = os.environ.get("GUILD_ID")

#variables
prefix = "!"
help_menu = discord.Embed(title="Help", description="", color=0x9c9c9c).add_field(name="/help", value="shows you this promt", inline=False)

#intents
intents = discord.Intents.all()

#Init bot
bot = commands.Bot(prefix, intents = intents)

@bot.event
async def on_ready():
    print("Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="help", description="displays help information")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(embed=help_menu, ephemeral=True)

@bot.tree.command(name="hello", description="Tells you that you used a slash command")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)

@bot.tree.command(name="say", description="says what you give it")
@app_commands.describe(arg ="What should I say?")
async def say(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message(f"{interaction.user.name} said: {arg}!")

bot.run(DISCORD_TOKEN)
from dotenv import load_dotenv
import os

import discord
from discord import app_commands
from discord.ext import commands

# Load .env data
load_dotenv()
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD_ID = os.environ.get("GUILD_ID")
PREFIX = os.environ.get("PREFIX")

# global variables
help_menu = discord.Embed(title="Help", description="", color=0x9c9c9c).add_field(
    name="/help", value="shows you this promt", inline=False)
sync = False

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    # await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f'We have logged in as {client.user}')


@tree.command(name="sync", description="syncs commands to the server")
async def sync(interaction: discord.Interaction):
    if interaction.user == interaction.user:  # ToDo - check if the user is the owner of the server
        try:
            await tree.sync(guild=discord.Object(id=interaction.guild_id))
            await interaction.response.send_message(f"Syncing commands to the server (guild_id = {interaction.guild_id})", ephemeral=True)
        except:
            await interaction.response.send_message(f"Failed to sync commands to the server (guild_id = {interaction.guild_id})", ephemeral=True)
    else:
        await interaction.response.send_message(f"you don't have permission to sync commands to the server", ephemeral=True)

# /help - Help menu


@tree.command(name="help", description="displays help information")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(embed=help_menu, ephemeral=True)

# /hello


@tree.command(name="hello", description="Tells you that you used a slash command")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.display_name}! This is a slash command!", ephemeral=True)

# /say


@tree.command(name="say", description="says what you give it")
async def say(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message(f"{interaction.user.display_name} said: {arg}!")

# /serverinfo


@tree.command(name="serverinfo", description="shows server information")
async def serverinfo(interaction: discord.Interaction):
    embed = discord.Embed(title="Server Info", description="", color=0x9c9c9c)
    embed.add_field(name="Server Name",
                    value=interaction.guild.name, inline=False)
    embed.add_field(name="Server Owner",
                    value=interaction.guild.owner, inline=False)
    embed.add_field(
        name="Members", value=interaction.guild.member_count, inline=False)
    embed.add_field(name="Server creation date",
                    value=interaction.guild.created_at.date(), inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)


@tree.command(name="getrole", description="gives a role to a user")
async def getrole(interaction: discord.Interaction):
    try:
        await interaction.response.send_message(f"{interaction.user.name} gave you a role!", ephemeral=True)
    except:
        await interaction.response.send_message(f"{interaction.user.name} did not give you a role!", ephemeral=True)

client.run(DISCORD_TOKEN)

import discord
commands = {
    "/help": "shows you this prompt",
    "/hello": "says hello to you",
    "/sync": "updates the bots slash commands",
    "/serverinfo": "shows basic infos about the server",
    "/getrole": "get a role",
}


def help():
    embed = discord.Embed(
        title="Help", description="Show all available commands", color=0x9c9c9c)
    for i in commands:

        embed.add_field(name=i, value=commands[i], inline=False)

    return embed

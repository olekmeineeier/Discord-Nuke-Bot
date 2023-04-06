import discord;from discord.ext import commands;import os

bot = commands.Bot(command_prefix="####", intents=discord.Intents.all())

token = input("Token >>> ")
try:
    guildid = int(input("Server ID you want to scrape (members,roles,etc.) >>> "))
except ValueError:
    print("Need int value")
    os._exit(1)
finally:pass




@bot.event
async def on_ready():
    global guildid
    guild  = bot.get_guild(guildid)
    if os.path.exists("./scraped"):
        pass
    else:
        os.makedirs("./scraped")
    f = open("scraped/members.txt", "w").close()
    with open("scraped/members.txt", "w+") as membersf:
        for member in guild.members:
            membersf.write(str(member.id) + "\n")
        membersf.close()
    os._exit(69699696969699696969696969969696969969696666666666666666666666669696965696969699696699696969696969699696969696969969696969969696969696996969696996696996969696969)




bot.run(token)
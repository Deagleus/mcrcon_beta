import discord
import mcrcon
from discord.ext import commands
import datetime
from mcrcon import MCRcon
import json



data = {"IP": "TEST", "PW": "TEST", "USER": "TEST"}
with open('botdata.txt', 'w') as file:
    json.dump(data, file)


class cogname(commands.Cog, name='minecraft'):
    def __init__(self, bot):
        self.bot = bot





def setup(bot):
    bot.add_cog(cogname(bot))

import discord
import mcrcon
from discord.ext import commands
from mcrcon import MCRcon


cogs = ['cogs.minecraft']

bot = commands.Bot(command_prefix='!', description="Deagleus va da la bot")

@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Streaming(name="mcrcon v0.1 bot", url="http://www.twitch.tv/deagleus"))
   for cog in cogs:
       bot.load_extension(cog)
   print('diglushana hasvehas')

@bot.command(name="unload", aliases = ['u'])
@commands.is_owner()
async def unload(ctx, name):
   bot.unload_extension("cogs." + name)
   await ctx.send(":flushed:  cogs." + name + " has been unloaded !")

@unload.error
async  def unload_error(ctx, error):
   if isinstance(error, commands.NotOwner):
      msg = 'Only the owner can use this!'
      await ctx.send(msg)

@bot.command(name="load", aliases = ['l'])
@commands.is_owner()
async def load(ctx, name):
   bot.load_extension("cogs." + name)
   await ctx.send(":flushed:  cogs." + name + " has been loaded !")
   
@load.error
async  def  load_error(ctx, error):
   if isinstance(error, commands.NotOwner):
      msg = 'Only the owner can use this!'
      await ctx.send(msg)
   if isinstance(error, commands.MissingRequiredArgument):
          msg = ':flushed:  Usage : `!load COGNAME`'
          await ctx.send(msg)
 
@bot.command(name="reload")
@commands.is_owner()
async def reload(ctx, name):
   bot.unload_extension("cogs." + name)

   bot.load_extension("cogs." + name)
   await ctx.send(":flushed:  " + name + " has been restarted !")
   
@reload.error
async def restart(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
          msg = ':flushed:  Usage : `!restart COGNAME`'
          await ctx.send(msg)          


bot.run('')





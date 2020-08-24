import discord
import mcrcon
from discord.ext import commands
import datetime 
from mcrcon import MCRcon
import json



with open("botdata.txt", "r") as datafile:
    data = json.load(datafile)
    

    
mcr = MCRcon(data["IP"], data["PW"])
user = data["USER"]


class cogname(commands.Cog, name='minecraft'):
    def __init__(self, bot):
        self.bot = bot

   

    @commands.command(name="summon", pass_context = True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def summon(self, ctx, mobname):
        mcr.connect() 
        if mobname in ('ender_dragon', 'wither', 'ghast', 'blaze'):
           await ctx.send(" " + mobname + " is not allowed on this server !  :flushed:")
           return
        else:
            await ctx.send("The command is sending... :desktop:")
            resp = mcr.command("execute at " + user + " run summon " + mobname + " ~ ~ ~")
            mcr.disconnect()
            await ctx.send(resp)

    @summon.error
    async def mine_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'You can use this command in {:.2f} seconds'.format(error.retry_after)
            await ctx.send(msg)
        if isinstance(error, commands.MissingRequiredArgument):
            msg = ':flushed:  Usage : `!summon MOBNAME`!'
            await ctx.send(msg)

    #@commands.command(name="give", aliases = ['gv'])
    #@commands.cooldown(1, 20, commands.BucketType.user)
    #async def mod_gv(self, ctx, itemname, itemcount: int):
    #    if itemcount > 1:
    #       await ctx.send(":flushed:   Nu poti trimite " + str(itemcount) + " iteme!   :pleading_face:")
    #        return
    #    if itemname in ('oak_boat', 'birch_boat', 'acacia_boat', 'dark_oak_boat', 'spruce_boat'):
    #        return
    #    else:
    #
    #        await ctx.send("Se trimite comanda... :desktop:")
    #        mcr.connect()
    #        resp = mcr.command("give " + user + " " + itemname + " " + str(itemcount))
    #        mcr.disconnect()
    #        await ctx.send(resp)
            
            
            
            
            
    @commands.command(name="give", aliases = ['gv'])
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def mod_gv(self, ctx, itemname):
        if itemname in ('oak_boat', 'birch_boat', 'acacia_boat', 'dark_oak_boat', 'spruce_boat'):
            return
        else:
    
            await ctx.send("The command is sending... :desktop:")
            mcr.connect()
            resp = mcr.command("give " + user + " " + itemname)
            mcr.disconnect()
            await ctx.send(resp)

    @mod_gv.error
    async def mine_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'You can use this command in {:.2f} seconds'.format(error.retry_after)
            await ctx.send(msg)
       #if isinstance(error, commands.MissingRequiredArgument):
       #   msg = ':flushed:  Ce-ai facut golane , ai uitat sa scri numarul de iteme  :pleading_face:'
       #    await ctx.send(msg)

    @commands.command(name="setinfo", pass_context = True)
    @commands.is_owner()
    async def setinfo(self, ctx, ip, password, user):
    
         with open("botdata.txt", "r") as datafile:
            data = json.load(datafile)
      
         data["IP"] = ip
         data['PW'] = password
         data['USER'] = user
         with open('botdata.txt', 'w') as file:
            json.dump(data, file)
         with open("botdata.txt", "r") as datafile:
            data = json.load(datafile)
         global mcr
         mcr = MCRcon(data["IP"], data["PW"])
                  
         await ctx.send("Set IP to : `" + ip + "`   :flushed:")
         await ctx.send("Set PASSWORD to : `" + password + "`   :flushed:")
         await ctx.send("Set USERNAME to : `" + user + "`   :flushed:")
         print("NEW IP : " + ip)
         print("NEW PASSWORD : " + password)
         print("NEW USERNAME : " + user)
         print(str(ctx.message.author))
         print("[=================]")
    
    @setinfo.error
    async def setinfo_error(self, ctx, error):
       if isinstance(error, commands.MissingRequiredArgument):
          msg = ':flushed:  Usage : `!setinfo IP PASSWORD USERNAME`'
          await ctx.send(msg)
         
    @commands.command(name="info", pass_context = True)
    async def info(self, ctx):
        
        
            with open("botdata.txt", "r") as datafile:
                 data = json.load(datafile)
            ip = data["IP"]
            user = data["USER"]
            word = data["PW"]
            

            embed = discord.Embed(title=' ', description='Server information for bot connection ')
            embed.add_field(name='Server Information', value='IP\nPassword\nUsername')
            embed.add_field(name='User-input Information', value= ip + "\n" + word + "\n" + user)
            embed.set_footer(text='MCRcon v0.1')
            embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1217915130954035213/Dq0D3BDD_400x400.jpg')

            await ctx.send(embed=embed)    









def setup(bot):
    bot.add_cog(cogname(bot))
import discord
import os
import random

from discord.ext import commands

def setup(bot):
    bot.add_cog(UtilCMDs(bot))

class UtilCMDs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cring(self, ctx):
        await ctx.message.channel.send('CRING')

    @commands.command()
    async def cringreact(self, ctx):
        # Get message prior to latest message (message before message that called command)
        prevMessage = (await ctx.message.channel.history(limit=3).flatten())[1]
        await ctx.message.delete()
        await prevMessage.add_reaction('🇨')
        await prevMessage.add_reaction('🇷')
        await prevMessage.add_reaction('🇮')
        await prevMessage.add_reaction('🇳')
        await prevMessage.add_reaction('🇬')

    @commands.command()
    async def reload(self, ctx):
        await ctx.message.channel.send('Reloading Cogs...')

        if ctx.message.author.guild_permissions.administrator:
            for cog in os.listdir('cogs'):
                if (cog.endswith('.py')):
                    self.bot.reload_extension(f'cogs.{cog[:len(cog)-3]}')

        else:
            print(f'**ERROR**: Attempted reload of Cogs from non-admin user: {ctx.message.author}')
            await ctx.message.channel.send('ERROR: Cannot reload Bot if not admin user')

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
                print(f'Bot shutting down by command from Guild: {ctx.message.guild.name} (Guild ID: {ctx.message.guild.id}) by user: {ctx.message.author}')
                await ctx.message.channel.send('Disconnecting client...')
                await ctx.bot.close()
            
        else:
            print(f'**ERROR**: Attempted shutdown of Bot from non-admin user: {ctx.message.author}')
            await ctx.message.channel.send('ERROR: Cannot shutdown Bot if not admin user')
    
    @commands.command()
    async def servericon(self, ctx):
        await ctx.message.channel.send(f'Retrieving {ctx.message.guild}\'s Server Icon:')
        await ctx.message.channel.send(ctx.message.guild.icon_url)

    @commands.command()
    async def help(self, ctx):
        # Send DM to command requester containing GitHub wiki link 
        await ctx.message.author.send('**Commands available at Raava\'s GitHub Wiki Page:**\nhttps://github.com/kosamson/RaavaApp/wiki')

    @commands.command()
    async def getavatar(self, ctx, userid):
        targetUser = ctx.bot.get_user(int(userid))

        if (targetUser == None):
            await ctx.message.channel.send("**ERROR**: User ID does not match a user in this server, please try again. (Right-click the user and click 'Copy ID' to obtain their ID)")

        else:
            await ctx.message.channel.send(f'Retrieving `{targetUser.name}#{targetUser.discriminator}`\'s Icon:')
            await ctx.message.channel.send(targetUser.avatar_url)

    @commands.command()
    async def postcring(self, ctx):
        imgIdx = random.randint(1, 24)
        img = discord.File(f'../postcringimgs/{imgIdx}.jpg', filename=f'{imgIdx}.jpg')
        await ctx.message.channel.send(file=img)
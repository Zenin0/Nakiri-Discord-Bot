#Imports necesarios para que los comandos funcionen
import discord,random,glob,datetime
from discord.ext import commands

bot = commands.Bot(command_prefix = '!', help_command=None)
#Esto es para despues cargarlo como cog
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_role(965943947971162142)
    async def verify(self,ctx):
        await ctx.message.delete()
        embed = discord.Embed(title ='Language/Idioma', description ='Welcome to the language selector\nBienvenido a la seleccion de idioma.', color=0xF4EFF3)
        #Embed image
        embed.set_image(url="https://cdn.discordapp.com/splashes/971599079584976996/c0fc270e65b75783340e2d22bc002201.jpg?size=2048")
        msg=await ctx.send(embed = embed)
        emoji = '✅'
        await msg.add_reaction(emoji)
def setup(bot):
    bot.add_cog(Slash(bot))
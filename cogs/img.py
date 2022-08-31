import discord,requests,random
from discord.ext import commands
from discord import Member

class img(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nakiri(self,ctx,user: discord.Member=None):
        nakiri_img=["XvTsE3e","XcvudNs","oe5efBn"]
        query=random.choice(nakiri_img)
        if user is None:
            description=f"Aquí tienes una imagen de Nakiri {ctx.author.mention}!"
        else:
            description=f"{ctx.author.mention} te ha enviado una imagen de Nakiri {user.mention}"
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/{query}/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))
        
    #IMG ABRAZO
    @commands.command()
    async def abrazo(self, ctx, user: discord.Member=None):
        if user is None:
            description=f"Ahí va un abrazo {ctx.author.mention}!"
        else:
            description=f"{ctx.author.mention} ha abrazado ha {user.mention}"
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/RkiH66c/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))

    #IMG MIMOS
    @commands.command()
    async def mimos(self, ctx, user: discord.Member=None):
        if user is None:
            description=f"Ahí van unos mimos {ctx.author.mention}!"
        else:
            description=f"{ctx.author.mention} esta mimando ha {user.mention}"
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/zvvZEln/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))

    #IMG MALO
    @commands.command()
    async def malo(self, ctx, user: discord.Member=None):
        if user is None:
            description=f"Quieres que te castiguen {ctx.author.mention}?"
        else:
            description=f"Lo siento {user.mention} pero vas a ser castigad@ por {ctx.author.mention} por algo que has hecho"
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/84L6k4l/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))

    #IMG SONROJAR
    @commands.command()
    async def sonrojar(self, ctx, user: discord.Member=None):
        if user is None:
            
            description=f"Awww {ctx.author.mention} se ha sonrojado, me pregunto porque?"
        else:
            description=f"Awww {user.mention} se a sonrojado por culpa de {ctx.author.mention}"
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/HRxK0Wf/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))

    #IMG CONFUNDIDO
    @commands.command()
    async def confuso(self, ctx, user: discord.Member=None):
        if user is None:
            
            description=f"Hmm {ctx.author.mention} esta confuso?"
        else:
            description=f"Hmm {user.mention} ha hecho que {ctx.author.mention} se confunda, que ha pasado?"
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/C5btF/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))

    #IMG BAILAR
    @commands.command()
    async def bailar(self, ctx, user: discord.Member=None):
        if user is None:
            description=f"{ctx.author.mention} está bailando?"
        else:
            description=f"{ctx.author.mention} baila con {user.mention}, vaya parejita..."
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/vPnS8PN/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))

    #IMG NOSE
    @commands.command()
    async def nose(self, ctx, user: discord.Member=None):
        if user is None:
            description=f"{ctx.author.mention} se encoge de hombros ¯\_(ツ)_/¯"
        else:
            description=f"{ctx.author.mention} se encoge de hombros a {user.mention} ¯\_(ツ)_/¯"
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/A8D9jGP/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))
    #IMG INSULTAR
    @commands.command()
    async def insulto(self, ctx, user: discord.Member=None):
        if user is None:
            description=f"{ctx.author.mention} se insulta a si mismo"
        else:
            description=f"{ctx.author.mention} insulta a {user.mention}"
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/6nixGHX/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))
    #IMG BESO
    @commands.command()
    async def beso(self, ctx, user: discord.Member=None):
        if user is None:
            description=f"Te besas a ti mismo {ctx.author.mention}? Vaya..."
        else:
            description=f"{ctx.author.mention} esta besando a {user.mention}, que bonitos juntos."
        em = discord.Embed(title="",description=description ,colour=0xF4EFF3)
        r = requests.get(f"https://api.imgur.com/3/album/2HitdsF/images?client_id=424077d40aee764").json()
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['data'][size]['link']))



def setup(client):
	client.add_cog(img(client))    
import discord, glob, datetime, random, requests
from discord.ext import commands
import urllib.parse, urllib.request, re
from discord_slash import cog_ext
from discord_slash import SlashCommand

client = commands.Bot(command_prefix='!')
slash = SlashCommand(client, sync_commands=True)
cd_mapping = commands.CooldownMapping.from_cooldown(1, 60,
                                                    commands.BucketType.user)


class utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    #COOLDOWN
    #COMANDO AVATAR
    @commands.command()
    async def avatar(self, ctx, miembro: discord.Member = None):
        if miembro is None:
            miembro = ctx.author
        embed = discord.Embed(title="Avatar de " + str(miembro),
                              color=0xF4EFF3)
        embed.set_image(url=miembro.avatar_url)
        await ctx.send(embed=embed)

    #COMANDO MONEDA
    @commands.command()
    async def moneda(self, ctx):
        n = random.randint(0, 1)
        if n == 1:
            await ctx.channel.send("Moneda tirada, tenemos... **Cara**!")
        else:
            await ctx.channel.send("Moneda tirada, tenemos... **Cruz**!")

    #COMANDO NUM
    @commands.command()
    async def num(self, ctx, fir=1, sec=10):
        n = random.randint(int(fir), int(sec))
        await ctx.channel.send(n)

    #COMANDO IMG
    ## Descubrir como hacerlo para que eliga una imagen aleatoria de una galeria de Imagur, se hace con el API, pero hay que mirarlo
    @commands.command()
    async def img(self, ctx):
        file_path_type = ["./img/*.jpg", "./img/*.gif"]
        images = glob.glob(random.choice(file_path_type))
        random_image = random.choice(images)
        await ctx.channel.send(file=discord.File(random_image))

    #COMANDO AFK
    @commands.command()
    @commands.guild_only()
    async def afk(self, ctx):
        now = datetime.datetime.now()
        userid = ctx.author.id
        await ctx.channel.send(
            f"> <@{userid}> esta ahora AFK\n> AFK desde hoy a las " +
            str(now.hour) + ":" + str(now.minute))

    #COMANDO MENSAJE
    @commands.command()
    @commands.guild_only()
    async def mensaje(self,
                      ctx,
                      user: discord.Member,
                      *,
                      message=f'Bienvenid@ al Servidor!'):
        #message = f'Bienvenid@ al Servidor!'
        embed = discord.Embed(title=message,
                              description=f'De parte de {ctx.author.name}',
                              color=0xF4EFF3)
        await ctx.send(f'*Mensaje  enviado*')
        await user.send(embed=embed)

    #COMANDO YT
    @commands.command()
    @commands.guild_only()
    async def yt(self, ctx, *, search):
        query_string = urllib.parse.urlencode({'search_query': search})
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})',
                                    htm_content.read().decode())
        await ctx.send('**El Mejor resultado :**' +
                       'http://www.youtube.com/watch?v=' + search_results[0])

    #Comando Novia
    @commands.command()
    async def novia(slef, ctx, who: discord.member = None):
        if who is None:
            who = ctx.author
        await ctx.send(f"A mi no me digas nada buscate tu una 😏")

    #COMANDO F
    @commands.command()
    @commands.guild_only()
    async def f(self, ctx):
        userid = ctx.author.id
        embed = discord.Embed(
            title='',
            description=f'**<@{userid}>**  a mostrado sus respetos',
            color=0x000000)
        await ctx.send(embed=embed)

    #COMANDO MINE
    @commands.command()
    @commands.guild_only()
    async def mine(self, ctx):
        await ctx.message.delete()
        server1 = '`tulant.aternos.me`'
        server2 = '`PIDIEF.aternos.me`'
        mods = '[Link de Descarga](https://drive.google.com/drive/folders/1CVGdgbBFJo2pdGudJ2Y2FsTWfPHZ-DF4?usp=sharing)'
        shaders = '[Link de Descarga](https://drive.google.com/file/d/1I-2l5n3afgUiLEagBviy9hyntez-J3LG/view?usp=sharing)'
        mem = 'Ampliar memoria min a `5GB/5000MB`'
        embed = discord.Embed(colour=0xF4EFF3)
        embed.set_thumbnail(
            url=
            "https://www.minecraft.net/etc.clientlibs/minecraft/clientlibs/main/resources/img/GrassBlock_HighRes.png"
        )
        embed.add_field(name="Servidor 1", value=server1)
        embed.add_field(name="Servidor 2/Vanilla", value=server2)
        embed.add_field(name="Ajustes", value=mem, inline=False)
        embed.add_field(name="Mods", value=mods, inline=False)
        embed.add_field(name="Shaders", value=shaders, inline=False)
        return await ctx.send(embed=embed)

def setup(client):
    client.add_cog(utils(client))

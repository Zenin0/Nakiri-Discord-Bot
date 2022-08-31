#PYTHON LIB
import os, discord, json
from discord.ext import commands
from requests import PreparedRequest
from discord import Member

#DISCORD LIB
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord_slash import SlashCommand
from requests import PreparedRequest
from discord_components import Button, Select, SelectOption, ComponentsBot, interaction
from discord_components.component import ButtonStyle
from keep_alive import keep_alive
from discord_components import Interaction

#NECESAROS
intents = discord.Intents.default()
intents.members = True
cogs = [
    "cogs.verify", "cogs.slash", "cogs.roles", "cogs.guild", "cogs.img",
    "cogs.nakiri", "cogs.utils"
]

#PREFIJO COMANDO/SYNC SLASH
client = commands.Bot(command_prefix='!', intents=intents, help_command=None)
slash = SlashCommand(client, sync_commands=True)


#BOT STARTUP
@client.event
async def on_ready():
    print('Bot {0.user} funcionando perfectamente'.format(client))
    print("-----------------------------------------")
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="!info | nakiri.x10.mx"))
    print("ID: " + str(client.user.id))
    print("Version de Discord: " + str(discord.__version__))
    print(f'Actualmente en {len(client.guilds)} servidores!')
    for server in client.guilds:
        print(server.name)
    print("-----------------------------------------")


#COGS
print("Cargando cogs . . .")
for cog in cogs:
    try:
        client.load_extension(cog)
        print(cog + " ha sido cargada.")
    except Exception as e:
        print(e)
print("\n")


#MENSAJE WELCOMER JOIN
@client.event
async def on_member_join(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    channel_id = guilds_dict[str(member.guild.id)]
    embed = discord.Embed(colour=0x808080)  #Color del embed
    req = PreparedRequest()  #Aqui empieza la imagen
    req.prepare_url(
        url='https://api.xzusfin.repl.co/card?',
        params={
            'avatar':
            str(member.avatar_url_as(format='png')),  #Avatar del usuario
            'middle': '¡Bienvenid@',  #Texto del medio
            'name': str(member.name),  #Nombre del usuario
            'bottom': str('A Tulant!'),  #Texto de abajo
            'text': '#CCCCCC',  #Color de texto
            'avatarborder': '#CCCCCC',  #Color del borde del avatar
            'avatarbackground':
            '#CCCCCC',  #Fondo del avatar en caso de que tenga transparencia
            #'background': '#808080' #Color de fondo
            'background':
            'https://wallpapercave.com/wp/wp6147812.jpg'  #Imagen de fondo
        })
    embed.set_image(url=req.url)  #Carga la imagen en el embed
    await client.get_channel(int(channel_id)
                             ).send(embed=embed)  #Envia el embed con la image
    #Mensaje que se le enviara por privado a quien se una
    message = '**Konakiri!** Bievenid@ a nuesto servidor \n **Contacto**\n✈️ Telegram: @Isaac_Sanz\n💬 Discord: ElmerKao#0058 \n🌐 Página Web: https://nakiri.x10.mx/'
    embed = discord.Embed(title=message, color=0xAA336A)
    await member.send(embed=embed)


#MENSAJE WELCOMER LEAVE
@client.event
async def on_member_remove(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    channel_id = guilds_dict[str(member.guild.id)]
    embed = discord.Embed(colour=0x808080)  #Color del embed
    req = PreparedRequest()  #Aqui empieza la imagen
    req.prepare_url(
        url='https://api.xzusfin.repl.co/card?',
        params={
            'avatar':
            str(member.avatar_url_as(format='png')),  #Avatar del usuario
            'middle': '¡Cuidate',  #Texto del medio
            'name': str(member.name),  #Nombre del usuario
            'bottom': str('y vuelve pronto >.<!'),  #Texto de abajo
            'text': '#CCCCCC',  #Color de texto
            'avatarborder': '#CCCCCC',  #Color del borde del avatar
            'avatarbackground':
            '#CCCCCC',  #Fondo del avatar en caso de que tenga transparencia
            #'background': '#808080' #Color de fondo
            'background':
            'https://wallpapercave.com/wp/wp6147812.jpg'  #Imagen de fondo
        })
    embed.set_image(url=req.url)  #Carga la imagen en el embed
    await client.get_channel(int(channel_id)
                             ).send(embed=embed)  #Envia el embed con la imagen


#AÑADIR JSON GUILD
#WELCOMER
@client.command(name='welcomer')
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def welcomer_channel(ctx, channel: discord.TextChannel):
    try:
        with open('guilds.json', 'r', encoding='utf-8') as f:  #ABRIR EL JSON
            guilds_dict = json.load(f)  #CARGAR EL DICCIONARIO EN guilds_dict
        guilds_dict[str(ctx.guild.id)] = str(
            channel.id)  #ASIGNAR GUILD ID AL CANAL
        with open('guilds.json', 'w',
                  encoding='utf-8') as f:  #ESCRIBIR EN EL JSON
            json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
        await ctx.send(
            f'Seleccionado el canal {channel.name} como canal de Bienvenida de {ctx.message.guild.name}'
        )
    except:
        await ctx.send("Ha ocurrido un error, intentelo más tarde")


#DELETE JSON GUILD
#WELCOMER_DEL
@client.command(name='welcomer_del')
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def welcomer_del(ctx):
    try:
        with open('guilds.json', 'r', encoding='utf-8') as f:  #ABRIR EL JSON
            guilds_dict = json.load(f)  #CARGAR EL DICCIONARIO EN guilds_dict
        guilds_dict.pop(f"{ctx.guild.id}")  #BORRAR LA PARTE DE LA ID GUILD
        with open('guilds.json', 'w', encoding='utf-8') as f:
            json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
        await ctx.send("Canal de Bienvenida eliminado correctamente")
    except:
        await ctx.send(
            "Ha ocurrido un error, *No hay registrado ningun canal actualmente*"
        )


#SI EL BOT ABANDONA EL SERVER LO BORRA DEL JSON GUILD
@client.event
async def on_guild_remove(guild):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    guilds_dict.pop(f"{guild.id}")
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)


#ERRORS
#WELCOMER
@welcomer_channel.error
async def welcom_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(
            f"No tienes permisos seleccionar un canal de bienvenida, para esto tienes que ser administrador"
        )


#WELCOMER
@welcomer_channel.error
async def welccomer_del(ctx, error):
    if isinstance(error, commands.ChannelNotFound):
        await ctx.send(f"No he podido encontrar ese canal")


#FALTA DE ARGUMENTOS
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            f"Se necesitan argumentos para ejecutar este comando, ejecute `!help <comando>` para verlo"
        )
    elif isinstance(error, CommandNotFound):
        return
    raise error


#TOKEN
keep_alive()
API = os.environ['API']
try:
    client.run(API)
except:
    os.system("kill 1")
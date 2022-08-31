import discord, random, datetime, time
from discord.ext import commands
from requests import PreparedRequest

startup = time.time()


class nakiri(commands.Cog):
    def __init__(self, client):
        self.client = client

    #COOLDOWN
    #COMANDO STATUS
    @commands.command()
    @commands.guild_only()
    async def status(self, ctx):
        mem = random.randint(
            2024, 2823
        )  #Como en replit no puedo saber la veradera memoria me la invento
        servers = 0
        users = 0
        activeservers = self.client.guilds  #Saca  los usuarios de todos los servidores en los que esta
        for guild in activeservers:  #Por cada usuario que recorre añade 1 a un contador
            servers += 1
        for guild in self.client.guilds:  #Saca los servidores a los que esta unido
            for member in guild.members:  #Por cada servidor, añade 1 al contador
                users += 1
        current_time = time.time()
        difference = int(
            round(current_time - startup)
        )  #Saca cuanto tiempo lleva encendido, startup esta definido en la linea 36, en el onready
        other = f"Localización: 🇪🇺 \nComandos: **45**\nUsuarios: **{users}** \n Uso de memoria: `{mem}/4096 MB`"  #Esto saca que es de europa, la memoria inventada, y los usuarios
        text = str(datetime.timedelta(
            seconds=difference))  #Muestra el tiempo que lleva funcionando
        embed = discord.Embed(colour=0xF4EFF3)  #Color del embed
        embed.set_thumbnail(
            url=
            "https://modworkshop.net/mydownloads/previews/38947_1632764140_d36ed6cef80762c9bd284e7d8382da9a.webp"
        )  #La imagen de perfil de nakiri
        embed.add_field(name="Activo durante", value=text)
        embed.add_field(name="Servidores", value=servers)
        embed.add_field(name="Otros", value=other, inline=False)
        try:  # En caso de que no se pueda enviar con un embed, se enviara con un simple texto
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Ativo durante: " + text)
            await ctx.send("Otros: " + other)
            await ctx.send("Servidores activo: " + servers)

    #COMANDO INFO
    @commands.command()
    async def info(self, ctx):
        await ctx.channel.send(
            '**Konakiri!** Soy un bot hecho por ElmerKao\nMi link de invitación es este: https://nakiri.x10.mx/invite\nPágina Web: https://nakiri.x10.mx/\nPlantilla del Servidor: https://nakiri.x10.mx/template\nPara empezar a usar el bot escribe **`!help`** o **`/help`** y haz click en la imagen de Nakiri'
        )

    #COMANDO SOPORTE
    @commands.command()
    async def soporte(self, ctx):
        await ctx.channel.send(
            "✈️ Telegram: @Isaac_Sanz\n💬 Discord: ElmerKao_#0058 \n🌐 Página Web: https://nakiri.x10.mx/"
        )

    #COMANDO HELP
    @commands.command()
    async def help(self, ctx, arg1=''):
        arg1 = arg1.lower()
        if arg1 == '':
            embed = discord.Embed(
                title="",
                description=
                "Debajo se pueden observar todos los comandos que se.",
                color=0xF4EFF3)
            embed.set_author(
                name="Hola Soy Nakiri~!",
                icon_url=
                "https://modworkshop.net/mydownloads/previews/38947_1632764140_d36ed6cef80762c9bd284e7d8382da9a.webp"
            )
            embed.add_field(
                name="UTILIDADES",
                value=
                "`avatar`,`moneda`,`afk`,`num`,`mensaje`,`yt`,`f`,`novia`",
                inline=False)
            embed.add_field(
                name="GUILD",
                value=
                "`clear`,`ban`,`kick`,`invitacion`,`ping`,`userinfo`\n`welcomer`,`welcomer_del`",
                inline=False)
            embed.add_field(
                name="IMAGENES",
                value=
                "`nakiri`,`abrazo`,`mimos`,`sonrojar`,`malo`,`confuso`,`bailar`\n`nose`,`insulto`,`beso`",
                inline=False)
            embed.add_field(name="NAKIRI",
                            value="`status`,`soporte`,`info`,`help`,`news`",
                            inline=False)
            embed.add_field(
                name="Ejemplos",
                value=
                "`!help <comando>` **para mas informacion del comando**\n`!help <categoría>` **para mas informacion de una categoría**\n `!help <comando> [Argumento Opcional]`\n`!help <comando> <Argumento Necesario>`",
                inline=False)
            embed.add_field(
                name="Links Utiles",
                value=
                "[Página Web](https://nakiri.x10.mx/) , [Invítame](https://nakiri.x10.mx/invite) , [Plantilla del Servidor](https://nakiri.x10.mx/template)\n\n*Mas comandos serán añadidos mas adelante\nAlgunos de los comandos solo se pueden ejecutar en servidores\n y otros solo en mensajes privados`!help dm` para verlos*",
                inline=False)
            await ctx.send(embed=embed)

        #UTILIDADES
        elif 'avatar' == arg1:
            await ctx.channel.send(
                " **Uso**: `!avatar [@user]`\nNakiri enviara el avatar del usuario mencionado, si no, de quien ejecuta el comando"
            )
        elif 'moneda' == arg1:
            await ctx.channel.send(
                " **Uso**: `!moneda`\nNakiri lanzara una moneda de Cara o Cruz y dirá el resultado"
            )
        elif 'afk' == arg1:
            await ctx.channel.send(
                " **Uso**: `!afk`\nNakiri avisará de que estas AFK")
        elif 'num' == arg1:
            await ctx.channel.send(
                " **Uso**: `!num [num1] [num2]`\nNakiri selecionara un numero aleatorio entre el <num1> <num2> excepto que no se le indique ninguno sera entre el 1 y el 10"
            )
        elif 'mensaje' == arg1:
            await ctx.channel.send(
                " **Uso**: `!mensaje <@Usuario> [mensaje]`\nNakiri enviará el mensaje, si no se especifica ninguno, se enviará uno  de bienvenida por privado al usuario mecionado (Se le hará saber quien lo ha enviado)"
            )
        elif 'yt' == arg1:
            await ctx.channel.send(
                " **Uso**: `!yt <video>`\nNakiri buscará el mejor video en relación a tu busqueda"
            )
        elif 'f' == arg1:
            await ctx.channel.send(
                " **Uso**: `!f `\nNakiri enviara un mensaje de respeto por tu parte"
            )
        elif 'novia' == arg1:
            await ctx.channel.send(" **Uso**: `!novia`\nNovia")

        #GUILD
        elif 'clear' == arg1:
            await ctx.channel.send(
                " **Uso**: `!clear <argumento> `\nNakiri **ELIMINARÁ** los mensajes, con 2 posibles argumentos \n`!clear all` Que **ELIMINARÁ** todos los mensajes del chat \n`!clear <NUM>` Que **ELIMINARÁ** la cantidad de mensajes indicados"
            )
        elif 'kick' == arg1:
            await ctx.channel.send(
                " **Uso**: `!kick <@usuario> `\nNakiri explusara al usuario mencionado si posees los permisos necesarios"
            )
        elif 'ban' == arg1:
            await ctx.channel.send(
                " **Uso**: `!ban <@usuario> `\nNakiri baneara al usuario mencionado si posees los permisos necesarios"
            )
        elif 'ping' == arg1:
            await ctx.channel.send(
                " **Uso**: `!ping`\nNakiri dirá el tiempo de reación ")
        elif 'invitacion' == arg1:
            await ctx.channel.send(
                " **Uso**: `!invitacion`\nNakiri creara una invitación instantánea"
            )
        elif 'userinfo' == arg1:
            await ctx.channel.send(
                " **Uso**: `!userinfo [@usuario]`\nNakiri mostrará información sobre tu usuario, si no se menciona ninguno, sera del propio"
            )
        elif 'welcomer' == arg1:
            await ctx.channel.send(
                " **Uso**: `!welcomer <canal-de-texto> `\nNakiri enviara por el canal de texto seleccionado una imagen de bienvenida para nuevos miembros"
            )
        elif 'welcomer_del' == arg1:
            await ctx.channel.send(
                " **Uso**: `!welcomer_del `\nNakiri eliminara tu servidor de su lista de bienvenidas"
            )

        #IMAGENES
        elif 'abrazo' == arg1:
            await ctx.channel.send(
                " **Uso**: `!abrazo [@usuario]`\nNakiri enviará un abrazo, en caso de que se mencione alguien, tu abrazaras a quien menciones"
            )
        elif 'mimos' == arg1:
            await ctx.channel.send(
                " **Uso**: `!mimos [@usuario]`\nTe mimarán, en caso de que se mencione alguien, tu mimarás a quien menciones"
            )
        elif 'sonrojar' == arg1:
            await ctx.channel.send(
                " **Uso**: `!sonrojar [@usuario]`\nTe sonrojaras, en caso de que se mencione alguien, tu sonrojaras a quien menciones"
            )
        elif 'malo' == arg1:
            await ctx.channel.send(
                " **Uso**: `!malo [@usuario]`\nNakiri te castigara, en caso de que se mencione alguien, tu castigaras a quien menciones"
            )
        elif 'confundido' == arg1:
            await ctx.channel.send(
                " **Uso**: `!confundido [@usuario]`\nTe confundiras, en caso de que se mencione alguien, tu confundiras a quien menciones"
            )
        elif 'bailar' == arg1:
            await ctx.channel.send(
                " **Uso**: `!bailar [@usuario]`\nBailarás, en caso de que se mencione alguien, bailarás con quien menciones"
            )
        elif 'nose' == arg1:
            await ctx.channel.send(
                " **Uso**: `!nose [@usuario]`\nTe encogerás de hombos, en caso de que se mencione alguien, te encogeras de hombos con quien menciones"
            )
        elif 'insulto' == arg1:
            await ctx.channel.send(
                " **Uso**: `!nose [@usuario]`\nTe insultarás, en caso de que se mencione alguien, insultarás a quien menciones"
            )
        elif 'beso' == arg1:
            await ctx.channel.send(
                " **Uso**: `!nose [@usuario]`\nTe besarás, en caso de que se mencione alguien, besarás a quien menciones"
            )

        #NAKIRI
        elif 'info' == arg1:
            await ctx.channel.send(
                " **Uso**: `!info`\nNakiri enviara un mensaje de bienvenida")
        elif 'soporte' == arg1:
            await ctx.channel.send(
                " **Uso**: `!soporte`\nNakiri enviara las opciones de contacto con el creador"
            )
        elif 'status' == arg1:
            await ctx.channel.send(
                " **Uso**: `!status `\nNakiri enviara un mensaje con estadisticas generales del Bot"
            )
        elif 'clero' == arg1:
            await ctx.channel.send(
                " **Uso**: `!clero`\nEnvía un MD a Nakiri con el comando !clero"
            )
        elif 'news' == arg1:
            await ctx.channel.send(
                " **Uso**: `!news`\nEnvía las novedades de Nakiri")

        #CATEGORIAS
        elif 'utilidades' == arg1:
            await ctx.channel.send(
                '```bash\n"avatar" : Avatar del usuario\n"moneda" : Moneda de Cara o Cruz\n"afk" : Aviso AFK\n"num" : Número aleatorio\n"mensaje" : Mensaje a DM\n"yt" : Búsquedas en YouTube\n"f" : Respeto\n```'
            )
        elif 'guild' == arg1:
            await ctx.channel.send(
                '```bash\n"clear" : Limpiar canales de texto\n"ban" : Banear usuarios\n"kick" : Expulsar a usuarios\n"invitacion" : Invitación instantánea\n"ping" : Tiempo de respuesta Nakiri\n"userinfo" : Información de usuario\n"welcomer" : Canal de Bienvenida\n```'
            )
        elif 'imagenes' == arg1:
            await ctx.channel.send(
                '```bash\n"abrazo" : Monit@s Chinas abrazando a otras\n"malo" : Monit@s Chinas castigando a otras\n"sonrojar" : Monit@s Chinas sonrojandose\n"confuso" : Monit@s Chinas confundidas\n"bailar" : Monit@s Chinas bailando\n```'
            )
        elif 'nakiri' == arg1:
            await ctx.channel.send(
                '```bash\n"status" : Información del bot\n"soporte" : Opciones de ayuda\n"info" : Informacion de Nakiri\n"help" : Comando de ayuda\n```'
            )
        #GUILD/DM
        elif 'dm' == arg1:
            await ctx.channel.send(
                '```bash\n"Solo DM" : clero\n"Solo Servidor" : welcomer,welcomer_del,clear,kick,ban,invitacion,userinfo,status,f,yt,mensaje,afk,play,stop,skip\npausa,continua,ahora,volumen,lista,mezcla,join,leave,invocar,quitar\n```'
            )

    #COMANDO INFO
    @commands.command()
    @commands.dm_only()
    async def clero(self, ctx):
        embed = discord.Embed(title="", color=0xF4EFF3)
        embed.add_field(
            name=
            "**Konakiri!** Por lo que veo quieres ser ascendido al Clero eh?\nBien, para hacerlo rellena este formulario y espera tu respuesta",
            value=
            "[Formulario](https://docs.google.com/forms/d/e/1FAIpQLScm44xEfBEVbL0VySV1OueraYr2INod0R5ABVNEqZE3sBupDA/viewform?usp=sf_link)",
            inline=False)
        await ctx.send(embed=embed)

    #NO SERVER
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, commands.PrivateMessageOnly):
            await ctx.send(
                "Este comando solo esta habilitado por mensajes privados.")


def setup(client):
    client.add_cog(nakiri(client))

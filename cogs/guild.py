import discord,json
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound

class guild(commands.Cog):
    def __init__(self, client):
        self.client = client
    #COMANDO CLEAR
    @commands.command()
    @commands.has_permissions(manage_messages = True)#Comprobar que quien lo ejecuta tiene permisos de admin si no no le deja
    @commands.guild_only()
    async def clear(self, ctx, amount):
        if amount == 'all':
            #Remove ten sextillion messages
            await ctx.channel.purge(limit=10000000000000000000000)
        else:
            amount=int(amount)+1
            await ctx.channel.purge(limit=amount)

    #COMANDO KICK
    @commands.command()
    @commands.guild_only()
    @has_permissions(kick_members=True)#Esto comprueba que tengas los permisos necesario para expulsar a alguien
    async def kick(self, ctx, member: discord.Member, *, reason='Ha Nakiri le ha parecido lo correcto'):
        await member.kick(reason=reason)
        await ctx.send(f'Usuario {member} Expulsado')
    
    #COMANDO BAN
    @commands.command()
    @commands.guild_only()
    @has_permissions(ban_members = True)
    async def ban(self,ctx, member: discord.Member, *, reason='Ha Nakiri le ha parecido lo correcto'):
        await member.ban(reason=reason)
        await ctx.send(f'Usuario {member} ha sido baneado')
    @commands.command()
    async def say(self, ctx, *message):
        await ctx.message.delete()
        message_content_to_post = ctx.message.content.replace("!say ","")
        await ctx.send(message_content_to_post)
        
    #COMANDO PING
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")
            
    #COMANDO INVITACION
    @commands.command()
    @commands.guild_only()
    async def invitacion(self, ctx):
        link = await ctx.channel.create_invite(max_age = 300)
        await ctx.channel.send("Aquí está la invición: " + str(link)) 
        
    #COMANDO USERINFO
    @commands.command()
    @commands.guild_only()
    async def userinfo(self,ctx, *, user: discord.Member = None):
        if isinstance(ctx.channel, discord.DMChannel):#Si esta en DM no responder
           return
        if user is None:#Si no se Menciona, quien ejecuta el comando es user
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"#Formato de fechas
        embed = discord.Embed(color=0xF4EFF3, description=user.mention)#Mencionarlo en la Descripcion y poner el color
        embed.set_author(name=str(user), icon_url=user.avatar_url)#Poner el avatar del Usuario
        embed.set_thumbnail(url=user.avatar_url)#Poner el avatar del Usuario en grande
        embed.add_field(name="Unido", value=user.joined_at.strftime(date_format))#Sacar cuando se unio
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)#Sacar lo que se va a usar en el tema de la cuenta
        embed.add_field(name="Posicion de Servidor", value=str(members.index(user)+1))#Sacar en que numero del servidor esta
        embed.add_field(name="Registrado", value=user.created_at.strftime(date_format))#Sacar cuando se creo la cuenta de discord
        if len(user.roles) > 1:#Los roles el usuario
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])#Los permisos de administracion
        embed.add_field(name="Permisos de Administracion", value=perm_string, inline=False)
        embed.set_footer(text='ID: ' + str(user.id))#ID en el footer
        return await ctx.send(embed=embed)#Enviar el embed

    #CLERO OK
    @commands.command()
    @commands.guild_only()
    async def clerok(self,ctx, *, user: discord.Member = None):
        await ctx.message.delete()
        if isinstance(ctx.channel, discord.DMChannel):#Si esta en DM no responder
           return
        embed = discord.Embed(title="Felicidades por ascender al Clero, estos son tus permisos y roles actuales\n\n\n\n",color=0xFFA500, description=user.mention)#Mencionarlo en la Descripcion y poner el color
        embed.set_thumbnail(url=user.avatar_url)#Poner el avatar del Usuario en grande
        if len(user.roles) > 1:#Los roles el usuario
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])#Los permisos de administracion
        embed.add_field(name="Permisos de Administracion", value=perm_string, inline=False)
        return await ctx.send(embed=embed)#Enviar el embed
        
        
    #ERRORS
    #KICK
    @kick.error
    async def kick_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes permisos para expulsar a gente!")
        else:
            raise error
    @kick.error
    async def kick_error_args(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Se necesitan argumentos para ejecutar este comando, ejecute `!help <comando>` para verlo")
        elif isinstance(error, CommandNotFound):
            return
        raise error
    
    #BAN
    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes permisos para banear a gente!")
        else:
            raise error
    @ban.error
    async def ban_error_args(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Se necesitan argumentos para ejecutar este comando, ejecute `!help <comando>` para verlo")
        elif isinstance(error, CommandNotFound):
            return
        raise error
    #CLEAR
    @clear.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            channel = ctx.channel
            await ctx.send(f"No tienes permisos para vaciar el canal {channel}")
        else:
            raise error
    @clear.error
    async def clear_error_args(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Se necesitan argumentos para ejecutar este comando, ejecute `!help <comando>` para verlo")
        elif isinstance(error, CommandNotFound):
            return
        raise error
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(813463522474197053)
        await member.add_roles(role)
def setup(client):
	client.add_cog(guild(client))
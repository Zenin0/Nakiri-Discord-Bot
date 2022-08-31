import discord, random, glob, json, datetime
from discord.ext.commands import has_permissions, MissingPermissions, CommandNotFound
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand
from discord.ext.commands import cooldown, BucketType
import asyncio
from discord_components import ComponentsBot
from discord.utils import get

#NEEDS
bot = ComponentsBot("!", help_command=None)
slash = SlashCommand(bot, sync_commands=True)
counter = 0
embed_color = 0xF4EFF3


#This is for making it a cog
class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #COMMAND SLASH Kick
    @cog_ext.cog_slash(name='Kick', description='Kick Member')
    @commands.has_any_role(889284330902417428)
    #Is better to define the arguments as how they should be instead of being str or int
    async def kick(self,
                   ctx,
                   member: discord.Member,
                   *,
                   reason='Ha nasgar le ha parecido lo correcto'):
        #Kick command itself
        await member.kick(reason=reason)
        #This is a simple message
        await ctx.send(f'Usuario {member} Kicked', hidden=True)

    #COMANDO SLASH ban
    #Works the same way as kick but for ban
    @cog_ext.cog_slash(name='Ban', description='Ban member')
    @commands.has_any_role(889284330902417428)
    async def ban(self,
                  ctx,
                  member: discord.Member,
                  *,
                  reason='Ha nasgar le ha parecido lo correcto'):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} Baned', hidden=True)

    #COMMAND SLASH setdelay
    @cog_ext.cog_slash(name='Setdelay',
                       description='Set slowmodde of X seconds')
    @commands.has_any_role(965943947971162142)
    async def setdelay(self, ctx, seconds: int):
        #Sets the delay from seconds arg
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Applied delay of  {seconds} seconds!", hidden=True)

    #COMMAND Purge
    @cog_ext.cog_slash(name='Purge',
                       description='Purge a channel, leave empty to pruge all')
    @commands.has_any_role(965943947971162142)
    async def clear(self, ctx, amount=10000000000000000000000):
        await ctx.send('Channel Purged!', hidden=True)
        await ctx.channel.purge(limit=amount)

    #COMMAND banlist
    @cog_ext.cog_slash(name='banlist', description='List all baned users')
    @commands.has_any_role(965943947971162142)
    async def banlogs(self, ctx):
        guild = ctx.guild
        bans = await guild.bans()
        embed = discord.Embed(title="Ban Logs", colour=discord.Color.red())
        for ban in bans:
            embed.add_field(name=f"Name: ", value=f"{ban.user}")
            embed.add_field(name="Is_bot?", value=f"{ban.user.bot}")
            embed.add_field(name="Reason: ", value=f"{ban.reason}")
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name='Avatar', description='Avatar del usuario')
    async def avatar_slash(self, ctx, miembro: discord.Member = None):
        if miembro is None:
            miembro = ctx.author
        embed = discord.Embed(title="Avatar de " + str(miembro),
                              color=0xF4EFF3)
        embed.set_image(url=miembro.avatar_url)
        await ctx.send(embed=embed)

    #COMANDO MONEDA
    @cog_ext.cog_slash(name='Moneda', description='Tira una moneda al aire')
    async def moneda_slash(self, ctx):
        n = random.randint(0, 1)
        if n == 1:
            await ctx.send("Moneda tirada, tenemos... **Cara**!")
        else:
            await ctx.send("Moneda tirada, tenemos... **Cruz**!")

    #COMANDO NUM
    @cog_ext.cog_slash(name='Number', description='Select a random number')
    async def num_slash(self, ctx, fir=1, sec=10):
        n = random.randint(int(fir), int(sec))
        await ctx.send(n)
    #COMANDO USERINFO
    @cog_ext.cog_slash(name='Userinfo', description='Show info of the user')
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
        
    #COMMAND change nickname
    @cog_ext.cog_slash(name='Nickother', description='Change nickname of user')
    @commands.has_any_role(965943947971162142)
    async def chnick(self, ctx, member: discord.Member, nick):
        roles_en = ctx.guild.get_role(role_en)
        roles_es = ctx.guild.get_role(role_es)
        staff_roles_en = ctx.guild.get_role(id_staff_role_en)
        staff_roles_es = ctx.guild.get_role(id_staff_role_es)
        if (ctx.author == member):
            if roles_en in ctx.author.roles:
                await ctx.send('You can\'t change your nickname', hidden=True)
            elif roles_es in ctx.author.roles:
                await ctx.send('No puedes cambiar tu apodo', hidden=True)
        else:
            await member.edit(nick=nick)
            if roles_en in ctx.author.roles:
                await member.send(
                    f'Your nickname was change by {ctx} to {nick}')
                if staff_roles_en in ctx.author.roles:
                    await ctx.send(
                        f'Nickname was changed for {member.mention}',
                        hidden=True)
            if roles_es in ctx.author.roles:
                await member.send(
                    f'Tu apodo ha sido cambiado por {ctx} a {nick}')
                if staff_roles_es in ctx.author.roles:
                    await ctx.send(
                        f'Apodo cambiado correctamente a {member.mention}',
                        hidden=True)

    #DELETED MESSAGES
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.bot:
            return
        elif message.author.bot == True:
            return
        edit_embed = discord.Embed(
            title=f"Message Deleted",
            description=
            f'**User:** <@{message.author.id}>\n**Channel:** <#{message.channel.id}>\n**Message:** \n{message.content}',
            color=embed_color)
        edit_embed.set_footer(text=f"Message ID: {message.id}\n")
        edit_embed.set_author(name=f"{message.author}",
                              icon_url=f"{message.author.avatar_url}")
        archive_edit = self.bot.get_channel(897621372933652581)
        await archive_edit.send(embed=edit_embed)

    #EDITED MESSAGES
    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        if message_before.author == self.bot:
            return
        elif message_before.author.bot == True:
            return
        elif message_before.content == message_after.content:
            return
        edit_embed = discord.Embed(
            title=f"Message Edited",
            description=
            f'**User:** <@{message_before.author.id}>\n**Channel:** <#{message_before.channel.id}>\n**Message (Before Edit):** \n{message_before.content}\n**Message (After Edit):** \n{message_after.content}\n\n[Message]({message_after.jump_url})',
            color=embed_color)
        edit_embed.set_footer(text=f"Message ID: {message_before.id}\n")
        edit_embed.set_author(name=f"{message_before.author}",
                              icon_url=f"{message_before.author.avatar_url}")
        archive_edit = self.bot.get_channel(897621372933652581)
        try:
            edit_embed.set_image(url=message_after.attachments[0].proxy_url)
        except IndexError:
            pass
        await archive_edit.send(embed=edit_embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(not_verified)
        await member.add_roles(role)


def setup(bot):
    bot.add_cog(Mods(bot))

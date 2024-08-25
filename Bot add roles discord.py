import random
import discord
from discord.ext import commands

config = {
    'token': 'MTI3NjE1ODg3OTk0NzgxNjk3MA.GqVFWS.DemFprpAYtsfaEpUeG4aWH_Q0i0CKe_k34aPis',
    'prefix': '$',
}

bot = commands.Bot(config['prefix'], intents=discord.Intents.all())

# @bot.event

# async def on_member_join(member):



@bot.command()
async def bot_roles_list(ctx):
    roles = ctx.guild.get_member(bot.user.id)
    rolesTring = ''
    author = ctx.message.author
    for role in roles.roles:
        rolesTring += str(role) + ', '
    await ctx.reply(f'Привет {author.mention}, мои роли {rolesTring}')

@bot.command()
async def appoint(ctx, user:discord.Member):
    defaultRole = ctx.guild.get_role(1273537192391868460)
    if (defaultRole in user.roles):
        await ctx.reply(f'Пользователь {user.mention} уже назначен на роль {defaultRole.mention}')
    else:
        await user.add_roles(defaultRole)
        await ctx.reply(f'Пользователь {user.mention} назначен на должность {defaultRole.mention}')

bot.run(config['token'])

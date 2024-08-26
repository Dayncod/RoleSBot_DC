import random
import discord
from discord.ext import commands

config = {
    'token': 'MTI3NjE1ODg3OTk0NzgxNjk3MA.G65gmK.Og2iQXC5MswW14wNqGVRfKM_lfpe1Qj0PxadjE',
    'prefix': '$',
}

bot = commands.Bot(config['prefix'], intents=discord.Intents.all())

@bot.event
async def on_member_join(member):
    chanal = bot.get_channel(1047202154445807707)
    defaultRole = member.guild.get_role(1273537192391868460)
    await chanal.reply(f'Добро пожаловать на сервер, {member.mention}, ты был назначен на роль {defaultRole.mention}')

# @bot.event
# async def on_message(ctx):
#     if(ctx.author != bot.user):
#         if(ctx.author.name == 'damond52'):
#             await ctx.reply(f'Выйди отсюда лох')
#         elif(ctx.author.name == 'dayncod'):
#             await ctx.reply(f'Привет красавчик)')
#         else:
#             await ctx.reply(ctx.content)


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

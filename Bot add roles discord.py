import random
import discord
from discord.ext import commands

config = {
    'token': 'MTI3NjE1ODg3OTk0NzgxNjk3MA.GqVFWS.DemFprpAYtsfaEpUeG4aWH_Q0i0CKe_k34aPis',
    'prefix': '$',
}

bot = commands.Bot(config['prefix'], intents=discord.Intents.all())

@bot.command()
# async def start(ctx):
#     roles = ctx.guild.get_member(bot.user.id)
#     rolesTring = ''
#     author = ctx.message.author
#     for role in roles.roles:
#         rolesTring += str(role) + ', '
#     await ctx.reply(f'Привет {author.mention}, мои роли {rolesTring}')

async def appoint(ctx):
    role = None
    await ctx.reply(f'Пользователь {ctx.message.author.mention} назначен на должность {role}')

bot.run(config['token'])

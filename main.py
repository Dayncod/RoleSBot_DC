import random
import discord
from discord.utils import get
from discord.ext import commands

config = {
    'token': 'MTI3NjE1ODg3OTk0NzgxNjk3MA.G65gmK.Og2iQXC5MswW14wNqGVRfKM_lfpe1Qj0PxadjE',
    'prefix': '$',
}

bot = commands.Bot(config['prefix'], intents=discord.Intents.all())

defaultRole = get(client.get_all_channels())

@bot.event
async def on_member_join(member):
    chanal = bot.get_channel(1047202154445807707)
    defaultRole = member.guild.get_role(1273537192391868460)
    await member.add_roles(defaultRole)
    await chanal.send(f'Добро пожаловать на сервер, {member.mention}, ты был назначен на роль {defaultRole.mention}')

@bot.command()
async def appoint(ctx, user:discord.Member, defaultRole):
    # defaultRole = ctx.guild.get_role(1273537192391868460)
    if (defaultRole in user.roles):
        await ctx.send(f'Пользователь {user.mention} уже назначен на роль {defaultRole.mention}')
    else:
        await user.add_roles(defaultRole)
        await ctx.send(f'Пользователь {user.mention} назначен на должность {defaultRole.mention}')

bot.run(config['token'])

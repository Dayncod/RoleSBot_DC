import random
import discord
from discord.ext import commands

config = {
    'token': 'MTI3NjE1ODg3OTk0NzgxNjk3MA.GqVFWS.DemFprpAYtsfaEpUeG4aWH_Q0i0CKe_k34aPis',
    'prefix': '$',
}

bot = commands.Bot(config['prefix'], intents=discord.Intents.all())

@bot.command()
async def rand(ctx, *arg):
    await ctx.reply(random.randint(0, 100))

bot.run(config['token'])

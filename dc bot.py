import discord
from discord.ext import commands
import dc_bot_plugin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def luffy(ctx):
    if ctx.message.attachments:
        for onepiece in ctx.message.attachments:
            await onepiece.save(f'./kaydedilenler/{onepiece.filename}')
            await ctx.send("Mesaj gönderildi patron")
            roblox,minecraft=dc_bot_plugin.yuuji(f'./kaydedilenler/{onepiece.filename}')
            await ctx.send(f"bu bir{roblox}tur...{minecraft} oranında eminim")
    else:
        await ctx.send("Herhangi bir resim göndermedin")
bot.run("YOUR TOKEN HERE")
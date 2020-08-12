from discord.ext import commands
import os
import traceback
import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
bosstime_list = list()
jst_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
dt_now = jst_now.strftime('%Y年%m月%d日 %H:%M:%S')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong-now')

@bot.command()
async def now(ctx):
    await ctx.send(dt_now)

bot.run(token)

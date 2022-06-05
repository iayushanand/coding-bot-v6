from __future__ import annotations

import os
import warnings

from discord.ext import commands

from ext.models import CodingBot

if not os.path.exists("./database"):
    os.mkdir("./database")

bot = CodingBot()

warnings.filterwarnings(action='ignore', module='wikipedia')

@bot.before_invoke
async def before_invoke(ctx: commands.Context[CodingBot]):
    bot.processing_commands += 1


@bot.after_invoke
async def after_invoke(ctx: commands.Context[CodingBot]):
    bot.processing_commands -= 1


TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)

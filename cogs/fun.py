import random

import discord
from discord.ext import commands

class Fun(commands.Cog, command_attrs=dict(hidden=False)):

    hidden = False
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="meme")
    async def meme(self, ctx: commands.Context):
        response = await self.bot.session.get("https://meme-api.herokuapp.com/gimme")
        meme_json = await response.json()

        meme_url = meme_json['url']
        meme_name = meme_json['title']
        meme_poster = meme_json['author']
        meme_sub = meme_json['subreddit']

        embed = discord.Embed(title = meme_name, description=f"Meme by {meme_poster} from subreddit {meme_sub}")
        embed.set_image(url=meme_url)

        await ctx.send(embed=embed)

    @commands.hybrid_command(name="8ball")
    async def eightball(self, ctx: commands.Context, question: str):
        # LONGEST LIST OF RESPONSES, FEEL FREE TO ADD/REMOVE OR OPTIMISE
        responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                    "Do not count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
                    "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
                    "Yes.", "Yes, definitely.", "You may rely on it."]
        response = random.choice(responses)
        
        embed = discord.Embed(title="8ball is answering", description=f"{question}\nAnswer : {response}")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url) # Support for nitro users
        await ctx.send(embed=embed)

    # NEXT : Lyrics command
    # DO YOUR COMMANDS HERE I HAVE NOT ENOUGH CREATIVITY TO THINK ABOUT THEM KEKW

async def setup(bot):
    await bot.add_cog(Fun(bot))
    
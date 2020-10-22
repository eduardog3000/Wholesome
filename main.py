import discord
from discord.ext import commands

from config import config

bot = commands.Bot(command_prefix=config.prefix)

# noinspection PyShadowingNames
@bot.command(aliases=['colour'])
async def color(ctx: commands.Context, color: str):
    # This is mainly for hints in the IDE, might remove
    assert ctx.guild is not None
    assert ctx.author is not None
    guild: discord.Guild = ctx.guild
    author: discord.Member = ctx.author

    roles = [role for role in guild.roles if role.id in config.colors]
    chosen = next(role for role in roles if role.name.lower() == color.lower())

    if chosen is None:
        raise commands.CommandError('Color not available.')

    await author.remove_roles(*roles, reason='User requested color change.')
    await author.add_roles(chosen, reason='User requested color change.')

    await ctx.send('Color changed!')

bot.run(config.token)

from .triviatest import triviatest


async def setup(bot):
    await bot.add_cog(triviatest(bot))
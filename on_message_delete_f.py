import discord

async def main(self, message):
    if not message.author.bot :
        embed = discord.Embed(title=f'{message.author.name} was deleted', color=0x51F5EA, description= message.content)
        await self.log_channel.send(embed=embed)

import discord

async def main(self, message):
    if message.author.bot :
        return

    embed = discord.Embed(title=f'message from {message.author.display_name} was deleted', color=0x51F5EA, description= message.content)
    await self.log_channel.send(embed=embed)

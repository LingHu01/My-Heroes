import discord

def main(self, message):
    embed = discord.Embed(title=f'{message.author.name} deleted', color=0x51F5EA)
    await self.log_channel.send(embed=embed)
